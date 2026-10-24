# Rank-four diagonal plateau exclusion

Conditional on the five pinned actual-geometric originals, the actual ordered maximal rank-four plateau `(k,l)=(2,2)` is impossible.

The proof retains all length-twelve derivative torsion and all five center-even stabilizer characters. Nine forced degree cases reduce by exact equivariant identities and four justified cohomology inequalities to 359 formal tuples. Torsion-safe horizontal-subbundle tests exclude 187. The remaining 172 force the upper annihilator to have rank five, degree -22 and generic second-fundamental rank one; the complete rank-one invariant defect identity then requires 18 to equal zero or a number at least 48.

This does not claim a rank-five lower bound, any other profile exclusion, square surjectivity, full-adjoint invertibility, or repair of the original theorem. No actual HM coefficients, parameters, jets, matrices, instance ranks, local-model experiments or historical candidate enumeration are used.

## Reproduce

- `python3 verify.py`
- `python3 -O verify.py`
- `python3 test_controls.py`

The first two reproduce `RESULT.json`; the third reproduces `CONTROLS.json`. All scripts locate their data relative to their own path and may be run from a different working directory. Python standard library only; no assertion-dependent checks.

`PROOF.md` contains the geometric ledger, both actual Euler presentations, all torsion signs/twists, the finite-domain coverage proof and the final complete-flag obstruction. `INPUTS.json` pins and authenticates all five originals. `RESULT.json` contains every horizontal rejection witness and every retained final tuple. The checker compares two independently implemented splitting-domain enumerations and checks physical McKay products against exact conjugacy-class characters over Q(sqrt5).

An exploratory cohomology inequality was rejected during independent review and removed before this packet was frozen. The proof explicitly avoids assuming that H1 of the upper endpoint surjects onto H1 of Q*. No published conclusion rests on that invalid inequality.
