# Vertex local cohomology and the finite Hartogs repair

## Result and inputs

Work over C, and use the universal primary ideal Q of ../global-rank-one-primary-closure/PROOF.md. Set B=R/Q, C=R/P, N=P/Q, and let m denote the homogeneous vertex ideal (or its image in any module under discussion). The dimension is seven. The companion HILBERT.md proves the graded C-module identification

N = Γ_*(X,F),  X=P^4×P^2,  F=Ω_{P^4} ⊠ I_Z,

where twists mean O_X(d,d) and Z is the three coordinate points of P^2. This is the full section module in all integer degrees: the sections vanish below degree two. The identification is as a C-module, and does not assert a splitting of B over C.

Then:

- depth(B_m)=3.
- H^3_m(B) is C^2 in degree zero and zero in all other degrees.
- H^i_m(B)=0 for i=0,1,2,4,5.
- H^6_m(B) is nonzero in every degree d≤−4; its precise dimension is given below.
- B is not globally S2: its generic two-zero-column strata have codimension two and depth one.
- There is a canonical finite birational S2/Hartogs hull B^h, obtained by filling the missing nilpotents along those codimension-two strata. It is Cohen–Macaulay off the vertex, but has depth two at the vertex.
- Consequently there is no finite birational Cohen–Macaulay intermediate algebra in the total quotient algebra that agrees with B in codimension one. This assertion deliberately does not exclude extensions changing the codimension-one algebra or nonbirational finite extensions.

## 1. Cohomology of the factors

The Euler sequence on P^4 is

0 → Ω(d) → O(d−1)^5 → O(d) → 0.

Using the elementary cohomology of line bundles, the only nonzero cohomology of Ω(d) is:

- H^0 for d≥2, of dimension k_d=5 binom(d+3,4)−binom(d+4,4);
- H^1 for d=0, of dimension one;
- H^4 for d≤−4, of dimension a_d=5 binom(−d,4)−binom(−d−1,4).

For d≥1, surjectivity on H^0 in the Euler sequence is multiplication by the homogeneous coordinates. At d=0 its cokernel is C. In degree four, the map from H^4(O(d−1)^5) to H^4(O(d)) is surjective, either from the terminating long exact sequence or by dualizing the injective map of sections. These observations also verify all endpoints, notably H^4(Ω(−4))=C^5.

The sequence

0 → I_Z(d) → O_{P^2}(d) → O_Z(d) → 0

gives:

- H^0(I_Z(d)) has dimension binom(d+2,2)−3 for d≥1 (zero at d=1), and is zero for d≤0;
- H^1(I_Z(d)) has dimension 3 for d<0, dimension 2 for d=0, and is zero for d≥1;
- H^2(I_Z(d)) has dimension binom(−d−1,2) for d≤−3, and is zero otherwise.

Indeed evaluation at the coordinate points is an isomorphism for linear forms and is surjective in every positive degree, using the three pure powers. At degree zero it is the diagonal inclusion C→C^3.

## 2. Kunneth and the full section module

Kunneth now shows that the only nonzero higher cohomology of F(d,d) is

H^2(X,F)_0 = C^2,
H^5(X,F(d,d)) = H^4(P^4,Ω(d)) ⊗ C^3   (d≤−4),
H^6(X,F(d,d)) = H^4(P^4,Ω(d)) ⊗ H^2(P^2,O(d))   (d≤−4).

All other higher groups vanish. For example H^1 vanishes: the possible H^0Ω⊗H^1I_Z term has disjoint twist ranges, and H^1Ω⊗H^0I_Z vanishes because H^0I_Z(0)=0. The nonzero H^2 comes precisely from H^1Ω⊗H^1I_Z at twist zero.

For a finitely generated graded module over the Segre coordinate ring, the section/local-cohomology exact sequence and isomorphisms are

0 → H^0_m(N) → N → Γ_*(X,F) → H^1_m(N) → 0,
H^{i+1}_m(N)_d = H^i(X,F(d,d))  (i≥1).

The middle map is an isomorphism here by the full section-module identification, not merely by agreement in large degree. Hence H^0_m(N)=H^1_m(N)=0. Thus the complete list is

H^3_m(N)_0 = C^2,
dim H^6_m(N)_d = 3 a_d  (d≤−4),
dim H^7_m(N)_d = a_d binom(−d−1,2)  (d≤−4),

with every other graded component and local-cohomology degree zero.

## 3. Passing from the nilmodule to B without a splitting

The reduced Segre coordinate ring C is Cohen–Macaulay of dimension seven. This can also be checked directly: the same section-module argument for O_X and Kunneth give H^i_m(C)=0 for i<7. Its top group has

dim H^7_m(C)_d = binom(−d−1,4) binom(−d−1,2)  (d≤−5).

Use the exact sequence of R-modules

0 → N → B → C → 0.

No C-module structure on B is being chosen. Local cohomology is taken over the ambient polynomial ring R; for N and C it agrees with local cohomology for the Segre irrelevant ideal. Since both adjacent C-groups vanish, the long exact sequence gives canonical isomorphisms

H^i_m(N) ≅ H^i_m(B)  (0≤i≤6),

and a short exact sequence

0 → H^7_m(N) → H^7_m(B) → H^7_m(C) → 0.

In particular depth(B_m)=3. The top graded dimensions add, although no canonical splitting is claimed. The infinite-dimensional H^6_m(B) also shows that B_m is not generalized Cohen–Macaulay; this reflects the positive-dimensional non-CM locus through the vertex.

## 4. Global S2 failure

On a nonzero-column chart the proved local form is

A ⊕ (b,c)A^4,

with square-zero multiplication on the second summand and A regular. At the prime (b,c), the reduced local ring A_(b,c) is regular of dimension two and its maximal ideal has depth one. Thus B has depth one at a codimension-two point, and fails S2. This is consistent with depth three at the vertex: S2 must hold at every prime, not just at the closed homogeneous vertex.

## 5. Constructing and identifying the finite Hartogs hull

Put

N^h = Γ_*(X, Ω_{P^4} ⊠ O_{P^2}).

The inclusion I_Z→O yields N⊂N^h. These modules can be regarded concretely inside the universal square-zero parameter algebra: the degree-d part consists of r-degree-d multiples of p-linear u-polynomial covectors of u-degree d−1 annihilating u. The Euler/Koszul description identifies these covectors with H^0(Ω(d)). For N the r-polynomial lies in (r_1r_2,r_1r_3,r_2r_3); for N^h it is unrestricted.

Define B^h=B+N^h inside that parameter algebra. Since N^h is stable under the reduced Segre action and all its products with the nilpotent part vanish, this is an algebra. Its reduced quotient is C and its nilradical is exactly N^h:

0 → N^h → B^h → C → 0.

The module N^h is finitely generated over C, in fact by its degree-two part: the u-Koszul kernel is generated in degree two, and multiplication Sym^2(r) ⊗ Sym^{d−2}(r) → Sym^d(r) is surjective. Taking the independent u and r factors gives the asserted diagonal generation. Consequently B^h is finite over B. It is birational in the scheme-theoretic sense of having the same total quotient algebra: after inverting a nonzero rank-one coordinate on the locus with two nonzero columns, N=N^h, and hence B=B^h. More explicitly every element added lies in the localization of B at a reduced nonzero element, so B^h embeds in the total quotient algebra of B.

On every nonzero-column chart N^h replaces (b,c)A^4 by A^4. To see the extra generators directly on x_1≠0, the allowed pure r_1^2 multiples of u_1p_i−u_ip_1, divided by x_1^2, recover the four normalized transverse nilpotents. Thus

B^h|_(nonzero-column chart) = A ⊕ A^4

as a square-zero algebra. It is CM there. The inclusion B→B^h is an isomorphism outside the union of the three two-zero-column loci; this excluded union has codimension two and contains the vertex.

Kunneth for F^h=Ω⊠O shows that its only intermediate cohomology is

H^1(X,F^h)_0=C.

Its other nonzero higher cohomology is top degree six in negative twists. The full section-module property and the same local-cohomology exact sequence therefore give

H^2_m(B^h)_0=C,
H^i_m(B^h)=0 for i=0,1,3,4,5,6.

In particular depth(B^h_m)=2. Together with the CM nonvertex charts, this proves that B^h is S2 everywhere.

Let U be the complement in Spec B of the three two-zero-column loci (including their vertex), and regard it also as an open subset of Spec B^h. Thus U means at least two columns are nonzero; it is strictly larger than the all-three-columns-nonzero open. No claim here identifies its section algebra with the section algebra of that smaller open. Since B^h is S2 and the complement has codimension at least two, Hartogs extension for the structure sheaf gives

B^h = Γ(U,O_U).

Thus this finite algebra is the intrinsic Hartogs/S2 hull, independent of the parameter presentation. There is no assertion that its extension over C splits globally.

## 6. Precise finite CM obstruction

Suppose B→T is an injective finite extension inside the same total quotient algebra, with no new components or embedded torsion, and it agrees with B on an open subset containing every codimension-one point. If T were Cohen–Macaulay, it would be S2. Shrink that common open further by removing the two-zero-column loci, so that T and B^h agree there. The complements still have codimension at least two in these finite equidimensional algebras. Hartogs extension for S2 structure sheaves then identifies both T and B^h with the sections of their common open, inside the same total quotient algebra. Hence T=B^h. But B^h has vertex depth two rather than seven, a contradiction. This proves the asserted no-go statement without using normality or assuming the algebras reduced.

This is an obstruction to a finite birational repair preserving codimension-one data. It makes no claim about arbitrary finite extensions, nonbirational covers, or modifications of codimension-one nilpotent lattices. Nonfinite resolutions likewise lie outside the statement.

All calculations concern universal graded geometry. No source operations, actual input matrices, rank evaluations, or numerical instances were used.
