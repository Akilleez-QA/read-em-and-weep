"""Restore only the hash-authenticated public certificate; run no mathematics."""
import gzip,hashlib,json
from pathlib import Path
root=Path(__file__).parent
receipt=json.loads((root/'compressed-certificate.json').read_text())
z=(root/receipt['compressed_file']).read_bytes()
if len(z)!=receipt['compressed_bytes'] or hashlib.sha256(z).hexdigest()!=receipt['compressed_sha256']:raise ValueError('compressed certificate hash mismatch')
raw=gzip.decompress(z)
if len(raw)!=receipt['bytes'] or hashlib.sha256(raw).hexdigest()!=receipt['sha256']:raise ValueError('certificate hash mismatch')
(root/receipt['file']).write_bytes(raw)
print('Restored and verified '+receipt['file'])
