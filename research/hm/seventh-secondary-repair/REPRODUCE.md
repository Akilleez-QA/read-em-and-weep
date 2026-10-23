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

Run `python verify.py` and `python -O verify.py`. Both must pass. The checker uses explicit exceptions and exact nine-class Q(sqrt(5)) arithmetic, verifies all source byte counts, SHA256 hashes and Git blob identities, and checks fixed bundle dimensions/degrees, normal parity/twists, the relevant line-bundle Ext vanishing and symbolic rank identities. Looping over possible integer ranks is not evaluation of any actual map.

The checker is not a formal proof checker. The actual derived extension, lift ambiguity, uniform base change, canonical correction, Tor boundary and elementary-modification arguments are proved in PROOF.md and independently reviewed. No actual coefficient, parameter, point, derivative, jet, matrix or instance rank is evaluated. The theorem does not select whether secondary torsion is present.
