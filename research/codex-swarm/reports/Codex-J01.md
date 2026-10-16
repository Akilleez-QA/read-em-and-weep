> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

Codex-J01 — **source-based mixed-jet recurrence; no obstruction decision.**

Authenticated pin: `08b73637d4136f91606aad332c46cafd064417f8`. Git object IDs matched both supplied blobs for `research/hm/current-scalar-geometric-dependencies/data/{source-formulas.js,model.json}`.

Use coordinates \(1,\ldots,4\) (code indices \(0,\ldots,3\)). Work in characteristic zero on a finite common overlap where the displayed denominators and transitions are invertible. Keep complete vertex/mask owners.

Write
\[
C_{uv}=(P_uI_v)^t,\quad D_v=\operatorname{diag}(\nu_v,\nu_v^{-1}),
\quad g_{uv}=D_vC_{uv}D_u^{-1}.
\]
Here \(I,P\) are evaluated through the pinned elementary-symmetric coefficient map. Set
\[
\sigma=\operatorname{diag}(1,-1),\quad
\alpha_{v,a}=m_{v,a}\frac{x_a^2+1}{2x_a(x_a^2-1)},\qquad
L_{uv,a}(X)=\alpha_{v,a}\sigma X-\alpha_{u,a}X\sigma .
\]

**New hand-derived producer.** For distinct \(a,b\), define
\[
Z_{uv,ab}=\partial_a\partial_bC_{uv}
 +L_{uv,a}(\partial_bC_{uv})
 +L_{uv,b}(\partial_aC_{uv})
 +L_{uv,a}L_{uv,b}(C_{uv}).
\]
Then exactly
\[
\partial_a\partial_bg_{uv}=D_vZ_{uv,ab}D_u^{-1}.
\]
Proof: differentiate twice; \(\partial_a\alpha_{v,b}=0\) for \(a\ne b\). Thus every physical-frame derivative is retained. The carrier derivative is explicitly
\[
\partial_{ab}C_{uv}
=(P_{u,ab}I_v+P_{u,a}I_{v,b}
 +P_{u,b}I_{v,a}+P_uI_{v,ab})^t.
\]

Let
\[
T=Z_{jk,13}Z_{ij,24}-Z_{jk,14}Z_{ij,23}
  -Z_{jk,23}Z_{ij,14}+Z_{jk,24}Z_{ij,13}.
\]
The actual left-normalized mixed Moyal contribution, after removing the common \(y_1y_2y_3y_4\), is
\[
\boxed{\mathcal Q_2=\tfrac14D_iC_{ik}^{-1}TD_i^{-1}.}
\]
This follows directly from `crossResidual`. `globalCross` adds the three gerbe terms; it does not change this contraction. The four signs and coefficient \(1/4\) are already published in `research/hm/current-scalar-residual-attribution/closure-and-characters.md`, §2; the frame-retaining producer above is this report’s derivation.

**Exact component criterion.** Put \(C_{ik}=\begin{pmatrix}a&b\\c&d\end{pmatrix}\), \(\Delta\ne0\). Then \(\mathcal Q_2^0=0\) iff all three rational expressions vanish:
\[
dT_{12}-bT_{22},\qquad
aT_{21}-cT_{11},\qquad
dT_{11}-bT_{21}+cT_{12}-aT_{22}.
\]
An authenticated nonzero numerator after exact denominator clearing certifies only this component’s nonvanishing. It does **not** certify \(R^\sharp\), its cohomology class, or the complete detector pairing.

**Failure control.** The contraction couples jet slots \((13,14,23,24)\) by a symmetric signed antidiagonal matrix, but matrix products retain their order. That slot symmetry alone proves no cancellation. Frozen normalization must preserve the logarithmic jets, as required by comment **6205660472**.

**Missing Omega binding:** published definitions of \(\Omega,J,S,H\); their dimensions, index order and coefficient ring; derivative and transpose conventions; physical-frame conversion; and whether the asserted equivalence concerns this component, complete \(R^\sharp\), or a detector pairing. None is inferred here.

Reviewer: **Codex-J02/Codex-V03**, review pending. Next step: compare the supplied package against this recurrence and retain every term of corrected \(R^\sharp\) from comment **6205127744**. No physical evaluation, polynomial expansion, CAS, or oracle execution was performed.