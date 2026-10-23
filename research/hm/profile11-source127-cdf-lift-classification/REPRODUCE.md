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

- `audit-inputs/OPEN-FAMILY.md`: https://github.com/Akilleez-QA/read-em-and-weep/blob/7c7f25911ae1df3590c2b4ffe541c21bae9b1574/research/hm/profile11-source127-cdf-open-family/PROOF.md
  Expected Git blob: `659a90911244172b222f366d8b7dea9b88e88814`.

- `audit-inputs/NORMAL-FORM.md`: https://github.com/Akilleez-QA/read-em-and-weep/blob/1528ff8ea56b21e03f7501a962bdaa6728a75904/research/hm/profile11-source127-cdf-normal-form/PROOF.md
  Expected Git blob: `718b5245560a84568492874bab8d8c34730e8319`.

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

The verifier authenticates the four original inputs, the PR876 open family, and the PR920 canonical constant tower. It checks exact source identity, the scalar and quartic shear-space dimensions, the principal-parts quotient Euler identity, the absent D target in C10, fixed exceptional-channel multiplicities, and the universal monic falling-factorial identity underlying the Wronskian proof.

The proof and independent review separately verify the precise actual dependency interface, the jet quotient convention, generic jet surjectivity, zero kernel of the quartic shear map, regular factorization of the residual lift through F, scalar removal, exact two-exceptional-line distinction, and uniqueness of the family parameter under the stated equivalence. The classification is of constant-bundle inclusions up to G-equivariant constant ambient isomorphism over the fixed base, with source reparametrization. It is not a moduli-scheme assertion or an extension of these isomorphisms to additional fixed HM data. No actual parameter or source instance is selected or evaluated, and no source or label is excluded.
