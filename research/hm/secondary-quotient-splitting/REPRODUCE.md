# Exact reproduction

Public package: PROOF.md, REVIEW.md, INPUTS.json, REPRODUCE.md and verify.py. The two immutable original texts are not duplicated in the public package. Reconstruct their exact raw bytes as follows, without normalizing line endings:

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

Run `python verify.py` and `python -O verify.py` from this directory. Both must pass. The checker uses explicit exceptions, not removable Python assertions. It authenticates every input by byte count, SHA256 and Git-blob identity, and checks exact abstract character identities and extension-space dimensions.

The actual quotient identification and forced nonsplitting are proved in the text using the imported exact maps and their surjectivity/injectivity. The checker does not evaluate an actual HM coefficient, select a parameter, calculate an instance rank, or prove the geometry by machine. Independent written review is not formal proof-assistant verification.

Novelty was checked against the exact SQUARE and SECOND notes, the available shared research notes, and repository PR searches for the rank-six/square quotient. The originals provide the actual kernel presentation and rank/degree, not the splitting or forced nonzero P-extension proved here. This is not an exhaustive assertion about all mathematical literature.
