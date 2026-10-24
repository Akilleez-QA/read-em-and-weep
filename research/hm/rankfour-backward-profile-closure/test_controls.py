#!/usr/bin/env python3
from pathlib import Path
import subprocess,json,sys,os
ROOT=Path(__file__).resolve().parent
mutations=['omit-rank-one','omit-rank-four','lower-image-full-annihilator','allow-zero-image','change-copy-between-branches','assume-canonical-copy','assume-evaluation-injective','swap-unequal-bundles','swap-physical-A-V','force-source-Z','global-zero-defects','circular-rankone-proof','claim-SF-five']
base=[sys.executable,str(ROOT/'verify.py'),'--contract-only'];env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'}
r=subprocess.run(base,capture_output=True,text=True,env=env)
if r.returncode:raise RuntimeError('unmutated integration contract failed: '+r.stderr)
rows=[]
for m in mutations:
 r=subprocess.run(base+['--mutation',m],capture_output=True,text=True,env=env)
 if r.returncode==0:raise RuntimeError('integration mutation accepted: '+m)
 rows.append({'mutation':m,'exit_code':r.returncode,'error':r.stderr.strip().splitlines()[-1]})
print(json.dumps({'status':'PASS','executed_mutation_rejections':len(rows),'baseline_passed':True,'controls':rows},indent=2,sort_keys=True))
