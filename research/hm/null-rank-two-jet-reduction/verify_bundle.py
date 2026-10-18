from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parent
for row in (root/'SHA256SUMS').read_text().splitlines():
    digest,name=row.split('  ',1)
    if hashlib.sha256((root/name).read_bytes()).hexdigest()!=digest: raise RuntimeError('Hash mismatch: '+name)
for rec in json.loads((root/'PROVENANCE.json').read_text())['sources']:
    if hashlib.sha256((root/rec['bundled_path']).read_bytes()).hexdigest()!=rec['bundled_sha256']: raise RuntimeError('Provenance mismatch')
a=(root/'logs/normal.json').read_bytes()
for name in ('optimized.json','other-cwd.json'):
    if a!=(root/'logs'/name).read_bytes(): raise RuntimeError('Regression results differ')
print('PASS: bundle hashes, excerpt pins, and normal/-O/alternate-cwd output equality')
