"""Portable negative pin control; no production code is executed."""
import json, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent
with tempfile.TemporaryDirectory(prefix='primitive-pin-control-') as td:
    altered=Path(td)/'altered-model.json'
    altered.write_bytes((ROOT/'inputs/model.json').read_bytes()+b'\n')
    r=subprocess.run([sys.executable,'-O',str(ROOT/'check.py'),'--model',str(altered)],capture_output=True,text=True)
    expected='RuntimeError: immutable SHA256 mismatch: model'
    if r.returncode==0 or expected not in r.stderr:
        raise RuntimeError('negative pin control did not reject the changed bytes')
print(json.dumps({'status':'PASS','optimized_python':True,'control':'changed model bytes rejected before model parsing','expected_failure':expected,'physical_evaluation':False},indent=2))
