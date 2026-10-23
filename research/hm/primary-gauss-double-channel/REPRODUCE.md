# Reproduce the bounded check

Python3 with its standard library is sufficient. From this directory run:

    python verify.py
    python -O verify.py

Both must reproduce RESULT.json exactly and report the same check count. The verifier uses explicit RuntimeError conditions, not removable assert statements. Run `python verify.py --write` only to intentionally regenerate the frozen result.

INPUTS.json pins all eight complete originals by immutable public URL, byte count, SHA256 and Git blob SHA1. The checker validates all three identities for each input. characters.py checks tensor multiplication by W against the exact nine-class character values over Q(sqrt5); the symmetric-power recurrence then computes only finite representation identities through degree31. The fixed182 records are read, not re-enumerated. No actual HM/source coefficient, parameter, point, derivative, matrix, tensor, jet, instance rank or source scan is computed.

Passing arithmetic does not prove the geometric steps. PROOF.md supplies the actual top-kernel bound, saturated graph contradiction, and coefficient-space interpretation. REVIEW.md records a separate whole-proof and packet review. This packet does not claim rank-three coverage or profile(1,1) closure.
