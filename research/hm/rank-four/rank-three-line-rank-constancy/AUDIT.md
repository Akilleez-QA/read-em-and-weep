# Independent audit: constant rank on the twenty-five lines

## Verdict

The argument in PROOF.md is valid with its explicitly stated dependencies: the twenty-five-line free A-orbit classification, N-equivariance and linearity of b, the identity rank(b)=4+rank(Q), and generic residual rank three (for example supplied by finiteness of Z₂). It proves residual rank exactly three at every point of each hypothetical line. It does not prove these lines exist, that they belong to the actual rank locus, or that the rank-three locus is finite.

## Checks of the potentially delicate steps

1. **The line stabilizer is a complement.** Its order is 120 by orbit–stabilizer and its intersection with A is trivial by freeness of the action on components. Thus it maps isomorphically onto SL₂(F₅).

2. **The Weyl phases and explicit operators are consistent.** With X e_j=e_(j+1), Z e_j=ζ^j e_j, and W_(a,b)=ζ^(ab/2)X^aZ^b, one has ZX=ζXZ and the displayed product scalar ζ^((bc−ad)/2). Directly on e_j, conjugation by D produces the scalar ζ^(ab/2+a²+(b+2a)j), which is exactly W_(a,b+2a). Conjugation by T replaces (a,b) by (2a,3b). Therefore D and T belong to the canonical projective complement, not merely to unspecified cosets of A. Also TDT⁻¹=D⁻¹ holds exactly for the chosen linear matrices, D⁵=I, and D's eigenvalue-one space is precisely Ce₀.

3. **The complement is the one inside the specified normalizer.** Conjugation by any projective normalizer element preserves the scalar commutator pairing, so its induced action on A lies in Sp₂(F₅)=SL₂(F₅). After matching that action with its canonical intertwiner, the remaining phase is a character of A. Nondegeneracy of the commutator pairing removes that character by an element of A. This proves the full normalizer is A⋊G₀. Since the specified N has that same finite order, it equals this normalizer. The proof's uniqueness-of-Heisenberg-representation input is standard and sufficient; no choice of a global linear Weil representation is being presumed.

4. **Every complement is A-conjugate.** The cocycle identity at the central element z=−I gives 2c(g)=(1−g)c(z). Since two is invertible on A, c is the coboundary of c(z)/2. This direct argument remains valid although 25 and 120 are not coprime.

5. **The projective line action is genuinely nontrivial.** If it were trivial, D would restrict to λI on the two-dimensional subspace, and the exact conjugation relation with its invariant T-action forces λ²=1. Together with λ⁵=1 this gives λ=1, contradicting the one-dimensional one-eigenspace. No scalar normalization gap occurs here.

6. **The image is A₅ and the minimum point orbit is twelve.** Perfectness and simplicity of PSL₂(F₅) imply a proper normal kernel is contained in the center. A faithful SL₂(F₅) action on P¹ is impossible: the central involution has two fixed points, perfectness fixes both individually, and a finite faithful point stabilizer on a smooth complex curve is cyclic. Hence the kernel is the center. Point stabilizers for the resulting faithful A₅-action are cyclic, of orders 1, 2, 3, or 5, so the point orbits have sizes 60, 30, 20, or 12.

7. **The determinantal argument includes exceptional points.** Generic rank seven guarantees a nonzero restricted seven-minor. The common-zero divisor of these degree-seven forms has degree at most seven and support exactly the rank-at-most-six locus on the line. Equivariance makes this support invariant. Any nonempty support contains at least twelve distinct points, which is impossible. Thus no residual-rank-two-or-lower point occurs anywhere on the line.

## Dependency clarification

Finiteness of Z₂ is stronger than generic residual rank three on the hypothetical lines. These are equivalent only as inputs sufficient for this particular proof, not logically equivalent global statements. The proof immediately specifies the weaker assumption it needs, so this wording does not affect validity. Its stated generalization to generic rank r≤11 follows by replacing seven-minors with r-minors (with rank zero trivial).

## Optional canonical description

A canonical-line identification is unnecessary for the rank theorem. It can also be justified: reflection R e_j=e_(−j) lies in G₀ and has eigenspaces of dimensions three and two. There is no G₀-invariant one-dimensional vector subspace: D and T force such a subspace to be Ce₀, whereas the Fourier intertwiner sends e₀ to a nonzero multiple of the sum of all five basis vectors. Complete reducibility applied to the finite inverse image of G₀ in SL(V) then makes the even three-dimensional space irreducible and the odd two-dimensional space the unique invariant two-dimensional subspace. Consequently any hypothetical free twenty-five-line orbit consists of the A-translates of the projectivized odd eigenspace. This additional description is abstract representation theory and evaluates no actual source operation.

## Addendum audit: Sections 7 and 8

The final expanded Section 7 and the pairwise-disjointness argument in Section 8 both pass independent review.

For Section 7, projective centrality of reflection upgrades to exact commutation because its trace is one. The finite inverse image of G₀ in SL(V) has order 600, so the stated complete-reducibility argument is legitimate. Irreducibility of the standard action on A and of the Heisenberg action on V establishes that the odd reflection line has exactly twenty-five A-translates.

For Section 8, the normalizations are important and correct: R_a is an actual involution of trace one, with R_a=W_(2a)R. If a≠b, then D_ab=R_aR_b=εW_(2a−2b), with ε⁵=1 and nonzero Weyl label. Its first four power traces vanish, and D_ab⁵=I. The discrete Fourier multiplicity formula therefore gives all five fifth roots as simple eigenvalues, including exactly one eigenvalue-one line. The exact relation R_a D_ab R_a=D_ab⁻¹ pairs the four nontrivial eigenspaces into two off-diagonal two-dimensional blocks, whose traces are zero. Consequently the trace-one involution R_a acts by +1 on the remaining D_ab=1 line. A common negative eigenvector for R_a and R_b would belong to that line and have the opposite R_a eigenvalue, a contradiction.

Thus the twenty-five canonical projective lines are pairwise disjoint. If the hypothetical reduced curve part occurs, it is their disjoint union. This conclusion correctly leaves the full determinantal scheme's nonreduced structure, embedded components, and isolated points unspecified.

The earlier generic-rank wording refinement has also been incorporated in PROOF.md; no remaining correction is requested.
