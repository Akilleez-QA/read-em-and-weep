# Lower dual-cubic images in ordered rank-four (3,1)

Conditional necessary classification, not profile closure:

- Rank-three image: saturated V O(1), with first quotient V O + O(2), O(4), or O(6).
- Rank-two image: saturated W' O(2) or W' O(4), with ten first-quotient possibilities.
- These branches force only the last plateau defect to vanish. The complete case ledger retains 37 positive-defect rows; the torsion-partition ledger retains 83.

The actual inverse-image construction, exact torsion sequences and nonsplit-extension checks are in PROOF.md. Rank one is not analyzed, and no actual instance or historical source enumeration is evaluated.

Reproduce using the Python standard library:

    python3 verify.py
    python3 -O verify.py

Both outputs must match RESULT.json, independently of working directory. INPUTS.json pins all six complete originals. QUOTIENTS.json, CASES.json, TORSION-LEDGER.json and ENDPOINT-EXCLUSIONS.json are readable certificate projections.

All geometric claims remain conditional on the original actual-bundle and primary-module premises. Source hashes authenticate bytes, not those premises.
