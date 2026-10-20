# An explicit rank-three excess surface with globally injective repeated inputs

Work over C. This is an abstract construction. No normalizer action or equivariance, prescribed target representation, or identification with the actual source operation is asserted.

## Theorem

There exists an outer-symmetric, cyclic-zero trilinear map f:V^3 -> J, with dim V=5 and dim J=20, such that every repeated-input map V/Cm -> J is injective, exactly one middle line [u] has residual rank three, every other middle has residual rank ten, and the middle fiber at u contains two swap-exchanged projective planes as irreducible components. Each plane is generically smooth in the fiber.

Thus a universal fiber-dimension bound of one is false under these abstract hypotheses, even with isolated residual-rank-drop support. This does not settle a version imposing a specified group action or the actual source operation.

## 1. Seven-dimensional residual kernel and correction

Write V=Cu direct-sum E, with E=<a,b,c,d>, and put U=<b,c,d>. Products denote symmetric products, xy=(x tensor y+y tensor x)/2. Set

    K=<ab,ac,ad,b²-a²,bc,bd,cd> subset Sym²E.

These seven tensors are linearly independent. Define v:K -> E by

    v(b²-a²)=c,
    v(ab)=v(ac)=v(ad)=v(bc)=v(bd)=v(cd)=0.

This is square-avoiding in the exact required sense: if 0!=e² belongs to K, then v(e²) is not in Ce. Indeed write e=Aa+Bb+Cc+Dd. The equations for e² in K are

    A²+B²=0, C²=0, D²=0.

Over C this forces C=D=0, B!=0, and A=+iB or -iB. Furthermore

    e²=B²(b²-a²)+2AB ab,
    v(e²)=B² c,

which is not proportional to e. There are precisely two square lines in K. Their scheme-theoretic multiplicities are irrelevant: this avoidance condition concerns every nonzero square tensor, and the argument checks all of them.

The kernel contains the transverse common-factor space aU, and v vanishes on aU. Hence every independent pair (a,z) with 0!=z in U satisfies both az in K and v(az) in span(a,z), with correction coefficients zero.

## 2. An explicit middle map and its plane components

Define symmetric bilinear maps B:E x E -> E and q:E x E -> C³ by

    B(e,e')=B_e B_e' c,
    q(e,e')=(A_e A_e'+B_e B_e', C_e C_e', D_e D_e'),

where subscripts denote coordinates in the displayed basis. Then ker q=K and B|K=v. Define h:Sym²V -> E direct-sum C³ by

    h(x0 u+e,z0 u+e')=(x0 e'+z0 e+B(e,e'), q(e,e')).

The map h has rank seven: h(u,E)=E, and q has rank three. It kills u² and has no other projective diagonal zero. To check the latter, if h(x0 u+e,x0 u+e)=0 and e!=0, then e² is in K and

    v(e²)=-2x0 e,

contradicting square avoidance.

Let X_h be the scheme cut out by h(x,z)=0 in P(V) x P(V). It contains

    S={([a],[z]): [z] in P(U)} isomorphic to P²,
    S'={([z],[a]): [z] in P(U)} isomorphic to P².

These planes are disjoint because a is not in U. Every point on them gives an independent triple with u.

Here is a direct check that they are components, rather than merely surfaces inside larger components. Consider a point ([a],[b+s c+t d]) with s,t nonzero. Use local projective charts x_a=z_b=1. In the eight tangent coordinates x0,x_b,x_c,x_d,z0,z_a,z_c,z_d, the linearizations of the seven defining equations are

    z0,
    x0,
    s x0+x_b,
    t x0,
    z_a+x_b,
    s x_c,
    t x_d.

They have rank six. Thus the Zariski tangent space is two-dimensional. Since the local fiber contains the smooth two-dimensional plane S, its local dimension is at least two; equality of local dimension and embedding dimension proves the local ring is regular of dimension two. Consequently S is an irreducible component, and the fiber is smooth on the stated open subset of S. Swap symmetry proves the same for S'. No general fiber-dimension theorem is needed for this assertion.

## 3. Universal cyclic operation

Set

    W=ker(V tensor wedge²V -> wedge³V), dim W=40,
    f0(x,m,z)=x tensor (m wedge z)+z tensor (m wedge x).

The operation takes values in W, is symmetric in x,z, and its cyclic sum vanishes by direct cancellation. For each nonzero m let

    A0_m(z)=m tensor (m wedge z),
    F_m=im(f0(-,m,-)).

Splitting V=Cm direct-sum E_m shows dim F_m=14: the four-dimensional mE_m part maps injectively to A0_m(V), while the ten-dimensional Sym²E_m part maps injectively to the symmetric lower block in E_m tensor (m wedge E_m). Thus F_m/A0_m(V) identifies with Sym²(V/Cm).

Let B0_u:Sym²E -> W be the restriction of f0(-,u,-), and define the seven-plane

    L={B0_u(r)-A0_u(v(r)): r in K} subset F_u.

The map from K is injective because its lower block recovers r. With rows Cu direct-sum E and second-factor columns u wedge E, a tensor in L has matrix

    [-v(r)^T; 2M(r)],

where M(r) is the symmetric contraction matrix of r. Every nonzero such tensor has second-factor support of dimension at least two. For rank(r)>=2 this follows from the lower block. If rank(r)=1, then r is a scalar square over C, and square avoidance makes v(r) independent of its one-dimensional contraction image.

In particular L contains no nonzero repeated-input tensor, all of which have tensor rank one. More strongly,

    L intersect F_m=0 whenever [m]!=[u].

Indeed F_m is contained in V tensor (m wedge V). If a nonzero tensor of L lies there, its support includes u wedge w1 and u wedge w2 for linearly independent w1,w2 in E. The membership u wedge wi in m wedge V implies m lies in span(u,wi): wedge with m, or use the support plane of a nonzero decomposable two-vector. The intersection of these two planes is Cu, contradiction.

Also L intersect A0_u(V)=0, directly from the lower block.

## 4. Quotient to a twenty-dimensional target

Put Wbar=W/L, of dimension 33. Choose a thirteen-plane M in Wbar satisfying

    M intersect (F_u/L)=0,
    M intersect image(F_m)=0 for all [m]!=[u].

Such M exist. The first condition is nonempty open, because dim(F_u/L)=7 and 13+7<=33. For the second, the image spaces F_m form a rank-fourteen subbundle on P(V) minus {[u]}, since L intersect F_m=0 there. The incidence of a middle, a line in its image, and a thirteen-plane containing that line has dimension

    4+13+dim Gr(12,32)=4+13+240=257,

whereas dim Gr(13,33)=260. Its image closure is proper, so a nonempty open subset avoids every such image simultaneously. Intersect the two nonempty open subsets of the irreducible Grassmannian.

Let T be the inverse image of M in W, and set J=W/T, f=quotient composed with f0. Then dim T=20, dim J=20, and

    T intersect F_u=L,
    T intersect F_m=0 for [m]!=[u].

Every repeated-input map remains injective: away from u its image lies in F_m, which survives injectively, while at u the graph L misses A0_u(V). The residual ranks are

    rank Q_m=10-dim(T intersect F_m),

because the four-dimensional repeated-input image survives. Thus the residual rank is three at u and ten at all other middles.

## 5. Exact identification of the middle fiber

The maps h and f(-,u,-) have the same kernel in Sym²V. Namely each has kernel

    Cu² direct-sum {r-u v(r): r in K}.

For h this follows by projecting first to q and then to E; for f it follows from T intersect F_u=L and f0(u,u,e)=A0_u(e). Both middle maps have rank seven. Hence their seven-dimensional spaces of scalar bilinear equations coincide, and their projective middle fibers agree scheme-theoretically. In particular the two generically smooth plane components constructed above belong to the global operation's rank-three fiber.

## Audit and limitations

- Symmetric-product factors are fixed explicitly; the graph uses r-u v(r), with no factor-of-two ambiguity. The universal lower block has the factor two, while f0(u,u,e)=A0_u(e).
- All square tensors in K were classified explicitly, rather than checked at sampled points.
- The surface is explicit and its component status is proved by a six-rank Jacobian calculation; no inference from equation counts is used.
- Global repeated-input injectivity, target dimension twenty, and all-other-middle residual rank ten are proved through one Grassmannian avoidance construction.
- The construction makes no claim of normalizer equivariance. If a proposed group action moves [u], this particular operation cannot be equivariant, since [u] is the unique residual-rank-drop point.
- It follows that abstract cyclic symmetry, outer symmetry, global repeated-input injectivity, square avoidance, target dimension twenty, and isolated rank-three support do not exclude excess surfaces. Additional hypotheses specific to the source or its group action would be indispensable for a universal dimension-one argument there.
