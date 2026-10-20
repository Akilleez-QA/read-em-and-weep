# Plane components of the K7 polar rank-drop locus

Work over C. Let E have dimension four, K⊂Sym²E have dimension seven, W=K⊥ have dimension three, and v:K→E be linear. Assume square avoidance:

    v(a²)∉Ca whenever a≠0 and a²∈K.

Write q_i(a)=B_i(a,a) for a basis of W, and M(a)b=(B_i(a,b))_i. Assume M has generic rank three. A compatible ordered threefold means an integral projective threefold Z⊂P(E)×P(E) meeting the independent-pair locus densely, on which ab∈K and v(ab)∧a∧b=0. The wedge identity on the diagonal is not itself square compatibility; all eigenline conclusions below use differentiation or an established square-avoidance theorem.

## Results

Let A=P(F)⊂P(E) be a plane contained in D={rank M≤2}, let z define F, and let r=dim(W|F).

1. If r=3, W has a common radical vector. This branch is already excluded by the common-radical K7 theorem.
2. If r=2, W contains z²; conversely every net containing z² has A⊂D, irrespective of its restricted dimension.
3. If r≤1, A cannot be a factor image of a compatible ordered threefold. These restriction cases do not in general force a common radical or a square in W.
4. Suppose W contains z² and has any base point [a]∈A with full polar rank M(a)=2. Then no compatible ordered threefold exists, with any factor images. A transverse common zero of the two restricted conics is a sufficient special case, but is not necessary.

Thus, after the earlier generic-rank≤2 and common-radical exclusions, a plane factor image is possible only in the following unexcluded branch:

    W=span{z², Q₁+zℓ₁+c₁z², Q₂+zℓ₂+c₂z²},

where Q₁,Q₂ are independent quadrics on F and at every common zero [a]∈P(F) the full covectors B₁(a,−),B₂(a,−) on E are dependent. Equivalently, the full polar rank is at most one at every net base point. This is stronger than requiring dependence only after restriction to F. It is a necessary condition, not an existence assertion.

## 1. Dependencies and factor-image reduction

We use the universal finite-partner-plane theorem in /research/hm/universal-polar/rank-three-compatible-fiber-structure/PROOF.md, Sections 1–2: no compatible ordered threefold can have a point or curve factor image. This theorem is independent of dim K and requires only square avoidance.

We also use the square-avoiding six-space theorem in /research/hm/universal-polar/rank-four-compatible-fiber-bound/PROOF.md, and the common-radical, generic-polar-rank-three exclusion in /research/hm/incidence-foundations/rank-three-common-radical-exclusion/PROOF.md. Restrictions of v retain square avoidance. No restricted subspace is claimed to remain a full residual kernel.

If a factor image is the plane A, the corresponding general fiber has dimension one. All partners lie in P(ker M(a)), so A⊂D. Conversely, the presence of a plane in D alone does not imply that any compatible threefold has that plane as a factor image.

## 2. Three independent restrictions force a common radical

Put Q_i=q_i|F. Their gradients have generic rank at most two because the full rows of M have rank at most two on F. The elementary low-polar-rank classification gives

    span(Q₀,Q₁,Q₂)=span{x²,xy,y²}

for independent x,y∈F*. This classification works on a three-dimensional vector space just as in /research/hm/middle-surface/polar-rank-two-net-exclusion/PROOF.md, Section 1. For completeness: the projective map [Q₀:Q₁:Q₂] has an integral nondegenerate curve image; a common factor of the three independent quadrics would instead make the map dominant onto P². A general line in P(F) avoids their finite base locus and maps onto that curve with degree formula 2=δ deg C. Hence C is a conic; its equation gives Q₀Q₂=Q₁² after changing basis, and unique factorization gives the displayed binary net.

Extend x,y to coordinates x,y,t on F and then x,y,t,z on E. Write

    q₀=x²+zL₀+c₀z²,
    q₁=xy+zL₁+c₁z²,
    q₂=y²+zL₂+c₂z²,

where L_i are linear in x,y,t. On F, the first three columns of the Jacobian have left relation (y²,−2xy,x²). Full rank at most two forces the transverse column to satisfy

    y²L₀−2xyL₁+x²L₂=0.

Comparing the coefficients of all degree-three monomials yields

    L₀=2αx,   L₁=αy+βx,   L₂=2βy.

In particular there are no t terms. Every q_i depends only on x,y,z, and the vector dual to t is a nonzero common radical vector. The earlier common-radical theorem excludes compatible threefolds for the whole net in this branch.

## 3. Two independent restrictions force the normal square

Choose q₁,q₂ with independent restrictions Q₁,Q₂, and a nonzero q₃ in the restriction kernel. Write q₃=zL+cz², with L∈F*.

The gradients dQ₁,dQ₂ are independent at a general point of F. Indeed, if dependent over C(F), Euler contraction gives dQ₂=(Q₂/Q₁)dQ₁ wherever Q₁≠0, whence d(Q₂/Q₁)=0. In characteristic zero the ratio would be constant, contrary to independence.

On F the gradient row of q₃ is L dz. If L≠0, the three full gradient rows are independent at a general point where L≠0 and dQ₁,dQ₂ are independent. This contradicts A⊂D. Thus L=0, and q₃ is a nonzero scalar multiple of z².

## 4. Zero-dimensional restriction: ternary six-space exclusion

If r=0, write W=zL for a three-dimensional subspace L⊂E*. At a general a∈F, some ℓ∈L has ℓ(a)≠0, since L cannot be contained in the one-dimensional space Cz. The equations B(a,b)=0 then force z(b)=0. All other equations vanish once both a,b belong to F. Thus ker M(a)=F generically on A.

If Z has first image A, its dense open lies in A×A, and hence so does Z. All its products lie in K₀=Sym²F⊂K, of dimension six. The restriction v|K₀ is square-avoiding, and multiplication of ordered pairs is finite. A compatible ordered threefold would therefore contradict the cited K6 theorem. The same argument applies to a second image A.

## 5. One-dimensional restriction: ternary polar-incidence exclusion

Choose a basis

    q₁=zℓ₁,   q₂=zℓ₂,   q₃=Q+zℓ₃,

where ℓ₁,ℓ₂ are independent linear forms on E and Q is a nonzero quadric on F, extended to E. Since ℓ₁,ℓ₂ cannot both restrict to zero on F, at a general a∈F one of their values is nonzero. The first two polar equations force z(b)=0; the last then says B_Q(a,b)=0. In particular M has generic rank two on A, and its partner line is contained in A.

Suppose Z has first image A. Then Z⊂A×A and, with I_Q denoting the ternary polar incidence,

    Z⊂I_Q={([a],[b])∈P(F)×P(F): B_Q(a,b)=0}.

If Q has rank one, write Q=l². For general a∈A, l(a)≠0 and all partners lie in the fixed line P(ker l)⊂A. The second image of Z is then at most a curve, contrary to the universal factor-image bound.

If Q has rank at least two, the bilinear polynomial B_Q(a,b) is irreducible. A factorization of a bidegree-(1,1) polynomial must be a product of a linear form in a with a linear form in b, which would give matrix rank one. Consequently I_Q is integral of dimension three, and Z=I_Q.

Choose a smooth projective zero [a] of Q. Such a zero exists for every ternary quadric of rank at least two over C. Then B_Q(a,−)≠0. The incidence I_Q is smooth at (a,a), with tangent pairs ξ,η∈F/Ca satisfying

    B_Q(a,ξ+η)=0.

For every ξ∈F/Ca the pair (ξ,−ξ) is such a tangent pair. Differentiate the compatibility identity on I_Q at (a,a), using local representatives. Terms differentiating v vanish because a∧a=0, and the remaining identity is

    v(a²)∧a∧(η−ξ)=0.

Thus v(a²)∧a∧ξ=0 for every ξ∈F/Ca. This quotient has dimension two, so v(a²)∈Ca: the intersection of the two distinct planes span(a,ξ₁) and span(a,ξ₂) is Ca. Since Q(a)=0 and a∈F, a²∈K. Square avoidance is contradicted.

This proves the exclusion without projecting v into F or assuming it preserves F. Alternatively, all products lie in the ternary five-space ker(Q:Sym²F→C), and the earlier K4 hyperplane-slice theorem gives the same contradiction.

## 6. A rank-two base point excludes the whole square-containing net

Suppose

    W=span{z²,q₁,q₂},   Q_i=q_i|F,

and there is [a]∈P(F) with Q₁(a)=Q₂(a)=0 and full polar rank M(a)=2. Thus the full covectors B₁(a,−),B₂(a,−) on E are independent; their restrictions to F need not be independent. Since z(a)=0, these are exactly the two possibly nonzero rows of M(a).

For any product xy∈K, the equation from z² is z(x)z(y)=0. Thus the entire product incidence is contained in

    (A×P(E)) ∪ (P(E)×A).

An integral compatible ordered threefold is contained in one of these closed subsets. After exchanging factors, its first image is contained in A. The universal point/curve-factor exclusion forces that image to equal A.

Let U⊂A be the open rank-two locus of M, which contains [a]. The partner incidence over U is the projectivization of its rank-two kernel vector bundle. It is a smooth irreducible P¹-bundle J→U, of dimension three. Since Z dominates A with one-dimensional fibers, Z restricts to all of J; more explicitly, its intersection with J is a closed subset with full general P¹ fiber, hence is dense and equals J. The compatibility identity therefore holds identically on J, in particular near (a,a).

The tangent space of J at (a,a) consists of pairs

    ξ∈F/Ca,   η∈E/Ca,   M(a)(ξ+η)=0.

This follows directly by differentiating B_i(x,y)=0 for i=1,2, using symmetry. The z² equation is identically zero on A×P(E), so supplies no additional tangent equation. In particular, for every ξ∈F/Ca the tangent pair (ξ,−ξ) belongs to T_(a,a)J. Smoothness of J is important: compatibility holds on this entire local threefold, rather than only on a possibly smaller branch.

Differentiating the compatibility identity as in Section 5 yields

    v(a²)∧a∧(η−ξ)=0.

Apply this to (ξ,−ξ). Since characteristic is zero,

    v(a²)∧a∧ξ=0   for every ξ∈F/Ca.

Choose two independent such directions ξ₁,ξ₂. Then

    v(a²)∈span(a,ξ₁)∩span(a,ξ₂)=Ca.

All three q_i vanish at a, so a²∈K, contradicting square avoidance. No assertion that v(a²) lies in F was needed beforehand, and it is unnecessary for the tangent differences to span all of E/Ca.

Consequently every net base point must have full polar rank at most one in any still-unexcluded square-containing case. All base points lie in A because z² belongs to W.

**Restricted transverse-conic corollary.** If Q₁,Q₂ have a transverse common zero [a] on P(F), then their polar covectors restricted to F are independent and hence the full polar rank at a is two. The theorem applies. The converse need not hold: the transverse z-components of the full rows can make them independent even when the restricted conics are not transverse. In the normal form of the Results section, those transverse gradient entries are ℓ₁(a),ℓ₂(a), so they must be included in checking the remaining condition.

This is genuinely stronger than the earlier transverse full-net basepoint criterion in this branch: at every basepoint of a net containing z², z=0 and d(z²)=0, so full-net polar rank is never three. The present proof uses the smooth partner P¹-bundle over A instead of the rank-three graph over P(E).

## 7. Exact remaining frontier

Combining this result with /research/hm/incidence-foundations/rank-three-common-radical-exclusion/REMAINING_SURFACE_DEGREES.md, any compatible ordered threefold must satisfy all earlier conditions: generic polar rank three, zero common radical, neither factor image a point or curve, and total divisorial polar rank-drop degree at most two. Its possible factor-image dimensions remain (2,2), (2,3), (3,2), (3,3).

For any factor image that is a plane A, its restriction dimension must now be exactly two. The net must contain the square of an equation of A, and every net base point must have full polar rank at most one. In particular the two restricted conics have no transverse common zero anywhere on A, but that latter condition alone is insufficient. In that square-containing case at least one factor is in A for every ordered product; there can be no (3,3) compatible component.

The possible restricted-conic configurations include common-component pencils and coprime pencils whose complete intersection is nonreduced at every support point. Each still has to satisfy the stronger full-polar-rank-at-most-one condition, including the transverse derivatives of q₁,q₂, at every common zero. A common-component pencil is not automatically unexcluded; even restricted nontransversality at every common zero is not enough to retain it.

Integral-quadric factor surfaces are not treated here. Nor are (3,3) components of nets without squares for which every full-net basepoint is Jacobian-degenerate. A plane lying in D with restriction dimension≤1 has been excluded as a factor image; its mere presence does not by this proof exclude a different factor surface or dominant-factor component. No existence claim is made for any remaining branch, and there is no universal K7 dimension-two theorem yet.

All statements concern reduced dimensions, not scheme multiplicities.
