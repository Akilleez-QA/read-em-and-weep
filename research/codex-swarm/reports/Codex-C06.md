> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

**Codex-C06 — symbolic E12 contract; scan remains on HOLD.**

Sources: pin `08b73637d4136f91606aad332c46cafd064417f8`; `research/hm/current-scalar-geometric-dependencies/{source-identity.md,data/source-formulas.js,data/model.json}`. Both supplied blob IDs match pinned Git objects. Public rules: GitHub comments #6141530883, #6205127744, #6205249609, #6205341120, #6205455951, #6205660472.

**Exact assigned domain.** Zero-based canonical ranks [12,24), with exponent κ=(-1,-2,-3,-3) on CCCB:

```text
permutation       123  132  213  231  312  321
orientation         +    -    -    +    +    -
standard vertices 1,9,13,15; 1,9,11,15; 1,5,13,15;
                  1,5,7,15; 1,3,11,15; 1,3,7,15
ranks 12..17      M21[10,1], row coefficient 1
ranks 18..23      M21[12,5], row coefficient 2
```

Standard tags encode coordinate1 as bit8. These ranks are not upstream seed numbers.

For each staircase assign common vertices, then sort by `(carrier,mask,standard)`, auxiliary carrier first. Carry the sorting parity and the original standard owner with each vertex. Duplicate common vertices give zero; repeated carriers alone do not.

Write the sorted vertices A,B,C,D. Published pruning requires carrier(A)<carrier(B), with B,C,D otherwise source-sorted. Each assigned standard row has six carrier choices and sixteen legal masks. The A-mask sum factors to one; three tail masks remain independent. Inner T34 insertions have their own N14 labels and fixed standard tags, distinct from outer54/29 labels.

**Factored demand.** For terminal entry (a,b), put
```text
u = e_a^t E_A I_B,       v = P_B H1_A e_b.
```
Dimensions are E:15×15, I:15×2, P:2×15, H1:15×10; u is 1×2 and v is 2×1. The selected J1 component is exactly `u R_BCD^t v`, with positive lift/block sign.

Set s=T34 F34,
```text
X_d = g_BC^-1 V_d(g_BC),
Y_d = g_BD^-1 V_d(g_BD) - X_d.
```
The E12 demand, before terminal coefficient extraction, is
```text
1/2 [
 (V1 s_CD) u X2^t v - (V2 s_CD) u X1^t v
 +(V2 s_BC) u Y1^t v - (V1 s_BC) u Y2^t v ].
```
Multiply by the retained outer weights, terminal coefficient and both orientation parities; then request κ in the authenticated frame. Prefix owners remain attached after face deletion.

**Separating-support rule.** In finite x coordinates, divide out the full-sign y-product consistently. Writing f=s/(y3 y4), the complementary derivatives become ∂1f,∂2f. For any resulting scalar kernel W,
```text
[κ](W ∂d f) = Σ_(α+β−e_d=κ) β_d W_α f_β.
```
Thus a branch is excluded if no support pair satisfies this equation with β_d≠0. This is a necessary-support rule, not a nonvanishing certificate. W includes weights and frame factors; use owned regular cancellation before differentiation. Source-frame conversion must precede support comparison.

**Additional exclusion derived here.** Ranks12–17 vanish whenever carrier(A) is auxiliary or 0: pinned `source-identity.md` §3 gives `e10^t E_A=0`, hence u=0 for arbitrary residual input. This extends that published primitive identity to these six demands; it does not exclude ranks18–23.

Evidence: definition reading and exact hand derivation only; no arithmetic tests or source evaluation ran. Reviewers: Codex-V01/V02; review pending. Unresolved: incumbent fingerprint, instantiated owned supports and inner T34 demands. Next step: bind that package and review these formulas before any held scan. No boundary/completeness conclusion follows.