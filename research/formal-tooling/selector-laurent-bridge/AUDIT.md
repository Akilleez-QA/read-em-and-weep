# Independent selector-to-Laurent bridge audit

Date: 2026-10-18. Verdict: **PASS for the stated single-term bridge and first-coordinate-zero theorem**, within the trust boundary below.

## Independent checks

The producer froze the five Lean source files before this audit's rebuild. `audit/rebuild.sh` copies those sources into a fresh temporary directory and recompiles, in order, the decision-evidence module, selector VC module, missing-face VC module, Laurent model, and new bridge. It uses the existing Vermilion/Mathlib installation, with the fresh directory first on `LEAN_PATH`; it does not reuse the producer's five compiled modules, install software, or rerun Rust generation.

The independent rebuild completed with exit **0**. The compiler identifies itself as Lean **4.33.0**, commit `d8b18978322de05a8f3dba51ef03cf5461676c17`. See `audit/independent-rebuild.log` and `audit/independent-rebuild.exit`.

All three copied proof-twin files are byte-for-byte identical to their accepted originals under `vermilion/examples/residue-selector/proofs/residue/`: `Evidence.lean`, `residue_term.lean`, and `missing_face_zero.lean`. This includes the actual `residue.residue_term.ensures_5` proof, rather than a restated substitute. The eight marked declaration blocks have individual SHA-256 hashes in `audit/source-binding.json`, alongside complete file hashes, the Rust source, generated manifest, successful prior runner receipt, toolchain specification, and Lake dependency manifest. The copied `ResidueBridge.lean` is also byte-identical to the existing model source in `lean-koszul`.

## Theorem content and dependency audit

- `accepted_postcondition` retains signed-64-bit range hypotheses for all five exponents and the coefficient. Its proof calls the imported `residue.residue_term.ensures_5` directly, as confirmed by Lean's printed elaborated proof.
- The generated VC's four SSA propositions are instantiated by nested conjunctions using the original signed clipping operation. The five arithmetic-range obligations and eight then/else SSA equivalences are supplied with proofs. They are not dropped, weakened, or replaced with an assumption that the returned value already equals the desired coefficient.
- `clipped_minus_one` proves the clipped constant is `-1`. `guard_iff_exponent` proves that the coordinatewise guard is exactly equality of the constructed `Fin 5 → Int` exponent to `ResidueBridge.residueExponent`.
- `returned_eq_single_coefficient` obtains the actual postcondition first, then identifies it with evaluation of `Finsupp.single` at the all-minus-one exponent. `returned_eq_singleton_residue` connects the same result to the singleton-list `ResidueBridge.interpret` and its formal residue.
- `first_coordinate_face_zero` retains those same six ranges and adds `0 ≤ e0`. It applies the actual accepted `residue.missing_face_zero.ensures_1`. Its extra call-result range premise is proved by splitting the conditional and using the coefficient range or the range of zero. The second conjunct is proved independently through `ResidueBridge.residue_eq_zero_of_nonnegative_coordinate` at coordinate `0 : Fin 5`. Thus both the lowered returned expression and its singleton Laurent interpretation are proved zero.

No exported theorem assumes the desired coefficient identity or either requested zero conclusion.

## Axioms and holes

The independently rebuilt imported postcondition and missing-face VC, and all four exported bridge theorems, report exactly:

`[propext, Classical.choice, Quot.sound]`

The coordinate-guard lemma reports only `propext` and `Quot.sound`; the clipping lemma uses the same standard three axioms. The model reports only subsets of those axioms. No `sorryAx`, additional custom axiom, `sorry`, or `admit` occurs in the checked five source modules or the reported theorem dependencies. This is an axiom-relative Lean kernel check, not an axiom-free claim.

## Exact scope and trusted boundaries

The result is a universal theorem for one selector term with bounded i64 inputs, connected to an unbounded-Int, finitely supported, additive Laurent-coefficient model. `returned` is the explicitly stated lowered conditional expression after substitution of the generated short-circuit propositions. It is not an independently verified Rust interpreter.

The pre-existing successful Vermilion runner receipt is inspected and source-bound; the full Rust-to-SST-to-VC generation/checking pipeline was not independently rerun here. Rust/Verus lowering, VC generation, embedding conventions, obligation completeness, and the reporting path remain trusted. The new Lean proof establishes the connection from the actual accepted generated VC to the formal single-term model; it does not certify that translation boundary or the full checker.

**Not covered:** machine list aggregation, accumulator overflow, a verified arbitrary-length executable residue evaluator, multiplication or a Laurent-ring implementation, linkage to an actual geometric/Cech/Serre residue, or any actual HM data or numerical value evaluation. The generic model has additive list lemmas, but no theorem here connects a machine aggregation loop to them. The first-coordinate-zero statement is algebraic coefficient exclusion, not a geometric extension theorem.

No actual HM values, models, ranks, polynomial instances, points, jets, residues, or Massey computations were evaluated. This audit made only local read/build/report changes, with no external writes, local Codex task, or new installation.

## Primary source fingerprint

`SelectorLaurentBridge.lean` SHA-256:

`6d0a2b06c7ccc5eb52b8321364e27a4bfea4e20aad61501e077842b101732cac`

The detailed source/proof binding is in `audit/source-binding.json`. The verdict applies to those exact source contents.
