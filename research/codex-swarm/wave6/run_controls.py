"""Bounded direct-file replay; historical snapshot checks stay explicit."""
import argparse,hashlib,json,os,pathlib,re,resource,subprocess,sys,time
HERE=pathlib.Path(__file__).resolve().parent
LANES=('full-source-application','full-lift-domain','total-gated-provider','wave6')


def limits():
    resource.setrlimit(resource.RLIMIT_AS,(768*1024**2,768*1024**2))
    resource.setrlimit(resource.RLIMIT_CPU,(59,59))


def snapshot(lane):
    p=HERE.parent/lane
    if lane=='wave6':return {f.name:hashlib.sha256(f.read_bytes()).hexdigest()for f in p.glob('test*.py')}
    raw=(p/'producer-ready.json').read_bytes();marker=json.loads(raw)
    hashes=marker.get('files_sha256',marker.get('files'))
    if type(hashes)is not dict:raise ValueError('unknown producer marker '+lane)
    for name,want in hashes.items():
        if pathlib.Path(name).name!=name:raise ValueError('nonlocal producer filename')
        if hashlib.sha256((p/name).read_bytes()).hexdigest()!=want:raise ValueError('producer drift '+lane+'/'+name)
    return {**hashes,'producer-ready.json':hashlib.sha256(raw).hexdigest()}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output');args=ap.parse_args()
    if args.output and pathlib.Path(args.output).name!=args.output:raise ValueError('receipt output must be a local filename')
    out={'schema':'bounded-wave6-replay-v1','limits_per_subprocess':{'address_space_MiB':768,'CPU_seconds':59,'wall_seconds':60},
         'physical_source_evaluated':False,'actual_fibers_enumerated':False,'execution_release':False,
         'lanes':[],'historical_snapshot_routes':[],'pending':[]}
    for lane in LANES:
        p=HERE.parent/lane;before=snapshot(lane)
        for testfile in sorted(p.glob('test*.py')):
            if lane=='total-gated-provider'and testfile.name=='test_independent.py':
                wrapper=p/'test_frame_followup.py'
                out['historical_snapshot_routes'].append({'lane':lane,'historical_file':testfile.name,
                    'historical_file_sha256':hashlib.sha256(testfile.read_bytes()).hexdigest(),
                    'reason':'Preserved independent test authenticates its original pre-frame producer marker. Direct stale replay would intentionally reject current producer bytes.',
                    'current_replay_route':'test_frame_followup.py transparently overrides only historical MARKER_SHA in memory and runs the historical cases plus independent frame controls.',
                    'wrapper_present':wrapper.is_file(),'exact_old_current_byte_identity_claimed':False})
                if not wrapper.is_file():out['pending'].append('TP frame follow-up wrapper not yet available')
                continue
            digest=hashlib.sha256(testfile.read_bytes()).hexdigest()
            for optimized in(False,True):
                cmd=[sys.executable,'-B']+(['-O']if optimized else[])+[testfile.name,'-v']
                t=time.monotonic()
                result=subprocess.run(cmd,cwd=p,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'},text=True,capture_output=True,timeout=60,preexec_fn=limits)
                log=result.stdout+result.stderr;counts=re.findall(r'Ran (\d+) tests?',log)
                logname=lane+'-'+testfile.stem+('-optimized.log'if optimized else'-normal.log')
                (HERE/logname).write_text(log)
                row={'lane':lane,'testfile':testfile.name,'testfile_sha256':digest,'optimized':optimized,
                     'tests':sum(map(int,counts))if counts else None,'suite_test_counts':[int(x)for x in counts],'returncode':result.returncode,
                     'seconds':round(time.monotonic()-t,3),'log':logname,'log_sha256':hashlib.sha256((HERE/logname).read_bytes()).hexdigest(),
                     'captured_output_sha256':hashlib.sha256(log.encode()).hexdigest()}
                out['lanes'].append(row)
                if result.returncode:
                    row['failure_output']=log[-16000:];print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(result.returncode)
                if hashlib.sha256(testfile.read_bytes()).hexdigest()!=digest:raise ValueError('test mutated during replay')
        if snapshot(lane)!=before:raise ValueError('producer mutation during replay '+lane)
    out['total_tests_per_mode']={str(mode):sum(r['tests']or 0 for r in out['lanes']if r['optimized']==mode)for mode in(False,True)}
    out['status']='pending follow-up'if out['pending']else'available controls pass'
    if args.output:(HERE/args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
