# Linear-algebra propagation: exact boundary

`Propagation.lean` uses Mathlib linear maps, submodules, quotient modules, and finite dimensions. Its conclusions are conditional; no actual geometric map is instantiated.

## Proven implications

1. An equivariant nonzero linear map into a target whose invariant subspaces are only zero and the whole space is surjective. The proof constructs its invariant range and rules out zero range using nonzeroness. The operator-family formulation is stronger than requiring group-action laws; those laws are unnecessary for this implication.
2. A surjective linear map carries any spanning family of its domain to a spanning family of its target. Pure cubic elements can be generators of a linearized cubic domain; individual cubic values need not cover the target set-theoretically.
3. If coordinate images together span the next target, applying coordinate linear maps to a spanning family spans the next target. An additional theorem derives this premise from a genuinely surjective assembled coordinate linear map whose elementary inputs span its source. Thus no single coordinate is assumed surjective.
4. Applying (3) twice proves spanning in both mixed channels.
5. If an upstairs image submodule contains a lower submodule and maps surjectively to its quotient, the upstairs image is the full space. The proof uses an actual quotient module and subtraction of representatives; there is no direct-sum splitting assumption.
6. With finite-dimensionality and imported dimensions four and eight, Mathlib rank-nullity gives ambient dimension twelve.
7. `conditional_full_retained_span` composes irreducibility, nonzero equivariance, generator spanning, both scalar identities, and both coordinate-spanning statements with the explicit geometric transfer premises to conclude fullness.

## Required geometric inputs, not supplied here

- Actual vector spaces and their actions, plus irreducibility of the cubic target.
- The actual canonical linearized cubic map, its equivariance, and its nonzeroness.
- Spanning of the linearized domain by the chosen cubic generators.
- Coordinate multiplication surjectivity (or its equivalent joint-spanning consequence).
- Scalar-linearity identities relating mixed families to the cubic family.
- The lower and upper upstairs/downstairs transfer statements.
- Finite-dimensionality and the four/eight dimensions of the retained filtration.

The file does not prove actual cohomology, multiplication-surjectivity geometry, a nonzero cubic scalar, a residual or physical-obstruction verdict. It performs no model-matrix, polynomial-instance, point, jet, or Massey-value computation.

## API source checked

Official Mathlib v4.19.0 sources in the pinned checkout:
- `Mathlib/LinearAlgebra/Quotient/Basic.lean`, including `Submodule.ker_mkQ`.
- `Mathlib/LinearAlgebra/Dimension/RankNullity.lean`, including `Submodule.finrank_quotient_add_finrank`.

Compiler verification is recorded separately in the compilation log and independent audit; this document alone is not a claim of kernel verification.
