# Reproduction

The publication consists of PROOF.md, INPUTS.json, verify.py, REPRODUCE.md, and REVIEW.md. The four copied immutable originals are omitted. Reconstruct them before running the verifier.

From this package directory, with an authenticated local clone of Akilleez-QA/read-em-and-weep containing the four commits, run:

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

The standard-library verifier checks the fixed nine-class character ring, the current exterior monad target, universal Koszul dimension arithmetic, and exactly the nine previously published abstract rows. It verifies the invariant bound filter and seven survivors. It does not evaluate an actual HM differential or any selected source coefficient, point, parameter, jet, derivative, matrix, or instance rank. The Koszul, symmetric-square monad, nonsplit Leray, and duality arguments require mathematical review of PROOF.md; the bounded checks do not replace that proof.

Expected output:

```text
PASS: four immutable inputs; fixed abstract character identities; nine-row invariant filter.
Surviving rows: [9, 10, 14, 15, 17, 18, 20]
No actual HM/source coefficients, points, parameters, jets, derivatives, matrices, or instance ranks evaluated.
```
