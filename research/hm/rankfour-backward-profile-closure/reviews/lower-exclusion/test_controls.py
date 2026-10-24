#!/usr/bin/env python3
from pathlib import Path
import json,subprocess,sys
R=Path(__file__).resolve().parent
mutations=['source-hash','physical-marking','omit-H1','source-dual-swap','omit-case','discard-earlier-defects','quotient-twist','derivative-twist','top-kernel-twist','weaken-top-slope','source-Z-only','maps-vs-sections']
base=(R/'RESULT.json').read_bytes()
for flags in([],['-O']):
 p=subprocess.run([sys.executable,*flags,str(R/'verify.py')],capture_output=True,cwd='/tmp')
 if p.returncode or p.stdout!=base:raise RuntimeError('normal/optimized independent result mismatch')
rows=[]
for name in mutations:
 p=subprocess.run([sys.executable,str(R/'verify.py'),name],capture_output=True,text=True,cwd='/tmp')
 if p.returncode==0:raise RuntimeError('mutation unexpectedly accepted: '+name)
 rows.append({'mutation':name,'rejected':True,'reason':p.stderr.strip().splitlines()[-1]})
print(json.dumps({'status':'PASS','normal_and_optimized_match':True,'rejected_mutations':rows},indent=2,sort_keys=True))
