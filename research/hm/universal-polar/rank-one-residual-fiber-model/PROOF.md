# Sharp residual-rank-one fiber bound and an isolated global quotient model

## Statement and scope

Work over C. Let E have dimension four, K be a nine-dimensional subspace of Sym²E, and v:K→E be linear. Assume square avoidance: v(e²)∉Ce for every nonzero e with e²∈K. Ordered distinct pairs ([a],[b]) are compatible when ab∈K and v(ab)∈span(a,b).

1. Every such compatible locus has dimension at most three. This is unconditional and does not depend on a K8 theorem.
2. For K the kernel of a nondegenerate symmetric bilinear form h, a general linear v is square avoiding and its compatible locus is nonempty of dimension exactly three.
3. These data can be realized by a single abstract operation f:V³→J, dim V=5, dim J=20, outer symmetric and cyclic zero, whose repeated-input maps are injective at every line. The residual rank is one at one specified middle [u] and ten at every other middle.
4. Its total separately projectivized independent-zero locus has dimension three, and its all-inputs-nonzero affine independent-zero locus has dimension six. Its rank-drop support is one point.

This is an abstract existence construction, not a source operation or an equivariant realization. It does not produce moving exceptional middles or an affine dimension-eight example. Under the separately established global hypothesis that the rank-drop middle support has dimension at most two, the pointwise bound only yields the upper bound 2+3+3=8 on components generically of residual rank one. The isolated example shows sharpness of the pointwise bound, not sharpness of that global bound.

The inspected ../rank-one-trace-quadric-kernels/PROOF.md concerns four-spaces in sl(3) and is logically distinct. The construction below extends the method of ../rank-five-surface-countermodel/PROOF.md, with every changed dimension and dominance issue checked here.

## 1. Universal upper bound by diagonal extension

Write K=ker h for a nonzero quadratic functional h. Its square locus B={ [e]∈P(E):h(e²)=0 } has dimension two, even if h is degenerate or a square.

Suppose there is an integral fourfold Z⊂P(E)×P(E) whose dense open consists of compatible distinct pairs. Such a Z can be obtained by general ample sections if a larger compatible component exists. The product-membership equations hold on its closure, so Z∩Δ is contained in the diagonal copy of B. Consequently dim(Z∩Δ)≤2.

Also Z meets Δ. Indeed a general ample divisor section produces an integral projective threefold S⊂Z. In P³×P³ the diagonal class is H1³+H1²H2+H1H2²+H2³. All four mixed degrees on S are nonnegative, and at least one is positive because (H1+H2)³ has positive degree on S. Thus [S]·[Δ]>0, precluding disjointness.

Normalize ν:N→Z. The inverse image D of Z∩Δ is nonempty and has dimension at most two, since normalization is finite. Let Li=ν*O(1,0),ν*O(0,1). On N\D the two tautological lines are independent, so dense compatibility gives uniquely determined regular sections α of L2 and β of L1 with

    v(ab)=αa+βb.

The wedge equation is closed, so the identity is valid everywhere off D. Since D has codimension at least two in normal N, the sections extend across D. Their identity extends by density. At any point over Δ it implies v(e²)∈Ce, contradicting square avoidance. Thus a compatible fourfold cannot exist, proving dimension at most three.

This is the diagonal–Hartogs argument of ../diagonal-hartogs-fiber-bound/PROOF.md in one higher dimension. No genericity or classification of h is used in this upper bound.

## 2. Sharp generic nine-dimensional kernel

Choose h nondegenerate and set K=ker h. Put A=Hom(K,E), so dim A=36.

### 2.1 A general correction avoids every square

The square locus in P(E) is a smooth quadric surface B. For fixed [e]∈B, the condition v(e²)∈Ce has codimension three in A, since evaluation A→E is surjective. Its incidence over B is a rank-33 vector bundle and has dimension 2+33=35. Because B is projective, its image in A is closed and of dimension at most 35. The complement U_square is nonempty open.

### 2.2 The rank-two product locus

Let T={ [q]∈P(K): rank(q)=2 }. Its ordered factor cover is

    X°={ ([a],[b])∈P(E)×P(E): h(ab)=0, [a]≠[b] }.

The full hypersurface X={h(ab)=0} is a P²-bundle over P(E), since h is nondegenerate. It is smooth and irreducible of dimension five, and X° is nonempty open. Multiplication X°→T is a finite étale double cover, quotient by exchanging the two distinct factor lines. Indeed every rank-two symmetric tensor over C has exactly two ordered factorizations, and the factors vary étale-locally as the distinct roots of a nondegenerate binary quadratic. This also follows by restricting the usual quotient Sym²(P(E)) to distinct points. Therefore T is smooth, irreducible, and of dimension five.

### 2.3 Compatibility incidence and its dominance

On T let S⊂E⊗O_T be the rank-two subbundle im(q), and let Q=(E⊗O_T)/S, rank two. The universal compatibility incidence

    I={ ([q],v)∈T×A : v(q)∈im q }

is the total space of a rank-34 vector bundle over T: evaluation at q onto E/im q is surjective. Thus I is smooth irreducible and dim I=5+34=39.

To verify that I→A is dominant, fix [q0]∈T and choose two linearly independent tangent vectors ξ1,ξ2∈T_[q0]T. As T is a locally closed subvariety of P(K), their representatives δq1,δq2 in K are independent modulo Cq0. Choose v0∈A with v0(q0)=0 and with v0(δq1),v0(δq2) projecting to a basis of E/im q0. Extend these assignments linearly to K.

In local frames the compatibility equations are the two coordinates of v(q) modulo im q. At (q0,v0), differentiating the moving quotient introduces no extra term because v0(q0)=0. The derivatives in the ξ1,ξ2 directions therefore span the equation space. Hence every target infinitesimal variation of v can be compensated by a variation of q, so I→A has surjective differential there. Both spaces are smooth, and the projection is consequently smooth at that point and dominant.

Generic-fiber dimension and constructibility give a nonempty open U_three⊂A on which the fibers are nonempty of dimension 39−36=3. Intersecting U_three with U_square is allowed because A is irreducible. Fix v in this intersection. Its compatible tensor locus C_v has dimension three, as does its finite ordered-factor cover. The special v0 was only a witness to dominance and was not required to avoid squares.

## 3. Universal tensor operation and its repeated-input variety

Let V=Cu⊕E and

    W=ker(V⊗Λ²V → Λ³V),   dim W=40,
    f0(a,b,c)=a⊗(b∧c)+c⊗(b∧a).

Exterior multiplication shows f0 lands in W; it is outer symmetric and cyclic zero. Its repeated-input tensor is A0_a(b)=a⊗(a∧b). Let F_a be the image of Sym²V under bc↦f0(b,a,c). Splitting V=Ca⊕U shows dim F_a=4+10=14 and

    F_a/A0_a(V) ≅ Sym²(V/Ca),
    F_a⊂V⊗(a∧V).

The rank-one tensor variety in P(W) is

    R={ [a⊗(a∧b)] : a∧b≠0 }.

It is the closed flag variety of a line in a two-plane, dimension 4+3=7. To check exhaustiveness, a⊗β belongs to W precisely when a∧β=0; in a splitting this forces β=a∧b. A quotient kernel avoiding R preserves all repeated-input injections.

## 4. Prescribed nine-dimensional graph

Put B0_u(q)=f0(a,u,b) for q=ab and define

    L={ B0_u(q)−A0_u(v(q)) : q∈K }⊂F_u.

It has dimension nine, projects isomorphically to K in F_u/A0_u(V), and is disjoint from A0_u(V). With the convention ab=(a⊗b+b⊗a)/2 and contraction matrix M(q), its tensor matrix, in rows Cu⊕E and columns u∧E, is

    [ −v(q)^T ]
    [  2M(q)  ].

Its second-factor support is u∧(im q+Cv(q)). If rank q≥2, this support has dimension at least two. If rank q=1, square avoidance again gives dimension two. Therefore every nonzero tensor in L has tensor rank at least two, and P(L) avoids R.

Furthermore L∩F_a=0 for every [a]≠[u]. Otherwise its second-factor support, which contains independent u∧w1,u∧w2, would be contained in a∧V. This implies a∈span(u,w1)∩span(u,w2)=Cu, a contradiction. This argument applies to all nonzero q in K, not merely compatible rank-two q.

## 5. Completion to one fixed twenty-dimensional target

Set Wbar=W/L, dimension 31, and G=Gr(11,Wbar), dimension 11·20=220. An M∈G determines its inverse image Ktot⊂W of dimension twenty. We impose three nonempty open conditions.

First, avoid R. Projection of R from P(L) is a morphism with closed image Y⊂P(Wbar), dim Y≤7. For each line y, the 11-planes containing it form Gr(10,30), dimension 200. The incidence of M meeting Y has dimension at most 207<220 and is closed under projection. Its complement is nonempty open.

Second, require M∩(F_u/L)=0. The latter space has dimension five, and 11+5≤31, so disjointness is nonempty open. This is precisely Ktot∩F_u=L.

Third, avoid all other F_a simultaneously. On B=P(V)\{[u]}, their images H_a in Wbar form a rank-14 subbundle, because L∩F_a=0. The incidence of a∈B, [z]∈P(H_a), and M containing z has dimension

    4+13+200=217<220.

Its image is constructible; its closure still has dimension at most 217. Removing that closure gives a nonempty open on which Ktot∩F_a=0 for every [a]≠[u]. Taking the closure is necessary since B is not proper.

The irreducibility of G makes the intersection of these three opens nonempty. Choose such Ktot and put J=W/Ktot, dim J=20, and f=p∘f0. It preserves outer symmetry and cyclic zero, and avoidance of R proves repeated-input injectivity everywhere.

## 6. Exact ranks and zero-locus dimensions

Repeated-input injectivity and the universal F_a description give

    rank Q_a = dim p(F_a)−4
             = 10−dim(Ktot∩F_a).

Thus rank Q_u=1 and rank Q_a=10 at every other middle. At u the residual kernel is exactly K and the correction is exactly v, since p(B0_u(q))=p(A0_u(v(q))).

For independent a,b∈E, set q=ab and take outer lifts x=a+αu, z=b+βu. The exact zero equation is

    f(x,u,z)=A_u(v(q)+βa+αb).

A zero exists precisely when q∈K and v(q)∈span(a,b); the two lift coefficients are then unique. This identifies the separately projectivized independent-zero fiber with the finite ordered-factor cover of C_v, dimension three. No extra lift parameter appears. At other middles Q_a is injective and no independent zeros exist.

The entire separately projectivized independent-zero locus therefore has dimension three. Restoring the three independent nonzero input scales is a (G_m)³ torsor, so the affine independent-zero locus has dimension six. If an actual middle vector u rather than its line is fixed, only two outer scales remain and the affine fiber has dimension five.

Only abstract tensor algebra and generic incidence arguments were used.  All dimension assertions concern reduced supports; no scheme-theoretic rank-drop multiplicity or equivariance is claimed.
