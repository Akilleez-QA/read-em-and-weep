# Independent audit: common-radical K7 exclusion

## Verdict

PASS, 2026-10-19. Independently checked PROOF.md, Sections 1–5, against the precise fixed-factor lemma and K6 theorem cited there. No missing case or repair was found. Under exactly the stated hypotheses, the compatible rank-two locus has dimension at most two.

The result requires a common radical line and generic polar evaluation rank three. It does not classify generic polar rank at most two or nets without a common radical. All dimensions are dimensions of reduced supports; nothing here asserts reduced scheme structure or bounds tangent spaces.

## 1. Hypotheses and reduction to ordered threefolds

The hypotheses are: complex vector space E of dimension four; K a seven-dimensional subspace of Sym²E; linear v:K→E satisfying v(a²)∉Ca whenever a≠0 and a²∈K; the three-dimensional annihilator W=K⊥ has a common radical line Ce; the evaluation map y↦(B_i(a,y)) has generic rank three.

Since the forms vanish on e, they descend to independent symmetric forms on V=E/Ce, of dimension three. Their evaluation matrix N(x) is generically invertible. A nonzero common radical in V would lie in the kernel of every N(x), which is impossible. By symmetry, N(x)=0 for x≠0 would itself give a common radical vector x, so the only rank-zero point upstairs is [e]. The common radical upstairs is therefore exactly Ce, even though the statement only requires it to contain Ce.

The multiplication map P(E)×P(E)→P(Sym²E) is proper and has finite fibers, since a nonzero quadratic product has only finitely many ordered factorizations. It is therefore finite onto its image. A compatible locus of dimension at least three supplies an integral three-dimensional subvariety meeting its rank-two open densely, and its ordered inverse image has an integral component of the same dimension. Taking its projective closure does not increase dimension.

On independent pairs, the conditions ab∈K and v(ab)∧a∧b=0 are exactly compatibility and are polynomial. Their validity extends to the closure. The wedge equation alone on the diagonal is not square compatibility; the proof never makes that inference.

The universal finite-partner-plane lemma excludes point and curve factor images. A dominant projection meets the rank-three open, where its sole partner is e. Its dense ordered graph, hence its closure, has constant second factor e. The universal fixed-factor bound two contradicts dimension three. This handles both projections and leaves precisely surface images.

## 2. Surface images of generic polar rank two

The determinant det N is a nonzero homogeneous cubic on V. Its pullback defines a hypersurface in P(E), with every irreducible reduced component a cone through [e]. This remains true for repeated factors: irreducible factors in the three quotient coordinates stay irreducible after adjoining the vertex coordinate. An integral surface contained in that hypersurface equals one reduced component, so it contains [e].

Over a general rank-two point of the factor surface A, the projective partner kernel is a line containing e. The fiber of the proper ordered threefold has dimension one. Its support, being a closed one-dimensional subset of this projective line, is the whole line. This does not require generic fibers to be irreducible or reduced. In particular (a,e) lies in the ordered closure and satisfies the compatibility identity.

Since a≠e on a dense open of A, these are genuinely rank-two compatible products. Closedness gives the fixed-e wedge identity on all A. The fixed-factor classification says every surface component of that closed support is a plane avoiding its fixed factor. The possible extra diagonal point contributes no surface. Since A is integral of dimension two and the fixed-factor locus has dimension at most two, A is such a plane. Its avoidance of e contradicts the cone property.

## 3. Rank-one curves downstairs

Because det N≠0, at least one 2×2 minor is a nonzero quadratic. If an integral curve C⊂P(V)=P² is contained in the rank-at-most-one locus, its irreducible plane equation divides every minor. Its degree is therefore at most two.

For an irreducible conic q, adj(N)=qC0 with C0 constant. Generic invertibility of N forces C0 invertible. The identity N adj(N)=det(N)I implies N C0=ℓI for a nonzero linear form ℓ: the diagonal polynomial identities give q|det(N), and off-diagonal entries vanish. Thus N=ℓC0⁻¹. Symmetry of each row-form B_i(x,y)=ℓ(x)r_i(y) implies r_i is proportional to ℓ. This contradicts invertibility of C0⁻¹. Hence each integral curve in the rank-one locus is a line. No smoothness assumption beyond irreducibility of a complex plane conic is needed; degree-one reduced components also cover nonreduced rank-drop equations.

## 4. Rank-one pencils and the kernel equality

For a line P(U) in this locus, U has dimension two and N|U is injective, because N(u)=0 has no nonzero solution. Thus N(U) is a genuinely two-dimensional pencil of nonzero rank-one maps. The elementary classification into common image or common kernel applies: for r⊗α and s⊗β, independence of both image vectors and covectors would make their sum rank two.

A common image line would leave a two-dimensional annihilator subspace of W whose symmetric forms vanish on U×V. Such forms descend to V/U, whose symmetric-square dual has dimension one. This contradicts independence of W. Therefore the pencil has a common two-dimensional kernel H.

If H≠U, their intersection contains a nonzero t. Membership t∈U gives H⊂ker N(t). Membership t∈H gives B_i(u,t)=0 for every u∈U; symmetry then gives U⊂ker N(t). Since H+U=V, this makes N(t)=0, impossible. Hence H=U, and every nonzero u∈U has exactly this kernel. In particular all forms vanish on U×U.

## 5. Rank-one surfaces and legitimate K6 restriction

The projection of A away from e lies in the rank-one locus in P(V). It cannot have point image, since the closure of a projection fiber is only a line. It cannot have surface image, since the rank-one locus is contained in the proper determinant cubic. Its image closure is therefore an integral curve C. The inverse cone over C has dimension two and contains A, forcing equality. The preceding argument makes C a line, so A=P(F), where F is the three-dimensional inverse image of U.

Common radical vanishing and B_i(U,U)=0 imply Sym²F⊂K, a six-dimensional subspace. For every a∈P(F) except e, the full kernel upstairs is exactly F. The dense portion of the ordered threefold above these points lies in P(F)×P(F); this product is closed, so it contains the entire threefold. Finite multiplication preserves its dimension and its dense rank-two open.

The cited K6 theorem in /research/hm/universal-polar/rank-four-compatible-fiber-bound/PROOF.md explicitly assumes only a six-dimensional symmetric-tensor subspace and square avoidance for a map to the ambient four-space. Its ternary-support case is precisely K0=Sym²F and permits v(K0) to have a component normal to F. Restriction of v preserves square avoidance. No projection of v to F, full residual-kernel hypothesis, or generic-middle claim is needed. The theorem therefore directly excludes the resulting compatible rank-two threefold.

This audit verified the dependency's exact statement and its ternary-support reduction, including the codomain condition of /research/hm/normalizer-rank-five/rank-six-cubic-web/REDUCIBLE.md. It does not claim to re-audit the entire earlier classification chain.

## Scope

All possible dimensions of either factor image and all possible generic polar ranks on a surface image have been covered. Closure arguments use proper projective projections and reduced component supports, so neither exceptional fibers, geometric-fiber monodromy, determinant multiplicities, nor diagonal points create an omitted case. No universal K7 conclusion beyond the specified common-radical generic-rank-three branch follows.

## 6. Integrated divisorial corollary

PASS. Combining the low-polar-rank exclusion with the common-radical exclusion, a K7 compatible threefold can remain only when the 3×4 polar matrix M has generic rank three and the net has zero common radical. The following further reduction is valid independently of the details of the low-rank proof once those two exclusions are granted.

Let Δ be the vector of signed maximal minors of M, with the alternating signs chosen so that MΔ=0. At least one minor is nonzero, and every nonzero entry is homogeneous of degree three. Let g be their homogeneous greatest common divisor, ignoring zero entries. Then 0≤deg g≤3. If deg g=3, Δ=ge for a nonzero constant vector e∈E. The polynomial identity MΔ=0 and the integral-domain property imply M(a)e=0 identically. Thus B_i(a,e)=0 for every a and i, making e a common radical vector (symmetry identifies either argument convention). This is excluded, so deg g≤2.

For the determinantal scheme D_W defined by the maximal minors, each reduced surface component in P³ is a hypersurface V(p) for an irreducible homogeneous polynomial p. All maximal minors vanish on it, so p divides every minor and therefore divides g. Conversely each irreducible factor of g defines a surface in D_W. At the generic point of V(p), the local ring is a discrete valuation ring and the ideal of minors is generated by p raised to the minimum of their valuations. This minimum is exactly the exponent of p in g. Accordingly the total degree of the divisorial part, with these generic scheme multiplicities, is deg g≤2. Embedded or lower-dimensional pieces of D_W do not affect this assertion.

Any surface factor image of an ordered compatible threefold lies in D_W, by the partner-fiber dimension argument, and equals one of its reduced surface components. It must consequently be a plane or an integral quadric. The possibilities for the divisorial support include one plane, two planes, or an integral quadric; the degree-two budget also allows a doubled plane. This is a necessary geometric restriction, not an exclusion of these possibilities.

The corollary does not dispose of a threefold with both factor images equal to P³. Such a component still requires every base point to be Jacobian-degenerate by the separate transverse-basepoint lemma. In particular, when D_W has no surface, the (3,3) all-base-points-degenerate branch remains open. No conclusion about scheme reducedness or global moving-middle dimension is added.
