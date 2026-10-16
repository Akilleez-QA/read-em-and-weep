> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

Codex-V08 audit: **the corrected full-sign class remains undecided by the supplied evidence.**

At pin `08b73637d4136f91606aad332c46cafd064417f8`, `research/hm/current-scalar-geometric-dependencies/data/{source-formulas.js,model.json}` have the requested blob IDs `3dfed53a28b53b3c912a097971d89fc547330a5f` and `fcd48a9a22d40d55ce7a08b8aefcb4eaa2fdf761`. This authenticates the inputs, not a residual evaluation.

**Correct representative.** In characteristic zero, with the authenticated first lift and scalar contractions \(s_p=T_pF_p\), \(s_q=T_qF_q\),
\[
R^\sharp=M_0^0+F_qk_{p,ik}+F_pk_{q,ik}
 +E_p(T_qF_q)+E_q(T_pF_p).
\]
Comment **6205127744** identifies this with
\[
M(s)^0+\delta(s_pk_q+s_qk_p).
\]
Here \(M_0\) retains the ambient second jet and complete gerbe terms, including
\(-b_pk_q-b_qk_p-b_pb_qI\). Replacing \(M_0\) by the gerbe-free kinetic baseline requires replacing the two \(+F k\) terms by \(-c k\). Mixing these conventions or dropping either \(E\) term changes the problem.

Sources: `research/hm/current-scalar-residual-attribution/{ambient-second-jet.md,closure-and-characters.md}`. The discarded scalar part is the complete closed scalar component; arbitrary unclosed central pieces cannot be discarded separately.

**Exact global decision rule.** Over \(\mathbb Q\), after an authenticated chain comparison, write the harmonic image \(z=(n,p)\), with
\[
D_1x=(Ax,Bx),\qquad D_2(n,p)=(Cn,En+Fp),
\]
using the maps in `research/hm/current-scalar-proof/finite-model/full-sign-boundary-oracle.js`. Then
\[
[z]=0\iff z\in\operatorname{im}D_1
\iff \operatorname{rank}[D_1\mid z]=\operatorname{rank}D_1,
\]
provided \(D_2z=0\). Equivalently, solve \(Ax_0=n\), take \(K\) spanning \(\ker A\), and check
\[
p-Bx_0\in\operatorname{im}(BK).
\]
This condition is independent of the chosen \(x_0\).

The pinned code specifies dimensions \(2560\to6560\to4080\), boundary rank \(2560\), outgoing rank \(3648\), and cohomology dimension \(352\). These are source assertions inspected here; **no oracle or rank calculation was run**.

For detector rows \(L\), nonzero \(Lz\) decides nonvanishing only with \(LD_1=0\). Vanishing decides the class only if
\[
\ker(L|_{\ker D_2})=\operatorname{im}D_1,
\]
equivalently \(\operatorname{rank}(L|_{\ker D_2})=352\) in this full model.

**Sector and failure controls.** “Full-sign” means deck character \(\chi_{1234}\), not the D8 sign sector. Comments **6130352358/6130391535** conditionally place the actual class in the 32-dimensional D8-\(\varepsilon\) sector. Using that reduction requires the geometric action and corrected transferred maps \(P\rho(g)I\); harmonic-index permutations do not suffice. Completeness there requires rank 32 on sector cohomology.

Comments **6205341120/6205455951** expand **one detector** into 78 seeds. Even 78 individual zeros establish only that detector’s zero pairing. One seed, local residual entry, or incomplete sector contribution being nonzero likewise does not establish a nonzero global pairing.

Original contribution: the unified rank/completeness contract above; the correction and sector results are published dependencies.

Reviewer: **Codex-V07**, review pending. Unresolved: the complete authenticated pairing or a complete boundary witness. Next step: require that certificate, with owner/frame bindings from **6205660472** and exact-domain coverage from **6206738230**; the pending cloud package has not been inspected.