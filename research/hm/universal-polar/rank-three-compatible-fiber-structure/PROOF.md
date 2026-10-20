# Scope and later implications

The universal lemmas below remain valid. Intermediate unresolved-case descriptions are historical: the universal K7 and K8 bounds are supplied by diagonal-hartogs-fiber-bound/PROOF.md and UNSQUARED_PENCIL.md. For any actual canonical operation satisfying a later global rank-at-least-five theorem, residual-rank-one through four loci are empty; these are not simultaneous live canonical alternatives. Conditional global dimension implications retain their separately stated hypotheses.

# Seven-dimensional kernels: finite partner planes and a generic two-dimensional fiber bound

Work over C. Let dim E=4, K⊂Sym²E, and v:K→E be linear. Assume square avoidance: v(a²)∉Ca for every nonzero a with a²∈K. Compatibility of independent a,b means ab∈K and v(ab)∈span(a,b). All dimensions below concern reduced supports. No restricted subspace is asserted to remain an entire residual kernel.

## 1. Universal finiteness of compatible partner planes

There are only finitely many pairs ([a],U), with dim U=3, such that aU⊂K and every independent pair (a,b), b∈U, is compatible. This assertion holds for every dim K.

Indeed let H be their parameter scheme in P(E)×Gr(3,E)=P(E)×P(E*). It is closed: aU⊂K is a bundle-map vanishing condition, and compatibility is the coefficientwise polynomial identity

    v(ab)∧a∧b=0 for all b∈U.

The incidence divisor D={([a],U):a∈U} has line bundle O(1,1), which is ample. H is disjoint from D. To see this, if a∈U choose b,c∈U independent modulo Ca. For t≠0, compatibility along a(a+tb) implies v(a(a+tb))∈span(a,b). Taking t→0 gives v(a²)∈span(a,b); the analogous c path gives v(a²)∈Ca, a contradiction.

If H had positive dimension, it would contain a projective integral curve Γ. The incidence section of O(1,1)|Γ would be nowhere zero, making this line bundle trivial. But its degree is positive by ampleness. Thus H has dimension zero and finite reduced support. This proof includes all limiting parameter pairs automatically; there is no monodromy or generic-plane extension gap.

Equivalently, the complementary-pair open set outside D is affine: ([a],U) corresponds to the rank-one projector onto Ca along U. A projective subvariety of this affine variety is finite.

## 2. Universal consequence for factor projections

For completeness, the fixed-first-factor compatible locus has dimension at most two, and each surface component is a plane P(U) recorded by H. Here is the pointwise argument, independent of dim K.

Put M_a={b:ab∈K}. If dim M_a≤3, a surface fills P(M_a), so it is a plane. If M_a=E, let π:E→E/Ca and T(b)=v(ab) mod Ca. Away from [a], compatibility is T(b)=λπ(b) for a unique λ. The pencil T−λπ has rank three for generic λ, giving a family of projective points of dimension at most one. Only finitely many λ are exceptional. Its rank never vanishes, since that would make v(a²)∈Ca. Its exceptional kernels have projective dimension at most two. Every surface component is consequently a plane. Such a plane avoids [a] by Section 1.

It follows that outside a finite set of first factors every compatible fiber has dimension at most one. Therefore an integral compatible ordered threefold cannot have a point or curve as either factor image. Its possible factor-image dimension pairs are

    (2,2), (2,3), (3,2), (3,3).

This improves the K7 frontier beyond the numerical hyperplane-slice bound: every point/curve-factor threefold is excluded for all K and all square-avoiding v.

## 3. A transverse square excludes a dominant factor image

Now suppose dim K=7 and put W=K⊥⊂Sym²E*, dim W=3. Choose a basis of symmetric bilinear forms B1,B2,B3 and define

    M(x):E→C³,   y↦(B1(x,y),B2(x,y),B3(x,y)).

The square locus is the base scheme B={ [x]:Bi(x,x)=0 for all i }. Suppose it has a point [a] with rank M(a)=3. Equivalently, the three base quadrics intersect transversely there.

Claim: no compatible ordered component dominates P(E) under either projection.

Near [a], M(x) has rank three and its kernel defines a regular map φ to P(E). At a, ker M(a)=Ca, hence φ(a)=a. Any component dominating the first factor has, on this rank-three open, its partner necessarily equal to φ(x). Its dense compatibility therefore gives the polynomial wedge identity

    v(xφ(x))∧x∧φ(x)=0

throughout this neighborhood (using local representatives). Differentiating M(x)φ(x)=0 at x=a and using symmetry gives

    M(a)(dφ_a(h)+h)=0.

On tangent spaces E/Ca this says dφ_a=−Id. Differentiate the wedge identity at a. The derivative of v contributes zero because a∧a=0; the remaining terms give

    v(a²)∧a∧(dφ_a(h)−h)=−2v(a²)∧a∧h=0

for every h∈E/Ca. Thus v(a²)∈Ca, contrary to square avoidance. The other projection is identical by symmetry.

Consequently a hypothetical compatible threefold with a three-dimensional factor image requires *every* base point of W to be Jacobian-degenerate. This is a necessary condition, not an assertion that degenerate nets admit compatible threefolds.

## 4. Surface images force a large polar rank-drop locus

Let D_W={ [x]:rank M(x)≤2 }. If an ordered threefold has a surface factor image A, its general fiber over A has dimension one. Since all partners belong to P(ker M(x)), rank M(x)≤2 for general x∈A. Hence A⊂D_W and dim D_W≥2.

Combining Sections 2–4, if W has a transverse base point and dim D_W≤1, no compatible threefold exists.

A useful checkable sufficient condition for dim D_W≤1 is:

1. W contains a nonsingular quadric;
2. every nonzero quadric in W has rank at least three.

Indeed the singular members form a plane quartic Δ⊂P(W). Each has rank exactly three and a unique kernel point. Every x∈D_W is the kernel point of some singular member: a nonzero linear relation among the rows of M(x) gives precisely that singular form. Thus D_W is the image of Δ under its regular kernel map, and dim D_W≤1.

## 5. New generic K7 theorem, and its exact limitations

For an arbitrary seven-space K, the six-space theorem in ../rank-four-compatible-fiber-bound/PROOF.md applied to a general hyperplane gives compatible projective dimension at most three. This uses only its pointwise square-avoidance statement. A component of dimension at least four would cut to a compatible threefold in a six-space, contradiction.

The preceding new results improve that bound to two whenever W has a transverse base point and dim D_W≤1. In particular:

**For a general seven-dimensional subspace K⊂Sym²E and any square-avoiding linear v:K→E, the compatible rank-two locus has projective dimension at most two.**

The stated conditions hold for a general net W. Three general quadrics have a transverse complete intersection of eight base points. The rank-at-most-two symmetric quadrics form a codimension-three subvariety of P(Sym²E*)=P9, so a general projective plane P(W) misses it. A general net also contains nonsingular quadrics. Section 4 then applies.

More precisely, any exceptional K7 admitting a compatible threefold must satisfy at least one of:

- every base point of its net is Jacobian-degenerate (needed whenever a factor image is three-dimensional);
- the polar rank-drop locus D_W contains a surface (needed whenever a factor image is two-dimensional).

If a transverse base point exists, every hypothetical threefold must have factor dimensions (2,2), with both factor surfaces contained in D_W. If dim D_W≤1, every hypothetical threefold must have factor dimensions (3,3), and every base point must be Jacobian-degenerate.

“General K” is a Grassmannian-generic assertion. It does not say that the kernel at a generic middle of a particular operation is Grassmannian-general. Thus no universal improvement from three to two is claimed for all residual-rank-three kernels, and no moving-middle or global dimension conclusion is imported without its separate hypotheses.

## Audit and scope

The finite-plane lemma is independent of the K5/K6 classification and strengthens their curve-plane exclusions. The transverse-square argument uses only differentiation of two explicit polynomial identities. The only numerical-bound dependency is the established pointwise K6 theorem. All work is abstract linear algebra and projective geometry. No identification with an actual source operation is asserted.
