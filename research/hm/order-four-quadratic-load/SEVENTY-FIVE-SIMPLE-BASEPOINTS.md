# The seventy-five simple base points and Chow ramification

## Source geometry and notation

Fix a general smooth modular parameter B in Gamma. The actual beta surface is the degree-fifteen scroll S_B, with normalization ν:R -> S_B. Let h=ν^*O(1). It has h²=15. Its twenty-five distinguished rulings map isomorphically to the HM lines; their union C_R has h.C_R=25 and C_R²=0.

ADHPR Proposition4.16 identifies each ruling line d_q as the directrix of the smooth rational cubic scroll X_q swept out by secants of the elliptic quintic E whose endpoints sum to q. It also states that the scroll is smooth off E and that four rulings pass through each point of E. Proposition4.19 gives a graph section in R mapping by multiplication by two to E. We use the exact actual-net dictionary, not a merely analogous family.

## 1. A directrix meets E simply

The cubic scroll X_q is F1, with negative section C0 and ruling f, polarized by C0+2f. Its rulings are the defining secants, so E.f=2. Write E=2C0+b f. Since E has degree five, E.(C0+2f)=2+b=5, hence b=3. Therefore

    E.C0=1.

As E is smooth and does not contain C0, its intersection with the directrix is one reduced point. In particular its tangent is distinct from the directrix tangent there.

At each graph point of R, the graph-section derivative maps nontrivially to the elliptic tangent because multiplication by two is etale. The ruling derivative maps nontrivially to the directrix tangent because each ruling maps isomorphically onto its line. The two tangent directions are distinct by the preceding computation. Thus ν is immersive at every graph point.

## 2. The other three branches are transverse to the HM line

Let p be the origin on the chosen HM line C_i for this modular parameter. The four rulings through p are indexed by the four two-torsion points. They are invariant under elliptic inversion. The distinguished ruling maps to C_i, fixed pointwise by the projective involution. The other three ruling lines through p are invariant but cannot be pointwise fixed: the fixed locus in P4 is the disjoint union of the HM line and the opposite fixed plane, which does not contain p. Their tangent eigenvalue at p is therefore minus one. The elliptic tangent also has eigenvalue minus one.

By the immersion proved in Section1, the tangent plane of each of the other three normalization branches is two-dimensional and lies in the minus-one eigenspace. The tangent of C_i lies in the plus-one eigenspace. These branch tangent planes are transverse to C_i. Consequently the pullback of I_C to each of these three points is its reduced maximal ideal on the smooth surface R: its linear parts span the full two-dimensional cotangent space, and Nakayama's lemma gives the assertion.

At the distinguished ruling, the pullback ideal has that ruling as a simple divisor. The same independent-tangent argument at its graph point, and the smoothness of S_B away from E elsewhere, verify multiplicity one throughout. Heisenberg equivariance gives the same description for all twenty-five HM lines. The three extra preimages for each line are distinct, and preimages belonging to different source points cannot coincide.

Thus on R the actual evaluation-minor base ideal consists of C_R with multiplicity one and seventy-five isolated reduced point bases, each disjoint from C_R. No other bases occur: outside the singular elliptic curve the normalization is an isomorphism, and a ruling meets that curve in the unique point described above.

## 3. The fixed-B kernel map has degree fifty

The six minors generate I_C(5), so after removing the fixed divisor C_R and blowing up the seventy-five reduced point bases, the kernel map is basepoint free. Its target is the plane of projective lines in P(U*) through B. Its line bundle is

    5h-C_R-sum_{j=1}^{75} F_j.

Its square is

    25*15 - 10*25 - 75 = 50.

Therefore this map dominates that plane and has degree fifty. This proves that the non-exceptional canonical Gamma-incidence component dominates the Chow divisor T, rather than assuming it from dominance of the ambient kernel map.

## 4. Generic multiplicities

The ambient map g:Bl_C(P4) -> Gr(2,4) has degree one hundred by KERNEL-GRASSMANNIAN-DEGREE.md. Every E_i maps birationally onto T. Let e be its common generic pullback multiplicity, and let m be the multiplicity of the non-exceptional component Z. The degree-fifty result above and uniqueness of a general Gamma-intersection give

    100=25e+50m.

Both e and m are positive integers, so e=2 and m=1. In particular the strict non-exceptional Chow pullback is generically reduced and each exceptional divisor has generic ramification index two.

The substituted degree-thirty Chow polynomial therefore has order eight along each HM line. Its reduced hypersurface off C is the canonical Gamma-incidence image. Since the latter maps generically birationally from the canonical threefold and h³=30, it has degree thirty. Thus the degree-thirty polynomial itself is reduced. This uses the degree-fifty argument; generic etaleness alone would not justify the conclusion.

Primary source: https://arxiv.org/pdf/alg-geom/9606013, Propositions4.16 and4.19 and Lemma4.15. All computations are symbolic intersection and local ideal arguments; no selected HM rank or coefficient test is used.

## 5. Residual ramification class

Since Y and Gr(2,4) are smooth and g is generically finite in characteristic zero, its Jacobian gives the effective ramification divisor

    R_g=K_Y-g^*K_Gr=15H-2 sum E_i.

The generic ramification index two gives coefficient one along each E_i. Removing these twenty-five components leaves an effective residual divisor with class

    R_res=15H-3 sum E_i=3D.

Its D³-degree is 600; the exceptional ramification has D³-degree 25*12=300. This is a line-bundle statement, not a claim that the residual ramification is pulled back from a cubic equation on the Grassmannian.
