# Canonical radical filtration in necessary type III

Conditional on type III from PR1127, the radical image equals its common annihilator in the canonical rank15 complement. It is a saturated rank6, degree−18 subbundle with type V O(-2)⊕V O(-4). The rank9 quotient has type V O(-2)⊕2V O(-4), and their extension is nonsplit despite the algebra radical having square zero.

- [Proof](PROOF.md)
- [Verifier](verify.py), standard-library exact polynomial matrices
- [Expected result](RESULT.json): 68 explicit checks
- [Pinned input manifest](INPUTS.json)

Reproduce with `python verify.py` and `python -O verify.py`; compare each output byte-for-byte with RESULT.json. No actual source instance or parameter sampling is performed. This does not select or eliminate type III, establish positive/Q/Gauss compatibility, or complete the original proof repair.
