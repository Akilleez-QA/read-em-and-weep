# Independent review of the determinant reduction and local frame defect

Reviewed on 2026-10-16: `raw_connection_followup.md`, SHA-256 `b508e10d02ba843db0a9de0748602b4283f94aadb7b95ba69c1e6554f78e1597`.

## Verdict

Accepted under the published source's homogeneous primitive, inverse-splitting, determinant-one, and physical-frame premises. Those premises supply the regularity and complete covering needed in this application; the deduction is not relying on rational agreement alone. The determinant ratio is a genuine global regular unit, hence constant on the proper connected product of elliptic curves. Consequently the displayed complementary identity

    V_a tau_i,c = -4 V_a V_c log(v_j(i)),  a != c,

is valid in the prescribed physical vertex frames. The local signs in (K), (N), (O), and (P) are also correct. No correction to the reviewed formulas is needed.

This review checks the mathematical implication from the accepted source identities. It does not rerun their computational certificates or evaluate any physical matrix, source polynomial, or jet.

## Sources and precise premises

The review uses the pinned [first-order source, sections 1–2 and 4](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/first-order-source.md) and the pinned [physical-frame theorem, sections 1–2 and 4](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-geometric-dependencies/frames-and-poles.md). The latter was also read directly at the pinned GitHub commit.

The required source facts are:

1. U0 and U1, with their displayed Q0 and Q1, are inverse splittings of the same constant complex, with extreme split matrices equal to the identities.
2. All 36 carrier cohomology transitions have determinant one. The source's physical determinant-one normalization is used with care below.
3. The homogeneous primitive denominators belong to the corresponding carrier complement, and the elementary W and eta invert a permitted pivot. Therefore U and Q are regular matrices on their own carrier opens after taking legal line frames.
4. Physical U and Q agree as rational matrices before differentiation between finite and infinity charts, by the homogeneous degrees and line powers in the physical-frame theorem.
5. The six carrier opens and both legal line opens in each factor form complete covers. The elementary cover argument added to the reviewed note establishes this without a source evaluation.

## 1. Carrier changes: the determinant cancellation is exact

Fix one legal line mask and one product coordinate chart. Write S_i=U0_i and T_i=U1_i, and put

    M_0 = S_i^(-1) S_j,    M_1 = T_i^(-1) T_j.

These intertwine the constant split differentials. In the split order (contractible rank 5, cohomology rank 2, contractible rank 8) in degree zero and (contractible rank 8, contractible rank 2) in degree one, they have block forms

    M_0 = [[I_5, *, *], [0, C_ij, *], [0, 0, A_ij]],
    M_1 = [[A_ij, *], [0, I_2]].

The identity extreme split changes force I_5 and I_2. Commutation with the middle differential forces the same A_ij in both places. Thus

    det(M_0)/det(M_1) = det(C_ij).

At the fixed line mask, C_ij is a conjugate of the source's carrier cohomology transition, so its determinant is one. This proves (H) directly, including its orientation. It avoids any possible determinant-functor permutation convention.

There is an important restriction here: the split cohomology columns scale as (1,nu^(-2)), whereas the normalized physical cohomology columns use (nu,nu^(-1)). Their common scalar discrepancy matters across different line masks. The proof correctly does not invoke determinant-one cohomology gluing across masks at this step.

## 2. Line masks, regularity, and infinity

Across line masks, use the displayed split columns themselves. Their total determinant powers are

    S: -2*5 + 0 - 2 + 2*8 = 4,
    T: 0*8 + 2*2 = 4.

Consequently det(S)/det(T) is mask-independent. This is the needed cross-mask gluing, independent of the cohomology normalization subtlety.

These are local units, not just rational functions that happen to agree. The source gives regular inverse matrices U and Q on each carrier/legal open. The line-power factors do not create hidden interior poles: their squares are 1 or (x^2-1)/x on a finite chart, and t or 1-t^2 on an infinity chart, with each relevant expression a unit on its legal open. All line powers in U and Q are even. Together with the carrier denominator bounds, this proves local regular invertibility. In particular both det(S)/det(T) and its reciprocal are regular there.

The physical-frame theorem's equality before differentiation supplies agreement at infinity. Equivalently, the unscaled homogeneous determinants both have degree -2, while their physical line determinant factors both have power 4. No unaccounted determinant-line transition remains in their ratio.

The complete-cover argument in the reviewed note is valid: if a homogeneous coordinate vanishes, a nonzero coordinate gives a nonvanishing primary equation; if none vanishes, the auxiliary equation is nonzero. The legal line opens also cover each elliptic factor. Hence the local units glue over all X, not merely a dense affine open. Properness and connectedness of this product of elliptic curves imply the glued regular function is constant.

The abstract determinant-line explanation is consistent with this direct calculation: the alternating total line exponent is

    5 + 15 - 30 + 10 = 0,

and the specified determinant-one cohomology trivialization is essential. Vanishing total line exponent alone would not justify treating an arbitrary set of local determinant ratios as one scalar function.

## 3. Complementary logarithmic derivative

Constancy gives dlog det(S_i)=dlog det(T_i). The elementary W/eta determinant gives

    det(T_i) = epsilon_i nu_i^4 / v_j(i)^2,

so (E) becomes

    tau_i = 8 dlog(nu_i) - 4 dlog(v_j(i)) + 30 gamma_i.

The gamma coefficient and the line-ratio logarithmic coefficient each depend on one coordinate at a time. Their complementary derivatives vanish. This proves (I) with coefficient -4. All logarithmic derivatives here are algebraic dlog expressions; no branch is selected.

At infinity v_local=tau_chart v_affine, with tau_chart a product of single-axis factors. Its mixed logarithmic derivative vanishes, so the formula is compatible with the transported invariant vector fields. No assertion that a homogeneous pivot is globally the constant one is needed.

## 4. Local frame-defect signs

Let C=sum_r sigma_r n_r k_r^2=-30 and Omega_i=B_i+k gamma_i. Then

    sum_r sigma_r k_r tr(Omega_i) = tau_i - 30 gamma_i.

Direct ordinary-wedge expansion gives

    str(B_i wedge B_j)
      = str(Omega_i wedge Omega_j)
        + gamma_j wedge tau_i - gamma_i wedge tau_j
        + 30 gamma_i wedge gamma_j.

Since theta_ij=gamma_i-gamma_j, adding theta_ij wedge (tau_i+tau_j) leaves

    str(Omega_i wedge Omega_j) + 30 gamma_i wedge gamma_j
      + gamma_i wedge tau_i - gamma_j wedge tau_j.

The last two terms are -delta(gamma wedge tau)_ij. This independently checks the sign in (K), hence s_raw=t-delta f in (L).

Under gamma_i^beta=gamma_i^alpha+rho, the tensorial tau_i is unchanged, so

    Delta f_cd,i = (rho_c tau_i,d - rho_d tau_i,c)/4.

For a separated physical line-frame change and a complementary a, V_a rho_c=V_a rho_d=0. Substitution of (I) yields

    V_a Delta f_cd,i = -rho_c P_i;ad + rho_d P_i;ac.

Thus (N)–(P) have the correct signs. In particular this computation does not make f global: its nontrivial compatibility defect still needs cancellation before the local primitive can establish a global boundary. The reviewed note preserves that obligation.
