# The everywhere polar-rank-at-most-two K7 branch is excluded

## Statement and scope

Work over C. Let E have dimension four, let K be a seven-dimensional subspace of Sym²E, and let W=K⊥ be its three-dimensional net of symmetric bilinear forms. For a basis B₀,B₁,B₂ of W write

    M(x)y=(B₀(x,y),B₁(x,y),B₂(x,y)).

Assume the generic rank of M(x) is at most two. Equivalently, every 3×3 minor is the zero polynomial; thus the entire P(E) is the polar rank-drop locus D_W.

Then there are independent linear forms ℓ,m∈E* such that

    W=span{ℓ²,ℓm,m²}=Sym²(span{ℓ,m}).

In particular, the generic polar rank is exactly two. Put R=ker ℓ∩ker m, a vector two-plane. For any linear map v:K→E satisfying square avoidance

    v(a²)∉Ca whenever a≠0 and a²∈K,

the ordered locus of independent compatible pairs

    C_v={([a],[b]): a,b independent, ab∈K,
                         v(ab)∈span(a,b)}

has dimension at most two. The compatible projective rank-two tensor locus consequently also has dimension at most two.

This is an exact classification and exclusion for generic polar rank at most two. It does not classify nets whose generic polar rank is three but whose proper polar rank-drop locus has a surface component. It makes no claim that any actual residual kernel is general or belongs to this branch.

## 1. Classification of the net

Let qᵢ(x)=Bᵢ(x,x). Consider the rational map

    f:P(E) ⇢ P²,   [x]↦[q₀(x):q₁(x):q₂(x)].

On the open set where q(x)≠0, its differential has rank rank M(x)−1. Indeed the affine differential is 2M(x), and its image contains q(x), by Euler's identity. Projectivizing quotients both the source radial direction and the target radial direction. In characteristic zero, the generic differential rank is the dimension of the image. Our assumption therefore makes the image dimension at most one. Independence of q₀,q₁,q₂ excludes a point image and excludes an image contained in a line. Its closure C⊂P² is thus an integral nondegenerate plane curve.

The qᵢ have no common nonconstant factor. A common quadratic factor would make them dependent. A common linear factor h would give qᵢ=hLᵢ for three independent linear forms Lᵢ. Then f agrees with the dominant linear projection [L₀:L₁:L₂] to P², contradicting the curve image. These are the only possible factor degrees.

Consequently the base locus has codimension at least two, and a general projective line L⊂P(E) misses it. The restriction f|L is nonconstant for a general L: constancy on general lines would imply that two general points have the same image, hence that f has point image. Thus f|L is a surjective morphism onto C, defined by three quadratic forms with no common zero, and

    (f|L)*O_C(1)=O_{P¹}(2).

If δ is the degree of this map onto C (or, equivalently, onto its normalization), the degree formula gives

    2=δ·deg C.

Nondegeneracy gives deg C≥2. Hence deg C=2 and δ=1. An integral plane conic over C is smooth. After changing the basis of W, its equation is z₀z₂=z₁², so the quadrics satisfy the polynomial identity

    q₀q₂=q₁².

We finish by unique factorization in C[E]. The polynomials q₀ and q₂ are relatively prime: any irreducible factor common to them also divides q₁, contradicting the absence of a common factor of the net. The identity then implies that q₀ and q₂ are each a nonzero constant times a square. Since each has degree two, they are squares of linear forms after rescaling over C. The same identity gives q₁ as their product up to sign. Thus

    q₀=ℓ²,   q₁=ℓm,   q₂=m²

after a further harmless choice of basis. Independence of the qᵢ implies independence of ℓ,m. Conversely, this binary net visibly has generic polar rank two, completing the classification.

## 2. The product locus has a factor in a fixed two-plane

Let p:E→E/R be the quotient. The displayed form of W says precisely

    K=ker(Sym²p:Sym²E→Sym²(E/R)).

Thus ab∈K if and only if p(a)p(b)=0 in Sym²(E/R). The symmetric algebra of E/R is a polynomial ring and has no zero divisors. Consequently

    ab∈K  ⇔  a∈R or b∈R.

In particular all square tensors in K are exactly the squares a² with a∈R. If E=A⊕R is any splitting, the normal form is

    K=(A R)⊕Sym²R.

The entire ordered product incidence lies in

    (P(R)×P(E)) ∪ (P(E)×P(R)).

## 3. Square avoidance bounds compatibility by two

We use the universal finite-partner-plane result proved in /research/hm/universal-polar/rank-three-compatible-fiber-structure/PROOF.md, Sections 1–2. In its precise form:

- Every fixed-first-factor compatible fiber has dimension at most two.
- Each surface component of such a fiber is a projective plane P(U), for a vector three-plane U.
- Only finitely many parameter pairs ([a],U) give such fully compatible planes. Thus outside a finite set of first factors every fiber has dimension at most one.

These statements apply to every K and require only the square-avoidance condition used here. To recall the key finiteness mechanism, the parameter locus of pairs ([a],U) satisfying aU⊂K and the coefficientwise identity v(ab)∧a∧b=0 for b∈U is projective. Square avoidance makes it disjoint from the ample incidence divisor a∈U in P(E)×Gr(3,E), so it has no projective curve and is finite. The fixed-factor pencil argument in the cited proof identifies every surface fiber with one of these planes.

Take any irreducible component Z of C_v. By Section 2 it is contained in one of the two displayed product subsets. Suppose first it is contained in P(R)×P(E). Its first-factor image has dimension zero or one. If zero, the universal fixed-fiber bound gives dim Z≤2. If one, its general first factor avoids the finite exceptional set, so the general fiber has dimension at most one. The fiber dimension theorem again gives dim Z≤1+1=2. The other subset is identical by exchanging factors. This proves dim C_v≤2.

The multiplication map ([a],[b])↦[ab] has finite fibers on independent pairs: a rank-two quadratic product has its two projective linear factors uniquely determined up to exchange. Its image is exactly the compatible rank-two tensor locus. The same bound therefore holds there.

## 4. Consequence for the exceptional K7 frontier

A hypothetical compatible threefold for a square-avoiding seven-space cannot occur when the generic polar rank is at most two. In the exceptional-net analysis, one may therefore restrict attention to generic polar rank three. Any surface-sized polar rank-drop obstruction that remains is a proper surface in P³, rather than the whole ambient P³.

This result neither removes the all-base-points-degenerate branch at generic polar rank three nor excludes proper surface components of D_W. Those are separate unresolved possibilities.

## Audit

The classification uses only the characteristic-zero generic differential-rank theorem, degree of a map from P¹ to a plane curve, and unique factorization. The compatible-dimension conclusion uses the previously established universal finite-partner-plane lemma, not a Grassmannian-general kernel assumption or any source-operation model. 

## Appendix: verification of the alternative gradient-syzygy proof

An independent algebraic route also works and uses the universal polarization lemma in ../quadratic-gradient-syzygy/PROOF.md, Section 1.

First, generic rank at most one is impossible. Choose nonzero q₀. Rank at most one makes dqᵢ proportional to dq₀ over the rational function field. Contracting with the Euler vector gives dqᵢ=(qᵢ/q₀)dq₀. Hence d(qᵢ/q₀)=0. In characteristic zero the only rational functions on E with zero differential are constants, contradicting independence.

Thus the generic rank is two. Choose two columns of the 3×4 Jacobian that are independent over C(E). Their cross product s is a nonzero vector of homogeneous quadratic polynomials. Since all four columns span a two-dimensional space over C(E), s is a left syzygy of the entire Jacobian; its polynomial dot products with all columns vanish identically. Divide by the homogeneous gcd of its entries. The resulting nonzero homogeneous polynomial vector r has a common entry degree d∈{0,1,2} and still satisfies

    Σ rᵢ dqᵢ=0.

Degree zero is impossible by independence of qᵢ. Degree one is also impossible: Euler contraction gives Σrᵢqᵢ=0; differentiation and subtraction of the syzygy give Σqᵢ drᵢ=0. Because drᵢ has constant coefficients and the qᵢ are independent, all drᵢ vanish, and homogeneous linear rᵢ are zero.

Therefore d=2. The universal polarization lemma gives r=Cq for a nonzero symmetric constant 3×3 matrix C and qᵗCq=0. The rank of C cannot be one or two: its quadratic form would factor over C, forcing a nonzero constant linear combination of the qᵢ to vanish in the polynomial domain. Thus rank C=3. A basis change gives q₀q₂=q₁². Unique factorization, equivalently the rank-three relation argument in the same cited proof, forces the full binary net. The compatibility argument in Sections 2–3 then applies unchanged.

This appendix validates all cases of the proposed syzygy route; it is independent of the general-line proof in Section 1 except for the shared elementary UFD conclusion.
