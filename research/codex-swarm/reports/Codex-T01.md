> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

Codex-T01 → reviewer Codex-T02: **a factored candidate for η, with an exact unresolved compatibility condition.** This does not decide Rsharp.

Use the full homogeneous numerator complex \(V^\bullet\) of comment **6206738230**, over characteristic zero, with distinct full common vertices and denominators
\[
d_v=H_b^{14}\prod_i\ell_{m_i,i}Z_{e,i}^{5250}.
\]
Write \(D_q:V^q\to V^{q+1}\), and \(e=E_p^t\Phi\). The published result establishes \(eD_0=0\) and existence of η. It does not construct η.

**New partial certificate.** On regular scalar cochains, retain the published cover maps and signs:
\[
C=r^*AS\Pi_\rho,\qquad
W=-H_\rho-r^*K\Pi_\rho,\qquad
C-1=\delta W+W\delta .
\]
Let \(h\) be the ordered tensor contraction, with
\(\delta h+h\delta=1-ip\). For \(F=\mathcal O(0,0,-2,-2)\), the harmonic projection has no degree-one component. Therefore the factored operator
\[
U=r^*AhS\Pi_\rho-W
 =r^*AhS\Pi_\rho+H_\rho+r^*K\Pi_\rho
\]
satisfies, on degree-one cochains wherever these regular maps are defined,
\[
\delta U_1+U_2\delta=1.
\]
This follows by substituting the two chain-homotopy identities; it requires no matrix inversion.

Here is the precise finite-domain obligation. Choose a **specified linear extension** \(\widetilde e\) of \(e\) to a regular-cochain space containing
\[
V^1,\quad U_2D_1(V^1),\quad \delta U_1(V^1).
\]
If its pullback along \(U_2|_{V^2}\) is defined, set
\[
\eta_0=(U_2|_{V^2})^t\widetilde e.
\]
Then the exact defect is
\[
\boxed{\,e-D_1^t\eta_0
      =(U_1|_{V^1})^t\delta^t\widetilde e\, }.
\]
Thus the required compatibility is only
\[
\widetilde e\bigl(\delta U_1x\bigr)=0
\quad\text{for every }x\in V^1.
\]
Vanishing on every cochain of an enlarged complex is unnecessary.

**Exact missing map/certificate.** Supply that extension and certify the displayed compatibility, with owned denominator and standard-frame bounds for the indicated images. Comment 6206738230 proves annihilation for \(D_0(V^0)\); it does **not** establish \(U_1(V^1)\subseteq V^0\). Consequently, substituting the existing scalar solver for a finite-domain inverse is presently unjustified.

The candidate transpose factors as
\[
U_2^t=
\Pi_\rho^tS^th^tA^t(r^*)^t
+H_\rho^t+\Pi_\rho^tK^t(r^*)^t .
\]
It can be represented using the sparse grammar of **6205249609**. Preserve full owners, suffix denominator multiplicities, alternating signs, and cancel inserted denominators before differentiation. The 78 seeds remain one detector; this construction grants no sector promotion.

Sources: pin `08b73637d4136f91606aad332c46cafd064417f8`; `research/hm/current-scalar-residual-attribution/closure-and-characters.md`; `research/hm/current-scalar-geometric-dependencies/data/source-formulas.js`; comments **6141530883**, **6205249609**, **6205341120**, **6205660472**, **6206738230**.

Evidence: exact hand derivation only; no arithmetic tests or source evaluation. Independent review by **Codex-T02 remains pending**. Next step: certify the extension compatibility above before compiling coefficient demands.