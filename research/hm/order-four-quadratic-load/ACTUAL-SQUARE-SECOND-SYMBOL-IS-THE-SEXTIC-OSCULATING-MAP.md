# The actual square second symbol is the sextic osculating map

## New conclusions

Retain the ACTUAL sextic normal sequence

    0 -> V O_L(-2) --i--> P4 O_L --q--> O_L(6) -> 0

on L=P(W), with its fixed invariant pairings. Write Q6=q^t for the associated P4-valued sextic section. This notation is distinct from the quartic quotient Q used in the scalar-correction notes.

1. On the discriminant conic of square smoothing directions, the actual second Bockstein is a nonzero scalar multiple of the SECOND POLAR of Q6. Its rank-three image is the osculating plane spanned by Q6, its first derivative, and its second derivative.
2. The sextic curve Q6 has vanishing sequence (0,1,2,4) exactly on the twelve-point polar orbit E and (0,1,2,3) elsewhere. The actual annihilator line c of the second symbol is its osculating-plane dual, a basepoint-free P4-dual-valued series of degree twelve. Its vanishing sequence is (0,2,3,4) on E and (0,1,2,3) elsewhere.
3. Let Delta12 be the invariant equation of E. There is a nonzero scalar C such that the COMPLETE incidence kernel is

    <Q6(p),c(ell)> = C [p,ell]^3
                      Polar_(3,9)(Delta12)(p,ell).        (1)

   The polarization is normalized to restrict to Delta12 on the diagonal. In particular the contact order at (p,p), p in E, is exactly four in either variable, not merely at least three.
4. For a square rooted at an arbitrary x in E, let y be the other fixed point of its order-five stabilizer. Then

    divisor_p <Q6(p),c(x)> = 4x+2y.                      (2)

   Thus this scalar section is nonzero at every one of the other ten polar points. This identifies a precise component of the actual final Serre tests rather than eliminating those ten points from them.

All statements are uniform geometric or representation identities. No actual source coefficient, point value, matrix, or rank has been evaluated. Equation (1) identifies the final-test family, not its pairing with the full R cochain. The companion ACTUAL-THIRD-BOCKSTEIN-VANISHES-ON-SQUARE-DIRECTIONS.md now proves that the full square pairing is zero, through the separate actual source-change/two-chart calculation. The discriminant-divisible third channel remains unresolved at this package cutoff.

## 1. The actual polar comparison

Use the determinant pairing to identify a point ell of P(W) with the negative linear section that vanishes there. The square direction is a=ell^2. Under this convention, restriction of the actual quadratic-in-a second symbol to the discriminant gives

    beta2_square:A O_L(-4) -> P4 O_L.                    (3)

There is precisely one equivariant Hom line for such a map:

    Hom_G(A tensor Sym^4 W,P4) has dimension one.

Indeed Sym^2 W tensor Sym^4 W decomposes as Sym^6 W plus Sym^4 W plus Sym^2 W, and P4 occurs once, in Sym^6 W=V+P4.

The second polar derivative of Q6 supplies another map of type (3). It is not zero: a nonzero homogeneous sextic cannot have all its second derivatives identically zero in characteristic zero. The actual beta2_square is also nonzero, and in fact has rank three everywhere because the actual second-symbol degeneracy scheme is disjoint from the discriminant. Therefore the two maps are proportional by a nonzero scalar. No inference from nonzero composable legs is involved.

Euler's homogeneous identity identifies the fiber span of the three second partial derivatives with the span of Q6, Q6',Q6'' in any regular affine parameter. Consequently the actual second-symbol annihilator is exactly the dual of this osculating plane. The quotient rank and all line twists in this comparison are retained.

## 2. Sextic ramification and the degree-twelve dual

The four components of Q6 are independent because their section map P4-dual->Sym^6 W is a nonzero map from an irreducible representation. They have no common zero: a common-zero divisor would be an invariant divisor of positive degree at most six, while every nonempty orbit on L has at least twelve points. Hence they define a nondegenerate, basepoint-free degree-six linear series of dimension four.

Its Wronskian is a nonzero section of

    O_L(4*6-2*(0+1+2+3))=O_L(12).

Nonvanishing is the usual characteristic-zero independence criterion. Its divisor is invariant, so it is exactly the reduced twelve-point orbit E. At every point of E its ramification weight is one, forcing the vanishing sequence (0,1,2,4). Away from E it is (0,1,2,3). This identifies E intrinsically with the ramification of the ACTUAL sextic normal curve, not a different twelve-point curve.

The covector annihilating Q6,Q6',Q6'' is their exterior product, using the invariant determinant of P4. Its line degree is

    3*6-2*(0+1+2)=12.

The rank-three statement in Section 1 makes this exterior product nowhere zero. It therefore gives an actual equivariant basepoint-free map

    c:O_L(-12) -> P4-dual O_L,                          (4)

unique up to a nonzero constant. Its image is the annihilator of image beta2_(ell^2). It spans all four dimensions because P4 is irreducible.

There is an elementary valuation proof of its vanishing sequences. If a local basis of the original four sections has distinct orders a0<a1<a2<a3, the ith exterior-product coordinate is a three-by-three Wronskian of the other three sections. Its leading order is

    sum_(j!=i) a_j - (0+1+2),

with nonzero leading coefficient by the Vandermonde determinant on those three distinct orders. For (0,1,2,3), these orders are (3,2,1,0); for (0,1,2,4), they are (4,3,2,0). Ordering them proves the claimed dual sequences. This is a valuation theorem for the actual sections, not a replacement by monomial local models.

The dual Wronskian consequently has divisor 3E, of degree36=4*12-12. In particular c has first-derivative ramification at each point of E, even though Q6 is immersive everywhere. These are the sextic normal curve and its degree-twelve dual, NOT the separate degree-eighteen third-gate curve.

## 3. The full incidence kernel is a polarized invariant

Define

    K(p,ell)=<Q6(p),c(ell)>.

It is an invariant section of O(6,12) on L times L. For fixed ell, its first three jets in p vanish at p=ell because c annihilates the second osculating plane. Thus K is divisible by the diagonal section [p,ell]^3. The quotient is an invariant section of O(3,9).

The invariant space of bidegree (3,9) is one-dimensional:

    Sym^3 W=S4,   Sym^9 W=S4+T6,
    dim[Sym^3 W tensor Sym^9 W]^G=1.

The nonzero invariant Delta12, polarized into degrees three and nine, belongs to this space and is nonzero because its diagonal restriction is Delta12. The incidence kernel is also nonzero: for each ell, the nonzero c(ell) cannot annihilate all four independent components of Q6. This proves (1), with C different from zero. No scalar value is selected.

At a point p0 of E, the polarized factor vanishes on the diagonal but has nonzero first derivative in either variable. If Delta12 is the diagonal of its symmetric twelve-linear tensor, differentiation in the first variable of Polar_(3,9) contributes 3/12 of dDelta12, while differentiation in the second contributes 9/12. Since E is reduced, both are nonzero. Multiplying by the cubic diagonal factor proves exact order four in either variable.

Away from E the polarized factor is already nonzero on the diagonal, so both contact orders are exactly three. These assertions include the leading contact multiplicities, not merely a zero-set comparison.

## 4. The order-five fiber and its complete contact divisor

Let x be ANY point of E, and let y be the other fixed point of its order-five stabilizer. Choose the abstract lift and sections exactly as in ACTUAL-C5-SQUARE-CORRECTION-HAS-A-SIMPLE-ROOT.md: the tautological weights at x,y are +1,-1, while s,t have section weights -1,+1, with t vanishing at x and s at y. Thus the square rooted at x is a=t^2, of weight2.

The actual second-symbol image has weights 2,4,6 in P4. Therefore its annihilator c(x) has dual weight2. The equivariant sextic-section map

    P4-dual -> H0(O_L(6))

sends c(x) to a nonzero section of weight2. Among degree-six monomials in s,t there is exactly one such weight line, namely s^2 t^4. Hence

    <Q6(p),c(x)> is a nonzero multiple of s(p)^2 t(p)^4.

This proves (2) without evaluating a coefficient. In particular it has no zero at the other ten points of E.

For comparison, fixing the FIRST argument instead gives a degree-twelve section in ell. Its divisor contains 4x+3y and one reduced stabilizer orbit of five further points. The order four at x follows from Section 3. At y, the dual sequence (0,2,3,4), together with the fiber weights, places the component paired with Q6(x) at order three. The residual degree is five, and every nonfixed stabilizer orbit has size five. This assertion does not identify that additional orbit with either of the five-point subsets of E.

## 5. Direct application to the actual final residue tests

The actual square third quotient is tested by

    zeta_ell = ell^2 i^t c(ell) in H0(V O_L(4)).          (5)

Thus (1) gives a canonical invariant description of the entire annihilator family used in the final Serre residue criterion. It does not replace the physical R/nu by an uncorrected vector representative.

There is also a precise non-exclusion statement at the remaining poles. At each p in E, the polar theorem gives a nonzero radical vector r_p and

    i_p r_p is a nonzero multiple of Q6(p),

with the appropriate one-dimensional coefficient factors. Consequently, for ell=x in E and p in E minus {x,y}, equations (2) and (5) imply

    <r_p,zeta_x(p)> != 0.                               (6)

The square t^2 is nonzero at those ten points, so no additional zero is introduced. Thus the final test does NOT discard their Gram-radical directions. At y the scalar contact <Q6(y),c(x)> vanishes, but the full local R residue proved in the C5 note lies in the different positive weight-zero direction and pairs nontrivially with zeta_x(y). There is no contradiction.

The global class uses the complete expression

    sum_p [<D_p,zeta_x'(p)>+<B_p,zeta_x(p)>],

where D_p and B_p are the PHYSICAL double and simple coefficients of R/nu. The derivative term, all ten remaining poles, the scalar-extension correction, and the actual connecting-space quotients remain. No nonzero global cohomology class or third-Bockstein value follows from (1), (2), or (6) alone. The companion square-vanishing theorem proves that this COMPLETE sum is zero; the non-exclusion of individual local directions is fully compatible with that cancellation.

## Reproduction and inputs

Run python verify_square_second_sextic_osculation.py. It checks the equivariant Hom dimensions, Wronskian and dual degrees, all possible weight-one vanishing sequences, the universal Wronskian valuation formula, the polarized-diagonal derivative factors, and the complete C5 sextic weight line. The actual geometry is proved above; no actual coefficients, matrix/rank evaluations, parameter scans, local-model experiments, or external writes occur.

Inputs are the actual second-symbol map and its square rank-three theorem, the sextic normal sequence in VERTEX-QUINTIC-RELATION-EXTENSION-AND-SQUARE-P4.md, and the actual polar and C5 notes named above. The degree-eighteen third-gate osculation theorem is not used as a substitute for this different sextic comparison.
