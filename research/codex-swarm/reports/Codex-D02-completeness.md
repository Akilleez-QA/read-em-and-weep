> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

**D02: the implication holds over \(\mathbf Q\), conditional on the published geometric identification and equivariance premises.** All 30 constant scalar maps separate the entire \(\varepsilon\)-sector.

Source pin: `08b73637d4136f91606aad332c46cafd064417f8`. Paths below are relative to `research/hm/`.

Let \(F\) be the pinned full-sign finite complex,
\[
D_1x=(Ax,Tx),\qquad D_2(n,p)=(Bn,Un+Cp),
\]
and let \(\bar S:H^2(F)\to\mathbf Q^{2430}\) collect all constant scalar coordinates. The published result in `current-scalar-proof/structural-relations.md`, §4, is
\[
K:=\ker\bar S=\operatorname{im}\bigl(\ker C\longrightarrow H^2(F)\bigr)
 \cong\ker C/T\ker A,\qquad \dim K=20.
\]

**Independent exact-sequence verification.** The positive subcomplex \(P\subset F\) has \(P^2=\mathbf Q^{80}\), \(P^3=\mathbf Q^{160}\), differential \(C\), and \(P^1=0\). For \(N=F/P\), the long exact sequence contains
\[
H^1(N)=\ker A\xrightarrow{\,T\,}H^2(P)=\ker C
 \longrightarrow H^2(F).
\]
Indeed, lifting \(x\in\ker A\) gives \(D_1x=(0,Tx)\). Thus the kernel of the last arrow is exactly \(T\ker A\). This confirms the quotient and its interpretation as classes represented by pure-positive cycles.

**Action and signs.** `finite-model/full-sign-boundary-oracle.js`, functions `makeBasis`, `unprunedTransfer`, and `fullH`, places \(p\) in internal degree \(2\), Čech degree \(0\), with exponent tuple \((0,0,0,0)\). Its genuine inclusion is the constant section on all 16 product charts. The internal perturbation \(\Delta\) preserves Čech degree; \(H\) lowers it. Hence
\[
H\Delta i(p)=0,\qquad I_Ap=(1+H\Delta)^{-1}i(p)=i(p).
\]
Under the coefficient-trivial factor action of comment **6130306841**, \(\rho(g)i(p)=i(p)\). Consequently
\[
P_A\rho(g)I_Ap=P_Ai(p)=p.
\]
This applies to every \(p\), hence every class in \(K\).

There is no hidden permutation sign here: all four Čech degrees are zero. The ordinary product \(y_1y_2y_3y_4\) carries no permutation sign; the negative-block \(H^1\) Koszul signs do not occur. The internal End complex is pulled back from the symmetric coefficient map, rather than permuted as four graded complexes. Therefore \(K\) is the trivial \(D_8\)-representation.

For \(W=H^2(F)[\varepsilon]\), \(a=(12)\) acts by \(-1\). If \(x\in K\cap W\), then \(x=ax=-x\), so \(x=0\). Thus
\[
\boxed{\bar S|_W\text{ is injective}.}
\]
With comment **6130391535**, its rank is \(32\). Completeness itself does not require that dimension calculation.

**Scope and failure controls.** Applying this to corrected \(R^\sharp\) requires an authenticated class comparison and the naturality/full-sign choice-independence premises of **6130352358** and `current-scalar-residual-attribution/closure-and-characters.md`. It fails as an inference from only two maps, one detector’s 78 summands, naive harmonic permutations, or characteristic-zero dimensions transplanted to another field. No source values or boundary witness have been established here.

**Review:** independently confirms V07 §5; additional D-worker review remains outstanding. Original contribution here is the exact-sequence and sign verification, not the published kernel/rank statements. Next step: authenticate the actual class comparison and all required scalar evaluations, or supply a complete boundary certificate. Only pinned-source reads and symbolic reasoning were performed; no arithmetic oracle ran.