# Reproduction

The publication consists of PROOF.md, INPUTS.json, verify.py, REPRODUCE.md, and REVIEW.md. The two copied immutable originals are omitted. Reconstruct them before running the verifier.

From this package directory, with an authenticated local clone of Akilleez-QA/read-em-and-weep containing both named commits, run:

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

The standard-library verifier checks fixed abstract A/shear channels, every W' target-support exclusion, tensor Euler identities, and universal quotient/final rank-degree balances. It does not select or evaluate actual HM/source coefficients, points, parameters, jets, derivatives, matrices or instance ranks. Forced nonvanishing, the unique shear, saturation and the actual quotient chain require mathematical review of PROOF.md; the bounded checks do not replace the proof.

Expected output:

```text
PASS: two immutable inputs; forced A normalization channels; Wprime support exclusion; all universal quotient and final target identities.
No actual HM/source coefficient, point, parameter, jet, derivative, matrix, or instance rank evaluated.
```
