# Rank-one trace quadrics really occur, and their nilpotent plane cubics carry nontrivial 3-torsion

## Scope and conclusions

Work over C. All spaces below are abstract universal subspaces of sl(U), with dim U=3. No identification with actual HM structural kernels is asserted.

1. There exist four-dimensional subspaces K⊂sl(U) containing no nonzero rank-one endomorphism for which q(A)=tr(A²)|K has rank exactly one. Thus the universal nonvanishing theorem for q cannot be strengthened to rank at least two (and in particular not to rank at least three).
2. One can choose such K so that its reduced projective nilpotent locus is a smooth plane cubic C. Scheme-theoretically the nilpotent locus is the complete intersection (ℓ²,h), where ℓ=0 is that plane and h=det|K; it is generically a doubled curve, not a reduced plane cubic.
3. On any smooth plane cubic arising as det=0 in a rank-one-free totally isotropic three-dimensional subspace, the regular-nilpotent kernel filtration has graded pieces M⁻¹⊗T, T, M⊗T, where M=O_C(1) and T is a nontrivial line bundle of order three. This is an additional constraint beyond the surface obstruction.

These are universal existence and structure statements. They do not assert that any actual structural kernel K_W has quadratic rank one.

## 1. Isotropic planes avoiding rank one

Let V=sl(U), of dimension eight, with nondegenerate symmetric bilinear form B(A,D)=tr(AD). Its projective null quadric Q⊂P(V) is smooth of dimension six.

Let Y⊂P(V) be the locus of nonzero rank-one traceless endomorphisms. A rank-one operator is u⊗φ, with trace φ(u). Consequently

    Y ≅ {([u],[φ])∈P(U)×P(U*): φ(u)=0}.

This is a smooth projective incidence flag variety of dimension three. Since (u⊗φ)²=φ(u)(u⊗φ), it lies in Q.

Let G=OG(3,V) be the orthogonal Grassmannian of totally isotropic three-dimensional vector subspaces. It is irreducible of dimension

    3(8−3)−3(3+1)/2 = 9.

Consider the projective incidence I={(y,R)∈Y×G: y∈P(R)}. For a fixed isotropic line y, the quotient y⊥/y is nondegenerate of dimension six, and isotropic three-spaces containing y correspond to isotropic two-spaces in this quotient. The fiber is OG(2,6), of dimension

    2(6−2)−2(2+1)/2 = 5.

Thus dim I=3+5=8. Its image in G is closed and proper, since the projection is projective and dim G=9. The nonempty open complement consists precisely of totally isotropic three-spaces R containing no nonzero rank-one endomorphism.

The dimension formula can be checked in local Grassmannian coordinates: the differential of the symmetric restriction-form equations is surjective, since nondegeneracy permits any prescribed symmetric pairing on the chosen isotropic subspace. Hence the k(k+1)/2 equations cut smoothly in Gr(k,n). Irreducibility follows from transitivity of the connected group SO(n,C) for k<n/2: Witt extension gives an orthogonal isometry between any two isotropic k-spaces, and, if necessary, its determinant is adjusted on their nonzero nondegenerate complementary quotient. All Grassmannians used here are below the maximal-isotropic threshold.

## 2. Extension to four dimensions with quadratic rank one

Choose R from this open complement. Since R is totally isotropic, R⊂R⊥, and R⊥/R is a nondegenerate quadratic vector space of dimension two. Choose a nonisotropic line in this quotient and let K⊂R⊥ be its inverse image. Then dim K=4, the radical of B|K is exactly R, and q|K has rank one.

In particular its projective zero set is exactly P(R): after choosing a linear equation ℓ for R⊂K, q|K=cℓ² for some c≠0.

Every traceless rank-one endomorphism has q=0. Any such endomorphism in K would therefore belong to R, contradicting the choice of R. Thus K is rank-one-free.

This construction proves that quadratic rank one is genuinely compatible with all the abstract hypotheses. It does not compute or exhibit an actual structural kernel.

## 3. A general choice yields a smooth nilpotent plane cubic

Inside Q let D be the determinant-zero divisor. Its points are exactly projective nilpotent traceless operators. Its singular rank-one locus is Y; on D\Y all operators are regular nilpotent, and D is smooth there as a hypersurface of Q.

Here is a direct verification of the latter assertion. At a regular nilpotent A, the differentials of q and det on sl(U) are represented under the trace pairing by 2A and adj(A)=A². They are linearly independent: a relation A²=tA would, by nilpotence and A²≠0, be impossible. Thus q and det cut transversely in P(V) at such a point. The projective radial direction causes no issue because both homogeneous equations vanish there.

The connected orthogonal group SO(V,B) acts transitively on Q and on G. By generic transversality in characteristic zero for translates in a smooth homogeneous variety, a general isotropic projective plane P(R) meets the smooth locus D\Y transversely. It avoids Y by Section 1. Consequently its intersection with D is a smooth curve, provided det|R is nonzero.

For completeness, det|R is nonzero for every R chosen in Section 1. Otherwise P(R) would be a projective surface of regular nilpotents, excluded by the filtration/Chern-class theorem in ../isotropic-four-kernel-exclusion/PROOF.md, Sections 1–3. The intersection is therefore a plane cubic and is nonempty. A smooth plane cubic is connected and irreducible (distinct positive-degree plane components must intersect), and has genus one.

Here is the incidence argument behind the transversality statement, so no special theorem about isotropic planes is required. Fix an isotropic plane P(R₀), set H=SO(V,B), and consider the action map a:H×P(R₀)→Q. It is smooth: the differential in the H direction alone surjects onto every tangent space of Q by transitivity. Thus Z=a⁻¹(D\Y) is smooth. The projection Z→H is dominant, because a general translated plane avoids Y and has a nonzero cubic restriction, hence meets D\Y. In characteristic zero, generic smoothness gives a nonempty open subset of H over which all its fibers are smooth. These fibers are exactly gP(R₀)∩(D\Y), up to translation. Intersect this open subset with the open condition of avoiding Y. The resulting intersections are smooth plane cubics. This uses only the ordinary generic smoothness theorem; no transversality at Y is assumed.

Now extend this general R to K as in Section 2. The projective nilpotent subscheme in P(K) is cut out by q and det, hence by ℓ² and h=det|K. Its reduction is the smooth plane cubic C={ℓ=h=0}. Because h|R defines a smooth curve, at each point of C its derivative in some direction tangent to the plane is nonzero. Locally h and ℓ are therefore independent regular parameters in the smooth ambient P³. The ideal (h,ℓ²) defines the double structure in the ℓ direction; in particular it is generically length two over C and has complete-intersection degree six. No assertion that this double structure globally splits is made.

## 4. Nilpotent filtration on the smooth cubic

Let R be any rank-one-free totally isotropic three-space such that C={det|R=0}⊂P(R) is smooth. Put M=O_C(1), E=U⊗O_C, and let N:E→E⊗M be the universal endomorphism. On C it has regular nilpotent fibers. As in the surface proof, its kernel flag F₁=ker N⊂F₂=ker N² has graded pieces

    L, L⊗M, L⊗M²,

where L=F₁. Taking determinants of the trivial bundle E gives L³⊗M³≅O_C. Thus T=L⊗M satisfies T³≅O_C, and the graded pieces become

    M⁻¹⊗T, T, M⊗T.

In particular deg L=−3 and deg(E/F₂)=3; the kernel-line and quotient-line classifying maps each pull back the respective projective hyperplane bundle to a line bundle of degree three. The middle graded piece T is a degree-zero 3-torsion line bundle.

## 5. The torsion cannot be trivial

Suppose T≅O_C. Then the kernel inclusion L=M⁻¹→U⊗O_C is represented by a nonzero vector of three sections of M. Every such section extends uniquely to a linear form on P(R): restriction H⁰(P²,O(1))→H⁰(C,O_C(1)) is an isomorphism, as follows from the ideal sequence of a plane cubic.

Let u be the resulting nonzero U-valued linear form on R. The kernel relation N u=0 on C says that each coordinate of the U-valued quadratic polynomial A↦A u(A) vanishes on C. The ideal of C has no nonzero homogeneous elements of degree two, so this relation holds identically on R.

But det|R is nonzero, by the same no-projective-surface theorem used above. On its nonempty complement, A is invertible, so u(A)=0. A linear polynomial vanishing on a dense open set is identically zero, contradicting the nonzero kernel inclusion.

Therefore T is nontrivial. Since its cube is trivial, it has exact order three in Pic⁰(C).

## Consequences and limitations

The projective-curve case is qualitatively different from the projective-surface case: smooth complete elliptic curves of regular nilpotents do exist, and the relevant obstruction is nontrivial 3-torsion rather than a positive self-intersection contradiction. Any proposed universal exclusion of low quadratic rank must fail; further exclusions for actual structural kernels must use additional properties beyond rank-one-freeness.

## 6. The determinant cubic is irreducible

Every K produced in Section 2 has nonzero restricted determinant h. Indeed h|R is already nonzero. If h were reducible over C, its total degree three would force a linear factor ℓ₀. The hyperplane L₀=ker ℓ₀⊂K would then be a three-dimensional rank-one-free subspace on which determinant vanishes identically. By ../constant-rank-kernel-nets/PROOF.md, Sections 1–4, q|L₀ has rank three. Restriction cannot increase quadratic rank, contradicting rank(q|K)=1. Hence h is irreducible.

Thus irreducible determinant cubics with trace-square rank one and rank-one-free K actually exist in universal algebraic geometry. Excluding the irreducible-cubic branch of an actual structural-kernel problem requires additional hypotheses about that problem. This corollary uses only the established constant-rank-net theorem and does not depend on any newer classification of reducible cubics.
