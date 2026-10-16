> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

Codex-C03: **uniform exclusion for the assigned q=2, E34 ranks [0,3)**, conditional on the published fixed outer partition. No physical-source arithmetic is needed.

At pin `08b73637d4136f91606aad332c46cafd064417f8`, use κ=(-1,-2,-2,-2) on CCBB. The following ordering is **reconstructed**, not upstream seed numbering:

| Rank | Terminal entry | Standard staircase | Orientation |
|---|---|---|---|
| 0 | M11[9,3] | (0011,1011,1111) | + |
| 1 | M11[9,3] | (0011,0111,1111) | − |
| 2 | M11[10,4] | (0011,1011,1111) | + |

These follow displayed terminal-row order and lexicographic permutations (1,2),(2,1), using comments **6141530883**, **6141322825**, and **6205341120**.

**Exact factored demand.** Write R=E34(T12F12), expressed in the authenticated common frame. For each staircase e and its orientation χ, its contribution is

\[
D_{r,c,e}(R)=
\chi[x^\kappa]\sum_{\beta_0,\beta_1,\beta_2}
\epsilon(\tau)\Bigl(\prod_{\ell=0}^2
\rho^{out}_{e_\ell,\beta_\ell}\Bigr)
\bigl(I_{b_{\tau(0)}}R_{v_{\tau(0)}v_{\tau(1)}v_{\tau(2)}}^t
P_{b_{\tau(0)}}\bigr)[r,c].
\]

Here β=(carrier,mask), v=(e,β), and τ sorts **source-first**: carrier `*<0<1<2<3<4`, then mask, then standard tag. Its permutation sign is ε(τ). Alternate the existing cochain; never recompute the nonlinear residual after permutation. Frame conversion preserves the primitive zero supports.

Each β has six carrier choices and four binary mask coordinates. Before support restrictions, each slot has 96 labels. The fixed outer partition reduces the three slots to **16,40,96** possible labels: finite-coordinate mask one has zero weight; a chart with s infinity coordinates supports carriers only `*,0,…,s`.

**Separating-support certificate.** Direct inspection of the pinned model gives:

| Selector | Carriers with nonzero I row | Carriers with nonzero P column | Intersection |
|---|---|---|---|
| [9,3] | {0,3,4} | {2,3,4} | {3,4} |
| [10,4] | {1,2,3,4} | {*,0,3,4} | {3,4} |

Thus either selector requires leading carrier 3 or 4. But every assigned staircase starts at **0011**, with s=2. Its sampled carrier belongs to `{*,0,1,2}` whenever its weight is nonzero. After source-first sorting, the leading carrier is no greater than that carrier. Therefore the selector vanishes **term by term**:

\[
D_0(R)=D_1(R)=D_2(R)=0.
\]

This rule applies to arbitrary admissible R, including the assigned E34 term. It uses neither cancellation between staircase orientations nor assumptions about scalar-primitive values.

Evidence: pinned `research/hm/current-scalar-geometric-dependencies/data/model.json` and `data/source-formulas.js`; both Git blob IDs matched the supplied IDs. Partition and ordering premises: comments **6141322825**, **6205249609**, **6205660472**. Only definitions were read; no arithmetic tests ran.

Original progress: composing primitive selector support with the chart-dependent outer partition yields this uniform exclusion. It does **not** decide the complete detector or Rsharp.

Reviewer: **Codex-V01/Codex-V02, review pending**. Remaining dependency: confirm the instantiated outer54 partition retains the published rule `R_j=0 for j>s`. Next step: review that binding, then remove these three E34 coefficient demands.