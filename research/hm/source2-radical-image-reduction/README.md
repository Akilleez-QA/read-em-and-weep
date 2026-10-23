# Source2 radical-image reduction

Conditional on a nonzero invariant-product-compatible radical line, every
non-V direction permits a genuine 41-to-37 -> 32-to-28 two-term reduction
preserving formal cohomology and the entire t-adic Bockstein sequence.
The exceptional mixed direction changes the quotient middle dimension
from36 to42, not its endpoint reduction.

The pure V alternative instead forces im(j2)=ker(Q)_D and
ker(j4)=im(Q). Its36-to-33 quotient has rank29, kernelA+P and cokernelP;
it is explicitly not cohomologically equivalent to the original complex.

Read PROOF.md for the complete conditional argument. INPUTS.json and inputs/
freeze seven published dependencies. No existence, scalarity, source cut,
pair cut, actual-source evaluation or completed repair is asserted.

## Reproduce

Python3 and SymPy are required (verified with SymPy1.14.0).

    python verify.py
    python -O verify.py

Both produce the same RESULT.json content:981 exact bounded checks.
The synthetic block models verify universal cancellation identities and a
negative control, not actual HM data. Written geometric dependencies remain
conditional inputs, not proof-assistant certifications.
