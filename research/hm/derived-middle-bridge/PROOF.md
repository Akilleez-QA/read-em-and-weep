# The derived intersection has no intermediate homology gaps

Work over C and forget one-dimensional equivariant determinant factors throughout. Put S=Sym(T), dim T=5, P=Sym(E tensor Sym^2 W), A=S^(2), and B=direct_sum_d Sym^d(E) tensor Sym^(2d)(W), as in PR540. P degree one corresponds to S degree two. Let O=direct_sum_d S_(2d+1), with its indicated P grading. Write T_i=Tor_i^P(A,B). Let M_i^a=H_i(C^a) denote the actual generalized Eagon--Northcott homology with PR507's S grading.

There are exact graded A-module identifications

T_i = direct_sum_d (M_i^0)_(2d),
(T_i)^vee = [direct_sum_d (M_(4-i)^8)_(2d+1)](7), 0<=i<=4.

These are module identifications, not only Euler identities. In particular all five T_i, including every intermediate T_1,T_2,T_3, are nonzero. More precisely there are nonnegative integers x,y such that their entire intermediate Hilbert functions are:

T_1: dimensions 10,225,x in P degrees 2,3,4;
T_2: dimensions 315+x,y in P degrees 4,5;
T_3: dimensions 91+y,85 in P degrees 5,6.

Every component not listed is zero. Thus length T_1>=235, length T_2>=315, and length T_3>=176. This does not determine x or y, and neither is identified with the separate parameter k in the minimal S resolution of Q.

## 1. Identify the complexes before using duality

Over P, use the universal 2 by 10 matrix of binary columns (-b_i,a_i),(-c_i,b_i), i=1,...,5. Its maximal-minor quotient is B scheme-theoretically by PR540. B is Cohen--Macaulay of dimension six, so the maximal-minor ideal has grade nine in the fifteen-variable regular ring P. The ordinary Eagon--Northcott complex C_P^0 is therefore a free resolution of B. Here the presentation source has shift -1, rather than the shift -2 used over S.

Base change P->S sends this universal matrix to the actual quadratic presentation. Consequently C_P^0 tensor_P S is exactly C_S^0, with polynomial degrees doubled on the free generators. S=A direct_sum O as a P-module, where O's degree d means S degree 2d+1. Taking its even summand commutes with kernels, images, and homology. It follows directly that T_i=(M_i^0)^(even), with the regrading claimed above. No flatness of P->A or P->S is asserted.

For the second identification, complementary chain duality gives

Hom_P(C_P^0,P) = C_P^8(10), with homological order reversed.

Since B is Cohen--Macaulay of codimension nine, the dual complex has cohomology only at its final cohomological position. Thus C_P^8 is a free resolution of a module N_8 satisfying

omega_B = N_8(-5).

This follows also from omega_B=Ext_P^9(B,P)(-15): the degree-ten shift from chain duality leaves the shift -5. In particular this exactness uses the proved universal grade-nine condition, never the false assertion that the actual five-variable specialization has grade nine.

Base changing C_P^8 to S computes M_i^8. Its odd summand gives Tor_i^P(O,N_8). PR540 identifies omega_A=O(-3). Its finite-length derived duality therefore becomes

(T_i)^vee = Tor_(4-i)^P(omega_A,omega_B)(15)
           = Tor_(4-i)^P(O,N_8)(7)
           = (M_(4-i)^8)^(odd)(7).

The shift is 15-3-5=7. All duals are graded vector-space duals, with M(s)_d=M_(d+s). These constructions respect the P action, hence the induced A action on T_i and its dual. Determinant orientations may be restored by retaining them in each canonical module; no equivariant trivialization is claimed here.

## 2. Entire intermediate support and two exact parameters

PR508 proves that M_3^8 starts in S degree at least seven. Complementary duality consequently bounds M_1^0 above by degree eight. Its first free term starts in degree four. PR508 and PR509 give dimensions 10 and 225 in degrees four and six. Taking the even part therefore gives all of T_1, with x=dim(M_1^0)_8>=0.

PR509 bounds M_2^0 to S degrees seven through ten. Its even part T_2 is thus supported only in P degrees four and five. Set y=dim(M_2^0)_10>=0.

The same reference bounds M_3^0 to S degrees nine through twelve. By PR508, its degree-twelve dimension is 85. Thus T_3 is supported in P degrees five and six, with its degree-six dimension exactly 85.

It remains to identify the degree-eight component of M_2^0 and the degree-ten component of M_3^0. These follow from two exact-degree Euler identities, not a numerical rank calculation.

The initial ordinary EN terms over S have ranks and shifts

S, 45S(-4), 240S(-6), 630S(-8), 1008S(-10).

In S degree eight the alternating free dimension is

495 - 45*70 + 240*15 - 630 = 315.

M_0^0=Q is zero there. M_3^0 starts in degree nine, and M_4^0 starts in degree thirteen: the latter follows from M_4^0=(Sym^8 H)^vee(-15) and the known concentration of Sym^8 H in degrees zero through two. Higher homology vanishes. Hence

315 = -dim(M_1^0)_8 + dim(M_2^0)_8,

so dim(M_2^0)_8=315+x.

In S degree ten the alternating free dimension is

1001 - 45*210 + 240*70 - 630*15 + 1008 = -91.

Here M_0^0,M_1^0,M_4^0 all vanish by the support already stated. Consequently

-91 = dim(M_2^0)_10 - dim(M_3^0)_10,

so dim(M_3^0)_10=91+y. This proves the complete displayed parametrization and every claimed lower bound. T_0=Q^(2) is nonzero; T_4 is nonzero by PR540. Thus the exact amplitude-four derived intersection has no missing homological degree.

As another useful translation of the canonical bridge, (M_1^8)_5 has dimension 91+y, so its previously unresolved degree-five dimension is at least 91; (M_2^8)_7 has dimension 315+x and (M_2^8)_5 has dimension y. These are translations under complementary duality, not a separate claim of further independent numerical information.

## 3. Scope and next missing map

The two parameters x and y encode specific remaining graded homology components, not an arbitrary rank of an evaluated matrix. The result upgrades the previous obstruction 'top Tor is nonzero' to an exact identification of the entire derived-intersection complex with the even ordinary EN defects, its odd canonical dual, and quantitative nonvanishing in every middle degree. Determining x or y still requires additional structure on the actual generalized differentials. Relative column Tor bundles cannot simply be substituted for the homology of the ten-column Koszul complex: these are different derived functors. No such substitution is used.

No selected actual HM/source-instance evaluation, numerical multiplication matrices or ranks, coefficient search, large computation, fixed-source first-order vanishing, higher-order lifting, or algebraicity claim occurs. This proof is authored and mathematically checked by its author against the displayed complexes; it awaits independent review and is not formally checked.

## Exact pinned dependencies

- PR540, determinantal-derived-excess, e19ff287ead83b2775cc6e861c291d73b3505b88: https://github.com/Akilleez-QA/read-em-and-weep/blob/e19ff287ead83b2775cc6e861c291d73b3505b88/research/hm/determinantal-derived-excess/PROOF.md
- PR507, generalized-en-defects, 87c9b317bd4b1116e63212a6d7ec2730486b2032: https://github.com/Akilleez-QA/read-em-and-weep/blob/87c9b317bd4b1116e63212a6d7ec2730486b2032/research/hm/generalized-en-defects/PROOF.md
- PR508, middle-defect-duality, a59d3dbfdad8b5516cd17c91890b669f2567bdb7: https://github.com/Akilleez-QA/read-em-and-weep/blob/a59d3dbfdad8b5516cd17c91890b669f2567bdb7/research/hm/middle-defect-duality/PROOF.md
- PR509, right-strand-injectivity, 721ad87b7a898f00f321707d2129279fea331523: https://github.com/Akilleez-QA/read-em-and-weep/blob/721ad87b7a898f00f321707d2129279fea331523/research/hm/right-strand-injectivity/PROOF.md
- PR494, higher-symmetric-powers, 72ab9a7524aef8c9d1c1fd989f8b0e83826dc916: https://github.com/Akilleez-QA/read-em-and-weep/blob/72ab9a7524aef8c9d1c1fd989f8b0e83826dc916/research/hm/higher-symmetric-powers/PROOF.md
- Public construction/reference: Andrew R. Kustin, Canonical complexes associated to a matrix, section 3, https://arxiv.org/abs/1509.04367 . The required grade-nine hypothesis is verified above for P, and explicitly not imposed on S.
