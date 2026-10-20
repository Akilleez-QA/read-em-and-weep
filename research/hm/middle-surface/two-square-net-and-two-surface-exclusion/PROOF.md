# Two-square K7 nets and two-surface factor images are excluded

Work over C. Let dim E=4, let K⊂Sym²E have dimension seven, let W=K⊥ have dimension three, and let v:K→E be linear and square-avoiding:

    v(e²)∉Ce whenever e≠0 and e²∈K.

An ordered compatible threefold is an integral projective threefold Z⊂P(E)×P(E), meeting the independent-pair locus densely, such that ab∈K and v(ab)∧a∧b=0 identically. The diagonal wedge identity alone imposes no square compatibility; the proof below obtains that compatibility by differentiation.

## Conclusions

1. If W contains two linearly independent squares, no ordered compatible threefold exists. Thus the projective compatible rank-two tensor locus has dimension at most two for every such K and v.
2. For arbitrary W and square-avoiding v, no ordered compatible threefold has factor-image dimensions (2,2), using the established integral-quadric and plane rank-drop theorems listed below.

The possible factor dimensions for any remaining threefold are therefore (2,3), (3,2), or (3,3). This does not exclude those remaining cases.

## Dependencies

- /research/hm/universal-polar/rank-three-compatible-fiber-structure/PROOF.md, Sections 1–2: universal finite-compatible-partner-plane theorem. In particular neither factor image of a compatible threefold is a point or curve.
- /research/hm/middle-surface/polar-rank-two-net-exclusion/PROOF.md: excludes nets of generic polar rank at most two.
- ../rank-three-common-radical-exclusion/PROOF.md: excludes nets with a common radical and generic polar rank three.
- ../rank-three-common-radical-exclusion/REMAINING_SURFACE_DEGREES.md: in the remaining branch, every surface factor image is a plane or integral quadric; the total divisorial polar rank-drop degree is at most two.
- /research/hm/middle-surface/quadric-polar-rank-drop-exclusion/PROOF.md: a net whose polar rank-drop locus contains an integral quadric admits no compatible threefold.
- ../plane-polar-rank-drop-exclusion/PROOF.md, Sections 2–5: a plane factor image P(F) must have restriction dimension dim(W|F)=2 and W must contain the square of an equation of F. Restriction dimension three forces a common radical, and dimensions at most one are excluded as factor images.

The argument uses only these stated results, not a claim that every plane in the rank-drop locus is itself a factor image.

## 1. Reduction of a two-square net

Write

    W=span{z²,y²,q},

where z,y∈E* are independent, since their squares are independent. Put A=ker z, B=ker y, and L=A∩B. Thus dim A=dim B=3, dim L=2, and A+B=E. Let B_q denote the symmetric bilinear form of q, so q(e)=B_q(e,e).

By the low-polar-rank and common-radical exclusions, a hypothetical compatible threefold allows us to assume that the generic polar rank is three and W has zero common radical.

For every pair in Z, the two square equations are

    z(a)z(b)=0,    y(a)y(b)=0.

Their common zero set is the union of the four closed products

    P(L)×P(E),   P(A)×P(B),   P(B)×P(A),   P(E)×P(L).

An integral Z must lie in one member of this finite union. The first and fourth have a curve factor image and are impossible by the universal theorem. Exchanging factors if necessary gives

    Z⊂P(A)×P(B).

Each image must equal the indicated plane, again because neither can have dimension at most one.

## 2. The restricted third equation is nonzero

Let R=B_q|A×B. Then R≠0.

Indeed choose coordinates x₁,x₂,y,z on E. Since A is z=0 and B is y=0, the restriction B_q(a,b) detects all coefficients of q except those of y² and z²: the xᵢxⱼ coefficients are detected on L×L, xᵢy on the y-direction in A paired with the xᵢ-direction in L⊂B, xᵢz on the xᵢ-direction in L⊂A paired with the z-direction in B, and yz on the y-direction in A paired with the z-direction in B. Therefore R=0 implies q∈span{y²,z²}, contradicting independence of the basis of W.

This rules out the whole-product, four-dimensional incidence exception.

## 3. Rank-one and irreducible restrictions

If R has matrix rank one, it has the form α(a)β(b) for nonzero α∈A*, β∈B*. Its zero set is

    P(ker α)×P(B)  ∪  P(A)×P(ker β).

Each component has a line factor image. Since Z is integral, it lies in one component, contradicting the universal factor-image theorem. This handles every reducible case: a nonzero bihomogeneous polynomial of bidegree (1,1) factors nontrivially only as a (1,0) form times a (0,1) form, equivalently only when its matrix has rank one.

Consequently rank R≥2 and

    I_R={([a],[b])∈P(A)×P(B):R(a,b)=0}

is an integral hypersurface of dimension three. Since Z is a closed integral threefold contained in I_R, it equals I_R. In particular the compatibility polynomial identity holds at every point of I_R and on its tangent spaces at smooth points.

## 4. A smooth diagonal point always exists

Restrict q to the vector two-plane L. A homogeneous binary quadratic over C has a nonzero zero e∈L; this remains true if the restriction is identically zero. Thus

    z(e)=y(e)=q(e)=0,

so e²∈K and ([e],[e])∈I_R.

The vector e cannot be in the radical of B_q. If it were, it would also be in the radicals of z² and y², since z(e)=y(e)=0, and hence be a common radical vector of W. That branch was already excluded.

The differential of R at ([e],[e]) is

    (ξ,η) ↦ B_q(ξ,e)+B_q(e,η),
    ξ∈A/Ce, η∈B/Ce.

This is well-defined because q(e)=0. If it vanished identically, B_q(e,−) would vanish on both A and B and therefore on A+B=E, contrary to e not being radical. Hence I_R is smooth at ([e],[e]), with a three-dimensional tangent space T.

No transversality of the binary quadratic on L is required. Its root may be repeated, and q|L may be zero. Smoothness follows from the full form on A+B, not from its restriction to L.

## 5. Tangent differences force a forbidden eigen-square

Define the linear tangent-difference map

    δ:T→E/Ce,   δ(ξ,η)=η−ξ.

Its kernel consists of pairs with ξ=η in E/Ce. Their common value belongs to

    (A/Ce)∩(B/Ce)=L/Ce,

which has dimension one. Thus dim ker δ≤1 and dim im δ≥2, since dim T=3.

Differentiate the polynomial compatibility identity on I_R at ([e],[e]), using any local representatives in E. The derivative of v contributes zero because e∧e=0. The remaining terms give

    v(e²)∧e∧(η−ξ)=0   for every (ξ,η)∈T.

If the class of v(e²) in E/Ce were nonzero, this equation would force every vector of im δ into its one-dimensional span. That contradicts dim im δ≥2. Therefore

    v(e²)∈Ce.

Since e²∈K, this contradicts square avoidance. This proves Conclusion 1.

The proof handles distinct square-defining hyperplanes automatically: independent squares force independent linear forms. The rank-zero restriction, rank-one/reducible restriction, common-radical diagonal roots, repeated binary roots, and identically zero binary restriction have all been treated explicitly.

## 6. Elimination of all (2,2) factor-image threefolds

Suppose now that W is arbitrary and an ordered compatible threefold Z has two surface factor images S,T. The previous low-rank/common-radical exclusions and divisorial-degree bound show that each image is a plane or an integral quadric. The integral-quadric rank-drop theorem excludes the presence of either integral quadric. Therefore S=P(A) and T=P(B) are planes.

The plane-factor theorem says

    dim(W|A)=dim(W|B)=2,

and W contains the square of a defining equation of each plane.

If A≠B, their defining equations are independent. Thus W contains two independent squares, excluded by Conclusion 1.

It remains to handle the coincident-plane case A=B. Put F=A=B. Because dim(W|F)=2, choose q₁,q₂∈W with independent restrictions Q₁,Q₂ to F. Their associated symmetric bilinear forms define independent bihomogeneous polynomials

    R₁(a,b), R₂(a,b)∈C[a₀,a₁,a₂,b₀,b₁,b₂]

of bidegree (1,1). Independence follows because restriction to the diagonal recovers Q₁,Q₂ in characteristic zero. On P(F)×P(F), both R₁ and R₂ vanish on Z.

An integral threefold in the four-dimensional product is a divisor. Therefore R₁,R₂ have a common irreducible bihomogeneous factor defining that divisor. This may be seen by taking the bihomogeneous prime ideal of the twofold affine cone over Z: it has height one in a polynomial UFD, and hence is generated by an irreducible bihomogeneous polynomial F₀. Its bidegree is one of (1,0), (0,1), (1,1), since it divides a nonzero (1,1) polynomial.

A factor of degree (1,0) or (0,1) forces one factor image of Z into a line, contradicting that both images equal P(F). A factor of degree (1,1) makes both R₁ and R₂ scalar multiples of F₀, contradicting their independence. Thus the coincident-plane case is impossible as well.

This proves Conclusion 2. The coincident-plane argument does not assume that the two restricted conics have distinct or transverse base points; all common-component and nonreduced-base-scheme cases are covered by the bihomogeneous factor argument.

## 7. Scope

For a compatible rank-two tensor component of dimension at least three, finite multiplication of independent ordered factors permits choosing an integral ordered compatible threefold. Consequently the two-square exclusion gives the stated dimension-at-most-two conclusion for that net class.

The (2,2) theorem instead excludes that factor-image type only. It does not by itself eliminate a threefold with a plane and a dominant factor, or one with two dominant factors. All statements concern reduced dimensions.
