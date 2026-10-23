# Reproduce the bounded checks

Run with Python 3, using only the standard library:

    python verify.py
    python -O verify.py

Both must return the same PASS JSON recorded in RESULT.json. The verifier
uses explicit exceptions, not assertions. It authenticates the four full
source copies against their immutable Git blobs and SHA256 hashes.

The polynomial ring has four FORMAL variables: two entries of a universal
column and two of a universal row. Tensor tests use all 27 basis triples
of the abstract orthogonal three-space. Four 2-by-2 rational examples
certify universal sharpness; four small interface controls distinguish
the incidence alternatives. These are not HM/source instances or chosen
actual parameters. No large computation or scan is performed.

The written proof, not replay alone, supplies actual map identification,
scalar-arrow surjectivity, source hypotheses, and the canonical V_h
comparison. See REVIEW.md for the independent whole-proof review.
