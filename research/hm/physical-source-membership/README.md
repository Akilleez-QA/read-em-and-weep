# Supplied corrected-source membership: a sharp cohomological interface

The new theorem distinguishes existence of compatible polynomial lifts
from checking a supplied full source a(V-bZ)-qW. It assumes the canonical
Atiyah probe, the preceding full-family division for V, and coherent
equivariant polynomial families in the actual full global complex.

The exact dimensions have different meanings:

| Quantity | Dimension |
| --- | ---: |
| Raw cubic source coefficient module R | 50 |
| Cohomology family space Hom_G(R,M2), containing [W] | 34 |
| Raw cohomological obstruction space Hom_G(R,M4) | 30 |
| Quotient obstruction when W is allowed to be chosen | 3 |
| Compatibility obstruction for prescribed W and canonical b | 27 |
| Residual sector when supplied b also varies | 28 |
| Compatible W cohomology-family torsor | 7 |

The 27 scalar multiplicity slots split as 6 V + 9 P4 + 12 D5. All are
attainable as W varies through otherwise unrestricted closed equivariant
cubic families. Thus a smaller criterion needs an additional actual
restriction on W. A linear detector through PR889's ten-dimensional
trace-family space would miss at least seventeen of these directions,
IF such a detector were independently defined on the obstruction space.
No extension of eta outside its certified source domain is assumed.

The prior canonical factorization already gives existential polynomial
choices. That old fact is not rebranded as the new result. For a supplied
packet, actual comparison of b with b_can and verification of all remaining
W compatibility conditions remain necessary. No primitive, contraction,
source coefficient, point, matrix, rank or calibration is evaluated here.

## Reproduce

    python verify_source_membership.py
    python -O verify_source_membership.py

Both runs report 127 exact character/multiplicity checks and seven negative
controls. These are universal diagnostics, not Lean or an actual-HM test.
PROOF.md supplies the written argument. REVIEW.md binds independent review
to final proof and checker bytes. SOURCE-MANIFEST.json authenticates seven
immutable source copies, including the physical-central-inversion premise.
FINAL-MANIFEST.json records artifact hashes; SHA256SUMS checks the package.

PR889 and PR866 remain unchanged. No external publication was performed by
this worker. The exact next action is to authenticate the supplied closed
family W and certify its defect [a(V-b_can Z)]-q[W]=0 in the actual 27-slot
space, after the preceding V division and correction comparison are fixed.
