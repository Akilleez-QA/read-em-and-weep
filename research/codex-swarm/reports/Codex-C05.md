> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

**C05 — symbolic E12 contract; scan remains on HOLD.**

Sources: pin `08b73637d4136f91606aad332c46cafd064417f8`; `research/hm/current-scalar-geometric-dependencies/data/{source-formulas.js,model.json}`, `research/hm/current-scalar-residual-attribution/{ambient-second-jet.md,closure-and-characters.md}`, and `research/hm/current-scalar-proof/finite-model/full-sign-boundary-oracle.js`. Public rules: comments **6141530883, 6205127744, 6205249609, 6205341120, 6205455951, 6205660472, 6206738230**.

**Exact domain.** Zero-based canonical ranks `[0,12)` comprise:
- ranks `0–5`: `M10[0,3]`, coefficient `1`;
- ranks `6–11`: `M10[2,6]`, coefficient `2`.

Both demand exponent `κ=(-1,-2,-3,-3)` on `CCCB`. Within each block, permutations are
`123,132,213,231,312,321`, with staircase signs `+,-,-,+,+,-`.
Using standard-tag bits `(8,4,2,1)`, the corresponding vertex lists are
`(1,9,13,15)`, `(1,9,11,15)`, `(1,5,13,15)`,
`(1,5,7,15)`, `(1,3,11,15)`, `(1,3,7,15)`.
These ranks are **not upstream seed numbers**.

**Factored selector.** For sorted common vertices `a,b,c,d`, the published pruning gives
\[
J_1=h_a j_b(R_{bcd}),\qquad
M10[r,t]=e_r^TH_{0,a}I_bR_{bcd}^tP_be_t.
\]
Thus put \(u=e_r^TH_{0,a}I_b,\ v=P_be_t\); the bare residual-entry coefficient is \(v_i u_j\). Dimensions are `H0:5×15`, `I:15×2`, `P:2×15`, `R:2×2`. The complete internal-degree `−1` label space has dimension `75+150+20=245`; this assignment selects two coordinates.

Labels retain four standard owners, four carrier labels in `(*,0,1,2,3,4)`, and four four-bit masks. Sort by **carrier, mask, standard tag**, auxiliary first; multiply by sorting parity and staircase sign. Repeated common vertices vanish. Surviving prefixes require `carrier(a)<carrier(b)`; tail carriers may repeat. The prefix-mask sum factors to one, leaving three independent tail masks. Never merge equal carriers’ tail owners.

In bare coordinates use
\[
\bar R=D_b^{-1}R_{\rm physical}D_b,\quad D_b=\operatorname{diag}(\nu_b,\nu_b^{-1});
\]
in particular \(\bar R_{10}=\nu_b^2R_{\rm physical,10}\). This conversion must occur exactly once.

**E12 coefficient rule.** On the residual tail set \(A=g_{bc},B=g_{cd}\),
\(L_i=A^{-1}V_iA,\ N_i=A^{-1}B^{-1}(V_iB)A\). Then
\[
E_{12}(s)=\tfrac12[(V_1s_{cd})L_2-(V_2s_{cd})L_1
 +(V_2s_{bc})N_1-(V_1s_{bc})N_2],
\quad s=T_{34}F_{34}.
\]
Apply the selector and outer weights to these four signed terms separately, retaining symbolic convolution:
\[
[\kappa](f\,V_i s)=\sum_\ell[\kappa-\ell]f\,[\ell](V_i s).
\]
No integration-by-parts shortcut is assumed.

**Separating-support exclusion.** A term is zero if certified supports satisfy
\(\kappa\notin\operatorname{Supp}(f)+\operatorname{Supp}(V_i s)\).
For cleared outer numerator demands, use exactly
\[
p_i+\sum_{\rm finite}a_{\ell i}-\sum_{\rm infinity}a_{\ell i}-m_i=\kappa_i,
\quad
m_i=\sum_{\rm infinity}(54d_b+29\deg\ell_{\rm mask}+5251).
\]
An infeasible owned demand is excluded; feasibility proves no nonvanishing. Here `s=1,m=4` gives numerator-degree upper bound `22429`, not occupied support.

**Status/control.** Original contribution: this restricted rank/sign table and assembled E12 demand contract. Selector pruning and finite-domain exactness are published dependencies. No arithmetic tests or physical evaluations ran; no additional exclusion or obstruction conclusion follows.

**Reviewer:** Codex-V01/Codex-V02; review pending. **Dependency/next step:** bind the unpublished incumbent fingerprint and owned canceled-quotient supports before instantiating demands. All 78 seeds still form one detector.