# AC01 transitive-binding repair follow-up

Date: 2026-10-16, 11:05 UTC.
Reviewed repair snapshot: [a807e98532a0b4a7bfeef0e086ce414328bdeaeb](https://github.com/Akilleez-QA/read-em-and-weep/blob/a807e98532a0b4a7bfeef0e086ce414328bdeaeb/research/codex-swarm/detector-admission/whole_envelope.py#L9-L19).
Baseline finding: `cost-review.md`, reviewed at d37436ee72fcb8bc93ce9b1ef7ff4febeed0c789. That report is preserved unchanged as the historical review.

## Narrow result

**The reported transitive-dependency authentication defect is fixed.** After authenticating the frozen SR marker and its producer files, `whole_envelope.build()` now reads the already-authenticated SR source-pins.json and validates the actual bytes of all ten declared local dependencies, before consuming their AST metadata. This includes the interfaces dependency missing from AC's direct pin list. Because `actual_route_certificate()` invokes this builder, the correction covers both the standalone and integrated metadata paths.

The correction authenticates the files specified by the frozen manifest. It does not establish source denotation, alter any resource bound, authenticate a current ledger, or grant physical execution authority.

## Independent metadata-only checks

The portable `check_transitive_binding.py` fixture was updated to copy every declared local dependency, so it can test the corrected builder without a missing-fixture-file failure. Its original two mutation semantics are unchanged:

1. Change the interfaces parity constant from -1 to +1 while retaining the same AST-node count.
2. Change the imported compiler's staircase range from 4 to 1,000,000 while retaining the same AST-node count.

The modified dependency files are never imported or executed. Only the metadata builder is imported; mutations occur in isolated copies, and original bytes are checked unchanged.

Results in both normal and optimized (`-O`) modes:

- Interfaces mutation: rejected with `SR local dependency drift: inserted-coefficients/interfaces.py`.
- Imported-loop mutation: rejected with `SR local dependency drift: scalar-compiler/compiler.py`.
- Portable control exit: 0.

Additional checks:

- All ten actual dependency digests agree with the frozen SR manifest.
- The unmodified repaired builder emits the same whole-route envelope as the reviewed published JSON.
- Replaying the updated portable fixture against the original baseline still reproduces both accepted mutations and the expected defect-detection exit 1.

This narrowly accepts the repair. Together with the separately checked e844d047 exponent-observation correction, both cost-review implementation findings are now resolved at this snapshot. The mathematical/physical admission boundary is unchanged: `BLOCKED_ROUTE`, with resource-unit reconciliation, byte/native-workspace binding, current all-worker state and release authority still separate obligations. Source/control acceptance remains scoped to its independent review.

No physical polynomial, source jet, coefficient, fiber enumeration, external write or execution release occurred in this verification.
