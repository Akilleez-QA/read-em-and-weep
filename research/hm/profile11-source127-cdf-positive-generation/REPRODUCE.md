# Reproduction and evidence boundary

The focused publication consists of PROOF.md, REVIEW.md, verify.py, this note, and audit-inputs/manifest.json. The three already-public input documents are not copied into the publication.

## Obtain exact inputs

Save the underlying source bytes, not GitHub HTML, from each immutable source into the indicated destination. The exact Git blob hashes authenticate the bytes independently of the displayed page.

- `audit-inputs/GENERATION.md`: https://github.com/Akilleez-QA/read-em-and-weep/blob/3aa461bc3581fb72fbf923fbe869ddee023b435a/research/hm/five-generator-module/PROOF.md
  Expected Git blob: `3d308f6fbdb5c224a085b41eec26e917a6031692`.

- `audit-inputs/FULL-MODULE.md`: https://github.com/Akilleez-QA/read-em-and-weep/blob/f4a73af666900ad2cb34a756d24b88e19dd6feaa/research/hm/negative-truncation-extension/PROOF.md
  Expected Git blob: `2ba0a7eee6ef2eb5413683e85618d7902dca3970`.

- `audit-inputs/ALGEBRA.md`: https://github.com/Akilleez-QA/read-em-and-weep/blob/c6c25eaf0e5a67c27eee7c3ba4f000df55997692/research/hm/profile11-source127-cdf-pencil-algebra/PROOF.md
  Expected Git blob: `83f5aee293995257459229e6b323522224ce8f3d`.

A reproducible alternative for readers with the GitHub CLI and Python installed is to fetch the exact blobs through the API. Run this from the publication directory. Repository authentication may be required.

```python
import base64
import hashlib
import json
import pathlib
import subprocess

root = pathlib.Path('.')
for entry in json.loads((root / 'audit-inputs/manifest.json').read_text()):
    endpoint = 'repos/Akilleez-QA/read-em-and-weep/git/blobs/' + entry['git_blob']
    response = json.loads(subprocess.check_output(['gh', 'api', endpoint]))
    if response['encoding'] != 'base64':
        raise RuntimeError('Unexpected encoding')
    data = base64.b64decode(response['content'])
    header = b'blob ' + str(len(data)).encode() + b'\0'
    if hashlib.sha1(header + data).hexdigest() != entry['git_blob']:
        raise RuntimeError('Blob mismatch')
    (root / 'audit-inputs' / entry['name']).write_bytes(data)
```

Then run:

    python3 verify.py
    python3 -O verify.py

The checker uses only the Python standard library. Its three expected blob hashes are hardcoded independently of the manifest. Missing or changed input bytes are errors.

## What the bounded checker establishes

It checks the same-sign quadratic factorization of all 126 formal degree-five monomials in three positive and two negative indeterminates, retaining both possible generator signs. This gives 252 parity checks and includes a mixed degree-two negative control to guard the n>=3 hypothesis. It also checks the fixed block and filtration dimension arithmetic imported from the exact algebra theorem.

The indeterminates are universal polynomial symbols, not selected actual source variables, parameters or evaluated points. The checker builds no actual tensor or matrix and performs no source-instance rank test. The pigeonhole argument in the written proof, not a finite sample, proves the general n>=3 lemma.

Actual degree-zero generation, the simultaneous source bridge and represented algebra are authenticated pinned hypotheses. The new surjectivity and nonextension arguments, and the injective compatible-algebra projection yielding the C/C^2 dichotomy, require the written proof and its independent mathematical review. The checker is not proof-assistant certification.

The aggregate positive radical channel is forced onto P, and the entire scalar-target projection is onto V+P. This does not assert surjectivity for one fixed positive quadratic or determine the full positive tensor. The radical-kernel marked extension is ruled out, but no theorem forces that extension. No source, stable label, source-dual pair or frontier count is removed; no full-module lift or actual-HM realization follows.
