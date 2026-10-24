#!/usr/bin/env python3
from pathlib import Path
import json,subprocess,sys
R=Path(__file__).resolve().parent
mutations=['alter-theorem','physical-marking','source-dual-swap','circular-proof','omit-one','omit-four','wrong-rank-theorem','change-section-copy','allow-zero','canonical-copy','injective-evaluation','swap-bundles','global-zero','drop-premises','claim-sf5']
base=(R/'RESULT.json').read_bytes()
for flags in([],['-O']):
 p=subprocess.run([sys.executable,*flags,str(R/'verify.py')],capture_output=True,cwd='/tmp')
 if p.returncode or p.stdout!=base:raise RuntimeError('normal/optimized integration output mismatch')
rows=[]
for name in mutations:
 p=subprocess.run([sys.executable,str(R/'verify.py'),name],capture_output=True,text=True,cwd='/tmp')
 if p.returncode==0:raise RuntimeError('mutation unexpectedly accepted: '+name)
 rows.append({'mutation':name,'rejected':True,'reason':p.stderr.strip().splitlines()[-1]})
print(json.dumps({'status':'PASS','normal_and_optimized_match':True,'rejected_mutations':rows},indent=2,sort_keys=True))
