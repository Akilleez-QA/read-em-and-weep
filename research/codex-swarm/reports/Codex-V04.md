> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

Codex-V04 — frame/normalization audit. Reviewer: Codex-V03, pending. No obstruction verdict.

Source: pin `08b73637d4136f91606aad332c46cafd064417f8`, `research/hm/current-scalar-geometric-dependencies/{data/source-formulas.js,data/model.json,frames-and-poles.md,source-identity.md}` and `research/hm/current-scalar-residual-attribution/{ambient-second-jet.md,closure-and-characters.md}`. Git blob IDs match both supplied hashes.

**Original artifact: endpoint-jet recurrence.** Work in characteristic zero on a common overlap where the legal frames and contractions exist. Write
\[
g^{phys}_{ij}=D_jg^{core}_{ij}D_i^{-1},\quad
N_i=D_i(p),\quad L_i=N_i^{-1}D_i,
\]
with diagonal \(D_i=\operatorname{diag}(\nu_i,\nu_i^{-1})\). Then
\[
\widehat g_{ij}=L_jg^{core}_{ij}L_i^{-1},\qquad
\omega_{i,a}=D_i^{-1}V_aD_i.
\]
For a matrix \(X\) with these endpoints define
\[
\nabla_aX=V_aX+\omega_{j,a}X-X\omega_{i,a}.
\]
Direct differentiation gives
\[
V_a(L_jXL_i^{-1})=L_j(\nabla_aX)L_i^{-1};
\quad
(V_bV_a\widehat g)(p)
=(\nabla_b\nabla_ag^{core})(p).
\]
Derivatives in the recurrence act on \(\omega\) too. Thus frozen \(N_i\) do **not** justify dropping frame jets. A tiny rejection control is \(g^{core}=I,L_i=I,L_j=\operatorname{diag}(1+t,(1+t)^{-1})\): the normalized first jet at zero is \(\operatorname{diag}(1,-1)\), not zero. This is a hand-derived formal control, not physical-source evaluation.

**Chart control.** The pinned splitting blocks satisfy \(2d+p=0\), hence agree before differentiation. At infinity retain both \(V=-z\partial_t\) and \(d\log x=-dt/t\). For a coefficient of weight \(w\),
\[
\partial_t[t^wf(1/t)]
=wt^{w-1}f(1/t)-t^{w-2}f_x(1/t).
\]
The first term rejects “substitute, then differentiate only the affine coefficient.” Completed internal-degree-\(r\) coefficients use \(w=r-2\) per inverted factor. Mixed source derivatives use distinct coordinates; this does not license arbitrary later derivatives.

**Gerbe control, already public (#6205127744).** After left normalization,
\[
M_0=R_{\rm kin}-b_pk_{q,ik}-b_qk_{p,ik}-b_pb_qI.
\]
Consequently
\[
M_0^0+F_pk_q+F_qk_p
=R_{\rm kin}^0-c_pk_q-c_qk_p.
\]
A B report must identify its baseline explicitly. Treating \(R_{\rm kin}\) as \(M_0\) adds the spurious \(b_pk_q+b_qk_p\). Nonlinear products precede transpose.

**Owner/cancellation control.** For an inserted denominator \(D\), certified cancellation \(P=DQ\) implies
\[
V(P/D)=\frac{D\,VP-P\,VD}{D^2}=VQ.
\]
Regularity belongs to the combined quotient; separate Leibniz pieces need not be regular. A05 must retain weight derivatives and occurrence-level owners through cancellation (#6205249609). Equal carrier labels cannot merge distinct common vertices: #6205660472’s repeated-carrier/different-mask edge has \(q=1/x_1\). The selector conversion \(\bar R_{10}=\nu_a^2R^{phys}_{10}\) cancels exactly once under consistent frozen endpoint normalization.

Only V/I proposals were present; no J/B/A05 implementation was available to accept or reject. No tests or oracle runs were performed. Next dependency: source-bound producer formulas with endpoint, chart, baseline and owner records; apply these controls before arithmetic admission. Neither a nonzero complete detector pairing nor a complete boundary certificate is supplied.