# The two fourth square channels have a C5 detection filtration

This addendum supplements the frozen FOURTH-BOCKSTEIN-AFTER-ACTUAL-THIRD-VANISHING.md. It gives an exact detection filtration, not an actual fourth-obstruction value.

## Exactly what a C5-square test can detect

Let E be the twelve-point C5 orbit on the square parameter line, with invariant equation Delta12. There is an exact representation sequence

    0 -> Delta12 Sym^8 W -> Sym^20 W -> H0(O_E(20)) -> 0.

Here Sym^8 W=P4+D5 and the quotient is 1+A+V+D5. Consequently evaluation on E detects precisely ONE of the two equivariant fourth square channels. Its kernel is the unique D5 subspace in Delta12 Sym^8 W.

At a C5 square a=t^2, the direction has weight2 and the actual second-symbol cokernel has weight8. A fourth symbol has direction weight8, so only the weight0 input h=X^2Y^2 can contribute. This differs from the cubic detectable input X^4. One zero fourth fiber at this orbit would therefore remove only one square coefficient, not both.

If that coefficient vanishes, the remaining square channel is Delta12 times the unique D5 inclusion into Sym^8 W. The latter has no common zero: a common divisor would be G-invariant, but a nonempty invariant divisor on the icosahedral line has degree at least12, exceeding8. Hence the remaining channel is basepoint-free off E. A further full-fiber zero at any square direction outside E would then force both square channels to vanish. These are detection statements, not actual fourth vanishing results.


Run verify_fourth_square_c5_detection_filtration.py. Only abstract representation arithmetic and invariant-divisor geometry are used; no actual coefficient or matrix evaluation occurs.
