# Historical scope-limited review receipt

This review concerns the original source, possibly a larger scope than the excerpt in this unit. It is not a review of normalized publication bytes.

# Independent structural audit

## Verdict

The abstract argument in `PROOF.md` is mathematically correct under its geometric hypotheses, with the usual intended assumptions that H is a vector bundle and N is a line bundle. No correction to its representation-theoretic decomposition or quotient is needed. Its application to the particular retained source remains conditional on section 5; this audit does not establish that condition.

## Checks

1. **Equivariant minimal generators.** The finite symmetric quotient is flat by the stated Cohen–Macaulay/regular argument. The pullback of O(1) is L with its ordinary permutation linearization. Künneth gives the required intermediate vanishing for every twist. In particular, the negative twists introduce no hidden positive-degree line-bundle summands into the section-module argument. Once the ordinary splitting is known, M is graded free over the trivially acted-on polynomial ring R. Equivariant degreewise lifts of Q exist by Maschke, and graded Nakayama plus equality of Hilbert series makes their free extension an isomorphism. This correctly avoids the invalid shortcut of averaging a bundle isomorphism. The representation multiplicities are intrinsic, while the splitting need not be canonical.

2. **Finite-duality sign.** The determinant of the tangent-factor permutation gives precisely the sign character on the canonical line of Y. Thus the equivariant identity is omega_Y = L^(-2) tensor sgn, whereas the base canonical line has trivial group action. Finite duality consequently gives B-dual = B(3) tensor sgn. Twisting both decompositions into nonpositive degrees and comparing their minimal-generator representations gives W_a-dual = sgn tensor W_(3-a). Together with the degree-one Schur–Weyl decomposition, this yields exactly the four multiplicity representations displayed in section 2.

3. **Ordinary full-deck linearization.** For the identical double covers with the geometric factor-permutation action, their full-deck eigensheaf is the ordinary product of the four odd function eigensheaves. Commutative multiplication of their local function frames produces no alternating sign. Therefore its line is ordinary L^(-2), and importing the canonical-line sign here would be incorrect. Cancellation of N in End E and the two finite projection formulas then give the equivariant cohomology decomposition in section 3. No cohomology dimensions are required.

4. **D8 restriction and quotient.** The specified subgroup stabilizes an unordered pairing, and its stated character is the restriction of the S4 sign character. The permutation action on the three pairings is 1 plus [22]; twisting induction by sign therefore gives sgn plus [22]. Frobenius reciprocity selects one character line from each [22] and the entire sign representation, with none from the remaining irreducibles. The resulting three-group decomposition is correct. The central S4-sign idempotent commutes with the D-character projector, and their product is the sign idempotent. Hence its image is canonically contained in the paired sector and has a canonical complementary kernel there. The quotient is canonical even though its displayed identification with the two classical cohomology groups depends on splitting choices.

## Limits of this verdict

Only the abstract proof was inspected. No companion program, concrete source expression, matrices, rank certificates, points, polynomial instances, jets, residuals, or detector values were inspected or evaluated.

In particular, the actual source must still be shown to transform by the geometric action and the character (-,-,+). A different pair-exchange sign or a convention-dependent twist changes the character selection. Showing that one source's sign projection is a boundary does not imply vanishing of the entire sign cohomology group. The abstract quotient establishes neither the vanishing of its remaining classes nor completeness of any proposed detector family. The final numerical comparison remains conditional on the separate classical cohomology inputs and is not certified by this audit.
