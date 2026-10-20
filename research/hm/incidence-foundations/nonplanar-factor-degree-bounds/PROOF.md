# Coincident quadric factor images

Work over C. Let dim E=4 and let K ⊂ Sym²E have dimension five and full support. Let X ⊂ P(E)×P(E) be an integral ordered-factor surface, with ab∈K throughout X, generically of rank two. Assume both factor images A,B are nonplanar integral surfaces.

Let Q₁,…,Q₅ be a basis of K⊥ and M(a) the 5×4 matrix with rows Qᵢ(a,−). Its vector kernel is M_a={b:ab∈K}. Symmetry gives b∈M_a iff a∈M_b.

We use the pure-K nonlinear-curve exclusion in `/research/hm/incidence-foundations/nonlinear-curve-factor-exclusion/PROOF.md` and the plane/nonplanar exclusion in `/research/hm/incidence-foundations/one-planar-factor-exclusion/PROOF.md`.

## Theorem

The ambient generic rank of M is four. Both projections of X are birational. The two factor images coincide, A=B, and their common image is an integral quadric surface.

## 1. Kernel rulings and birationality

There is no nonlinear integral curve C such that dim M_a≥2 at general a∈C. Otherwise, on a dense open of C choose a rational rank-two subbundle of the kernel bundle and projectivize. Its closure is an integral ordered-factor surface with first image C. Multiplication has finite fibers (a quadratic has at most two ordered factorizations), so its product image is a surface, generically rank two. The chosen surface is an ordered-factor component above that image, contradicting nonlinear-curve exclusion.

Consequently dim M_a=1 generically on each of A,B: otherwise choose a nonlinear curve through the corresponding good open. Such a curve exists by a general sufficiently ample section. The unique kernel line makes each projection of X birational. This argument is independent of ambient rank four.

The same observation rules out ambient generic rank at most two, by choosing any nonlinear curve meeting the generic ambient open.

## 2. Ambient rank three: image dimension at most two

Suppose ambient generic rank is three. Its kernel line defines f:P³⇢P³. Write D for its image closure. The graph has dimension three. For general b∈D its inverse fiber is contained in P(M_b), by symmetry, whence dim M_b≥4−dim D.

If dim D=2, a nonlinear curve in D contradicts Section 1. If dim D=1, Section 1 forces D to be a line P(L), dim L=2.

In this line case, generic dim M_b≥3. Equality holds: if dim M_b=4, then bE⊂K and uniqueness of the ambient generic kernel would make f constant. For distinct general b,c∈P(L), the spaces bM_b,cM_c have dimension three and intersect in at most Cbc. Since dim K=5, their intersection is exactly Cbc and their sum is K. Hence c∈M_b. Varying c shows L⊂M_b. Thus Sym²L⊂K⊂LE.

Choose E=L⊕V. The quotient H=K/Sym²L is a two-dimensional subspace of L⊗V containing b⊗v_b for all general b∈P(L). Its projective pencil contains infinitely many rank-one tensors, so its 2×2 determinant vanishes identically. Choose two such tensors with independent first factors. Their second factors must be proportional, since otherwise their sum has rank two. Thus H=L⊗Cv for one v∈V, and K=Sym²L+Lv is supported on L+Cv, contrary to full support.

If D is the point [e], then eE⊂K, so K=eE+Cq with q∉eE. Modulo e, K has image Cq̄ in Sym²(E/Ce), with q̄≠0. For any product ab with neither factor e, π(a)π(b) is a nonzero multiple of q̄. If q̄ has rank three there are no such products. Otherwise its factors are fixed up to the finite ordered interchange, and a,b each lie on one of at most two fixed projective lines through e. Products with a factor e have a point factor image. No integral ordered-factor surface can therefore have both factor images surfaces. This excludes the constant case for X, without claiming it impossible for arbitrary full-support K.

## 3. Ambient rank three: dominant image

The remaining case is that f is dominant. Symmetry and uniqueness of the generic kernel give f(f(a))=a, so f is a birational involution.

For a general plane U⊂P³, the graph over U is an integral surface and its second image is a surface: intersect U with the dense isomorphism open of f. The plane/nonplanar theorem forces that image to be a plane.

Here is the precise degree-one argument. The assignment U↦closure(f(U)) is rational on the dual P³: its coefficients are obtained from the unique linear dependence among the homogeneous coordinates of f restricted to U. It is generically injective, since on the isomorphism open equal image planes have equal strict inverse transforms. Thus the dual assignment is dominant. The strict inverse transform of a general target plane is consequently a plane.

Write f=[F₀:F₁:F₂:F₃] with homogeneous coordinates of degree d and no common factor. A general target plane pulls back to a degree-d linear combination of these polynomials. Its zero divisor has no extra exceptional component: there are only finitely many exceptional divisors, all in the complement of the isomorphism open, and a general target plane contains none of their images. The base locus has codimension at least two, so contributes no fixed divisor. The strict inverse transform has multiplicity one because f is an isomorphism at its generic point. Therefore that degree-d equation defines a reduced plane, and d=1.

We have f([a])=[Ta] for invertible T. Hence a(Ta)∈K for every a. Their span is the image of the operator I⊗T+T⊗I on Sym²E. Triangularize T with nonzero eigenvalues λ₁,…,λ₄. This operator has diagonal entries λᵢ+λⱼ for i≤j. The four entries 2λᵢ are nonzero. At most four of the six off-diagonal entries vanish: zero-sum pairs form disjoint complete bipartite graphs between eigenvalues λ and −λ, on four vertices in total. Thus at least six diagonal entries are nonzero, and the span has dimension at least six. This contradicts dim K=5.

Sections 1–3 prove ambient generic rank four.

## 4. The maximal-minor gcd sharpens degree four to degree two

Let Δ₁,…,Δ₅ be the signed 4×4 maximal minors of M. At least one is nonzero; all are homogeneous quartics, with zero entries allowed. Let g be their homogeneous gcd over the nonzero entries. The cofactor identity gives

    (Δ₁,…,Δ₅) M = 0.

If deg g=4, division by g gives a nonzero constant vector c with cM=0. This means ΣcᵢQᵢ(a,−)=0 identically, contrary to independence of the basis Qᵢ.

Nor can deg g=3. The divided vector would give a nonzero homogeneous-linear syzygy Σlᵢ(a)Qᵢ(a,−)=0. Put qᵢ(a)=Qᵢ(a,a), so ∇qᵢ=2Qᵢ(a,−). Dotting the gradient syzygy with a gives Σlᵢqᵢ=0. Differentiating this identity and subtracting the original gradient syzygy gives Σqᵢ∇lᵢ=0. The qᵢ are linearly independent quadrics, so every constant coefficient of every ∇lᵢ vanishes. Homogeneous linear lᵢ must then all vanish, a contradiction. Thus deg g≤2.

Each irreducible factor image is a hypersurface in P³. Its irreducible equation divides all the Δᵢ, hence divides g. Thus deg A,deg B≤2. Nonplanarity makes each degree at least two, so both are quadrics. If they were distinct, their coprime equations would have product dividing g, giving 4≤deg g≤2, a contradiction. Hence A=B is an integral quadric, and g is a nonzero scalar multiple of its equation.

## 5. The common quadric carries a nonidentity birational involution

Write Q=A=B. The birational first projection identifies X with the closure of the graph of a rational self-map τ:Q⇢Q; the second projection makes τ birational. The swapped surface Xᵗ also lies in the ordered-factor incidence and dominates Q under its first projection. For general a∈Q, the kernel M_a is a single vector line by Section 1. Thus X and Xᵗ have the same unique second factor over general a, so Xᵗ=X. Equivalently, τ²=id as rational maps. Moreover τ is not the identity: that would put X in the diagonal and make its generic product a square of rank one, contrary to the rank-two hypothesis.

This involution conclusion is still purely a statement about K. It does not imply that τ is regular everywhere or extends to a projective-linear transformation of P(E).

There is a further consequence only when additional data are present. Suppose v:K→E is linear, v(ab)∈span(a,b) densely on the product family, and v(e²)∉Ce whenever 0≠e²∈K. Then the fixed-linear-correspondence exclusion in `/research/hm/incidence-foundations/nonplanar-linear-correspondence-exclusion/PROOF.md` applies if τ is the restriction of an ambient projectivity: write that projectivity as [T] with T invertible, and closure gives aT(a)∈K throughout Q. Its hypotheses are exactly dense compatibility and square avoidance as stated. It supplies a contradiction. Therefore, under these extra assumptions, τ cannot be the restriction of any ambient projective-linear automorphism.

The precise remaining case is consequently a genuinely nonlinear nonidentity birational involution of the same integral quadric, which may be smooth or a cone and whose rational map may have points of indeterminacy. This proof does not eliminate that case.

## Scope and provenance

The gcd and linear-syzygy refinements in Section 4 were independently checked. No compatibility or square avoidance is needed for this theorem. It reduces the both-nonplanar case to a common integral quadric surface; it does not classify or eliminate this case.
