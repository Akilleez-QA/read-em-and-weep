# AC-R independent observed-height repair acceptance

**Current-scope disposition: ACCEPT the repaired prospective AC package at marker `3bb840e094487e88f9a8aae0f6e12aa1be103ac871ca9d21e588bc2763727b47`. The auxiliary observed-height defect is repaired. The separately accepted conditional whole-route finite M/F/B/T/H/retained-logical-S argument remains unchanged. Physical status remains BLOCKED_ROUTE; no execution release.**

This is acceptance of the repair under the original mathematical/source premises, not authentication of actual source values, denominators, byte occupancy or a current global ledger. The original qualified report is preserved byte-for-byte. Its required repair accurately describes the original snapshot; this follow-up resolves that requirement for the current marker. The producer marker's `independent_followup: pending` is unchanged handoff text; this report supplies the current independent disposition.

## Scope and immutable history

Read the original report in full, the new marker, the producer diff and original bytes against `d37436ee72fcb8bc93ce9b1ef7ff4febeed0c789`, `rf_bounds.py`, the RF `Execution.observe`/Poly/Rational implementations, and the whole-envelope builder. Read-only Git objects confirmed the original review/counterexample at `b3c61eba2686e50d764b1a34f842974e142fd132`.

Only these authorized files were written in the repository:

- `test_independent.py`: frozen marker, current case09 inequality/name/comment, and producer count in the runner's final message.
- `test_height_followup.py`: six bounded independent controls and normal/-O supervision.
- This report.

No producer edits, Git mutations or posts occurred. No actual source coefficients, polynomials, jets, residuals, physical fibers, owner constructions or partition evaluation were performed. The existing independent/producer controls parse stored constants solely as metadata. Every RF arithmetic control is tiny and fictional; large exponents remain sparse integers, never expanded powers. No old RF/BI/SR suite was replayed.

Original report SHA256, identical to the preserved commit:

`8ba5e4028c0ec9a12f6bf0b76491dce5c422dbe5242b382be3de286fa3da356b`

Original independent test SHA256 at that commit:

`b66c82d24e6b3174b746d43d472f67cc46828100e1c498c4b17c74bc2b68d65c`

Historical case09 intentionally reproduced **11 > 3**. It was not a repair test. The current case keeps coefficient-only `bound.bits == 3`, verifies aggregate observed upper `== 11`, and verifies actual RF peak `11 <= 11`. The historical reproduction remains in the original commit and original report; neither was rewritten or replayed against repaired code.

## Why the repaired bound is sound

The contract takes canonical RF Poly operands and conservative nonnegative `terms`, uniform per-coordinate `degree`, and coefficient-Fraction `bits` metadata. It bounds operation-local RF observations; an aggregate Execution with unrelated prior observations requires `max(inherited_peak, operation_upper)`. It does not bound arbitrary raw constructor histories from normalized output metadata alone, nor promise a valid Rational with a zero denominator.

RF observes `max(abs(numerator).bit_length(), denominator.bit_length())` for each Fraction. Poly construction observes each nonnegative exponent through `observe(Fraction(power))`, even before cancellation removes the term. Partial also observes the old differentiated exponent through `ex.q(e[i])`. Negation observes the scalar -1.

The repaired maximum includes 1, the output coefficient estimate, both input coefficient estimates, and input/output degree bit lengths. Thus:

- Add constructs from input exponents bounded by max(d,e), including canceled terms. Its coefficient sum bound h+g+1 also covers intermediate insertion values.
- Multiply observes exponent sums bounded by d+e. At most k=min(m,n) pairs contribute to a fixed exponent; a common-denominator prefix bound gives k(h+g)+ceil(log2(max(1,k)))+1. Input-height maxima remain covered when one operand is empty and no products occur.
- Negation preserves exponents; its h+1 estimate covers coefficient scaling and the scalar observation.
- Partial retains degree d conservatively. This covers both surviving exponents and the old integer multiplier. The coefficient estimate h+ceil(log2(max(1,d)))+1 covers multiplication by that integer. Empty results and differentiation on an absent axis remain covered.

Rational composition already accumulates the maximum from every polynomial primitive, so the repaired exponent maximum propagates without a separate Rational source change. Generic add covers cross products and summation; equal-denominator and zero shortcuts are dominated. Partial includes two polynomial partials, three products, negation and addition; multiplication includes numerator/denominator products. Normalization's reciprocal has height <=hD, scaling gives numerator <=hN+hD and denominator <=2hD, and scaling preserves exponents. Canonical-zero/constant-denominator branches introduce only constant exponents/heights. Nonzero denominators remain an external algebraic premise.

The six new tests inspect every literal `observe` call during each checked operation, coefficient/term/degree output bounds, and cumulative peaks with an inherited maximum. They cover 112 polynomial subcases (seven degrees through 2^127, four empty/cancel/collision patterns, four operations), explicit exponent carry from 127 to 128 bits, active/absent-axis partials, 45 Rational subcases (zero/equal/unequal/cancel branches), propagated multi-operation Rational metadata, and a deliberately unrelated 2049-bit historical observation. These finite controls support the source argument above; they do not establish universality by sampling.

## Whole-route proof and metadata are separate

Only four of the 15 producer inventory files changed from the original producer: `rf_bounds.py`, `test_certifier.py` (10 to 11 controls), and appended/explanatory text in `PROOF.md` and `README.md`. The marker changed accordingly. All other 11 producer files are byte-identical to `d37436ee7`, including every stored metadata envelope, recurrence artifact, admission implementation, candidate and blocked-route artifact, source manifest and whole-envelope builder.

The executable coefficient/degree/term/counter recurrences are unchanged. The repair adds a maximum to the observed-height return value. For common operands bounded by b>=2^20, input exponent bits and coefficient heights are already bounded by b; output degree bits for sum/product and the retained partial degree fit the same loose primitive majorant `(b+2)^16`. Consequently the original compound F and its M-fold B iteration still absorb the repaired maximum, including empty-product cases. There is no change to activation M, terminal weighted-degree K, finite descent T, terminal height H, counter total or retained logical S. S already includes integer/exponent payloads and K. This is the original proof's explicit degree control, not an inference from the physical hold.

The new metadata control regenerates `actual-PI-dot-envelope.json`, `rf-recurrences.json` and `whole-route-envelope.json` exactly, and checks the exact blocked-route artifact. The existing 13 independent controls separately retain catalog derivation, canonical control/guard checks, coefficient bounds, terminal division, whole-sum ordering and logical-storage checks. This follow-up does not replace their original mathematical premises or the external source-denotation acceptance.

Unchanged artifact SHA256 values:

| Artifact | SHA256 |
|---|---|
| whole-route-envelope.json | `627fbd2234c57d75ec9ef286cf93e4c7ca6c0593eae81a4a8180838e6c4ebd0d` |
| whole_envelope.py | `93408c2aa015385990894458a453b9d00b43385ccdf71d7f24d681123e15079d` |
| actual-PI-dot-envelope.json | `066b79faa2bfee91e3dcf352e1f91290a7c7c16996e0b902210142a22d8f3453` |
| actual-input-bounds.json | `d1da8cdbf4818e585a33b0115e0db334f88f647d3ba06827e26da29070d40955` |
| actual-seed-envelope.json | `9ba920ba94452b71cfd550c3aa59cf948ee9257ff4c20f671d504a665d571ce4` |
| rf-recurrences.json | `79b701989e16678ad2cae092d90723e3f64921ff2a1a204b45a593b871b5f14a` |

## Exact replay and frozen checks

One run of each supervisor was made, sequentially from the repository root:

```sh
/usr/bin/python -B research/codex-swarm/detector-admission/test_independent.py
/usr/bin/python -B research/codex-swarm/detector-admission/test_height_followup.py
```

The launch wrapper imported `test_height_followup`, took `frozen_snapshot()` before both supervisors, compared it after each, and saved equal before/after manifests. The actual script arguments were absolute paths under `/home/akilleez/LOCAL LLM/read-em-and-weep/`; the commands above use the equivalent repository-relative paths. The first supervisor launched four separate children; the second launched two. Exact child modes and outcomes:

| Script | Python flags | Entry argument | Cases passed | Wall seconds |
|---|---|---|---:|---:|
| test_independent.py | `-B` | `--child` | 13/13 | 2.921 |
| test_independent.py | `-B -O` | `--child` | 13/13 | 2.421 |
| test_independent.py | `-B` | `--producer-child` | 11/11 | 0.317 |
| test_independent.py | `-B -O` | `--producer-child` | 11/11 | 0.317 |
| test_height_followup.py | `-B` | `--child` | 6/6 | 0.117 |
| test_height_followup.py | `-B -O` | `--child` | 6/6 | 0.117 |

Total: **60 test-method executions**, with the 13 independent, 11 producer and six repair-follow-up cases kept separate in each mode. Each child had RLIMIT_AS=805306368 bytes (768 MiB), RLIMIT_CPU=59 seconds, and a supervisor `subprocess.run(..., timeout=60)` wall deadline. Direct `--child` entries self-install address-space/CPU limits; the supervisor supplies the wall timeout. Checks use exceptions/unittest rather than removable assert statements. All children exited zero. Times are control runtimes, not physical-route costs.

All 15 AC digests and its marker were authenticated before/between/after children. The outer 55-file local snapshot covered AC, RF/SR inventoried files and markers, local pinned dependencies, relevant source manifests and the immutable original report, and matched before and after the tests. The current independent suite additionally authenticated its declared immutable dependency bytes. Producer metadata's single pinned catalog request was supplied by the existing byte-only subprocess interceptor; the test runs launched no Git processes.

Key frozen/reviewer SHA256 values:

| File | SHA256 |
|---|---|
| producer-ready.json | `3bb840e094487e88f9a8aae0f6e12aa1be103ac871ca9d21e588bc2763727b47` |
| rf_bounds.py | `46f735013590ac3af675a32e7462bc482fcabe0ec0be43aef96837afb069a455` |
| test_certifier.py | `52bd9451c2323777cf7c710d2a4e32f370599078b3ac1c380b0f5e24192266a5` |
| test_independent.py (current) | `76257fe77dc33182fe3c8cfc922fac2193226f930a0960e788f551ccf8239264` |
| test_height_followup.py | `3caaaa87095235e3d11b44363ee5a8348eea6ebabba35a21604145079f59c107` |
| RF field.py | `4dade295de59741ceb54eb4574c58ffc82c8a1a17063fd1c081656a8b2069b01` |
| RF marker | `0d73ba3649961454a0795d408938abf9e857bd4e44feb47b99b666f2fd6e3340` |
| SR marker | `f7f6d523c5f55af2b571cf8912e7473ac21f1a5949354d8bbb6d94eaddec794a` |

Local replay receipts, outside the repository:

- `/tmp/acr-height-frozen-before.json` and `/tmp/acr-height-frozen-after.json`: both `cb2004cd26aa5847bd40ddeda0bbc6c9fa8a6d83714411c9bedfa478eae8159f`.
- `/tmp/acr-height-test_independent.py.log`: `41642f5a5bde4d0c748cdfab750506adf807e1c97eb3db4df8e6f71e79ab4e05`.
- `/tmp/acr-height-test_height_followup.py.log`: `5985c04afe88fb51670c0e4cba5b2c67b79d6a1c6cc1869c1f8506c08bb10294`.

No tests remain in flight. Publication and final replays belong to root.

## Physical disposition

**BLOCKED_ROUTE remains.** No actual byte-layout/workspace factor, RF/native-integer cap-unit reconciliation, authoritative current all-worker spent/reservation/live-allocation/alias/last-use ledger, or explicit physical execution release follows from this acceptance. Unknown fields remain unknown. The retain-all S is a logical bound; conditional layout-dependent bytes are still conditional. Historical allowances are not current caps or new scratch. A huge upper proves neither no-fit nor a lower bound nor algorithm-independent impossibility.
