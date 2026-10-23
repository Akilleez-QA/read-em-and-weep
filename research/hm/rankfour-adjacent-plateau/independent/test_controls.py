#!/usr/bin/env python3
"""Fail-closed mutation controls for the independent universal checker."""
from pathlib import Path
import json, subprocess, sys, tempfile, shutil
ROOT=Path(__file__).resolve().parent
base=(ROOT/'verify.py').read_text()
mutants={
 'endpoint_parity':('return n if n%2==0 else n-1','return n'),
 'defect_weight':('identity==(120,0,0,3,6,4,2)','identity==(120,0,0,3,5,4,2)'),
 'quotient_twist':('check(-2+4==0+2,','check(-2+3==0+2,'),
 'physical_marking':("euler_e2==cscale(-1,C['V'])","euler_e2==cscale(-1,C['A'])"),
 'line_tail_h1':('left=cadd(line_euler(-2),line_euler(-4))','left=line_euler(-4)'),
}
def run(path,optimized=False):
    args=[sys.executable]+(['-O'] if optimized else [])+[str(path/'verify.py')]
    return subprocess.run(args,text=True,capture_output=True,cwd='/tmp')
results={}
for optimized in (False,True):
    proc=run(ROOT,optimized)
    if proc.returncode or proc.stdout!=(ROOT/'RESULT.json').read_text(): raise RuntimeError('baseline replay failed')
    results['baseline_optimized' if optimized else 'baseline']='PASS'
with tempfile.TemporaryDirectory(prefix='rankfour-adjacent-controls-') as tmp:
    path=Path(tmp); shutil.copytree(ROOT/'inputs',path/'inputs')
    for name,(old,new) in mutants.items():
        if base.count(old)!=1: raise RuntimeError('ambiguous mutation '+name)
        (path/'verify.py').write_text(base.replace(old,new))
        proc=run(path)
        if not proc.returncode: raise RuntimeError('mutation not rejected '+name)
        results[name]='REJECTED'
    (path/'verify.py').write_text(base)
    p=path/'inputs'/'ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md'
    p.write_bytes(p.read_bytes()+b'\n')
    proc=run(path)
    if not proc.returncode: raise RuntimeError('source tamper accepted')
    results['source_bytes']='REJECTED'
print(json.dumps({'status':'PASS','controls':results},indent=2,sort_keys=True))
