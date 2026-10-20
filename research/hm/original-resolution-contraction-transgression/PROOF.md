# A regular vertex-connection reduction of the complementary remainder

## Precise result and limit

This note gives an explicit regular edge-cochain reduction of the complete complementary source representative. It does **not** prove that the remaining source obstruction is zero or nonzero. It also identifies the exact residual for one bounded contraction-only primitive ansatz. That residual need not vanish universally: a tiny rational rank-two control gives precisely `diag(1,-1)/4`. The control is not the physical source.

All source inputs are read at PR79 commit

    8fb699a29b10ee6a53af8f74fb5f909e4c82d6e9.

The indispensable inputs are equation (21) of `supertrace_projection_followup.md`, equations (13)–(15) of the complete-remainder `PROOF.md`, the genuine ordered-nerve convention in `null-permutation-sector/REVIEW.md`, and the accepted `closed-k-source-review/REVIEW.md`. Their exact source files and Git blobs are in `source-pins.json`.

No source polynomial, source transition, source jet, coefficient, detector value, or source-point specialization is computed here. The test script uses invented rational 2-by-2 matrices only. The proof uses the accepted source identities at their stated mathematical scope. 

## 1. Convention: genuine full ordered nerve before projection

Use coordinate labels `1,2,3,4`, with `p=(1,2)` and `q=(3,4)`. On a triple `(i,j,k)`, put

    A=g_ij,  B=g_jk,  g_ik=BA,
    L_a=A^(-1) V_a A,
    U_a=A^(-1) B^(-1) (V_a B) A,
    H_ab=A^(-1) V_a V_b A,
    J_ab=A^(-1) B^(-1) (V_a V_b B) A.

The fields `V_a` are the physical commuting invariant fields, not derivatives with the physical frame held constant. Every matrix on a triple is in the first row frame. For a vertex or edge matrix `X` in frame `j`, write

    X^i = g_ij^(-1) X g_ij.

Thus the second-edge current is `L_jk^i=U`. The source current is a twisted Čech one-cocycle, `L_ik=L_ij+L_jk^i`.

For scalar coefficient functions `f`, write

    (d_V f)_a=V_a f,
    [alpha wedge X]_(a,b)=alpha_a X_b-alpha_b X_a.

Here `d_V` of a contracted scalar is a coefficient one-form; it does not mean exterior differentiation of the uncontracted two-form. In particular `d_V(K_cd)` contains all its symmetric mixed physical derivatives.

Use the genuine all-tuples source extension `t'=s_raw+delta h_scalar`. Do not replace it with guessed antisymmetry or sort tuples before averaging. The gerbe edge correction is not antisymmetric under edge reversal. The algebra proving equation (21), the contraction identities, the transition composition, and the scalar comparison use no inequality between vertex labels, so they also identify this genuine extension on every supplied ordered edge. Restriction to increasing tuples is made only after the identities below. This is the same full-nerve convention as the pinned permutation review.

Let

    e=(1/24) sum_(sigma in S4) sign(sigma) rho(sigma).

This is the full geometric action on coordinates, physical frames, masks, fields and all cochain terms; it leaves tuple positions in place. It commutes with `delta`. All appearances of `1-e` below refer to that full 24-term action. No three-coset replacement is used.

## 2. The regular vertex form and its descent defect

In the accepted physical column normalization,

    G_ij=P_i I_j=g_ij^t,
    Gamma_i=P_i dI_i,
    kappa_i=-(Gamma_i)^0,
    z_ij=P_i Z_ij I_i=-dG_ij G_ij^(-1)=-L_ij^t.

The common-ambient last equality has **no extra scalar line-frame term**. The source projection defect is

    Q_ij=P_i h_j T_j I_i-G_ij P_j T_j h_j I_i,
    T_i,c=V_c D+2 a_i,c D.

It is distinct from the kinetic expression `Q2`. The accepted descent identity is

    G_ij Gamma_j G_ij^(-1)-dG_ij G_ij^(-1)-Gamma_i=Q_ij.

Define row-End one-forms

    theta_i=(Gamma_i^0)^t=-kappa_i^t,
    chi_ij=(Q_ij^0)^t.

Taking the tracefree transpose gives exactly

    theta_j^i-theta_i=L_ij+chi_ij.                    (2.1)

In particular both `L` and `chi` are twisted Čech one-cocycles. This does not assert `chi=0`. Formula (2.1) is an equality in the prescribed physical cohomology frames, rather than a license to recompute `Gamma` after an arbitrary nonconstant cohomology regauging without its derivative correction.

Regularity is important. Equivalently, `theta=-kappa^t` is obtained from the tensorial regular pivot-connection difference in equation (21). A change of local ambient line reference changes `P_i dI_i` by a scalar one-form times the rank-two identity, because the inclusion lies in weight one; tracefree projection removes that change. Thus `theta_i` is a regular row-End one-form on the complete source vertex, including its infinity portions. The source contraction, `T`, and `Q` give regular `chi` on every legal edge. All transports use invertible regular transitions on their declared intersections.

## 3. Exact edge transgression without a closedness assumption

Let `t` be any regular scalar edge cochain of the needed character. Define

    alpha_ij=d_V t_ij,
    S_ij=theta_i+theta_j^i,
    C_r(t)_ij=(1/2)[alpha_ij wedge S_ij]_r.          (3.1)

On a triple, define the completely explicit residual

    B_r(t)_ijk=(1/2)[
        alpha_jk wedge chi_ij
        -alpha_ij wedge chi_jk^i
        +d_V(delta t)_ijk wedge S_ik
    ]_r,                                           (3.2)

where `S_ik=theta_i+theta_k^i`. Scalars on the second edge require no matrix conjugation. Then

    E_r(t)=delta C_r(t)-B_r(t).                     (3.3)

This is a cochain identity, not just a class identity, and does not assume `delta t=0`.

Proof. Write `beta_ij=theta_j^i-theta_i=L_ij+chi_ij`, and transport all terms to frame `i`. The sum in `delta C` is

    2 delta C_r(t)=[
      alpha_jk wedge (2theta_i+2beta_ij+beta_jk^i)
      -alpha_ik wedge (2theta_i+beta_ij+beta_jk^i)
      +alpha_ij wedge (2theta_i+beta_ij)
    ]_r.

Substitute `alpha_ik=alpha_ij+alpha_jk-d_V(delta t)_ijk`. The result is

    2 delta C_r(t)=[
      alpha_jk wedge beta_ij-alpha_ij wedge beta_jk^i
      +d_V(delta t)_ijk wedge S_ik
    ]_r.

The `L` parts give exactly the pinned formula

    E_ab(t)=(1/2){
      (V_a t_jk)L_b-(V_b t_jk)L_a
      +(V_b t_ij)U_a-(V_a t_ij)U_b
    }.

The other parts are (3.2). This proves (3.3), including its signs and coefficient. No physical differentiation of matrix transport is performed in this Čech calculation; there are consequently no missing transport derivatives in this step. Physical differentiation has already occurred in `alpha` and `d_V(delta t)` and must be retained there.

## 4. Apply the identity to the differentiated contraction and Q2

Keep the full source contraction scalar

    K_ij;cd=
      str(h_i T_i,c Z_ij,d-h_i T_i,d Z_ij,c)
      -tr(P_i T_i,c h_i Z_ij,d I_i
           -P_i T_i,d h_i Z_ij,c I_i).              (4.1)

The accepted exact differential is

    delta K=Lambda,
    Lambda_ijk=tr(Q_ij^0 wedge z_jk^i)
                  +(eta_ij/2) wedge W_jk,
    W_jk=tau_k-tau_j+15q_jk.                        (4.2)

The plus sign in (4.2) is essential. The accepted review proves an actual-source `Lambda` nonidentity; it does not prove that its differentiated pairing below is nonzero.

For complementary pairs `(r,s)=(p,q),(q,p)`, abbreviate

    D_(r|s),ijk=[
        d_V K_s,jk wedge chi_ij
        -d_V K_s,ij wedge chi_jk^i
        +d_V Lambda_s,ijk wedge (theta_i+theta_k^i)
    ]_r.                                           (4.3)

Define the bounded regular contraction-only primitive ansatz

    P_K=(1-e)( C_p(K_q)+C_q(K_p) )/4.               (4.4)

The precise source identity is

    (1-e){Q2+[E_p(K_q)+E_q(K_p)]/4}
       =delta P_K+(1-e){Q2-[D_(p|q)+D_(q|p)]/8}.    (4.5)

Consequently this particular primitive absorbs the differentiated contraction **together with Q2 if and only if** the following equality of actual source cochains holds:

    (1-e){Q2-[D_(p|q)+D_(q|p)]/8}=0.               (4.6)

Equation (4.6) is not established for the physical source here. In particular the two `dK wedge chi` terms and the `dLambda wedge (theta_i+theta_k^i)` term cannot be suppressed by saying that `K`, `Q2`, or their sum is closed. This is an exact necessary-and-sufficient test for the stated ansatz only; failure of (4.6) would not rule out another edge primitive.

For clarity, Q2 in (4.5) is not opaque. With

    S={(13,24,+1),(14,23,-1),(23,14,-1),(24,13,+1)},

its exact source formula is

    Q2=(1/8) sum_(ab,cd,epsilon in S) epsilon {
       [tr(U_a U_b)+tr(U_a L_b)+tr(U_b L_a)] H_cd^0
       -tr(H_cd^0 U_a)L_b-tr(H_cd^0 U_b)L_a
       +[tr(L_c L_d)+tr(U_c L_d)+tr(U_d L_c)] J_ab^0
       -tr(J_ab^0 L_c)U_d-tr(J_ab^0 L_d)U_c
    }.                                             (4.7)

The published full alternation identity says `e Q2=0`; there is no analogous deletion of the defect in (4.6).

## 5. The bounded ansatz fails as a universal identity

This is an invented rational rank-two complex, not a source substitution. Work near the origin in four independent variables, with `V_a=partial_(x_a)`, where the following units are invertible:

    a=1+x_2 x_4,  b=(1+x_1)(1+x_3),
    A=diag(a,a^(-1)),  B=diag(b,b^(-1)).

Take a complex concentrated in degree zero with dimension two, `D=h=0`. On three vertices choose

    I_0=1,  I_1=A^t,  I_2=(BA)^t,  P_i=I_i^(-1).

Then `PI=IP=1` and every contraction identity holds. Its physical row transitions are exactly `g_01=A`, `g_12=B`, `g_02=BA`. The split connections `-dI_i I_i^(-1)` are flat and determinant one. Here `K=0`, `Lambda=0`, and `chi=0` identically, so `P_K=0` and every defect in (4.3) is zero.

At the origin, put `h0=diag(1,-1)`. The cross-jet data are

    L_a=0 for all a,
    U_1=U_3=h0, U_2=U_4=0,
    H_24^0=H_42^0=h0, all other cross H^0 zero,
    J_13=J_31=1, all other cross J zero.

Thus every relevant `J^0` is zero. Only `(ab,cd)=(13,24)` contributes in (4.7), and

    Q2=tr(h0^2)h0/8=h0/4.                          (5.1)

The repeated-coordinate Hessians `J_11^0=J_33^0=-h0` are immaterial: every term of Q2 and of its 24 slot permutations uses distinct coordinates. The full signed permutation average of Q2 is zero by its symmetric Hessian slots, or by the independent 24-term check. Consequently `(1-e)Q2=h0/4` on this control. The proposed universal equality (4.6) therefore fails by exactly `h0/4`.

If the source ranks and weight commutator are desired in the control, add constant identity contractible pairs with ranks 5 in degrees `(-1,0)`, 8 in `(0,1)`, and 2 in `(1,2)`. Together with the middle rank-two cohomology these give ranks `(5,15,10,2)` and weights `(-1,1,3,5)`. Let only the two cohomology columns vary as above, and set the forms `a_i=gamma_i=q_ij=0`. The block differential and contraction are constant, `[D,k]=-2D`, `T=[D,A_i]=0`, and the same `K=Lambda=chi=0` and Q2 value follow. This is a formal direct-sum embedding, not a computation with the physical source or a simulation of its D.

This is useful but deliberately bounded: it rules out a universal derivation of (4.6) from contraction, flatness, determinant one and connection descent alone. It does not refute (4.6) for the actual pinned 32-dimensional complex, nor does it say the displayed nonzero cochain has a nonzero cohomology class. Other scalar terms in the complete representative and other possible primitives are not set to zero by this test.

## 6. Every physical contraction derivative is retained

For `a` complementary to `(c,d)`, differentiation of (4.1) gives

    V_a K_cd =
      str( (V_a h)T_c Z_d+h(V_a T_c)Z_d+hT_c(V_a Z_d)
                  -(c exchanged with d) )
      -tr( (V_a P)T_c hZ_d I
           +P(V_a T_c)hZ_d I
           +PT_c(V_a h)Z_d I
           +PT_c h(V_a Z_d)I
           +PT_c hZ_d(V_a I)
                  -(c exchanged with d) ).          (6.1)

All factors carry the same endpoints as (4.1). In particular

    V_a T_i,c=V_a V_c D+2(V_a a_i,c)D+2a_i,c V_a D.  (6.2)

Neither `V_a h`, `V_a I`, `V_a P`, nor either derivative of `D` is frozen. The physical derivatives include the original line-frame derivatives.

For completeness, if `Q_c` denotes the source projection defect in (4.2),

    V_a Lambda_cd =
      tr( (V_a Q_c^0)z_d+Q_c^0(V_a z_d)
                   -(c exchanged with d) )
      +(1/2){(V_a eta_c)W_d+eta_c(V_a W_d)
                   -(c exchanged with d)},         (6.3)

where the second-edge z is transported to frame i **before** differentiating. Thus its derivative includes the derivative of that transport. The exact derivative of Q is

    V_a Q_ij,c =
      (V_a P_i)h_j T_j,c I_i
      +P_i(V_a h_j)T_j,c I_i
      +P_i h_j(V_a T_j,c)I_i
      +P_i h_j T_j,c(V_a I_i)
      -(V_a G_ij)P_j T_j,c h_j I_i
      -G_ij(V_a P_j)T_j,c h_j I_i
      -G_ij P_j(V_a T_j,c)h_j I_i
      -G_ij P_j T_j,c(V_a h_j)I_i
      -G_ij P_j T_j,c h_j(V_a I_i).                 (6.4)

Here `V_a G_ij=(V_a P_i)I_j+P_i(V_a I_j)`. Equations (6.1)–(6.4) are ordinary physical product rules, including every I/P/h/D term. They impose no source calculation and no claim that an antisymmetric curvature identity replaces the symmetric derivatives.

There is also a useful independent closure diagnostic. Because `delta L=0`,

    delta E_r(t)_ijkl=-(1/2)[
      d_V(delta t)_jkl wedge L_ij
      +d_V(delta t)_ijk wedge L_kl^i
    ]_r.                                           (6.5)

Hence even the existence of *some* primitive for the isolated combination in (4.5) requires

    delta Q2=(1/8) sum_(r,s) [
      d_V Lambda_s,jkl wedge L_ij
      +d_V Lambda_s,ijk wedge L_kl^i
    ]_r                                            (6.6)

before projection, or its `(1-e)` image after projection. This is a necessary condition, not a proven source failure or a sufficiency theorem. Nonzero `Lambda` alone cannot decide (6.6).

## 7. Full ordered-nerve reduction, with all surviving source terms

Write the compact scalar without dropping any part as

    t'_s=v_s+K_s/4+w_s+g_s,
    v_s=-(1/4)[tr(kappa_i wedge L_ij^t)]_s,
    w_s=(1/8)[eta_ij wedge tau_j]_s
                         +(15/4)[q_ij wedge d_i]_s,
    g_cd=-15q_c,ij q_d,ij/8.                         (7.1)

Here `d_i` is the regular one-form `gamma_i-a_i`, not an exterior derivative. The source scalar equation remains

    delta t'_s=F_s=b_s-c_s,
    c_cd=(1/4)tr(U_c L_d-U_d L_c).                   (7.2)

Set

    P_full=(1-e){C_p(t'_q)+C_q(t'_p)}.              (7.3)

Then the precise full complementary reduction is

    (1-e){Omega+Q2+Q4+E_p(t'_q)+E_q(t'_p)}
      =delta P_full+(1-e){Omega+Q2+Q4
                         -B_p(t'_q)-B_q(t'_p)}.    (7.4)

Each surviving B term is explicitly

    B_r(t'_s)=(1/2)[
      d_V(v_s+K_s/4+w_s+g_s)_jk wedge chi_ij
      -d_V(v_s+K_s/4+w_s+g_s)_ij wedge chi_jk^i
      +d_V F_s,ijk wedge (theta_i+theta_k^i)
    ]_r.                                           (7.5)

There is a second useful version displaying the Q2/contraction question by itself:

    R30(t')=delta P_K+(1-e){
      Omega+Q4+Q2-[D_(p|q)+D_(q|p)]/8
      +E_p(v_q+w_q+g_q)+E_q(v_p+w_p+g_p)
    }.                                             (7.6)

Here `R30(t')=(1-e)R(t')`; it is not literally the published `Rraw30=(1-e)R_raw`. The accepted comparison is `R(t')=R_raw+delta H_compare`, where `H_compare=B_p(h_scalar,q)+B_q(h_scalar,p)` in the pinned pivot-descent note. Therefore a reduction for the published raw representative follows by replacing `P_full` with `P_full-(1-e)H_compare` in (7.4), or `P_K` with `P_K-(1-e)H_compare` in (7.6), with the displayed residual unchanged. The letter B in the existing comparison is the pinned BI vertex-to-edge operator, not the new triple defect (3.2).

Thus the full source identity retains Omega, Q4, the exact Q2 residual (4.6), the rank-two local-connection term, weighted traces, pivot scalar terms, and the original gerbe correction. No independent closedness is assigned to any summand.

The complementary derivatives of `g_cd` are zero for the accepted source's separated-coordinate reason: for `a` outside `{c,d}`, `V_a q_c=V_a q_d=0`. Thus its contributions to `E_r`, `C_r`, and the first two terms of `B_r` vanish when `r` is complementary. Its `delta g` likewise has zero complementary derivatives. This is a proved cancellation **after** retaining the gerbe term in (7.1), not a deletion of the weighted or pivot terms. In particular

    V_a(q_c d_i,d-q_d d_i,c)
      =q_c V_a d_i,d-q_d V_a d_i,c

for complementary a, and those derivatives generally survive. Derivatives of `eta`, `tau`, `kappa`, and every contraction factor survive as indicated. For example

    V_a v_cd=-(1/4)tr(
       (V_a kappa_c)L_d^t+kappa_c(V_a L_d)^t
       -(V_a kappa_d)L_c^t-kappa_d(V_a L_c)^t),

    V_a w_cd=(1/8){
       (V_a eta_c)tau_j,d+eta_c V_a tau_j,d
       -(V_a eta_d)tau_j,c-eta_d V_a tau_j,c}
       +(15/4){q_c V_a d_i,d-q_d V_a d_i,c}.          (7.7)

Here

    V_a kappa_c=-[(V_a P_i)(V_c I_i)+P_i V_a V_c I_i]^0,
    V_a L_d=H_ad-L_a L_d.

The source gerbe coefficient has zero complementary derivative, so `V_a F_cd=-V_a c_cd` for complementary a. An entirely explicit version of the latter is

    V_a c_cd=(1/4)tr{
      J_ac^0 L_d-J_ad^0 L_c+U_c H_ad^0-U_d H_ac^0
      -(L_a+U_a)(U_c L_d-U_d L_c)
    }.                                             (7.8)

To check (7.8), use `V_a U_c=J_ac-U_a U_c+[U_c,L_a]`, differentiate the two trace products in (7.2), and use coefficient cyclicity. Trace parts of H and J multiply traceless L and U and vanish. This equation retains second jets rather than replacing them by exterior curvatures.

For reference, the retained terms in (7.4) have their pinned explicit meanings

    Omega=(1/8)sum_S epsilon [J_ab,H_cd],
    k_r(X)=[X_a,X_b]/4,
    Q4=(1/2){[k_p(U),k_q(L)]+[k_q(U),k_p(L)]}
          +T4_(p|q)+T4_(q|p)
          -c_q k_p(L+U)-c_p k_q(L+U),

    T4_(ab|s)=(1/4){
      tr(U_a k_s(U))L_b-tr(U_b k_s(U))L_a
      +tr(L_b k_s(L))U_a-tr(L_a k_s(L))U_b
    }.                                             (7.9)

Thus (7.4)–(7.9) specify every survivor; no unnamed lower-order term is hidden in the reduction.

## 8. Full-cover regularity and precise remaining obligation

The cochains `C_r(t')` and `C_r(K)` are finite products of regular source cochains, their physical invariant derivatives, and the regular vertex form `theta`. The invariant fields are regular on the product of curves, including infinity. Applying a regular derivation preserves the structure sheaf of each source open; it introduces no new divisor outside that open's already allowed complement. Matrix transport uses the regular inverse transition on each legal intersection. The same argument applies to the defects B and D. No rational partition of unity, inverse Euler operator, division by a new function, or square root is introduced.

Consequently (7.3) and (4.4) are genuine regular edge cochains on the full cover. Finite geometric averaging preserves this regularity, and restriction to increasing tuples preserves the identities. The nonalternating source gerbe convention is respected throughout. This establishes a full-cover **reduction**, not a primitive for the final obstruction: the residual in (7.4), or equivalently (7.6), is still present.

The actual-source question left by the bounded contraction ansatz is exactly (4.6). The complete source question left by the full reduction is whether the displayed residual in (7.4) is itself a regular boundary. Neither is decided by the invented failure (5.1), the accepted nonclosedness of K, or the previously established sign-sector primitive. No conclusion about a detector value, the remaining thirty coordinates, or global nonvanishing is made.
