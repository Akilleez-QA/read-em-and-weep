# Reproduction and evidence boundary

The focused publication consists of PROOF.md, REVIEW.md, verify.py, this note, and audit-inputs/manifest.json. It does not duplicate the eight already-public inputs.

## Obtain exact immutable inputs

Save underlying source bytes, not GitHub HTML, from these immutable sources to the listed destinations. The manifest records the same exact Git blob hashes.

- `audit-inputs/SOURCE-BRIDGE.md`: https://github.com/Akilleez-QA/read-em-and-weep/blob/af0e03d26da5e47d18ae732291aca46f4d448dc5/research/hm/source2-first-constant-block/PROOF.md
  Expected Git blob: `0641ffadf54324d5520aec89767658e938815223`.

- `audit-inputs/GAUSS.md`: https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md
  Expected Git blob: `303c6927265296440470b9dd4015fe6e8d55ca4d`.

- `audit-inputs/UNIFORM.md`: https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/UNIFORM-TWIST-FOUR-FIVE-HYPERPLANE-COHOMOLOGY.md
  Expected Git blob: `d34434e3bffe4e9de4a6aaa4d5e469336b12d5d0`.

- `audit-inputs/FULL-MODULE.md`: https://github.com/Akilleez-QA/read-em-and-weep/blob/f4a73af666900ad2cb34a756d24b88e19dd6feaa/research/hm/negative-truncation-extension/PROOF.md
  Expected Git blob: `2ba0a7eee6ef2eb5413683e85618d7902dca3970`.

- `audit-inputs/FULL-FAITHFUL.md`: https://github.com/Akilleez-QA/read-em-and-weep/blob/e103e25456897a1123f9636eb20080e8641ce66a/research/hm/profile11-degree28-pencil-algebra/PROOF.md
  Expected Git blob: `e18035dcceb1c7e0d0d4356ee578937d3172390b`.

- `audit-inputs/ACTUAL.md`: https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md
  Expected Git blob: `b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3`.

- `audit-inputs/NORMAL-FORM.md`: https://github.com/Akilleez-QA/read-em-and-weep/blob/1528ff8ea56b21e03f7501a962bdaa6728a75904/research/hm/profile11-source127-cdf-normal-form/PROOF.md
  Expected Git blob: `718b5245560a84568492874bab8d8c34730e8319`.

- `audit-inputs/CLASSIFICATION.md`: https://github.com/Akilleez-QA/read-em-and-weep/blob/91af637305fd0a76b4e68a889b2a2cb59f8f7067/research/hm/profile11-source127-cdf-lift-classification/PROOF.md
  Expected Git blob: `6742093385b0aefc7b678151d90e7966bf4effa6`.

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

The verifier itself needs only the Python standard library. It rechecks all eight immutable Git blob hashes before using the data. An input is accepted only when its exact source bytes match the published hash.

## Checks and scope

The verifier authenticates the three original actual-sheaf notes, the exact simultaneous source bridge, the weaker full-faithfulness theorem, full-module Euler rigidity, and the two c-d-f normal-form/classification proofs. It checks all omitted-block Hom vanishings, the one-dimensional radical Hom space, the invariant-free degree26 obstruction, exact covariant cohomology block characters and dimensions, the unique radical P-channel, and the Clebsch-Gordan identities for the complete radical rank triple. These are small fixed universal character checks, not actual-source evaluations.

The proof and independent review separately establish preservation of all actual kernels by singular constant maps, exact endomorphism algebra and multiplication, covariant full faithfulness and simultaneous identification with both fixed actual pencils, the scalar full-module restriction image, the conditional positive-quadratic/submodule certificate, and the natural acyclic/duality argument proving radical ranks (0,8,4). The three-dimensional scalar quotient is not an Ext group, an algebra quotient, or an evaluated compatibility rank. Neither the radical P-channel value nor a forced full-module lift is asserted. No source or stable label is excluded; no ledger count is changed.
