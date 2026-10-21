# The restricted cubic normalization is everywhere unramified

Status: structural derivation over C, independently mathematically reviewed in REVIEW.md. Not formally checked. No actual HM/source coefficients, selected vectors or matrices, point evaluations, rank tests, numerical scans, or computer algebra are used. The value of r is not selected.

## 1. Dependencies and statement

Use PR604 at a4a0b5ed6e9dd0c18e3a263d1b3f8d9a49f2bf8d (research/hm/cubic-embedding-locus/PROOF.md), PR605 at 9df4c45d0c76ded1075a0652707bdbcd1f424189 (research/hm/cubic-exceptional-fibers/PROOF.md), and PR606 at fa0abd98780293ef455a0f1191b13e250666f9ea (research/hm/cubic-endpoint-flatness/PROOF.md). Their actual-primary and modular dictionary assumptions remain in force. The embedded blowup geometry is PR601 at a582a76063b21fb4773d85d16fb39a3b54dee3bc, research/hm/conductor-blowup/PROOF.md, Sections 3–4.

Write Phi:M=Bl_Z(P4)->V for the finite normalization and g=Phi|Y:Y->T for its restriction to the smooth embedded resolution of the primary surface. Every exceptional E_z is linearly embedded by Phi and

    Y intersect E_z = R_z^+ disjoint-union R_z^-,

scheme-theoretically, where the R_z^± are two skew lines. They are the exceptional curves over the two normalization points over z. Each normalization point is a vertex of one pentagon, with precisely two distinct incident component lines. Their strict transforms meet the corresponding exceptional curve at distinct points, because the pentagon is embedded and its adjacent sides have distinct tangent directions.

The ambient nonnormal locus Sigma is empty, sixty points, or sixty disjoint lines according as r=0,1,2. The common r remains unknown.

**Theorem.**

1. For every value of r, g is unramified everywhere. Every scheme-theoretic fiber of g consists of reduced points, of length at most three. In particular the surface has no differential-failure points, even if r=2 and the ambient normalization has 120 of them.
2. The reduced singular locus and the reduced nonnormal locus of T coincide and are precisely the values with at least two preimages under g. This locus is finite. Thus g is a closed immersion if and only if it is injective on geometric points.
3. If r=1, a bad ambient point y in Sigma_ell contributes to this surface locus if and only if both of its exceptional preimages belong to Y. By normalizer symmetry there are either zero or sixty such points. A point with just one preimage in Y is a smooth point of T, despite being a singular point of V; a point with no preimages in Y is not on T.
4. If r=2, fix ell with endpoints z,w, let Q=Sigma_ell=Phi(C), where C is the strict transform of ell, and let A_z,A_w be the exceptional components of Phi^(-1)(Q). Let R_z^+ be the exceptional line containing p_z=C intersect E_z and R_z^- the other one. Then A_z is different from both R_z^±, meets R_z^+ exactly at p_z, and may meet R_z^- at one additional point q_z. The analogous description holds at w. Scheme-theoretically,

    g^(-1)(Q) = C disjoint-union {q_z if it exists}
                          disjoint-union {q_w if it exists}.

The curve C maps isomorphically onto Q and the optional points are reduced. Thus the bad surface values on Q are exactly the images of these optional points. At each y in Q the fiber length is

    1 + #{optional points mapped to y}.

In particular T is smooth at the general point of every Q, and has at most 120 singular/nonnormal points in total in this case. Coinciding images of the two optional points give a three-point reduced fiber; no such coincidence or existence is asserted. More precisely symmetry leaves only four possibilities: T is smooth; T has sixty bad values each with two preimages; T has sixty bad values each with three preimages; or T has 120 bad values each with two preimages. These describe fiber cardinalities, not analytic double- or triple-point types.

## 2. Exceptional bad-line lifts are not surface exceptional curves

Assume r=2. The lines Q associated to different component lines are pairwise disjoint by PR604. The line A_z in E_z maps isomorphically to Q, contains p_z, and hence cannot equal R_z^-.

Let ell' be the other side of the same pentagon at the normalization vertex over z. Its strict transform meets R_z^+ at a point p'_z different from p_z. Its target line Q' is a distinct component of Sigma and contains Phi(p'_z). If A_z equalled R_z^+, then Phi(p'_z) would belong to Q as well as Q', contradicting disjointness. Hence A_z is distinct from R_z^+ too.

Two distinct projective lines meeting at p_z have distinct tangent lines and reduced scheme-theoretic intersection {p_z}. Also A_z can meet the other projective line R_z^- at at most one reduced point q_z. This point is different from p_z since R_z^+ and R_z^- are disjoint. It cannot equal either of the two pentagon-side marked points on R_z^-: otherwise the same disjoint-bad-line argument would give a contradiction.

## 3. The ambient lost direction is transverse to the surface

For r=0 or r=1, the ambient differential is injective everywhere by PR604–605, so its restriction to Y is injective. For r=2 the only ambient failures occur at the p_z,p_w associated with component lines. It therefore suffices to analyze p=p_z.

Let h be a nonzero vector in T_p C. Both C and A_z map isomorphically to Q, so there is a unique nonzero a in T_p A_z with dPhi(a)=dPhi(h). Their difference k=h-a is a nonzero vector spanning the one-dimensional ambient tangent kernel. It is nonzero because C is transverse to E_z, whereas a is tangent to E_z.

The intersection T_pY intersect T_pE_z equals T_pR_z^+. Indeed Y meets E_z in the reduced smooth divisor R_z^+ near p, and this exceptional divisor is reduced Cartier on the smooth surface Y, so its defining equation has nonzero differential on Y at p. Since h belongs to T_pY, k would belong to T_pY if and only if a did. But a lies in T_pE_z, and Section 2 gives

    T_p A_z != T_p R_z^+.

These are one-dimensional subspaces, so a does not belong to T_pY. Thus k is not tangent to Y, and the differential of g is injective at p. The same proof works at every other endpoint. Cotangent Nakayama makes this equivalent to g being unramified.

## 4. The full surface inverse-image scheme of Q

PR606 identifies the complete scheme N=Phi^(-1)(Q) with the reduced nodal chain A_z union C union A_w. Consequently g^(-1)(Q)=N intersect Y scheme-theoretically inside M.

Away from the two chain junctions this is immediate: C is contained in Y, and each exceptional component intersects Y in the intersections with the two skew projective lines. Section 2 identifies the latter intersections as the junction and possibly one reduced additional point. At an optional point the intersection is reduced since two distinct projective lines have a reduced intersection, and Y intersect E_z already has its stated reduced line structure.

At p_z the completed local ring of N is C[[u,v]]/(uv), with the branch C given by v=0 and A_z given by u=0. Since Y contains C, its image ideal in this ring is contained in (v). Because T_pA_z is not contained in T_pY, some local equation of Y has nonzero derivative along A_z. Its image in the node ring is v times a unit. Therefore the image ideal is exactly (v), and the intersection is exactly the smooth branch C, with no embedded point or thickening. The calculation at p_w is identical. Equality of these finite local ideals descends from completion. This proves the full displayed scheme description in the theorem, not just its support.

In particular every fiber of g over Q is the disjoint union of its one reduced point on C and any of the optional points with that image. The same reduced-fiber conclusion follows directly everywhere from unramifiedness and the finite C-fiber condition.

## 5. Exact surface failure criterion

We recall the finite local-algebra argument. If a finite birational morphism from a smooth complex variety has one geometric preimage at y and is unramified there, write A=O_(T,y) and B=(g_*O_Y)_y. The unique preimage makes B local, with residue field C. Tangent injectivity gives m_B=m_AB by Nakayama; then B/m_AB=C. Nakayama applied to the finite A-module B/A gives B=A. Thus g is an isomorphism in a neighborhood of y and T is smooth there.

If there are at least two geometric preimages, T is nonnormal at y, because its finite normalization is not an isomorphism there. A regular local ring is normal, so y is singular. Hence the reduced singular and nonnormal loci are both exactly the multiple-fiber locus. The ambient isomorphism away from Sigma confines this locus to Sigma. The explicit classifications in Sections 1 and 4 make it finite, of cardinality at most sixty or 120 according to r=1 or r=2.

If g is injective on geometric points, the same local argument everywhere gives an isomorphism Y->T. Composing with the closed embedding T in P9 gives a closed immersion. The converse is immediate.

## 6. Symmetry makes the remaining finite alternatives uniform

The normalizer preserves S, Z, the blowups M and Y, and the complete cubic system, so it acts equivariantly on g:Y->T. PR604 proves transitivity on the sixty component lines ell, and thus on their nonempty bad loci Sigma_ell. For r=1 the condition that both preimages belong to Y is invariant; it therefore holds for all sixty bad ambient values or for none.

For r=2 the number n of distinct multiple-fiber values on Q is invariant and belongs to {0,1,2}. If n=0, there are none anywhere. If n=2, each of the two optional points gives a different value, each with exactly two preimages; there are 120 such values. If n=1, there are sixty values in total; their fiber length is uniformly either two or three, since equivariance takes the unique bad value on one Q to the unique bad value on any other Q. This proves the four listed alternatives without assuming transitivity on ordered endpoint flags.

The optional point q_z cannot map to alpha=Phi(p_z), because Phi embeds A_z and q_z differs from p_z. Similarly q_w cannot map to beta. Thus any bad value at an endpoint has exactly two surface preimages, and any three-point surface fiber must lie away from both endpoints.

## 7. Contribution and limitations

The ambient and surface geometries differ sharply: the ambient map may lose a tangent direction at 120 points and be nonnormal along sixty entire lines, while the restricted surface map never loses a tangent direction and its image is smooth at the general point of every such line. All possible surface failure is now a finite reduced-fiber identification problem. In r=2 it reduces exactly to whether each exceptional lift line meets the opposite branch's exceptional line, and whether the two optional images coincide.

This does not prove the remaining intersections exist or are empty. It does not choose or exclude r, claim transverse intersections of image surface branches, determine local analytic singularity types or the conductor length at a multiple point, or prove normality of T. Complete-system ampleness and the known degree products alone do not exclude finite identifications; no inference of very ampleness is made from them. No new numerical intersection-theory exclusion of r is claimed.
