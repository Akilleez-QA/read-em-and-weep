# Reducing the remaining column alternative to one quadratic channel

## Inputs and statement

Work over C with the actual normalizer action and parameter line P=P(W'^*). Use [PR526, commit c887d466428bced729a73bbc8578a889e9ecaf45](https://github.com/Akilleez-QA/read-em-and-weep/blob/c887d466428bced729a73bbc8578a889e9ecaf45/research/hm/column-parity-blocks/PROOF.md). The entire column kernel is the kernel of

beta:R6 tensor O -> (W0 + Qspin) tensor O(2),

where R6 is the six-dimensional odd irreducible of G=SL2(F5), W0 is the other binary two-dimensional irreducible, and Qspin=Sym3(W') is the odd four-dimensional irreducible. The column parameter is u(lambda)=5 dim ker(beta_lambda). Its determinant is an invariant section of O(12).

[PR523, commit d02ae6cb6d324bad2b858c6969ed4ce8d43b5e42](https://github.com/Akilleez-QA/read-em-and-weep/blob/d02ae6cb6d324bad2b858c6969ed4ce8d43b5e42/research/hm/column-kernel-vanishing/PROOF.md) proves that every splitting summand of K=ker(beta) has degree at most -3, and eliminates all positive-generic jumps. [PR525, commit 2a33ad1d88f446fe42d5dd986a0f33e2c24e44e9](https://github.com/Akilleez-QA/read-em-and-weep/blob/2a33ad1d88f446fe42d5dd986a0f33e2c24e44e9/research/hm/column-extreme-exclusion/PROOF.md) gives the uniform bound u<=10. Thus the remaining alternatives are constant zero, five or ten, or zero away from the reduced twelve-point orbit Omega and five on it. Constant zero is already impossible for beta: its determinant would be a nowhere-vanishing section of O(12).

The representation facts used below are the binary icosahedral table and symmetric-power identities of [Horrocks--Mumford (1973), Sections 2--3 and appendix](https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf): G is perfect, its two-dimensional irreducibles are odd, Sym3(W')=Qspin, Sym5(W')=R6, Sym1(W')=W', and W0 tensor Sym2(W')=R6. Also Sym2(W') tensor W'=W'+Qspin.

We prove:

1. Constant u=5 is impossible.
2. Constant u=10 holds if and only if the W0 projection gamma of beta is identically zero.
3. If gamma is nonzero, det(beta) is nonzero, and the actual column parameter is zero off Omega and five on Omega.

No nonvanishing of the actual gamma scalar is assumed or established here.

## 1. Excluding constant u=5

Suppose u=5 everywhere. Then beta has constant rank five. Its kernel is a G-equivariant line bundle K=O(-d), with d>=3 by PR523. Its image J is a rank-five subbundle of 6O(2), so deg J=d<=10. Its cokernel is therefore the line bundle O(12-d).

Line-bundle linearizations differ from the standard one by a character of G, and G is perfect. Thus they have no character ambiguity. The central involution acts as -1 on R6 and trivially on the parameter base. Since it acts on O(-d) by (-1)^d, d must be odd. The possibilities are d=3,5,7,9. The case d=3 is impossible because an equivariant inclusion O(-3)->R6 tensor O would require R6 in Sym3(W'), which is Qspin.

The equivariant quotient map

(W0+Qspin) tensor O(2) -> O(12-d)

requires a nonzero intertwiner from W0+Qspin to Sym^(10-d)(W'). For d=5 this symmetric power is R6, and for d=9 it is W'. Neither contains W0 or Qspin. Consequently d=7 is the only remaining possibility.

For d=7 the quotient is a nonzero scalar multiple of the standard cubic evaluation on Qspin=Sym3(W'), and is zero on W0. The standard binary evaluation sequence is

0 -> Sym2(W') tensor O(-1) -> Sym3(W') tensor O -> O(3) -> 0.

It can be proved directly by multiplying a binary quadratic by the tautological annihilating linear form. Twisting by O(2) shows that the kernel of the quotient is

J = W0 tensor O(2) direct sum U' tensor O(1),

where U'=Sym2(W'). Hence

H0(J)=R6 direct sum W' direct sum Qspin.

The surjective map R6 tensor O -> J induced by beta is equivariant. Its induced map on global sections lands in the sole R6 summand of H0(J), which is precisely H0(W0 tensor O(2)). Equivalently, there is no equivariant morphism from R6 tensor O to U' tensor O(1). The map therefore has image inside the rank-two summand W0 tensor O(2), contradicting its required rank five. This excludes constant u=5.

## 2. Characterizing constant u=10

Suppose u=10 everywhere. Then beta has constant rank four and K has rank two. Write its splitting degrees as d1<=d2. The preceding vanishing gives d1,d2>=3, while deg(im beta)=d1+d2<=8. Thus the only possibilities are (3,3), (3,4), (3,5), and (4,4).

The ordinary splitting by degree can be made G-equivariant: its degree filtration is G-stable, and ordinary splittings can be averaged over the finite group. A same-degree block has the form M_d tensor O(-d), with M_d a genuine coefficient representation.

For (3,4) and (3,5), the degree-three rank-one block would require R6 in Sym3(W'), impossible. For (3,3), the coefficient representation M_3 has dimension two. Since K is a subbundle of the odd bundle R6 tensor O and O(-3) is odd, M_3 must be even. Every nontrivial two-dimensional irreducible of G is odd, so M_3 must be a sum of trivial lines. Each gives the same forbidden degree-three line map. Therefore K=2O(-4) as an ordinary bundle.

The image J has rank four and degree eight. Every splitting summand of its subbundle inclusion into 6O(2) has degree at most two. Thus J=4O(2). After twisting by O(-2), its inclusion into (W0+Qspin) tensor O is constant and identifies it with an invariant four-dimensional subspace. The only such subspace is Qspin. Hence the W0 component gamma of beta vanishes identically.

Conversely, if gamma=0, beta takes values in Qspin tensor O(2), so its rank is at most four. The already established uniform u<=10 gives rank(beta)>=4 at every point. Thus beta has rank exactly four everywhere and u=10 constantly.

## 3. The single-channel alternative

The W0 component is an equivariant quadratic bundle morphism

gamma:R6 tensor O -> W0 tensor O(2).

Its space of equivariant coefficients is Hom_G(R6,W0 tensor Sym2(W'))=Hom_G(R6,R6), which is one-dimensional. Therefore gamma is specified by a single scalar relative to any nonzero choice of this universal intertwiner. The theorem does not infer that scalar is nonzero.

If gamma is nonzero, Section 2 excludes constant ten, Section 1 excludes constant five, and the positive-degree determinant excludes constant zero. The remaining alternative from PR523/525 is the exact jumping pattern: zero off Omega and five on Omega. Equivalently det(beta) is nonzero. If gamma is zero, the pattern is uniformly ten.

Thus the unresolved column question is now precisely whether this actual quadratic channel scalar vanishes. This is distinct from the quartic-generator invariant already proved nonzero in PR524. There is no implication between their nonvanishing statements asserted here.

## Scope

Authored structural mathematics requiring independent review. Conditional on the exact pinned inputs; not formally proof-assistant checked. No selected column/source-instance evaluation, numerical rank computation, coefficient search or large computation was performed. Original fixed-pair residual, higher-order lifting, and algebraicity remain separate unresolved questions.
