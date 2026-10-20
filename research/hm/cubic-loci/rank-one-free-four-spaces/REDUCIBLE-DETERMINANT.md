# Rank-one-free four-spaces with reducible determinant

## Universal theorem

Work over C. Let W have dimension three and let K be a four-dimensional linear subspace of sl(W) containing no nonzero rank-one endomorphism. Write h(A)=det A and q(A)=tr(A²).

The polynomial h|K is nonzero. The following conditions are equivalent:

1. h|K is reducible over C.
2. K contains a three-dimensional subspace L on which determinant vanishes identically.
3. After conjugation, K=so(3,C) ⊕ C S, where S is a nonzero symmetric traceless invertible matrix.

In this normal form, with C(x)v=x×v and A=tS+C(x),

    h(t,x)=t Q(t,x),       Q(t,x)=(det S)t²+xᵀSx,
    q(t,x)=(tr S²)t²−2xᵀx.

Consequently the projective determinant surface is the reduced union of the plane P={t=0} and the smooth irreducible quadric B={Q=0}. Their intersection D is a smooth conic, and they meet transversely along D. There is exactly one plane component, so L is uniquely determined by K.

The spectral incidence

    X={h=0, q≠0} ⊂ P(K)

has exactly two irreducible components P°=P\V(q) and B°=B\V(q). Each component is a nonempty smooth surface. They intersect along the nonempty smooth irreducible curve D°=D\V(q), and the singular scheme of X is precisely this reduced curve. Locally along D°, X has the ordinary normal-crossing equation uv=0 in a smooth three-dimensional ambient space. In particular X is reduced, pure of dimension two, and is not smooth.

This is a fixed-K classification of the reducible determinant branch. It makes no assertion that any actual structural kernel K_W has dimension four or reducible determinant, or that the corresponding locus of W is nonempty, smooth, or of any particular dimension.

## Dependency

The constant-rank-net conjugacy and four-space obstruction are proved in [the preceding unit](../constant-rank-nets/PROOF.md). No actual-operation hypothesis is used.

## 1. Reduction to a symmetric extra generator

If h|K were identically zero, every nonzero member of K would have rank exactly two, contrary to the imported four-space obstruction. Thus h|K is a nonzero homogeneous cubic.

A reducible homogeneous cubic over C has a homogeneous linear factor: in any nontrivial factorization, the positive degrees sum to three, so some irreducible factor has degree one. Its kernel L in K has dimension three and determinant vanishes identically there. Conversely, vanishing on a hyperplane implies divisibility by its defining linear equation, so the existence of L makes h|K reducible.

By the imported singular-net classification, conjugate so that L=so(3,C). Choose an extra generator T of K and decompose it uniquely into its symmetric and skew-symmetric parts. Subtracting its skew-symmetric part does not change K, giving

    K=so(3,C) ⊕ C S,       Sᵀ=S,       tr S=0.

Here S is nonzero because T is outside L. This reduction is conjugation of endomorphisms, not merely unrelated left and right changes of basis.

## 2. Exact rank-one-free criterion

We prove for every nonzero symmetric traceless S that the space above contains no nonzero rank-one element if and only if S is invertible.

Suppose first that S is singular. A complex symmetric matrix of rank at most two admits a decomposition

    S=aaᵀ+bbᵀ

for vectors a,b, allowing b=0 in rank one. This follows by congruence reduction of a symmetric bilinear form to a diagonal matrix with its nonzero diagonal entries normalized to one. Put u=a+ib and v=a−ib. Then

    S=(uvᵀ+vuᵀ)/2,       uᵀv=tr S=0.

Since S≠0, neither u nor v is zero. The nonzero rank-one matrix R=uvᵀ is traceless, and R−S=(uvᵀ−vuᵀ)/2 is skew-symmetric. Therefore R lies in K, contradicting rank-one-freeness.

Conversely suppose S is invertible, and assume R=tS+C(x) has rank one. Every rank-one matrix is uvᵀ with u,v nonzero. Its symmetric part (uvᵀ+vuᵀ)/2 has rank at most two because its image is contained in span(u,v). But the symmetric part of R is tS. Invertibility of S forces t=0. Now R is skew-symmetric. A nonzero skew-symmetric matrix over a field of characteristic different from two has even rank, and in size three has rank two, so cannot have rank one. This contradiction proves the criterion.

This also proves the converse implication from normal form (3) to the theorem's hypotheses and reducibility, without claiming realization by an actual structural kernel.

## 3. Universal determinant and trace identities

For the cross-product operator one has the polynomial identities

    C(x)²=xxᵀ−(xᵀx)I,       adj(C(x))=xxᵀ.

The latter follows either by the universal cofactor formula or from the size-three adjugate identity and the former. Since S is symmetric and C(x) skew-symmetric, transpose invariance of determinant implies det(tS+C(x))=det(tS−C(x)). The homogeneous cubic expansion therefore has only terms of degree zero or two in x. The degree-zero term is t³det S. The term linear in t is

    t tr(adj(C(x)) S)=t xᵀSx.

The constant-in-t determinant det C(x) is zero. This gives h=tQ as stated.

The trace pairing between a symmetric and a skew-symmetric matrix is zero. Using the displayed cross-product square identity therefore gives

    tr((tS+C(x))²)=t²tr S²−2xᵀx.

No orthogonal diagonalization of S is assumed; complex symmetric matrices need not be orthogonally diagonalizable. The formulas hold for all symmetric S by polynomial identities.

## 4. Geometry of the cubic and its open incidence

The quadratic form Q has block matrix diag(det S,S) in coordinates (t,x). Since det S≠0, it is nondegenerate of rank four. Hence B is a smooth irreducible quadric in P³. The polynomial Q is not divisible by t, so tQ is square-free and defines exactly the two reduced irreducible components P and B.

Their intersection is

    D={t=0, xᵀSx=0} ⊂ P².

Since S is invertible, this is a smooth irreducible conic. At a point [0:x] of D, the differential of Q has x-part 2Sx, which is nonzero, while dt has zero x-part. Thus dt and dQ are independent and P and B meet transversely everywhere on D. The quadric is irreducible and has no plane component, proving uniqueness of P and of the singular three-space L.

On P the quadratic q is −2xᵀx, so P° is the complement of a smooth conic. It is nonempty, smooth, and irreducible.

We check that D° is nonempty, which simultaneously proves nonemptiness of B°. If q vanished everywhere on D, the quadratic xᵀx would vanish on the irreducible conic cut out by xᵀSx. Its prime homogeneous ideal is generated by xᵀSx. Equality of degrees would force these two quadratics to be proportional. Thus S would be a scalar matrix. Since tr S=0 in characteristic zero, this scalar would be zero, contrary to invertibility. Therefore D° is nonempty. In fact the two conics have no common component, so their intersection is a finite degree-four intersection scheme counted with multiplicity; no claim of four distinct deleted points is needed.

A nonempty open subset of an irreducible smooth quadric is irreducible and smooth, giving the assertions for B°. The intersection D° is a nonempty open subset of a smooth irreducible conic. Both surface components remain distinct after taking these opens. Consequently they are exactly the two irreducible components of X.

Away from D, one factor of h=tQ is invertible on its respective surface and the other factor cuts out a smooth surface, so X is smooth there. Along D°, the independent differentials dt,dQ allow t,Q to be completed to regular local coordinates. Thus the local equation of X is uv=0. Its Jacobian singular ideal is (u,v), so the singular scheme is exactly the reduced smooth curve D°. This establishes the scheme-theoretic assertions and transversality, not merely the topology of the cubic's support.

