# The all-finite Lambda diagnostic is affine in the last two masks

This derives a finite mask reduction for the specific closed-K diagnostic from the preceding all-finite weighted-trace note. It does not establish that the diagnostic vanishes or run any physical computation.

Use column transitions throughout this note. Let the rational carrier data be I_i^0, P_i^0, and set C_i=diag(nu_i,nu_i^-1). Whole ambient line transport, already required in the supertrace proof, identifies the physical common-frame contraction as

    I_i=I_i^0 C_i, P_i=C_i^-1 P_i^0,
    G_ij=C_i^-1 K_ij C_j, K_ij=P_i^0 I_j^0.

The transpose of G is the previously used row transition. The carrier matrices K and their derivatives depend on the base coordinates but not the legal masks. Work on the common legal finite open where these expressions are defined.

Define Gamma_i^0=P_i^0 dI_i^0 and h=diag(1,-1). Then

    Gamma_i=C_i^-1 Gamma_i^0 C_i+C_i^-1 dC_i,
    dC_i C_i^-1=ell_i h.

Substitution in the exact projection descent equation gives

    Q_ij=C_i^-1 Q_ij^0 C_i,
    Q_ij^0=K_ij Gamma_j^0 K_ij^-1-dK_ij K_ij^-1-Gamma_i^0.  (1)

Here superscript 0 means rational carrier reference, NOT tracefree projection. Write tf(Q_ij^0) for its tracefree part. All derivatives of C cancel in (1); dropping them before forming Q would not justify this equality.

Put z_jk^0=-dK_jk K_jk^-1. The transported physical second-edge current is

    G_ij z_jk G_ij^-1
      =C_i^-1 [K_ij z_jk^0 K_ij^-1
                +ell_j K_ij h K_ij^-1
                -ell_k K_ik h K_ik^-1] C_i.              (2)

The common outer conjugation disappears in its trace pairing with Q_ij. Define one-forms

    A_j=tr(tf(Q_ij^0) K_ij h K_ij^-1),
    A_k=tr(tf(Q_ij^0) K_ik h K_ik^-1),
    u_ij=dlog(v_pivot(j)/v_pivot(i)).

Combining (2) with the previous scalar trace reduction yields

    Lambda_ijk = T_ijk
              +(A_j-19u_ij) wedge ell_j
              +(19u_ij-A_k) wedge ell_k,                 (3)

where the mask-independent two-form is

    T_ijk=tr(tf(Q_ij^0) wedge K_ij z_jk^0 K_ij^-1)
                         -2u_ij wedge u_jk.              (4)

The ordering of wedge factors in (3) is significant. In particular tr(Q wedge ell H)=tr(QH) wedge ell. No wedge reversal has been hidden in A_j or A_k.

## Exact consequence for legal-mask work

On the original finite chart,

    ell_j=sum_a m_j,a r_a dx_a,
    ell_k=sum_a m_k,a r_a dx_a,
    r_a=(x_a^2+1)/(2x_a(x_a^2-1)).

Thus Lambda is independent of the FIRST mask, and affine, with no quadratic mask products, in the eight bits of the LAST two masks. For a fixed ordered carrier triple, its rational two-form identity on this common finite open is equivalent to the vanishing of the mask-zero constant term and the eight single-bit coefficients in (3). This is nine rational two-form identities, not evaluations at nine different base points.

For a selected pair (c,d), contraction kills every ell bit outside c,d. Consequently that one pair contraction is equivalent to FIVE rational identities: its constant term and the four coefficients corresponding to j,c; j,d; k,c; k,d. For the two disjoint target pairs (0,1) and (2,3), this is ten scalar rational identities per ordered carrier triple, including their separate constant terms. This does not bound polynomial complexity, grant actual arithmetic, or prove any of these identities.

The source's common legal open contains all mask choices simultaneously after removing the finitely many line-frame zeros and poles. A rational identity established there has the usual dense-open meaning. This note does not separately prove regular extension at infinity or change the earlier global cover premises.

## Scope and next check

This reduction concerns Lambda=delta K, not the second-jet Omega symbol, the complete Rsharp, or a detector. It leaves the fixed Omega preparation untouched. The finite frame/trace identities should be independently reviewed before using the mask reduction in a future source computation. A nonzero coefficient would refute the closed-K shortcut on that domain; it would not prove a global obstruction. All source quantities in (1)-(4) require at most first derivatives.
