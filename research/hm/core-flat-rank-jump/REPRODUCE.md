# Reproduction

The publication consists of PROOF.md, INPUTS.json, verify.py, REPRODUCE.md, and REVIEW.md. The three copied immutable originals are omitted. Reconstruct them before running the verifier.

From this package directory, with an authenticated local clone of Akilleez-QA/read-em-and-weep containing all three named commits, run:

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

The standard-library verifier checks the fixed nine-class characters, all displayed low-degree channel exclusions, the one-dimensional extension space, and the complete evaluation characters at both proved splitting types. It does not evaluate or scan the auxiliary parameter. No selected actual HM/source coefficient, point, parameter, jet, derivative, matrix or instance rank is evaluated. Saturation on the full product, the nonzero extension, relative diagonal exactness and base change require mathematical review; these bounded character checks do not replace those arguments.

Expected output:

```text
PASS: three immutable inputs; saturated-channel character exclusions; nonzero extension test; both complete evaluation characters; degree identities.
No actual HM/source coefficient, point, parameter, jet, derivative, matrix, or instance rank evaluated. No auxiliary parameter scan performed.
```
