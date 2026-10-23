# Type II source126 joint-annihilator gate

This packet proves that the joint P-row rank is at least one independently
of Q compatibility. Conditional on compatibility of the full two-dimensional
negative-pencil radical, only four common-annihilator footprints remain:

| (r,epsilon,d) | restricted dimensions | restricted cokernel | quotient kernel/cokernel |
|---|---|---|---|
| (1,0,0) | 27→28 | P+D | D / 0 |
| (1,0,1) | 32→28 | P | 0 / 0 |
| (1,1,0) | 31→28 | D | D / P |
| (2,0,0) | 27→24 | D | D / P |

Only the second row admits acyclic quotient cancellation. In the last two,
the internal first symbol on the actual A kernel is a nonzero multiple of
binary-quadratic multiplication, rank three for every nonzero direction.
This does not contradict original first-symbol vanishing, because the
internal D cokernel maps to zero in the original P cokernel.

No row occurrence, source exclusion, or catalogue-pair decrease is asserted.
PROOF.md supplies the argument, INPUTS.json pins nine public originals,
and verify.py runs 129 exact checks normally or under python -O.
The synthetic tests are not actual HM matrices or source realizations.
