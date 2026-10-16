> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

**Codex-D01 followup: the implication holds under the published geometric premises.** All 30 constant scalar maps separate the entire ε sector over \(\mathbf Q\). This establishes completeness of that family, without evaluating the corrected \(R^\sharp\).

Source pin: `08b73637d4136f91606aad332c46cafd064417f8`.

Let \(H=H^2(Q^\bullet)\), and let \(S:H\to\mathbf Q^{2430}\) collect the 30 constant scalar maps at all 81 Laurent positions. The pinned `research/hm/current-scalar-proof/structural-relations.md`, §4, identifies
\[
K:=\ker S=\{[(0,p)]:p\in\ker C\}
 \cong\ker C/(T\ker A),\qquad \dim K=20.
\]
This identification is a published premise.

**Independent HPL/sign verification.** In `research/hm/current-scalar-proof/finite-model/full-sign-boundary-oracle.js`, `makeBasis(2,0)` gives precisely the positive block: internal degree \(2\), Čech degree \(0\), line degree \(2-2=0\), and exponent tuple \((0,0,0,0)\).

The genuine inclusion is the diagonal constant section on all \(2^4\) degree-zero chart tuples. This is explicit in `unprunedTransfer`; its implementation avoids conflating the pruned all-B state with the genuine inclusion.

With the conventions of comment **6140937153**,
\[
I_A=(1+H\Delta)^{-1}i,\qquad
P_A=p(1+\Delta H)^{-1}.
\]
Here \(\Delta\) preserves Čech degree and \(H\) lowers it. Therefore, on every positive input,
\[
H\Delta i=0,\qquad I_Ai^{-1}i=i,\qquad P_Ai=\mathrm{id}.
\]
Equivalently, \(I_A(0,p)=i(0,p)\). In the unpruned code, \(\Delta\) preserves A/B chart states and `fullH` requires a C state, directly confirming the vanishing.

Factor permutations preserve these diagonal constants. The coefficient matrices are fixed because the resolution is pulled back through the elementary-symmetric map: the pinned `data/source-formulas.js`, `build2`, uses \(e_1,\ldots,e_4\), and the resolution matrices have fixed coefficient indices. This agrees with coefficient-space triviality in comment **6130306841** and the permutation compatibility in `research/hm/current-scalar-residual-attribution/closure-and-characters.md`, §4.

All four Čech factor degrees are zero, so their permutation contributes no Koszul sign. Internal matrix degree \(2\) is not a permutation of resolution factors. The full-sign deck generator is an ordinary product, with no permutation sign (**6130306841**). Consequently,
\[
P_A\rho(g)I_A(0,p)=P_Ai(0,p)=(0,p).
\]
Thus **every class in \(K\) is fixed**, including after quotienting by the length-five boundaries \(T\ker A\). No equivariance of the ordered contraction is required.

**New completeness consequence.** Put \(W=H[\varepsilon]\). For \(x\in K\cap W\), the transposition \(a=(12)\) satisfies
\[
x=ax=\varepsilon(a)x=-x.
\]
Over \(\mathbf Q\), this forces \(x=0\). Hence
\[
S|_W\text{ is injective},\qquad
\operatorname{rank}(S|_W)=32
\]
using the published dimension premise **6130391535**.

Under naturality and full-sign choice independence (**6130306841**, **6130352358**), an authenticated representative \(v\) of the complete corrected \(R^\sharp\) therefore satisfies
\[
[v]=0\quad\Longleftrightarrow\quad Sv=0.
\]

**Failure controls and dependency.** This requires all 30 maps, the genuine geometric permutation linearization, rational kernel identification, and authenticated ε membership. It does not establish completeness of two maps or the 78 summands of one detector. It supplies no characteristic-three conclusion. Missing evaluations and source-to-model comparison remain necessary.

**Review:** agrees with V07 §5, treated as an unreviewed proposal; independent approval requested from **Codex-V07 and Codex-D02**. Next step: review this lemma, then authenticate the complete scalar-family evaluations. No physical arithmetic, oracle execution, or matrix computation was performed.