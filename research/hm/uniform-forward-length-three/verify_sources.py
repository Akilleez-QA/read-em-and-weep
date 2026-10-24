#!/usr/bin/env python3
"""Authenticate the four retained immutable public inputs; no network or experiment."""
from pathlib import Path
import hashlib
import json
ROOT = Path(__file__).resolve().parent
EXPECTED = {
 'ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md': ('b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3', 'a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256', 9672),
 'POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md': ('303c6927265296440470b9dd4015fe6e8d55ca4d', '0928dd8261ac0d2659188af6520b564611b289cd0e271185ef5f4e3bafe3a6a2', 5414),
 'TWIST-ONE-ACTUAL-SECTION-KERNEL-VANISHING.md': ('26d41b06b3b3f7c1131098dd2c64901530156907', '44882df7ae6758d4404b8cdc167e31aa318b54a4047cdc67b347c32b2a69cfab', 3977),
 'GAUSS-DETERMINANT-ORBIT-RAMIFICATION.md': ('a79287dc4afe3ba9eb0d3439db4846169bf1c2a3', '783454715e967929ad81e6f09f8f4a155073fbdab89974bee056416e4f866e71', 12488),
}
COMMIT = 'db51525015bb7c5e825833d550d08dedf6f6ea96'
PREFIX = 'research/hm/order-four-quadratic-load/'
BASE_URL = 'https://github.com/Akilleez-QA/read-em-and-weep/blob/'
rows = json.loads((ROOT/'INPUTS.json').read_text())
if len(rows) != len(EXPECTED) or {Path(r['file']).name for r in rows} != set(EXPECTED):
 raise RuntimeError('Input set mismatch')
for row in rows:
 name = Path(row['file']).name
 blob, sha256, size = EXPECTED[name]
 if (row['file'] != 'sources/'+name or row['commit'] != COMMIT or
     row['repository_path'] != PREFIX+name or row['url'] != BASE_URL+COMMIT+'/'+PREFIX+name):
  raise RuntimeError('Input provenance mismatch: '+name)
 if (row['git_blob_sha1'],row['sha256'],row['bytes']) != (blob,sha256,size):
  raise RuntimeError('Input pin mismatch: '+name)
 raw = (ROOT/row['file']).read_bytes()
 if (len(raw) != size or hashlib.sha256(raw).hexdigest() != sha256 or
     hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest() != blob):
  raise RuntimeError('Input byte mismatch: '+name)
print(json.dumps({'status':'PASS','immutable_inputs_authenticated':len(rows)},sort_keys=True))
