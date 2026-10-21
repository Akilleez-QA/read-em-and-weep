# Determinantal annihilation and the scalar-ideal layers of defect homology

## Setup and results

Work over a characteristic-zero field k. Let S=Sym(T), dim T=5, and let phi:S(-2)^10 -> S^2 be the established quadratic presentation of H. Put D=I_2(phi), I=Ann_S H, Q=S/D, R=S/I, and J=I/D, an ideal of Q. Let C^a (0<=a<=8) be the generalized Eagon–Northcott complexes in PR507, and write M_i^a=H_i(C^a). Graded duals use M^vee_d=Hom_k(M_(-d),k).

We prove:

1. Every M_i^a is annihilated by D, including the previously unresolved middle defects. The assertion is scheme-theoretic annihilation, not merely support on the determinantal locus.
2. For the positive top defect N=M_4^8=Q^vee(-15), suppressing the orientation line, the scalar ideal acts nontrivially and its exact image is

I N = (S/m^2)^vee(-15).

Its dimensions are 5 and 1 in degrees 14 and 15. Moreover 0:_N I=R^vee(-15)=Sym^2 H(-10). Thus N does not descend to an R-module.
3. The self-dual middle defect M=M_2^4 admits a canonical three-step filtration with R-module successive quotients

0 subset J M subset (0:_M J) subset M.

The outer layers are dual under total-degree-15 duality, and the central layer (0:_M J)/(J M) is itself nondegenerately self-dual. No symmetry type of its pairing is asserted.

The claims concern auxiliary graded-module defects. They do not establish original fixed-source vanishing, higher-order lifting, or algebraicity.

## 1. Universal nullhomotopies of maximal minors

Let P=k[z_(r,c)] be the polynomial ring on the twenty entries of a generic 2 by 10 matrix X. Give each z degree two. Denote by E^a the generalized Eagon–Northcott complex for X, with the normalization used for C^a. The generic maximal-minor ideal has grade nine, and the classical generic exactness theorem says E^a is a free resolution of its zeroth homology for 0<=a<=8. Its zeroth homology is P/I_2(X) for a=0 and Sym^a(coker X) for a>=1.

Every maximal minor delta of X annihilates this zeroth homology. For a=0 this is tautological. For a>=1, the adjugate identity for its selected 2 by 2 submatrix gives delta P^2 subset im X, so delta kills coker X and hence every positive symmetric power.

Multiplication by delta on E^a is therefore a lift of the zero endomorphism of the resolved module. It is chain homotopic to zero. For completeness, construct the homotopy inductively. Since delta on E_0 has image in ker(E_0 -> H_0), lift it through d_1 using projectivity of E_0. After constructing h_(i-1), the map delta id-h_(i-1)d_i lands in ker d_i=im d_(i+1), so lift it to h_i. At the final position the remaining map is zero because the last differential is injective. The lifts may be chosen homogeneous of internal degree four. Thus d h+h d=delta id.

For any 2 by 10 matrix over a k-algebra, its entries define a ring map out of P. Tensor the polynomial identity d h+h d=delta id along this map. Exactness need not survive tensoring, but the homotopy identity does. Consequently every specialized maximal minor annihilates every homology module of the specialized generalized complex. Applying this universal statement to phi proves D M_i^a=0.

This argument does not evaluate any selected coefficients or numerical rank. The generic exactness theorem is used only over the twenty-independent-variable ring, where its grade hypothesis holds. It is not incorrectly imposed on the five-variable presentation.

The same proof identifies M_i^a with Tor_i^P(H_0(E^a),S). The annihilation follows at chain level, not from an unjustified inference that equality of radicals gives equality of annihilators.

## 2. The exact nonzero scalar action on the canonical determinantal defect

The pinned excess-module result gives

J^2=0, Ann_S(J)=m^2, and Q/J=R.

Under the perfect evaluation pairing Q times Q^vee -> k, the orthogonal complement in Q of J Q^vee is Ann_Q(J). Indeed q is orthogonal precisely when every functional vanishes on jq for every j in J, equivalently jq=0 for every j. Since Ann_S(J)=m^2 and D subset m^2, Ann_Q(J)=m^2/D. Therefore

J Q^vee = (Q/Ann_Q(J))^vee = (S/m^2)^vee.

The equality means the canonical dual injection into Q^vee. After shifting by -15 and reinstating the one-dimensional orientation line Omega when desired,

I N=J N=(S/m^2)^vee(-15) tensor Omega.

This has five generators in degree 14, one-dimensional socle in degree 15, and annihilator m^2. In particular it is nonzero: the top positive homology N is genuinely a Q-module which is not an R-module.

Independently, a functional in Q^vee is killed by J exactly when it vanishes on J. Hence

0:_N I=(Q/J)^vee(-15) tensor Omega=R^vee(-15) tensor Omega.

Forgetting orientation and using Sym^2 H=R^vee(-5), this is Sym^2 H(-10), of length 64. The exact image I N has length six. These are different submodules: one is the common kernel of the ideal action, the other its generated image. No single linear operator with these kernel and image dimensions is being asserted. The quotient N/(0:_N I) is J^vee(-15), of length 30.

Thus replacing Q by R for all positive generalized defect modules is rigorously excluded. This exclusion is independent of the unresolved determinantal parameter k.

**Optimal common annihilator.** The intersection of Ann_S(M_i^a), over 0 <= a <= 8 and i > 0, is exactly D. Section 1 places D in every annihilator. Conversely N=M_4^8 is Q^vee(-15) tensor Omega, whose annihilator equals Ann_S(Q)=D: an element annihilates Q^vee if and only if every linear functional vanishes on its products with Q, equivalently it annihilates Q. Thus the intersection is contained in D. Zero homology terms have annihilator S and do not affect this intersection. In particular, D is the optimal uniform annihilator of positive generalized homology, not merely a sufficient one.

## 3. A self-dual scalar-layer filtration of the middle defect

Put M=M_2^4. PR507 gives an S-linear identification M with M^vee(-15) tensor Omega. Choose an orientation to view this as a perfect S-balanced bilinear pairing B; its nonzero graded pairings have degrees summing to 15. No symmetric or alternating assertion is needed. By Section 1, M is a Q-module.

Set A=J M and K=0:_M J. Because J^2=0, A subset K. S-balancedness and nondegeneracy imply both left and right orthogonal complements of A are K: for example B(jx,y)=B(x,jy), and vanishing for every x,j is equivalent to jy=0. Double orthogonality then identifies the orthogonal complements of K with A.

The pairing therefore descends to a nondegenerate S-balanced pairing on C=K/A. Since J K=0, C is an R-module. The outer layers A and M/K are perfect duals with total degree 15 and orientation Omega. In particular

length M = 2 length A + length C,

and, writing a_d=dim A_d and m_d=dim M_d,

dim C_d=m_d-a_d-a_(15-d).

These are actual module filtrations, not chosen direct-sum decompositions.

PR508 places M in degrees 5 through 10. Since J begins in degree three, A is supported in degrees 8 through 10; since m^2 J=0, m^2 A=0. Correspondingly M/K is supported in degrees 5 through 7. The central R-layer C remains self-dual in degrees 5 through 10. In particular a_10<=m_5, a_9<=m_6, and a_8<=m_7. These constraints isolate the possible failure of scalar descent in an upper-degree submodule killed by m^2. They do not determine the action ranks or imply that A vanishes.

## Sources and exact dependencies

The generic generalized Eagon–Northcott resolution theorem and its construction are standard; a public account is Andrew R. Kustin, “Canonical complexes associated to a matrix,” introduction, Section 3, and Theorem 8.4: https://arxiv.org/abs/1509.04367 . The new specialization argument above explicitly uses a nullhomotopy, not generic exactness after specialization.

- PR507, generalized homology reciprocity and N=Q^vee(-15): https://github.com/Akilleez-QA/read-em-and-weep/blob/87c9b317bd4b1116e63212a6d7ec2730486b2032/research/hm/generalized-en-defects/PROOF.md
- PR508, middle-defect support and nonvanishing: https://github.com/Akilleez-QA/read-em-and-weep/blob/a59d3dbfdad8b5516cd17c91890b669f2567bdb7/research/hm/middle-defect-duality/PROOF.md
- PR498, Ann_S(J)=m^2 and the excess module: https://github.com/Akilleez-QA/read-em-and-weep/blob/77018c2e6904a4ef9adfee5f2f48e49894b63fe9/research/hm/determinantal-excess-module/PROOF.md
- PR495, the square-zero extension Q of R: https://github.com/Akilleez-QA/read-em-and-weep/blob/b972aa22b72658b419e2c8948a56e0eec7f59e13/research/hm/fitting-thickening/PROOF.md
- PR491, Sym^2 H=R^vee(-5): https://github.com/Akilleez-QA/read-em-and-weep/blob/e9ed26058f69f3b96bdcdf920cb638e9dd68def8/research/hm/endomorphism-rigidity/INDEPENDENT-DERIVATION.md

Authored structural proof conditional on these pinned inputs; independent mathematical review is required before publication. Not formally checked. No selected HM/source-instance evaluation, numerical multiplication matrices or ranks, coefficient searches, or large computation were used.
