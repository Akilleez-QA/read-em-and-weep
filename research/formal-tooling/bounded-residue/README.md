> Publication note: Read PUBLICATION.md first. The final AUDIT.md supersedes the original pending-audit sentence below. Checks described here occurred on October 18, not during publication. Historical scripts and hashes have `.historical.txt` suffixes.

# Fixed-two-term Rust residue aggregation

This is a new, universally quantified bounded implementation demo using the already installed Vermilion compiler at commit `1a56a4f38cbb126b7d73b04207e9c6fda9f179bf` and Lean 4.33.0. No installations or accepted-original source changes were made.

## Checked results

`bounded.rs` implements a five-exponent coefficient selector and `residue_two`: exactly two explicitly unrolled calls followed by one i64 addition. All twelve inputs are arbitrary signed64 integers. Each coefficient is additionally required to lie between `-4611686018427387903` and `4611686018427387903`, inclusive, i.e. ±(2^62−1). Selection returns that coefficient or zero; their sum therefore fits signed64. This is a deliberately conservative sufficient bound, not a necessary one. The code does not calculate absolute values or a potentially overflowing budget.

The positive official checker accepted **9 obligations: 8 VCs and 1 explicit decision-evidence obligation**, exit 0 (`positive.log`, `positive.exit`). The evidence twin uses `Classical.propDecidable p`; all other positive generated proof bodies use the existing `vrml` tactic. The initial evidence-placeholder failure is retained separately. The overflow theorem is `bounded.residue_two.assert_2`, statement hash `919ee63e1b70623e`; the final postcondition theorem is `bounded.residue_two.ensures_3`, hash `0b1bf9253df95dc5`.

`bounded_wrong.rs` changes only the aggregation postcondition by adding 1 to the claimed answer, while keeping the same executable body and safety bounds. Its decision evidence is repaired separately, so `negative.log` records rejection specifically at `bounded_wrong.residue_two.ensures_3`, hash `317219485f094080`, exit 1 in the Lean phase. This is not a frontend error. Its negative proof twin intentionally retains a failed proof placeholder and is not an accepted proof. No concrete coefficient instance or HM value was needed.

## Mathematical link

`BoundedBridge.lean` imports the accepted positive proof twin and existing Laurent bridge. `two_term_residue` supplies all twelve machine-range premises and both conservative coefficient bounds. It proves both selector call-result range premises from the coefficient-or-zero expressions, directly applies the generated overflow theorem, then directly applies the generated postcondition theorem. Its result equates the lowered clipped sum expression with `ResidueBridge.residue (ResidueBridge.interpret [(ea, ca), (eb, cb)])`. Repeated exponents are allowed and combine by addition.

`returnedTwo` is an explicit representation of the generated returned expression after call-spec substitution, not a callable Rust function imported into Lean or a verified Rust interpreter. `bridge.log` prints the proof term including the two generated declaration references. The theorem reports only `propext`, `Classical.choice`, and `Quot.sound`. The separate `Axioms.lean` checks all nine accepted generated declarations.

## Reproduction

Run `./recheck.sh`. It uses only installed dependencies, reruns both checker paths, requires negative exit 1 in the Lean phase, freshly compiles local byte-identical copies of the prior Laurent bridge and its dependencies, compiles the positive twin, then compiles the new bridge and audits generated declaration axioms. The script's final `recheck.log` and `recheck.exit` record the result. `source-sha256.txt` binds the frozen source files and script. Machine checker receipts and IR snapshots are retained under `receipt/`.

The underlying commands, from `${ARTIFACT_ROOT}/vermilion-tooling/vermilion`, are:

```
source ../env.sh
./scripts/run_example.sh examples/bounded-residue bounded.rs --per-file --lib BoundedResidue --manual-proofs
./scripts/run_example.sh examples/bounded-residue bounded_wrong.rs --per-file
```

The `--lib` option enables the official twin checker; no new Lake library registration or upstream configuration change was required for this per-file example. See `recheck.sh` for exact LEAN_PATH and native plugin configuration for standalone compilation.

## Exact boundary

This checks exactly two terms, explicitly unrolled. It does not verify an array representation, a loop invariant, arbitrary-length aggregation, arbitrary-precision executable arithmetic, an analytic residue, or a full geometric bridge. The earlier arbitrary-list mathematical accumulation theorem remains separate; this implementation uses its own simple two-coefficient bound and does not import that contract.

Rust-to-SST correspondence, call-spec lowering, VC generation, embedding conventions, and checker orchestration remain the existing Vermilion trust boundary. Lean checks the emitted statements; compiler correctness is not foundationally proved here. The positive selector specification and addition obligation are checked together, but the Lean bridge does not independently prove operational semantics for function calls.

No actual HM source/model matrices, products, ranks, polynomial instances, points, jets, residuals, or Massey computations were used. Only universal integer source and proofs were processed.

Independent audit has been requested; this producer receipt does not claim its outcome.
