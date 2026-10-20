> Scope: Historical unknown-value language describes what this argument does not decide, not the current status of later results. All stipulated geometric/source assumptions remain explicit. No actual source evaluation is asserted.

# Ordered-edge connection transgression with its complete defect

## Verdict and scope

This is a universal symbolic identity and a bounded ansatz exclusion. It does **not** prove a regular primitive for the remaining physical obstruction. The new step relative to the specific pinned notes read below is an endpoint-average connection transgression for an arbitrary scalar **edge** cochain, without assuming that cochain closed. It replaces the differentiated contraction by an explicit boundary and two displayed defect families. It also proves that no constant-coefficient endpoint-linear primitive of the stated form can remove those defects universally. It does not exclude a source-specific identity, a larger ansatz, or a combined primitive with Q2.

No physical source was evaluated, no physical transition or derivative instance was constructed, and no detector value was computed. This document makes no novelty claim relative to unread archive material.

## Sources read

Repository: Akilleez-QA/read-em-and-weep.

At commit `8fb699a29b10ee6a53af8f74fb5f909e4c82d6e9`:

- `research/hm/null-source-integration/complete-raw-remainder/supertrace_projection_followup.md`, especially (21), blob f606285d39dd59c9d89a69f93761d9374007a777.
- Same directory `curvature_descent_followup.md`, especially (8), (13), (14), blob 000796a385402f17a9636d5179aad218a9b823ad.
- Same directory `PROOF.md`, especially (13)-(15), blob cf61b556444fa982f4f482de1c9b8414e8f7914c.
- `research/hm/null-source-integration/closed-k-source-review/REVIEW.md`, blob 3616fe3768b5e73b7917c30c82ca6591b0acc043.

At commit `4659e4425c6b5ab6b1899e6af93656ac03ff0862`:

- `research/hm/null-complete-remainder-normal-form/RESULT.md`, blob 3304f6849ee24c0594354c5bbfb4832f77268987.

Public mathematical discussion: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6246445896 and https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6259839595 .

## 1. Conventions and exact assumptions

Use an increasing triple i<j<k. Work in column cohomology frame i. All j and k coefficient matrices are transported there by conjugation with G_ij and G_ik. Transport is transitive. Scalar cochains commute with matrices. Delta is the ordinary ordered Cech differential, with the local-system transport on End coefficients.

Let theta_ij=L_ij^t. Thus the actual induced common-frame difference is z_ij=-theta_ij, with **no added scalar line-frame derivative**. Define Q to be the projection-descent defect of the curvature note, not the kinetic expression Q2. Its tracefree part is denoted qE. The accepted connection equation is

    delta kappa = -theta-qE.                                  (A)

Here kappa_i=(P_i A_i I_i)^0. This is a vertex End-valued one-form; its ordinary transported difference is used, not an invented globally descending connection.

For a scalar edge cochain u and r=(a,b), write

    [du wedge X]_r = (V_a u) X_b-(V_b u) X_a.

The V derivatives act on scalar coefficients in the physical convention. They commute with scalar restrictions and therefore V(delta u)=delta(Vu). No assertion that V commutes with matrix transport is required: no transported matrix is differentiated in the proof. Write f=du, F=delta u. All displayed wedges mean ordinary coefficient wedges, not a total Cech/form product convention.

The transpose of the source operator is exactly

    E_r(u)^t_ijk = (1/2)[f_jk wedge theta_ij
                                      -f_ij wedge theta_jk]_r. (B)

Indeed U^t is theta_jk transported to i. Scalar multiplication introduces no transpose reversal sign. For scalar pair-valued u, the pair contraction is made first, exactly as in the source definition of E.

Regularity premises: each scalar u is a regular cochain in its specified character sheaf on every admitted overlap; V gives the specified regular physical derivative into the relevant coefficient sheaf; the evaluated local kappa_i are regular on their own charts; transition conjugations and restrictions are regular on overlaps; the resulting products have the required output character. These are geometric premises, not established by a rational formula or by a pole count here. Under these premises the edge cochain constructed below is regular. Without them the identity is only an identity of rational cochains.

## 2. The endpoint-average identity

Define

    B_r(u)_ij = (1/2)[du_ij wedge (kappa_i+kappa_j)]_r,        (C)

with kappa_j transported to i. Define the explicit degree-two defect

    D_r(u)_ijk = (1/2)[
        -du_jk wedge qE_ij +du_ij wedge qE_jk
        +dF_ijk wedge (kappa_i+kappa_k)]_r.                  (D)

Then the exact universal identity is

    E_r(u)^t = -delta B_r(u)+D_r(u).                         (E)

Proof. Suppress the pair contraction. Since f_ik=f_ij+f_jk-dF,

    2 delta B = f_jk wedge(kappa_j+kappa_k)
              -f_ik wedge(kappa_i+kappa_k)
              +f_ij wedge(kappa_i+kappa_j)
              =f_jk wedge(delta kappa)_ij
               -f_ij wedge(delta kappa)_jk
               +dF wedge(kappa_i+kappa_k).

Insert (A) and compare with (B). This proves every sign and factor in (D)-(E). In particular the dF term has a **plus** sign. No closedness of u, E_r(u), Q2, or either summand is used.

This formula is distinct from the BI formula E(delta f)=delta B(f), whose input is an already exact scalar cochain and whose primitive uses a scalar vertex cochain. Formula (E) takes the actual possibly nonclosed edge scalar and displays exactly what prevents the endpoint-average primitive from working.

## 3. Differentiated contraction plus Q2

Use K_r for the pair contraction of the full two-term contraction scalar, and Lambda=delta K from the curvature note:

    Lambda_ijk=tr(qE_ij wedge z_jk)
             +(eta_ij/2) wedge(delta tau_jk+15q_jk).         (F)

Here the final q is the scalar gerbe one-form, unrelated to qE. Set

    C_K = [E_p(K_q)+E_q(K_p)]/4,
    B_K = [B_p(K_q)+B_q(K_p)]/4,
    D_K = [D_p(K_q)+D_q(K_p)]/4.

Then

    (Q2+C_K)^t = -delta B_K + Q2^t+D_K.                   (G)

Explicitly,

    D_K = (1/8) sum_(r,s)=(p,q),(q,p) [
       -dK_s,jk wedge qE_ij+dK_s,ij wedge qE_jk
       +d(Lambda_s,ijk) wedge(kappa_i+kappa_k)]_r.          (H)

Thus the specific candidate primitive -B_K succeeds for the combined term **if and only if** Q2^t+D_K=0 as a cochain. A further correction C succeeds if and only if delta C=Q2^t+D_K. Neither identity is proved here. Formula (H) is the exact surviving obligation, with both projection and weighted gerbe terms in Lambda retained. It does not assume either original summand closed.

Every derivative of K is the derivative of its full expression

    K_cd=str(h T_c Z_d-h T_d Z_c)
           -tr(P T_c h Z_d I-P T_d h Z_c I).

For example V of the first unswapped word is str((Vh)T_c Z_d+h(VT_c)Z_d+hT_c(VZ_d)); V of the second is the sum of the five words differentiating P,T_c,h,Z_d,I in their original order. The swapped words have the same derivatives with the original minus signs. In VT, retain V(dD+2aD), so derivatives of D and a survive. Formula (H) is not permission to freeze I,P,h,D. Derivatives of Lambda in (F) include both factors of each wedge and the derivatives of qE, z, eta, tau, and q.

## 4. Complete scalar and surviving full remainder

Put

    S_cd,ij = -(1/4)tr(kappa_i wedge L_ij^t)_cd
              +(1/8)(eta_ij wedge tau_j)_cd
              +(15/4)(q_ij wedge d_i)_cd
              -(15/8)q_c,ij q_d,ij.

The complete source scalar is exactly t'_r=K_r/4+S_r. Nothing in S has been deleted. Hence, before any symmetry projection,

    R(t')^t = -delta B_K
       +Omega^t+Q2^t+Q4^t+D_K
       +E_p(S_q)^t+E_q(S_p)^t.                            (I)

Alternatively apply (E) to the *whole* scalar. Since delta t'_r=F_r,

    R(t')^t = -delta[B_p(t'_q)+B_q(t'_p)]
       +Omega^t+Q2^t+Q4^t+D_p(t'_q)+D_q(t'_p),            (J)

where the last two D terms use dF_q and dF_p respectively, not dLambda/4. This is often safer because it never separates a paired connection/contraction contribution. The source's separated-coordinate statement can set the complementary E derivative of the final q_c q_d term to zero only under that stated source hypothesis; (I)-(J) do not need that deletion.

Applying 1-e_sign is valid to these equalities only if that projection is defined on these cochains and commutes with delta. The primitive is then the corresponding projection of the displayed edge cochain, provided the regularity and character premises in section 1 hold. No claim that the projected residual vanishes follows.

Equations (I)-(J) are alternative decompositions at the original ordered-nerve level. They are NOT an additional deletion to append to the single-boundary four-family normal form at 4659e44. Comparison with that normal form must carry the whole exact identity through its maps; otherwise a boundary can be subtracted twice. No current-curl, selector, homotopy, or nonclosed-defect family from that normal form is declared zero here.

## 5. Rigorous bounded exclusion: endpoint-linear ansatz cannot be universal without defects

Consider all ansatzes with constant coefficients alpha,beta

    P_r(u)_ij=[du_ij wedge(alpha kappa_i+beta kappa_j)]_r.

Direct calculation gives

    delta P = alpha[du_jk wedge(-theta_ij-qE_ij)]_r
             -beta[du_ij wedge(-theta_jk-qE_jk)]_r
             +[dF wedge(alpha kappa_i+beta kappa_k)]_r.     (K)

In the universal algebra of scalar edge cochains and vertex coefficients satisfying only (A), there is no choice alpha,beta with delta P=E_r(u)^t for every u and every such connection datum. To prove this, first restrict to qE=0 and dF=0 and compare the two independent cross monomials in (B),(K). They force alpha=beta=-1/2. With these coefficients, allow arbitrary nonclosed scalar cochains: the extra term is then -[dF wedge(kappa_i+kappa_k)]_r/2 and is not an identity zero. For a wholly formal scalar check, set theta=qE=0 and all kappas to the same nonzero formal one-form c; choose u_ij=u_jk=0 and u_ik with du_ik wedge c nonzero. Then E=0 but delta P=du_ik wedge c, disproving that identity. This is an invented free-symbol control, not a physical input or a matrix instance.

Even with dF=0, arbitrary qE leaves the two qE terms. Thus the root cause is precise: endpoint variation produces the desired antisymmetric cross-current term, but necessarily also the nonclosed-scalar and projection-descent terms. Within this ansatz class there is no tunable coefficient left to remove them.

This bounded exclusion is stronger than merely recording a failed coefficient guess, but weaker than excluding a combined primitive: source K is not a freely variable scalar, qE is constrained by the source, and Q2 may cancel the residual in (H). The test above therefore does not refute any physical source-specific cancellation. The exact physical question Q2^t+D_K=delta C remains open. No nonvanishing or retained-value claim follows.
