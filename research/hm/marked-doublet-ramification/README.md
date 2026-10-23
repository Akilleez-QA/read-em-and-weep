# Marked doublet ramification

PROOF.md establishes the rank-one threshold4, rank-two saturation cutoff5, and the conditional unique-channel twelve-point defect for W'O(-3) mapping to O(-8)+W O(3). Both cutoffs have abstract equivariant sharpness controls. This is not a new source/profile exclusion or a completed proof repair.

Run `python verify.py` and `python -O verify.py`; compare the outputs to RESULT.json. The full pinned dependencies and their authenticated hashes are in INPUTS.json and inputs/. No non-standard Python packages or selected actual-instance computations are used.

The character calculations are bounded universal representation-ring tests. The independent finite A5 calculation verifies subgroup counts and possible cyclic stabilizer orders. The geometric arguments, including actual-source nonvanishing, saturation and the orbit divisor, are stated in PROOF.md with explicit dependency boundaries.

Independent review and authenticated public source responses are retained in independent/. Run `python independent/independent_check.py` and `python -O independent/independent_check.py`; both outputs match independent/RESULT.json.
