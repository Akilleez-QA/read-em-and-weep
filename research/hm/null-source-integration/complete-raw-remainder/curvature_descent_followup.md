# Curvature, projection descent, and the exact test for removing the contraction scalar

## Result

The surviving contraction term K from the full supertrace reduction has an explicit Cech differential. On a source triple, with the second edge transported to the first cohomology frame,

    (delta_S K)_ijk
      = tr(Q_ij^0 wedge z_jk)
        +(eta_ij/2) wedge( delta_S tau_jk+15q_jk )
      =: Lambda_ijk.                                       (1)

Here z_ij=-L_ij^t, and Q_ij is the exact projection defect from the previous proofs. The PLUS sign of the eta term follows from A_j-A_i=Z_ij+k eta_ij/2.

Consequently, deleting K/4 from the compact scalar representative gives an explicit candidate s_alt satisfying

    delta_S s_alt,r = F_r-(1/4)contraction_r Lambda.         (2)

This decides the proposed closed-scalar shortcut precisely. It works if the actual source proves contraction_p Lambda=contraction_q Lambda=0. Under that condition the accepted scalar H1 vanishing and BI remove both complementary E(K) terms by a global boundary. The curvature and descent identities derived here do not themselves establish that additional pairing identity.

The exact induced curvature is also a two-term expression involving the same covariant derivative T_i and the source contraction. A small invented complex below satisfies the relevant determinant-one and local-flatness conditions but has Lambda nonzero. It verifies the signs and shows why local curvature identities alone do not supply the missing pointwise equality. It is not an actual-source or global-obstruction counterexample.

## 1. Source inputs and notation

Use the [original first-order source](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/first-order-source.md), [physical-frame theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-geometric-dependencies/frames-and-poles.md), [BI scalar comparison and H1 argument](https://github.com/Akilleez-QA/read-em-and-weep/blob/e93cf712f9da4926a8450cc870ed45a7bfc379ab/research/codex-swarm/source-boundary-analysis/PROOF.md), and the [full supertrace reduction published at 75f94a9](https://github.com/Akilleez-QA/read-em-and-weep/commit/75f94a9a1682e32b79869998548c74c519e6cc9e).

Retain the physical column-frame convention G_ij=P_i I_j=g_ij^t. The source contractions satisfy

    P_i I_i=1,  D I_i=0,  P_i D=0,
    E_i=I_iP_i=1-Dh_i-h_iD.

The symbol h_i in this note is the complex contraction, not the scalar vertex correction used in the pivot-descent note. All coefficient products are in a common physical ambient frame. Exterior wedges are ordinary coefficient wedges; Cech endpoints retain their source order. No total Cech/forms-product sign is silently inserted.

The established notation is

    A_i=Btilde_i=nabla'_i-nabla_(a_i),
    d_i=gamma_i-a_i,  eta_ij=-2(a_j-a_i)=q_ij+2(delta_S d)_ij,
    Z_ij=A_j-A_i-k eta_ij/2=nabla'_j-nabla'_i,
    T_i=[D,A_i]=nabla_(a_i)D=dD+2a_iD,
    z_ij=P_i Z_ij I_i=-dG_ij G_ij^(-1)=-L_ij^t,
    b_i=P_i A_i I_i,  kappa_i=b_i^0,
    tau_tilde_i=str(kA_i)=tau_i-30d_i.

In particular [D,Z]=0, tr(z)=0, str(k)=0 and str(k^2)=-30. The previous result gives

    K_ij=str(A_i wedge Z_ij)-tr(b_i wedge z_ij),             (3)

equivalently

    K_ij;cd=str(h_i T_i,c Z_ij,d-h_i T_i,d Z_ij,c)
       -tr(P_i T_i,c h_i Z_ij,d I_i
                         -P_i T_i,d h_i Z_ij,c I_i).

Formula (3) retains the full four-block supertrace through its exact projection identity. The matrix Q below is unrelated to the previously named kinetic expressions Q2 and Q4.

## 2. Induced connection and exact projection descent

Define, in the source's prescribed parallel cohomology frame,

    Gamma_i=P_i dI_i,
    Gamma_hat_i=Gamma_i+a_i I,
    kappa_i=-Gamma_i^0=-Gamma_hat_i^0.                      (4)

Gamma_hat is the connection induced from the pivot ambient connection; Gamma uses the local ambient reference derivative. The distinction matters for their full scalar descent, although their tracefree parts agree. These are not asserted to be coefficients of one global connection on the cohomology bundle.

The previous matrix projection identity applied to A_j is

    P_i A_j I_i-G_ij(P_j A_j I_j)G_ij^(-1)=Q_ij,
    Q_ij=P_i h_j T_j I_i-G_ij P_j T_j h_j I_i.              (5)

Because A_j-A_i=Z_ij+k eta_ij/2 and k acts as +1 on the middle bundle containing the cohomology inclusion,

    G_ij b_j G_ij^(-1)-b_i
       =z_ij+(eta_ij/2)I-Q_ij.

Using b_i=-Gamma_i-a_i I and eta/2=a_i-a_j gives the exact full connection equation

    G_ij Gamma_j G_ij^(-1)-dG_ij G_ij^(-1)-Gamma_i=Q_ij.    (6)

For the projected pivot connection the corresponding equation is

    G_ij Gamma_hat_j G_ij^(-1)-dG_ij G_ij^(-1)
                           -Gamma_hat_i=Q_ij-(eta_ij/2)I.  (7)

Thus the tracefree statement, with all frames included, is

    G_ij kappa_j G_ij^(-1)-kappa_i+L_ij^t=-Q_ij^0.         (8)

The distinction between (6) and (7) prevents losing the central pivot difference. Likewise the formula -P_i dI_i for kappa is tied to the prescribed parallel cohomology frames; an arbitrary new nonconstant cohomology gauge requires its derivative term.

Equation (6) and the transition cocycle imply delta_S Q=0. More explicitly, with twisted transport understood,

    Q_ik=Q_ij+G_ij Q_jk G_ij^(-1).

Since Q=z+delta_S Gamma in these fixed source frames, Q and z represent the same Atiyah class of the cohomology bundle, with the convention z=-dG G^(-1). This does not say Q vanishes as a cochain or that the complete second-order obstruction is that Atiyah class.

## 3. Curvature is an explicit covariant-differential defect

The curvature of Gamma_i is

    Curv_i=dGamma_i+Gamma_i wedge Gamma_i
          =dP_i(1-E_i) wedge dI_i.                         (9)

Indeed dP_i I_i=-P_i dI_i, so inserting E_i in dP_i wedge dI_i gives minus Gamma_i wedge Gamma_i. Substituting 1-E_i=Dh_i+h_iD and differentiating P_iD=DI_i=0 gives

    Curv_i=-P_i(dD)h_i wedge dI_i
            -dP_i h_i wedge(dD)I_i
          =-P_i T_i h_i wedge dI_i
            -dP_i h_i wedge T_i I_i.                       (10)

In the last equality the added scalar connection terms vanish only because P_iD=0 and DI_i=0. The physical derivative of D itself remains.

The pivot connection is flat, da_i=0. Its central cross terms also cancel in the ordinary wedge, hence Gamma_hat_i has the same curvature (9)-(10). In tracefree form,

    Curv_i^0=-d kappa_i+kappa_i wedge kappa_i.              (11)

The flatness of the whole split connection does not imply Curv_i=0: Gamma_i is obtained by projecting the ambient reference connection through a varying inclusion and projection.

The connection descent (6) also gives the exact curvature compatibility

    G_ij Curv_j G_ij^(-1)
      =Curv_i+d_(Gamma_i) Q_ij+Q_ij wedge Q_ij,              (12)

where d_(Gamma)Q=dQ+Gamma wedge Q+Q wedge Gamma for a one-form Q. Equations (10)-(12) control curvature and exterior derivatives; they do not remove the symmetric mixed physical derivatives that can occur when the complementary E operators are applied.

## 4. Exact Cech differential of the surviving contraction scalar

Compute delta_S of (3), retaining the two trace calculations separately. The chain-map difference Z is an ambient one-form Cech cocycle, so

    delta_S str(A_i wedge Z_ij)_ijk
      =str((A_j-A_i) wedge Z_jk)
      =str(Z_ij wedge Z_jk)
        +(eta_ij/2) wedge str(kZ_jk).

Both Z factors commute with D, so the first supertrace is exactly the cohomology trace tr(z_ij wedge z_jk), with z_jk transported to frame i.

For the second term of (3), equation (5) gives

    delta_S tr(b_i wedge z_ij)_ijk
      =tr((z_ij+(eta_ij/2)I-Q_ij) wedge z_jk)
      =tr(z_ij wedge z_jk)-tr(Q_ij wedge z_jk).

The central term vanishes because tr(z_jk)=0. Subtracting proves

    delta_S K=tr(Q_ij^0 wedge z_jk)
                  +(eta_ij/2) wedge str(kZ_jk).             (13)

The weighted trace can be reduced without any new matrix calculation:

    str(kZ_jk)=delta_S tau_tilde_jk+15eta_jk
              =delta_S tau_jk+15q_jk.                      (14)

The second equality uses tau_tilde=tau-30d and eta=q+2delta_S d. Equations (13)-(14) prove (1). In particular no exterior-curvature argument is needed to determine this Cech differential.

The pairing Lambda is a Cech two-cocycle; here it is even explicitly exact, Lambda=delta_S K. Its vanishing cohomology class must not be confused with the stronger cochain identity Lambda=0 required for K itself to be closed. Nor is Lambda the complete raw second-order obstruction R.

## 5. The closed-scalar shortcut has an exact source-specific hypothesis

For r=(c,d), let s_alt be the compact representative with K/4 omitted:

    s_alt,cd,ij=(1/4)[-tr(kappa_i wedge L_ij^t)
                      +(eta_ij/2) wedge tau_j
                      +15q_ij wedge d_i]_cd
                      -15q_c,ij q_d,ij/8.                 (15)

Thus t'_r=s_alt,r+K_r/4. The first-order equation delta_S t'_r=F_r immediately gives (2). It can also be verified directly, including the gerbe representative sign, as follows.

The connection part of (15) is -tr(Gamma_i wedge z_ij)/4. By (6), its differential is

    (1/4)tr(z_ij wedge z_jk)
                     -(1/4)tr(Q_ij wedge z_jk).

After contraction_r the first term is -c_r in the source convention F_r=b_r-c_r. For the other scalar-form terms,

    delta_S(eta_ij wedge tau_j)=-eta_ij wedge delta_S tau_jk,
    delta_S(q_ij wedge d_i)=-(delta_S d)_ij wedge q_jk.

Finally the derivative of the edge gerbe representative is

    delta_S[-15q_c,ij q_d,ij/8]
       =15(q_c,ij q_d,jk+q_d,ij q_c,jk)/8.

Subtracting b_r=15q_c,ij q_d,jk/4 and combining eta=q+2delta_S d leaves precisely

    delta_S s_alt,r
       =F_r-(1/4)[tr(Q_ij^0 wedge z_jk)
               +(eta_ij/2) wedge(delta_S tau_jk+15q_jk)]_r. (16)

This supplies a strict and checkable missing identity:

    [tr(Q_ij^0 wedge z_jk)
       +(eta_ij/2) wedge(delta_S tau_jk+15q_jk)]_p=0,
    [tr(Q_ij^0 wedge z_jk)
       +(eta_ij/2) wedge(delta_S tau_jk+15q_jk)]_q=0         (17)

on every actual source triple, with the stated transport and physical contractions. No actual source evaluation or proof of (17) is supplied here.

If (17) is proved, K_p and K_q are regular scalar one-cocycles in the same pair-character sheaves as the original scalar solutions. BI's accepted H1 vanishing on the common cover then gives regular vertex cochains f_p,f_q with K_r=delta_S f_r. Therefore

    [E_p(K_q)+E_q(K_p)]/4
      =delta_S[B_p(f_q)+B_q(f_p)]/4.                        (18)

This removes the contraction contribution globally without asserting K=0 pointwise. It supplies no finite cutoff for the resulting primitive.

If (17) is not known, deleting K changes the first-order equation by the explicit error (16). A replacement scalar correction c_r would have to satisfy delta_S c_r=contraction_r Lambda/4; K_r/4 is the correction already available. Nonzero Lambda would invalidate this particular closed-scalar shortcut, but would not prove that E_p(K_q)+E_q(K_p) cannot itself cancel or be a boundary by another identity.

## 6. A tiny exact control: local flatness does not imply (17)

This is an invented rational split complex. It has no physical source inputs and requires no runtime. Work where u=1+y is invertible. Take C^0 of dimension 3, C^1 of dimension 1, and

    D=(x,0,1),
    I0=((1,0),(0,1),(-x,0)),
    P_i=((1,0,0),(0,1,0)),       h_i=(0,0,1)^t,
    P_j=((1+x,0,1),(0,1,0)),     h_j=(-1,0,1+x)^t.

Both I_i=I_j=I0 satisfy the contraction identities with these P and h. Put M=diag(u,u^(-1)) and take I_k=I0 M, P_k=M^(-1)P_j, h_k=h_j. The three splitting bases U_l=(I_l,h_l) have determinant one, and D U_l=(0,0,1), so they split the same constant differential. Let A_l=-dU_l U_l^(-1) on C^0 and zero on C^1. Set all pivot connections to zero, so eta=q=0. Each A_l is flat and has supertrace zero.

Directly,

    G_ij=1,  G_jk=G_ik=M,
    Gamma_i=0,  Gamma_j=diag(-dx,0),
    Gamma_k=diag(-dx+dy/u,-dy/u),
    Q_ij=diag(-dx,0),
    z_jk=diag(-dy/u,dy/u).

All three induced local curvatures are zero, yet

    tr(Q_ij^0 wedge z_jk)=dx wedge dy/u != 0.

The contraction transgressions are K_ij=K_jk=0 and K_ik=-dx wedge dy/u. For K_ij every form coefficient is proportional to dx. For K_jk, the chosen U_k=U_j diag(M,1) gives Z_jk h_j=0 and h_j Z_jk I_j=0, so both terms of the contraction formula vanish. Finally A_i=E31 dx and the (1,3) coefficient of the dy part of Z_ik is -dy/u, while b_i=0; equation (3) therefore gives K_ik=-dx wedge dy/u directly. Its Cech differential is the same positive dx wedge dy/u.

This checks both the sign in (13) and the necessity of an additional source identity for the shortcut. The example concerns only these formal implications; it says nothing about the actual source pairing (17) or the global obstruction class.

## 7. What this does and does not cancel in the complete remainder

There are exact new cancellations: the two chain-map supertrace products cancel in delta_S K, the pivot scalar terms cancel in the full connection descent, and the scalar first-order defect reduces to the two pairings in (17). The remaining K is therefore an explicit descent transgression controlled by a D/h realization of the Atiyah cocycle Q and the pivot-line weighted trace (14), rather than an unspecified four-block expression.

No term in the previously established Omega+Q2+Q4 has been discarded. The curvature equations concern antisymmetric exterior derivatives, while E differentiates the full physical edge scalar, including I,P,h,D and symmetric mixed derivatives. Equations (10)-(17) alone do not identify those E contributions with a cancellation of Q2 or Q4. Even if (17) is proved and (18) removes K, the boundary problem for Omega+Q2+Q4+E_p(s_alt,q)+E_q(s_alt,p) remains.

The precise next claim required for this shortcut is (17), or a different explicit scalar correction solving the error in (16). No coefficient, source jet, physical matrix, owner list, or finite projection has been computed; no existing finite-domain or execution authorization is enlarged.
