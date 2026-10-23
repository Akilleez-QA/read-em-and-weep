# Reproduction and evidence boundary

The focused publication consists of PROOF.md, REVIEW.md, verify.py, this note, and audit-inputs/manifest.json. It does not duplicate the six already-public inputs.

## Obtain exact immutable inputs

Save underlying source bytes, not GitHub HTML, from these immutable sources to the listed destinations. The manifest records the same exact Git blob hashes.

- `audit-inputs/ACTUAL.md`: https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md
  Expected Git blob: `b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3`.

- `audit-inputs/STRICT-TOP.md`: https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md
  Expected Git blob: `d7506dae49b4be43230450c4132bd5db91f137ef`.

- `audit-inputs/pairs.json`: https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/one-one-endpoint-necessary-pairs.json
  Expected Git blob: `fe0afa410d89340d3082dc814277f89fbb582c19`.

- `audit-inputs/frontier.json`: https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/rank-three-quotient-frontier-144.json
  Expected Git blob: `8b5971092f9ef762584912609fd5e9301c4e271d`.

- `audit-inputs/HIGH-D-KERNEL.md`: https://github.com/Akilleez-QA/read-em-and-weep/blob/2db172b32dc014c06521a3fcba20261db5bb00fa/research/hm/profile11-source127-acff-exclusion/PROOF.md
  Expected Git blob: `3448047b9f67b258955f0fe53c3368b6f7615d9e`.

- `audit-inputs/D-REDUCTION.md`: https://github.com/Akilleez-QA/read-em-and-weep/blob/b84ea860de5ebe38cff3c54054e80dd4be5ac77c/research/hm/profile11-source127-abcf-reduction/PROOF.md
  Expected Git blob: `ac36f048fc0987a1c78fbd9a61bc18077963ce20`.

One reproducible alternative, for readers with the GitHub CLI and Python installed, is the following. It fetches each exact Git blob, decodes the API's base64 content, and verifies the blob hash before writing the input file. GitHub authentication may be needed if repository access requires it.

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
    assert response['encoding'] == 'base64'
    data = base64.b64decode(response['content'])
    header = b'blob ' + str(len(data)).encode() + b'\0'
    assert hashlib.sha1(header + data).hexdigest() == entry['git_blob']
    (root / 'audit-inputs' / entry['name']).write_bytes(data)
```

Run that preparation from the publication directory, then run:

    python3 verify.py

The verifier itself needs only the Python standard library. It rechecks all six immutable Git blob hashes before using the data. An input is accepted only when its exact source bytes match the published hash.

## Checks and scope

The verifier authenticates the four original inputs and public PR905/PR913 dependency chain. It checks exact source identity, the forced constant-A Euler coefficient, all six rank-two kernel types, the A-injection obstruction, scalar separation, the invariant-free actual-target extension, exact rank14 cohomology, all five constant budgets and three residual possibilities, and every final Hom channel.

The proof and independent review separately verify the actual positive Gauss preimage, coefficient multiplicity, saturation, coherent scalar splitting, the pullback target of the derivative, and the source-specific nonzero low-D interface. The entire a-b-c-f source is excluded; no whole stable label or c-d-f family is excluded. No selected actual HM/source coefficients, parameters, points, derivatives, matrices, instance ranks, models, scans or large computation are used.
