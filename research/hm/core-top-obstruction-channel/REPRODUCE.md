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

The standard-library verifier checks the fixed nine-class character table, the universal balanced quotient identities, the two surviving invariant cohomology lines, and vanishing of every other invariant H1 summand. It performs no selected actual HM/source coefficient, point, parameter, jet, derivative, matrix or instance-rank evaluation. The orbit-divisor argument, actual-map cohomology functoriality and nonzero universal pairing require mathematical review; the bounded checks do not replace the proof.

Expected output:

```text
PASS: four immutable inputs; universal balanced quotient identities; two invariant cohomology lines; every other invariant H1 summand vanishes.
No actual HM/source coefficient, point, parameter, jet, derivative, matrix, or instance rank evaluated.
```
