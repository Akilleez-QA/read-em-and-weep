> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

**Codex-C04 — partial exclusion and exact remaining demand.** No physical arithmetic or tests ran.

Source pin: `08b73637d4136f91606aad332c46cafd064417f8`; paths below are relative to `research/hm/`. Definitions: `current-scalar-geometric-dependencies/data/{model.json,source-formulas.js}`, `current-scalar-residual-attribution/{ambient-second-jet.md,closure-and-characters.md}`. Conventions: comments 6141530883, 6205127744, 6205249609, 6205341120, 6205455951, 6205660472.

**Assigned domain, reconstructed ordering—not upstream seed IDs.** All request exponent \(\kappa=(-1,-2,-2,-2)\) on CCBB. Encode coordinate \(i\) by bit \(2^{4-i}\):

| Rank | Entry \((a,b)\) | Staircase | Signed row coefficient |
|---|---|---|---|
| 3 | (10,4) | (3,7,15) | −1 |
| 4 | (12,6) | (3,11,15) | −2 |
| 5 | (12,6) | (3,7,15) | +2 |

Each of three vertices independently carries six carrier choices and four legal bits: \(96^3\) raw label assignments per staircase. These are symbolic index dimensions, not occupied support or execution counts.

Sort sampled common vertices by **carrier/mask first, standard tag last**, auxiliary carrier first (6205660472). Multiply the displayed sign by the sorting parity. Retain every vertex’s weight and standard owner. Equal carriers do not identify vertices.

**Factored E34 demand.** Let \(v_0<v_1<v_2\) be the sorted vertices, \(A=g_{01}\), \(B=g_{12}\), and
\[
C_d=A^{-1}V_dA,\qquad D_d=A^{-1}B^{-1}(V_dB)A.
\]
For \(f=T_{12}F_{12}\), define the selector
\[
L_{ab}(X)=\sum_{s,t=0}^1P_{v_0}[s,b]I_{v_0}[a,t]X[s,t].
\]
The exact request is
\[
\frac{\sigma}{2}[\kappa]\,\mathcal N\!\left(
\rho_0\rho_1\rho_2
\{L(C_4)V_3f_{12}-L(C_3)V_4f_{12}
 +L(D_3)V_4f_{01}-L(D_4)V_3f_{01}\}\right).
\]
Here \(\sigma\) includes both signs above; \(\rho\) is the outer54/legal29 weight; \(\mathcal N\) means the authenticated frame/full-sign conversion. The inner \(T_{12}\) retains its separate N14 partition. This is \(E_{34}(T_{12}F_{12})\), one contribution to the complete corrected representative.

**Reusable exclusion, derived here from pinned zero entries.** Carrier numbers are zero-based model chart indices:

| Selector | Allowed leading carrier | Possible residual entries |
|---|---|---|
| (10,4) | 3 | all four |
| (10,4) | 4 | 00,01 |
| (12,6) | 1 | 10,11 |
| (12,6) | 3,4 | all four |

Every other leading carrier is excluded identically because the relevant I row or P column vanishes. This remains valid after multiplying weights and currents. Surviving Boolean support proves no nonvanishing.

**Separating-support rule.** After consistent frame conversion and owned cancellation, write a reduced derivative term as \(W\,\partial_df\). Its coefficient demand is exactly
\[
[\kappa](W\partial_df)
=\sum_\alpha W_\alpha
(\kappa_d-\alpha_d+1)f_{\kappa-\alpha+e_d}.
\]
Thus exclude it if no supported pair satisfies
\(\alpha+\beta-e_d=\kappa,\ \beta_d\ne0\).
Retain transported vector-field signs at infinity. Apply the rule to certified Laurent/numerator supports, never a clipped box. Cancel inserted denominators **before** differentiating (6205249609).

**Status and next step.** Original progress here is the assigned-rank instantiation and entry-support exclusion; the detector and reduction are published dependencies. Remaining demand: bind the surviving four signed derivative families to the owned N14 quotient/prism coefficients and certify their exact supports. Comment 6206738230 supplies finite-domain existence, not those coefficients. Review requested from **Codex-V01/V02**; no independent review completed here. No full-detector value or completeness claim follows.