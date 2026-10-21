# Generic cubic-alone coverage for the HM adjoint endpoint

Let F be the normalized Horrocks–Mumford bundle on complex P^4, B=End_0(F), and C its twenty-five transverse evaluation-degeneracy lines. There is a nonempty Zariski-open set Omega in P(H^0(O(3))) such that, for every v in Omega,

v:H^1(B(2)) -> H^1(B(5)) is surjective.

Consequently, simultaneously for EVERY quadratic u, including zero,
Q5(u,v)=H^1(B(5))/(uH^1(B(3))+vH^1(B(2)))=0,
P5^(2,1)(u,v)=H^1(B(5))/(u^2H^1(B(1))+vH^1(B(2)))=0.

No coprimality or good-quadratic assumption is needed. Membership of the original selected cubic in Omega is NOT established. Q4, actual-source membership, lifting and algebraicity remain separate.

The new argument combines primitive symmetry of the line arrangement with a proved optimal-partition lemma and the published generic-hyperplane theorem. It establishes cubic-alone coverage, rather than inferring squared-quotient vanishing from Q5=0.

## 1. The exact generic residual-defect formula

Put W=H^0(O(3)), of dimension35. For each component l, restriction W->H^0(O_l(3)) is onto; let U_l be the image of its dual in W*, of dimension4. For nonempty A in the index set E of lines, put

r(A)=dim(sum_(l in A) U_l), R=r(E)<=35,
tau=min_(partitions Pi of E) sum_(A in Pi)(r(A)-1).

Choose v restricting nontrivially to each component, an open condition. Write H_v=ker(v:W*->C). Global cubics whose restriction on each line is a scalar multiple of v form

F_v=(sum_l(U_l intersect H_v))^perp.

Indeed, U_l intersect H_v is exactly the annihilator of the line spanned by v|l in H^0(O_l(3)). The admissible scalar tuples identify with F_v/I_C(3). Dividing by diagonal constants then divides out the additional line represented by v, since v is not in I_C(3). Thus the residual multiplication defect is

R-1-dim(sum_l(U_l intersect H_v)).                 (1)

This uses the actual weighted-restriction transpose proved in PR457 and its restriction-kernel formulation in PR532. It does NOT assume that cubic restriction on C is injective, or assume the numerical dimension of H^1(B(2)).

Lovasz's generic-hyperplane theorem, in the form of Antolini–Dewar–Tanigawa Theorem2.10, states that for a generic hyperplane H in W*,

dim(sum_l(U_l intersect H))=tau.                   (2)

The hypotheses hold over C, and each U_l has positive dimension. Cubics parametrize all hyperplanes of W*, not a restricted family. Combining (1)-(2), the generic residual defect is R-1-tau. The theorem is imported and credited, not claimed as new.

## 2. A primitive-symmetry optimal-partition lemma

For a submodular rank function r, set f(A)=r(A)-1 for nonempty A. Optimal partitions minimize sum f. Their join is optimal, so they have a unique coarsest member.

Proof. For optimal partitions P,Q, take a block A of P and the disjoint blocks B_1,...,B_s of Q meeting A. Their union U contains A. Repeated intersecting submodularity gives

f(A)+sum_i f(B_i) >= f(U)+sum_i f(A intersect B_i).

To see the telescoping explicitly, at step i the intersection of A union B_1 union ... union B_(i-1) with B_i is A intersect B_i, which is nonempty. Optimality of Q under merging gives f(U)>=sum_i f(B_i); optimality of P under splitting A gives sum_i f(A intersect B_i)>=f(A). Therefore all inequalities are equalities. Merging the B_i preserves optimality. Repeating for every block of P produces P join Q. The finite join of all optimal partitions is their unique coarsest optimum.

A rank-preserving group fixes that coarsest partition. Under a primitive action on E it is either the one-block partition or the singleton partition. Hence, when singleton ranks all equal d,

tau=min{r(E)-1, |E|(d-1)}.                        (3)

This is a combinatorial deduction; no subset ranks were evaluated.

## 3. The normalizer action on the 25 HM lines is primitive

The primary HM paper describes H/Z=F_5^2 and the projective normalizer (H/Z) semidirect SL_2(F_5), with its natural conjugation action. The line configuration is normalizer-stable.

Here is a proof that the action on components is the corresponding affine two-transitive action. The paper's reversal iota:x(i)->x(-i) has a two-dimensional negative eigenspace. Its projectivization is the line i=r=0 of equation(3.6). Choose the SL_2 complement so that its central involution is projectively this reversal. Such a choice is possible: in the affine quotient every lift of -I is (a,-I), and all these are translation-conjugate because2 is invertible in F_5. The order-two lifts differ by no nontrivial order-five central scalar. The complement therefore preserves the negative eigenspace and its line l_0. Even if phrased projectively, the eigenspaces have unequal dimensions two and three and cannot be interchanged.

The stabilizer of l_0 in H/Z is an SL_2-invariant subgroup of F_5^2, hence either zero or the whole space. The latter would make the negative eigenspace a proper H-invariant vector subspace, contradicting irreducibility of the Schrödinger representation. Thus H/Z acts regularly on the orbit of l_0, of size25, which is all the components.

With l_0 as origin, the complement acts naturally on F_5^2 and transitively on its24 nonzero vectors. The affine action on the lines is therefore two-transitive and primitive. This uses the published group and line geometry, not an evaluated source matrix or selected multiplication.

## 4. Generic residual surjectivity

The normalizer permutes the U_l, so r is invariant under its primitive action. The singleton partition cost is25(4-1)=75, whereas the one-block cost is R-1<=34. Equation(3) gives tau=R-1. Therefore (1)-(2) give zero generic residual defect.

There is consequently a nonempty open of cubics for which the actual map
H^1(B(2))/P_2 -> H^1(B(5))/P_5
is surjective, where P_2 and P_5 are the natural primary cup images.

No cubic-restriction injectivity premise was used. The geometric residue interpretation still requires the transverse evaluation resolution, compatible determinant duality and primary monad cohomology. These are the explicit geometric inputs of PR532, not a substitution of universal generation for fixed-polynomial surjectivity.

## 5. Add primary coverage

Write A=V_1 and W' for the primary two-dimensional quotient representation. Primary HM cohomology gives M_0=H^1F=A*, M_3=H^1F(3)=W'. The dual of primary Lemma3.3(vi) gives

S_3=A tensor (J_5 directsum W'),
Hom(M_0,M_3)=A tensor W'.

The target is irreducible for the full normalizer and occurs with multiplicity one. The actual cubic multiplication is equivariant and nonzero: primary degree-zero generation gives S_3 M_0=M_3. Thus it is the onto projection to A tensor W', up to an invertible scalar. This is the primary projection already established in PR462; the argument and published inputs are retained here.

The rank-two locus in Hom(M_0,M_3) is nonempty open, so its inverse image is a nonempty open of cubics. Intersect it with the residual-good open from Section4. Projective cubic space is irreducible, so their intersection Omega is nonempty.

Naturality of the primary cup maps gives a diagram of exact rows
0->P_2->H^1(B(2))->N_2->0,
0->P_5->H^1(B(5))->N_5->0,
with vertical multiplication by v. For v in Omega the first map is onto because v:M_0->M_3 is onto; the third map is onto by Section4. Lifting a residual target and then lifting the primary remainder proves surjectivity of the middle map. This proves the stated cubic-alone theorem.

## 6. Consequences and boundaries

Since vH^1(B(2)) already equals H^1(B(5)), adjoining ANY quadratic or squared-quadratic contribution leaves a zero quotient. This proves both displayed quotients simultaneously, without a condition on u.

This does not contradict PR530's warning: Q5=0 alone need not imply P5^(2,1)=0. The stronger cubic-alone coverage is what proves both here. In K_j=H^1(B(j-1)) notation the same target is K_6, so the indices match PR530/535.

The result strengthens generic independent-pair vanishing: one cubic open works for every quadratic, with the HM bundle fixed. It does not show that the original invariant cubic belongs to the open, give a numerical failure-locus bound, settle Q4, evaluate a source class, or prove a lift or algebraicity. No selected coefficient, matrix or rank evaluation, parameter search, or experiment was performed. This is mathematical reasoning, not formal verification.

## Sources

- Horrocks–Mumford (1973), Sections1 and3, equation(3.6), primary cohomology and Lemma3.3:
https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf
- Antolini, Dewar, Tanigawa, Dilworth truncations and Hadamard products of linear spaces, arXiv2508.04798v1, Theorem2.10 (generic-hyperplane theorem credited to Lovasz; AppendixA supplies a proof):
https://arxiv.org/pdf/2508.04798v1
- PR532, restriction-kernel residue model:
https://github.com/Akilleez-QA/read-em-and-weep/blob/5f08a072fa8d3bdf12007a6aab2f374c85c5e503/research/hm/residue-restriction-ambiguity/PROOF.md
- PR457, actual multiplication transpose:
https://github.com/Akilleez-QA/read-em-and-weep/blob/961694c4f3c805f0d58508811a42da4030dce7a6/research/hm/fixed-cubic-interpolation/PROOF.md
- PR462, primary cubic projection:
https://github.com/Akilleez-QA/read-em-and-weep/blob/a10049b8f7c57f30476c6f9c5554685583ea8c1b/research/hm/primary-pair-failure/PROOF.md
- PR530, square-versus-linear distinction:
https://github.com/Akilleez-QA/read-em-and-weep/blob/fe7a4cec04bf2ddb7e77d22109345c4ac66eda90/research/hm/square-quotient-colon-comparison/PROOF.md
