"""Verify the closed, flat public inventory including checker source and logs."""
from pathlib import Path
import hashlib
P=Path(__file__).resolve().parent
entries={}
for line in (P/'SHA256SUMS').read_text().splitlines():
 digest,name=line.split('  ',1)
 if name in entries or '/' in name or name=='SHA256SUMS':raise ValueError('invalid inventory')
 entries[name]=digest
actual={x.name for x in P.iterdir() if x.name!='SHA256SUMS'}
if actual!=set(entries):raise ValueError('missing/extra inventory files')
for name,digest in entries.items():
 if hashlib.sha256((P/name).read_bytes()).hexdigest()!=digest:raise ValueError('hash mismatch: '+name)
print('PASS closed inventory ('+str(len(entries))+' files)')
