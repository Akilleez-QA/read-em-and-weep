# Ordinary, left-star and right-star scalar twists all fail in the fixed common-star prescription

## Result and boundary

Fix p=(0,1), the accepted actual source row transitions g, the derivations V_0,V_1, and the ordered first scalar coefficient

    b_ijk = (15/4) q_0,ij q_1,jk,
    q_d,ij = (m_j,d−m_i,d) r_d,        r_d=y_d/x_d.

Use one common ambient associative star algebra on overlaps, with

    H*G = HG + ε μ(H,G) + ε² ν(H,G) mod ε³,
    μ(H,G) = [(V_0 H)(V_1 G)−(V_1 H)(V_0 G)]/2.

For every constant λ, there is no extension satisfying

    T_jk*T_ij = h_ijk T_ik + λ ε² μ(b_ijk,g_ik) mod ε³,       (0.1)
    T_ij = g_ij+ε U_ij+ε² W_ij,
    h_ijk = 1+ε b_ijk+ε² c_ijk,

where h_ijk T_ik denotes ordinary scalar multiplication, c is an arbitrary scalar 2-cochain, U is any valid first lift, and W is any matrix-valued second edge. No choice of the associative second coefficient ν changes the obstruction.

For a unital/normalized ambient star product, ν(1,G)=ν(G,1)=0. Then λ=0 is ordinary scalar multiplication, λ=1 gives h_ijk*T_ik, and λ=−1 gives T_ik*h_ijk, through the stated order. Thus changing only the side or kind of scalar multiplication does not repair the fixed same-pair prescription.

A short additional result in §7 excludes the joint constant family

    b^(A,B)_ijk = A q_0,ij q_1,jk+B q_1,ij q_0,jk

together with the same constant-λ modification: compatibility forces A=B=0. This includes simultaneously changing multiplication side and making a constant same-edge cross-bilinear scalar coboundary repair of the original b. It is not a classification of arbitrary scalar cochains.

All results here keep the original g and one common ambient star algebra. They introduce no algebra-overlap automorphisms. They do not exclude general star-gerbes with algebra transition automorphisms, non-scalar higher twists, changed zeroth transitions, arbitrary changed first scalar coefficients, other deformation formulations, mixed-class exactness, or algebraicity. No actual source, model, matrix, polynomial, point, jet, residual or detector is executed or evaluated.

## 1. Accepted inputs

The accepted same-pair ordinary-twist proof and its independent review are copied under dependencies/. The corrected structural-closure v2 proof and accepted display erratum are also copied there. We use these previously proved structural facts:

1. X=C⁴ is integral, where C is the smooth projective complex curve y²=x³−x. Its legal opens are U_0=C\{O} and U_1=C\{P_0,P_1,P_−1}.
2. The actual row transitions satisfy g_jk g_ij=g_ik and det(g_ij)=1. Their structural formula is

       g_ij = D(ν_j)(P_ci I_cj)^t D(ν_i)^−1,
       D(z)=diag(z,z^−1),       ν_i=product_d r_d^(m_i,d).

   On a common carrier c, the proved identity P_c I_c=Id₂ gives g_ij=D(ν_j/ν_i). No primitive matrix expansion is used.
3. The commuting global product derivations obey V_d x_d=y_d, V_d y_d=(3x_d²−1)/2, and kill coordinates from other factors.
4. The prescribed b has a regular first lift, and every valid first lift in this proof obeys

       U_jk g_ij+g_jk U_ij+μ(g_jk,g_ij)=U_ik+b_ijk g_ik.     (1.1)

   The composite-edge term U_ik is present, as in the corrected v2 display.
5. The owner cover contains the auxiliary carrier Ω_c=f⁻¹D(v_0 v_1 v_3 v_4), with the coefficient map f discussed in §4.

The scalar cocycle identity follows directly from additivity of q:

    b_ijk+b_ikl=b_jkl+b_ijl.                              (1.2)

It holds for either ordered cup and therefore also for the joint family in §7. No scalar second-order cocycle condition is imposed on c.

## 2. Exact correction and direct associator

A scalar in a μ slot means that scalar times Id₂. Product-factor Leibniz gives

    μ(b,G)=−μ(G,b),
    μ(b,HG)=μ(b,H)G+H μ(b,G).                            (2.1)

For a normalized unital product, direct expansion gives

    h*T = hT+ε² μ(b,g),
    T*h = hT+ε² μ(g,b)=hT−ε² μ(b,g) mod ε³.             (2.2)

There is no contribution from derivatives of c at this order. We do not posit an associative binary operation called "twisted multiplication." Only the ambient * is assumed associative.

Define the second-order defect of (0.1) by

    T_jk*T_ij−h_ijk T_ik−λ ε² E_ijk=ε² D^λ_ijk,
    E_ijk=μ(b_ijk,g_ik).                                 (2.3)

Because (1.1) holds, this defect has no lower-order coefficient. Explicitly,

    D^λ_ijk = W_jk g_ij+g_jk W_ij−W_ik
              +U_jk U_ij+μ(U_jk,g_ij)+μ(g_jk,U_ij)
              +ν(g_jk,g_ij)−b_ijk U_ik−c_ijk g_ik
              −λ μ(b_ijk,g_ik).                         (2.4)

In particular there is one U_jk U_ij term and one −b_ijk U_ik term. No mixed-parameter factor two is inserted.

Apply the single ambient associativity equation

    0=T_kl*(T_jk*T_ij)−(T_kl*T_jk)*T_ij.                (2.5)

The ordinary scalar product-rule errors, obtained directly by expanding *, are

    T_kl*(h_ijk T_ik)−h_ijk(T_kl*T_ik)
       =ε² μ(g_kl,b_ijk)g_ik,

    (h_jkl T_jl)*T_ij−h_jkl(T_jl*T_ij)
       =ε² g_jl μ(b_jkl,g_ij).                         (2.6)

Terms pairing a derivative of b with U, derivatives of c, and ν terms involving εb start at degree three. Define the scalar

    K_ijkl = c_ijk+c_ikl−c_jkl−c_ijl
              +b_ijk b_ikl−b_jkl b_ijl,                (2.7)

which is the degree-two coefficient of h_ijk h_ikl−h_jkl h_ijl. Its degree-one coefficient vanishes by (1.2).

Insert (2.3) into (2.5), using (2.6) at the two scalar endpoints and (2.3) again on the composite edges. Every term of degree two is then displayed in

    0 = g_kl D^λ_ijk−D^λ_jkl g_ij+D^λ_ikl−D^λ_ijl
         +K_ijkl g_il+F_raw−G_raw+λ B(E),               (2.8)

    F_raw=μ(g_kl,b_ijk)g_ik,
    G_raw=g_jl μ(b_jkl,g_ij),
    B(E)=g_kl E_ijk−E_jkl g_ij+E_ikl−E_ijl.            (2.9)

This is a direct ambient-star associator calculation. It neither assumes that (0.1) is an associative twist operation nor assumes that its scalar h satisfies a second-order cocycle.

## 3. The row coboundary of the correction, including its sign

Use LEFT normalization

    M^λ_ijk=g_ik⁻¹ D^λ_ijk,
    N_ijk=g_ik⁻¹ μ(b_ijk,g_ik),
    F=g_il⁻¹F_raw,       G=g_il⁻¹G_raw,

and the row Čech convention

    (δ_row N)_ijkl
       =g_ij⁻¹N_jkl g_ij−N_ikl+N_ijl−N_ijk.           (3.1)

Multiply (3.1) on the left by g_il and use the row transition identities:

    g_il δ_row N
      =μ(b_jkl,g_jl)g_ij−μ(b_ikl,g_il)
         +μ(b_ijl,g_il)−g_kl μ(b_ijk,g_ik).

Using b_ijl−b_ikl=b_ijk−b_jkl from (1.2), and using both decompositions g_il=g_jl g_ij=g_kl g_ik, this becomes

    μ(b_jkl,g_jl)g_ij−μ(b_jkl,g_jl g_ij)
      +μ(b_ijk,g_kl g_ik)−g_kl μ(b_ijk,g_ik)

      =−g_jl μ(b_jkl,g_ij)+μ(b_ijk,g_kl)g_ik
      =−G_raw−F_raw.                                   (3.2)

Thus the exact correction identity is

    δ_row N=−F−G,          B(E)=F_raw+G_raw.             (3.3)

This independent Leibniz derivation verifies the correction sign. In particular it does not depend on the choice of U, W, c or ν.

The four D terms in (2.8) are −g_il δ_row M^λ. Combining (2.8) and (3.3) gives

    δ_row M^λ=K Id+(1+λ)F+(λ−1)G.                      (3.4)

Equivalently, D^λ=D^0−λ E and M^λ=M^0−λ N, so (3.3) makes the same sign transparent. Define

    A_λ=(1+λ)F+(λ−1)G.                                 (3.5)

For determinant-one g, both F and G are linear combinations of conjugates of currents g⁻¹V_d g. These currents have trace zero by differentiating det(g)=1. Hence A_λ is already traceless. More generally, taking trace-free parts of (3.4) would suffice:

    δ_row tf(M^λ)=tf(A_λ),     tf(Z)=Z−tr(Z)Id/2.        (3.6)

A successful extension would have D^λ=0, and therefore A_λ=0 on every common quadruple.

This condition is independent of U and ν. Any scalar c contributes only K Id. Writing W_ij=g_ij w_ij, changing W changes M^λ by

    (δ_row w)_ijk=g_ij⁻¹w_jk g_ij−w_ik+w_ij,

and δ_row²=0 leaves (3.4) unchanged. Thus arbitrary valid first lifts, scalar second coefficients and matrix-valued second correcting edges cannot remove a nonzero A_λ.

## 4. One nonempty common source open for every witness

Use the SAME existing auxiliary carrier Ω_c=f⁻¹D(v_0 v_1 v_3 v_4) for all vertices below. The nonconstant x-map C→P¹ is surjective, its fourth product is surjective, and the coefficient map (P¹)⁴→P⁴ is surjective over C because every binary quartic factors into four binary linear forms, including repeated and infinity factors. Thus f is surjective and Ω_c is a nonempty open of the integral X.

Write a legal mask as the integer m_0+2m_1+4m_2+8m_3. The principal witnesses are the strictly increasing four-mask tuples

    Q_1=(0,1,2,3),       Q_2=(0,2,5,7).                (4.1)

The joint-family corollary additionally uses

    Q_A=(0,1,3,5),       Q_B=(0,2,3,6).                (4.2)

The masks in their union are 0,1,2,3,5,6,7. The common legal locus of all these actual owners is exactly

    L=(U_0∩U_1)_0 × (U_0∩U_1)_1 × (U_0∩U_1)_2 × U_0,3.

Each factor is a nonempty open of the integral curve, so L is dense and nonempty. Consequently Ω_c∩L is nonempty. All owners can use the same finite standard chart, since L is contained in U_0 on every factor. This is a genuine intersection of existing source owners, rather than a new localization invented for a primitive.

On L, r_0,r_1,r_2 and x_0,x_1,x_2 are regular units. Every relevant transition and coefficient is regular on Ω_c∩L by the accepted structural results. V_0 and V_1 annihilate r_2. The fresh bit 2 in Q_2,Q_A,Q_B therefore preserves increasing owner order without contributing to the differentiations. No point, source program, primitive entry or physical polynomial is evaluated.

## 5. Two isolated endpoint anomalies for the fixed ordered b

Set H=diag(1,−1) and r'_d=V_d r_d. On one carrier, use only the abstract cocharacter identities

    D(uv)=D(u)D(v),
    D(z)⁻¹ V D(z)=(Vz/z)H.                             (5.1)

Within each quadruple, its vertices are labeled i=0,j=1,k=2,l=3; these position labels are distinct from their mask values.

### Q_1 forces λ=−1

For masks (0,1,2,3), the ν values are

    1, r_0, r_1, r_0 r_1.

Thus

    g_23=D(r_0),    g_02=D(r_1),    g_03=D(r_0 r_1),
    b_012=(15/4)r_0r_1,             b_123=0.

By (5.1) and left normalization,

    F=(15/8)r'_0 r'_1 H,       G=0,
    A_λ(Q_1)=(1+λ)(15/8)r'_0 r'_1 H.                  (5.2)

The sign is positive: the final edge increases bit 0, and the surviving term is (V_0g_23)(V_1b_012)/2.

### Q_2 forces λ=1

For masks (0,2,5,7), the bit vectors in positions (0,1,2) are

    (0,0,0), (0,1,0), (1,0,1), (1,1,1).

The ν values are 1,r_1,r_0r_2,r_0r_1r_2. In particular,

    g_01=D(r_1),    g_13=D(r_0r_2),    g_03=D(r_0r_1r_2),
    b_012=0,                        b_123=(15/4)r_0r_1.

Since b_012 is the zero section, F=0. For the other endpoint, the transition identity cancels the left factor exactly:

    G=g_03⁻¹g_13 μ(b_123,g_01)=g_01⁻¹ μ(b_123,g_01).

Here V_0g_01=0, V_0b_123=(15/4)r'_0r_1 and g_01⁻¹V_1g_01=(r'_1/r_1)H. Therefore

    F=0,       G=(15/8)r'_0 r'_1 H,
    A_λ(Q_2)=(λ−1)(15/8)r'_0 r'_1 H.                  (5.3)

The sign of G is positive; the negative ordinary anomaly at λ=0 comes from its coefficient λ−1, not from G itself. The r_2 factor contributes no supported derivative and cancels from the displayed normalization.

## 6. Nonvanishing and the fixed-b contradiction

The quotient rule and the curve relation, as rational identities already used in the accepted proof, give

    V(y/x)=[x(3x²−1)/2−y²]/x²=(x²+1)/(2x).

Consequently the common section in (5.2)–(5.3) is

    (15/8)r'_0r'_1 H
       =15(x_0²+1)(x_1²+1)/(32x_0x_1) · H.            (6.1)

Each x_d is nonconstant, so x_d²+1 is not the zero rational function. The product X is integral, and x_0,x_1 are units on Ω_c∩L. Thus (6.1) is regular there and is not identically zero. It may vanish on proper divisors; pointwise nonvanishing everywhere is not needed.

Equation (3.6) on Q_1 therefore requires λ=−1. The same necessary condition on Q_2 requires λ=1. These cannot both hold in characteristic zero. This proves the fixed-b statement for every constant λ.

In particular, left star multiplication (λ=1) leaves twice the Q_1 witness, and right star multiplication (λ=−1) leaves minus twice the Q_2 witness. Ordinary multiplication (λ=0) leaves both with opposite signs. All comparisons keep the actual g, ordered b and common ambient star algebra fixed.

## 7. Bounded joint-family corollary

This section is independently derived and does not use the separate bilinear-repair packet as an accepted dependency. Replace b only within the displayed constant two-parameter family

    b^(A,B)_ijk=A q_0,ij q_1,jk+B q_1,ij q_0,jk.        (7.1)

It is a scalar 2-cocycle. If any first lift exists, the direct associativity argument in §§2–3 applies with this b, since it used only the first-lift equation and scalar cocycle. The conclusion below is necessary even if first-lift existence is not separately known.

For an edge ab of a quadruple put d_ab,s=m_b,s−m_a,s and define

    β_ijk=A d_ij,0 d_jk,1+B d_ij,1 d_jk,0,
    b^(A,B)_ijk=β_ijk r_0r_1.

Same-carrier cocharacter calculus gives the exact general formulas

    F=(β_012/2)(d_23,0−d_23,1) R,
    G=(β_123/2)(d_01,1−d_01,0) R,
    R=r'_0r'_1 H.                                      (7.2)

Indeed, the first formula uses the two logarithmic currents of g_23 and the two derivatives of β_012r_0r_1. The second uses G=g_01⁻¹μ(b_123,g_01). These formulas retain the scalar-slot order and its sign; extra bit-2 currents vanish by product support.

For completeness the four direct substitutions are:

    Q_A=(0,1,3,5): β_012=A, β_123=0,
                      d_23=(0,−1), d_01=(1,0),
                      F=(A/2)R, G=0.

    Q_B=(0,2,3,6): β_012=B, β_123=0,
                      d_23=(−1,0), d_01=(0,1),
                      F=−(B/2)R, G=0.

    Q_1=(0,1,2,3): β_012=A, β_123=B,
                      d_23=(1,0), d_01=(1,0),
                      F=(A/2)R, G=−(B/2)R.

    Q_2=(0,2,5,7): β_012=B, β_123=A,
                      d_23=(0,1), d_01=(0,1),
                      F=−(B/2)R, G=(A/2)R.             (7.3)

The displayed d pairs retain only coordinates 0,1. All four quadruples are strictly increasing actual source masks on the common nonempty open of §4. R is a nonzero section there by §6.

The necessary condition A_λ=0 on Q_A and Q_B gives

    (1+λ)A=0,        (1+λ)B=0.                         (7.4)

If either A or B is nonzero, then λ=−1. Substituting that value into Q_1 and Q_2 gives respectively

    A_−1(Q_1)=B R,       A_−1(Q_2)=−A R,

which force B=0 and A=0, a contradiction. Therefore joint compatibility for every constant λ forces A=B=0. We assert no sufficient condition or existence at A=B=0.

To identify the bounded coboundary-repair subfamily, let e_ij=t q_0,ij q_1,ij with constant t. Additivity of q gives directly

    (δe)_ijk=e_jk−e_ik+e_ij
       =−t(q_0,ij q_1,jk+q_1,ij q_0,jk).

Starting from the original b, this produces A=15/4−t, B=−t, hence A−B=15/4. Moreover U'=U+e g is a regular first lift of b+δe: its change in the first-lift equation is (δe)g. The just-proved necessary A=B=0 is impossible on this affine line for every λ. Thus even simultaneously choosing constant t and constant λ does not repair this family; the antisymmetric choice t=15/8 is included.

This corollary does not cover general scalar coboundaries, arbitrary first coefficients or modified algebra-overlap descent.

## 8. What the calculation does and does not establish

The obstruction here is a nonzero trace-free associativity compatibility term for a fixed family of descent equations. It is not a nonzero same-pair Čech cohomology class: the corresponding second-order defect has a nonzero boundary. It also does not calculate the already-closed mixed representative or determine whether that class is exact.

Allowing algebra transition automorphisms, non-scalar higher twists, a different g, or a first coefficient outside the bounded §7 family changes the problem. The present argument does not exclude any of those possibilities. No broad no-go for star-gerbes, all quantizations or algebraicity is asserted.

The accompanying controls use invented commuting scalar jet labels and free noncommuting words to check the universal algebra, plus small integer mask metadata to check (7.3). They do not construct or evaluate a physical matrix, curve point, source polynomial, production model or residual. The accepted source binding and the geometric nonempty-open/nonzero-section arguments remain the written structural proof. Independent audit is separate.
