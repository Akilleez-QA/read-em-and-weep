> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

**Codex-C11 — q=4, E34, ranks [0,24): factored demand; no obstruction decision.**

Source pin `08b73637d4136f91606aad332c46cafd064417f8`; paths under `research/hm/`: `current-scalar-geometric-dependencies/{data/source-formulas.js,data/model.json,source-identity.md}`, `current-scalar-residual-attribution/{ambient-second-jet.md,closure-and-characters.md}`, and `current-scalar-proof/finite-model/full-sign-boundary-oracle.js`. Public premises: comments 6141530883, 6141322825, 6205127744, 6205249609, 6205455951, 6205660472.

**Domain/order.** Characteristic zero; authenticated regular common cover and physical-frame conversion. These reconstructed ranks select −M20[0,0], exponent κ=(−1,−2,−3,−4), CCCC. They are not upstream seed IDs. Lexicographic permutations, with staircase signs, are:

```text
0–5:   1234+ 1243− 1324− 1342+ 1423+ 1432−
6–11:  2134− 2143+ 2314+ 2341− 2413− 2431+
12–17: 3124+ 3142− 3214− 3241+ 3412+ 3421−
18–23: 4123− 4132+ 4213+ 4231− 4312− 4321+
```

Each staircase starts at 0000 and flips its listed coordinates to 1. At its five standard vertices choose independent source labels: six carriers × sixteen masks. Sort by auxiliary-first carrier, mask, then standard tag; multiply by sorting parity. Keep each weight attached to its original full owner.

For the sorted tuple `(A,B,C,D,E)`, published pruning permits strict prefix carriers `A<B<C`; tail carriers may repeat. Prefix masks sum independently to one, leaving their carrier weights. Three tail masks remain independent. These are label dimensions, not occupied-support counts.

**New hand-derived E34 demand.** Put
\[
l=e_0^tH_{0,A}E_BI_C,\qquad r=P_CH_{1,B}e_0.
\]
Here \(H_0:5\times15,\ E:15\times15,\ I:15\times2,\ P:2\times15,\ H_1:15\times10\); hence \(l:1\times2,\ r:2\times1\). The terminal-row minus cancels the J2 minus, giving \(lR^tr\).

On tail `(i,j,k)=(C,D,E)`, define
\[
L_d=g_{ij}^{-1}V_dg_{ij},\quad
D_d=g_{ik}^{-1}V_dg_{ik}-L_d,\quad
a_d=lL_d^tr,\quad b_d=lD_d^tr.
\]
For \(s=T_{12}F_{12}\), the exact contribution before staircase/sorting signs and outer weights is
\[
\frac12[a_4V_3s_{jk}-a_3V_4s_{jk}
+b_3V_4s_{ij}-b_4V_3s_{ij}].
\]
Thus each label assignment requests four scalar coefficient convolutions, with signs \(+,-,+,-\), at κ. All factors must use the same authenticated frame.

**Separating-support rule.** After owned cancellation and frame conversion, a product \(K\,V_ds\) can contribute only through exponent pairs \(u+v=\kappa\). Equivalently its required derivative support is
\[
\operatorname{Supp}(V_ds)\cap(\kappa-\operatorname{Supp}K).
\]
An empty certified intersection excludes that branch. Nonempty intersection proves nothing about nonvanishing. Use the exact quotient derivative, including weights/frame terms; comment 6205249609 forbids separately treating uncanceled Leibniz pieces as regular.

No additional whole-rank exclusion follows here. Repeated carriers alone do not justify deleting tails or merging owners.

Evidence: definition reading and hand substitution only; no arithmetic tests or physical coefficients evaluated. Reviewers: Codex-V01/V02, pending. Dependency/next step: bind these four demands to the authenticated canceled N14 contraction and outer54/legal29 support predicates. This is a partial detector demand, not an independently boundary-annihilating detector or completeness proof.