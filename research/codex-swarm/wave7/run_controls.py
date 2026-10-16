"""Final bounded, direct-file Wave7 replay of reviewed artificial controls.

This does not discover or evaluate source coefficients/fibers. Exact frozen
producer/test/review bytes must be supplied by the final handoff manifests.
Use --plan for a read-only inventory while producers/reviews are still active.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import subprocess
import sys
import time

HERE=Path(__file__).resolve().parent
BASE=HERE.parent
ROOT=HERE.parents[2]
LANES=('exact-curve-field','source-boundary-analysis','detector-realization','detector-admission','wave7')

def need(ok,message):
    if not ok:raise ValueError(message)
def sha(raw):return hashlib.sha256(raw).hexdigest()
def digest(path):return sha(path.read_bytes())
def local_name(name):
    need(type(name)is str and Path(name).name==name and name not in('','.', '..'),'local filename required')
    return name
def repository_path(name):
    need(type(name)is str and bool(name),'repository-relative path required')
    path=Path(name)
    need(not path.is_absolute()and not any(x in('','..','.')for x in path.parts)
        and path.as_posix()==name,'canonical safe repository-relative path required')
    target=ROOT/path
    need(target.resolve().is_relative_to(ROOT.resolve()),'repository path escapes root')
    return target
def verify_dependency_snapshot(snapshot,declared):
    need(type(snapshot)is dict and snapshot==declared,'exact declared dependency union required')
    result={}
    for name,want in snapshot.items():
        need(type(want)is str and re.fullmatch('[0-9a-f]{64}',want)is not None,'SHA256 dependency pin required')
        value=digest(repository_path(name));need(value==want,'transitive dependency drift: '+name)
        result[name]=value
    return result
def dependency_inputs(bindings):
    declared={}
    for lane,collection in(('detector-realization','local_dependencies'),('detector-admission','workspace_inputs')):
        pins=json.loads(repository_path('research/codex-swarm/'+lane+'/source-pins.json').read_bytes())
        for row in pins[collection]:
            name='research/codex-swarm/'+row['path'];repository_path(name)
            need(name not in declared or declared[name]==row['sha256'],'conflicting source dependency pins')
            declared[name]=row['sha256']
    result=verify_dependency_snapshot(bindings['dependency_snapshot'],declared)
    source=json.loads(repository_path('research/codex-swarm/detector-realization/source-pins.json').read_bytes())
    wanted=sorted(source['git_objects'],key=lambda r:(r['commit'],r['path']))
    rows=bindings['immutable_input_pins']
    need(type(rows)is list and sorted(rows,key=lambda r:(r['commit'],r['path']))==wanted
        and len(rows)==3,'exact three SR immutable input records required')
    git_inputs={}
    for row in rows:
        need(re.fullmatch('[0-9a-f]{40}',row['commit'])is not None,'full immutable commit required')
        repository_path(row['path']);ref=row['commit']+':'+row['path']
        raw=subprocess.check_output(['git','show',ref],cwd=ROOT,timeout=10)
        need(sha(raw)==row['sha256'],'immutable source input drift: '+ref)
        git_inputs[ref]=sha(raw)
    return result,git_inputs
def limits():
    resource.setrlimit(resource.RLIMIT_AS,(768*1024**2,768*1024**2))
    resource.setrlimit(resource.RLIMIT_CPU,(59,59))

def test_snapshot(lane):
    p=BASE/lane
    return {f.name:digest(f)for f in sorted(p.glob('test*.py'))}

def producer_snapshot(lane):
    if lane=='wave7':return {}
    p=BASE/lane;raw=(p/'producer-ready.json').read_bytes();marker=json.loads(raw)
    files=marker.get('files_sha256',marker.get('files'))
    need(type(files)is dict and files,'recognized nonempty producer manifest: '+lane)
    for name,want in files.items():
        local_name(name);need(type(want)is str and digest(p/name)==want,'producer drift: '+lane+'/'+name)
    return {'producer-ready.json':sha(raw),**files}

def plan():
    out=[]
    for lane in LANES:
        p=BASE/lane;row={'lane':lane,'test_files':test_snapshot(lane),'producer_marker_present':(p/'producer-ready.json').is_file()}
        if row['producer_marker_present']:row['producer_marker_sha256']=digest(p/'producer-ready.json')
        out.append(row)
    return {'schema':'wave7-read-only-replay-plan-v1','final_inputs_frozen':False,'lanes':out,
        'physical_source_evaluated':False,'actual_fibers_enumerated':False,'execution_release':False}

def authenticate(bindings,reviews):
    need(bindings['schema']=='wave7-program-bindings-v1'and bindings['state']=='frozen-for-final-replay','final program bindings not frozen')
    need(bindings['runner_sha256']==digest(HERE/'run_controls.py'),'runner drift')
    need(reviews['schema']=='wave7-external-reviews-v1'and reviews['state']=='frozen-for-final-replay','final review inputs not frozen')
    need(bindings['external_reviews_sha256']==digest(HERE/'external-reviews.json'),'review manifest drift')
    lane_rows=bindings['lanes'];need(type(lane_rows)is list and [r['lane']for r in lane_rows]==list(LANES),'exact final lane order')
    result={'producers':{},'tests':{},'review_files':{},'immutable_review_pins':{},'integration_inputs':{}}
    for row in lane_rows:
        lane=row['lane'];current=producer_snapshot(lane)
        need(current==row['producer_snapshot'],'producer snapshot drift: '+lane)
        tests=test_snapshot(lane);need(tests==row['test_files'],'final test set/byte drift: '+lane)
        counts=row['expected_tests_per_file'];need(set(counts)==set(tests),'final per-file test count coverage: '+lane)
        need(all(type(n)is int and n>0 for n in counts.values()),'positive exact per-file test counts')
        result['producers'][lane]=current;result['tests'][lane]=tests
        for ext in row.get('external_tests',[]):
            local_name(ext['name']);need(type(ext['expected_tests'])is int and ext['expected_tests']>0,'positive public regression count')
            matches=[pin for pin in reviews.get('immutable_external_review_pins',[])if all(pin.get(k)==ext.get(k)for k in('commit','path','sha256'))]
            need(len(matches)==1,'executed public regression must have exactly one immutable review pin')
    for row in reviews['local_review_files']:
        path=Path(row['path']);need(not path.is_absolute()and '..'not in path.parts,'repository review path')
        value=digest(ROOT/path);need(value==row['sha256'],'local independent review drift: '+str(path))
        result['review_files'][str(path)]=value
    for row in reviews.get('immutable_external_review_pins',[]):
        ref=row['commit']+':'+row['path'];raw=subprocess.check_output(['git','show',ref],cwd=ROOT,timeout=10)
        need(sha(raw)==row['sha256'],'external review bytes drift: '+ref)
        if 'git_blob'in row:need(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==row['git_blob'],'external review blob drift')
        if 'bytes'in row:need(len(raw)==row['bytes'],'external review byte count drift')
        result['immutable_review_pins'][ref]=sha(raw)
    for name,want in bindings.get('integration_inputs',{}).items():
        local_name(name);value=digest(HERE/name);need(value==want,'integration input drift: '+name)
        result['integration_inputs'][name]=value
    dependencies,git_inputs=dependency_inputs(bindings)
    result['dependency_snapshot']=dependencies;result['immutable_input_pins']=git_inputs
    return result

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--plan',action='store_true');ap.add_argument('--output');args=ap.parse_args()
    if args.output:local_name(args.output)
    if args.plan:
        need(args.output is None,'--plan is read-only and does not write receipts')
        print(json.dumps(plan(),indent=2,sort_keys=True));return 0
    bindings_raw=(HERE/'program-bindings.json').read_bytes();reviews_raw=(HERE/'external-reviews.json').read_bytes()
    bindings=json.loads(bindings_raw);reviews=json.loads(reviews_raw)
    before=authenticate(bindings,reviews)
    out={'schema':'bounded-wave7-replay-v1','limits_per_subprocess':{'address_space_MiB':768,'CPU_seconds':59,'wall_seconds':60},
        'program_bindings_sha256':sha(bindings_raw),'external_reviews_sha256':sha(reviews_raw),'authenticated_before':before,
        'physical_source_evaluated':False,'actual_fibers_enumerated':False,'execution_release':False,'runs':[],
        'final_test_files_per_lane':{r['lane']:len(r['test_files'])for r in bindings['lanes']}}
    status=0
    try:
        for row in bindings['lanes']:
            lane=row['lane'];p=BASE/lane
            jobs=[(name,want,None,row['expected_tests_per_file'][name])for name,want in sorted(row['test_files'].items())]
            jobs += [(ext['name'],ext['sha256'],ext,ext['expected_tests'])for ext in row.get('external_tests',[])]
            for name,want,external,expected in jobs:
                local_name(name)
                for optimized in(False,True):
                    command=[sys.executable,'-B']+(['-O']if optimized else[])
                    if external is None:
                        command += [name]+(['--child']if (lane in('exact-curve-field','source-boundary-analysis','detector-realization','detector-admission')and name=='test_independent.py')or(lane=='detector-admission'and name=='test_height_followup.py')else[])+['-v']
                    else:
                        ref=external['commit']+':'+external['path']
                        raw=subprocess.check_output(['git','show',ref],cwd=ROOT,timeout=10)
                        need(sha(raw)==want,'public regression drift before execution')
                        # Actual __main__ globals are necessary for unittest discovery.
                        command += ['-c',"import sys;sys.argv=["+repr(name)+"];exec(compile("+repr(raw)+","+repr(ref)+",'exec'))"]
                    start=time.monotonic()
                    try:
                        result=subprocess.run(command,cwd=p,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'},
                            capture_output=True,text=True,timeout=60,preexec_fn=limits)
                        elapsed=time.monotonic()-start;log=result.stdout+result.stderr;rc=result.returncode
                    except subprocess.TimeoutExpired as exc:
                        elapsed=time.monotonic()-start
                        def decoded(s):return s.decode(errors='replace')if isinstance(s,bytes)else s or''
                        log=decoded(exc.stdout)+decoded(exc.stderr)+'\nWALL TIMEOUT\n';rc=124
                    counts=[int(x)for x in re.findall(r'Ran (\d+) tests?',log)]
                    logname=lane+'-'+Path(name).stem+('-optimized.log'if optimized else'-normal.log')
                    (HERE/logname).write_text(log)
                    run={'lane':lane,'testfile':name,'testfile_sha256':want,'optimized':optimized,
                        'suite_test_counts':counts,'tests':sum(counts),'expected_tests':expected,'external_source':external,
                        'returncode':rc,'seconds':round(elapsed,3),'log':logname,'log_sha256':digest(HERE/logname),
                        'captured_output_sha256':sha(log.encode())}
                    out['runs'].append(run)
                    need(elapsed<60,'post-return wall deadline exceeded')
                    need(rc==0,'test subprocess failed: '+lane+'/'+name)
                    need(counts and sum(counts)==run['expected_tests'],'final suite count mismatch: '+lane+'/'+name)
                    if external is None:need(digest(p/name)==want,'test mutated during run: '+lane+'/'+name)
        need((HERE/'program-bindings.json').read_bytes()==bindings_raw,'program bindings mutated')
        need((HERE/'external-reviews.json').read_bytes()==reviews_raw,'review bindings mutated')
        after=authenticate(bindings,reviews);need(after==before,'final producer/test/review input mutation')
        out['authenticated_after']=after;out['status']='all frozen reviewed artificial controls pass'
    except Exception as exc:
        out['status']='FAILED';out['error']=str(exc);status=1
    out['total_tests_per_mode']={str(mode):sum(r['tests']for r in out['runs']if r['optimized']==mode)for mode in(False,True)}
    out['completed_testfile_runs']=len(out['runs'])
    if args.output:(HERE/args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True));return status

if __name__=='__main__':raise SystemExit(main())
