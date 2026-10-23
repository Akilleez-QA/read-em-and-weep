# Reproduction and exact scope

The five public files are PROOF.md, REVIEW.md, INPUTS.json, REPRODUCE.md and verify.py. Reconstruct the omitted four exact originals from their immutable public locations, retaining raw bytes:

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

Run `python verify.py` and `python -O verify.py`. Both must pass. The checker uses explicit exceptions, exact nine-class Q(sqrt(5)) characters and byte-count/SHA256/Git-blob authentication of the four originals. It verifies the fixed Hom multiplicities, symmetric-power decompositions, unique invariant and degree/rank arithmetic used in the proof. It does not certify a selected actual secondary coefficient or rank. The base-divisor exclusion, evaluation-kernel splitting, nonzero polarization, exact row geometry, determinantal scheme and conditional full-kernel criterion and original-kernel extension classification are proved mathematically and independently reviewed. No selected actual HM/source data or large computation is used.
