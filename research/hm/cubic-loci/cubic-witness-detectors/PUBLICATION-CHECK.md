# Independent publication check: fixed cubic witness and finite detector families

Verdict: PASS for the exact versions below, with the explicit hypotheses and genuinely proved predecessor inputs. Review date: 2026-10-20 UTC.

## Reviewed versions

- INPUTS.md: `0997e7dbb47f1a198335cda45ba72b688c8ff7b22469ea5b55ef1efd233f721d`
- README.md: `109f7dd461fb6204b141ab0f8f64bb9e2c7ebdd0a3efe7b39d632a89256a1f47`
- cubic-explicit-weight-basis/PROOF.md: `692a3b98c24a34dddea5cf325944374ea28619fb1672004ee41f7d8d8aa432c4`
- cubic-explicit-weight-basis/REFINEMENT.md: `36215363742e72bad71047db8f654849990bb5a244348a20f6664f9fed63307c`
- cubic-single-witness-selection/PROOF.md: `c4576a96163d6cd1a51892c7b9edd3a29a42d37305ef1d6fe35ca182df1b5f55`

## Mathematical and dependency verification

The symmetric-pair map is nonzero for nonzero cubic by polarization and the permutation identities. Its source is the actual irreducible Sym^2 V, not a dimension-based guessed module. The fixed-line stabilizer permutes the four allowed weights transitively, forcing the specified repeated-input class nonzero. Literal target and Serre-dual character conventions select the stated quotient lines. The ordinary residue statement is conditional on regular representatives and imports P06's general trace normalization; it does not evaluate that residue or assert the special orbit-reduced formula.

The twenty-value basis proof uses structural repeated-input nonvanishing, distinct weight support, the unique arithmetic-progression triple for each remaining weight, and surjectivity of the actual cubic image. The reflection calculation uses determinant-corrected SL5 lifts from P05B, not a missing section of pairing00. These show nonzero classes and basis status without computing class coordinates or scalar values.

The mixed finite families use actual coordinate multiplication and strict coefficient transfer. The refinement correctly keeps 66 symmetric coefficient pairs, 64 eligible upper coordinate indices, and 88 eligible unordered lower coordinate pairs. Thus 64 times 66 plus 88 times 11 equals 5,192 indices. These are spanning indexed families: zero entries and repeated values remain allowed, and no twelve-element pivot or minimal basis is selected. Discarded upper values have zero leading symbol and may still have lower components; the separately spanning lower family handles them. Lower transfer and zero retained filtration-zero part justify exact lower removals.

The dependency closure is units04–05, pairing foundation00, P01–P05B, and P06 for the retained witness-residue theorem. The physical statement is completeness of these abstract tests on the stipulated retained sector, not a binding or evaluation of an actual physical source.

Availability and immutable public pinning of the named predecessors remain publication requirements. Historical receipts describe their original manuscripts, not these normalized bytes. Subsequent edits require renewed review; staging alone is not publication. This check does not establish novelty.

## Evidence boundary

The review used static proof reads, universal mathematical reasoning, and file checksums. No actual HM/source/model matrix, product, rank, selected input, point, jet, residue, detector, or Massey value was evaluated. No actual physical residual was identified or decided.
