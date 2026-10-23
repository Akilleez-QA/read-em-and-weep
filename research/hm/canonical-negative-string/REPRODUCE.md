# Reproduction

The publication consists of PROOF.md, INPUTS.json, verify.py, REPRODUCE.md, and REVIEW.md. The four copied immutable originals are omitted. Reconstruct them before running the verifier.

From this package directory, with an authenticated local clone of Akilleez-QA/read-em-and-weep containing all four named commits, run:

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

The standard-library verifier uses exact arithmetic on nine fixed character classes. It checks the current-monad Euler identity for F(3), the symmetric-square section character, symmetric multiplication channels, residual representation dimensions and degree balances. It authenticates all four immutable originals before reporting success. Both `python3 verify.py` and `python3 -O verify.py` must pass.

The computation neither evaluates a monad differential nor substitutes for symmetric-square exhaustion, the Koszul joint-kernel argument, actual ring commutativity, or the inherited kernel diagrams. No selected actual HM/source coefficient, point, parameter, jet, derivative, matrix or instance rank is evaluated; no source-pair scan is performed. The proof and independent review supply those geometric arguments.

Expected output:

```text
PASS: four immutable originals; current F3 Euler and even B5 sections; symmetric string characters; six quintic channels; weighted 49-to-32 degree balances.
No selected actual coefficient, point, parameter, jet, derivative, matrix, instance rank, source-pair scan or large computation evaluated.
```
