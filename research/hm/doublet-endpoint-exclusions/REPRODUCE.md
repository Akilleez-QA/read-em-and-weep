# Reproduction

Run from this directory:

    python3 verify.py > /tmp/doublet-normal.json
    python3 -O verify.py > /tmp/doublet-optimized.json
    cmp /tmp/doublet-normal.json /tmp/doublet-optimized.json
    cmp /tmp/doublet-normal.json RESULT.json

Python standard library only. Every check raises explicitly, not through assertions. Immutable originals and their complete provenance are in INPUTS.json. The historical JSON is read for exact labels only; its enumeration is not rerun. Universal character and integer identities support the written geometric proof and do not replace it. No actual-instance experiment occurs.

Independent implementation (separate results):

    python3 independent/independent_check.py > /tmp/doublet-independent.json
    python3 -O independent/independent_check.py > /tmp/doublet-independent-O.json
    cmp /tmp/doublet-independent.json /tmp/doublet-independent-O.json
    cmp /tmp/doublet-independent.json independent/RESULT.json

The independent review is in independent/REVIEW.md, with its own complete source manifest and unchanged checker. Only relative publication paths and the production-output location in the review were adapted.
