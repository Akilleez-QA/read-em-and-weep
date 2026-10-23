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

Run `python verify.py` and `python -O verify.py`. Both must pass. The checker uses explicit exceptions, exact nine-class Q(sqrt(5)) characters and byte-count/SHA256/Git-blob authentication of all three originals. It verifies the two forbidden Hom spaces, the six allowed one-dimensional spaces and the 30-to-24 dimension reduction. The actual neighborhood long exact sequence and determinantal-ideal statements are proved mathematically, not by instance evaluation. No selected HM/source data or large computation is used.
