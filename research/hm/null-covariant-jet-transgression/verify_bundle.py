#!/usr/bin/env python3
"""Verify exact packet inventory, hashes, dependency pins and regression parity."""
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parent
listed={}
for row in (root/'SHA256SUMS').read_text().splitlines():
    digest,name=row.split('  ',1)
    if name in listed or Path(name).is_absolute() or '..' in Path(name).parts:
        raise RuntimeError('Invalid manifest entry')
    listed[name]=digest
actual={str(p.relative_to(root)) for p in root.rglob('*') if p.is_file() and p.name!='SHA256SUMS' and '__pycache__' not in p.parts}
if set(listed)!=actual: raise RuntimeError('Manifest inventory mismatch')
for name,digest in listed.items():
    if hashlib.sha256((root/name).read_bytes()).hexdigest()!=digest: raise RuntimeError('Hash mismatch: '+name)
for record in json.loads((root/'PROVENANCE.json').read_text())['sources']:
    if listed[record['bundled_path']]!=record['bundled_sha256']: raise RuntimeError('Dependency pin mismatch')
normal=(root/'logs/normal.json').read_bytes()
for mode in ('optimized','other-cwd'):
    if normal!=(root/'logs'/f'{mode}.json').read_bytes(): raise RuntimeError('Regression parity failed')
for result in json.loads(normal).values():
    if result['status']!='PASS': raise RuntimeError('Recorded checker failed')
print('PASS: exact inventory, SHA-256 hashes, frozen dependency pins, and normal/-O/alternate-cwd parity')
