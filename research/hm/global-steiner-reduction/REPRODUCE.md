# Reproduction and scope

Publish only PROOF.md, REVIEW.md, INPUTS.json, REPRODUCE.md and verify.py. The omitted audit-inputs directory consists of exact immutable public repository originals, not unpublished data.

Reconstruct the originals from the same directory as this packet:

```sh
python - <<'PY'
from pathlib import Path
from urllib.request import urlopen
import hashlib,json
root=Path('.'); (root/'audit-inputs').mkdir(exist_ok=True)
for item in json.loads((root/'INPUTS.json').read_text()):
    url='https://raw.githubusercontent.com/Akilleez-QA/read-em-and-weep/'+item['ref']+'/'+item['path']
    b=urlopen(url).read()
    if len(b)!=item['bytes']: raise RuntimeError('length: '+item['key'])
    if hashlib.sha256(b).hexdigest()!=item['sha256']: raise RuntimeError('SHA256: '+item['key'])
    h=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
    if h!=item['blob']: raise RuntimeError('Git blob: '+item['key'])
    (root/'audit-inputs'/(item['key']+'.md')).write_bytes(b)
PY
python verify.py
python -O verify.py
```

Python standard library only. The verifier uses exact rational arithmetic in Q(sqrt(5)) on the fixed nine conjugacy classes of SL2(F5). It authenticates the five original byte strings, computes the B(1) and B(2) Euler characters from the normalized-monad K-class, and checks coefficient dimensions, the unique W/A components, and the two extension channels. It performs no actual HM/source evaluation or parameter scan. It does not certify the geometric proof automatically; the source vanishings, actual evaluation diagram, saturation and extension identification require the written proof and independent review.
