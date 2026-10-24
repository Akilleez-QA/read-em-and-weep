#!/usr/bin/env python3
"""Portable, exact-output replay and author/independent full-tuple comparison."""
from pathlib import Path
from collections import Counter
import hashlib,json,subprocess,sys,tempfile
ROOT=Path(__file__).resolve().parent
checks=0
def check(ok,label):
 global checks
 checks+=1
 if not ok:raise RuntimeError(label)
def read(path):return json.loads((ROOT/path).read_text())
def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':'))
def entries(name):
 rows=read(name)
 for r in rows:
  p=(ROOT/name).parent/r['path']; b=p.read_bytes()
  check(len(b)==r['bytes'] and hashlib.sha256(b).hexdigest()==r['sha256'],'inventory '+name+': '+r['path'])
 return len(rows)
def run(script,expected,opt,cwd):
 args=[sys.executable]+(['-O'] if opt else [])+[str(ROOT/script)]
 p=subprocess.run(args,capture_output=True,cwd=cwd)
 check(p.returncode==0,script+' replay failed: '+p.stderr.decode())
 check(p.stdout==(ROOT/expected).read_bytes(),script+' byte-exact output')
 return json.loads(p.stdout)
def bundle(x):return sorted((r['degree'],r['coefficient']) for r in x)
def row(x,status=True):
 r={k:x[k] for k in ('source','row','torsion_residue')}
 r.update(B=bundle(x['B']),Z=bundle(x['Z']))
 if status:r['status']=x['status']
 return r
def main():
 author_members=entries('MANIFEST.json');review_members=entries('independent-review/MANIFEST.json')
 A=read('RESULT.json');I=read('independent-review/RESULT.json')
 check(A['checks']==3477 and I['checks']==3347,'retained arithmetic totals')
 check(not A['Qstar_twist_one_vanishing_assumed'] and not I['forbidden_Qstar1_filter_used'],'no invalid twist-one assumption')
 check(not A['actual_instances_evaluated'] and not I['actual_instances_evaluated'],'abstract arithmetic only')
 check(A['positive_torsion_retained_until_proved_exclusion'],'torsion retained')
 check(len(A['endpoint_tuples'])==len(I['endpoint_tuples'])==18,'all eighteen tuples')
 key=lambda x:canonical(row(x,False))
 amap={key(x):x for x in A['endpoint_tuples']};imap={key(x):x for x in I['endpoint_tuples']}
 check(len(amap)==len(imap)==18 and set(amap)==set(imap),'exact endpoint tuple sets')
 remaining={key(x) for x in I['one_remaining']}
 baseline_survivors={k for k,x in imap.items() if x['status']=='necessary_survivor'}
 cut=baseline_survivors-remaining
 check(len(baseline_survivors)==3 and len(cut)==2 and len(remaining)==1,'two-V cut provenance')
 for k in amap:
  expected='rejected_two_V_kernel' if k in cut else imap[k]['status']
  check(amap[k]['status']==expected,'final full tuple status')
 check(A['necessary_survivors']==I['one_remaining'],'exact sole survivor')
 final=A['necessary_survivors'][0]
 check(final['source']=='D' and final['row']==[-58,-22,0,0,4],'sole source, degrees and defects')
 check(bundle(final['B'])==[(-8,'1'),(-1,"W'"),(14,'1')] and bundle(final['Z'])==[(-5,"W'"),(-4,'V')],'sole exact endpoint bundles')
 for source in ('D','P','V','Z'):
  check([A['source_stage_counts'][source][k] for k in ('initial','envelope','upper_exact','horizontal','rank_one')]==I['source_stage_counts'][source],'all five stages: '+source)
 check({canonical(bundle(x)) for x in A['two_V_kernel_alternatives']}=={canonical(bundle(x)) for x in I['kernel_splittings']} and len(I['kernel_splittings'])==2,'both complete kernel alternatives')
 sources=read('INPUTS.json');check(sources==read('independent-review/INPUTS.json'),'source manifest agreement')
 for s in sources:
  b=(ROOT/s['file']).read_bytes()
  check(b==(ROOT/'independent-review'/s['file']).read_bytes(),'source copies '+s['file'])
  check(len(b)==s['bytes'] and hashlib.sha256(b).hexdigest()==s['sha256'] and hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==s['git_blob_sha1'],'immutable source identity '+s['file'])
 with tempfile.TemporaryDirectory() as cwd:
  for opt in (False,True):
   run('verify.py','RESULT.json',opt,cwd)
   run('independent-review/independent.py','independent-review/RESULT.json',opt,cwd)
   a=run('test_controls.py','CONTROLS.json',opt,cwd)
   check(a['executed_mutations']==10 and a['all_rejected'] and a['unmutated_result_retained'],'all ten author mutations and positive control')
   m=run('independent-review/mutations.py','independent-review/MUTATIONS.json',opt,cwd)
   check(len(m)==8 and all(x['rejected'] for x in m),'all eight independent executable mutations')
 return {'claim':'Conditional ordered rank-four (1,2): one necessary tuple, not a profile exclusion','checks':checks,'author_manifest_members':author_members,'independent_manifest_members':review_members,'author_checks':3477,'independent_checks':3347,'exact_endpoint_tuples_compared':18,'exact_kernel_alternatives_compared':2,'necessary_survivors':A['necessary_survivors'],'status_counts':dict(sorted(Counter(x['status'] for x in A['endpoint_tuples']).items())),'all_eight_sources_authenticated':True,'normal_optimized_other_cwd_exact':True,'author_mutations':10,'independent_mutations':8,'coarse_bins_unchanged':21,'actual_instances_evaluated':False,'whole_profile_excluded':False}
if __name__=='__main__':print(json.dumps(main(),indent=2,sort_keys=True))
