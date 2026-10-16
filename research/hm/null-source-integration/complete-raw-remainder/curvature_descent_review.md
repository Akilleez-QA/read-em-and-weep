# Independent review of curvature and contraction-scalar descent

Reviewed on 2026-10-16: `curvature_descent_followup.md`, SHA-256 `3e88449a435b159a1edc3bf595867656481c6903ff19dbf9ce46f174be5298b0`.

## Verdict

Accepted under the already stated source, regularity, and scalar-character premises. The induced-curvature formula, projection descent, and Čech differential of K have the displayed signs. In particular the eta contribution to delta_S K is positive, and omitting K/4 changes the first-order scalar equation by minus Lambda/4.

The flat invented control verifies this positive sign and the failure of a general local-flatness implication. The proposed H1 shortcut remains conditional on the actual pair contractions of Lambda vanishing, or on supplying a replacement correction. Nothing here proves the actual source identity or a global obstruction value.

This review is algebraic. No physical source matrix, polynomial, jet, overlap, or finite projection was evaluated.

## 1. Projection descent and the central pivot term

From the exact projection defect and A_j-A_i=Z_ij+k eta_ij/2,

    G_ij b_j G_ij^(-1)-b_i
       =z_ij+(eta_ij/2)I-Q_ij.

Substituting b_i=-Gamma_i-a_i I and eta_ij/2=a_i-a_j cancels the central term. This gives

    G_ij Gamma_j G_ij^(-1)-dG_ij G_ij^(-1)-Gamma_i=Q_ij.

Adding the pivot coefficient back into Gamma_hat instead gives Q_ij-(eta_ij/2)I. Thus (6) and (7) correctly distinguish the ambient-reference and pivot-induced connections. The tracefree descent (8) follows with -Q_ij^0 on the right.

With the convention z=-dG G^(-1), one has Q=z+delta_S Gamma. Both z and Q satisfy the transported Čech cocycle equation. Their common Atiyah-class interpretation uses this fixed sign convention and does not imply that either representative vanishes.

## 2. Curvature and its compatibility

Differentiating PI=1 gives dP I=-P dI. Hence

    dP(IP) wedge dI=-Gamma wedge Gamma,
    dGamma+Gamma wedge Gamma=dP(1-IP) wedge dI.

Insert 1-IP=Dh+hD. The differentiated identities PD=0 and DI=0 give, respectively,

    dP D=-P dD,
    D dI=-(dD)I.

Both terms therefore have minus signs:

    Curv=-P(dD)h wedge dI-dP h wedge(dD)I.

Replacing dD by T_i=dD+2a_iD is valid because the additional terms are killed by PD=0 and DI=0. No derivative of the actual D is discarded.

Since da_i=0 and the ordinary-wedge cross terms with a central one-form cancel, Gamma_hat has the same curvature. Writing Gamma=-kappa plus a central one-form gives

    Curv^0=-d kappa+kappa wedge kappa.

Here tr(kappa wedge kappa)=0 by ordinary coefficient cyclicity. Finally the transported connection Gamma_i+Q_ij has curvature G_ij Curv_j G_ij^(-1), proving (12) with both positive mixed terms Gamma_i wedge Q and Q wedge Gamma_i.

These are exterior-curvature identities; they impose no vanishing of the symmetric mixed derivatives used by E.

## 3. The positive Čech differential of K

Use K_ij=str(A_i wedge Z_ij)-tr(b_i wedge z_ij), with the second edge transported to the first frame. Since Z is a cocycle,

    delta_S str(A_i wedge Z_ij)
      =str((A_j-A_i) wedge Z_jk)
      =str(Z_ij wedge Z_jk)
        +(eta_ij/2) wedge str(kZ_jk).

The two Z factors are chain maps, so their supertrace is the induced cohomology trace. Meanwhile the exact descent of b gives

    delta_S tr(b_i wedge z_ij)
      =tr(z_ij wedge z_jk)-tr(Q_ij wedge z_jk).

The intermediate central eta term vanishes because tr(z_jk)=0. Subtracting the two calculations yields

    delta_S K=tr(Q_ij^0 wedge z_jk)
                  +(eta_ij/2) wedge str(kZ_jk).

The eta sign is positive. Also

    str(kZ_jk)=delta_S tau_tilde_jk+15eta_jk
             =delta_S tau_jk+15q_jk,

because the -30 delta_S d and +30 delta_S d terms cancel. This proves (1) and (13)–(14). Lambda is an exact Čech two-cocycle; its zero cohomology class is insufficient to make K a closed one-cochain.

## 4. Scalar equation and the conditional H1 shortcut

Since t'=s_alt+K/4, the sign in delta_S s_alt=F-Lambda/4 follows immediately. The separate direct calculation in section 5 agrees. In particular,

    delta_S(eta_ij wedge tau_j)=-eta_ij wedge delta_S tau_jk,
    delta_S(q_ij wedge d_i)=-(delta_S d)_ij wedge q_jk.

The gerbe differential minus b_r is the contraction of -15 q_ij wedge q_jk/8. Together with the q wedge d term it becomes -15 eta_ij wedge q_jk/8. The eta wedge tau term contributes -eta_ij wedge delta_S tau_jk/8. These are precisely the scalar part of -Lambda/4, with no sign change from the row/column contraction convention.

The H1 argument is properly conditional. The source's squared line factors and logarithmic differentials are deck-invariant; the constant deck signs of normalized I and P cancel in their projected products. Thus the uncontracted scalar K is invariant, while contraction by the physical V_c and V_d supplies the pair character. Under the accepted physical-frame regularity, K_r is a regular cochain in the same pair-character sheaf used in BI. If its Čech differential vanishes, BI's affine-cover and H1 argument applies. It then gives K_r=delta_S f_r, and the positive BI identity E(delta_S f)=delta_S B(f) proves (18), including the factor 1/4.

If Lambda_r is not known to vanish, this application of H1 is unavailable. A scalar correction would need differential Lambda_r/4, as stated; K_r/4 is already such a correction. Neither case decides the remaining complete obstruction.

## 5. Independent check of the invented control

For the displayed control, each U_l=(I_l,h_l) has determinant one and D U_l=(0,0,1). Thus the contractions split the same constant differential, and A_l=-dU_l U_l^(-1) is flat with supertrace zero.

The connection coefficients follow directly from Gamma_l=P_l dI_l:

    Gamma_i=0,
    Gamma_j=diag(-dx,0),
    Gamma_k=diag(-dx+dy/u,-dy/u).

They are diagonal with closed entries, so all three induced curvatures vanish. Since G_ij=I and G_jk=M,

    Q_ij=diag(-dx,0),
    z_jk=diag(-dy/u,dy/u).

Their tracefree pairing is +dx wedge dy/u. Also K_ij=0 because all its coefficients use dx, and K_jk=0 because the relative split change preserves the contractible direction. For the remaining edge, A_i=E31 dx and the (1,3) coefficient of Z_ik in the dy direction is -1/u; b_i=0. Hence K_ik=-dx wedge dy/u, giving

    delta_S K=K_jk-K_ik+K_ij=+dx wedge dy/u.

This verifies the claimed sign and the limited logical countercontrol. It has no physical-source or global-obstruction implication. The note correctly retains the independent obligations concerning Omega, Q2, Q4, all complementary E terms, and any finite-domain bounds.
