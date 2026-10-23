# Source2 zero-arrow reduction

Conditional on a regular non-V compatible radical line, the reduced negative
pencil has an intrinsic zero-arrow space Z=V+D. The actual invariant product
has exactly two possible restriction ranks on it:

- Rank8: the obstruction complex reduces further to24-to-20, preserving all
  t-adic Bocksteins of the original41-to-37 family.
- Rank3: split off a permanent D kernel and retain an active24-to-25 complex.
  Every37-minor vanishes identically on the entire affine negative-quadratic
  perturbation family Q+Sym²W. Its original41-to-37 map cannot be onto there.

Neither rank is selected or evaluated. These are conditional restrictions,
not a proof repair, source/pair cut, or assertion about other quadrics.
PROOF.md supplies the full argument and its scope. Five public immutable
proofs are frozen in INPUTS.json and inputs/.

## Reproduce

Python3 and SymPy are required (verified with SymPy1.14.0).

    python verify.py
    python -O verify.py

Both produce RESULT.json:244 exact bounded checks. Synthetic controls only;
no actual source-instance data is used. Independent review is separate from
these reproducible checks and is not proof-assistant certification.
