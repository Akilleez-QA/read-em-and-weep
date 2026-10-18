#!/usr/bin/env python3
"""Verify portable bytes only; never execute imported mathematical sources."""
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parent
count=0
for line in (root/'SHA256SUMS').read_text().splitlines():
    wanted,name=line.split('  ',1)
    path=root/name
    if path.resolve().parent!=root and root not in path.resolve().parents: raise RuntimeError('unsafe manifest path')
    actual=hashlib.sha256(path.read_bytes()).hexdigest()
    if actual!=wanted: raise RuntimeError('digest mismatch: '+name)
    count+=1
for entry in json.loads((root/'pins.json').read_text())['dependencies']:
    if hashlib.sha256((root/entry['path']).read_bytes()).hexdigest()!=entry['sha256']: raise RuntimeError('dependency pin mismatch')
print(json.dumps({'status':'pass','verified_files':count,'scope':'bytes only'},indent=2))
