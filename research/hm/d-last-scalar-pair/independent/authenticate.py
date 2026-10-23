#!/usr/bin/env python3
"""Check retained fresh public-source responses against a supplied author packet."""
import argparse,hashlib,json
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('packet',type=Path);args=ap.parse_args();p=args.packet
R=Path(__file__).resolve().parent
pins={'PROOF.md':'590dfb8da397d866059bf341b66eca2c7e408819fbf3fa2d7257313ab1f5d619','verify.py':'1098eec3826a8bb35afc523cc93ba3be1116e31d5837b9a069855317547ce98f','RESULT.json':'6ae1126050a074efcc989a7b7536ca8bb230078f9ce9167e553144d75278d5ea','INPUTS.json':'1ff429f45d8bc9cd3a23ff9d65f1564add97fe50a13a644d9a7359f673f1f1ae'}
checks=0
def check(b):
 global checks
 checks+=1
 if not b:raise RuntimeError('Source authentication mismatch')
for f,h in pins.items():check(hashlib.sha256((p/f).read_bytes()).hexdigest()==h)
fresh={r['file']:r for r in json.loads((R/'FRESH.json').read_text())}
rows=json.loads((p/'INPUTS.json').read_text())
for r in rows:
 f=fresh[r['file']];b=f['content'].encode()
 check(b==(p/r['file']).read_bytes());check(len(b)==r['bytes']);check(hashlib.sha256(b).hexdigest()==r['sha256']);check(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==r['git_blob_sha1']==f['sha'])
print(json.dumps({'checks':checks,'status':'PASS','source_count':len(rows),'pins':pins},indent=2,sort_keys=True))
