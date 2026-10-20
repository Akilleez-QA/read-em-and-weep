# Same-pair exclusion for the fixed ordinary scalar-twist prescription

## Result and boundary

Fix either p=(a,b)=(0,1) or (2,3), the actual source row transitions g, the product derivations V_a,V_b, and the source's ordered first scalar coefficient

    b_ijk = (15/4) q_a,ij q_b,jk,
    q_d,ij = (m_j,d - m_i,d) r_d,        r_d = y_d/x_d.

For these fixed data there is no second-order extension satisfying

    T_jk * T_ij = h_ijk T_ik mod ε³,
    T_ij = g_ij + ε U_ij + ε² W_ij,
    h_ijk = 1 + ε b_ijk + ε² c_ijk,

where multiplication on the right is ORDINARY scalar multiplication, c is any scalar 2-cochain, and * is an associative second-order product with first coefficient

    μ(H,G) = ((V_a H)(V_b G) - (V_b H)(V_a G))/2.

The exclusion holds for every first lift U satisfying the prescribed first-order equation and every second correcting edge W. It follows from a nonzero trace-free associativity compatibility term on a nonempty actual four-owner intersection. No point is selected or evaluated.

This is a failure of this particular scalar-twisted descent prescription at the repeated-pair order. It is NOT a nonzero mixed obstruction class or a nonzero same-pair cohomology class: the same-pair defect is not even closed. It does not exclude a changed first scalar coefficient, different zeroth-order frame prescription, star-multiplied twist, non-scalar twist, or another deformation formulation. It does not settle mixed exactness, quantization in another formulation, or algebraicity.

## 1. Accepted geometric and source inputs

The accepted local packet `structural-raw-closure-20261018/PROOF.md`, particularly §§2–6, and its independent `REVIEW.md` establish the following as identities of actual regular maps and rational denotations:

1. X=C⁴, with C the smooth projective complex curve y²=x³−x. The legal opens on one factor are U_0=C\{O} and U_1=C\{P_0,P_1,P_−1}.
2. There is one common complex and, on each carrier c, actual primitive maps satisfying P_c I_c=Id₂.
3. The physical row transition is

       g_ij = D(ν_j) (P_ci I_cj)^t D(ν_i)^−1,
       D(z) = diag(z,z^−1),       ν_i = product_d r_d^(m_i,d).

   Its actual inverse is the ordinary inverse; g_jk g_ij=g_ik and det(g_ij)=1. These are regular transitions on the original carrier/legal intersections.
4. V_d is the global invariant product-factor derivation, with

       V_d(x_d)=y_d,    V_d(y_d)=(3x_d²−1)/2,

   and it kills coordinates from other factors. The different V_d commute. The q and b above are the actual ordered source coefficients.
5. The literal first lift exists: U_ij=g_ij(s_raw,p,ij Id+k_p,ij), and it satisfies

       U_jk g_ij + g_jk U_ij + μ(g_jk,g_ij)
           = U_ik + b_ijk g_ik.                         (1.1)

   A display in the accepted closure proof §6 omits the U_ik term on the right. Its immediately preceding identity δ_row x=b Id−C gives (1.1), with that term present, and its subsequent defect equation uses exactly (1.1). We use the proved cochain identity, rather than the incomplete display.

The public [null-second-order-raw-closure proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/4ae1ba6081db6563389d5ff78597cf2e98ecc04f/research/hm/null-second-order-raw-closure/PROOF.md) was read at the named commit. Its Git blob is a3894976f186b3f3bfb4d4953497c468ae041b3b, unchanged from the snapshot in the accepted local packet. It fixes the ordinary scalar multiplication convention and the mixed-sector scope. Its mixed formula is not used to obtain the repeated-pair coefficient: §2 derives that coefficient directly with one parameter.

The accepted product-root proof supplies the actual owner cover, frames and coefficient map used in §3. Its primitive matrices are not expanded here. None of the physical source, matrix, polynomial, model, jet or residual programs is executed or evaluated in this argument.

## 2. One-parameter associativity, derived directly

Work modulo ε³ over characteristic zero. The standard associative extension has

    H*G = HG + ε μ(H,G) + ε² ν(H,G),
    ν(H,G) = [(V_a²H)(V_b²G)
             −2(V_aV_bH)(V_aV_bG)+(V_b²H)(V_a²G)]/8.

The coefficient 1/8 is 1/(2!·2²), from the exponential of the commuting bidifferential operator. Leibniz and commutation prove associativity for ordered matrix coefficients. The calculation below uses only associativity and the first coefficient μ, so its conclusion also applies to any other associative second-order extension with this same μ.

First set T=g+ε U with any solution U of (1.1), and let h=1+ε b+ε² c for arbitrary scalar c. Define the full second-order defect by

    T_jk*T_ij − h_ijk T_ik = ε² D_ijk,

so its precise single-parameter expression is

    D_ijk = U_jk U_ij + μ(U_jk,g_ij)+μ(g_jk,U_ij)
            +ν(g_jk,g_ij) − b_ijk U_ik − c_ijk g_ik.  (2.1)

There is one U_jk U_ij term, one term at each μ endpoint, and one −b U term. There is no factor two from two formal parameters.

The ordered b obeys b_ijk+b_ikl=b_jkl+b_ijl, since the q are additive edge cocycles. Put

    K_ijkl = c_ijk+c_ikl−c_jkl−c_ijl
             +b_ijk b_ikl−b_jkl b_ijl.               (2.2)

This is the ε² coefficient of the ordinary scalar difference h_ijk h_ikl−h_jkl h_ijl. It is permitted to be nonzero; no second-order scalar cocycle assumption is required.

Now expand the single associativity equation

    0 = T_kl*(T_jk*T_ij) − (T_kl*T_jk)*T_ij.

Insert the defects. The first-order equation eliminates every coefficient of degree at most one. In moving h through the remaining star products, the only degree-two errors are

    μ(g_kl,b_ijk g_ik)−b_ijk μ(g_kl,g_ik)
        = μ(g_kl,b_ijk)g_ik,

    −μ(b_jkl g_jl,g_ij)+b_jkl μ(g_jl,g_ij)
        = −g_jl μ(b_jkl,g_ij).

A scalar in a μ slot means that scalar times Id. Derivatives of c first contribute at degree three. A derivative of b multiplied by a first lift also first contributes at degree three. The result is exactly

    0 = g_kl D_ijk − D_jkl g_ij + D_ikl − D_ijl
        + K_ijkl g_il + A_ijkl,

    A_ijkl = μ(g_kl,b_ijk)g_ik
              −g_jl μ(b_jkl,g_ij).                  (2.3)

This proves both the coefficient and its sign from the one-parameter equation, independently of the mixed formula.

Use LEFT normalization M_ijk=g_ik^−1 D_ijk and

    (δ_row M)_ijkl
       = g_ij^−1 M_jkl g_ij − M_ikl + M_ijl − M_ijk.

Because g_il=g_kl g_ik=g_jl g_ij, the four D terms in (2.3) equal −g_il δ_row M. Hence

    δ_row M = K Id + g_il^−1 A,
    δ_row tf(M) = tf(g_il^−1 A).                    (2.4)

Here tf(Z)=Z−tr(Z)Id/2. Conjugation commutes with tf. The anomaly has no U, ν or c in it. Thus its trace-free value is independent of the chosen first lift, the scalar second coefficient, and the associative second-order coefficient ν.

Adding an arbitrary second edge W replaces D by

    D + W_jk g_ij + g_jk W_ij − W_ik.

Writing W_ij=g_ij w_ij, this replaces M by M+δ_row w, whose boundary is unchanged. In particular, a successful extension would imply tf(g_il^−1 A)=0 on every common quadruple. Alternatively, inserting a successful T directly into associativity gives 0=K Id+g_il^−1 A, and its trace-free part gives the same necessary condition.

For determinant-one transitions each normalized anomaly summand is a scalar linear combination of conjugates of g^−1 V_d g. These currents have trace zero. Thus the normalized A in (2.4) is already traceless, but the explicit calculation below suffices without this general observation.

## 3. A nonempty actual four-owner intersection

Use the SAME auxiliary carrier c at all four vertices, namely the inverse image of D(v_0 v_1 v_3 v_4)⊂P⁴. This is an actual carrier of the accepted source, not a new auxiliary localization of a primitive.

Its pullback is nonempty. Indeed, the nonconstant x-map C→P¹ is surjective; the product map C⁴→(P¹)⁴ is surjective; and the coefficient map (P¹)⁴→P⁴ is surjective over C because every binary quartic factors as a product of four binary linear forms, allowing repeated and infinity factors. Thus their composite f is surjective. The displayed auxiliary D-open is a nonempty open of P⁴, so its pullback Ω_c is a nonempty open of the integral X.

Fix the other two legal bits to zero, and assign the bits in positions (a,b) as

    vertex 0: (0,0),     vertex 1: (1,0),
    vertex 2: (0,1),     vertex 3: (1,1).             (3.1)

For either source pair a<b these are the distinct increasing legal masks 0,2^a,2^b,2^a+2^b. All four vertices have the same carrier. Thus this certificate is compatible even with the frozen convention of retaining only increasing source keys.

Their common legal locus is

    L = (U_0∩U_1)_a × (U_0∩U_1)_b
        × product_(d≠a,b) U_0.

Each factor is a nonempty open of the integral curve. Therefore L is a dense nonempty open of X, and Ω_c∩L is nonempty. Its further intersection with the finite reference chart in the other factors is still nonempty and dense. No chosen point, numerical specialization, physical polynomial evaluation or primitive calculation is involved in this nonemptiness argument.

On the a and b factors, the overlap U_0∩U_1 excludes O,P_0,P_1,P_−1. Consequently x_d and r_d are regular units there. All transitions, inverses and coefficients used below are regular on this genuine common owner intersection by the accepted geometric proof.

## 4. Exact normalized anomaly on that intersection

For the same carrier, P_c I_c=Id₂ reduces the physical transition formula to

    g_ij = D(ν_j/ν_i).

This is substitution of a proved morphism identity, not expansion of a primitive matrix. Let H=diag(1,−1). The cocharacter identities D(uv)=D(u)D(v) and

    D(z)^−1 V D(z) = (Vz/z)H

are formal identities in the invertible scalar z. From (3.1),

    g_01=D(r_a),       g_12=D(r_b/r_a),
    g_23=D(r_a),       g_02=D(r_b),
    g_13=D(r_b),       g_03=D(r_a r_b).             (4.1)

The actual ordered cup formula, with no antisymmetrization, gives

    b_012=(15/4)r_a r_b,        b_123=0.

For completeness b_013=(15/4)r_a r_b and b_023=0, consistent with the ordinary scalar cocycle. Write r'_d=V_d r_d. Since V_b g_23=0 and V_b b_012=(15/4)r_a r'_b, (2.3) gives

    A_0123 = (15/8) r_a r'_b (V_a g_23)g_02.

Normalize on the left as required. The identities g_03=g_23 g_02 and the commutation of the diagonal cocharacters yield

    g_03^−1 A_0123
       = (15/8) r_a r'_b (g_23^−1 V_a g_23)
       = +(15/8) r'_a r'_b H.                     (4.2)

This is already trace-free. There is precisely one 1/2 from μ; no second same-pair contribution doubles it.

Using only the curve relation and the quotient rule,

    V(y/x) = [x(3x²−1)/2−y²]/x²
            = (x²+1)/(2x).

Therefore the exact normalized anomaly is

    tf(g_03^−1 A_0123)
      = +15(x_a²+1)(x_b²+1)/(32 x_a x_b) · H.      (4.3)

It is a nonzero rational section. Each x_d is nonconstant and hence transcendental over C in its curve function field, so x_d²+1 is not the zero function. The product function field is a domain. The denominator is a unit on the a,b legal overlap. Thus (4.3) is regular there and is not identically zero on the nonempty carrier/legal intersection. It may vanish on proper divisors; the proof needs nonzero as a section, not nonzero at every point.

As a separate sign cross-check, the all-ordered Čech convention also allows the cyclic square (0,0),(1,0),(1,1),(0,1). In that order g_23=D(r_a^−1), g_02=D(r_a r_b), and g_03=D(r_b), while b_012=(15/4)r_a r_b and b_123=0 still hold. The logarithmic current changes sign, giving −(15/8)r'_a r'_b H. This verifies the negative sign for that cyclic order. The primary certificate (3.1)–(4.3) uses increasing masks and does not depend on allowing a cyclic ordering.

## 5. Consequence and precise comparison with the mixed sector

Equation (4.3) violates the necessary condition (2.4), proving the result. Even allowing c to fail the ordinary scalar cocycle cannot help: its entire associativity contribution K Id is scalar. Even changing the first lift cannot help: its coefficients cancel before the anomaly is formed. Even adding a second matrix-valued edge cannot help: that changes the defect by a Čech boundary. This excludes the fixed ordinary scalar-twist prescription through ε² for either p² or q².

In contrast, at the mixed p q coefficient the accepted theorem differentiates b_q only in p directions and b_p only in q directions. Product-factor support kills those derivatives, so the actual mixed residual is closed. Nothing here changes that theorem or determines whether its closed class is exact. The repeated-pair failure occurs because V_a and V_b act on the same scalar coefficient b_p. It is a separate compatibility obstruction to extending the stated descent equation, not an answer to the open mixed-class problem.

No successful source/model run, detector evaluation, guard release, quantitative execution certificate, higher-order existence, or algebraicity conclusion is asserted. The proof consists of the one-parameter associative expansion, the accepted structural same-carrier identity, and a rational-section nonvanishing argument.
