# Reproduction

The publication consists of PROOF.md, INPUTS.json, verify.py, REPRODUCE.md, and REVIEW.md. The six copied immutable originals are omitted. Reconstruct them before running the verifier.

From this package directory, with an authenticated local clone of Akilleez-QA/read-em-and-weep containing the six commits, run:

```sh
export HM_REPO=/path/to/read-em-and-weep
python3 - <<'PY'
import json, os, pathlib, subprocess
out=pathlib.Path('audit-inputs')
out.mkdir(exist_ok=True)
for item in json.loads(pathlib.Path('INPUTS.json').read_text()):
    data=subprocess.check_output(['git','-C',os.environ['HM_REPO'],'show',item['ref']+':'+item['path']])
    (out/(item['key']+'.md')).write_bytes(data)
PY
python3 verify.py
```

Fetch missing named commits through the repository's authorized Git access if necessary. INPUTS.json also supplies each immutable GitHub source URL. Preserve the original bytes: verify.py authenticates the Git blob, including terminal newlines, before reporting success.

The standard-library verifier checks the fixed nine-class character ring, the current monad target decomposition, and exactly the21 previously published abstract rows with both source and target characters. It applies the new necessary tests and verifies the nine survivors and unique extension-capable row9. It does not evaluate an actual HM differential or any selected source coefficient, point, parameter, jet, derivative, matrix, or instance rank. The Koszul, nonsplit Leray, duality, and ampleness arguments require mathematical review of PROOF.md; the bounded checks do not replace that proof.

Expected output:

```text
PASS: six immutable inputs; nine abstract character classes; current monad target; 21 fixed rows with both exact characters.
Surviving rows: [7, 9, 10, 12, 14, 15, 17, 18, 20] ; possible invariant extension and rank-one sigma: [9]
No actual HM/source coefficients, points, jets, derivatives, matrices, or instance ranks evaluated.
```
