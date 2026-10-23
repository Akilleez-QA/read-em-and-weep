# Compatible W choices do not tune the fourth-neighborhood scalar

For fixed actual lower data and two already compatible full global choices
(W,E), the actual cone boundary identifies their difference with a unique
global cone adjoint gN. The global physical coefficient theorem kills its
entire weight-four coefficient. Thus all seven compatible equivariant
family directions are invisible, including the four D5-family slots.

The conclusions are linked but distinct:

- The authenticated physical source row has the same value on both full
  corrected sources. The complete weight-sixteen affine data remain fixed.
- The scalar norms agree on actual 4Q, so PR815's entire rho on Q agrees.
  This is not ambient or fifth-order norm invariance.
- The physical row descends through cone restriction of certified exact
  sources D=dC^0_4, since it annihilates D intersect qC^1_2. This is not
  an extension to arbitrary ambient S and does not bypass membership.

PR866's thirteen-dimensional coefficient blind space is not contradicted:
its sections need not lift to global actual cone adjoints, whereas these
compatible variations do. Changing W cannot absorb a nonzero mixed-row
normalization defect. The actual row, the full lower projection y, and
their normalization comparison remain to be supplied.

## Reproduction

    python verify_compatible_torsor.py
    python -O verify_compatible_torsor.py

Both runs report 66 exact q-adic/character/weight checks and eight negative
controls. In particular a formal next-order coefficient remains nonzero,
even with the lower square condition imposed, preventing promotion to
ambient norm invariance. The diagnostics do not prove the geometric inputs
or evaluate any actual HM coefficients, points, matrices, source ranks,
physical rows or calibrations.

PROOF.md contains the written theorem and strict domain/order boundaries.
REVIEW.md binds independent review to final proof and checker bytes.
SOURCE-MANIFEST.json authenticates seven immutable sources.
FINAL-MANIFEST.json and SHA256SUMS record the frozen package.

PR889 and PR894 are unchanged. No publication or proof-assistant
formalization was performed by this worker.
