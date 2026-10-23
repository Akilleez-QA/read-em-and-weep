# Reproduction and evidence boundary

## Obtain the exact immutable inputs

The focused publication includes the proof, review, verifier, this reproduction note, and `audit-inputs/manifest.json`. It does not duplicate the seven already-public input files. Before running the verifier, save the exact file contents from the following immutable GitHub sources to the listed paths. Save the underlying source text, not the GitHub HTML page. The manifest records the same commit, repository path, Git blob hash, and verified source URL for each file.

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

- `audit-inputs/PR828.md`: https://github.com/Akilleez-QA/read-em-and-weep/blob/ae077cbe42d65cde27d65ce88923dc35851b6952/research/hm/profile11-horizontal-quotient-exclusion/HORIZONTAL-CONSTANT-QUOTIENT-EXCLUSION.md
  Expected Git blob: `6b43295c16eda2abd79e9d3c774d4d57139e1ff7`.

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

## Checks and limitations

The script performs a small fixed calculation in the abstract representation ring of the binary icosahedral group, exact original-catalog reads, rank/degree arithmetic, and Git-blob integrity checks. It does not read or evaluate any actual HM/source coefficients, parameters, points, derivatives, matrices, or instance ranks, and performs no source scan or large computation.

The mathematical argument is in PROOF.md. The independently written REVIEW.md binds its conclusion to exact proof and verifier SHA256 hashes. The verifier is not a replacement for the actual-connection and coherent-lattice arguments and is not Lean certification. The independent reviewer ran it against all seven exact files; those files need not be duplicated in this focused publication.

Only the common-divisor-twelve high-P branch in the four exact source127 tuples displayed in PROOF.md is excluded. The basepoint-free branch remains open in each of those edges. No whole-source decrement, whole-label decrement, current compatible-pair count, or global theorem completion is asserted.
