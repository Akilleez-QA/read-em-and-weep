# Independent audit: quartic singular-surface exclusion

## Verdict

An independently tasked mathematical reviewer verified the central 38>27 contradiction, the scheme-theoretic and commutative-algebra details, and the squarefree/non-squarefree normality dichotomy. No substantive correction was needed. The proof distinguishes support purity from the stronger Cohen–Macaulay/no-embedded-points conclusion, as recommended by the reviewer.

## Checks

1. **Nonempty zero locus.** A nowhere-zero section of the rank-three bundle would produce a rank-two locally free quotient and force its nonzero third Chern class to vanish.

2. **Regular section only under the excluded hypothesis.** Three local generators bound the codimension of every minimal component by three. Containment in a singular locus of dimension at most one forces each minimal component to have codimension exactly three. The ambient regular local rings are Cohen–Macaulay, so the three generators form a regular sequence. Only at this point do the no-embedded-components conclusion and degree 38 follow. See [Stacks, local complete intersections](https://stacks.math.columbia.edu/tag/00S8).

3. **Scheme containment, including nilpotents.** The local determinant formula gives q∈I_Z² and dq∈I_ZΩ¹. Changes of trivialization add multiples of q, so the Jacobian containment is invariant. The ideal direction is J⊂I_Z and the scheme direction is Z⊂S, not the reverse.

4. **Euler and the affine cone.** In characteristic zero, q belongs to the ideal of its cubic partials. In the contradiction case S contains a nonempty curve and has dimension at most one. The homogeneous coordinate ring of its affine cone has dimension two, and J has height three. Irrelevant-origin or saturation phenomena do not alter the height relevant to this argument.

5. **Three constant polar combinations.** After a regular sequence of length i<3, all associated primes of its complete-intersection quotient have height i. Such a prime cannot contain J of height three. Its intersection with the linear span of the partials is consequently a proper linear subspace. Finite prime avoidance over C selects a non-zero-divisor at each step. No smoothness or transversality of the resulting complete intersection is asserted or required.

6. **Degree comparison.** The complete-intersection curve has Hilbert series (1−t³)³/(1−t)⁵ and degree 27. Its closed subscheme Z has degree at most 27 by Hilbert-polynomial additivity (or generic-length comparison). This comparison includes generic nilpotent multiplicities and cannot be evaded by nonreduced singular schemes. Thus degree 38 is impossible.

7. **Different normality conclusions.** For squarefree q, the branch has singular locus of dimension exactly two and fails R₁ as a threefold. The integral spectral cover has the same-dimensional singular support but dimension four, so it satisfies R₁. Both are hypersurfaces and S₂. Therefore the branch is nonnormal while the cover is normal. See [Serre's criterion](https://stacks.math.columbia.edu/tag/031O). A weighted-projective realization adds no singular vertex on the cover: z²=q excludes that ambient vertex.

8. **Repeated factors.** A nonsquare non-squarefree quartic has a repeated linear factor and is L²Q with Q quadratic nonsquare. Repetition of a quadratic factor would make the entire quartic square. The hyperplane L=0 is singular in the branch, and its lift makes the cover fail R₁. This includes L³M, as well as an irreducible residual quadratic or a product of two distinct residual linear factors.

9. **Degree of the singular surface.** Independently checked after the main argument: in the squarefree case ht J=2, and two general polar cubics give a degree-nine complete-intersection surface containing S scheme-theoretically. Consequently deg₂ S≤9, including generic nilpotent multiplicities; lower-dimensional and embedded components do not affect this leading coefficient.

10. **Normalization and the unchanged module.** Independently checked in a second review pass: the nonsquare quadratic Q is squarefree, so Y:w²=Q is integral and normal. The inclusion z=Lw is finite and birational, making Y the normalization of X, including Q=LM. The restriction sequence and H⁰(B(1))=0 force φ|H to be generically nonzero nilpotent of rank one. A compatible normalization-algebra action on the same underlying F would give Lψ=φ with ψ:F→F(1); taking traces forces ψ∈H⁰(B(1))=0, a contradiction. The relation ψ²=Q·id is valid but not needed for this contradiction. Pullback followed by torsion removal or reflexive hull is not excluded, and must not be assumed to have pushforward F.

## Scope

The theorem concerns the singular dimension of a possible quartic determinant. It does not prove that the section's own zero scheme has dimension two, and it does not resolve H⁰(B(2)). Squarefree reducible branches automatically have singular surfaces at factor intersections. For irreducible squarefree branches, nonnormality is a necessary condition, not an impossibility theorem.
