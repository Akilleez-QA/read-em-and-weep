# The remaining special D5 octic does not extend: exclusion of scalar a=12

## Statement and scope

At an order-five hyperplane, the actual Cartan boundary is nonzero on its source weight-zero line. Together with the previously proved weight-one nonvanishing, this excludes the remaining scalar a=12 possibility. Using the established classification and no-off-diagonal-divisor theorem, the actual residual map has generic rank four in every remaining target type.

This is a universal ideal-sheaf argument retaining all actual nonzero parameter hypotheses, not a selection of actual HM coefficients or an evaluated boundary matrix. It does not claim completion of the original global proof repair.

## 1. Actual geometry and the octic

Use the actual regular section curve C=Q disjoint-union Y, with

    I_Q=(z,q_c(y,u)),
    I_Y=(x²,xq,q²,g), g=kappa xz²-aq,
    a=c y, q=A y²+B u², q_c=C y²+D u².

All c,kappa,A,B,C,D are nonzero, and q,q_c have no common root in P1. The invariant positive-plane conic is

    q0=rho x²+sigma yz, rho sigma!=0.

Inversion fixes x,y,z and negates u. All displayed polynomials are even. The refinement a=c y follows from inversion-equivariance of the Ferrand quotient: its nonzero even coefficient b=kappa z² fixes the quotient linearization, so the other coefficient a is even.

Let R=(u=0), and put

    G=g|R/kappa = xz²-(cA/kappa)y³.

We prove q0 G² does not extend to H0(I_C²(8)). No normalization of the actual constants is necessary.

## 2. Inversion reduces all possible lifts to one quadratic correction

Suppose F in H0(I_C²(8)) restricts to q0 G². Average F under inversion, preserving its restriction, to make F even. The explicit octic

    F_base=q0 g²/kappa²

belongs to I_Y² and has the required restriction to R. Hence F-F_base vanishes on u=0. Because it is even, its polynomial is divisible by u², so

    F=F_base+u² H, deg H=6.

The divisor u=0 contains no component of Y, and O/I_Y² is Cohen-Macaulay, since Y is a regular codimension-two curve. Thus u is a nonzerodivisor on O/I_Y², and the ordinary sheaf colon satisfies (I_Y²:u²)=I_Y². Consequently

    H in H0(I_Y²(6)).

The established exact image of the ordinary square on Pi=(x=0) is

    I_Y²|Pi = q² (a,q)².                           (1)

The pair (a,q) is a regular sequence of degrees (1,2). Its ordinary square has generators a², aq, q² in degrees 2,3,4. The square resolution on P2 and line-bundle H1 vanishing therefore give

    H0((a,q)²(2))=C a².

Applying (1) to the sextic H shows H|Pi=gamma a²q² for a scalar gamma. Restricting the proposed octic yields

    F|Pi=a²q² [sigma yz/kappa²+gamma u²].           (2)

There is no implicit use of an unsaturated polynomial square: (1) is the proved image ideal sheaf, and the complete-intersection square resolution computes its global sections in the needed degree.

## 3. The disjoint conic forces an impossible quadratic

Since F belongs to I_Q², its trace (2) belongs to the ordinary square of (z,q_c) on Pi. Let T be the complete intersection (z,q_c) in that plane. The factors a and q are units near T: a=c y is nonzero at both roots of q_c, since its u² coefficient is nonzero, and q has no common root with q_c. Thus (2) implies

    sigma yz/kappa²+gamma u² in H0(I_T²(2)).

The regular pair (z,q_c) again has degrees (1,2), so

    H0(I_T²(2))=C z².

But yz, u² and z² are independent quadratics, and sigma/kappa² is nonzero. This contradiction proves the asserted nonextension.

This argument uses the full scheme T, including its square ideal, not only vanishing at its support.

## 4. Actual Cartan and residual consequences

The source weight-zero line of Sym⁸W is the monomial X⁴Y⁴. Cartan polarization followed by wedge with w=X³Y sends it to a combination of SK and G² with a nonzero coefficient on G². The coefficient is universally nonzero (the symmetric polarization coefficient is binomial(4,2)²/binomial(8,4)); the two nonzero wedge normalization factors do not change this conclusion.

The shadow q0 SK extends: K belongs to I_Z(3), and H1(I_C(4))=0 gives a lift of q0K to H0(I_C(5)); multiplying by S supplies the octic lift. Thus the actual weight-zero Cartan boundary is nonzero precisely as forced by the G² nonextension above.

At ell=X, the scalar a=12 target O_T(14) has stabilizer weight -14=1 modulo five, whereas this source line has weight0. Equivariance rules out its nonzero image in that scalar line. Therefore scalar a=12 is impossible.

The earlier weight-one nonextension already excludes scalar a=14 and a=18. Types IV and VII are impossible, and the remaining types I, II, III, V and VI all have generic residual rank four: types I, II and V by the unconditional no-off-diagonal-divisor theorem; type III because its low V O(4) coupling cannot vanish now that scalar12 is excluded; and type VI because its low W-prime O(5) coupling cannot vanish now that scalar14 is excluded.

This conclusion concerns the established residual map and classification. Any implication for the original global proof must be made through its separately checked reduction, not inferred merely from this note's title.

## 5. Generic odd-sector vanishing, without a positive-sector claim

The established projected invariant-positive channel has generic rank two off the negative discriminant, and its kernel is exactly the rank-four residual source W tensor S6*. The rank-four residual theorem above therefore gives rank 2+4=6 for the full first smoothing obstruction from its six-dimensional source to its ten-dimensional target. Thus that actual first-order obstruction is generically injective.

For a general nondegenerate negative quadratic q_minus, use the actual smoothing family

    Q_s=(q_minus+s q0=0).

For every s!=0 this is a smooth inversion-even quadric. The checked first-order lifting reduction bounds the nearby odd section space by the kernel of the first obstruction. That kernel is now zero. Proper cohomology and upper semicontinuity consequently give

    h0(Q,B_Q(4))_-=0

on a nonempty open subset of the irreducible smooth-even quadric family, hence generically on that family. This is the reduction in RESIDUAL-SMOOTHING-NONVANISHING-AND-EVEN-RANK.md, section 1 and the smoothing-consequence paragraph, with its former residual-rank lower bound replaced by the rank-four theorem proved here. In particular no higher-order lifting assertion is needed once the first-order kernel is zero.

This closes the generic odd-sector branch only. It does not establish positive-sector maximal rank or claim the original complete repair.

## Dependencies and independent verification

SPECIAL-HYPERPLANE-ADJOINTS-ARE-EXACTLY-SQUARES.md at immutable special-source commit d29d27e5c92cf105b60bce4e828f4860582a2bee supplies the actual ideal sheaves, ordinary-square image (1), and regularity statements. SPECIAL-FIBER-PRIMARY-VANISHING-AND-EXACT-OCTIC-GATE.md supplies H1(I_C(4))=0 and the exact obstruction comparison. SPECIAL-CARTAN-OCTIC-NONEXTENSION-EXCLUDES-A14-A18.md supplies the weight convention, wedge identification, and previous exclusions. NO-OFF-DIAGONAL-DIVISOR-FORCES-RESIDUAL-INJECTIVITY.md supplies the residual-rank implications.

An independently derived proof using two successive ideal colons is retained in SPECIAL-D5-NONEXTENSION-INDEPENDENT-TWO-COLON-PROOF.md. It reaches the contradictory nonzero trace -eta(D/B)y⁴z² after harmless formal coordinate normalization. The shorter inversion proof above is sufficient on its own.
