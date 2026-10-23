# Reproduction

The published proof package omits the five copied originals. Reconstruct them from INPUTS.json before running verify.py. Run from the package directory:

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

Network access to raw.githubusercontent.com is required for the reconstruction snippet. A failed download or authentication is not a reconstructed input. An authenticated checkout containing the pinned commits can alternatively supply identical bytes with git show <ref>:<path>, using INPUTS.json's exact fields. Verify their recorded Git-blob SHA1 before saving; never substitute current branch files.

verify.py uses Python's standard library and exact Q(sqrt5) arithmetic for the nine fixed binary-icosahedral classes. It checks character orthogonality, the plane Steiner Euler characters, all six even-layer invariant cohomology dimensions, both Leray section-bundle invariant vanishings, the unique invariant vertex channel, K10 and K12 Euler characteristics, the two possible internal transgression rank patterns, and the resulting top-boundary nonvanishing implications. It authenticates all five copied originals.

These checks are bounded abstract arithmetic. They neither enter nor evaluate an actual HM/source coefficient, point, parameter, derivative, matrix or instance rank. Geometry proves the filtrations, connecting-map naturality, cohomology vanishings and nonvanishing theorem; characters alone do not prove any unspecified map has a chosen rank.

Independent whole-proof review is recorded in REVIEW.md, including the Steiner low-twist argument, both Leray spectral sequences, retained nonsplit filtrations and the Gysin comparison.
