# Reproduction and evidence boundary

The focused publication consists of PROOF.md, REVIEW.md, verify.py, this note, and audit-inputs/manifest.json. It does not duplicate the nine already-public input files.

## Obtain the exact inputs

Save underlying source bytes, not GitHub HTML, at these destinations. The manifest records the same immutable URLs and Git blob hashes.

- `audit-inputs/ACTUAL.md`: https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md
  Expected Git blob: `b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3`.

- `audit-inputs/STRICT-TOP.md`: https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md
  Expected Git blob: `d7506dae49b4be43230450c4132bd5db91f137ef`.

- `audit-inputs/pairs.json`: https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/one-one-endpoint-necessary-pairs.json
  Expected Git blob: `fe0afa410d89340d3082dc814277f89fbb582c19`.

- `audit-inputs/frontier.json`: https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/rank-three-quotient-frontier-144.json
  Expected Git blob: `8b5971092f9ef762584912609fd5e9301c4e271d`.

- `audit-inputs/PR802.md`: https://github.com/Akilleez-QA/read-em-and-weep/blob/e484640a6565c278321bf6557860262c1ac1b7df/research/hm/profile11-o16-constant-span-exclusion/PROOF.md
  Expected Git blob: `98a1bd6123e148476da0b997d879aecbf885ec97`.

- `audit-inputs/PR796.md`: https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md
  Expected Git blob: `46a0de762000f21182f6d3168f3ecfd63adaf75f`.

- `audit-inputs/PR859.md`: https://github.com/Akilleez-QA/read-em-and-weep/blob/6129e92a26572779003f3295227f688b77ed881c/research/hm/profile11-o16-high-p-divisor/PROOF.md
  Expected Git blob: `79ec9cd555997cb9e3b8dc76f3b64fa3f836ad2e`.

- `audit-inputs/PR867.md`: https://github.com/Akilleez-QA/read-em-and-weep/blob/b2a12c98bc162062a938b7a7a6a90ab45786e340/research/hm/profile11-o16-cdf-kernels/PROOF.md
  Expected Git blob: `76a6bd75b77232af222ccb91555499b4a4437311`.

- `audit-inputs/PR870.md`: https://github.com/Akilleez-QA/read-em-and-weep/blob/3a05d057a12d24d62bf3c8e0e96fa778a4022ad5/research/hm/profile11-source127-cf-exclusions/PROOF.md
  Expected Git blob: `cfc219e5ce5c0658c484bfef21c3c90bd2d45468`.

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

The verifier itself needs only the Python standard library. It rechecks all nine immutable Git blob hashes before using the data. An input is accepted only when its exact source bytes match the published hash.

## Checks and limitations

The verifier uses only Python standard-library exact abstract representation arithmetic, original-catalog reads, small fixed rank/degree checks, and Git blob integrity checks. It performs no selected actual HM/source coefficient, parameter, point, derivative, matrix or rank evaluation and no selected model, source scan or large computation.

The independent review binds the exact proof and verifier hashes. The verifier is not a substitute for the written actual-connection, coherent-image and saturation arguments. The result leaves one explicit internal scalar-row branch and does not claim a whole-source exclusion, realizability, or a frontier-count change.
