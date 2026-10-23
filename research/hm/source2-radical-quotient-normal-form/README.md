# Regular radical-image quotient normal form

For any source2 radical direction other than pure V or the unique exceptional
mixed direction, the actual fixed negative-pencil quotient has isomorphism
type N0 + N8 + (V+D)[2]. This requires no Q-compatibility. If compatibility
holds, it describes the negative arrows of the reduced obstruction complex,
not a decomposition respected by Q.

PROOF.md proves the new arrow-level identification from the three frozen
public inputs in INPUTS.json and inputs/. No actual instance is selected.
The original source and four-pair frontier are not excluded or resolved.

Reproduce with Python3 and SymPy (verified with SymPy1.14.0):

    python verify.py
    python -O verify.py

Both yield RESULT.json:745 exact bounded checks.
