# The corrected fourth-square source is nonzero on the reduced cubic

## Result and limitation

For the uniform order-five detecting square input a=t²,h=X²Y², the actual corrected source

    [v_h−b ζ_a] in C/J

is NONZERO. Its Cminus projection is already nonzero. This is a value of the LOWER source, not of the fourth Bockstein: a nonzero source can still have zero value after the required next ambient division and multiplication.

The proof first identifies Cminus canonically on the reduced genus-four curve, then compares the explicit midpoint and Atiyah sections. All tensor parameters remain symbolic and nonzero. There is no actual-instance coefficient, matrix, rank test, or scan.

## 1. A canonical reduced-curve realization of Cminus

The actual double-cubic sequence and the proven nilpotent splitting are

    0 -> N8 -> M8 -> pi_*O_D(−2,12) -> 0,
    N8=O_L(4) ⊕ Wprime O_L(1).

The first summand is exactly the scalar/class(N) subbundle. Twist by O_L(−2). Since H0(Wprime O_L(−1))=H1(Wprime O_L(−1))=0 and H1(O_L(2))=0, one gets

    0 -> A -> H0(M8(−2)) -> H0(D,O_D(−2,10)) -> 0.

The ACTUAL global boundary quotient is H0(M8(−2))/A=Cminus. Hence there is a canonical equivariant isomorphism

    Cminus = H0(D,O_D(−2,10)).                         (1)

No isotypic splitting of the effective twelve-space is used. As a check, D has genus4, the line has degree24, and Riemann–Roch gives h0=21 and h1=0. Thus (1) has the already-established character V+2P4+2D5.

In particular, an absolute section vanishes as a Cminus class if and only if its restriction to the reduced D vanishes. The three scalar directions are exactly the global nilpotent layer in this twist.

## 2. The two actual sections

The absolute midpoint theorem gives the full uncorrected midpoint class as r_mid/(νg²). The absolute Atiyah theorem gives t(a)=aζ_a as r_t/g², where

    r_t=2k a ∂z(a f g).

On D this restricts to

    r_t/g²=2k a² f_z/g.                                (2)

The relative derivative f_z/g has the required line O_D(−2,6): under w=−1/z, f_z transforms by z^−1 on D and g by z^5. Thus multiplication by a² gives O_D(−2,10), as required by (1).

For this detecting input the actual canonical third correction is b=γa, γ a fixed nonzero scalar in the already-chosen frame/normalization. The Cminus projection of the corrected source is therefore

    (r_mid−θ r_t)/(νg²) on D,   θ=νγ.                  (3)

The same conclusion below holds for EVERY constant θ, so it is independent of the otherwise fixed overall Čech sign convention. No sign or numerical normalization of γ is inferred anew.

## 3. An exact nonproportionality identity

Use the actual symbolic divisor frame

    f=A X²Y+B Y³z+Ac X³z²−Bc XY²z³,
    g=−λ(BXY⁴z^−3+A X³Y²z^−4)/(2Ac),   a=z².

All A,B,c,λ,k are nonzero and unassigned. Divide in the polynomial variable X over the field of rational functions in Y,z and these symbols. Put

    F=λkY⁶/(A c⁴ z⁷).

The exact remainders modulo f are

    rem(r_mid,f)=−F P/6,
    rem(r_t,f)=2F Q,

where

    P=A²X²+7ABc²z⁵X²−2ABcz³XY+ABzY²
        +2B²c⁴z¹⁰X²−8B²c³z⁸XY+5B²c²z⁶Y²,
    Q=−A²X²−4ABc²z⁵X²+2ABcz³XY−ABzY²
        +B²c⁴z¹⁰X²+2B²c³z⁸XY−2B²c²z⁶Y².

Thus (3) could vanish only if P+12θQ were the zero polynomial. Its X²z^0 coefficient forces θ=1/12, whereas its X²z^10 coefficient forces θ=−1/6. Because A,B,c are nonzero, these conditions contradict one another.

This is a symbolic identity valid uniformly over the full stabilizer orbit, not an evaluation at selected actual coefficients or at a selected numerical base point. Since the actual D is integral and g is its nowhere-zero quotient-line trivialization, nonzero remainder is exactly nonzero restriction to D. Equation (1) therefore proves the Cminus projection of the corrected source nonzero.

The actual Cplus/J variation is a distinct direct summand and cannot cancel this nonzero Cminus class. Consequently the actual corrected source in C/J is nonzero, as stated.

## 4. What remains

Actual third vanishing says multiplication by a kills this corrected lower source in P4 BEFORE the next division. The next step requires its actual ambient division by q0, followed by multiplication by a and quotient by im β2. Neither (1) nor the nonzero restriction calculation decides that next value. In particular, no fourth-channel nonvanishing, Smith exponent, or generic section count is concluded.

Dependencies: ACTUAL-CUBIC-SUPPORT-IS-GENUS-FOUR-WITH-EXACT-FIVE-TORSION.md §6; the actual double-cubic/global-boundary quotient; ACTUAL-MIDPOINT-ABSOLUTE-SECTION-FOR-THE-FOURTH-SQUARE-INPUT.md; ACTUAL-ATIYAH-CLASS-HAS-AN-ABSOLUTE-DOUBLE-CUBIC-REPRESENTATIVE.md; and the published canonical nonzero square-source correction.

Run python verify_corrected_square_source_reduced_cubic.py. It checks both exact symbolic remainders, the incompatible constant-ratio equations, and the line-degree/cohomology dimensions. The geometric comparison dependencies are not replaced by that algebraic check.
