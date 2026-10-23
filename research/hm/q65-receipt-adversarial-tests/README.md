# q65 full-CLI synthetic adversarial regressions

A new, standalone standard-library regression artifact for the receipt-accounting
edge of proof-repair execution. This is not a mathematical certificate or a
replacement runner. **Zero mathematical shards were executed.**

## Reproduce

Requires Python 3.9+ (observed run: Python 3.12.14); no installation or network is
needed. From this directory:

```sh
python3 -B run_tests.py --output replay-results.json
python3 -B reproduce_boundary.py
```

Both commands may also be invoked by absolute path from an unrelated working
directory. Every tested invocation runs the unmodified pinned validator as a
separate process using `python -I -S -B ... aggregate ...`, not merely its
`validate_receipts` callable. Each process has a five-second wall timeout. The
full regression run uses 77 short CLI subprocesses and temporary fabricated logs.
There is no symbolic payload in this package and no mathematical producer is
imported or executed.

The new test code lives in `fixture_support.py`, `run_tests.py`, and
`reproduce_boundary.py`. `pinned/` contains three **unmodified** public input
files, not new production code. The package does not modify the production
validator or enable the shipped production execution gate.

## Pinned input

Repository: `Akilleez-QA/read-em-and-weep`.
PR: [#827](https://github.com/Akilleez-QA/read-em-and-weep/pull/827).
Exact commit: `fce4a9139101cd88eb50842174580fcd4fc6e160`.
Original path: `research/hm/q-middle-shard-contract/`.

| Input | SHA256 |
|---|---|
| q65_shards.py | 1d1abf9ca1b965b5a6467957b6875ae9e30c52d849daf0a3bac5d2b91373c393 |
| CONTRACT.json | c4ecc98cdad68bd2a7bef743778487adb6fd5b0a78b311aec2d85b9a330152ef |
| execution-lock.json | 81c05e416284a4b4216c9daa164e9760708f01112efc36b4136d1a8038155350 |

These match the publication hashes in
[REVIEW.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/fce4a9139101cd88eb50842174580fcd4fc6e160/research/hm/q-middle-shard-contract/REVIEW.md).
Every run verifies all three hashes before and after testing, checks the 73 unique
catalogue IDs and 8/55/10 category counts, and checks the shipped lock is disabled.
The contract's semantic digest is
`234140e8bb0eacf6e28fd015a73235265570e5dfece824eedb0d81d628d57727`.

Coordination was read through
[PR1 comment 6355174235](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6355174235).
This artifact addresses the
[full-CLI-versus-callable validation boundary](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6355027458)
without duplicating the mathematical runtime/runner work.

## Observed result

`observed-results.json` records the actual first completed run:

- 76 expected outcomes matched: 5 synthetic acceptance controls and 71 precise
  adversarial rejections.
- An additional forged-producer trust-boundary probe was accepted, as described
  below. It is **not** counted as a rejected attack or as a mathematical result.
- All rejection cases returned no success stdout and the exact expected final
  `ValueError` line. A nonzero exit for an unrelated earlier error cannot satisfy
  the test.
- First run elapsed wall time: 3.495 seconds. This is a machine-specific observation,
  not a performance guarantee.
- Input bytes and the disabled production gate remained unchanged.
- No synthetic receipt/log directory survives a successful or failed test exit.
  The retained report stores observations, not executable completion receipts.

## Coverage

Every case starts with a fresh complete 73-receipt synthetic packet. A single
specified mutation is then applied. Lock mutations recompute receipt lock hashes
so the intended prerequisite gate, not a stale hash, is exercised.

- Full log-byte validation: altered stdout, changed line endings, missing log,
  blank/partial logs, missing log path, traversal, absolute path and symlink escape.
- Exact final-nonblank-line semantics: trailing error/later work, marker substring,
  quoted/padded/truncated marker, different unit marker, NUL and ANSI decoration,
  and a self-consistent wrong marker in both log and receipt.
- Accepted controls: a full packet, reversed receipt order, trailing blank lines,
  CRLF line endings and an exact marker without a final newline.
- Completeness: separately missing each of the eight global prerequisites, missing
  a harmonic/trace unit, duplicate global/harmonic/trace IDs and an unknown ID.
- Metadata: receipt schema/fixture isolation, contract/runtime/input bindings,
  nonzero/boolean/string exit codes, failure status, timeout/termination, disabled
  assertions, missing/extra/failed check and negative elapsed time.
- Runtime prerequisites: disabled lock, wrong contract pin, absent or nonhex runtime
  pins, missing/extra/unreviewed helper coverage, absent certificates and unfrozen
  Python/SymPy metadata. Contract digest tampering is also rejected.

## Synthetic/production distinction

The aggregate CLI has no fixture mode. To reach all its production-path checks,
temporary receipts use `fixture_only: false` and a **temporary synthetic lock**.
They also carry `synthetic_test_artifact: true`; every generated log starts with a
synthetic warning except cases explicitly replacing it. Runtime/certificate hashes
are deterministic hashes of strings saying that no execution/evidence exists.
None is represented as a real review, execution, helper certificate or mathematical
PASS. The checked-in disabled lock is never overwritten.

The pinned validator's raw success string is `execution_receipts_complete`.
The report preserves that actual stdout inside explicitly synthetic observations,
not as a claim that any real execution completed.

## Producer-trust boundary (not a newly claimed bug)

`reproduce_boundary.py` changes one fabricated log to:

```text
SYNTHETIC: no checks were run
ERROR before forged marker
Q65_UNIT_COMPLETE q65-shards-v1/global/primitive-cg
```

It recomputes that log's receipt digest. With the other 72 fabricated receipts
self-consistent, the pinned CLI exits 0 and prints `execution_receipts_complete`.
The negative regression `marker_then_error` rejects the opposite ordering.

This precisely demonstrates the stated boundary: hashes authenticate consistency
with supplied bytes, not the honesty or mathematical correctness of the producer.
An exact final marker is not independent evidence that the preceding checks ran.
PR827's [contract](https://github.com/Akilleez-QA/read-em-and-weep/blob/fce4a9139101cd88eb50842174580fcd4fc6e160/research/hm/q-middle-shard-contract/SHARD-CONTRACT.md)
already requires independent producer review and warns that a malicious or
incorrect producer can report false checks. No new defect is claimed from this
accepted probe. Do not broaden these results to arbitrary malformed JSON, race
conditions, actual runtimes, algebra, or source-instance validity.
