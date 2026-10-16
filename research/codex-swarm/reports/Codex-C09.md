> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

**Codex-C09 — symbolic demand contract; E12 scan remains HOLD.** No obstruction value or complete boundary proof obtained.

Source pin: `08b73637d4136f91606aad332c46cafd064417f8`. Read `research/hm/current-scalar-geometric-dependencies/{source-identity.md,frames-and-poles.md,data/source-formulas.js,data/model.json}`, the specified residual-attribution notes, and finite-model definitions. Blob IDs match the supplied formula/model pins.

**Domain and signs.** Define E12 as the one-based residual entry \(R_{12}\). Ranks \(0,\ldots,23\) select the first displayed q=4 terminal row, \(-M20[0,0]\), with lexicographic permutations below. Each sign is its staircase orientation:

```text
0–5:   1234+ 1243− 1324− 1342+ 1423+ 1432−
6–11:  2134− 2143+ 2314+ 2341− 2413− 2431+
12–17: 3124+ 3142− 3214− 3241+ 3412+ 3421−
18–23: 4123− 4132+ 4213+ 4231− 4312− 4321+
```

For permutation π, standard vertices are \(e_0=0,\ e_j=\sum_{t\le j}2^{\pi_t-1}\). The requested Laurent exponent stays \(\kappa=(-1,-2,-3,-4)\); do not permute it.

A common vertex has 16 standard tags, six carriers \((*,0,1,2,3,4)\), and 16 legal masks: 1,536 labels. Each fixed staircase has five independent 96-choice carrier/mask labels. Sort by **carrier, mask, standard tag**, auxiliary first; multiply by sorting parity. Retain every vertex owner. Only sorted carrier profiles \(A<B<C\le D\le E\) survive. Prefix-mask sums for A,B factor to one; the three tail masks remain independent. Repeated tail carriers are allowed.

**Factored demand.** Put
\[
L=e_0^tH_{0,A}E_BI_C,\qquad
U=P_CH_{1,B}e_0,\qquad E_B=I_BP_B .
\]
Here L is \(1\times2\), U is \(2\times1\); both \(e_0\)'s select matrix index zero. Comments **6205455951** and **6141530883** give two cancelling minus signs: J2 and its terminal row. Consequently this sector demands
\[
\operatorname{sgn}(\pi)\operatorname{sgn}(\sigma)
[\kappa]\;W\,L_2U_1\,\nu_C^{-2}\,R^\sharp_{12,CDE},
\]
summed over the stated labels. W is the owned outer54/legal29 weight product.

The frame factor follows from
\(\bar R=D_C^{-1}R_{\rm physical}D_C\):
\(\bar R_{12}=\nu_C^{-2}R_{{\rm physical},12}\).
It cancels only with consistently frozen-point-normalized residual leaves (**6205660472**).

The residual leaf means all five corrected contributions:
\[
M(0)_{12}+F_qk_{p,12}+F_pk_{q,12}
+E_p(T_qF_q)_{12}+E_q(T_pF_p)_{12}.
\]
No gerbe-baseline substitution is implicit (**6205127744**).

**Reusable exclusion and coefficient rule — original specialization.** Reject E12 whenever either Boolean matrix path is absent:
\[
H_{0,A}[0,:]\,I_BP_BI_C[:,2],\qquad
P_C[1,:]\,H_{1,B}[:,0].
\]
Indices 1,2 here denote first/second residual coordinates. Absence proves zero; presence proves only UNKNOWN.

For each cleared factored numerator, preserve separate owner supports. With five vertices, its coordinate degree is at most **28036**. Demand precisely
\[
p_i+\sum_{\rm finite}a_{\ell i}-\sum_{\rm infinity}a_{\ell i}
=\kappa_i+m_i,
\quad
m_i=\sum_{\rm infinity}
(54d_b+29\deg\ell_m+5251).
\]
An empty signed Minkowski-support intersection excludes the coefficient. A nonempty intersection does not establish nonvanishing. Append no extra twist (**6205249609**).

Evidence: definition reads and hand derivation only; no scan or arithmetic tests ran. Reviewer: **Codex-V01/Codex-V02**, pending.

Unresolved dependency/next step: bind the unpublished incumbent fingerprint to E12 convention, rank, owned labels, frame and partition metadata before instantiating any coefficient support. These 24 sectors remain part of the single 78-seed detector; no local promotion is justified.