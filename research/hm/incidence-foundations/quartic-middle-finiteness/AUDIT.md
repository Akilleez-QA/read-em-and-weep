# Independent audit: rank-two flags and quartic middle finiteness

## Verdict and scope

PASS over C under the three stated hypotheses: trilinearity, outer symmetry plus cyclic zero, and injectivity of every repeated-input map V/Ca -> J. The closed rank-at-most-two flag incidence has finite image in the pair of middle-line and hyperplane spaces. Both quartic normal forms transfer to this incidence with the stated minus sign WHEN the actual correction is compatible on a dense open of the quartic surface. The kernel type alone does not imply that compatibility. The combined line-projected surface consequence is valid using the separately established finite rectangular and annihilation incidences.

This audit independently checks the argument in PROOF.md, including all boundary points, the splitting convention, the intrinsic corrected hyperplane, and the dimension statements. It does not claim that the flag incidence itself has finite support. Its two-plane fibers have not been bounded here. No assertion about reduced scheme structure is needed.

## 1. Repeated-input independence

Put A_a(b)=f(a,a,b). Outer symmetry and cyclic zero imply

    f(x,u,x)=-2A_x(u),
    A_(u+t x)(x)=A_u(x)-t A_x(u).

For independent u,x, both repeated values are nonzero. If they were dependent, write A_u(x)=t A_x(u). The second identity would contradict repeated-input injectivity, since u+t x and x remain independent for every scalar t. This establishes the exact independence needed below, with no genericity restriction.

## 2. Complete boundary exclusion

Let X be a two-plane contained in a hyperplane H, and let M be the image span of f(X,u,H), assumed to have dimension at most two.

If u belongs to X, M contains A_u(H). Its dimension is three because the kernel of A_u on V is precisely Cu. Thus this case is impossible.

Suppose u belongs to H but not X. Outer symmetry gives f(x,u,u)=A_u(x), and A_u is injective on X. Therefore M=A_u(X), of dimension two. For every x in X, the value f(x,u,x) lies in M. The inverse of the linear isomorphism A_u:X -> M defines a homogeneous quadratic map

    g(x)=(A_u|X)^(-1)f(x,u,x).

After choosing a nonzero volume form on X, x wedge g(x) is a homogeneous binary cubic. It has a nonzero zero over C, whether or not it is identically zero. At that x, g(x) is proportional to x. Hence -2A_x(u) is proportional to A_u(x), contradicting Section 1.

It follows that u is outside H at EVERY point of the determinantal incidence. No constancy of a normal form, image rank, or residual-kernel type in a family was used. The argument also covers rank-zero and rank-one restrictions by contradiction within the same proof.

## 3. Projector argument and scheme qualifications

The incidence is closed in P(V) times Flag(2,4;V), defined by the three-by-three minors of the trilinear bundle map. The target may be taken finite-dimensional without loss by replacing J by the span of the image of f.

Its reduction is projective with finitely many irreducible components. By Section 2 the tautological middle line and hyperplane form a direct-sum decomposition of the trivial V-bundle. Projection onto the line along the hyperplane is therefore a regular matrix on the whole reduced incidence. Explicitly, for H=ker alpha, it is u tensor alpha divided by alpha(u). This expression is invariant under rescaling either representative and its denominator is nowhere zero.

On an integral projective component, every entry is constant. The image and kernel recover the middle and hyperplane, so their pair is constant. Finitely many components give finitely many pairs. One can equally apply constancy on reduced connected projective components. Nilpotent scheme structure is irrelevant to this set-theoretic conclusion and is not shown to vanish.

The use of a CLOSED flag incidence is essential: it proves compactness and boundary control directly, rather than assuming that initially chosen quartic data extend with the same normal form. Even a family whose quartic presentation degenerates cannot acquire a new moving middle through this incidence.

## 4. Sign, transfer, and intrinsic hyperplane

Fix a nonzero u and write E=V/Cu with a linear splitting s:E -> V. Use precisely the convention

    A_u(v(ab))=f(s(a),u,s(b))  for ab in K.

Assume the actual correction v is compatible on a dense rank-two open of the quartic surface. Under that hypothesis, the quartic classification gives K of dimension five and full support, K contained in XE for dim X=2, and v=D_d where

    D_d(ab)=d(a)b+d(b)a.

Define s'(a)=s(a)-d(a)u. Expansion gives

    f(s'(a),u,s'(b))
      =f(s(a),u,s(b))-A_u(d(a)b+d(b)a).

The quadratic cross term vanishes because f(u,u,u)=0. Thus the lifted K is killed by f(-,u,-). The image H=s'(E) is a hyperplane complementary to Cu, and X'=s'(X) is a two-plane in H. The symmetric product X'H has dimension seven, with the lifted five-dimensional K in its kernel. Therefore rank f(X',u,H) is at most two. This verifies the required flag membership with the correct minus sign.

The hyperplane is intrinsic, although existence alone suffices for finiteness. Under s -> s+t*u, the correction changes by v -> v+D_t. Therefore d -> d+t, and the corrected splitting s-d*u is unchanged. Replacing u by c*u changes A_u by c squared and the middle bilinear map by c, so v and d change by 1/c; again the corrected splitting is unchanged.

There is no ambiguity in d: for d nonzero, the kernel of D_d on Sym^2 E is Sym^2(ker d). This follows by choosing a vector e with d(e)=1 and decomposing Sym^2 E into Sym^2(ker d), e*(ker d), and Ce squared. Thus D_d vanishing on K would force K to have support in the proper hyperplane ker d. Full support excludes that. Consequently any two complements killing K agree.

All this is pointwise. No regular familywise choice of u, splitting, basis, factor line, or contraction is needed to apply the fixed finite-image incidence.

## 5. Entire quartic fibers and dimension

Every middle in this section is assumed to have the actual correction densely compatible on the quartic surface. Merely having residual kernel type A or B is insufficient. Once compatibility supplies the contraction and it is removed, the equations below show that the entire rank-two locus is compatible.

The exact rank-two-locus calculation in /research/hm/normalizer-rank-five/line-projected-rank-five-reduction/QUARTIC_REALIZATION.md, Section 1, uses only the two local normal forms and does not depend on its separate global-realization construction. It is applicable here.

Indeed if ab belongs to K contained in XE, its image in Sym^2(E/X) is zero. The symmetric algebra is a domain, so one factor belongs to X. The exact two-dimensional kernels W_l then parametrize all such products. Squarefreeness guarantees independent factors. Their ordered locus is the union of the projective-bundle surface and its swapped image, hence has dimension two.

After removing the contraction, the lift equation is

    f(l+alpha*u,u,m+beta*u)=A_u(beta*l+alpha*m).

Repeated-input injectivity and independence of l,m force alpha=beta=0. An independent zero cannot have a zero residual outer factor by the same injectivity, nor proportional nonzero residual outer factors because that would give a square in K. Thus the ordered projective fiber is exactly the surface union just described. Finite middle image gives projective dimension two; the three independent nonzero input scalings give affine dimension five. Empty loci, naturally, satisfy the asserted upper bound.

## 6. Integration with line-projected rank-five surfaces

The classification in /research/hm/normalizer-rank-five/line-projected-rank-five-reduction/PROOF.md bounds the generic factor-kernel bundle to degrees zero, one, or two. Its degree-two case is exactly the quartic classification used above. Degree zero yields a corrected (2,2) annihilation rectangle with middle in the previously proved finite C_(2,2) image. Degree one, after the square-avoidance exclusions and the dependent-span exclusion stated there, leaves the explicit full-support cubic type III.

For type III the finite-incidence theorem in /research/hm/incidence-foundations/finite-rectangular-incidence/PROOF.md applies under precisely the same tensor hypotheses. Its Section 5 supplies the corrected rectangular spans, so type III middle points are finite as well. This is the stronger finite-incidence result, not merely the earlier dimension-one bound for rectangular middle images. The underlying determinant-pole argument in /research/hm/incidence-foundations/fixed-splitting-curve-exclusion/STRONGER.md allows constant as well as moving middle curves; the boundary quotient-projector argument of the finite-incidence proof then handles its remaining noncomplementary triples.

Consequently the UNION of all three middle sets is finite. This proves finite middle image for the full-support five-dimensional residual-kernel surface stratum WITH an ordered factor image equal to a line. A component generically having such projective surface fibers therefore has constant middle and projective dimension two, giving affine dimension five after restoring scalings. The broader formulation with generic fiber dimension at most two is also valid over this finite middle set.

This integration does not classify surfaces whose factor images are not lines, does not show that the whole rank-five middle stratum is finite, and does not control moving-middle components with generic projective fibers of dimension one. The quartic flag theorem itself does not require the finite-rectangular theorem; only the combined degree-one integration uses it.

## 7. Reference correction and provenance

In PROOF.md, Section 7, the type III transfer is in Section 5 of /research/hm/incidence-foundations/finite-rectangular-incidence/PROOF.md, rather than Section 4. This is a citation correction only and does not affect the argument. The theorem and Sections 4–5 were corrected to state dense compatibility of the actual quartic correction explicitly. That scope correction is necessary and is incorporated throughout this audit: no contraction conclusion is inferred from the kernel type alone.

