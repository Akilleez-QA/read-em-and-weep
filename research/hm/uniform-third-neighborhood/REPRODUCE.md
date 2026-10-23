# Reproduction and scope

Publication consists of five files: PROOF.md, verify.py, INPUTS.json, REPRODUCE.md, and REVIEW.md. The four copied repository inputs are intentionally omitted. Reconstruct their exact immutable bytes before running the verifier.

In a clone of Akilleez-QA/read-em-and-weep with the commits in INPUTS.json available, run from the directory containing this package:

```sh
export HM_REPOSITORY=/absolute/path/to/read-em-and-weep
python3 - <<'PY'
import json, os, pathlib, subprocess
root = pathlib.Path('.')
out = root / 'audit-inputs'
out.mkdir(exist_ok=True)
for item in json.loads((root / 'INPUTS.json').read_text()):
    data = subprocess.check_output([
        'git', '-C', os.environ['HM_REPOSITORY'], 'show',
        item['ref'] + ':' + item['path'],
    ])
    (out / (item['key'] + '.md')).write_bytes(data)
PY
python3 verify.py
python3 -O verify.py
```

Fetch missing commits from the named repository before using git show. Alternatively retrieve each INPUTS.json URL at its exact immutable ref using GitHub's raw-file interface, preserving bytes. The verifier authenticates each input with the Git blob formula SHA1("blob " + decimal byte length + NUL + bytes), so newline changes are detected.

The deterministic bounded verifier uses the nine abstract conjugacy classes of the binary icosahedral group with exact rational arithmetic in Q(sqrt(5)). It checks character orthogonality/completeness, the unique dual-y cup channel, vanishing of the equivariant Hom determining the HN complement, the ordinary Ext differences, and all displayed ranks/degrees. It authenticates four original Git blobs. No actual selected coefficients, points, jets, derivatives, matrices, or instance ranks are evaluated. Explicit require checks remain active under python -O.

The verifier does not replace the geometry: actual identification with the nonzero cup, fiberwise exactness of the dual-y sequence, finite-neighborhood eigensheaves, cohomology and derived base change, and distinction between cohomology splitting and bundle splitting are independently reviewed mathematical steps.

Expected output in both modes:

    PASS: four immutable inputs; nine abstract character classes; unique dual-cup and HN channels; all Ext/rank/degree identities.
    No selected actual HM coefficients, points, jets, derivatives, matrices, or instance ranks evaluated.
