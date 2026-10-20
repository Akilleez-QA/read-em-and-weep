Editorial scope: This is a mathematical source edition. Historical review and check statements describe the original artifact, not a fresh run. Supporting snapshots are dependencies, not additional new results. Later PR145 mixed-class vanishing supersedes historical unknown mixed-class status; it does not resolve the six pure diagonal conditions.

Supporting dependency only: this complete source text is not a fresh result of this packet.

# Midpoint connections expose a curvature term, not a vanishing jet remainder

## Result and scope

In the pinned first-row frame, the complete new jet family has the exact identity

    S2 = sum_a ∇^P_a Φ_a + C4 + M2.                         (1)

Here Φ is explicit below, C4 is a quartic curvature correction, and M2 is an explicit current–second-jet family. Consequently

    R_alg = Q4 + sum_a ∇^P_a Φ_a + C4 + M2,                (2)

with the FULL existing Q4 retained. The proposed shortcut of discarding M2 is false as a universal identity. After applying the actual nonconstant coefficient kernel, (1) also produces its full covariant-adjoint derivative. Neither the covariant divergence nor this local rewriting proves a zero residue, a Čech boundary, or cancellation of the complete remaining target.

This is formal algebra over a commutative Q-algebra. No actual source, model, owner, current or jet values, matrix-polynomial products or experiments were used. The checker only expands scalar indeterminates with rational coefficients and fixed trace/Lie structure constants. The reported remote commit ba479d5073c1357b2cdfac4e5796ee8747a15132 and PR1 comment 6250556252 are supplied context, not newly authenticated here.

## 1. Exact input and midpoint identities

Use commuting physical derivations V_1,...,V_4, determinant-one transitions A=g_ij, B=g_jk and G=BA, and the exact first-endpoint inputs

    L_a=A^-1(V_a A),
    U_a=A^-1 B^-1(V_a B)A,
    T_a=L_a+U_a,
    H_ab=tf(A^-1 V_a V_b A),
    J_ab=tf(A^-1 B^-1(V_a V_b B)A).

Thus H_ab=H_ba and J_ab=J_ba. Every B quantity is transported by the literal A^-1(...)A before any bracket or trace. Write d(X,Y)=tr(XY).

Define two auxiliary connection coefficients IN THIS fixed physical trivialization:

    P_a=L_a/2,             Q_a=L_a+U_a/2,
    ∇^P_a X=V_a X+[P_a,X], ∇^Q_a X=V_a X+[Q_a,X].

The exact derivative relations are

    V_a L_b=H_ab-[L_a,L_b]/2,
    V_a U_b=J_ab-[L_a,U_b]-[U_a,U_b]/2.                   (3)

The second relation includes the derivative of A^-1(...)A. Indeed differentiating that transport contributes [U_b,L_a]. Therefore

    H_ab=∇^P_a L_b,        J_ab=∇^Q_a U_b,
    Q_a-P_a=T_a/2,
    ∇^P_a U_b=J_ab-[T_a,U_b]/2.                         (4)

Maurer–Cartan gives flat coefficients 0,L,T. Interpolation between these flat endpoints gives, for C_a(t)=t L_a and E_a(t)=L_a+t U_a,

    F^C(t)_ac=t(t-1)[L_a,L_c],
    F^E(t)_ac=t(t-1)[U_a,U_c].

In particular the midpoint connections required in (4) are GENERALLY CURVED:

    F^P_ac=-[L_a,L_c]/4,   F^Q_ac=-[U_a,U_c]/4.           (5)

These follow directly by substituting (3) into V_a P_c−V_c P_a+[P_a,P_c] and its Q analogue. Within the two displayed affine interpolation families, requiring the normalized symmetric jets in (4) forces t=1/2 as a universal identity: at general t the extra term is (t−1/2)[L_a,L_b], respectively (t−1/2)[U_a,U_b]. Moving to a flat endpoint changes the jet formula; it cannot remove curvature for free.

These are fixed-frame auxiliary covariant derivatives, not a declaration that normalized physical jets are tensorial under arbitrary coordinate-dependent changes of endpoint frames. To use another trivialization one must transport the full auxiliary connection and all physical jet definitions. Resetting the reference connection to zero after such a change is not licensed.

## 2. The entire S2 and the explicit remainder

Throughout sum_e means exactly these FOUR entries, with no full S4 alternation:

    (a,b,c,d,e)=(1,3,2,4,+1), (1,4,2,3,-1),
                (2,3,1,4,-1), (2,4,1,3,+1).

Set

    a_ab=d(T_a,T_b)-d(L_a,L_b),
    b_cd=d(T_c,T_d)-d(U_c,U_d).

The complete input is

    8 S2=sum_e e{[J_ab,H_cd]+a_ab H_cd+b_cd J_ab
                    -d(U_a,H_cd)L_b-d(U_b,H_cd)L_a
                    -d(J_ab,L_c)U_d-d(J_ab,L_d)U_c}.       (6)

Define

    Φ_1=([U_3,H_24]-[U_4,H_23])/8,
    Φ_2=(-[U_3,H_14]+[U_4,H_13])/8,
    Φ_3=Φ_4=0,

    C4=(1/64)sum_e e[U_b,[[L_a,L_c],L_d]]
      =([U_3,[[L_1,L_2],L_4]]
         -[U_4,[[L_1,L_2],L_3]])/32,                    (7)

and retain the ENTIRE linear-jet correction

    M2=(1/8)sum_e e{
          a_ab H_cd+b_cd J_ab
          -d(U_a,H_cd)L_b+d(U_b,H_cd)U_a
          -d(T_a,H_cd)U_b
          -d(J_ab,L_c)U_d-d(J_ab,L_d)U_c}.               (8)

In particular (8) has not discarded the original J-current terms. Its H-current terms include the exact connection-mismatch correction from (4).

## 3. Proof of (1), including the curvature coefficient

The connection acts as a derivation of the bracket. Thus (4) gives for every entry

    [J_ab,H_cd]
      =∇^P_a[U_b,H_cd]−[U_b,∇^P_a H_cd]
         +[[T_a,U_b],H_cd]/2.                            (9)

The entry set is antisymmetric under a↔c, with b,d fixed. Since H_cd=∇^P_c L_d,

    sum_e e[U_b,∇^P_a H_cd]
      =(1/2)sum_e e[U_b,(∇^P_a∇^P_c−∇^P_c∇^P_a)L_d]
      =(1/2)sum_e e[U_b,[F^P_ac,L_d]].                   (10)

There is no derivative of U_b in this antisymmetrization: (10) only compares the second term on the right of (9); its derivative-of-U contribution was already retained in the first and third terms of (9).

Substituting (5) into minus (10), with the outside factor 1/8 in (6), produces exactly +1/64 times the signed nested bracket in (7). This fixes both the plus sign and coefficient of C4.

Rank two supplies

    [[X,Y],Z]=2(d(Y,Z)X−d(X,Z)Y).

Therefore the final term of (9) is

    [[T_a,U_b],H_cd]/2
       =d(U_b,H_cd)T_a−d(T_a,H_cd)U_b.

Adding this to ALL linear-jet terms of (6), the +d(U_b,H_cd)L_a part cancels precisely the original −d(U_b,H_cd)L_a. What remains is (8). The differentiated brackets sum to the Φ in (7). This proves (1).

This is a covariant integration-by-parts identity. It uses one paired antisymmetrization and curvature, not the already established full-sign exterior transgression. The existing full-S4 boundary result does not dispose of (8).

## 4. Explicit obstruction to the proposed truncation

In universal traceless coordinates (z,x,y),

    d(X,Y)=2z_X z_Y+x_X y_Y+y_X x_Y.

The coefficient of the scalar monomial

    z_U1 z_U3 z_H24

in the z-coordinate of M2 is exactly 1/4. Only the positive (13,24) entry contributes. Its a_13 H_24 term contributes 2 before the overall 1/8. The +d(U_3,H_24)U_1 and −d(T_1,H_24)U_3 contributions cancel each other for this monomial; all other terms have different variable support. Neither C4 nor Q4 contains an H variable.

This is coefficient extraction from a universal identity, not a numerical specialization or evaluation of any jets. It proves M2 is not the zero polynomial and specifically refutes

    S2 = sum_a ∇^P_a Φ_a + C4

with the displayed Φ and C4. It does NOT prove that no different flux exists, that the physical source specializes to nonzero M2, or that the complete weighted obstruction is nonzero. Derivatives of a different flux or other source families could still cancel it.

## 5. The full Q4 stays in the same identity

For p=(a,b), r=(i,j) in ((12),(34)) or ((34),(12)), put

    BL_p=[L_a,L_b], BU_p=[U_a,U_b],
    M_p=[L_a,U_b]+[U_a,L_b],
    Delta_p=d(U_a,L_b)−d(U_b,L_a).

The retained quartic is exactly the supplied Q4=R22+R31:

    R22=([BU_12,BL_34]+[BU_34,BL_12])/32
           −(Delta_12 M_34+Delta_34 M_12)/16,

    R31=(1/32)sum_(p,r){
          [U_b,[L_a,BU_r]]−[U_a,[L_b,BU_r]]
          +[L_a,[U_b,BL_r]]−[L_b,[U_a,BL_r]]}.

C4 is an ADDITIONAL quartic term in this representation, not a replacement for Q4. The old −c_P k_Q,ik−c_Q k_P,ik corrections remain inside Q4: both F=b−c branches were already included in deriving R_alg=Q4+S2. No F or raw scalar is replaced by an endpoint value. No central term is removed before the original tracefree projection.

## 6. Pairing with the actual nonconstant kernel

For each original residual occurrence use the complete scalar linear functional

    K_lambda(X)=p w_lambda ell_lambda(X)

in the pinned frame. This includes the actual test, all original weights, HPL factors, restrictions, selector and the prescribed transpose. Define its induced coefficient derivative by

    K_lambda;a^P(X)
      =V_a(K_lambda(X))−K_lambda(∇^P_a X)
      =K_lambda;a(X)−K_lambda([L_a/2,X]).                 (11)

It is linear in X over the coefficient algebra. Equation (1) implies the exact scalar identity

    K_lambda(R_alg)
       =sum_a V_a(K_lambda(Φ_a))
          +K_lambda(Q4+C4+M2)
          −sum_a K_lambda;a^P(Φ_a).                     (12)

For a local trace-dual representative K_lambda(X)=d(W_lambda,X),

    K_lambda;a^P(X)=d(V_a W_lambda+[L_a/2,W_lambda],X).    (13)

Thus the commutator correction has a PLUS sign in the dual-matrix derivative. All derivatives of p, weights, HPL coefficients and selectors stay inside V_a W_lambda. The local existence of this representative does not authenticate a smaller detector family, and we do not construct or evaluate W_lambda.

Only the algebraic R_alg slot in the complete remaining-target normal form is replaced. The actual Ccur terms, coupled test/selector term, cohomology-current and overlap-homotopy insertions, the same K_d Delta Z_d defect, and its one existing Čech boundary remain unchanged. This local Φ is not that previously defined Čech homotopy K_d; no second copy of the old boundary is subtracted.

The first term in (12) is an ordinary physical-derivative flux before the existing extraction/coordinate conversion. Converting it to rational-coordinate flux requires the same source-adjoint derivation/extraction premises. Even where that conversion is admitted, the final term in (12) survives. A covariant divergence by itself is therefore not a zero-residue certificate. No independent pole/owner-domain assertion for the newly split terms, rational-divergence certificate, closure claim or obstruction value is made.

## 7. Formal checks and provenance

check.py verifies the transport-mismatch collection for all four signs, (1) coefficientwise with a completely arbitrary symmetric remainder of the second covariant derivatives, both midpoint curvatures, and the explicit surviving coefficient. It rejects omission or sign reversal of C4, omission of the moving-transport correction, and omission of M2. The symmetric remainder cancels by the a↔c pairing; only the universal connection commutator identity is imposed. The source geometric identities and moving-frame normalization are established by the displayed proof and pinned premises, not independently recovered from source values by the checker.

The polynomial helper code is copied from the supplied rank-two checker (standard library only). It never constructs a matrix, substitutes a source value, or multiplies matrix polynomials. Normal and python -O runs are recorded. This is author checking, not an independent review.

Read inputs: rank-two-jet-reduction-public/RESULT.md and REVIEW.md; its current-kernels, quartic, corrected-full-sign, common-frame-correction, baseline-audit and current-audit dependencies; complete-remainder-normal-form-public/RESULT.md and its supplied dependency packet, especially current-curl and source-adjoint. The midpoints and (1), (7), (8), (12) are the bounded new deduction. Existing full-sign transgression, Q4 and complete-normal-form conclusions remain prior results with their original premises.
