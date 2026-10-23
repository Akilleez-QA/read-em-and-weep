# Reproduction and evidence boundary

The focused publication has five files: PROOF.md, REVIEW.md, verify.py, this note, and audit-inputs/manifest.json. The two already-public input proofs are not duplicated.

## Exact inputs

Save the underlying source bytes, not GitHub HTML, to the destinations below. The manifest records the same immutable paths and object hashes.

- `audit-inputs/ALGEBRA.md`: https://github.com/Akilleez-QA/read-em-and-weep/blob/c6c25eaf0e5a67c27eee7c3ba4f000df55997692/research/hm/profile11-source127-cdf-pencil-algebra/PROOF.md
  Expected Git blob: `83f5aee293995257459229e6b323522224ce8f3d`.

- `audit-inputs/GENERATION.md`: https://github.com/Akilleez-QA/read-em-and-weep/blob/2be52725fe471efdc64d74bd87702b581f9f6a48/research/hm/profile11-source127-cdf-positive-generation/PROOF.md
  Expected Git blob: `becd3300950c2379d1f03294863d8335a83a1087`.

Readers with the GitHub CLI and Python can instead fetch the exact Git objects through the API, using this snippet from the publication directory. Repository access may require authentication.

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

Only the Python standard library is needed for the checker. It authenticates both input blobs against hardcoded expected hashes independent of the manifest. Missing or changed bytes are errors.

## Verification scope

The checker uses exact rational arithmetic in Q(sqrt(5)) on the nine fixed binary-icosahedral character classes. It verifies orthogonality, the two universal symmetric-product kernel identities at degrees 7 and 18, all stated cohomology and relation characters, and the dimension sequences 72/93/21 and 9/16/7. Negative controls guard against omitting the constant preimage in ker q_- or omitting the degree-one quotient block in its cokernel.

These are small fixed abstract representation checks. No actual HM/source tensor, parameter, point, derivative, coefficient, matrix or instance rank is evaluated. The checker does not prove actual-map naturality, the six-term exact sequence, the block intersection, or degree-zero generation; those are established in the written proof and independently audited dependency interfaces.

The new kernel Z is only the restricted symmetric-negative quadratic product kernel. Its G-representation splitting is not canonical and does not specify its actual embedding. It is not the full module's minimal relation space. The positive quadratic action is onto the intrinsic seven-dimensional cokernel only as an aggregate over all positive quadratics; no individual positive form is selected. No full-window/full-module lift, actual-HM realization, source exclusion or count decrement follows.
