# Reproduction and limitations

Public package: PROOF.md, REVIEW.md, INPUTS.json, REPRODUCE.md and verify.py. Reconstruct the omitted exact input from its immutable public source, retaining original bytes:

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

Run `python verify.py` and `python -O verify.py`. Both must pass. The checker uses explicit exceptions, verifies source byte count, SHA256 and Git-blob identity, and checks only fixed abstract characters and small rank/degree arithmetic. The equivariant bundle argument, actual injections, canonical evaluation and splitting logic are supplied by the written proof and independent review, not by an instance calculation or proof assistant.

The two displayed types form an exhaustive list of possibilities for the actual K under the retained premises. Neither is selected, and existence of both actual cases is not asserted. The square inclusion and secondary maps are not replaced by abstract arrows after choosing a bundle isomorphism.
