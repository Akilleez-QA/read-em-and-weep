# Full constant two-direction cup ansatz: scalar-side compatibility forces zero

## Result and scope

Retain the accepted actual row transitions g, p=(0,1), one common ambient associative star product with first coefficient

    μ(H,G)=((V_0 H)(V_1 G)−(V_1 H)(V_0 G))/2,

and the scalar-side modification with a constant λ:

    T_jk*T_ij = h_ijk T_ik + λ ε² μ(b_ijk,g_ik) mod ε³,
    T=g+εU+ε²W,     h=1+εb+ε²c.

Allow the full constant cup ansatz

    b_ijk = D q_0,ij q_0,jk + A q_0,ij q_1,jk
          + B q_1,ij q_0,jk + E q_1,ij q_1,jk,
    q_d,ij=(m_j,d−m_i,d)r_d,      r_d=y_d/x_d.

Here D=C00, A=C01, B=C10, E=C11 are arbitrary complex constants. Necessary second-order associativity compatibility forces

    D=A=B=E=0,

for every constant λ. This is strictly stronger than the accepted off-diagonal exclusion. Diagonal cup terms cannot cancel the four existing cross-term witnesses; two additional strictly increasing actual mask tuples exclude the remaining pure diagonal possibility.

This is a necessary condition only. No existence at b=0 is claimed. The statement is conditional on any valid first lift U and is independent of that choice, arbitrary scalar c, matrix second edge W, and the associative second star coefficient. No actual source program, model, primitive matrix, physical polynomial, curve point, jet, detector or residual is executed or evaluated. All calculations below are structural identities; the optional control reads only integer mask metadata.

## Dependencies and conventions

Use these accepted packets in the parent directory:

- same-pair-scalar-twist-side-exclusion-20261018/PROOF.md, especially §§1–4 and the signed compatibility identity (3.4).
- constant-bilinear-twist-repair-exclusion-20261018/PROOF.md, for the accepted original first lift and scalar-edge repair convention.

The first packet proves the following identity for every scalar additive-cup 2-cocycle b, not just its displayed off-diagonal examples. With LEFT normalization of the second-order equation defect M, it reads

    δ_row M = K Id + (1+λ)F+(λ−1)G,
    F=g_il^−1 μ(g_kl,b_ijk)g_ik,
    G=g_il^−1 g_jl μ(b_jkl,g_ij),
    K=c_ijk+c_ikl−c_jkl−c_ijl+b_ijk b_ikl−b_jkl b_ijl.

The correction sign follows from δ_row(g_ik^−1 μ(b_ijk,g_ik))=−F−G. Its derivation uses only scalar cocycle, ambient associativity, and Leibniz, so it applies unchanged here. Each q is additive on edges. Expanding (a_a+v_a)(v_b+w_b) verifies the scalar cocycle for every ordered cup q_a,ij q_b,jk, including a=b. Therefore the full b above is a scalar 2-cocycle.

The determinant-one currents are trace-free. On a same-carrier quadruple the accepted cocharacter reduction gives

    g_ab=D_cochar(ν_b/ν_a),
    D_cochar(z)^−1 V D_cochar(z)=(Vz/z)H,
    H=diag(1,−1),       ν_a=product_d r_d^(m_a,d).

Thus F and G below are multiples of H and already trace-free. A successful extension has M=0, so necessarily

    (1+λ)F+(λ−1)G=0.                                  (1)

The scalar K cannot cancel this term. This also explains why none of U,W,c or the second star coefficient can repair the necessary condition.

## General structural endpoint formula

For positions i,j,k,l of a mask quadruple put

    u_s=m_j,s−m_i,s,   v_s=m_k,s−m_j,s,
    w_s=m_l,s−m_k,s,          s=0,1.

Write

    α=u_0v_0, γ=u_1v_1, β=A u_0v_1+B u_1v_0,
    α'=v_0w_0, γ'=v_1w_1, β'=A v_0w_1+B v_1w_0.

Then b_ijk=Dαr_0²+βr_0r_1+Eγr_1², with the analogous primed formula for b_jkl. Define rational sections

    R=r'_0r'_1 H,      r'_d=V_d r_d,       t=r_0/r_1.

Cocharacter calculus, product-factor support and the scalar-slot order in μ give

    F=[−D α w_1 t + β(w_0−w_1)/2 + E γ w_0/t] R,
    G=[ D α' u_1 t + β'(u_1−u_0)/2 − E γ' u_0/t] R.   (2)

For example, the D term in F is

    −(1/2)w_1(r'_1/r_1)(2Dαr_0r'_0)H
       =−Dαw_1 t R.

The E term in G has the minus sign because it comes from
−(V_1b_jkl)(V_0g_ij)/2. The normalization for G is exactly
G=g_ij^−1 μ(b_jkl,g_ij). The F normalization conjugates by g_ik, which commutes with these cocharacter currents. This derives (2) without expanding any primitive transition. Any bit-2 factor is killed by both supported derivations.

## Common actual source domain

Use the same accepted auxiliary carrier

    Ω_c=f^−1D(v_0v_1v_3v_4)

for every vertex. Its nonemptiness follows from the accepted surjectivity of the product x-map and the binary-quartic coefficient map. All six tuples below use masks in {0,1,2,3,4,5,6,7}, where the integer encoding is m_0+2m_1+4m_2+8m_3. They share the genuine legal open

    L=(U_0∩U_1)_0 × (U_0∩U_1)_1 × (U_0∩U_1)_2 × U_0,3.

Here C is the smooth projective complex curve y²=x³−x,
U_0=C\{O}, and U_1=C\{P_0,P_1,P_−1}. Each factor of L is a nonempty open. The accepted X=C⁴ is integral; hence Ω_c∩L is nonempty. Fix the same finite standard tag at every vertex, possible because L lies in U_0 in every factor. Increasing integer masks then give increasing actual full owner keys. No new localization or invented owner is introduced. The functions r_0,r_1,r_2 and x_0,x_1,x_2 are regular units on this common open.

## Rational independence, with product assumptions explicit

The accepted quotient-rule identity is

    r'_d=(x_d²+1)/(2x_d).

Each x_d is a nonconstant rational function. The product X is integral over the algebraically closed field C, so its rational function ring is a field and each factor's nonzero rational functions pull back injectively. Thus r'_0r'_1 is nonzero. Restriction to Ω_c∩L remains nonzero; nowhere-vanishing is not required. Consequently one can cancel the nonzero rational section R in a scalar equality of its multiples.

We also need independence of 1 and t, and of 1 and t^−1, over C. Here is a structural proof that avoids any choice or evaluation of a point. The elliptic involution (x,y)↦(x,−y) on the first curve factor induces a C-automorphism σ of the product function field C(X), fixing the other three factors. It sends r_0 to −r_0 and fixes r_1, so σ(t)=−t. Because t is nonzero and the characteristic is zero, t cannot be a constant. The same argument applies to t^−1. Thus a+bt=0 or a+bt^−1=0, for constants a,b, forces a=b=0 (apply σ and subtract).

This uses the actual independent curve-product structure: the factorwise involution exists globally on X and acts on its field. The carrier Ω_c need not be invariant under σ. An identity on its nonempty common open first extends to the rational function field, where σ can be applied. No independence of arbitrary functions on arbitrary non-product varieties is assumed, and no independence among 1,t,t^−1 jointly is needed.

## The four existing witnesses and diagonal contamination

Formula (2) yields the following complete endpoint table, with each entry giving the scalar multiplying R:

    Tuple                F/R                   G/R
    Q_A=(0,1,3,5)         A/2                   E/t
    Q_B=(0,2,3,6)        −B/2                  −Dt
    Q_1=(0,1,2,3)         A/2                  −B/2
    Q_2=(0,2,5,7)        −B/2                   A/2

For transparency, their consecutive supported differences (u,v,w) are

    Q_A: ((1,0),(0,1),(0,−1)),
    Q_B: ((0,1),(1,0),(−1,0)),
    Q_1: ((1,0),(−1,1),(1,0)),
    Q_2: ((0,1),(1,−1),(0,1)).

In particular Q_A and Q_B no longer have G=0: their diagonal contributions must not be silently discarded. Applying (1) to these two tuples and using the rational independence just proved gives

    (1+λ)A=0,    (λ−1)E=0,
    (1+λ)B=0,    (λ−1)D=0.                            (3)

If either A or B is nonzero, (3) gives λ=−1. The diagonal-free Q_1 and Q_2 then give respectively B=0 and A=0, a contradiction. Hence

    A=B=0,       (λ−1)D=(λ−1)E=0.                     (4)

This answers the narrow cancellation question already using the four existing witnesses: diagonal cups cannot save either off-diagonal coefficient. However these four witnesses alone leave the possibility λ=1 with pure diagonal b. Excluding that possibility requires another step.

## Two additional increasing witnesses exclude the diagonals

Take

    Q_D=(0,1,4,6),    (u,v,w)=((1,0),(−1,0),(0,1)),
    Q_E=(0,2,4,5),    (u,v,w)=((0,1),(0,−1),(1,0)).

These are strictly increasing actual masks on the same common open. Formula (2), before any coefficient is set to zero, gives

    Q_D: F=Dt R,       G=(A/2)R,
    Q_E: F=−(E/t)R,   G=−(B/2)R.                      (5)

After A=B=0, equation (1) on these tuples forces

    (1+λ)D=0,       (1+λ)E=0.                          (6)

Combining (6) with (4) yields 2D=2E=0. Characteristic zero gives D=E=0. Together with A=B=0, this proves the claimed full constant-cup exclusion for every constant λ.

## Corollary: all constant same-edge quadratic scalar repairs fail

The proof also excludes simultaneously choosing λ and a scalar edge repair

    e_ij=s q_0,ij²+t_0 q_0,ij q_1,ij+u q_1,ij²,

with constant s,t_0,u, starting from b^0=(15/4)q_0,ij q_1,jk. Edge additivity and δe=e_jk−e_ik+e_ij give

    δ(q_d²)_ijk=−2q_d,ij q_d,jk,
    δ(q_0q_1)_ijk=−q_0,ij q_1,jk−q_1,ij q_0,jk.

Thus the repaired coefficients are

    D=−2s, A=15/4−t_0, B=−t_0, E=−2u,

and A−B=15/4 prevents all four from vanishing. Every such repair has the regular first lift U'=U^0+e g by the accepted scalar-edge correction identity; diagonal squares are regular on their legal edges for the same reason as the cross product. Therefore this whole bounded quadratic repair family fails at second order, for every λ.

This does not classify general scalar coboundaries, variable coefficient cups, arbitrary first scalar cochains, algebra-overlap automorphisms, changed g, non-scalar higher twists, other deformation formulations, a mixed class's exactness, or algebraicity. The obstruction is a trace-free associativity compatibility term, not a claim of a closed non-exact same-pair Čech class. Independent audit is still required; the tiny metadata control is only a transcription check.
