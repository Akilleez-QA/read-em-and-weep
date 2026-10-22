# Every surviving quadric obstruction has a singular integral spectral cover

## Statement and inputs

Let Q⊂P4 be a smooth complex quadric threefold in the common primary-injective/residual-surjective open. Put V=F|Q, where normalized HM F has determinant O(-1). Primary injectivity gives H0(V(2))=0. Any nonzero φ∈H0(End_0(V)(4)) defines an integral double spectral cover

π:Y=Spec_Q(O_Q⊕O_Q(-4))→Q,

whose multiplication is specified by λ²=-det φ. This Y is necessarily singular. This is a necessary condition on actual kernel sections, not their exclusion.

## 1. No generic-rank-one twisted endomorphism

In fact there is no nonzero map ψ:V→V(4) of generic rank one. Its kernel is reflexive rank one: the image is torsion-free, and the depth lemma applied to the kernel of the bundle map gives the S2 condition. On smooth Q it is therefore O_Q(a). Likewise the saturation of the image in V(4) is a rank-one reflexive subsheaf O_Q(b+4). Here Pic(Q)=Z·O_Q(1).

Both O(a) and O(b) inject into V. Since H0(V(2))=0, multiplying any section of V(k), k≤2, by a nonzero polynomial of degree2-k shows H0(V(k))=0. Thus a,b≤-3.

The quotient V/O(a) is rank-one torsion-free with double dual O(-1-a), so equals I_W(-1-a) for a subscheme W of codimension at least two. The nonzero induced map

I_W(-1-a)→O(b+4)

extends across codimension two, since Hom(I_W,O_Q)=O_Q. Hence H0 O_Q(a+b+5)≠0. But a+b+5≤-1, contradiction.

If the trace-free characteristic polynomial of nonzero φ split over K(Q), its eigenvalue s would be a rational section of O_Q(4) with square -det φ. The local coefficient of s is integral over every normal local ring of Q and so regular; hence s is a global section. Then φ-s·id is nonzero of generic rank one, contradiction. The same argument includes det φ=0. Therefore the spectral polynomial is irreducible over K(Q), and Y is integral.

## 2. A smooth spectral cover would give a line bundle

The spectral correspondence here is elementary: φ equips V with the module action of O_Q⊕O_Q(-4). Let L denote the resulting coherent sheaf on Y, so π_*L=V. Since the quadratic polynomial is irreducible, L has generic rank one over Y.

At any closed point of Y, a regular system of parameters of the underlying smooth base Q is a regular sequence on this module, because its pushforward is a rank-two locally free O_Q-module. Localizing preserves regularity. Thus L is maximal Cohen–Macaulay of depth three. If Y were smooth, Auslander–Buchsbaum over its regular local rings at closed points would make L locally free (the nonfree locus is closed). Its generic rank one then makes L a line bundle.

## 3. Rational cohomology alone gives an integrality contradiction

Y is a smooth two-section of the ample line bundle O_Q(4), if it is smooth at all. Wiśniewski's Proposition1.1(d), printed p207 in the primary paper below, says pullback induces an isomorphism on complex cohomology outside the middle degree for a smooth n-section of an ample line bundle. In particular

H²(Y,C)=C·h,  h=π*H,  ∫_Y h³=2∫_Q H³=4.

No integral Picard-group assertion and no generic-branch Noether–Lefschetz assumption are needed.

For a line bundle L on a finite flat double cover,

det(π_*L)=Norm(L)⊗det(π_*O_Y).

Here π_*O_Y=O_Q⊕O_Q(-4) and det V=O_Q(-1), so Norm(L)=O_Q(3). On first Chern classes this means π_*c1(L)=3H. Since π_*h=2H and H²(Y,C) is one-dimensional, c1(L)=(3/2)h. Therefore

∫_Y c1(L)³=(3/2)³·4=27/2.

The left side is an integer for a genuine line bundle on a smooth projective threefold. Contradiction. Consequently Y is singular.

Equivalently, the discriminant divisor (-detφ=0) in |O_Q(8)| cannot be smooth: locally λ²=f has singularities exactly over f=df=0. No assertion that this divisor is reduced, irreducible, or has only isolated singularities is made.

## Boundary and provenance

The surviving obstruction must therefore be a rank-one maximal Cohen–Macaulay spectral sheaf on a singular integral double cover, with pushforward exactly V. This is narrower than allowing arbitrary twisted endomorphisms or smooth spectral covers. It does not rule out singular covers, which can have extra divisor classes or non-locally-free rank-one MCM modules.

Primary topology source: Jarosław A. Wiśniewski, “On topological properties of some coverings. An addendum to a paper of Lanteri and Struppa”, Canadian Journal of Mathematics44(1992),206–214, Proposition1.1(d), p207, DOI10.4153/CJM-1992-013-8:
https://www.cambridge.org/core/services/aop-cambridge-core/content/view/4E979157FC0BF4D5504E42C2EC711689/S0008414X00010464a.pdf/on-topological-properties-of-some-coverings-an-addendum-to-a-paper-of-lanteri-and-struppa.pdf

The proposition was read in full at its source. It applies to arbitrary smooth n-sections, not just general cyclic branch divisors. Its hypotheses hold for the assumed smooth spectral cover, embedded in Tot(O_Q(4)), finite of degree two over Q. The elementary spectral, depth, and norm calculations above supply the application.

Actual HM inputs: PR538 at d5d9bd997145b0ecf7d7bd659a19fb7845afb75f and common-open proof at14f4154ce6657e791a5e0fcdd9fdb67f9014712f. This proof uses no selected polynomial values, HM matrices, rank evaluations, or numerical experiments. It makes no full Q4 claim.

## 4. Elementary strengthening: every kernel section vanishes somewhere

The smooth-cover contradiction also has an independent elementary proof which localizes a forced singularity. Write the formal Chern roots of F as α,β. Those of B=End_0(F) are 0,α−β,β−α. Hence

c1(B)=0,
c2(B)=−(α−β)²=4c2(F)−c1(F)²=15H²,
c3(B)=0.

On Q the rank-three bundle B_Q(4) therefore has

c3(B_Q(4))=(4H)³+(4H)c2(B_Q)=124H³,
∫_Q c3(B_Q(4))=248.

Every global section φ of this bundle has a nonempty zero scheme. Otherwise O_Q→B_Q(4) is a subbundle and its cokernel is a rank-two vector bundle, forcing c3(B_Q(4))=0, contradiction.

At a zero p of φ, all local entries of φ lie in the maximal ideal m_p, so detφ∈m_p². The spectral equation λ²+detφ=0 consequently has no linear term at (p,0); in the smooth four-dimensional total space of O_Q(4), this is a singular point of Y. Thus every kernel section forces spectral singularities specifically over its own nonempty zero scheme. This argument requires neither the cyclic-cover topology theorem nor a Picard-group assertion.

If the zero scheme is finite, its length is exactly248. Indeed three local component functions of a section on the smooth threefold cut a zero-dimensional scheme, hence form a regular sequence in each regular local ring. Its class is the top Chern class and its length equals the displayed integral. Finiteness, reducedness, and regularity of a general section are NOT asserted. A positive-dimensional zero locus is allowed; in that case248 is a localized Chern intersection number, not its length or the number of singular points.
