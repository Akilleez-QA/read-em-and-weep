# Uniform lexicographic exclusion in the column third linear strand

## Claim and dependencies

For every nonzero column parameter lambda in the characteristic-zero family of PR511/513, the remaining parameter u=beta_{3,4}(A_lambda) satisfies

u in {0,5,10,15,20}.

In particular the previously permitted values 25,30,35,40 are impossible. No assertion is made that all five remaining values occur, or that u=0.

The pinned repository inputs are:

- PR511, commit 55bc80b2cb660edd741c93747df7304ee51a061e, which proves HF(A_lambda)=(1,5,5), uniformly for every nonzero lambda: https://github.com/Akilleez-QA/read-em-and-weep/blob/55bc80b2cb660edd741c93747df7304ee51a061e/research/hm/binary-symmetric-propagation/PROOF.md .
- PR513, commit df947c1ce092c0c59dcef187639147da8a7b2873, which proves that u is a multiple of five and gives the resolution template: https://github.com/Akilleez-QA/read-em-and-weep/blob/df947c1ce092c0c59dcef187639147da8a7b2873/research/hm/column-level-resolution/PROOF.md .

The new external dependency is the graded lexicographic Betti bound (Bigatti–Hulett–Pardue), together with the Eliahou–Kervaire formula. Both precise graded statements are recorded as Lemmas 2 and 3 of the research article *Graded Betti Numbers of Balanced Simplicial Complexes*, https://doi.org/10.1007/s40306-021-00449-8 . Bigatti's original characteristic-zero proof is at https://arxiv.org/abs/alg-geom/9205006 . We use these published theorems, not a newly claimed proof of them.

## Proof

Write S=k[x_1,...,x_5] and order variables x_1>...>x_5 lexicographically. Let L be the lex ideal with the same Hilbert function as A_lambda. Since there are no degree-one relations and exactly ten degree-two relations, its quadratic minimal generators are exactly

x_1^2, x_1x_2, x_1x_3, x_1x_4, x_1x_5,
x_2^2, x_2x_3, x_2x_4, x_2x_5, x_3^2.

Set L_d=S_d for d>=3. This indeed defines the required lex ideal: its degree-two complement consists of five monomials, and all higher degrees of its quotient vanish. Additional cubic minimal generators are allowed in this comparison ideal; no claim that L is quadratically generated is needed.

The graded lex bound gives beta_{3,4}(S/J_lambda)<=beta_{3,4}(S/L). For the latter Betti number only quadratic generators contribute to the Eliahou–Kervaire formula. If m(q) is the largest index of a variable dividing q, their m(q) values, in the displayed order, are

1,2,3,4,5,2,3,4,5,3.

Consequently

beta_{3,4}(S/L)
 = sum_q binom(m(q)-1,2)
 = 0+0+1+3+6+0+1+3+6+1
 = 21.

Thus u<=21. The center of the Heisenberg group acts on internal degree four by a nontrivial central character, so the relevant homology is a direct sum of five-dimensional irreducibles, as proved in PR513. Therefore 5 divides u. Combining this divisibility with nonnegativity and u<=21 proves the claim.

The comparison ideal is an auxiliary monomial ideal determined solely by the Hilbert function, not a selected actual HM/source instance. This argument performs no evaluation of the column tensor and no multiplication-matrix rank computation.

## Consequences for the next dependency

In the PR513 resolution template the ambiguous degree-four terms are now

F_2,degree4 = (5+u)S(-4), with multiplicity at most 25,
F_3,degree4 = uS(-4), with multiplicity at most 20.

The internal-degree-four Koszul differential

A_1 tensor Lambda^3(T) -> A_2 tensor Lambda^2(T)

has a 50-dimensional source and a five-dimensional incoming boundary space. Its rank is therefore 45-u, hence at least 25, rather than the earlier lower bound five. This is a theorem about every member of the family; it is not an evaluated matrix rank.

For the intrinsic comparison in PR516, the identity a=5+u-rho-sigma consequently gives rho+sigma<=25, using a>=0. The conditional discussion of u=40 forcing a>=5 has an impossible premise and can no longer describe any column. The new bound does not decide a, b, rho, sigma, cubic generation of the associated Gorenstein quotient, or the rank of its middle Tor map.

## Scope and verification

This is a new numerical exclusion obtained from a structural degeneration theorem and Heisenberg divisibility. It is not a reformulation of the earlier u<=40 bound. The ten-generator list and binomial sum are explicitly displayed for independent checking. No coefficient search, selected-instance calculation, or large computation is involved.

The uniform vanishing u=0 remains unproved. In particular this note does not supply injectivity modulo Koszul boundaries of the actual middle tensor. It makes no first-order, higher-order, or algebraicity conclusion about an actual selected HM/source instance. Status: authored proof awaiting independent review, not formally machine-checked.
