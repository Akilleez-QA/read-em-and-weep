"""Byte/schema authentication only; the historical producer is NEVER executed."""
from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parent
manifest=json.loads((P/'historical-manifest.json').read_text())['sha256']
for local,remote in [('model.json','data/model.json'),('historical-A-receipt.json','certificates/homogeneous-identities.json'),('historical-producer-INERT.txt','checks/verify_homogeneous_identities.py')]:
 if hashlib.sha256((P/local).read_bytes()).hexdigest()!=manifest[remote]:raise ValueError('historical manifest binding')
m=json.loads((P/'model.json').read_text()); receipt=json.loads((P/'historical-A-receipt.json').read_text())
if hashlib.sha256(json.dumps(m,separators=(',',':')).encode()).hexdigest()!=receipt['modelSha256']:raise ValueError('receipt canonical model')
if len(m['charts'])!=6 or receipt['byIdentity']['E_identity']!=6*15*15:raise ValueError('A coverage count')
source=json.loads((P/'SOURCE_EXCERPTS.json').read_text())
producer=(P/'historical-producer-INERT.txt').read_text().splitlines(keepends=True)
h=source['homogeneous'];excerpt=''.join(producer[h['start_line']-1:h['end_line']])
if excerpt!=h['text'] or hashlib.sha256(excerpt.encode()).hexdigest()!=h['sha256']:raise ValueError('homogeneous excerpt')
for pin in json.loads((P/'PINS.json').read_text()):
 if 'local_file' in pin and hashlib.sha256((P/pin['local_file']).read_bytes()).hexdigest()!=pin['sha256']:raise ValueError('pin')
print(json.dumps({'status':'PASS','A_imported_not_recomputed':True,'historical_manifest_model_producer_receipt_bindings':True,'A_recorded_entry_count':1350,'homogeneous_excerpt_exact':True},indent=2))
