Publication copy of the completed review; original-byte SHA256: `b24710e4de30e62bbe138a1500430c72afa878e0bbc4b9391b9b15bae7fb95d5`. Paths are artifact-relative. Historical status refers to the review stage described below.

# Independent universal namespace equivalence review

Verdict: PASS for explicit initializer namespace values, lexical/global bindings and the approved small formal probes. No actionable initializer difference found. This does not verify sparse initialization, a q-middle adapter, q65 coefficients, source feasibility or an actual obstruction.

The candidate is `q-middle-explicit-init/initializer.py`, SHA256 `14d57d45128498daee5c6adc9eeda343c2d909ac41713fb5ed09acde3341085a`. The reviewed guard is SHA256 `6915a220408dc3bb5045b6cfaaaef8267a6516319cdb98deca5ba5717614c6fc`.

## Successful bounded run

`run-0003` completed with exit zero in 2.159163 child CPU seconds and 2.413820 wall seconds; direct-child peak RSS was 75,825,152 bytes. Cleanup completed and all 89 guard-recorded input hashes remained unchanged. Limits were the unchanged guard defaults: 60 CPU seconds, 75 wall seconds and sampled process-group RSS threshold 1,610,612,736 bytes at 0.1-second sampling. As documented by the guard, this host has no enforced address-space cap and sampled RSS has no guaranteed between-sample overshoot bound.

Runtime: pinned Python 3.12.14, SymPy 1.14.0 and mpmath 1.3.0 in `the isolated runtime`. No frozen payload module was imported. The only source-derived code executed was the separately pinned initializer-only reference harness; historical top-level jobs and all family/source builders were excluded. A profile tripwire rejected calls named build_symbols, source_map, iter_coefficients, middle_apply, graded_module or build_module.

The comparison checked the complete inventories: 150 outer names and 32 names in the independent complete-symbol namespace, excluding only documented loader plumbing/new root. These include all scalar expressions and symbol assumptions, matrix dimensions and entries, lists, tuples, dictionaries and temporary values. No algebraic fallback was required: values matched structurally. Imported modules/callables were checked separately by identity.

All 46 function bindings were checked, including globals used only inside nested lambdas/comprehensions. The candidate's closure cells were compared with the reference's global dependencies. Function bodies and all initializer statement segments were authenticated by exact AST comparison against pinned source files before accepting the runtime comparison. The five-entry complete-symbol recovery solve remained present; its family builder was defined but never called.

Forty safe probes passed: A/B/Bcoef on both spinor basis columns and a free spinor; getp/putp and getY/putY round trips; small free-coefficient exterior operations; DD/NN and their cubic representation matrices; and complete-helper monomial, coefficient, transvectant, op4 and quartic recovery operations. Negative fixtures rejected a changed theta assumption and a changed reference tau tensor. The output's `negative_symbol` inventory records the deliberately invalid fixture, not an accepted namespace.

## Preserved unsuccessful attempts

- `run-0001`: reviewer metadata failure. The AST digest inventory was generated under system Python 3.9, while the worker ran Python 3.12, whose AST serialization adds fields. The candidate's construction had completed; the static comparison rejected the mismatched metadata. Regenerated only the AST metadata using the pinned runtime.
- `run-0002`: reviewer binding-inspection failure. Shallow inspect.getclosurevars saw candidate op4's captured tv but omitted the reference global tv used inside its nested lambda. Replaced the dependency collector with a recursive code-object walk, preserving local/argument exclusions. This is the necessary lexical-versus-global normalization, not an initializer change.

Both failed receipts, stdout/stderr and exact reviewer input snapshots remain in their original run directories. The successful run also contains its input snapshot. No receipt was overwritten, no producer or frozen payload file was modified, and no failed attempt was labeled PASS.

## Reproducible artifact hashes

- compare.py: `b0e52cbc670c3e3b236d3024d54cdb776227c8aad47a56c303df0ce2a2626214`.
- launch.py: `44211a8ea562f19f11daff67a89eb526a09574fd407d7d1cb5f63f42c49ab31f`.
- pins.json: `e7123f9542325db453ec07acff7a3521d9041429c69acc98cb09cd1ec263566a`.
- reference_namespace.py: `cd1d2c945aa7a40dfbe7d1d0351915445c88738c23faaf0f70eadd6dcf5624f4`.
- reference_complete.py: `835e3082a412b569389546d4b2130aa438d049844e2a631db6c0ae5a095e1ed2`.
- run-0003/receipt.json: `4a062578c3eb98b4fc9ce3a9b709dc0084dd5b4deb3466663dc80d68bb0d82a4`.
- run-0003/stdout.txt: `cc423310ddf6ab191c05dfe4233b6a83972f7f3d689fd4e56b7a7780fdca8092`.
- run-0003/stderr.txt: empty, SHA256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- run-0001/receipt.json: `3a5796179bd5aab0cd07ed4f01dabdee8690ac4c5e245bddbb016765687a3086`.
- run-0002/receipt.json: `032276399f0cdd504d7d5e06ee410f35a38044ff42a1df3c1135f5e5f19207ac`.

pins.json binds all 80 payload files, the handoff manifest, candidate initializer/receipt, guard, and reference harnesses. The supervisor additionally binds pins.json and the exact comparison/launch scripts. It checks unchanged inputs after each worker exits.

The next independent gate remains complete sparse-attribute/API integration, both legacy tripwires, the q-middle raw8-constructor bypass, and reference-renaming behavior. The separate q65 initializer and all mathematical shards remain outside this review.
