# Fixed complementary splittings admit only finitely many rank-one middles

## Statement

Work over C. Let V have dimension five, let J be finite-dimensional, and let f:V×V×V→J be trilinear, outer symmetric, and cyclic zero. Assume for every nonzero a∈V that

    A_a: V/Ca → J,    b ↦ f(a,a,b)

is injective. Fix a complementary decomposition V=X⊕Y with dim X=2 and dim Y=3. Then the closed projective locus

    B_X,Y = {[u]∈P(V): dim f(X,u,Y)≤1}

has finite support. In particular it contains no complete curve.

This is an abstract tensor statement, independent of any source ranks or physical realization. It does not exclude curves along which the splitting varies.

## 1. Two elementary consequences of repeated-input injection

Cyclic zero gives f(a,a,a)=0 and, together with outer symmetry,

    f(b,a,b)=−2f(b,b,a)=−2A_b(a).

If a,b are linearly independent, A_a(b) and A_b(a) are linearly independent in J. Indeed both are nonzero. Any dependence could therefore be written A_a(b)=t A_b(a). Expanding and using the preceding identity gives

    A_(a+t b)(b)
      = f(a+t b,a+t b,b)
      = A_a(b)+t[f(a,b,b)+f(b,a,b)]+t²f(b,b,b)
      = A_a(b)−t A_b(a)
      = 0.

But a+t b and b are independent, contradicting injectivity of A_(a+t b).

Every [u]∈B_X,Y lies outside P(X) and P(Y). If u∈X, the rectangular image contains A_u(Y), of dimension three because Y∩Cu=0. If u∈Y, it contains A_u(X), of dimension two because X∩Cu=0. Both contradict the rank bound.

Consequently, writing u=x+y with x∈X and y∈Y gives independent nonzero x,y. Outer symmetry implies

    c(u):=f(x,u,y)=f(x,x,y)+f(x,y,y)=A_x(y)+A_y(x)≠0.

This cubic vector lies in f(X,u,Y). In particular the rectangular rank is exactly one at every point of B_X,Y; there is no rank-zero issue.

## 2. The line-bundle contradiction

Suppose B_X,Y contains an integral complete curve. Let T be its normalization and let

    U = O_P(V)(−1)|_T,    deg U=−d,

where restriction includes pullback to T. Here T is smooth projective and d>0 because the map T→P(V) is nonconstant. Write W=X⊗Y, a constant six-dimensional vector space.

The linear dependence on the middle input defines a bundle map

    U⊗W → J⊗O_T.

It has constant rank one, so its image is a line subbundle M of the trivial J-bundle, and the induced map U⊗W→M is surjective. Tensoring by U* shows that M⊗U* is globally generated. Therefore

    deg M + d ≥ 0.                                      (1)

The fixed projections P_X and P_Y induce bundle maps U→X⊗O_T and U→Y⊗O_T. Applying f to these maps and the middle inclusion U→V⊗O_T gives

    U^⊗3 → J⊗O_T,
    u⊗u⊗u ↦ f(P_Xu,u,P_Yu).

It factors through M. Section 1 shows that this map is nonzero on every fiber; a nowhere-vanishing map between line bundles is an isomorphism. Hence

    M ≅ U^⊗3,       deg M=−3d.                          (2)

Equations (1) and (2) give −2d≥0, a contradiction.

Finally B_X,Y is projective and closed, being cut out by the 2×2 minors of the matrix of the linear map u↦[f(−,u,−)|_(X×Y)]. Every positive-dimensional complex projective variety contains an integral projective curve. Therefore B_X,Y is zero-dimensional and has finite support. This is a set-theoretic finiteness statement; reducedness is not asserted.

## 3. Equivalent rank-one determinantal interpretation

On T, the surjection U⊗W→M is equivalently a nowhere-zero family of scalar rectangular forms valued in M⊗U*. The projected inputs x and y each carry one additional copy of U. Their evaluation is the nowhere-zero cubic above. Thus a rank-one factorization would force the globally generated line bundle M⊗U* to be U², a negative-degree line bundle. This is the precise obstruction beyond merely avoiding P(X) and P(Y).

## Scope and dependencies

Only outer symmetry, cyclic zero, global repeated-input injection, the fixed complementary (2,3) splitting, and elementary projective-curve/line-bundle facts are used. No finite-exceptional-polar theorem, scroll classification, residual-rank assumption, or earlier incidence dimension theorem is needed. The proof addresses fixed splittings only. A moving splitting need not have everywhere-regular fixed projectors, so the cubic construction used here cannot be transferred across its degeneration points without additional work.


