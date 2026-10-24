# Reproduce the narrow triplet zero-defect result

Requires Python 3; the independent checker additionally requires SymPy (reviewed with 1.14.0).

Run from this directory:

    python verify.py
    python -O verify.py
    python verify-independent.py

The two author outputs agree byte-for-byte and perform 35 fixed checks. The independent checker uses assertions and explicitly rejects optimized execution, rather than silently skipping checks. Its saved normal output is VERIFY-INDEPENDENT.txt.

PROOF.md and REVIEW-INDEPENDENT.md contain the full conditional argument and hash-bound whole-proof review. INPUTS.json pins the two complete immutable source proofs. Fresh independently fetched source copies are retained and compared by the independent checker.

This packet proves original t=0, B=O(6)+A_std(-6), and deg L=-42 for the actual rank-four maximal (1,1) triplet quotient only. It does not exclude or realize that quotient or close the profile. No public write was performed by the proof worker.
