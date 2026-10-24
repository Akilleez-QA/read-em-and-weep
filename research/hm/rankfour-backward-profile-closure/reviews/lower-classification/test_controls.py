#!/usr/bin/env python3
from pathlib import Path
import json,subprocess,sys
from concurrent.futures import ThreadPoolExecutor
R=Path(__file__).resolve().parent
MUTATIONS=['source-hash','physical-marking','omit-H1','source-dual-swap','global-zero-defects','maps-vs-sections','source-Z-only','omit-second-backstep','full-annihilator-identification','dimensions-only','dual-target-twist','drop-target-multiplicity','ordinary-Ext-zero','low-branch-all-zero','omit-quartic','endpoint-derivative-twist','force-torsion-into-N','allow-even-torsion','inverse-image-twist']
base=(R/'RESULT.json').read_bytes()
for flags in ([],['-O']):
 p=subprocess.run([sys.executable,*flags,str(R/'verify.py')],capture_output=True,cwd='/tmp')
 if p.returncode or p.stdout!=base:raise RuntimeError('normal/optimized output mismatch')
def test(name):
 p=subprocess.run([sys.executable,str(R/'verify.py'),name],capture_output=True,text=True,cwd='/tmp')
 return {'mutation':name,'rejected':p.returncode!=0,'reason':p.stderr.strip().splitlines()[-1]if p.stderr.strip()else 'accepted'}
with ThreadPoolExecutor(max_workers=4)as pool:rows=list(pool.map(test,MUTATIONS))
if not all(x['rejected']for x in rows):raise RuntimeError('accepted mutations: '+', '.join(x['mutation']for x in rows if not x['rejected']))
print(json.dumps({'status':'PASS','normal_and_optimized_match':True,'rejected_mutations':rows},indent=2,sort_keys=True))
