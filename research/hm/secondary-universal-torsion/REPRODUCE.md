# Reproduction and exact scope

The five public files are PROOF.md, REVIEW.md, INPUTS.json, REPRODUCE.md and verify.py. Reconstruct the omitted five exact originals from their immutable public locations, retaining raw bytes:

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

Run `python verify.py` and `python -O verify.py`. Both must pass. The checker uses explicit exceptions and exact nine-class Q(sqrt(5)) arithmetic, then verifies source byte counts, SHA256 hashes and Git blob identities. It checks the channel/Ext/Euler multiplicities, kernel degrees, abstract stabilizer weights and the disjoint exhaustive Boolean support partitions. These 64 Boolean supports are not actual coefficient samples. No actual coefficient, parameter, point, derivative, jet, matrix or instance rank is evaluated.

The checker does not prove bundle-map identities, the geometric orbit bound, local elimination, Smith normal forms or the exact splitting of E. Those arguments are supplied in PROOF.md and independently reviewed. The global torsion alternative does not select which case the actual secondary map occupies.
