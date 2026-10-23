# Reproduction and evidence boundary

The focused publication consists of PROOF.md, REVIEW.md, verify.py, this note, and audit-inputs/manifest.json. It does not duplicate the seven already-public inputs.

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

- `audit-inputs/PR859.md`: https://github.com/Akilleez-QA/read-em-and-weep/blob/6129e92a26572779003f3295227f688b77ed881c/research/hm/profile11-o16-high-p-divisor/PROOF.md
  Expected Git blob: `79ec9cd555997cb9e3b8dc76f3b64fa3f836ad2e`.

- `audit-inputs/PR867.md`: https://github.com/Akilleez-QA/read-em-and-weep/blob/b2a12c98bc162062a938b7a7a6a90ab45786e340/research/hm/profile11-o16-cdf-kernels/PROOF.md
  Expected Git blob: `76a6bd75b77232af222ccb91555499b4a4437311`.

- `audit-inputs/PR885.md`: https://github.com/Akilleez-QA/read-em-and-weep/blob/53939364de5459822be1a32be08f2b12dbbb4280/research/hm/profile11-source127-hbf-kernel-reduction/PROOF.md
  Expected Git blob: `3d473e81c158e45c923a1177e71701c40ac477c5`.

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

The verifier itself needs only the Python standard library. It rechecks all seven immutable Git blob hashes before using the data. An input is accepted only when its exact source bytes match the published hash.

## Checks and scope

The verifier checks the seven immutable Git blob hashes and exact original source127 g-b identity; the five possible high-P kernel characters; every changed internal channel and endpoint vanishing; the representation tests used to identify the projected Euler plane; original twist-one compatibility; and the numerical nested-projection rank bounds.

The proof separately supplies the actual connection, coherent-image, saturation, dual-sequence and independence arguments. The fixed check does not evaluate a selected actual HM/source coefficient, parameter, point, derivative, matrix, instance rank, model or scan. No large computation is required. It does not claim exclusion of another source edge or of the whole stable label.
