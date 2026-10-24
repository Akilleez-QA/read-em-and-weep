#!/usr/bin/env python3
"""Re-execute genuine proof mutations in isolated Python processes."""
from pathlib import Path
import subprocess, sys, json
ROOT=Path(__file__).resolve().parent
modes=['source-hash','physical-marking','omit-H1','defect-weight','endpoint-parity','K-twist','dual-twist','source-dual-swap','dimensions-only']
result={}
for mode in ['',*modes]:
 command=[sys.executable,str(ROOT/'verify.py')]+([mode]if mode else [])
 run=subprocess.run(command,capture_output=True,text=True)
 if mode:
  if run.returncode==0:raise RuntimeError('Mutation incorrectly passed: '+mode)
  result[mode]=run.stderr.strip().splitlines()[-1]
 else:
  if run.returncode!=0:raise RuntimeError(run.stderr)
  if run.stdout!=(ROOT/'RESULT.json').read_text():raise RuntimeError('base output differs')
opt=subprocess.run([sys.executable,'-O',str(ROOT/'verify.py')],capture_output=True,text=True)
if opt.returncode or opt.stdout!=(ROOT/'RESULT.json').read_text():raise RuntimeError('optimized replay failed')
print(json.dumps({'status':'PASS','ordinary_and_optimized_replay':True,'mutations_rejected':result},indent=2,sort_keys=True))
