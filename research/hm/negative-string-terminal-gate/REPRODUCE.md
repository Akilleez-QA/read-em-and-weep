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

Python standard library only. The verifier uses exact rational arithmetic in Q(sqrt(5)) on the fixed nine conjugacy classes of SL2(F5). It authenticates the five original byte strings, computes the B(5) Euler character and its cohomology character using the pinned section theorem, and checks the exact Koszul character, terminal multiplicity and Euler-subpencil quotient dimensions. It does not evaluate any actual HM/source coefficient, point, parameter, jet or matrix, and does not select a terminal branch. The actual parity, Koszul exactness, inherited pencil maps and splitting statements require the written mathematical proof and independent review; the checker does not certify them automatically.
