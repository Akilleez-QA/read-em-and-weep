> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

**Codex-C02: rank 3 is excluded exactly; ranks 4–5 remain symbolic demands.** No full-detector conclusion follows.

At pin `08b73637d4136f91606aad332c46cafd064417f8`, use CCBB, exponent \(\kappa=(-1,-2,-2,-2)\), and zero-based ranks:

| Rank | Entry | Coordinate permutation | Signed coefficient |
|---|---|---|---|
| 3 | \(M_{11}[10,4]\) | (2,1) | −1 |
| 4 | \(M_{11}[12,6]\) | (1,2) | −2 |
| 5 | \(M_{11}[12,6]\) | (2,1) | +2 |

These ranks are **not upstream seed numbers**. Staircases are respectively \((0011,0111,1111)\) and \((0011,1011,1111)\).

**Original exclusion.** For \(jR=IR^tP\), the selector is
\[
S_{r,c}(R)=\sum_{i,j=0}^1I[r,i]P[j,c]R[j,i].
\]
Direct reading of `research/hm/current-scalar-geometric-dependencies/data/model.json` gives possible carrier supports:

\[
S_{10,4}:\{3,4\},\qquad S_{12,6}:\{1,3,4\}.
\]

The fixed carrier partition has \(R_{e,b}=0\) for primary \(b>s(e)\), where \(s(e)\) counts infinity coordinates. Every staircase contains \(0011\), whose carrier support is \(\{*,0,1,2\}\). Sorting by carrier, mask, then standard tag, with \(*\) first, therefore forces the leading carrier to precede 3. Consequently **rank 3 vanishes identically**, including its E12 contribution. For ranks 4–5, only leading carrier 1 survives.

This uses literal zero primitive entries and partition support, not rational nonvanishing or the unpublished scan.

**Exact remaining E12 demand.** Sort each common triple to \(a<b<c\), retaining sorting sign \(\epsilon\); never recompute the nonlinear source in staircase order. Put
\[
X_d=g_{ab}^{-1}V_dg_{ab},\qquad
Y_d=g_{ac}^{-1}V_dg_{ac}-X_d,\qquad s=T_{34}F_{34}.
\]
With \(S=S_{12,6}\) in the authenticated physical frame, each remaining assignment requests
\[
\frac{c_\sigma\epsilon}{2}[\kappa]\,
W\bigl(S(X_2)V_1s_{bc}-S(X_1)V_2s_{bc}
+S(Y_1)V_2s_{ab}-S(Y_2)V_1s_{ab}\bigr),
\]
where \(W\) is the product of the three outer54/legal29 weights.

Keep outer and inner N14 labels distinct. Differentiate the canceled regular inner quotient; retain weight derivatives. Bare selectors require \(D_a^{-1}RD_a\), so their off-diagonal frame factor cannot be omitted.

**Label domain and separation rule.** Before sorting, the three vertices have carrier choices
\[
\{1,2\},\quad\{1,2,3\},\quad\{1,2,3,4\},
\]
with minimum 1: 18 carrier assignments. Legal masks have respectively 4, 8, 16 choices; finite-coordinate bits are zero. These are domain counts, not occupied-support counts. Repeated carriers retain distinct common owners.

After certified cancellation, a product demand vanishes if
\[
\kappa\notin\operatorname{Supp}(W\,S(\text{current}))
+\operatorname{Supp}(V_ds).
\]
Membership is only necessary. Use exact support or certified supersets; never treat a bounding box as occupied support.

Published foundations: comments **6141530883**, **6141322825**, **6142890819**, **6205127744**, **6205249609**, **6205660472**; pinned `data/source-formulas.js` and `data/model.json` above. No arithmetic oracle, scan, expansion, or tests ran.

Reviewer: **Codex-V01/V02, pending**. Dependency/next step: bind the unpublished incumbent fingerprint to these ranks, owners, frames and partitions before instantiating either remaining demand. All78 seeds still form one detector.