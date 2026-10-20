# Constant bilinear scalar repairs do not remove the ordinary-twist failure

## Result and exact scope

Fix p=(0,1), the accepted actual source row transitions g, and the product-factor derivations V_0,V_1. Retain ordinary scalar multiplication in the descent equation

    T_jk * T_ij = h_ijk T_ik mod ε³,
    T_ij = g_ij + ε U_ij + ε² W_ij,
    h_ijk = 1 + ε b_ijk + ε² c_ijk,

where * is any associative second-order product with first coefficient

    μ(H,G) = ((V_0 H)(V_1 G) − (V_1 H)(V_0 G))/2.

Let A,B be constants and take the off-diagonal bilinear first scalar coefficient

    b^(A,B)_ijk = A q_0,ij q_1,jk + B q_1,ij q_0,jk,
    q_d,ij = (m_j,d − m_i,d)r_d,       r_d = y_d/x_d.

The necessary second-order associativity condition for this prescription forces

    A = B = 0.                                               (0.1)

In particular, start with the original b^0=(15/4)q_0,ij q_1,jk and make a constant same-edge cross-bilinear scalar repair

    e_ij = t q_0,ij q_1,ij,
    b' = b^0 + δe,
    s' = s_raw,p + e.                                       (0.2)

Then A=15/4−t and B=−t, so A−B=15/4. No t can satisfy (0.1). Every repair (0.2), including antisymmetrization, still has a regular first lift but admits no second-order extension of this ordinary-scalar-twisted equation. Arbitrary scalar c, arbitrary valid first lift U, and arbitrary matrix-valued second edge W cannot remove the failure.

This is a bounded exclusion of the displayed constant off-diagonal bilinear ansatz. We do not claim that (0.2) exhausts all scalar coboundaries or all cohomologous representatives. We do not prove existence when A=B=0. We do not change frames, replace ordinary scalar multiplication by star multiplication, allow non-scalar twists, transport the fresh increasing-mask argument to p=(2,3), determine a mixed obstruction class, or settle another deformation formulation or algebraicity.

## 1. Accepted inputs and conventions

We use the accepted same-pair ordinary-twist exclusion and the corrected structural-closure v2 proof. Exact copies are included under dependencies/. The v2 first-order display contains its required composite-edge term U_ik; its correction is independently accepted in the included erratum review.

The geometric inputs, already established in those packets, are:

1. X=C⁴ is integral, where C is the smooth projective complex curve y²=x³−x. The legal factor opens are U_0=C\{O} and U_1=C\{P_0,P_1,P_−1}.
2. The source row transitions satisfy g_jk g_ij=g_ik, det(g_ij)=1, and

       g_ij = D(ν_j)(P_ci I_cj)^t D(ν_i)^−1,
       D(z)=diag(z,z^−1),     ν_i=product_d r_d^(m_i,d).

   The proved same-carrier identity P_c I_c=Id₂ reduces this to g_ij=D(ν_j/ν_i) when all vertices have carrier c.
3. V_d is the global product-factor derivation with

       V_d x_d=y_d,    V_d y_d=(3x_d²−1)/2,

   and V_d kills functions from every other factor. The V_d commute. The q above are the actual ordered source scalars.
4. The source scalar s_raw,p and the fixed traceless edge k_p give the regular first lift U^0_ij=g_ij(s_raw,p,ij Id+k_p,ij), with the corrected equation

       U^0_jk g_ij + g_jk U^0_ij + μ(g_jk,g_ij)
           = U^0_ik + b^0_ijk g_ik.                       (1.1)

We use the scalar edge differential (δe)_ijk=e_jk−e_ik+e_ij. For a row-endomorphism edge x it is g_ij^−1 x_jk g_ij−x_ik+x_ij. These agree on scalar multiples of Id.

All new arguments below use proved identities of regular maps and rational sections. No physical source, model, actual primitive matrix, actual polynomial, point, jet, residual, or detector is executed or evaluated. 

## 2. The repair and its first lift, with the sign derived

Write a_d=q_d,ij and z_d=q_d,jk. Edge additivity gives q_d,ik=a_d+z_d. Direct scalar expansion yields

    δ(q_0 q_1)_ijk
      = z_0 z_1 − (a_0+z_0)(a_1+z_1) + a_0 a_1
      = −a_0 z_1 − a_1 z_0.                              (2.1)

Therefore b'=b^0+δe has

    A=15/4−t,       B=−t,       A−B=15/4.                 (2.2)

Conversely every constant pair on this affine line is obtained from exactly one t, namely t=−B. This algebraic classification concerns the explicitly specified repair family (0.2); it is not a cohomology classification of arbitrary possible repairs.

Both ordered cup terms q_0,ij q_1,jk and q_1,ij q_0,jk are scalar 2-cocycles, by additivity of the two q edges. Hence every b^(A,B) has

    b_ijk+b_ikl=b_jkl+b_ijl.                              (2.3)

Define U'_ij=U^0_ij+e_ij g_ij, equivalently U'=g(s' Id+k_p). Relative to (1.1), the change in the three first-lift terms is

    e_jk g_jk g_ij + e_ij g_jk g_ij − e_ik g_ik
        = (δe)_ijk g_ik.                                (2.4)

Thus U' satisfies exactly the first-order equation with b'. No change to k_p or μ is needed. The q are regular on their relevant legal edges: a nonzero mask difference enforces the factor overlap U_0∩U_1; a zero difference gives the zero section. Consequently e,s',U' are regular on the original edge domains.

The antisymmetric representative is t=15/8:

    b^anti = (15/8)(q_0,ij q_1,jk − q_1,ij q_0,jk),
    s^anti = s_raw,p + (15/8)q_0 q_1.                    (2.5)

It is therefore included in the family, with a valid first lift. The failure proved below is at second order, not a failure to construct that first lift.

## 3. Necessary associativity condition, retaining all corrections

For any b satisfying (2.3), suppose the first-order equation holds for some U. Keep all second correcting edges W, and let c be any scalar 2-cochain. Write

    T_jk*T_ij − h_ijk T_ik = ε² D_ijk mod ε³.

If ν denotes the second coefficient of the associative product, then

    D_ijk = W_jk g_ij + g_jk W_ij − W_ik
          + U_jk U_ij + μ(U_jk,g_ij)+μ(g_jk,U_ij)
          + ν(g_jk,g_ij) − b_ijk U_ik − c_ijk g_ik.    (3.1)

We rederive the needed compatibility rather than importing a mixed-parameter coefficient. To order two, the ordinary scalar product-rule errors are exactly

    T_kl*(h_ijk T_ik) − h_ijk(T_kl*T_ik)
        = ε² μ(g_kl,b_ijk)g_ik,

    (h_jkl T_jl)*T_ij − h_jkl(T_jl*T_ij)
        = ε² g_jl μ(b_jkl,g_ij).                       (3.2)

A scalar in a μ slot denotes that scalar times Id. The identities follow by Leibniz in the scalar slot. A derivative of c, a first lift paired with a derivative of b, or a second product coefficient paired with εb first contributes at degree three.

Apply associativity in the order

    0 = T_kl*(T_jk*T_ij) − (T_kl*T_jk)*T_ij.

Using (3.1)–(3.2), the degree-two coefficient is

    0 = g_kl D_ijk − D_jkl g_ij + D_ikl − D_ijl
        + K_ijkl g_il + 𝒜_ijkl,

    K_ijkl = c_ijk+c_ikl−c_jkl−c_ijl
             + b_ijk b_ikl−b_jkl b_ijl,

    𝒜_ijkl = μ(g_kl,b_ijk)g_ik − g_jl μ(b_jkl,g_ij).  (3.3)

Thus the second endpoint carries a minus sign, and each μ contributes its single factor 1/2. The scalar cocycle (2.3) kills the degree-one scalar product difference; no condition on the degree-two scalar K is assumed.

Set M_ijk=g_ik^−1 D_ijk. The row Čech differential is

    (δ_row M)_ijkl=g_ij^−1 M_jkl g_ij−M_ikl+M_ijl−M_ijk.

The transition cocycle makes the four D terms in (3.3) equal −g_il δ_row M. Hence

    δ_row tf(M)=tf(g_il^−1 𝒜_ijkl),
    tf(Z)=Z−tr(Z)Id/2.                                  (3.4)

If the required second-order equation were solvable, D would be zero, forcing the right side of (3.4) to vanish on every common quadruple. This necessary condition depends only on g,b,μ. In particular, changing U or W, changing the associative ν, or choosing a scalar c with any K cannot cancel a nonzero trace-free anomaly.

## 4. Two fresh increasing quadruples on one actual common open

Use the same existing auxiliary carrier c at every vertex, with

    Ω_c = f^−1 D(v_0 v_1 v_3 v_4) ⊂ X.

This is the actual auxiliary carrier of the accepted source. It is nonempty: each nonconstant x-map C→P¹ is surjective, their product is surjective, and the coefficient map (P¹)⁴→P⁴ is surjective over C by factorization of binary quartics. Therefore f is surjective, so the inverse image of the nonempty displayed projective open is nonempty. No point is selected.

The mask integer is m_0+2m_1+4m_2+8m_3. In each quadruple its positions are i=0,j=1,k=2,l=3; those vertex labels must not be confused with the mask values themselves. Use

    Q_A: masks (0,1,3,5),
    Q_B: masks (0,2,3,6).                                (4.1)

Both quadruples have four distinct strictly increasing source masks on the same carrier. Choose the same finite standard tag at all vertices: every factor of the common legal locus below already lies in U_0, so this does not shrink that locus. Thus the carrier and standard-tag portions of the source key are fixed and increasing numerical masks give increasing full source keys. They vary bits 0,1,2 and keep bit 3 zero. Their common legal locus is the SAME nonempty open

    L=(U_0∩U_1)_0 × (U_0∩U_1)_1 × (U_0∩U_1)_2 × U_0,3.

Every factor is nonempty and open, so L is dense in the integral X. Hence Ω_c∩L is nonempty. Here x_0,x_1,x_2 and r_0,r_1,r_2 are regular units. All coefficients and transitions below are regular on this genuine common carrier/legal intersection, without adding a new localization.

The third varying factor supplies the fresh high bit that preserves increasing order while allowing the needed negative change in bit 0 or bit 1. V_0 and V_1 annihilate r_2 exactly by product-factor support.

## 5. First quadruple isolates A, with positive sign

For Q_A the successive bit vectors in positions (0,1,2) are

    (0,0,0), (1,0,0), (1,1,0), (1,0,1).

The ν factors are respectively 1,r_0,r_0 r_1,r_0 r_2. The (q_0,q_1) values on the successive edges are

    edge 01: (r_0,0),
    edge 12: (0,r_1),
    edge 23: (0,−r_1).

Thus, for every A,B,

    b_012=A r_0 r_1,       b_123=0,
    g_23=D(r_2/r_1),       g_02=D(r_0 r_1),
    g_03=D(r_0 r_2)=g_23 g_02.                         (5.1)

Let H=diag(1,−1), r'_d=V_d r_d. The abstract cocharacter identity

    D(z)^−1 V D(z)=(Vz/z)H

and product-factor support give

    V_0 g_23=0,
    g_23^−1 V_1 g_23=−(r'_1/r_1)H,
    V_0 b_012=A r'_0 r_1.                             (5.2)

Because b_123 is the zero section, its derivatives are also zero. The only anomaly term in (3.3) is μ(g_23,b_012)g_02. Using LEFT normalization and commuting only the diagonal cocharacters,

    g_03^−1 𝒜_0123
      = g_02^−1 g_23^−1 μ(g_23,b_012)g_02
      = −(1/2)[−(r'_1/r_1)H][A r'_0 r_1]
      = +(A/2)r'_0 r'_1 H.                             (5.3)

It is already trace-free. The positive sign results from the minus term in μ and the negative bit-1 logarithmic current.

## 6. Second quadruple isolates B, with negative sign

For Q_B the successive bit vectors in positions (0,1,2) are

    (0,0,0), (0,1,0), (1,1,0), (0,1,1).

The ν factors are respectively 1,r_1,r_0 r_1,r_1 r_2. The successive (q_0,q_1) edge values are

    edge 01: (0,r_1),
    edge 12: (r_0,0),
    edge 23: (−r_0,0).

Therefore

    b_012=B r_0 r_1,       b_123=0,
    g_23=D(r_2/r_0),       g_02=D(r_0 r_1),
    g_03=D(r_1 r_2)=g_23 g_02.                         (6.1)

Here the supported logarithmic current is instead

    g_23^−1 V_0 g_23=−(r'_0/r_0)H,
    V_1 g_23=0,
    V_1 b_012=B r_0 r'_1.

Consequently the same associator and LEFT normalization give

    g_03^−1 𝒜_0123
      = +(1/2)[−(r'_0/r_0)H][B r_0 r'_1]
      = −(B/2)r'_0 r'_1 H.                             (6.2)

This is also trace-free. The negative sign now comes from the negative bit-0 current in the positive term of μ. No cyclic or decreasing owner tuple is used in either certificate.

## 7. Exact nonzero rational sections and the contradiction

The quotient rule and the curve relation give, as an identity of rational functions,

    V(y/x)=[x(3x²−1)/2−y²]/x²=(x²+1)/(2x).

Thus (5.3) and (6.2) are exactly

    Q_A:  +(A/8) [(x_0²+1)(x_1²+1)/(x_0 x_1)] H,
    Q_B:  −(B/8) [(x_0²+1)(x_1²+1)/(x_0 x_1)] H.       (7.1)

Each x_d is nonconstant, so x_d²+1 is not the zero rational function. The function field of the integral product X is a domain, and x_0,x_1 are units on Ω_c∩L. The bracketed rational function in (7.1) is therefore a regular section there which is not identically zero. Restriction to a nonempty open of an integral variety cannot turn a nonzero rational section into the zero section. It may vanish on proper divisors; nowhere-vanishing is not required.

The necessary condition (3.4) on Q_A forces A=0. The same condition on Q_B forces B=0. This proves (0.1). For the repair family (2.2), these two conclusions contradict A−B=15/4. Equivalently the first certificate would require t=15/4 and the second t=0.

For the antisymmetric choice A=15/8, B=−15/8, BOTH fresh quadruples have the same nonzero normalized anomaly

    +(15/64)[(x_0²+1)(x_1²+1)/(x_0 x_1)]H.             (7.2)

No evaluation at a chosen point is part of this argument.

## 8. Why the fresh masks matter, and what is not concluded

For comparison, the earlier increasing square with masks (0,1,2,3) has b_012=A r_0r_1, b_123=B r_0r_1, and g_23=g_01=D(r_0). Its two normalized anomaly terms add to

    ((A+B)/2)r'_0r'_1 H.

Antisymmetrization kills that particular witness because A+B=0. It does not kill (5.3) and (6.2). The new high-bit masks are what separate the two coefficients while keeping all source keys increasing.

This proves an associativity incompatibility of the stated ordinary scalar-twist prescription under the specified constant repairs. It does not produce a nonzero mixed class or a nonzero same-pair cohomology class. The trace-free second-order defect in this prescription has a nonzero boundary; that is different from exhibiting a closed non-exact class. Nothing here changes the accepted complementary-pair mixed closure theorem, and nothing determines its exactness.

The accompanying producer checks use only invented commuting scalar labels, invented noncommutative words, and small integer mask metadata. They check coboundary signs, first-lift correction order, scalar-slot Leibniz order, the two mask supports, and sign/factor mutations. They do not evaluate the geometric curve, physical q/r formulas, any actual transition or primitive, or a source program. The geometric nonemptiness and rational-section argument are supplied by the written proof. Independent audit remains separate from these producer controls.
