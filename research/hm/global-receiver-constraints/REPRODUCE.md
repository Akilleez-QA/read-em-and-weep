# Reproduction and exact scope

The five public files are PROOF.md, REVIEW.md, INPUTS.json, REPRODUCE.md and verify.py. Reconstruct the omitted two exact originals from their immutable public locations, retaining raw bytes:

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

Run `python verify.py` and `python -O verify.py`. Both must pass. The checker uses explicit exceptions and exact nine-class Q(sqrt(5)) character arithmetic. It verifies all seven authenticated type ranks/degrees, every Hom(C,O(6)) vanishing, source-target channel counts, the common quotient vanishings, named channel dimensions and bundle degrees, and both input byte counts, SHA256 hashes and Git blob identities.

The checker is not a formal proof checker. Universal evaluation exactness, actual factorization, receiver canonicity, joint kernels and the named global subbundle inclusions are proved in PROOF.md and independently reviewed. No selected actual coefficient, point, parameter, derivative, jet, matrix or instance rank is evaluated. The seven-row check is a fixed abstract character calculation, not selection of an actual row.
