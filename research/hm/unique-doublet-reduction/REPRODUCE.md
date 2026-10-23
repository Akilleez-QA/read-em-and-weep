# Reproduction

The publication consists of PROOF.md, INPUTS.json, verify.py, REPRODUCE.md, and REVIEW.md. The copied immutable original is omitted. Reconstruct it before running the verifier.

From this package directory, with an authenticated local clone of Akilleez-QA/read-em-and-weep containing the named commit, run:

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

The standard-library verifier checks the fixed nine-class character ring, the unique W source and its two allowed target channels, the two universal block types, and residual rank, degree, section and Ext identities. It does not select or evaluate any actual HM/source coefficient, point, parameter, jet, derivative, matrix or instance rank. Subbundle saturation, universal tensor Euler normalization and the inherited actual maps require mathematical review of PROOF.md; the checks do not replace that proof.

Expected output:

```text
PASS: immutable PR1002 input; unique-doublet support; universal block types; residual rank, degree, section and Ext identities.
No actual HM/source coefficient, point, parameter, jet, derivative, matrix, or instance rank evaluated.
```
