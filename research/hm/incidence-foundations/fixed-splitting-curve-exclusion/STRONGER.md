# Moving rectangular curves: determinant poles force finite middle image

## Theorem

Over C, let dim V=5 and let J be a complex vector space and let f:V³→J be a trilinear map that is outer symmetric and cyclic zero, with A_a:V/Ca→J, b↦f(a,a,b), injective for every nonzero a. Define the closed projective incidence

    R = {([u],X,Y)∈P(V)×Gr(2,V)×Gr(3,V): dim f(X,u,Y)≤1}.

Then the middle image of R has finite support. This strengthens the dimension-one bound in /research/hm/middle-surface/squarefree-scroll-middle-families/PROOF.md and excludes nonconstant-middle curves even when their splittings vary.

The proof uses neither a target dimension assumption nor physical/source ranks. It does not assert that R itself is finite: fibers at fixed middles can still have positive dimension.

## 1. Pointwise facts on all of R

For independent a,b, the vectors A_a(b), A_b(a) are independent. Indeed a dependence A_a(b)=tA_b(a) would imply

    A_(a+t b)(b)=A_a(b)−tA_b(a)=0,

contradicting injection. The expansion follows from outer symmetry and cyclic zero, as detailed in PROOF.md in this folder.

At every point of R, u lies in neither X nor Y. If u∈X, injection gives dim A_u(Y)≥2; if u∈Y, injection gives dim A_u(X)≥2. Both images are contained in the rectangular image, a contradiction.

Also dim(X∩Y)≤1. Otherwise X⊂Y. Every nonzero h∈X then satisfies

    0≠f(h,u,h)=−2A_h(u)∈f(X,u,Y).

A scalar coordinate on that image line would be a quadratic form on the two-dimensional X having no projective zero, which is impossible over C. A zero-dimensional image is already contradicted by the displayed nonzero value.

If X⊕Y=V, write u=a+b with a∈X,b∈Y. Both are nonzero, and

    c(u)=f(a,u,b)=A_a(b)+A_b(a)≠0.

If X∩Y=Ch, then f(h,u,h)=−2A_h(u)≠0 lies in the rectangular image. Thus the rectangular image has dimension exactly one EVERYWHERE on R.

At a noncomplementary point, put H=X+Y, of dimension four. Outer symmetry gives

    f(h,u,H) ⊂ f(X,u,Y).

We claim u∉H. Otherwise both f(h,u,h)=−2A_h(u) and f(h,u,u)=A_u(h) belong to the same image line, contradicting their independence. Thus

    V=Cu⊕H                                               (1)

at every noncomplementary point.

## 2. A complete curve entirely in the boundary has constant middle

Let T be a smooth projective integral curve mapping to R, and suppose X∩Y has dimension one everywhere on T. The image H of the addition map X⊕Y→V⊗O_T is then a rank-four subbundle. Here and below X,Y denote pulled-back tautological subbundles, and U denotes the middle tautological line.

Equation (1) gives U⊕H≅V⊗O_T. The projector onto U along H is a globally regular matrix on the complete integral curve, so all entries are constant. Its image U is therefore a constant line. The middle map is constant.

Consequently, on any complete curve with nonconstant middle map, the addition map X⊕Y→V⊗O_T is generically invertible.

## 3. Degree inequality from the rank-one rectangular map

Assume, for contradiction, that T→R is a smooth projective integral curve with nonconstant middle map. Write

    deg U=−d,                 d>0,
    deg det X=−d_X,           deg det Y=−d_Y.

The determinant of the generically invertible addition map defines an effective divisor D. At each point its multiplicity is the order of this determinant, and

    deg D=d_X+d_Y.

The rectangular map is everywhere rank one, so it has a line subbundle image M⊂J⊗O_T and induces a surjection

    U⊗X⊗Y ↠ M.

Tensoring by U*⊗det X*⊗det Y* gives a quotient line bundle of

    (X⊗det X*)⊗(Y⊗det Y*) ≅ X*⊗Λ²Y*.

Since X and Y are subbundles of the trivial V-bundle, X* and Y* are globally generated; so is X*⊗Λ²Y*. Therefore its quotient line bundle is globally generated, and

    deg M+d+deg D ≥ 0.                                   (2)

## 4. Exact poles of the projected cubic

Off D, use the splitting X⊕Y=V to write u=a+b. This defines the nonvanishing meromorphic bundle map

    s:U³ → M,       s(u³)=f(a,u,b).

There are no zeros or poles off D, by Section 1. We compute its order at a point p∈D of multiplicity m.

Choose a local parameter t and local frames. The addition matrix has corank exactly one at p, by Section 1. Over the local discrete valuation ring its Smith normal form therefore has four unit diagonal entries and one entry t^m times a unit. The local middle generator u has nonzero image in V/(X_p+Y_p) by (1). Its component in the exceptional Smith coordinate is consequently a unit. Its inverse image under the addition matrix has an exact pole of order m, with leading coefficient a nonzero vector in the special-fiber kernel.

That kernel consists of pairs (αh,−αh), where h spans X_p∩Y_p. Thus, after incorporating a nonzero scalar into h if desired, the actual projected vectors have expansions

    a=t^(−m)αh+terms of higher valuation,
    b=−t^(−m)αh+terms of higher valuation,       α≠0.

The chosen middle generator is regular and has value u₀ at p. Hence

    f(a,u,b)
      =−t^(−2m)α² f(h,u₀,h)+terms of higher valuation.

The leading coefficient is nonzero: f(h,u₀,h)=−2A_h(u₀)≠0 because u₀∉X_p. As M is a line SUBBUNDLE of the trivial J-bundle, valuation measured in J agrees with valuation measured in a local nonvanishing frame of M. Thus s has an exact pole of order 2m.

We have proved

    divisor(s)=−2D.

Since s is a meromorphic section of Hom(U³,M), its divisor has degree deg M+3d. Consequently

    deg M+3d=−2deg D.                                   (3)

Combining (2) and (3) yields

    0 ≤ deg M+d+deg D = −2d−deg D < 0,

the desired contradiction.

## 5. From curves to finite middle image

If the projective middle image of R had positive dimension, some integral projective curve in R would have nonconstant middle image. For completeness, choose an integral component dominating a positive-dimensional image, restrict over an integral curve in that image, choose a dominating component, and take sufficiently general hyperplane sections until obtaining a projective multisection curve. Normalize that curve to obtain a T of the forbidden kind.

Therefore the middle image is zero-dimensional and projective, hence has finite support. No reducedness of R or its image scheme is asserted.

## 5.1. The complementary triples themselves are finite

In fact every irreducible component of R that meets the complementary open set is zero-dimensional. If such a component had positive dimension, it would contain a nonconstant complete integral curve meeting that open set. Normalize it and repeat Sections 3–4, now allowing d≥0. They yield

    0≤−2d−deg D.

Thus d=0 and deg D=0. The nonnegative Plücker degrees satisfy d_X+d_Y=deg D=0, so both Grassmannian maps are constant. The middle map is constant because d=0. The resulting map to R is therefore constant, contrary to choosing an actual integral curve in R.

There are finitely many irreducible components of the projective incidence. Consequently its complementary triples form a finite set. Positive-dimensional components of R, if any, are entirely noncomplementary and have constant middle. This strengthening is set-theoretic.

## 6. Consequences for the explicit compatible type III scroll stratum

Use the definitions and fixed-middle computations in /research/hm/middle-surface/squarefree-scroll-middle-families/PROOF.md and /research/hm/middle-surface/squarefree-scroll-middle-families/ADDENDUM.md. Every compatible type III cubic scroll produces a point of R, by its intrinsic (2,3)-rectangular spans. Its middle therefore belongs to the finite set just proved, including both complementary and contraction cases.

Whenever the ENTIRE residual kernel is the explicit type III kernel and its scroll is densely compatible, the full projective independent-zero fiber has dimension exactly two, as proved in that addendum. A component dominated by these ordered scroll surfaces consequently has projective dimension two and affine dimension exactly five, accounting for the three independent nonzero vector scalings. Any other independent-zero component supported over these same finite middles and satisfying those full-kernel hypotheses has affine dimension at most five.

In particular, neither a six-dimensional nor a seven-dimensional affine independent-zero component can be generically dominated by these compatible explicit type III scrolls. This does not change the separate conditional bound six for arbitrary components in the explicit kernel family whose generic compatible fibers are at most curves and whose middle image can have dimension two. It also supplies no classification of unclassified residual kernels.

## Scope and provenance

The new finiteness theorem uses only the stated universal tensor hypotheses and elementary bundle geometry on complete curves. Its pointwise boundary and rank-one facts were proved here, so even the earlier finite-polar and middle-dimension theorems are not dependencies. The scroll corollary additionally uses the already established explicit full-kernel fiber calculation and finite ordered lift reconstruction.

All work is abstract mathematical reasoning.
