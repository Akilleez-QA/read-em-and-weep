# Scalar Cartan boundaries: Wronskian, exceptional-zero, and first-normal gates

## Hypotheses and new conclusions

Let C8=Sym^8 W=P4 direct-sum D5 be the Cartan space of plane square products. Write

    phi:C8 tensor O_T -> F4(2)

for the ACTUAL boundary delta(q0 -), and suppose its image lies in a scalar summand O_T(a+2), with a=12,14,or18. Let R(r,s)=phi_r(ell_s^8)=D(r,s)^2 f(r,s). The actual P4 nonvanishing theorem is assumed: the global G-map phi|P4 is nonzero.

The following are new constraints on occurrence of these scalar possibilities. Conclusion 1 is stronger: it holds without the scalar-target hypothesis.

1. For ALL SEVEN target types, vanishing of the leading diagonal scalar forces phi to be nonzero on D5. Hence the GLOBAL SECTION map C8 -> H0(F4(2)) is injective. This statement does not require a scalar target. It is not fiber injectivity; in a scalar target the fiber image still has rank one.
2. In the a=18, raw-diagonal-order-four family there is precisely one abstract coupling line which annihilates P4. It is the canonical fourth-osculating covector of the D5 binary-octavic linear series. The actual P4 nonvanishing theorem excludes that line. Its construction uses no selected coefficients.
3. For a=12 or14, the actual P4 fiber boundary is nonzero at EVERY parameter. For a=18, it vanishes scheme-theoretically on EXACTLY the twelve-point order-five orbit, with simple multiplicity. Thus any actual nonzero P4 fiber boundary at even one of those twelve parameters would exclude scalar a=18.
4. In the a=18 case the actual Cartan image line is either O_T(20) or O_T(8): the only possible common base divisor is the full twelve-point orbit. The a=12 and14 Cartan image lines are O_T(14) and O_T(16), respectively.
5. Scalar a=18 forces a particular W-prime first-normal lift in H0(I_R B(6)). This lift is unique with its prescribed normal tensor and is NOT an ordinary negative-linear product of ambient twist-five adjoints. Its connecting class is the nonzero W-prime channel of H1(B(4)). This is an explicit necessary actual-map criterion, not an assertion that the required normal tensor is attained.

No scalar type, coupling value, selected rank, or actual fiber is evaluated here. These constraints do not by themselves exclude an actual scalar case.

## 1. Wronskian nonvanishing forces both Cartan constituents

For a fixed m-dimensional subspace U of binary forms of degree n over C, the generic vanishing sequence at a point of P1 is 0,1,...,m-1. Equivalently, its Wronskian is nonzero: in an affine coordinate the first m derivatives of a basis have nonzero determinant because independent polynomials in characteristic zero have nonzero Wronskian. Therefore no nonzero varying vector of U can vanish to order at least m at the moving generic point.

The scalar zero-leading cases have raw diagonal orders

    a=12: order5;
    a=14: order6;
    a=18: order4 or8.

In fact the leading-scalar implication holds for every one of the seven target types, not only scalar targets. The established divided-cross-block theorem says that vanishing of the leading scalar makes the vector-valued raw section R divisible by D^4: a conditional third diagonal factor forces a fourth because H0(F4(4))^G=0.

If phi killed D5, trivialize its target at the generic r and take each scalar coordinate of R(r,-). Each is an octavic in the fixed four-dimensional P4 subspace of C8*, over C(T), and each vanishes at s=r to order at least four. The generic first-four-jet evaluation on that fixed P4 space is invertible by its nonzero Wronskian. Thus every coordinate would be zero. This contradicts the proved nonzero actual Cartan boundary. Therefore phi|D5 is nonzero. Together with the actual phi|P4 nonvanishing and the inequivalence of the two irreducibles, this makes C8 -> H0(F4(2)) injective globally on sections for every zero-leading-scalar case.

There is also a stronger abstract statement when raw order is at least five: then a D5-only family is impossible by the same argument with m=5. Consequently in the a=12/order5, a=14/order6, and a=18/order8 invariant lines, both constituent maps are automatically nonzero even before invoking actual P4 nonvanishing. Only the a=18/order4 family admits the exceptional D5-only line described next.

## 2. The unique excluded D5-only line is an osculating construction

Let U=D5 be the unique five-dimensional summand of H0(O_T(8)). It is basepoint-free: a nonempty common base divisor would be G-stable of degree at most eight, but the smallest nonempty icosahedral orbit has twelve points.

The Wronskian of this five-dimensional degree-eight linear series has degree

    5(8-5+1)=20.

It is a nonzero invariant section of O_T(20), since the determinant characters are trivial. That invariant space is one-dimensional, so it is a nonzero multiple of F20. This invariant has a reduced zero divisor: a repeated orbit would already have degree at least24, and the invariant divisor of total degree20 can only be the twenty-point orbit. Hence each ramification weight is one. The vanishing sequence at these points is exactly 0,1,2,3,5, and elsewhere it is 0,1,2,3,4.

It follows that the order-three jet evaluation is onto EVERYWHERE:

    0 -> O_T(-20) -> D5 tensor O_T -> J^3(O_T(8)) -> 0.

Indeed J^3 has rank four and degree 4*8-4*3=20, and the first four jets have rank four for both vanishing sequences above. Its kernel defines a nowhere-zero D5-valued coefficient vector of degree20. Pairing it with the source octavic variable gives an invariant biform R_D of bidegree(20,8), divisible by D^4 but not by D^5. Thus R_D/D^2 is a scalar divided section of bidegree(18,6) with exact diagonal order two.

This is the UNIQUE D5-only biform of these degrees with raw diagonal order at least four. At a generic point every such vector lies in the same jet-kernel line, and the equal degree together with its nowhere-zero coefficient vector makes the ratio a global constant. Therefore it spans the unique abstract P4-annihilating line in the two-dimensional zero-leading scalar family. The actual boundary cannot lie on it, by the established actual P4 nonvanishing theorem.

This identifies a forbidden coupling line intrinsically, without computing a coefficient vector for F20, choosing an actual section, or evaluating a residual matrix.

## 3. Exact exceptional zeros of the P4 constituent

Universal character inner products give

    mult(P4,Sym^8 W)=mult(P4,Sym^14 W)
      =mult(P4,Sym^16 W)=mult(P4,Sym^20 W)=1,
    mult(P4,Sym^2 W)=mult(P4,Sym^4 W)=0.

The unique degree-eight P4 linear series has no basepoint, again because a nonempty G-stable divisor would have degree at most eight. Multiplication by the degree-twelve invariant F12 gives a nonzero P4 copy in Sym^20 W. Multiplicity one therefore identifies the ENTIRE degree-twenty P4 covariant as

    F12 times the degree-eight P4 covariant.

The actual P4 map is nonzero, so in scalar a=18 its zero divisor is exactly div(F12), not a proper subset or a higher multiple. F12 is reduced and its zeros are the twelve-point order-five orbit.

For degrees14 and16, a nonempty P4 base divisor could only have degree12, since the next positive binary invariant degree is20. Dividing it out would leave a P4 covariant of degree2 or4, respectively. Both multiplicities vanish. Thus the P4 maps for scalar a=12 and14 are basepoint-free.

The common zero divisor of the full Cartan map is contained in the P4 zero divisor. Consequently it is empty in a=12,14. In a=18 it is either empty or all of div(F12), because that reduced orbit is transitive. The image sheaf of the scalar Cartan map is correspondingly O(20) or O(20)(-div F12)=O(8). This is the ACTUAL line image on T, not a claim that O(8) is saturated inside O(20).

## 4. The degree-eight P4 series has a canonical linear syzygy

Put W-prime for the other binary two-space. The universal identities are

    W tensor W-prime = P4,
    mult(W-prime,Sym^9 W)=0.

The Euler inclusion O_T(-1)->W tensor O_T therefore gives a canonical subbundle

    W-prime tensor O_T(-1) -> P4 tensor O_T.

Its composition with the degree-eight P4 evaluation map is zero: such a composition would be an equivariant map W-prime -> Sym^9 W, which is impossible. The quotient of the Euler inclusion is W-prime O(1); its induced map to O(8) is onto because the P4 evaluation is basepoint-free. Its kernel is O(-6). Thus the full evaluation kernel has the equivariant splitting

    ker[P4 O -> O(8)] = W-prime O(-1) direct-sum O(-6).

The extension splits because H1(O(5))=0, and a splitting can be averaged over G. For scalar a=18, multiplication of the evaluation by F12 changes its image divisor but NOT this kernel. Hence its canonical W-prime O(-1) syzygy lies in the actual boundary kernel G5.

## 5. A necessary first-normal non-product Koszul class

Use the actual exact sequence

    0 -> A O_T(-4) -> E5,+ -> G5 -> 0.

The equivariant obstruction to lifting the syzygy W-prime O(-1)->G5 is

    Hom_G(W-prime, A tensor H1(O_T(-3)))
      = Hom_G(W-prime, A tensor W)=0.

Lifts have no ambiguity, since H0(O_T(-3))=0. Thus there is a unique equivariant lift. Twisting by one and using the blowup dictionary gives a W-prime subspace of H0(I_R B(6)), whose prescribed first normal tensor is q0 times the canonical P4 linear syzygy.

The exact two-generator Koszul sequence is

    0 -> B(4) -> W tensor B(5) -> I_R B(6) -> 0.

The established actual H0(B(4))=0 and the actual cohomology characters give the following multiplicities of W-prime:

    H0(W tensor B(5)): 1;
    H1(B(4)): 1;
    H1(W tensor B(5)): 0.

Consequently the W-prime multiplicity space of H0(I_R B(6)) has dimension exactly two, with an exact sequence of multiplicity spaces

    0 -> C (ordinary products) -> C^2 -> C (connecting class) -> 0.

The prescribed lift cannot belong to the ordinary-product copy. If it did, its normal coefficient would be the W-prime projection of W tensor the ambient P4 summand of H0(B(5)). Equality with q0 times the prescribed P4 syzygy would force the ambient P4 restriction to R to equal q0 times the plane Cartan P4. Here no information is lost by taking the W-prime projection: adjunction uses W tensor W-prime=P4, so the corresponding whole P4 map is recovered.

The entire ambient P4 would then restrict to zero on C0=(q0=0). But the actual identity H0(B(5))=Sym^2 H0(F(3)), together with generation on C0, realizes that kernel as the space of quadratic equations of an integral nondegenerate ruled surface in P3. It has dimension at most one and cannot contain a four-space. This contradiction excludes the ordinary-product copy.

Therefore scalar a=18 necessarily selects a lift with NONZERO connecting class in the unique W-prime of H1(B(4)). This is a lower-normal geometric condition independent of the existing fourth-normal leading-scalar lift gate. The nonzero connecting W-prime channel exists automatically by this exact sequence. Its existence is NOT an excluded obstruction and does not prove scalar occurrence. The dimensions alone do not ensure that the required q0 first-normal tensor is attained; that remains the actual-map condition.

## Verification and limits

verify_scalar_cartan_occurrence_gates.py checks the universal character multiplicities, the exact Koszul W-prime counts, and jet degree identities. The Wronskian, orbit, lifting, and ruled-surface arguments above are mathematical proofs. No actual HM/source coefficients, selected matrices, numerical ranks, or consumed local-model experiment are used.

Dependencies: actual P4 nonvanishing and ruled-surface quadratic bound; TWIST-FIVE-GLOBAL-COHOMOLOGY-AND-BOUNDARY-DEFECT.md; DIAGONAL-SCALAR-LIFT-NONPRODUCT-OBSTRUCTION.md for actual H1(B(4)); the scalar-target and scalar-zero-jet proofs. No external write or publication is performed here.
