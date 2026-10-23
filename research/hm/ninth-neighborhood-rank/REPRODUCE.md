# Reproduction and scope

Publication consists of five files: PROOF.md, verify.py, INPUTS.json, REPRODUCE.md, and REVIEW.md. The three copied repository inputs are intentionally omitted. Reconstruct their exact immutable bytes before running the verifier.

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

The deterministic bounded verifier authenticates the three exact original Git blobs and checks the universal relative-dualizing exponents, the Serre comparison twist, inversion parity, and every displayed rank/degree identity. It performs no coefficient, point, jet, derivative, matrix, or instance-rank evaluation. Explicit require checks remain active under python -O.

These arithmetic checks do not establish the geometric rank theorem by themselves. The mathematical proof and independent whole-proof review establish finite/global section comparison, flat Gorenstein duality, the actual square-section restriction, cohomology/base change, and naturality identifying the actual image. No executable dependency beyond the Python standard library is required.

Expected output in both modes:

    PASS: three immutable inputs; dualizing and Serre twists; parity; ranks/degrees of source, target, kernel, image, and cokernel.
    No actual HM coefficients, points, jets, derivatives, matrices, or instance ranks evaluated.
