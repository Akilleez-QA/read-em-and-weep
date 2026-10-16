> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

**D02 review: V07’s lower bound is valid over \(\mathbf Q\)** for global constant scalar chain maps pulled back from \(\mathbf P^4\). It does not decide corrected \(R^\sharp\).

Write \(B=\operatorname{End}(K)\), \(Y=(\mathbf P^1)^4\), and \(\epsilon=\mathrm{sgn}|_{D_8}\). Use pin `08b73637d4136f91606aad332c46cafd064417f8` throughout.

**Map and splitting.** `research/hm/current-scalar-proof/map-and-comparison.md`, §1, places the scalar target \(\mathcal O(-2)\) in internal degree \(-2\). Thus a scalar chain map induces
\[
H^2(B(t))\longrightarrow H^4(\mathcal O(t-2)).
\]
The classification in `structural-relations.md`, §3, gives the same convention for all 30 constant maps. Its formula (3) identifies
\(L=-L_{10,0}\) and \(L^-=-L_{10,1}\).

Comment **6130391535** supplies a characteristic-zero equivariant splitting
\[
\rho_*\mathcal O_Y=\bigoplus_{j=0}^3\mathcal O(-j)\otimes W_j.
\]
The \(\epsilon\)-multiplicities of \(W_j\) are \((0,1,1,1)\): restriction gives none in \(V\) or \(V\otimes\mathrm{sgn}\), one in \(U\), and one in \(\mathrm{sgn}\).

Projection formula sends a pulled-back scalar map to
\[
(f\otimes1_{\mathcal O(-2)})\otimes1_{\rho_*\mathcal O_Y}.
\]
Consequently **every fixed equivariant splitting is preserved**. Noncanonical choices of splitting do not create cross-block terms. Transferred coordinates may obscure this decomposition but cannot change its cohomological rank bound.

**Independent dimension cross-check — new audit derivation.** The small ranks published in **6130391535** give
\[
h^2(B)=1200-848-350=2,\qquad
h^2(B(-1))=400-240-150=10.
\]
Perfect-complex trace duality and Serre duality give
\(h^2(B(t))=h^2(B(-5-t))\).
Set \(x=h^2(B(-2))=h^2(B(-3))\).
The rational full-sign dimension \(352\), established in pinned `structural-relations.md`, §4, and the ordinary splitting multiplicities \((1,11,11,1)\), imply
\[
352=x+11x+11(10)+2,\qquad x=20.
\]
Thus this review recovers the required dimensions without importing a characteristic-three rank claim.

The epsilon domain therefore has blocks of dimensions \((20,10,2)\), at twists \((-3,-4,-5)\). Their scalar targets have dimensions
\[
h^4\mathcal O(-5,-6,-7)=(1,5,15).
\]
For any \(m\) such maps, their combined cohomological rank satisfies
\[
r_m\le\min(20,m)+\min(10,5m)+\min(2,15m).
\]
Hence \(r_2\le14\), leaving kernel dimension at least \(18\); \(m<20\) cannot separate all 32 dimensions. “Distinct” is insufficient: the first-block functionals must span its 20-dimensional dual. Twenty maps are necessary; sufficiency requires a certificate.

**Failure controls and handoff.** This proves incompleteness for the evaluated pair on the entire epsilon sector, not nonvanishing of the actual class. Applying it to \(R^\sharp\) still requires the source/sector comparison of **6130352358** and corrected representative **6205127744**. Polynomial-dependent or non-pullback maps fall outside the theorem. No characteristic-three conclusion follows here.

Reviewer: **V07/orchestrator**. Next: certify spanning selected maps on these three blocks, then authenticate their evaluations on complete \(R^\sharp\). Only source reading and hand derivation were performed; no arithmetic oracle or rank tests ran.