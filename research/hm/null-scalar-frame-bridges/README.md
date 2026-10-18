# Conditional scalar and moving-frame bridges

This portable package preserves two narrow mathematical/source-review results:

- `scalar/PROOF.md`: the frozen scalar function lowers to the specified 25-monomial, four-block endpoint/supertrace/gerbe polynomial.
- `frame/PROOF.md`: the frozen moving-frame code implements the split connection under the stated field, shape, localization, contraction and denotation premises.

These are conditional implementation bridges. Actual primitive contraction/denotation, exact-field correctness, legal owners and localization remain assumptions. No physical model, source, owner, matrix payload or jet is evaluated. No whole-model correctness, ID0=0, transport, HPL or aggregate admission is established. Permission to execute production code is not implied.

## Exact premises

The scalar bridge requires exactly four legal square blocks in the documented endpoint/direction order, ranks (5,15,10,2), weights (-1,1,3,5), signs (-1,1,-1,1), correct q/block denotations, and exact arithmetic. Short tuples would truncate the production zip and are outside the theorem. Complementary-direction factorization applies only to the distinct directions identified in the proof; repeated derivatives require additional y-derivative terms.

The frame bridge requires a localized commutative exact coefficient field, a Leibniz derivation, correct scalar/matrix/entrywise derivative operations, invertible nu and pivot coordinate, correctly shaped rectangular matrices, legal directions/masks and correctly denoted carrier data. The explicit contraction equations and dimensions are listed in `frame/PROOF.md`. They are declared mathematical premises, not authenticated actual-model identities. The optional direct left-inverse check also declares delta gamma=0; the minimal square right-inverse argument does not need that additional equation. The proof does not audit JavaScript jet arithmetic or transport.

## Inputs and immutable pins

`pins.json` retains every original source SHA-256 and every available immutable commit/path URL. It has no machine-specific paths. Source files are deliberately not redistributed. Supply the exact bytes separately. All six inputs now have immutable commit/path URLs. The original field and compiler entries supplied only content hashes. Their bytes were reconciled with retained commit-pinned fetch records by matching SHA-256, byte length, and independently recomputed Git blob identifiers. `provenance-reconciliation.json` records that limited evidence. Neither file is executed or semantically verified by hashing it; no network re-fetch was performed.

Either arrange files beneath a chosen SOURCE_ROOT according to each pin's `source_root_path`, or pass explicit paths. Different source revisions occupy separate commit directories.

From this package directory, using Python 3.9 or newer and only the standard library:

    python scalar/check.py --source-root SOURCE_ROOT
    python -O scalar/check.py --source-root SOURCE_ROOT
    python frame/check.py --source-root SOURCE_ROOT
    python -O frame/check.py --source-root SOURCE_ROOT

Alternatively:

    python scalar/check.py --raw-engine RAW_ENGINE --source-formulas SOURCE_FORMULAS --first-order FIRST_ORDER --denotation DENOTATION --field FIELD --compiler COMPILER
    python frame/check.py --raw-engine RAW_ENGINE --source-formulas SOURCE_FORMULAS --first-order FIRST_ORDER

Explicit file arguments override the source-root location for that input. The scalar checker verifies six inputs; the frame checker verifies its original three. Inputs are read as text/bytes and the raw engine is parsed using ast. No supplied source is imported, executed, evaluated or compiled into executable code. Checkers print JSON to stdout without modifying input files or the pin manifest.

## Reproducibility correction and controls

The original checkers used Python assert statements. Those assertions disappear under -O; an original optimized run would therefore not establish enforcement. The packaged checkers replace every assert with an explicit `require` call that raises on failure, preserving the same mathematical tests under normal and optimized execution. This strengthens reproducibility, not the mathematical theorem or its premises. Original proof/checker directories are unchanged.

`logs/scalar-normal.json`, `logs/scalar-optimized.json`, `logs/frame-normal.json`, and `logs/frame-optimized.json` record fresh passing runs of these packaged checkers. Scalar controls reject six semantic formula mutations plus one ordered-word mutation. The reversed-word test is only source-word preservation, not a numerical refutation of cyclic ordinary matrix trace. Frame controls reject eight static source-contract changes; they are not numerical counterexamples. Formal inverse reductions use declared equations and invented noncommutative words.

`python test_controls.py --source-root SOURCE_ROOT` independently runs positive controls and deliberately corrupted-pin and corrupted-expected-polynomial checks in both modes. It copies only this package's checker/manifest into a temporary directory; it never runs production source. `logs/control-tests.json` records these results. No private operational records or source snapshots are included.

Verify package integrity from this directory with:

    sha256sum -c SHA256SUMS

The manifest uses relative paths and covers all distributed files except itself. Integrity hashes do not prove the mathematical premises or public accessibility of source URLs. This package was prepared locally and has not been published.
