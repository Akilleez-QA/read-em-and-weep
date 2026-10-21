# Complete polarization of a primitive twist-three eigenquotient

## Inputs and scope

Work over C with the normalized Horrocks–Mumford bundle F on P4, a general smooth quadric Q, V=F|Q, E=V(3), and X=P_Q(E) in the quotient convention. Write H for the hyperplane class and L for O_X(1). Let T be an integral primitive twist-three eigenquotient divisor of class 2L−2H. On the common open where all fifty marked values are nonzero, the four ambient sections already generate L|T. No smoothness, normality, rational singularities, or canonical singularities of T is assumed.

The normalized monad and cohomology inputs are recorded in the immutable proof at commit d5d9bd997145b0ecf7d7bd659a19fb7845afb75f, research/hm/actual-primary-image-extension/PROOF.md, and in PR543's AMBIENT-BETA-SECONDARY-MAP.md. The original source is Decker, “Monads and cohomology modules of rank 2 vector bundles”, Compositio Mathematica 76 (1990), 7–17, especially pp.12–16:
https://www.numdam.org/article/CM_1990__76_1-2_7_0.pdf

These inputs give H0F(1)=0, H0F(3)=C4, dimensions H1F(1)=10 and H1F(3)=2, and H^iF(1)=H^iF(3)=0 for i≥2. The standard Heisenberg linearization makes the four sections of F(3) invariant.

## 1. Coefficient-free generic surjectivity in the remaining Rao degree

Put A_j=H1(P4,F(j)), and S=C[x0,...,x4]. The monad is

5O(−1) → 2Ω²(2) → 5O.

If K is its middle kernel, the two short exact sequences and the vanishing of intermediate cohomology of line bundles give, for every t≥0,

A_t = coker[H0(2Ω²(t+2)) → 5H0(O(t))].

Here H1(Ω²(t+2))=0 for t≥0, by the exterior Euler sequence. These identifications commute with multiplication. Thus the nonnegative graded Rao module is a quotient of 5S generated in degree zero. In particular S2·A1=A3.

Consider the linear space W of multiplication maps μ_q:A1→A3 for q∈S2. Suppose every map has rank at most one. A linear space of rank-at-most-one maps has either a common image line or a common kernel hyperplane. Indeed, write each nonzero map as v⊗α. Two such maps can have rank-at-most-one sum only if their image vectors or their covectors are dependent. If two image vectors are independent, their covectors coincide up to scale, and comparison with both forces every covector to be proportional. Otherwise all images share one line.

A common image line contradicts S2·A1=A3, since dim A3=2. In the other alternative, the common kernel K0 is a hyperplane of A1. The multiplication family is Heisenberg-equivariant, so its common kernel is stable, giving a one-dimensional Heisenberg quotient A1/K0.

This is impossible. The center acts trivially on F(3): the four invariant sections generate its fibers over a dense open, so the central bundle automorphism is the identity there and hence everywhere. Consequently it acts on F(1)=F(3)⊗O(−2), and therefore on A1, by a nontrivial fifth-root character. But the center of the order-125 Heisenberg group is its commutator subgroup and acts trivially on every one-dimensional representation. A1 has no one-dimensional quotient with its central character.

Therefore some μ_q has rank two. Quadratic equations whose multiplication map has rank two form a nonempty Zariski-open subset of the parameter space of all quadric equations. Intersecting with the smooth and previously established common-good opens is legitimate. This proves generic surjectivity, not surjectivity for every smooth quadric.

## 2. Exact complete cohomology

The restriction sequence

0 → F(1) --q--> F(3) → V(3) → 0

gives

0 → C4 → H0(V(3)) → C10 --μ_q--> C2 → H1(V(3)) → 0.

Thus for arbitrary q in the cohomological setup, if r=rank μ_q, then h0(V(3))=14−r and h1(V(3))=2−r, with higher cohomology zero. For a general Q, Section 1 proves

h^i(Q,V(3)) = (12,0,0,0).

On X, the restriction sequence for L has left term O_X(−L+2H), which is relatively acyclic because it has degree −1 on every projective-line fiber. Consequently

Rπ_*O_T(L)=V(3),

where π:T→Q. Hence, on the same common open,

h^i(T,O_T(L)) = (12,0,0,0).

In particular the four ambient sections are an incomplete subsystem. They cannot be used as the complete h0 in a Riemann–Roch or positivity argument.

## 3. Numerical verification without smoothness

The previously checked intersection numbers are L4=50, HL3=30, H²L²=10, H³L=2. Therefore L³|T=40. Since T is anticanonical and Cartier in smooth X, ω_T=O_T and c2^vir(T)=c2(X)|T. The projective-bundle tangent sequence gives c2(X)=6LH−11H², and therefore

c2^vir(T)·L = 12HL³−34H²L²+22H³L = 64.

The local-complete-intersection Riemann–Roch identity reads χ(O_T(L))=L³/6+c2^vir(T)·L/12=12, agreeing with the direct calculation. This uses virtual Chern classes and asserts nothing about the topological Chern numbers of a singular T.

## 4. New restriction on the complete polarization map

Because the four ambient sections generate L|T, its complete twelve-dimensional space of sections does also. Its morphism has nondegenerate integral three-dimensional image Y⊂P11: dimension three follows from L³=40>0. If δ is the generic degree, then

δ·deg(Y)=40.

The elementary minimum-degree bound for a nondegenerate integral projective variety gives deg(Y)≥codim(Y)+1=9. Hence δ≤4, and divisibility by 40 leaves only

(δ,deg(Y)) = (1,40), (2,20), or (4,10).

This is the complete-series map. It must not be confused with the degree-40 map to P3 defined by the four-dimensional ambient subsystem. No alternative here is asserted impossible.

## Boundary

The new conclusions are generic Rao surjectivity, exact complete polarization cohomology, and the three possible degrees of its complete-series morphism. They do not exclude primitive twist three or prove the full repair. No selected coefficients, rank samples, experiments, or external writes are used.
