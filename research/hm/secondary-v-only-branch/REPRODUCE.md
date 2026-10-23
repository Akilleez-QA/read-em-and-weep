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

Run `python verify.py` and `python -O verify.py`. Both must pass. The checker uses explicit exceptions, exact nine-class Q(sqrt(5)) arithmetic, and source byte/SHA256/Git-blob checks. It verifies the canonical source/Hom multiplicities, one-dimensional discriminant and Ext spaces, and the degrees of all original-kernel alternatives. Actual pullback identifications, constant fiber rank, scalar normalization and extension-model arguments are proved in PROOF.md and independently reviewed. No actual coefficient value, point, jet or matrix is evaluated.
