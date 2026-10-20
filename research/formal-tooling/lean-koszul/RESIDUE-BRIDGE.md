# Sparse Laurent coefficient bridge

Verified 2026-10-18. Source: `ResidueBridge.lean`.

## Result

For arbitrary `R` with `AddCommMonoid R` (in particular integers and any commutative ring), exponents are `Fin 5 → ℤ` and a sparse list consists of `(exponent, coefficient)` pairs. `interpret` is a concrete recursive sum of `Finsupp.single` functions in `Exponent →₀ R`. It is not an opaque interpretation or an assumed semantic axiom. Duplicate exponent entries add; zero entries contribute zero.

- `coefficient_interpret`: selecting and summing entries at any target exponent equals evaluation of the finitely supported interpretation at that exponent.
- `residue_interpret`: the selection at `(-1,-1,-1,-1,-1)` equals the formal Laurent residue coefficient.
- `residue_predicate`: all five coordinates being `-1` is equivalent to equality with that exponent.
- `selectSum_eq_zero`: excluding the target from every entry makes its coefficient zero.
- `residue_eq_zero_of_nonnegative_coordinate`: if every list entry has nonnegative exponent at one fixed chosen coordinate, its formal residue is zero. The coordinate is arbitrary, so this covers each of the five possible choices.

## Verification receipts

Source SHA-256: `f90f3b54a4e9f97d9109bdb67decb4ef9c881704c80d7b6cec5cf8ed52923846`.

1. Lean 4.19.0 with the existing pinned Mathlib environment:
   `./check-lean.sh ResidueBridge.lean --root=${ARTIFACT_ROOT}/lean-koszul -o ${ARTIFACT_ROOT}/lean-koszul/ResidueBridge.olean`
   Exit 0; `ResidueBridge.compile.log` contains all five axiom reports. The `.olean` is for 4.19 only.
2. Unchanged source under existing Vermilion Lean 4.33.0 (commit `d8b18978322de05a8f3dba51ef03cf5461676c17`) and its pinned Mathlib dependencies:
   from `${ARTIFACT_ROOT}/vermilion-tooling/vermilion`, `source ../env.sh; lake env lean ${ARTIFACT_ROOT}/lean-koszul/ResidueBridge.lean`.
   Exit 0; separate receipt `ResidueBridge.lean433.compile.log`. No 4.33 `.olean` was written over the 4.19 output.
3. Independent source review and fresh 4.19 compilation passed. Reviewer verified duplicate handling, exact theorem hypotheses, concrete Finsupp interpretation, and source hash.

Printed dependencies are only `propext`, `Classical.choice`, and `Quot.sound`; `residue_predicate` uses only `Quot.sound`. No new axioms, `sorry`, `admit`, `unsafe`, or `native_decide` occur in the source.

## Scope and remaining work

This supplies a universal additive formal Laurent-coefficient meaning for the mathematical all-minus-one selector predicate. It is compatible with the predicate checked in the earlier five-i64 selector experiment, but is not a formal theorem importing or relating the generated Rust/Verus/Vermilion function declarations. The integer embedding from those bounded inputs remains to be connected explicitly if an end-to-end program-to-model statement is wanted.

The summation here is exact abstract addition, not machine-i64 accumulation. No overflow theorem is claimed. Multiplication, full TW/HM geometry, an analytic-residue theorem, and all other model-specific bridges remain outside scope. No HM terms, products, ranks, polynomial instances, points, jets, residuals, or Massey values were evaluated. No additional dependency downloads or toolchain changes were needed.
