# Reproduction and exact scope

The five public files are PROOF.md, REVIEW.md, INPUTS.json, REPRODUCE.md and verify.py. Reconstruct the omitted three exact originals from their immutable public locations, retaining raw bytes:

```python
from pathlib import Path
import json, urllib.request
root = Path('.')
(root / 'audit-inputs').mkdir(exist_ok=True)
for item in json.loads((root / 'INPUTS.json').read_text()):
    url = 'https://raw.githubusercontent.com/Akilleez-QA/read-em-and-weep/' + item['ref'] + '/' + item['path']
    data = urllib.request.urlopen(url).read()
    (root / 'audit-inputs' / (item['key'] + '.md')).write_bytes(data)
```

Run `python verify.py` and `python -O verify.py`. Both must pass. The checker uses explicit exceptions and verifies source byte counts/SHA256/Git blobs, exact fixed character identities, the unique channels and vanishing Hom spaces, abstract stabilizer weights and bundle-degree arithmetic. The actual quotient diagram, universal channel constructions, reduced determinantal ideals and original graph-lift kernels are proved in PROOF.md and independently reviewed. No actual coefficient or point is selected; the invariant binary form is used universally, not evaluated at an HM/source instance.
