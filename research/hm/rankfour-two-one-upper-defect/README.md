# Ordered rank-four (2,1): upper-defect restriction

**Theorem:** the upper adjacent derivative defect δ2 of an actual maximal ordered rank-four (2,1) plateau is 0 or12. This is not a closure of the (2,1) profile.

The seven high-defect numerical cases give31 exact/cohomological tuples, then26 horizontal contradictions and five literal residual tuples. The pinned actual four-source cubic H1 bound excludes four. A complete rank-one flag forces a rank11 degree−12 subbundle of E, contradicting H0(E(1))=0, in the last case.

- `PROOF.md`: full geometric and finite-domain proof, including nonreduced torsion layers.
- `verify.py`: standalone exact universal arithmetic checker; no external dependencies.
- `RESULT.json`: canonical output with every horizontal witness and the exact residual boundary.
- `INPUTS.json`, `inputs/`: six immutable complete original sources, with byte/hash/ref authentication.
- `test_controls.py`, `CONTROL-RESULT.json`:24 genuine verifier mutations, rejected in normal and optimized subprocesses.
- `REPLAY.json`: normal, optimized and outside-directory output agreement.
- `MANIFEST.json`, `SHA256SUMS`: frozen artifact hashes.

Run `python verify.py` and `python test_controls.py` from any working directory. No actual HM coefficients, parameter values, jets, matrices or ranks are evaluated. All arithmetic concerns universal representation rings and abstract splitting possibilities. The proof does not use the invalid general implication H1(subbundle)>=H1(ambient), and retains all applicable torsion signs and twists.
