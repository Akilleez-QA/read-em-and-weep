#!/usr/bin/env python3
"""Run only the audited static checker in isolated copies; never production."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
ROOT=Path(__file__).resolve().parent
pins=json.loads((ROOT/'pins.json').read_text())
checks=[]
with tempfile.TemporaryDirectory(prefix='transition-static-') as td:
 copy=Path(td)/'bundle';shutil.copytree(ROOT,copy)
 for mode in [[],['-O'],['-OO']]:
  for pin in pins:
   path=copy/pin['file'];original=path.read_bytes()
   try:
    path.write_bytes(original+b'\nchanged input\n')
    result=subprocess.run([sys.executable,*mode,str(copy/'check.py')],cwd=td,capture_output=True,text=True,timeout=30)
    if result.returncode==0 or 'frozen input digest changed' not in result.stderr:
     raise ValueError('Changed pin was not rejected: '+pin['file'])
    checks.append({'file':pin['file'],'mode':mode or ['normal'],'rejected':True})
   finally:path.write_bytes(original)
  result=subprocess.run([sys.executable,*mode,str(copy/'check.py')],cwd=td,capture_output=True,text=True,timeout=30)
  if result.returncode:raise ValueError('Portable baseline failed: '+result.stderr)
print(json.dumps({'status':'PASS','rejected_pin_mutations':len(checks),'portable_baselines':3,'scope':'isolated copies of static checker only','checks':checks},indent=2))
