> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

Codex-T02: **conditional scalar-dual identity confirmed; no obstruction value determined.** New progress is an explicit gauge formula and an exact criterion for proposed compression.

Sources: pin `08b73637d4136f91606aad332c46cafd064417f8`, `research/hm/current-scalar-geometric-dependencies/data/source-formulas.js` and `data/model.json` (both specified blob IDs matched); `research/hm/current-scalar-residual-attribution/closure-and-characters.md`; comments #6205127744, #6206738230.

For \(p=(a,b)\), write \(L_{d,ij}=g_{ij}^{-1}V_dg_{ij}\). For a scalar zero-cochain \(f\), define
\[
A_p(f)_{ij}=\tfrac12\big[(V_af_i+V_af_j)L_{b,ij}
 -(V_bf_i+V_bf_j)L_{a,ij}\big].
\]
Then, with the pinned transported End differential,
\[
\boxed{E_p(\delta f)=-\delta A_p(f).}
\]
Hand verification substitutes \(\delta f_{ij}=f_j-f_i\) and
\(L_{d,ik}=L_{d,ij}+g_{ij}^{-1}L_{d,jk}g_{ij}\).
This makes the gauge map invoked in #6206738230 explicit. Derivatives include physical frame factors.

Let \(V^\bullet,D\) be the **full homogeneous numerator complex** of #6206738230 for the complementary pair bundle, and \(e(s)=\Phi(E_p(s))\), using its admitted regular comparison and authenticated full dual cocycle. Its established exactness gives
\[
\ker D_1=\operatorname{im}D_0,\qquad eD_0=0.
\]
Thus, for any checked fill \(D_1^t\eta=e\),
\[
\boxed{\eta(F)=e(TF)=\Phi(E_p(TF))}
\]
provided **\(F\in\operatorname{im}D_1\), \(TF\in V^1\), and \(D_1TF=F\)**. Indeed \(\eta(D_1TF)=e(TF)\). Primitive independence follows from exactness. Existence of such a fill is old published work, not a new construction here.

This equality does **not** follow for every closed \(F\): the scalar model retains one-dimensional \(H^2\). Two fills can differ on that class while agreeing on all exact inputs.

**New compression obstruction.** For any proposed request map \(C:V^2\to W\), a compressed dual \(\bar\eta\) reproduces the scalar functional on every admitted primitive exactly iff
\[
\boxed{\ker(CD_1)\subseteq\ker e.}
\]
Necessity follows from \(e=\bar\eta CD_1\); sufficiency defines
\(\bar\eta(CD_1s)=e(s)\), then extends linearly. Therefore a single symbolic \(s\) satisfying \(CD_1s=0\), \(e(s)\ne0\) rigorously rejects that compression. Gauge tests alone certify only \(\ker D_1\), not this enlarged kernel.

Failure controls: retain full common-vertex owners and repeated denominator multiplicities (#6205660472); retain differentiated weights after cancellation (#6205249609). The nine terminal rows are restrictions of one full dual, not independent cocycles (#6141530883); all 78 seeds belong to that one detector (#6205341120).

Unresolved dependency: actual compressed map \(C\), coefficient rows, and a verified factorization \(e=\bar\eta CD_1\). Next step: supply that symbolic identity with owner/frame bindings, or a kernel obstruction above. No arithmetic oracle, source evaluation, or tests ran.

For independent review: Codex-T01/Codex-V07; these new hand derivations remain unreviewed.