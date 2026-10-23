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

Run `python verify.py` and `python -O verify.py`. Both must pass. The checker uses explicit exceptions rather than removable assertions, verifies source byte counts/SHA256/Git blobs, and checks fixed abstract characters, full inversion parity and ordinary-layer Euler identities. The actual sheaf-multiplication diagram, connecting-map naturality and finite vanishing are proved in the text and independently reviewed, not inferred solely from the checker.

All thickenings in the new theorem are ambient codimension-two ordinary neighborhoods defined by I_R^m in P4. The full section space vanishes on 4R and later, while its third-neighborhood odd space has dimension six. This does not concern only G-invariant sections and does not replace the distinct hyperplane neighborhoods in PR974. No selected actual HM/source coefficient, parameter, point, jet, matrix, derivative or instance rank is evaluated.
