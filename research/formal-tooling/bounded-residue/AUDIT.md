# Independent audit: fixed-two-term residue aggregation

Audited 2026-10-18 UTC. Verdict: **PASS within the explicitly bounded two-term scope below.**

## Independent checks

- Inspected the actual `bounded.rs` body, its freshly emitted textual IR, all generated Lean obligations, the repaired positive proof twin, and `BoundedBridge.lean`.
- Ran the official positive checker independently without the fast-path library flag: exit 0, eight VCs newly checked and one decision-evidence obligation discharged interactively. See `audit/positive-recheck.log` and `.exit`. This initial run may have overlapped the producer's final reproduction, so the subsequent clean, sequential run is authoritative.
- After the producer confirmed its checker idle, reran the complete `recheck.sh`: exit 0. See `audit/full-recheck.log` and `.exit`. This freshly regenerated both source obligation sets, kernel-checked the positive twin, confirmed negative Lean-phase rejection, rebuilt every local bridge dependency from source, rebuilt the positive twin, checked the new bridge, and printed axioms for all nine accepted declarations.
- Preserved independent run/check/IR receipts under `audit/`. The deliberately false source differs only by `+ 1` in the aggregation postcondition, with unchanged executable code and bounds. Its sole **uncovered** error is `bounded_wrong.residue_two.ensures_3`, hash `317219485f094080`, Lean-phase exit 1. The raw diagnostic stream also contains an evidence diagnostic explicitly marked `covered_by_twin=true`; this is not a second unresolved failure. See `audit/negative-isolation.log`.
- Independently compared all nine generated/twin declaration signatures and manifest hashes for both sources; all match. Every frozen SHA-256 entry still matches after reproduction. See `audit/check_binding.py` and `audit/binding.log`. Hashes identify these artifacts; they do not establish compiler correctness.

## Bounds and generated safety obligation

The program executes exactly two calls of the five-coordinate selector, followed by `x + y`. Both coefficients satisfy `-(2^62-1) <= c <= 2^62-1`; selected contributions are coefficient or zero. Their sum lies between `-9223372036854775806` and `9223372036854775806`, inside the signed64 range `[-9223372036854775808, 9223372036854775807]`. These conservative bounds are sufficient, not necessary.

The actual emitted addition-overflow VC is `bounded.residue_two.assert_2`, hash `919ee63e1b70623e`, source line 26. It concludes signed64 range of the mathematical selected sum. The postcondition VC `bounded.residue_two.ensures_3`, hash `0b1bf9253df95dc5`, proves clipping of that sum equals the unbounded mathematical sum, using the checked overflow premise. Twelve signed-input premises and both coefficient-bound premises are present. The remaining VCs check the selector's minus-one arithmetic and postcondition. No arithmetic budget is computed by executable code.

## Bridge and axioms

`BoundedBridge.two_term_residue` directly applies the accepted generated overflow and postcondition theorems; it does not merely restate their result as an assumption. The two call-result range premises are proved by coefficient/zero case analysis. All twelve machine-range premises and both extra coefficient bounds remain explicit. The result is equality to formal coefficient extraction at the all-minus-one exponent from the sum of exactly two Laurent terms; repeated exponents are permitted and add.

Fresh compilation of the dependency copies, positive twin, new bridge, and axiom audit succeeded. The printed bridge proof term contains both generated aggregation theorem references. Every accepted generated declaration and the final bridge theorem reports only `propext`, `Classical.choice`, and `Quot.sound`; no `sorryAx`, added project axiom, or SMT oracle axiom appears. The negative twin's intentional failed proof placeholder is not an accepted proof. Generated evidence placeholders are resolved by the accepted twin's explicit `Classical.propDecidable` proof.

## Exact claim and remaining trust boundary

This is a universal bounded-input proof for **two explicitly unrolled selector calls plus one addition**. There is no array, arbitrary-length executable loop, loop invariant, or arbitrary-precision implementation. It does not implement the earlier arbitrary-list accumulation contract. `returnedTwo` represents the emitted clipped return expression after call-spec substitution; it is not an imported executable Rust function or a verified Rust interpreter.

Rust frontend/SST correspondence, call-spec substitution, VC generation, machine embedding, and checker orchestration remain trusted compiler infrastructure. The bridge relies on the separately checked selector specification through that lowering boundary. It establishes formal Laurent coefficient extraction, not an analytic residue theorem or full geometric/HM bridge. No actual HM source/model, coefficient instance, matrix product/rank, point, jet, residual, or Massey evaluation was used. No installation or original accepted-source modification was needed for this audit.
