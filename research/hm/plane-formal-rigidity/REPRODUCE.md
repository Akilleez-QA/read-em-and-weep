# Reproduction and scope

Publish the five files PROOF.md, REVIEW.md, INPUTS.json, REPRODUCE.md and verify.py. The exact original inputs are deliberately not duplicated in the public package. INPUTS.json pins each repository commit, path, Git blob, byte count and SHA256. The proof retains the original inputs of PR952 and PR955 as premises.

Reconstruct the omitted input directory from exact raw GitHub bytes, without newline normalization:

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

Then run `python verify.py` and `python -O verify.py` from the package directory. Both must pass. The checker uses explicit exceptions, not Python assertions. It checks exact abstract nine-class arithmetic and authenticates all three inputs. It does not implement a proof assistant, construct actual bundle transitions, choose a deformation class, or compute an instance rank. The higher-layer vanishings, equivariant descent, compatible uniqueness and finite nonextension argument require the written proof and independent review.

The new claim is marked formal classification and uniqueness up to normal dilation. The previously known nonzero second-normal class is explicitly not presented as a new result. No global bundle isomorphism, algebraization, actual first failing order, vertex scalar or source/frontier cut is claimed.
