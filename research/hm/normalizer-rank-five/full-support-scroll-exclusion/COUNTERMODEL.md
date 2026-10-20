# An isolated globally realizable full-support cubic-scroll fiber

## Result

There exists an abstract outer-symmetric, cyclic-zero trilinear map f:V³->J over C, with dim V=5 and dim J=20, for which every repeated-input map A_a:V/Ca->J is injective, and:

- rank Q_u=5 at one specified middle line [u];
- rank Q_a=10 at every other middle line;
- ker Q_u has full four-dimensional support;
- its compatible residual locus is exactly a smooth cubic scroll;
- the separately projectivized independent-zero fiber over [u] is the disjoint union of two smooth cubic scrolls, exchanged by outer-factor interchange.

The total projective independent-zero locus has dimension two and its all-inputs-nonzero affine version has dimension five. This is not a seven-dimensional counterexample, not a positive-dimensional middle family, and not an occurrence or equivariance claim about any specified source operation.

## 1. A squarefree residual model with exactly one compatible surface

Write V=Cu direct-sum E, and choose a basis x,y,z,w of E. Put

    K=span{k1=xz, k2=yz, k3=xy, k4=xw+y², k5=yw}.

Define v:K->E by

    v(k3)=x,  v(k4)=y,  v(k1)=v(k2)=v(k5)=0.

The companion PROOF.md, Sections 6 and 6.1, establishes that K has no nonzero square, has full support, and

    R2(K)=S union P(y span{x,z,w}),

where S is the smooth cubic scroll parametrized by

    q=(s x+t y)(a z+b(s y+t w)).

All points of S have rank two. Direct substitution gives

    v(q)=b s(s x+t y),

so every point of S is compatible. For a point of the additional plane write q=y(Ax+Bz+Cw). Its correction is A x. Since x,y,z,w are independent, compatibility is equivalent to

    A=0,  or B=C=0.

The first locus is the line P(y span{z,w}), the s=0 ruling of S. The second is the point [xy], also in S. Thus the compatible rank-two locus is exactly S, set-theoretically. This exact statement is enough for every dimension and component claim below; no assertion about its compatibility scheme structure is needed.

## 2. Universal trilinear model and the prescribed graph

Put

    W=ker(V tensor exterior²V -> exterior³V),  dim W=40,
    f0(a,b,c)=a tensor (b wedge c)+c tensor (b wedge a).

This is outer symmetric and cyclic zero. Its repeated map is

    A0_a(b)=a tensor (a wedge b).

For each nonzero a define F_a=im[Sym²V->W, bc->f0(b,a,c)]. A splitting V=Ca direct-sum U shows that dim F_a=14, that A0_a(V) has dimension four, and that

    F_a/A0_a(V) is naturally Sym²(V/Ca).

Indeed a² maps to zero, aU maps isomorphically to A0_a(V), and Sym²U maps injectively into U tensor (a wedge U). Also F_a is contained in V tensor (a wedge V).

Define B0_u(q)=f0(-,u,-)(q), using E as representatives, and prescribe the five-plane

    L={B0_u(q)-A0_u(v(q)):q in K} inside F_u.

With ab=(a tensor b+b tensor a)/2 and M(q) its symmetric contraction matrix, the lift has tensor matrix

    [ -v(q)^T ]
    [  2M(q)  ]

in first factor Cu direct-sum E and second factor u wedge E. Its second-factor support is

    u wedge (im q+Cv(q)).

Every nonzero q in K has rank at least two, so every nonzero member of L has tensor rank at least two and second-factor support dimension at least two. The graph map is injective, hence dim L=5.

The projective tensor-rank-one locus X in P(W) is exactly the repeated-input flag variety

    {[a tensor (a wedge b)]: a,b independent},

of dimension seven. To check this, a tensor beta lies in W precisely when a wedge beta=0; splitting off a forces beta=a wedge b. The line Ca and plane span(a,b) are recovered from the factors, so this is the closed projective flag image. We have P(L) disjoint from X.

Furthermore

    L intersect F_a=0 for [a] different from [u].           (1)

If a nonzero graph lift lay in F_a, its second support would contain u wedge e1 and u wedge e2 for independent e1,e2 in E, and both would belong to a wedge V. Thus a belongs to span(u,e1) intersect span(u,e2)=Cu, a contradiction. This direct support argument is sufficient; no formula for F_a intersect F_u is needed.

## 3. Generic extension preserves the graph and avoids every other middle

Let Wbar=W/L, dim Wbar=35, and consider G=Gr(15,Wbar), of dimension 300. A point M determines the inverse-image twenty-plane N in W containing L.

The condition M intersect (F_u/L)=0 is a nonempty open because dim(F_u/L)=9 and 15+9<=35. It says N intersect F_u=L.

Over B=P(V) minus {[u]}, the images H_a of F_a in Wbar form a rank-fourteen subbundle by (1). The incidence of triples (a,[h],M) with [h] in P(H_a) intersect P(M) has dimension

    4+13+dim Gr(14,34)=4+13+280=297<300.

Its image is constructible; the closure still has dimension at most 297. Its complement therefore gives a nonempty open on which N intersect F_a=0 for every a in B. Irreducibility of G permits both open conditions simultaneously.

These two conditions already imply P(N) disjoint from X. Every point of X belongs to some F_a. For a different from u there is no intersection, and for a=u the intersection is L, which has no rank-one tensor. Thus no extra assumption is needed to retain all repeated-input injections.

For completeness, this is exactly the generic extension argument of rank-five-surface-countermodel/PROOF.md, Sections 3--5. Its only local hypotheses are dim K=5 and tensor-rank-at-least-two for every nonzero graph lift. It never requires ternary support. Both hypotheses have been independently checked above.

## 4. The quotient has the stated exact residual ranks

Choose N as above and let J=W/N, f be the image of f0. Then dim J=20. Outer symmetry and cyclic zero descend. Avoidance of X makes every repeated-input map A_a injective. For the residual map

    Q_a:Sym²(V/Ca)->J/A_a(V/Ca)

one has

    rank Q_a=dim(image F_a in J)-4
            =10-dim(N intersect F_a).

Consequently rank Q_u=5 and rank Q_a=10 for all other middle lines. Moreover projection of L to F_u/A0_u(V) identifies ker Q_u exactly with K, and the graph equation gives

    f(-,u,-)(q)=A_u(v(q)) for q in K.

Thus the correction used above is exactly the actual fixed-middle graph correction, with no additional sign or factor two.

## 5. Exact ordered fiber and two scroll components

For q=l n with l,n independent in E, write v(q)=c l+d n. Outer lifts l+alpha u, n+beta u give

    f(l+alpha u,u,n+beta u)=A_u(v(q)+beta l+alpha n).

The unique ordered zero directions are therefore [l-d u],[n-c u]. On our scroll l=sx+ty, n=a z+b(sy+tw), and c=bs,d=0. They become

    ([sx+ty], [u], [a z+b(s(y-u)+t w)]).                  (2)

Put X0=span{x,y} and Y0=span{z,y-u,w}. These are complementary subspaces of V, of dimensions two and three. The two outer factors in (2) lie respectively in X0 and Y0 and are never zero. Formula (2) is an algebraic morphism from S: the factor line l is the ruling projection, and the second line is defined on the projective-bundle model with its correct fiber weights. It is a section of the degree-two ordered-factor reconstruction over S and is an isomorphism onto its image, since multiplying residual factors recovers q. Interchanging the two outer entries gives a second such image.

The two images are disjoint because X0 and Y0 are complementary, so no outer line can belong to both. Every compatible rank-two tensor belongs to S by Section 1 and has exactly these two ordered factorizations. Therefore they exhaust the independent-zero fiber. Each is a smooth cubic scroll as an abstract variety (the statement concerns its isomorphism type; no single-projective-space degree is assigned to its embedding in the product).

At every other middle line Q_a is injective and no independent zero exists. Hence the whole projective independent-zero locus is precisely these two surfaces, and restoring three nonzero input scalings gives affine dimension five.

## Scope

This is a universal algebraic existence construction, using only abstract tensor identities and Grassmannian incidence dimensions. No actual source operation or physical source instance is evaluated, no numerical rank calculation is used, and no external action is performed. The only writes are mathematical proof artifacts. The result shows that full-support smooth cubic-scroll fibers genuinely occur under the coarse global injection and isolated rank-drop hypotheses; the squarefree case cannot be dismissed as a merely formal local exception.
