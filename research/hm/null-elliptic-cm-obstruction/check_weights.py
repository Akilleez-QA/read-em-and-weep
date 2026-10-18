"""Integer exponent metadata only; no source or weight evaluation."""
import json,hashlib
from pathlib import Path
P=Path(__file__).resolve().parent
b=(P/'weight-metadata.json').read_bytes()
def need(ok,m):
 if not ok:raise RuntimeError(m)
need(hashlib.sha256(b).hexdigest()=='707663b97c3a8289d6531172a1c509e54ceccb3185a6e07f4f28153fbc119375', 'metadata pin')
x=json.loads(b);r=x['requests'];need(len(r)==30,'count');need([a['id'] for a in r]==list(range(30)),'ids')
odd=[];terms=0
for a in r:
 ps=set()
 for t in a['terms']:
  e=t['dual_monomial'];need(len(e)==4 and all(isinstance(k,int) and k>=0 for k in e),'exponents')
  ps.add(sum(e)%2);terms+=1
 need(len(ps)==1,'one parity per polynomial weight')
 if ps=={1}:odd.append(a['id'])
need(odd==[21,24,26,28],'odd IDs')
print(json.dumps({'status':'pass','requests':30,'terms':terms,'even_weights':26,'odd_weight_ids':odd,'detector_character_claim':False,'metadata_sha256':hashlib.sha256(b).hexdigest()},indent=2))
