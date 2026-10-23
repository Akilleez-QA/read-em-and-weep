# Source126 invariant-product compatibility

The fixed negative-pencil algebra has two or three diagonal vertices and a two-dimensional square-zero radical. The actual canonical invariant positive product prevents every nontrivial vertex-subset projector from extending compatibly, including every radical shear. The remaining compatible algebra is exactly of the form C·1 ⊕ J_Q, where J_Q is a subspace of that radical and has dimension0,1,or2.

This is a new compatibility reduction, not a source exclusion or a completed proof repair. It changes neither the stable-label count nor the source-dual candidate count. It does not prove the compatible algebra scalar.

- PROOF.md: block reconstruction, exhaustive idempotent argument, universal image bounds and local-algebra consequence.
- verify.py:173 checks of authenticated inputs, fixed McKay characters, all14 nontrivial vertex subsets, and formal radical shears.
- INPUTS.json and inputs/: five immutable source files and their original Git blob hashes.
- RESULT.json: deterministic test output.

Reproduce with Python3:

    python verify.py
    python -O verify.py

Both runs produce identical results. There are no third-party Python dependencies. No actual HM coefficients, chosen parameters, points, derivatives, multiplication matrices or selected-instance ranks are evaluated. The actual invariant-product image is an explicitly cited pre-existing geometric theorem. These tests do not replace mathematical review or provide proof-assistant certification.

The independent review corrected an early hand-computed TypeI-X bound from26 to30; the final derivation and verifier both give30, still strictly below33. The final bounds are23 for F separations and30 for X/Y separations.
