# Independent audit: distinct planar factor images

## Verdict and hypotheses

The algebraic argument in `PROOF.md` is correct over **C**. It excludes an irreducible ordered-factor surface whose two projections dominate distinct planes P(U), P(W), where dim E=4, dim U=dim W=3, and whose product span has vector dimension at most five, provided a linear map v on that span is densely compatible and satisfies square avoidance:

    v(e²) ∉ Ce for every nonzero e² in its domain.

The same irreducible surface must dominate both factors. Dominance of a reducible union is insufficient: P(U)×{[w₀]} ∪ {[u₀]}×P(W) is a counterexample to that weaker graph-classification statement. The contact criterion below applies to reduced varieties, or whenever the wedge identity holds scheme-theoretically.

## 1. Exact rank criterion and normalization

Put H=U∩W. For an isomorphism T:U→W define

    F(ab)=(aT(b)+bT(a))/2.

Here is an independent proof of its kernel criterion. Choose z∈U\H, so E=W⊕Cz. Write Q∈Sym²U as Q_H+zh+cz² with Q_H∈Sym²H and h∈H. The zW-component of F(Q) is

    z·T(h/2+cz).

Thus F(Q)=0 and injectivity of T imply h=c=0: every kernel element belongs to Sym²H.

Write T(h)=A(h)+ℓ(h)w using W=H⊕Cw. If ℓ≠0, vanishing of the Hw-component says that contraction of Q_H with ℓ is zero. Consequently Q_H belongs to Sym²(ker ℓ), so Q_H is a scalar multiple of k² for some nonzero k∈H. But F(k²)=kT(k)≠0. Hence a nonzero kernel requires T(H)=H.

Now A=T|H is invertible. On Sym²H, the determinant of F is

    det(F|Sym²H) = (det A)(tr A)/2.

Therefore F has a nonzero kernel exactly when tr A=0. In that case A has distinct nonzero eigenvalues λ, −λ, and its symmetric-square operator has eigenvalues λ, 0, −λ. The kernel is exactly one-dimensional and rank F=5.

Rescale T by λ⁻¹, choose eigenvectors x,y in H, choose z outside H, and set w=Tz. Then x,y,z,w are a basis, Tx=x, Ty=−y, Tz=w, and

    im F = <x², y², xz+xw, yw−yz, zw>.

These five generators are independent. Rescaling T does not change its projective graph or product span. This also independently verifies the trace-zero condition obtained from the symmetric inverse image of Λ²H in `PROOF.md`.

## 2. Dense compatibility and square contact

The polynomial identity v(aT(a))∧a∧T(a)=0 extends from a dense set to all a. At independent factors it is equivalent to compatibility. Thus the special curves used in the proof need not meet the originally specified dense open set.

Along a=x+sy, s≠0, compatibility and passage to s=0 give v(x²)∈<x,y>. Along a=x+tz, t≠0, the support plane is

    <x+(t/2)(z+w), z−w>,

whose limit is <x,z−w>. Hence v(x²) belongs to the intersection of these two limiting planes, namely Cx. This directly contradicts the stated square-avoidance hypothesis.

More generally, at a diagonal point with local lifts a=b=e, differentiating v(ab)∧a∧b=0 gives

    v(e²)∧e∧(db−da)(ξ)=0.

The derivative of v(ab) contributes zero because its other two wedge factors are both e. The class D(ξ)=(db−da)(ξ) modulo Ce is independent of the scalar lifts. If im D has dimension at least two, the displayed equations force v(e²)∈Ce. No smoothness assumption is needed when using the Zariski tangent space and a regular identity on a reduced variety. In the normal form, the y and z directions at x give −2y and w−z, which are independent modulo Cx.

## 3. Upgrade from distinct planar images to a linear graph

Multiplication U⊗W→Sym²E has kernel Λ²H of dimension one and image dimension eight. A product span of dimension at most five therefore gives at least three independent bilinear equations. Let M(a) be their q×3 matrix of linear forms, q≥3. Dominance over P(U) forces generic rank at most two.

Generic rank one is impossible. A linear space of matrices of rank at most one has either a fixed image line or a fixed row line. Indeed, two rank-one tensors with independent first and second factors have rank-two sum; comparison with a fixed nonzero tensor forces a common factor throughout the space. A fixed image line makes the q bilinear equations constant multiples of one equation. A fixed row line confines the generic second factor to a fixed projective line. These contradict, respectively, independence and second-projection dominance.

Choose two rows independent over C(P(U)), then a third independent of them over C. The resulting 3×3 matrix N has generic rank two, identically zero determinant, and three constant-linearly independent rows. Its nonzero adjugate has homogeneous quadratic entries and generic rank one.

The factorization

    adj(N)=h c rᵗ,   deg h+deg c+deg r=2,

with homogeneous primitive vectors c,r is valid over the polynomial UFD C[a₀,a₁,a₂]. To verify this, divide a nonzero column by the gcd of its entries. Every other column is a rational multiple of the resulting primitive vector c. A denominator would divide every entry of c, so these multiples are polynomials. Divide their vector by its common gcd h to obtain r. Homogeneity gives the degree formula.

The identities N adj(N)=adj(N)N=0 give Nc=0 and rᵗN=0. The right kernel c describes the generic graph. Its dominant second projection forces deg c≥1. If deg r=0, r gives a nonzero constant relation between the three chosen bilinear equations, a contradiction. Thus deg c=deg r=1 and h is constant. Dominance makes the linear map c:U→W invertible. Irreducibility and closure then identify the entire surface with its projective graph.

## 4. Coincident-plane extension

The additional argument in Section 5 of `PROOF.md` and in `COINCIDENT_PLANES.md` is valid under the extra hypotheses dim K=5 and full support E. For coincident factor plane P(U), the product span K′ lies in Sym²U and has dimension between three and five.

- Dimension five forces K′=K and contradicts full support.
- Dimension four is excluded by the abstract theorem in `/research/hm/normalizer-rank-five/rank-six-cubic-web/REDUCIBLE.md`. Its statement genuinely allows an arbitrary linear map K′→E, not only a residual-kernel map or a map taking values in U. Restriction of v preserves compatibility and square avoidance. The irreducible-cubic proof uses adjugate divisibility and a Veronese intersection; the reducible cases reduce to compatible planes or quadrics with a forced compatible square. The application imports none of the additional residual-kernel hypotheses.
- In dimension three, closure and density force every member of K′ to have rank at most two. The classification in `/research/hm/normalizer-rank-five/extremal-kernel-planes/PROOF.md`, Section 2, gives a binary plane Sym²B or a common-factor plane eU′. Support containment in U gives B⊂U in the first case; in the second it gives e∈U and U′⊂U, hence U′=U. Thus the stated binary-cubic argument and the two common-factor paths are both legitimate and force a compatible square.

The lower bound dim K′≥3 follows from the fact that S is a surface. These cases exhaust the possible span dimensions; no extension of v or new generic-rank hypothesis is needed.

## Scope

The distinct-plane upgrade uses the dimension-five product-span bound essentially. Together with the cited, checked ternary results, it excludes coincident planes when K has dimension five and full support. With the separately established point/curve-factor reductions, the stated remaining frontier is a surface with both factor projections two-dimensional and at least one nonplanar image. This audit does not independently re-prove those point/curve-factor reductions. One planar and one nonplanar image remains outside these arguments. The contact criterion supplies a sufficient obstruction; it does not establish that a suitable diagonal contact exists in the remaining cases.
