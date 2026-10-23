# Reproduction and precise scope

The focused publication consists of PROOF.md, REVIEW.md, verify.py, this note, and audit-inputs/manifest.json. The four already-public proof inputs are not duplicated.

## Obtain exact inputs

Save the underlying source bytes, not GitHub HTML, from each immutable source into the indicated destination:

- `audit-inputs/ACTUAL.md`: https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md
  Expected Git blob: `b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3`.

- `audit-inputs/FULL-MODULE.md`: https://github.com/Akilleez-QA/read-em-and-weep/blob/f4a73af666900ad2cb34a756d24b88e19dd6feaa/research/hm/negative-truncation-extension/PROOF.md
  Expected Git blob: `2ba0a7eee6ef2eb5413683e85618d7902dca3970`.

- `audit-inputs/ALGEBRA.md`: https://github.com/Akilleez-QA/read-em-and-weep/blob/c6c25eaf0e5a67c27eee7c3ba4f000df55997692/research/hm/profile11-source127-cdf-pencil-algebra/PROOF.md
  Expected Git blob: `83f5aee293995257459229e6b323522224ce8f3d`.

- `audit-inputs/NEGATIVE-SQUARE.md`: https://github.com/Akilleez-QA/read-em-and-weep/blob/3d9e1f3949241a6b2bbb48781c056b72b7262dd7/research/hm/profile11-source127-cdf-negative-square/PROOF.md
  Expected Git blob: `bdcb7d5b14f7477bcd616e0e682fa5f45e250a5d`.

Alternatively, readers with the GitHub CLI and Python may fetch exact objects with this snippet from the publication directory. Repository authentication may be required.

```python
import base64
import hashlib
import json
import pathlib
import subprocess

root=pathlib.Path('.')
for entry in json.loads((root/'audit-inputs/manifest.json').read_text()):
    endpoint='repos/Akilleez-QA/read-em-and-weep/git/blobs/'+entry['git_blob']
    response=json.loads(subprocess.check_output(['gh','api',endpoint]))
    if response['encoding']!='base64':
        raise RuntimeError('Unexpected encoding')
    data=base64.b64decode(response['content'])
    header=b'blob '+str(len(data)).encode()+b'\0'
    if hashlib.sha1(header+data).hexdigest()!=entry['git_blob']:
        raise RuntimeError('Blob mismatch')
    (root/'audit-inputs'/entry['name']).write_bytes(data)
```

Then run:

    python3 verify.py
    python3 -O verify.py

The checker uses only the standard library and hardcodes the expected input hashes independently of the manifest. All checks remain active with Python optimization.

## What is checked

Exact arithmetic in Q(sqrt(5)) checks the fixed nine irreducible characters, their orthogonality and dimension-square completeness, the center-even representation list, the three possibilities for a dimension-three even representation, invariant bilinear-form multiplicities, and the existence of the abstract V+P projections used in the constructions. It checks fixed block and radical-character arithmetic. It performs no numerical matrix-rank test, parameter selection, actual-source evaluation, or large search.

The written proof separately establishes symmetry of the invariant forms, the faithful represented action, the exact quotient-support and cross-component criterion, and the three uniform formal constructions. Character multiplicities alone do not prove those statements. Independent mathematical review, not this checker, audits those derivations and the authenticated interfaces.

The formal maps are equivariant aggregate maps on Sym2(T_+) tensor N2. They keep the fixed negative pencil and its exact restricted relation/cokernel sequence unchanged, and satisfy aggregate generation and both known projected-surjectivity conditions. They are not asserted to factor through positive-linear multiplication, satisfy all mixed window squares, extend the actual HM module, or realize an actual source. This is a sharp limitation of the explicitly listed aggregate interface, not of all possible full-module information. No source, label, pair or count is removed.
