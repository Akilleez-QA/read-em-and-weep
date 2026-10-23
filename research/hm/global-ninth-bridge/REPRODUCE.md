# Reproduction and exact scope

The five public files are PROOF.md, REVIEW.md, INPUTS.json, REPRODUCE.md and verify.py. Reconstruct the omitted six exact originals from their immutable public locations, retaining raw bytes:

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

Run `python verify.py` and `python -O verify.py`. Both must pass. The checker uses explicit exceptions, verifies the fixed restriction and relative-duality twists, parity cancellation, bundle ranks/degrees, Steiner coefficient sizes and negative determinant degrees, and authenticates all six input byte counts, SHA256 hashes and Git blob identities.

The checker is not a formal proof checker. Uniform vanishing, base change, relative duality, the actual incidence and restriction maps, and the finite/global determinant constraint are proved in PROOF.md and independently reviewed. It does not evaluate actual HM/source coefficients, points, parameters, derivatives, jets, matrices or instance ranks. Neither global-to-finite bridge is assumed split.
