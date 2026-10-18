"""Verify all delivered bytes against the portable manifest."""
from pathlib import Path
import hashlib
root=Path(__file__).resolve().parent
seen=set()
for line in (root/'SHA256SUMS').read_text().splitlines():
    digest,name=line.split('  ',1)
    if name in seen: raise RuntimeError('Duplicate manifest entry: '+name)
    seen.add(name)
    p=root/name
    if hashlib.sha256(p.read_bytes()).hexdigest()!=digest: raise RuntimeError('Digest mismatch: '+name)
actual={str(p.relative_to(root)) for p in root.rglob('*') if p.is_file() and p.name!='SHA256SUMS'}
if seen!=actual: raise RuntimeError('Manifest file inventory mismatch')
print('PASS: '+str(len(seen))+' packet files verified')
