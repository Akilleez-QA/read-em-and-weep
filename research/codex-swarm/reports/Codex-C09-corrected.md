> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

C09 correction: I withdraw the identification E12=R12 and the reversed standard-bit encoding. E12 denotes the correction operator \(E_{12}(T_{34}F_{34})\).

**Authenticated scope.** PR79 commit `5df68750f766b18a746e50bff662b09829225ab1`, `research/hm/null-support-certificates/seed-fingerprint.json`: C09 owns q=4 local ranks 0–23, original seeds 30–53, row 7, M20[0,0], \(\kappa=(-1,-2,-3,-4)\), chart CCCC. Seed4 E12 belongs to C02 and remains reserved.

For local rank \(r\), let \(\pi\) be the rth lexicographic permutation of coordinates 1–4. Its standard tags are
\[
t_j=\sum_{h=1}^{j}2^{4-\pi_h},\qquad j=0,\ldots,4.
\]
Thus seed30 has tags \((0,8,12,14,15)\). Standard coordinate i uses bit \(4-i\); legal-mask coordinate i uses bit \(i-1\). These dictionaries differ. The effective coefficient is \(+\operatorname{sgn}\pi\): the terminal-row minus and J2 minus cancel (#6141530883, #6205455951).

**Corrected exact demand.** Work in characteristic zero on the authenticated regular common cover. Sort full vertices by carrier/mask/standard, auxiliary carrier5 having sorting key −1 only; retain sorting sign \(\epsilon\). Write sorted owners \(A,B,C,D,E\). Put
\[
l=e_0^tH_{0,A}(I_BP_B)I_C,\qquad
r=P_CH_{1,B}e_0.
\]
Both \(e_0\)'s select matrix index zero. For a physical row-End matrix X based at C, define
\[
\mathcal B(X)=l(D_C^{-1}XD_C)^tr,\qquad
D_C=\mathrm{diag}(\nu_C,\nu_C^{-1}).
\]
Consistently frozen-point-normalized leaves instead give \(\mathcal B(X)=lX^tr\); use exactly one conversion (#6205660472).

For tail \((i,j,k)=(C,D,E)\), set
\[
L_d=g_{ij}^{-1}V_dg_{ij},\quad
J_d=g_{ik}^{-1}V_dg_{ik}-L_d,\quad
a_d=\mathcal B(L_d),\quad b_d=\mathcal B(J_d).
\]
With \(s_{34}=T_{34}F_{34}\), C09’s demand is precisely
\[
\sum_{\pi,\mathrm{labels}}
\frac{\operatorname{sgn}\pi\,\epsilon}{2}
[\kappa]\,W\!
\left(
a_2V_1s_{34,jk}-a_1V_2s_{34,jk}
+b_1V_2s_{34,ij}-b_2V_1s_{34,ij}
\right).
\]
Here W is the owned outer54/legal29 weight product. This follows by substituting the four-term E12 identity and the transported-current identity in #6205127744/#6205249609.

Preserve weighted owners 0–4, deleted-prefix owners 0,1, kernel owners 0,1,2, and tail owners 2,3,4. Prefix-mask summation retains carrier weights and standard owners. Repeated tail carriers do not merge owners. Alternate the authenticated cochain; do not recompute its nonlinear residual after reordering.

Both scalar roles remain:
\[
R^\sharp=M(0)^0+F_{34}k_{12}+F_{12}k_{34}
+E_{12}(T_{34}F_{34})+E_{34}(T_{12}F_{12}).
\]
Only the fourth summand is assigned here. Differentiate the canceled regular N14 quotient, retaining weight and physical-frame derivatives.

**Evidence and control.** Ran the inspected V01 metadata binder: all78 complete fingerprint dictionaries matched, including every assigned seed30–53; source-formulas/model blob hashes matched the supplied pins at `08b73637d4136f91606aad332c46cafd064417f8`. No physical arithmetic, matrices, expansions, scans, or file writes ran.

The correction specializes published identities; it proves no new vanishing. Empty certified coefficient-support intersections exclude branches; nonempty intersections remain UNKNOWN. Reviewer: V01, revised formula review pending. Dependency/next step: bind these four demands to complete owned regular-support records. No detector value or boundary/completeness conclusion follows.