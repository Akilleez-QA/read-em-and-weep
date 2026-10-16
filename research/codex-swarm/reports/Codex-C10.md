> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

Codex-C10 — symbolic demand contract; E12 scan remains HOLD.

At pin `08b73637d4136f91606aad332c46cafd064417f8`, ranks **[24,48)** are precisely the `+M31[10,0]` row, exponent κ=(−1,−2,−3,−4), chart CCCC (#6141530883). They are not upstream seed numbers.

Rank `24+j` uses the jth lexicographic permutation below. Signs are staircase orientations:

```text
1234+ 1243− 1324− 1342+ 1423+ 1432−
2134− 2143+ 2314+ 2341− 2413− 2431+
3124+ 3142− 3214− 3241+ 3412+ 3421−
4123− 4132+ 4213+ 4231− 4312− 4321+
```

The five standard vertices start with all coordinates finite and switch coordinates to infinity in that order.

**Labels and selector.** Each common vertex has standard tag (16 choices), carrier (6), legal mask (16): 1,536 vertices. Sort source-first by `(carrier,mask,standard)`, auxiliary carrier first. Retain the alternating sorting sign ε; repeated identical common vertices vanish. For sorted owners A,B,C,D,E, surviving prefixes require strictly increasing carriers A<B<C; tail carriers may repeat. Prefix-mask sums collapse independently, but their carrier weights and standard owners persist (#6205455951/#6205660472).

Put E_X=I_XP_X and
```text
a = row10(E_A E_B I_C),       dimension 1×2,
b = col0(P_C H1_B eta_A),    dimension 2×1.
```
Here E is 15×15, I is 15×2, P is 2×15, H1 is 15×10, and eta is 10×2. The selected residual is
`Σuv a_u b_v R_vu`.
Both terminal-row and lift signs cancel, leaving **sgn(π)ε** (#6205455951). These are alternating cochain requests; do not reconstruct the nonlinear residual on a newly reordered tail.

**New factored E12 demand rule.** Let tail transitions be g_CD, g_DE, g_CE and define
```text
L_d=g_CD^−1 V_d(g_CD),
J_d=g_CE^−1 V_d(g_CE)−L_d,
c_d=Σuv a_u b_v(L_d)_vu,
t_d=Σuv a_u b_v(J_d)_vu.
```
For s=T34F34, the selected E12 contribution is exactly
```text
½[c₂ V₁s_DE − c₁ V₂s_DE
   +t₁ V₂s_CD − t₂ V₁s_CD].
```
Thus each rank requests four signed coefficient families, multiplied by its owned outer weight W and sgn(π)ε. Equivalently, without expansion,
```text
[κ](W K V_ds_edge)
 = Σ_{h+l+n=κ} W_h K_l (V_ds_edge)_n,
```
with K respectively c₂,−c₁,t₁,−t₂. Inner T34 uses N14; outer W uses54/29. Differentiate only after certified inserted-denominator cancellation. Preserve physical frame derivatives (#6205127744/#6205249609).

**Separating-support exclusion.** A family is zero if its exact regular supports admit no h+l+n=κ, or its selector is structurally zero. In particular A=auxiliary or carrier0 kills this entire M31 word because row10(E_A)=0 (`research/hm/current-scalar-geometric-dependencies/source-identity.md`, §3). Passing Boolean support proves only UNKNOWN. A vanishing subset of ranks supplies no detector conclusion.

Evidence: pinned source/model blob IDs match the supplied IDs; derivation uses the cited public identities. No arithmetic tests or physical evaluations ran. Reviewer: Codex-V01/V02, pending.

Dependency/next step: bind the unpublished incumbent fingerprint to these ranks, owners, frames and canceled coefficient supports before any scan. The full finite-domain lemma (#6206738230) applies to the complete detector; it does not authorize promoting this slice to boundary annihilation.