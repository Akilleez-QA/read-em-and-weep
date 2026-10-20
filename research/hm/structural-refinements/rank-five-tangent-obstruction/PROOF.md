> Scope: read CURRENT-SCOPE.md and DEPENDENCIES.json with this complete historical derivation. Historical open-case wording is qualified there.

# A fixed global quotient defeats the first-order tangent-dimension bound

## Result and scope

Over C there exists one fixed outer-symmetric, cyclic-zero operation

    f: V × V × V → J,    dim V=5, dim J=20,

such that every repeated-input map A_a:V/Ca→J is injective, and at a specified middle line [u]:

1. rank Q_u=5;
2. ker Q_u is the tracefree symmetric-square hyperplane on a nondegenerate ternary support;
3. the independent-zero fiber has projective dimension exactly two;
4. the Zariski tangent space to the determinantal middle locus {rank Q≤5} contains a two-dimensional plane.

Thus the stated hypotheses do not imply that the kernel of the first-variation obstruction has dimension at most one, even for a single globally defined operation with global repeated-input injectivity. This is a synthetic quotient countermodel to that particular tangent-bound strategy. It does NOT construct a reduced middle surface, prove that the tangent directions integrate, or control the dimension of the entire rank-drop support. It leaves stronger arguments involving the good-stratum support/metric equations or higher-order integrability open.

 

## 1. Universal tensor space and a good kernel graph

Use the universal operation from [rank-five-surface-countermodel](https://github.com/Akilleez-QA/read-em-and-weep/blob/9f4af00ab7ba91719a3f4d91ec4c1f71c12d96c4/research/hm/universal-polar/rank-five-surface-countermodel/PROOF.md):

    W=ker(V⊗Λ²V→Λ³V),       dim W=40,
    f0(a,b,c)=a⊗(b∧c)+c⊗(b∧a).

Write B_a:Sym²V→W for B_a(bc)=f0(b,a,c), and F_a=im B_a. The established universal identities give

    ker B_a=Ca²,   dim F_a=14,
    A0_a(b)=a⊗(a∧b).

The projective repeated-input tensor variety

    X={ [a⊗(a∧b)] : a∧b≠0 }⊂P(W)

is closed of dimension seven. A quotient whose projective kernel avoids X preserves every repeated-input injection simultaneously.

Fix a splitting

    V=Cu⊕E0⊕Cz,       dim E0=3,

a nondegenerate form h on E0, and K=ker(h:Sym²E0→C), of dimension five. Choose v:K→E0 with

    v(e²)∉Ce for every nonzero e²∈K,

and whose compatible rank-two locus { [q] : rank q=2, v(q)∈im q } has dimension exactly two. Existence of such a v is proved by the two intersecting nonempty-open arguments in Sections 2.1–2.2 of the cited countermodel. Those arguments are entirely independent of the quotient constructed here.

Set

    L={B_u(q)−A0_u(v(q)):q∈K}⊂F_u.

Then dim L=5 and P(L)∩X is empty. Indeed the second-factor support of a nonzero graph tensor is

    u∧(im q+Cv(q)),

which has dimension at least two: for symmetric rank at least two this is immediate, and for a square it follows from square avoidance. A repeated-input tensor has second-factor support of dimension one.

## 2. An injective two-plane of universal first variations

Choose e∈E0 with h(e,e)≠0 and put

    D=span(e,z)⊂V/Cu.

For ξ∈D and q∈K define

    d(ξ,q)=B_ξ(q)−f0(u,ξ,v(q)).

This is precisely the variation of the full middle-linear map on the fixed kernel vector q−u v(q). Let π:W→W/F_u. We claim that

    d_bar:D⊗K→W/F_u,    ξ⊗q↦π(d(ξ,q))

is injective, so its image S has dimension ten.

To see this, project W to its component containing no u, using V=Cu⊕E with E=E0⊕Cz. Every element of F_u and every correction f0(u,ξ,v(q)) projects to zero. Thus a relation in d_bar gives

    B_e(q_e)+B_z(q_z)=0 in W(E).

The first summand lies in E0⊗Λ²E0; the second lies in E0⊗(z∧E0). These are disjoint summands of E⊗Λ²E. Hence both vanish. The map B_z restricted to Sym²E0 is injective by the universal middle-map formula. The kernel of B_e on Sym²E0 is Ce². Since e²∉K by h(e,e)≠0, q_e=q_z=0. This proves the claim without specifying any tensor entries.

## 3. A lifting lemma that avoids the entire repeated-input variety

Let R=F_u/L, of dimension nine. There is an exact sequence

    0→R→π^{-1}(S)/L→S→0.

Its linear splittings form an affine space A modeled on Hom(S,R), of dimension 10·9=90. Each splitting defines a fifteen-dimensional subspace N⊂W such that

    L⊂N,    N∩F_u=L,    π(N)=S.

We prove that a nonempty open subset of these splittings has P(N)∩X empty.

No point of X∩P(F_u) can belong to P(N), since N∩F_u=L and P(L) avoids X. For x∈X\P(F_u), membership in P(N) is possible only if π(x)∈P(S). For such an x, choose a nonzero representative w and let s=π(w). Its class modulo L lies over s. The condition that a splitting σ contain x is exactly

    σ(s)=w mod L.

It imposes nine independent affine linear conditions on A: evaluation Hom(S,R)→R at nonzero s is surjective. The condition is independent of the chosen scalar representative.

The eligible points x form a locally closed subset of X of dimension at most seven. Therefore the bad incidence has dimension at most

    7+(90−9)=88<90.

Its image in A is constructible with closure of dimension at most 88. The complement of that closure is nonempty open and every splitting in it has P(N)∩X empty. Properness of the eligible subset is not needed; taking the closure of its incidence image is essential.

Fix such an N. By construction, for all ξ∈D and q∈K,

    d(ξ,q)∈N+F_u.                                      (1)

The nine-dimensional freedom F_u/L is the decisive feature: containing a prescribed repeated-input point costs nine conditions, more than the seven-dimensional family of all such points.

## 4. Extend to a twenty-dimensional quotient kernel

Put W'=W/N, of dimension 25. Choose a five-dimensional subspace M'⊂W', and let M⊂W be its inverse image. Then dim M=20 and N⊂M.

Two nonempty open conditions on Gr(5,25) can be imposed simultaneously:

(a) M' avoids the nine-dimensional image of F_u. This is possible because 5+9≤25 and is equivalent to M∩F_u=L.

(b) P(M) avoids X. Since P(N) avoids X, projection defines a morphism X→P(W'); its image Y is closed and has dimension at most seven. For a fixed point y∈P(W'), the five-planes containing its line have dimension

    dim Gr(4,24)=80,

whereas dim Gr(5,25)=100. The incidence over Y thus has dimension at most 87<100; its proper image is a closed proper subset. Its complement gives (b).

The Grassmannian is irreducible, so the two nonempty opens intersect. Choose M there and set

    J=W/M,    f=p∘f0.

This is one fixed global operation, not a family of unrelated corrections. Outer symmetry and cyclic zero descend. Condition (b) gives global repeated-input injectivity. Condition (a) gives

    rank Q_u=10−dim(M∩F_u)=5,
    ker Q_u=K,
    B_u(q)=A_u(v(q)) for q∈K.

The compatible-rank-two reconstruction in Sections 6–7 of the cited countermodel applies unchanged. Consequently the independent-zero fiber at [u] has dimension exactly two, and [u] has all the required good pointwise properties.

## 5. Verification of the two-dimensional tangent plane

Let I_u=p(F_u), of dimension nine. The full middle-linear map

    Φ_a:Sym²V→J,    bc↦f(b,a,c)

has image containing im A_a of dimension four for every a. Thus its rank≤9 locus is exactly the residual rank≤5 locus. At u,

    ker Φ_u=Cu²⊕{q−u v(q):q∈K}.

For a determinantal rank≤9 locus at a point of rank exactly nine, the Zariski tangent condition in direction ξ is that the variation of Φ carry its kernel into its image.

On the kernel vector u² the variation is

    f(u,ξ,u)=−2A_u(ξ)∈I_u.

On q−u v(q), it is p(d(ξ,q)). Equation (1), together with N⊂M, gives

    p(d(ξ,q))∈p(F_u)=I_u

for every ξ∈D and q∈K. Hence

    D⊂T_[u]{rank Q≤5},       dim D=2.

Equivalently, the first-variation obstruction from the question vanishes identically on D:

    [f(q,ξ)−f(u,ξ,v(q))]=0 in J/I_u.

Cyclic zero changes this to [f(q,ξ)+f(u,v(q),ξ)]=0 because the difference is a full-middle-image term. This also checks the sign convention against the derivative of the repeated-input correction.

## 6. Exact limitation and relation to the boundary results

The countermodel rules out a universal assertion that the rank≤5 determinantal tangent space is at most one-dimensional at every good point under outer symmetry, cyclic zero, and global repeated-input injectivity. Unlike free metric/correction examples, the model is realized by one fixed quotient of the universal forty-dimensional tensor space with twenty-dimensional target.

It does not show that the chosen two-plane is tangent to a reduced surface, that nearby kernels stay supported on ternary spaces, or that nearby fibers remain two-dimensional. The rank≤5 scheme could have obstructed tangent directions or nonreduced structure. No claim about generic residual rank or the global rank-drop-support dimension is made.

Accordingly, the canonical-complement boundary theorem, full-flag divisor theorem, and metric-discriminant localization theorem are not contradicted. They concern an actual good-general middle surface. A successful exclusion may use those global constraints, the infinitesimal equations preserving ternary support and its correction, or integrability beyond the displayed first-variation test. The present result proves that the displayed tangent test alone cannot supply the proposed universal dimension bound.
