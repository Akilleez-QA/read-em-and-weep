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
    (root/'audit-inputs'/item['local']).write_bytes(b)
PY
python verify.py
python -O verify.py
```

Python standard library only. INPUTS.json records exact raw bytes for three proof originals and two JSON catalogue/ledger originals. Preserve those bytes, including final newline conventions. The verifier authenticates byte length, SHA256 and Git blob for all five, and checks that the catalogue's upstream ACTUAL proof hash is the same original parameter-pencil theorem. It reads only the four pinned frontier pairs and their three named E types for the conditional arithmetic; it performs no source-instance search.

The remaining checks use exact rational arithmetic in Q(sqrt(5)) on the fixed nine conjugacy classes: global B(6) Euler character, actual plane section character, and H0/H1(E(2)) for the three fixed types. No actual coefficient, point, parameter, jet, matrix or instance rank is evaluated. The checker does not certify the naturality and geometric arguments automatically; these require the proof and independent review. Necessary ledger membership is not a realization theorem, and no terminal branch is selected.
