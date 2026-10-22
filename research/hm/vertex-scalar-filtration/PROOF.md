# The fourth-square scalar has only the degree-eight polynomial block

## Result and dependencies

Let Q be the fixed rank-three quadric, I its actual Serre zero ideal, L its vertex line, and C its smooth conic component. Keep the physical-positive involution and fixed positive/negative coordinate decomposition. Write U for the binary positive-coordinate representation and W for the negative-coordinate representation. Thus the positive coordinates are Sym^2 U, the negative coordinates are W, and O_Q(1) has binary cover weight two.

For every source a in A=Sym^2 W and h in D5=Sym^4 U with nonzero restrictions to Q, [PR691](https://github.com/Akilleez-QA/read-em-and-weep/pull/691), commit [dac9a7eca25d112dff9702ec863d161709792326](https://github.com/Akilleez-QA/read-em-and-weep/commit/dac9a7eca25d112dff9702ec863d161709792326), supplies an intrinsic section

    S4 = a^3 h rho4,       rho4 in H0(O_Q(6))_+,

with rho4 in I^2 on the entire smooth locus. Here J4^2=q^3 S4 Id and J4 restricts to a J3 on 3Q. The result proved below is

    rho4 in Sym^8 U tensor Sym^2 W,

inside the fixed polynomial decomposition of H0(O_Q(6))_+. This is a 27-dimensional scalar target, not a computation of rho4, not its vanishing, and not a value of beta4.

We use the actual regular-pair and harmonic-frame inputs of [the third-neighborhood square-zero theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-CORRECTED-THIRD-NEIGHBORHOOD-LIFT-IS-SQUARE-ZERO.md), section 2. We use its full filtered actual pair, not a homogeneous replacement. The physical parity and polynomial block descriptions are also fixed in [the square-filtration theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/POSITIVE-SECOND-BOCKSTEIN-SQUARE-FILTRATION.md), sections 1 and 2.

## 1. Work at the generic vertex, with the actual frame

Pass to the binary cover of a negative affine chart, then to the generic point of L and its completion in the two binary positive variables. The coefficient field is k=C(L). We retain the actual filtered frame from the cited third-neighborhood theorem. The actual matrix n of N has weighted order at least eight, with leading matrix n8 supplied by a regular pair f3,g5 of degrees 3,5. A trace-free matrix of weighted degree d has diagonal entry degree d, upper entry degree d-2, and lower entry degree d+2. Regular matrices therefore have weighted order at least -2. The relevant degrees are even, as in the cited frame calculation.

The determinant factor and any nonhomogeneous higher terms are included in n and in its leading regular-pair description. We do not change the frame to make its determinant constant or discard its higher terms. In the cited harmonic convention, the local actual first-normal lift has coefficients

    Ns = H(n) + q H(T) mod q^2,       ord(n)>=8, ord(T)>=4.

Here H is the homogeneous harmonic lifting operator, extended termwise to the completion. The actual first-normal coherence gives

    J3|2Q = F Ns,       F|Q=a^2 h.

The physical negative quadratic a is q-independent and is a unit over k. The positive source h has binary degree four. The scalar coefficient of q in F is regular, so has nonnegative binary order. No constancy of that coefficient, or of the actual bundle coefficients, is assumed.

The harmonic decomposition is fixed explicitly in [the universal second-normal product](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/UNIVERSAL-SECOND-NORMAL-HARMONIC-PRODUCT-AND-OPERATOR-DEFECT.md), section 1. For every r>=0, the q^r coefficient B_r of a product of harmonic lifts lowers binary degree by exactly 4r when nonzero. This follows just from homogeneity: q has binary degree four, and homogeneous harmonic decomposition preserves total degree. It does not require a formula or evaluation for B_3. For matrix products the same rule holds with weighted matrix degrees: opposite off-diagonal shifts cancel, and diagonal/off-diagonal shifts add correctly. This also holds for scalar-matrix products. All estimates therefore apply termwise to the full completed series.

## 2. The second coefficient of J3 starts at degree four

Write in this frame

    J3 = H(L0)+q H(L1)+q^2 H(L2) mod q^3.

The first two coefficients satisfy

    L0=a^2 h n,       ord(L0)>=12,       ord(L1)>=8.

Indeed L1 is the sum of F0 T, F1 n and B1(F0,n), where F0=a^2 h has order four and F1 has order at least zero. Their respective lower bounds are 8,8,8.

The q^2 coefficient of the already proved identity J3^2=0 is the sum of

    L0 L2 + L2 L0,
    L1^2,
    B1(L0,L1)+B1(L1,L0),
    B2(L0,L0).

The last three lines have weighted scalar order at least sixteen. By trace-free rank-two polarization, the first line is tr(L0 L2) Id. Suppose L2 has a nonzero term of lowest degree d<4. Regularity and parity restrict d to -2,0,2. Its degree 12+d trace equation is

    a^2 h tr(n8 (L2)_d)=0.

The graded binary polynomial ring over k is a domain. Since a and h are nonzero, cancellation gives tr(n8 (L2)_d)=0. The regular-pair trace kernel gives, writing (L2)_d=[[x,y],[z,-x]],

    y=f3 y1,       z=g5 z1,
    x=(f3 z1-g5 y1)/2.

The degrees of y1 and z1 are d-5 and d-3, both negative for d=-2,0,2. Thus (L2)_d=0, a contradiction. This proves ord(L2)>=4. Equivalently one may eliminate these three low degrees successively; higher terms of n cannot enter before the preceding lower terms of L2 have vanished. This is a filtered argument for the actual matrix, not a truncation assumption.

## 3. Retain the arbitrary fourth coefficient

Let Jtilde be the lift of J3 to 4Q with no q^3 harmonic coefficient. Its cubic scalar square coefficient chi has the following contributions and lower bounds:

    L1 L2 + L2 L1:                   8+4 =12,
    B1(L0,L2)+B1(L2,L0):           12+4-4=12,
    B1(L1,L1):                     8+8-4=12,
    B2(L0,L1)+B2(L1,L0):          12+8-8=12,
    B3(L0,L0):                    12+12-12=12.

Thus ord(chi)>=12. However this does NOT establish ord(S4)>=12 for the actual fourth lift. There is an arbitrary regular trace-free matrix K such that

    J4=a Jtilde+q^3 H(K) mod q^4.

Because a is q-independent, its square coefficient is exactly

    S4=a^2 chi+a tr(L0 K)
      =a^2 chi+a^3 h tr(n K).

Regularity gives ord(K)>=-2, and hence the last term has order at least 4+8-2=10. Therefore the correct unconditional estimate from this calculation is

    ord(S4)>=10.

Retaining this term is essential; neither global choice-independence nor the local first-normal theorem authorizes deleting it. The actual factorization S4=a^3 h rho4 and the domain property of the graded scalar ring now give

    ord(rho4)>=6

at the generic vertex. This is sufficient. No division by h as a regular unit, or membership in I^2 after division, has been asserted. Order additivity uses the nonzero leading homogeneous h of degree four, while a is a unit only over the generic coefficient field.

## 4. Global polynomial blocks and source zeros

The fixed cone coordinate ring is the even Veronese of binary positive variables of weight one and negative variables of weight two. Its global degree-six physical-positive sections have the direct polynomial decomposition

    Sym^0 U tensor Sym^6 W,
    Sym^4 U tensor Sym^4 W,
    Sym^8 U tensor Sym^2 W,
    Sym^12 U.

The four binary degrees are 0,4,8,12. Generic vertex order at least six kills the first two polynomial blocks: a coefficient polynomial on the integral line L that vanishes over C(L) vanishes identically. Equivalently the relevant graded coefficient bundles are locally free on L and have no sections supported at finitely many source-zero points. This promotes the conclusion across every zero of a, without applying Hartogs to the square ideal or inverting a there. We obtain global binary order at least eight.

Finally rho4 lies in I^2 along C by PR691, so its restriction to C is zero. The first three polynomial blocks restrict to zero because they contain negative coordinates. The degree-twelve pure-positive block restricts injectively, indeed isomorphically, to H0(O_C(6))=Sym^12 U. That last block must vanish. Only Sym^8 U tensor Sym^2 W remains, of dimension (8+1)(2+1)=27.

This target reduction does not prove the remaining vertex I^2 membership. At binary degree eight the associated square-ideal coefficient bundle is P4 O_L(-2), whereas the ambient coefficient bundle is Sym^8 U O_L(2). The residual section can still have nonzero image in the square-ideal quotient. No actual coefficient, derivative, matrix rank, selected instance, or large computation is used here.
