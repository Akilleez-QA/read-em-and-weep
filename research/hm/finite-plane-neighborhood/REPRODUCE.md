# Reproduction

The five-file published package omits the copied prior proof. Reconstruct that exact immutable input before running verify.py. From this package directory:

```sh
python3 - <<'PYINPUTS'
import hashlib
import json
from pathlib import Path
from urllib.request import urlopen
out = Path('audit-inputs')
out.mkdir(exist_ok=True)
for item in json.loads(Path('INPUTS.json').read_text()):
    url = ('https://raw.githubusercontent.com/Akilleez-QA/read-em-and-weep/'
           + item['ref'] + '/' + item['path'])
    with urlopen(url) as response:
        data = response.read()
    actual = hashlib.sha1(b'blob ' + str(len(data)).encode('ascii')
                          + bytes([0]) + data).hexdigest()
    if actual != item['blob']:
        raise RuntimeError('Immutable input mismatch: ' + item['key'])
    (out / (item['key'] + '.md')).write_bytes(data)
    print(item['key'], actual)
PYINPUTS
python3 verify.py
python3 -O verify.py
```

Network access to raw.githubusercontent.com is needed for the download. Authentication or download failure is not successful reconstruction. Alternatively use an authenticated repository checkout and git show <ref>:<path> with the exact INPUTS.json fields; authenticate the Git-blob bytes before saving. Never substitute current branch versions.

The standard-library verifier uses exact nine-class Q(sqrt5) character arithmetic, with orthogonality checks. It checks the invariant normal-layer dimensions zero/one/one/two, ordinary-neighborhood indices3/5/7, the dual twist4, both allowed obstruction alternatives, and the exact prior proof bytes. It performs no actual HM/source coefficient, point, parameter, derivative, matrix or instance-rank evaluation.

The checker is not a proof of the duality theorem: PROOF.md proves the derived identification, exact ordinary ideal power, and natural map orientations. REVIEW.md independently checks these geometric steps, the ordinary third-neighborhood candidate, and its forced failure at order four or six. The prior proof's broader verifier can be reproduced separately from its own immutable package and instructions.
