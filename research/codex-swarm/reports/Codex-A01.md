> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

Codex-A01 — **blocked at survivor binding; no expansion performed.** C03/C04 reports were absent at both inventory checks. This artifact specifies their missing handoff, not instantiated demands or an obstruction result.

Domain: characteristic zero, complete corrected full-sign row-End representative, actual common vertices \(v=(e,b,m)\). Source pin `08b73637d4136f91606aad332c46cafd064417f8`; Git resolved both supplied formula/model blob IDs exactly.

Each C03/C04 survivor record must supply:

- Producer, source pin, exact definition of “q2,” and branch (`q2` or `E34`).
- Detector/seed ID, terminal row and entry, staircase, orientation and exact rational multiplier.
- Ordered full owners for the residual triple, retained prefix factors and inserted vertices; sorting permutation/sign and carrier lookup IDs.
- Target matrix entry, derivative multi-index, tensor states, bundle twist, coordinate charts and coefficient exponent.
- Physical or frozen-point-normalized frame convention; explicit conversion factors and normalization.
- Separate outer54/legal29 and inner N14 partition factors, owned denominator multiplicities, numerator shifts and coefficient-convolution constraints.
- Cancellation/regularity justification before differentiation; pruning evidence distinguishing structural zero from UNKNOWN.

Absent fields remain **unfilled**, never defaulted. In particular, “q2” cannot safely be identified with `q(i,j,2)`.

Proposed owner-preserving DAG key:
\[
\operatorname{Hash}(\text{canonical encoding}[
\text{pin},\text{formula version},\text{op},
\text{ordered child keys},\text{exact constants},
\text{ordered full owners},\text{frame},
\text{entry},\text{jet index},\text{twist},
\text{partition role},\text{owned pole multiset}]).
\]
Coefficient-demand keys additionally contain chart, tensor state and target exponent. Preserve matrix operand order. Carrier-only primitive blobs may be shared, but their owner/frame bindings remain distinct nodes. Hash equality requires canonical-payload equality verification.

Actual reusable source expressions, from `research/hm/current-scalar-geometric-dependencies/data/source-formulas.js`, `globalBuild2`:
\[
C_{uv}=P_{b_u}I_{b_v},\quad
g_{uv}=\left[\operatorname{diag}(\nu_u^{-1},\nu_u)
C_{uv}\operatorname{diag}(\nu_v,\nu_v^{-1})\right]^t,
\]
\[
q(u,v,a)=\frac{m_{v,a}-m_{u,a}}{X_a},\qquad
b_{ab}=\tfrac{15}{4}q(i,j,a)q(j,k,b).
\]
Reuse \(P_b,I_b,\nu_v,g_{uv},g_{uv}^{-1}\) and demanded jets through these bindings; equal carriers do not imply equal \(q\).

For E34, set \(A=g_{ij},G=g_{ik}\) and reuse
\[
L_d=A^{-1}V_dA,\qquad
W_d=G^{-1}V_dG-L_d,\quad d=3,4.
\]
Then, for \(s=T_{12}F_{12}\),
\[
E_{34}(s)=\tfrac12[
(V_3s_{jk})L_4-(V_4s_{jk})L_3
+(V_4s_{ij})W_3-(V_3s_{ij})W_4].
\]
This follows from comments **6205127744/6205249609**; **6205660472** fixes owner/frame binding. Demand scalar derivatives only after certified inserted-owner cancellation.

Original contribution: this handoff/key contract; the identities are published results. Failure controls: reject owner collapse, ambiguous frames, unprepared derivatives and unsupported zero claims. No tests, physical evaluation or arithmetic oracle ran; no reserved scan was duplicated.

Reviewer: **Codex-A02/Codex-V03**, pending. Next step: obtain complete C03/C04 records, then bind only their surviving demands. No local result promotes to the full detector.