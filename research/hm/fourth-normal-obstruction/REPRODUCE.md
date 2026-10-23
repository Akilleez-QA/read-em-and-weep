# Reproduction and scope

Publication consists of five files: PROOF.md, verify.py, INPUTS.json, REPRODUCE.md, and REVIEW.md. The five copied repository inputs are intentionally omitted. Reconstruct their exact immutable bytes before running the verifier.

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

The deterministic bounded verifier uses the nine abstract conjugacy classes of the binary icosahedral group with exact rational arithmetic in Q(sqrt(5)). It checks character orthogonality/completeness, A⊗V=P⊕D, A⊗A=1⊕A⊕D, the unique D cup channel, relevant dimensions, and the rank-nine degree-minus-twelve numerical contradiction. It checks no actual tensor coefficients, selected points, jets, derivatives, matrices, or instance ranks. Its explicit require checks remain active under python -O.

The verifier is not a substitute for the proof's geometry: multiplication injectivity, the Grauert–Mülich generic-line theorem, the actual Lie-cup identification, the nonzero Schur contraction, and the constant-subbundle argument are mathematical steps reviewed independently. The external theorem is stated precisely and linked in PROOF.md; it is not downloaded or executed by verify.py.

Expected output in both modes:

    PASS: five immutable inputs, nine abstract character classes, plane-cup channels, rank9 degree-12 contradiction arithmetic.
    No actual HM/source coefficients, points, jets, derivatives, matrices, or instance ranks evaluated.
