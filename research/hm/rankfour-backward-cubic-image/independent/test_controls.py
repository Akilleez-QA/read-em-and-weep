#!/usr/bin/env python3
from pathlib import Path
import json,subprocess,sys
R=Path(__file__).resolve().parent
mutations=['source-hash','physical-marking','omit-H1','source-dual-swap','global-zero-defects','maps-vs-sections','image-parity','saturation-cap','intertwiner-multiplicity','endpoint-derivative-twist','source-Z-only','omit-quartic','dimensions-only']
base=(R/'RESULT.json').read_bytes()
for flags in ([],['-O']):
 result=subprocess.run([sys.executable,*flags,str(R/'verify.py')],capture_output=True,cwd='/tmp')
 if result.returncode or result.stdout!=base:raise RuntimeError('normal/optimized result mismatch')
rows=[]
for name in mutations:
 p=subprocess.run([sys.executable,str(R/'verify.py'),name],capture_output=True,text=True,cwd='/tmp')
 if p.returncode==0:raise RuntimeError('mutation unexpectedly accepted: '+name)
 rows.append({'mutation':name,'rejected':True,'reason':p.stderr.strip().splitlines()[-1]})
print(json.dumps({'status':'PASS','baseline_normal_and_optimized_match':True,'rejected_mutations':rows},indent=2,sort_keys=True))
