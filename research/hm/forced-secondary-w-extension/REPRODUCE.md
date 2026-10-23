# Reproduction

The public package consists of PROOF.md, REVIEW.md, INPUTS.json, REPRODUCE.md and verify.py. The exact original inputs are omitted rather than duplicated. Reconstruct their raw bytes using the immutable commit/path entries, without newline normalization:

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

Then run `python verify.py` and `python -O verify.py`. Both must pass. The checker uses explicit exceptions rather than removable assertions. It checks exact abstract character identities, Hom/Ext dimensions, the V-channel character restriction, ranks/degrees and input byte count, SHA256 and Git-blob identity.

The checker does not choose or evaluate any actual HM matrix, jet, deformation, point, coefficient, extension class, or rank. The actual nonvanishing and canonical pushout are proved from the imported map formula and exact sequences, and checked by independent mathematical review. This is not proof-assistant verification.

The new result closes the W-extension zero alternative explicitly left in PR968 and identifies the resulting actual rank-five subbundle. It leaves the residual two-dimensional extension direction and secondary boundary rank unselected, while excluding the kernel of the V-channel functional. All original premises retained by PR968 and FIRST remain premises here.
