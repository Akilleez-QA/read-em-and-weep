# Reproduction and exact scope

The five public files are PROOF.md, REVIEW.md, INPUTS.json, REPRODUCE.md and verify.py. Reconstruct the omitted one exact original from their immutable public locations, retaining raw bytes:

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

Run `python verify.py` and `python -O verify.py`. Both must pass. The checker verifies source byte/SHA256/Git-blob identity, exact fixed characters, the low-degree rank-one exclusions, abstract C10 stabilizer weights, and conditional rank arithmetic using explicit exceptions. It does not select any actual secondary coefficient or evaluate any actual orbit point. Universal bundle constructions, comparison normalization and determinantal multiplicities are established in the proof and independent review, not inferred from the checker.
