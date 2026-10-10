# Portable exact-Q quotient evaluator

This package evaluates the twelve accepted compact source pairs in the graded
ring Z[v,w,z]/(v^6,w^37,z^22), retaining a common rational denominator. Each
pair has two orientations of the remaining axes, giving 24 full quotients.
No scalar coordinate is selected by this evaluator.

The numerical evaluate() body matches the historical exact-Q v3 body after
three explicit adaptations: JSON checkpoint serialization, the checkpoint
filename, and an additional independently recomputed liveness guard. The
portable input contract is new. It is bound to exact source bytes and
mathematical payload digests, and never pretends to be an old configuration or
source-proof receipt. `test_evaluator.py` verifies the historical body digest.

## Fast checks

Python 3.10+, standard library only, with assertions enabled:

```sh
python3 test_evaluator.py
python3 test_wrapper.py
python3 test_roles.py
```

The tests compare signed non-dyadic rational fixtures, cancellation, ordinary
71st powers and checkpoint/resume with an independent Fraction polynomial
oracle. They reject foreign contracts, incorrect denominators, bad frontier
indices/liveness, unpinned source files and malformed role permutations. Final
terminal products are reconstructed independently with Fractions. These small
fixtures do not evaluate the actual geometric source.

Six mocked wrapper tests cover success, cooperative resume, the two-attempt
limit, process failure, hard timeout and refusal of a nonempty output directory.
They check the requested OS memory limit and subprocess timeout arguments;
they do not pretend that a mock is a full operating-system stress test.
All 24 synthetic role permutations are also tested, each with checkpoint/resume
and an independent Fraction-oracle comparison.

## Source inputs and bounded actual evaluation

First run the separate current-scalar-numerator and current-scalar-jet-sources
regenerators. The source directory must contain
`pairs/pair-IJ/graded-jet.compact.json` and `integer-clearing.json` for all twelve
ordered pairs. No source DAG or checkpoint is bundled here.

```sh
python3 check_sources.py --sources /path/to/generated-sources
python3 run_quotient.py --sources /path/to/generated-sources --roles 0123 --output /path/to/new-edge-output
python3 validate_quotient.py --config /path/to/new-edge-output/config.json
```

The source paths shown are placeholders supplied by the person running the
command. Each edge output directory must be new and empty. The wrapper allows
at most two attempts, with a 900-second hard wall, an 840-second cooperative
checkpoint and a 2 GiB address-space limit per attempt. It runs one process at
a time. It archives the first cooperative attempt before resuming, verifies
the remaining source references and live denominators, and stops on failure,
hard timeout or exhaustion. This guarded runner requires a POSIX platform with
`resource.RLIMIT_AS` and process-group signals.
The post-run Fraction terminal validator executes outside these per-attempt
subprocess limits; it is a separate arithmetic check.

Checkpoints are plain JSON, not executable pickle data. They remain tied to
the new configuration, program and input hashes. A completed output is
immutable to the evaluator. Do not bypass guards or delete prior outputs to
claim an uninterrupted run.

`expected.json` pins all twelve accepted compact and clearing files, their
mathematical content, and all 24 historical exact coefficient hashes. The
validator checks the complete coefficient array, denominator and nonzero
count, and independently reconstructs the terminal product using Fraction
arithmetic. Run metadata and timing are new; only the mathematical coefficient
hash is expected to match the historical output.

The earlier first-axis 0/1/2 pair files contain historical single-target
projection metadata. The evaluator deliberately evaluates the entire compact
source and retains all homogeneous degrees separately, rather than using that
metadata as a filter. The current 46-coordinate selector belongs to the
separate supplied-quotient result package.

## Verification and limits

The portable synthetic evaluator, JSON resume and input-rejection fixtures
pass. Exact source generators and expected source/result hashes are separate
evidence. A full fresh 24-edge replay is not claimed by this publication;
any representative actual run is reported separately with its exact roles and
coefficient hash. The numerical core's historical acceptance does not replace
testing the relocated contracts and checkpoint changes.

This is a source-to-quotient arithmetic stage. It does not independently prove
that the source represents the geometric obstruction, discharge the scalar
projection's pole/support hypotheses, or prove that the full obstruction
vanishes. Those mathematical dependencies remain explicit in the scalar proof
and source packages.
