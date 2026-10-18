"""Verify the complete portable packet inventory."""
from pathlib import Path
import hashlib,json
P=Path(__file__).resolve().parent
expected={}
for line in (P/'SHA256SUMS').read_text().splitlines():
 h,name=line.split('  ',1)
 if name in expected or Path(name).name!=name:raise RuntimeError('bad manifest name')
 expected[name]=h
actual={x.name for x in P.iterdir() if x.is_file() and x.name!='SHA256SUMS'}
if actual!=set(expected):raise RuntimeError('inventory mismatch')
for name,h in expected.items():
 if hashlib.sha256((P/name).read_bytes()).hexdigest()!=h:raise RuntimeError('hash mismatch '+name)
print(json.dumps({'status':'pass','verified_files':len(expected)}))
