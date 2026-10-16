#!/usr/bin/env python3
"""Replay the entire public package without physical polynomial evaluation."""
from pathlib import Path
import hashlib,json,subprocess,sys
if not __debug__:raise SystemExit('optimized Python refused')
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
from prepare_artifacts import prepare

def main():
    for line in (ROOT/'SHA256SUMS').read_text().splitlines():
        digest,name=line.split('  ',1)
        if hashlib.sha256((ROOT/name).read_bytes()).hexdigest()!=digest:
            raise ValueError('package hash mismatch: '+name)
    prepare()
    import traverse_selected_scalar_demand as demand
    import compile_actual_scalar_differential_kernel as compiler
    selected=demand.encode(demand.build())+b'\n'
    if selected!=(ROOT/'selected-scalar-demand-dag.json').read_bytes():raise ValueError('selected DAG replay mismatch')
    generated=json.dumps(compiler.build(),sort_keys=True,separators=(',',':')).encode()+b'\n'
    if generated!=(ROOT/'actual-scalar-differential-kernel.json').read_bytes():raise ValueError('compiler replay mismatch')
    for path in sorted(ROOT.glob('test_*.py')):
        subprocess.run([sys.executable,str(path)],cwd=ROOT,check=True)
    print('PASS: byte-identical public artifacts; all abstract and metadata controls passed.')
    print('No physical polynomial evaluation, full-domain Laurent admission, or obstruction value is established.')
if __name__=='__main__':main()
