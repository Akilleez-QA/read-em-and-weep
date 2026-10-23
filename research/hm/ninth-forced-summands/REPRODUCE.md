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

Run `python verify.py` and `python -O verify.py`. Both must pass. The checker uses explicit exceptions and exact nine-class Q(sqrt(5)) character arithmetic. It checks the required Hom vanishings, explicitly retains the nonzero reverse W-to-A Hom and opposite-order ordinary Ext, verifies Cartier duality twists and all ranks/degrees, and authenticates the three original byte counts, SHA256 hashes and Git blob identities.

This is not a formal proof checker. The actual adjacent-layer pullback, full-sheaf duality, nonzero actual cup, target elimination, filtered canonicity and resulting actual split summands are proved in PROOF.md and independently reviewed. No actual coefficient, point, parameter, derivative, jet, matrix or instance rank is evaluated, and no residual map or source alternative is selected.
