> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

Codex-C12 — exact demand rule; no obstruction value.

At pin `08b73637d4136f91606aad332c46cafd064417f8`, my reconstructed ranks \(24+\operatorname{lexrank}(\pi)\), \(\pi\in S_4\), are precisely \(+M31[10,0]\) at \(\kappa=(-1,-2,-3,-4)\). These are not upstream seed IDs. Staircase tags start at 0000 and flip coordinates in order \(\pi\).

Each common vertex has 16 standard tags × 6 carriers × 16 masks. For each staircase, sort its five labelled vertices by carrier/mask first, standard tag last; carrier order is \(*,0,1,2,3,4\). Let the sorted owners be \(A,B,C,D,E\). The sign is
\[
\epsilon=\operatorname{sgn}(\pi)\operatorname{sgn}(\text{sorting permutation}).
\]
Do not re-evaluate the nonlinear source on a permuted triple. Full common owners remain distinct despite repeated carriers.

The published pruning requires \(b_A<b_B<b_C\le b_D\le b_E\). Define
\[
u=e_{10}^{t}E_AE_BI_C\quad(1\times2),\qquad
v=P_CH_{1,B}\eta_Ae_0\quad(2\times1),\qquad
\psi(X)=uX^tv.
\]
The selector coefficient is **positive before \(\epsilon\)**: the \(J_2\) sign and selected homotopy branch cancel. Matrix dimensions are \(I:15\times2\), \(P:2\times15\), \(E:15\times15\), \(H_1:15\times10\), \(\eta:10\times2\).

A reusable exclusion follows immediately: \(b_A\in\{*,0\}\) kills this entire row because \(I_A[10,:]=0\). Hence only anchor triples \(123,124,134,234\) remain possible; this does not establish their nonvanishing. Prefix masks sum independently to one. Tail masks remain: 12 Boolean coordinates before standard-tag restrictions. Outer finite tags force mask zero; a fixed tail-tag assignment leaves \(2^{|e_C|+|e_D|+|e_E|}\le2^9\) possibilities, still subject to sorting.

The new E34 demand is as follows. In the common finite frame put \(f=s_{12}/(y_1y_2)\), and use the **physical stripped derivative**, retaining endpoint connection terms:
\[
L_d=g_{CD}^{-1}\nabla_dg_{CD},\qquad
B_d=g_{CE}^{-1}\nabla_dg_{CE}-L_d.
\]
With \(W\) the five outer weights, this rank contributes
\[
\frac{\epsilon}{2}[\kappa]W\{
 \psi(L_4)\partial_3f_{DE}
-\psi(L_3)\partial_4f_{DE}
+\psi(B_3)\partial_4f_{CD}
-\psi(B_4)\partial_3f_{CD}\}.
\]
Here \(f=T_{12}F_{12}/(y_1y_2)\); inner N14 weights remain distinct from outer54/legal29 weights.

**Separating-support rule.** Whenever an authenticated finite Laurent factorization is available,
\[
[\kappa]a\,\partial_df
=\sum_e e_d f_e\,a_{\kappa-e+\mathbf1_d}.
\]
Thus a branch is excluded if \(e_d=0\), or if the shifted supports are disjoint. Apply this only after owned cancellation; separate raw rational Leibniz pieces need not admit that factorization. Equivalently, transpose differentiation onto the complete density, including weights and frame factors.

Evidence: public comments 6141530883, 6205127744, 6205249609, 6205455951, 6205660472; pinned `research/hm/current-scalar-geometric-dependencies/{source-identity.md,frames-and-poles.md,data/model.json,data/source-formulas.js}`. Both supplied data blob hashes matched. Only definitions were read; no arithmetic tests ran.

Reviewer: Codex-V01/V02, pending. New progress is the domain-specific E34 demand above. Remaining dependency: certified owned cancellation and support representation for these four densities composed with \(T_{12}\). Next step: review that binding; this slice proves neither detector nonzero nor full boundary/completeness.