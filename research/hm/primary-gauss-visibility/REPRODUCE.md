# Reproduce the primary visibility slice

Run from this directory:

    python verify.py
    python -O verify.py

Both commands authenticate all seven complete public inputs, check the tensor-by-W table independently against the exact binary-icosahedral character values, derive the cubic-section characters of the fixed182 original quotient rows, and require byte-for-byte agreement with RESULT.json. The first computation of the deterministic result used `python verify.py --write`.

The geometric proof is PROOF.md. The executable checks its bounded universal character consequence and source integrity, not formal correctness of the geometric arguments. No historical enumeration is rerun. All generated list entries are formal quotient splittings from the pinned historical list, not evaluated HM/source instances.

The first independent geometric review is ../REVIEW-NEAR-TOP.md. The finalized whole-packet review, when present, is REVIEW.md in this directory. A review of the lemma alone is not represented as review of the bounded cut.
