# The degree-seven residual spinor defect is supported on the vertex line

## Result

Under the actual saturated spinor filtration and reduced-conic first-jet theorem, the complete defect has the canonical disjoint-support decomposition

    T = i_* O_C0(5) direct-sum T_L,
    Supp(T_L) = L,
    chi(T_L(t)) = 7t+21,
    h0(T_L)=21, H1(T_L)=0.

Its one-cycle is exactly

    [T]_1 = [C0] + 7[L].

Thus T_L has generic length seven along L. The statement concerns set-theoretic support and the exact cycle: T_L may live on a nonreduced neighborhood of L. The independent depth-lemma proof in INVARIANT-CONE-RESIDUAL-DEFECT-PUSHFORWARD.md shows that it is pure, with no zero-dimensional subsheaf or associated component. It is not asserted to be a rank-seven vector bundle on the reduced line, or to come from a global ideal tensored with S(2).

The new ingredients are an equivariant degree-seven curve-support lemma and the local complete-intersection argument excluding isolated defect away from the vertex. No actual multiplication coefficient, matrix, rank test, or experiment is used.

## 1. Exact inputs

Let G=SL2(F5), with center Z={1,z}. It acts on the ambient five-space as V direct-sum W, where V and W are nonisomorphic irreducibles of dimensions three and two, and z acts respectively as +1 and -1. The invariant rank-three quadric Q0 has fixed loci

    C0=Q0 intersect P(V), a smooth conic,
    L=P(W), its vertex line.

They are disjoint. The cone is smooth off L. The group G is perfect, G/Z=A5, and z is its unique involution. Indeed a nonidentity order-two matrix in SL2(F5) has both eigenvalues -1 and is -I. The only proper normal subgroups of G are 1 and Z: a normal subgroup projecting onto A5 would either be G or define a quotient of order two, the latter impossible by perfectness.

The established actual filtration is

    0 -> S -> E -> J -> 0,
    E=F_Q0(2), J torsion-free of rank one, J**=S(2),
    T=S(2)/J.

It is equivariant and saturated. The first-jet theorem identifies its defect near C0 with i_*O_C0(5), and gives the canonical decomposition

    T=i_*O_C0(5) direct-sum T',
    Supp(T') intersect C0 is empty,
    chi(T'(t))=7t+21, h0(T')=21, H1(T')=0.

All degrees below are ordinary projective degrees with respect to O_Q0(1). In particular deg C0=2 and deg L=1.

## 2. Parity for a center-stable curve disjoint from C0

Let C be an integral projective curve in Q0, disjoint from C0, stable under z, and different from L. The two negative linear coordinates u,v have no common zero on C, because their common-zero locus on Q0 is C0. They give a morphism

    psi:C -> L=P(W).

On the normalization C_tilde, the pullback of O_L(1) is O_C(1) pulled back to C_tilde. This line bundle has positive degree deg C, so psi is nonconstant and finite, and

    deg psi = deg C.

The involution z is trivial on L but nontrivial on C. If it were trivial on C, then C would be contained in the fixed locus C0 union L, contrary to the hypotheses. Hence psi on C_tilde factors through the degree-two quotient by z. It follows that

    deg C is even.                               (1)

This uses a morphism without base points; no degree correction at a vertex intersection is omitted. The projection from the negative coordinates remains defined at points of C intersect L.

## 3. Small component orbits cannot occur

Let D be a G-invariant effective one-cycle of degree at most seven whose support is disjoint from C0. Consider an orbit of its irreducible components, with orbit size k and common component degree e. Orbit multiplicities are positive and constant, so k e<=7. Also k divides 120 by orbit-stabilizer.

The only candidates k<=7 are 1,2,3,4,5,6. A nontrivial action of the perfect group G on at most four objects is impossible because S4 is solvable. Thus

    k is 1,5,or6.                                 (2)

If k=5 or6, the component stabilizer has order24 or20. By Cauchy's theorem it contains an involution, which must be z. Each component is therefore center-stable. Such an orbit cannot contain L, since L is G-stable. By (1), every component has even degree at least two. This gives total orbit degree at least10 or12, contradicting deg D<=7.

Consequently every component of D is individually G-stable.

## 4. An invariant nonvertex component would have impossible small genus

Suppose a component C is G-stable and C!=L. Its degree is even by (1), and is at most six. Its linear span is a G-stable projective subspace of P(V direct-sum W). Complete reducibility and the nonisomorphic irreducible factors imply that the only nonempty proper choices are P(V) and P(W). The first would put C inside C0, and the second would give C=L. Thus C spans P4.

Castelnuovo's bound for an integral nondegenerate curve of degree d in P4 is

    g(C_tilde) <= 3 m(m-1)/2 + m epsilon,
    d-1=3m+epsilon, 0<=epsilon<=2.

For d<=6 this is at most two. A verified primary source for the bound and the general-hyperplane-section proof is Joe Harris, "A Bound on the Geometric Genus of Projective Varieties," Annali della Scuola Normale Superiore di Pisa, series 4, volume 8 (1981), pages 35-68, Section 1, especially pages 36-40: [original paper](https://www.numdam.org/article/ASNSP_1981_4_8_1_35_0.pdf). Here the geometric genus is bounded by the arithmetic genus even if C is singular. No smoothness, rationality, or linear normality of C is assumed.

Only this small-degree consequence is needed, and it also has a shorter proof. On the normalization put M=nu*O_C(1). Nondegeneracy gives five independent sections, so h0(M)>=5, while deg M=d<=6. If M were special, Clifford's inequality would give h0(M)<=d/2+1<=4, a contradiction. Thus h1(M)=0, and Riemann-Roch gives g=d+1-h0(M)<=d-4<=2. This proves the required genus bound without the full Castelnuovo formula.

The G action on C_tilde is faithful. Its kernel is normal in G, and cannot contain z because z acts nontrivially on C. The normal-subgroup statement in Section 1 leaves only the trivial kernel.

A faithful action of G on a smooth projective curve of genus at most two is impossible:

- Genus zero: the central involution would embed as a nonidentity involution in PGL2. Its centralizer is the normalizer of a one-dimensional torus, hence is solvable. The image of the perfect nontrivial group G cannot lie in that solvable centralizer.
- Genus one: after choosing an origin, the automorphism group is an extension of the abelian translation group by a finite cyclic group. Any homomorphism from the perfect group G to this abelian-by-cyclic group is trivial.
- Genus two: Hurwitz's bound gives |Aut(C_tilde)|<=84(g-1)=84, smaller than |G|=120.

This contradiction proves the support lemma:

    Every G-invariant effective one-cycle of degree <=7,
    disjoint from C0, is supported on L.           (3)

This is a geometric consequence of equivariance and degree, not an assumption that the components are rational.

## 5. Isolated defect off L is also impossible

Apply (3) to the one-cycle of T'. Its curve support lies on L, with total multiplicity seven. It remains essential to exclude isolated zero-dimensional support away from L; a cycle calculation alone would not do so.

On U=Q0 minus L, the sheaves S and S(2) are line bundles and E is a rank-two vector bundle. Locally trivialize them. The inclusion S->E is then a pair of functions (f,g) in a regular local ring. Saturation implies that f,g have no common height-one factor, because otherwise the cokernel J would have torsion along a divisor.

At a zero, the ideal (f,g) has height at most two by the principal ideal theorem, and at least two by saturation. It therefore has height two and is a regular sequence. The wedge map identifies the local quotient J with (f,g), its reflexive hull with the ring, and T with the complete-intersection quotient by (f,g), tensored with the local target line. Thus T|_U is a Cohen-Macaulay one-dimensional complete-intersection sheaf wherever it is nonzero. In particular it has neither isolated nor embedded point support there.

Near C0 the reduced-conic theorem already identifies T exactly with i_*O_C0(5). Elsewhere off L, any nonzero stalk of T' would therefore lie on a curve component off L, contradicting (3). Hence

    Supp(T') is contained in L.

Its positive degree seven makes its support exactly L. Set T_L=T'. The companion global MCM/depth argument independently excludes isolated and embedded zero-dimensional support even on L; the local argument above is sufficient for the support identification and does not require that stronger input. All Hilbert and cohomology assertions in the opening statement follow from the already exact first-jet subtraction. Since C0 and L are disjoint, the decomposition is canonical.

## Scope and dependencies

The actual filtration, Hilbert polynomial and cohomology are proved in INVARIANT-CONE-SPINOR-FILTRATION-AND-NILPOTENT.md. The reduced-conic theorem and exact degree-seven subtraction are in INVARIANT-CONE-CONIC-FIRST-JET-AND-RESIDUAL-DEFECT.md. This note determines the remaining set-theoretic support and cycle, while preserving all possible non-Cartier and infinitesimal behavior at L.

It does not prove the positive rank33 objective or exclude positive adjoint sections that fail to commute with the canonical nilpotent. Those questions require additional control of the vertex-supported sheaf or the filtration extension.

The companion verifier checks the finite orbit-degree possibilities, the parity exclusions, the relevant Castelnuovo values, the Hurwitz inequality, and the exact Hilbert/cohomology subtraction. It does not inspect any actual HM map.
