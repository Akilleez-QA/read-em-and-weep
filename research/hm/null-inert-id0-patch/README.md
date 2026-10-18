# Inert ID0 production-integration candidate

**NON-APPLIED. NO PHYSICAL EXECUTION OR NUMERICAL RESULT.**

This portable review bundle proposes two additions against immutable source commit `e93cf712f9da4926a8450cc870ed45a7bfc379ab` of [Akilleez-QA/read-em-and-weep](https://github.com/Akilleez-QA/read-em-and-weep/tree/e93cf712f9da4926a8450cc870ed45a7bfc379ab/research/codex-swarm).

- A production-field shared Laurent certificate retains one fully divided quotient and binds the exact rational, immutable frame context and existing Execution.
- An appended `actual_id0` unconditionally raises before inspecting arguments or constructing anything. Its complete candidate construction remains unreachable in the same function. All old program bytes and guards remain unchanged.
- The terminal reads exponents (-3,-3,-1,-1), (-2,-2,-2,-2), (-1,-1,-3,-3), with weights 1:2:1. No detector value was produced.

The independent static review accepts only this inert review scope. Complete source/proof closure, invented-input implementation tests, resource/lifetime proof and separate operational acceptance remain outstanding. Frame labels do not authenticate source provenance. Existing production import-time behavior is unchanged and is not certified safe by the entrypoint refusal. Do not import candidate text, apply this patch or interpret review acceptance as execution permission.

## Contents

- `candidate.patch`: original reviewed diff, unchanged.
- `candidate-text/`: original full candidate text, unchanged; `.py.txt` is intentional.
- `PROOF.md`: public-safe proof and limitations, with private operational details removed.
- `public-pins.json`: public source URLs, immutable commit/blob/hash pins, candidate hashes and exact retained ID0 record.
- `retained-requests.json`: retained request data, bound by its recorded hash; ultimate-source authentication remains an explicit review gap.
- `validate_static.py`: portable derivative of the supplied static validator.
- `review/REVIEW.md`: unchanged independent findings and limitations.
- `review/validate_independent_static.py`: portable derivative of the independent static validator.
- `validation-*.txt`, `review/independent-*.txt`: normal/optimized results reproduced with the portable validators.
- `dependency-inventory.json`: generated static import and selected-pin inventory, not full dependency acceptance.
- `PORTABILITY.md`, `original-reviewed-hashes.json`: exact adaptation boundary and original reviewed hashes.
- `SHA256SUMS`: hashes for all bundled files except itself.

No private connector receipts, private preparation manifest, accounting records, credentials, hardcoded machine paths or production source snapshot are bundled.

## Reproduce static validation

Use Python 3.10 or newer. Supply a read-only source directory containing the pinned `exact-curve-field/`, `detector-realization/` and other source subdirectories. For a checkout at the stated commit this is `research/codex-swarm/`. The validators first check the supplied source bytes against immutable pins; they never import or evaluate them.

From this bundle directory, with SOURCE_ROOT set to that directory:

    python -B validate_static.py --source-root "$SOURCE_ROOT"
    python -B -O validate_static.py --source-root "$SOURCE_ROOT"
    python -B review/validate_independent_static.py --source-root "$SOURCE_ROOT"
    python -B -O review/validate_independent_static.py --source-root "$SOURCE_ROOT"

The first validator writes only `dependency-inventory.json` inside this bundle. Source files are read-only. The inventory's presence flags may vary between a partial frozen snapshot and a complete checkout; all selected source pins must still match. The independent validator reconstructs the diff as text without applying it, checks the retained-record digest, and recursively checks the public function's refusal semantics.

Finite AST checks are not a formal semantic proof or executed tests of the new field API. See the independent review's specific validator limitations. D0 remains unknown.
