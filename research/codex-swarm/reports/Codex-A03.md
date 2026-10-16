> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

Codex-A03 — **conditional partition recurrence; no certified C03/C04 demand found.** The available roster is an unreviewed proposal. No expansion, source arithmetic, oracle run, or test was performed.

Sources: pin `08b73637d4136f91606aad332c46cafd064417f8`, `research/hm/current-scalar-geometric-dependencies/data/{source-formulas.js,model.json}`; their blob IDs match the supplied pins. Partition definitions: GitHub comments **6141322825, 6142890819**; outer powers/domain: **6205249609**; owner/frame corrections: **6205660472**.

**New conditional coefficient recurrence.** Work over the characteristic-zero source field, on one fixed standard chart \(e\). Let \(s\) be its number of infinity coordinates, \(d=s+1\), and \(z\) its four local coordinates. Put
\[
A_i=(-1)^{s-i}H_{s-i}(z_{\rm finite}),\qquad g_i=A_iv_i,\quad 0\le i\le s.
\]
The published identity is \(\sum_i g_i=1\).

For carrier power \(N\), set
\[
M=2N-1,\quad L_0=5M,\quad L=d(L_0-1)+1.
\]
Thus inner N14 uses \((M,L_0)=(27,135)\); outer54 uses \((107,535)\).

For each assigned carrier index \(j\), compute \(B_j=E_j/v_j^{L_0}\) without polynomial division. Define
\[
f_{i,j,n}=A_i^n v_i^{\,n-L_0[\,i=j\,]}.
\]
Allow \(0\le n<L_0\) for \(i<j\), \(n\ge L_0\) for \(i=j\), and \(n\ge0\) for \(i>j\). All powers are nonnegative. Initialize
\[
D_0(0,0)=1
\]
and all other states zero. For \(i=0,\ldots,s\), update
\[
D_{i+1}(r+n,\alpha+\beta)\mathrel{+}=
D_i(r,\alpha)\binom{L-r}{n}[z^\beta]f_{i,j,n},
\quad n\le L-r.
\]
Then \([z^\alpha]B_j=D_d(L,\alpha)\). Negative polynomial indices give zero. The binomial factors telescope to the exact multinomial coefficient; the restrictions implement “first index reaching \(L_0\).” This derives a recurrence for the published formula, not a new partition theorem.

**Owned carrier cancellation kernels.**
\[
R_j/h_j^N=B_j\sum_{k=N}^{M}\binom Mk
h_j^{k-N}v_2^{M-k}a^{M-k},
\]
\[
R_*/a^N=\sum_{j=0}^{s}B_j\sum_{k=0}^{N-1}\binom Mk
h_j^kv_2^{M-k}a^{M-k-N}.
\]
These are polynomial identities. Retain each occurrence’s owner even when carrier equations coincide.

For legal power \(P\), infinity coordinate \(t\), and \(U=2P-1\), the canceled mask kernels are
\[
L_0/t^P=\sum_{k=P}^{U}\binom Uk t^{2k-P}(1-t^2)^{U-k},
\]
\[
L_1/(1-t^2)^P=\sum_{k=0}^{P-1}\binom Uk t^{2k}(1-t^2)^{U-k-P}.
\]
Use \(P=1\) inside and \(P=29\) outside; finite masks have weights \((1,0)\).

**Demand contraction/admission.** For a certified finite Laurent numerator \(Q\) and polynomial kernel \(W\),
\[
[z^\kappa](WQ)=\sum_\alpha W_\alpha Q_{\kappa-\alpha}.
\]
Prune a DP state only with a certified remaining-support exclusion; a missing coefficient is unresolved, not zero. Convert infinity exponents and frames before applying this rule.

Reject demands lacking full owners \((e,b,m)\), multiplicities, orientation, channel, partition tag, canceled denominator ledger, or exact target exponent. Differentiate only the combined canceled inner quotient, retaining weight derivatives. Never identify inner N14 with outer54/legal29.

Reviewer: **Codex-A04/Codex-V05, pending**. Dependency: authenticated C03/C04 demand and cloud label binding. Next step: review these identities, then bind one demand’s owner/frame ledger and derive its finite backward index set. This supplies neither a resource certificate nor a verdict on complete \(R^\sharp\).