# Independent review of pivot-connection descent

Reviewed on 2026-10-16: `pivot_connection_descent.md`, SHA-256 `33057f9b088669e2b2622173998d10a0a44cf86506bb95c3ded919e8f2058fe5`.

## Verdict

Accepted under the source premises explicitly stated in the note and accepted in the preceding determinant review. The pivot connections are regular on the actual source opens; the auxiliary-frame cancellation is exact; both Čech sign systems and the tensorial formula (18) check out. No formula correction is required.

The result is an explicit regular change of representative that eliminates the auxiliary-frame defect. It establishes neither a vanishing class nor a finite-cutoff certificate. The note preserves these distinctions correctly. This review uses mathematical identities only; no physical source matrix, polynomial, jet, or overlap was evaluated.

## 1. Pivot regularity and gluing

The primary carrier condition implies its pivot section is nonzero; the auxiliary carrier's permitted pivot is also nonzero. Thus the chosen section of N-squared is nowhere zero on the carrier. In a regular line frame its coefficient w_i is a regular unit. The accepted physical-frame identity

    v_local = tau_chart v_affine,
    nu_B^2 = tau_chart nu_A^2

proves that w_i=v_pivot/nu_i^2 has no hidden infinity-chart factor. The legal-frame coefficients and their inverses are regular on their respective legal opens. No new inversion is introduced outside a source vertex's allowed open.

The connection a_i=-(1/2)dlog(w_i) is therefore regular and flat. It is the unique connection on N whose induced connection makes the specified N-squared section parallel. This construction works even if N itself has no chosen square-root trivialization there: changing the line frame by e_beta=e_alpha t gives

    w_i^beta=t^(-2)w_i^alpha,
    a_i^beta=a_i^alpha+dlog(t).

These are exactly the connection gluing rules. The same rule holds for gamma_i, so d_i=gamma_i-a_i is an intrinsic regular one-form. Neither a global connection on all of X nor compatibility of a_i between different carriers is required.

Because tau_i is tensorial, h_i=contraction(d_i wedge tau_i)/4 is a regular scalar vertex cochain. The physical V's preserve regular functions, and the source transition currents are regular on their overlaps. Consequently B_p(h_q), B_q(h_p), and H are regular row-End edge cochains. This proves sheaf regularity, without asserting any particular finite denominator budget.

## 2. The two Čech signs

For the source differential, transport M_r(z)_jk to the i-frame and use L_r,ik=L_r,ij+U_r,ijk. Then

    delta_S M_r(z)
      = (z_j+z_k)U_r-(z_i+z_k)(L_r+U_r)
        +(z_i+z_j)L_r
      = (z_j-z_i)U_r-(z_k-z_j)L_r.

This is exactly (8). The endpoint order and the minus before the second endpoint difference are correct. A common auxiliary rho has delta_S rho=0, so replacing each M by Z in the source differential of (6) introduces no additional source term.

For the double complex, auxiliary degree is the sign-bearing degree:

    D_tot = delta_A + (-1)^p delta_S.

Since K and C have bidegree (0,1), their total differentials have components (delta_S K,delta_A K) and (delta_S C,delta_A C), with positive signs. For (N,A) of bidegrees (0,2) and (1,1), total closure gives

    delta_S N=0,
    delta_A N-delta_S A=0,
    delta_A A=0.

For a primitive with components P of bidegree (0,1) and Q_desc of bidegree (1,0), the mixed component is delta_A P-delta_S Q_desc. Thus (10)–(11) are correct. Source-closedness of N uses the admitted source-closedness of R_raw, as the note states.

## 3. Exact cancellation of the auxiliary defect

The transformation a_i^beta-a_i^alpha=rho gives

    Delta g_i = contraction(rho wedge tau_i)/4 = Delta f_i.

This identity precedes differentiation and holds for arbitrary auxiliary changes, including nonseparated ones. Applying the same linear B operators gives delta_A C=A. Therefore

    H=K-C,
    t'=t-delta_S g=s_raw+delta_S(f-g)

are independent of the auxiliary frame, with f-g=h. The signs in (16) and (19) follow immediately:

    R(t')=R_raw+delta_S H,
    (N,A)-D_tot C=(R(t'),0).

There is no need to assume delta_S A=0, and no omitted Q_desc is used in this construction.

The prescribed physical-frame check tau_i=8a_i+30gamma_i yields h_i=(19/2)contraction(gamma_i wedge a_i). The note correctly restricts this coefficient identity to those prescribed frames. Arbitrary auxiliary changes also change the extreme split-basis matrices, so this identity cannot replace the intrinsic definition of h. Its possible vanishing on particular vertices does not invalidate the global representative change.

## 4. Tensorial formula and projection correction

With sum sigma n k^2=-30 and Btilde_i=B_i+k d_i I,

    Wtilde_ij=W_ij-d_j wedge tau_i+d_i wedge tau_j
                         -30 d_i wedge d_j.

Also eta/2=q/2+delta_S d. Substitution into the bracket of (18) leaves exactly

    W_ij+(q/2) wedge (tau_i+tau_j)
         +d_j wedge tau_j-d_i wedge tau_i.

This is the original bracket plus delta_S(d wedge tau). The +30 term in (18), the sign of eta, and the unchanged original q-gerbe correction are all necessary and correct. In particular eta is not entitled to q's separated-coordinate differentiation rule.

For the projection identity, each arrow of D raises k by 2, so [D,k]=-2D. The shift of [D,B_j,a] is therefore -2d_j,a D. In the first correction term it is killed by D I_i=0; in the second it is killed by P_j D=0. Thus the right-hand side of (20) is unchanged. The shift supplies no chain-map collapse of the four blocks.

## 5. Scope

The pivot choice provides a definite source-specific alternative to simply setting g=f. Algebraically it remains a change by an explicitly identified boundary. Its value is that all remaining expressions and their comparison cochain now live regularly on the actual source cover, with the auxiliary-frame compatibility already resolved.

Existence of the global primitive P' in (21) is still equivalent to existence of a primitive for R_raw. Neither is supplied by descent alone. Likewise the argument gives no 54/29 bound, no extension of a detector's admitted domain, and no source symmetry conclusion. Those exclusions are mathematically necessary and are stated accurately in the reviewed note.
