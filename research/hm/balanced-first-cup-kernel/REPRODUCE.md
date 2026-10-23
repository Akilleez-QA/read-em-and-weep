# Reproduction and verification scope

The public package has five files: PROOF.md, REVIEW.md, INPUTS.json, REPRODUCE.md and verify.py. The two exact original inputs are omitted to avoid duplication. Reconstruct their raw bytes without newline normalization:

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

Run `python verify.py` and `python -O verify.py`. Both must pass. Explicit exceptions are used instead of optimization-removable assertions. The checker authenticates byte counts, SHA256 and Git blobs; checks the fixed nine-class characters and universal SL2 Laurent-weight decompositions; and records the two nonzero universal tensor coefficients and the derivative-span dimension consequence.

The binary variables and orthogonal operators in the proof are abstract representation variables. They are not selected actual HM/source coefficients, physical points or matrices. The proof of the derivative-span inequality is universal and uses no numerical rank computation. The checker does not implement a proof assistant, evaluate the actual first-cup tensor, or substitute a generic rank for an authenticated map.

The new result chooses the actual negative two-step K type from PR975's two possibilities and proves surjectivity of the actual ambient 30-to-24 first odd-scaling cup. It neither changes the existing projected two-root bound nor computes the later secondary boundary or global odd-quadric sections. The exact original hypotheses retained by both inputs remain in force.
