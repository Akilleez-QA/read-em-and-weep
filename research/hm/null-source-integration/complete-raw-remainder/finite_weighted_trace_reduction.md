# All-finite weighted-trace reduction of the remaining pairing

This is an additional algebraic reduction on the source's original all-finite chart, with the prescribed physical vertex frames. It uses the determinant identity and the already derived formula

    Lambda_ijk = tr(Q_ij^0 wedge z_jk)
                 +(eta_ij/2) wedge(delta tau_jk+15 q_jk).

The second edge is transported to the first cohomology frame. It does not evaluate any source point, prove Lambda vanishing, or remove any term from the complete obstruction.

## Source coefficients and frame discipline

Let m_i,a be the legal-mask bits at vertex i, and write

    b_i = sum_a m_i,a dlog(x_a),
    ell_i = dlog(nu_i),
    p_i = dlog(v_pivot(i)).

These letters denote one-forms, not the first-order correction matrix b used in other notes. In particular ell is the refined physical-frame logarithmic derivative, not the old connection gamma. The pinned generator gives, on this chart,

    ell_i = sum_a m_i,a (x_a^2+1)/(2x_a(x_a^2-1)) dx_a,
    gamma_i = ell_i-b_i/2,
    q_ij = b_j-b_i.

The pivot connection in the prescribed vertex frame is a_i=ell_i-p_i/2. Hence the intrinsic connection difference d_i=gamma_i-a_i has the explicit coefficient

    d_i=(p_i-b_i)/2.

Use the already invariant definition eta=q+2 delta d, rather than subtracting coefficients of a from different prescribed frames. It gives the useful cancellation

    eta_ij=p_j-p_i.                                      (1)

The determinant calculation gives tau_i=8 ell_i-4 p_i+30 gamma_i in these prescribed frames. Tau is the scalar weighted trace of the tensorial block differences. Thus

    tau_i=38 ell_i-4 p_i-15 b_i,
    delta tau_jk+15 q_jk=38(ell_k-ell_j)-4(p_k-p_j).       (2)

Equations (1)-(2) are direct substitutions into the actual finite-chart coefficient formulas. They do NOT substitute tau=8a+30gamma into a difference of arbitrarily common-frame connection coefficients. That tempting shortcut would drop the 38 delta ell term. Under a change of auxiliary frame, those connection coefficients change while tau does not; the split determinant coefficients must be transported too.

## Exact reduced pairing

Set u_ij=p_j-p_i and r_jk=ell_k-ell_j. Then

    Lambda_ijk = tr(Q_ij^0 wedge z_jk)
                 +19 u_ij wedge r_jk
                 -2 u_ij wedge u_jk.                    (3)

All elliptic vector-field factors are retained when contracting a pair: a two-form coefficient in dx_a wedge dx_b acquires y_a*y_b. Equation (3) is an identity of forms before that contraction.

The accepted source-specific closed-scalar test is therefore exactly

    [tr(Q_ij^0 wedge z_jk)+19 u_ij wedge r_jk
                         -2 u_ij wedge u_jk]_p = 0,
    [tr(Q_ij^0 wedge z_jk)+19 u_ij wedge r_jk
                         -2 u_ij wedge u_jk]_q = 0.      (4)

No matrix in (4) is assumed zero. In particular, even with identical masks, when r_jk=0, the pivot-ratio term remains. With equal carrier pivots at i and j, u_ij=0, only the projection/current trace remains. Neither specialization is a general source theorem.

## Only first derivatives are needed for this diagnostic

The existing connection descent gives Q_ij=z_ij+delta Gamma_ij, with transported delta Gamma, Gamma_i=P_i dI_i and z_ij=-dG_ij G_ij^-1. Consequently the pairing (3) can be constructed from the prescribed source I/P and transition values and first derivatives, plus the displayed scalar logarithmic derivatives. It does not require differentiating the full four-block scalar, reconstructing D/h defects, or computing second derivatives.

This is a first-jet diagnostic for the particular proposed removal of K/4. It is separate from the fixed second-jet Omega specialization and does not enlarge that execution contract. A nonzero contraction rejects only the closed-K shortcut; it does not prove a nonzero global obstruction. If both contractions vanish on the whole actual cover, the prior H1/BI argument applies under its stated regularity premises. A zero at one point would not supply that global hypothesis.

No claim of extension of these explicit coefficients through infinity or a changed finite-domain cutoff is made here. The invariant Lambda formula remains the reference outside this chosen chart.

Sources: PR79 raw_connection_followup.md (determinant trace), pivot_connection_descent.md (intrinsic d and eta), curvature_descent_followup.md (delta K), and PR90 pinned source-formulas.js at 779c1f7604db6fd48ce6e389b30a96f7aebef9f7. All claims here follow algebraically from those source-bound premises. No actual source specialization ran.
