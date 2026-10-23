# Reproduction and review boundary

Run:

    python verify.py
    python -O verify.py

The checks use nine fixed abstract binary-icosahedral conjugacy classes, exact rational arithmetic in Q(√5), coordinate symmetric degrees two through eight, and the λ-ring formula displayed in PROOF.md. No actual HM multiplication map, source parameter, polynomial coefficient, point, matrix or instance rank is selected or evaluated.

The verifier checks character orthogonality/completeness, the exact square-class map, the exterior-square coordinate character, all nine Euler-character values, central parity, the two tensor identities for the 21-dimensional minimal factor and the genuine 25-dimensional complement. It does not replace the written proofs of the minimal factor criterion, actual cohomological concentration or the scope distinction at the mixed squares.

When audit-inputs/manifest.json and the five corresponding copied inputs are present, their Git blob IDs are authenticated exactly. Obtain each original from its manifest commit/path; retain its exact UTF-8 bytes. If those private audit copies are omitted, the abstract character checks still run, but they do not authenticate the source files. An independent reviewer must read the source proofs, not infer their claims from verifier success.

Expected character results:

- K4+ = 1+4A+2V+3P+3D, dimension46.
- K4− = 3Wp+3S+6T, dimension54.
- Minimal factor = 1+A+V+P+2D, dimension21.
- Unused complement = 3A+V+2P+D, dimension25.

All three constructions retain the fixed negative pencil and give positive-linear factors on this prescribed middle G-module. They do not retain the unknown actual positive factors or certify any mixed equation. In particular, the actual opposite-parity negative map and its A O(-6) kernel must not be replaced by a zero arrow when interpreting this conclusion.
