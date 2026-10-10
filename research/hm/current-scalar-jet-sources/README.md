# Current scalar leading and secondary source regeneration

This package regenerates the completed **original current-L exact-Q** source
circuits from the pinned scalar numerator. It writes four unfiltered leading
axis DAGs, their exact concrete-tag normal forms, all 12 ordered compact
secondary-pair jets, and the corresponding integer-clearing metadata.
Every one of these 32 generated artifacts must match its original SHA-256
byte-for-byte. It also independently recomputes conservative support enclosures.

It does **not** evaluate any polynomial quotient, homogeneous projector, scalar
coordinate, or generating series. It does not contain the newer second-map
`scalar-lminus-rational` investigation.

## Dependencies and quick start

- Python 3.9+ (standard library only; do not use `python -O`).
- Node.js with BigInt support (tested with Node 24).
- Sibling package `../current-scalar-numerator`, including its unchanged
  `tagged_ring.js` and the numerator builder.
- To regenerate the numerator from its source, the numerator package in turn
  requires sibling `../current-scalar-source-bridge` and its source inputs.
- No sealed/generated DAG, quotient, checkpoint, or coefficient array is a
  committed input to this package.

From the parent directory containing the three published sibling packages:

```sh
python current-scalar-numerator/verify_numerator.py \
  --bridge current-scalar-source-bridge --output-dir /tmp/current-L-numerator
python current-scalar-jet-sources/regenerate.py \
  --numerator /tmp/current-L-numerator/numerator/local-numerator.dag.json \
  --output-dir /tmp/current-L-jets --jobs 1
```

Both output directories must be new. Replace them when repeating a run. The jet
script defaults to sibling `current-scalar-numerator`; use
`--numerator-package PATH` to override its location. Omitting `--output-dir`
uses a temporary directory and removes generated files after verification;
`--receipt NEWFILE.json` preserves the small receipt separately. Existing
outputs are never overwritten, and no original sealed directory is a write
location.

The numerator must have exact SHA-256:
`0254c93650e6ca6c1e9cbbb01810704eede98d10d0b75229fcff5d8fa2123e66`.
The exact tagged-ring implementation hash is listed in
`implementation-provenance.json`.

Small, fast arithmetic/normalization tests:

```sh
python current-scalar-jet-sources/test_sources.py
node current-scalar-jet-sources/test_leading_two_jet.js
```

The JavaScript fixture accepts an optional explicit `tagged_ring.js` path.
It tests the two extracted coefficients of every concrete tag and compound
fixtures on all four axes at fixed small integer assignments of the remaining
coordinates, including cancellation without lowering the degree
bound and rejection of negative exponents. Python fixtures cover reverse-shift
truncation, denominator clearing using discarded terms, support failures,
concrete normalization, source binding, and refusal to overwrite outputs.
These fixtures supplement the all-32-pin regeneration test, not a full symbolic
verification of the geometric source.

## Output contract

```text
axes/axis-I.dag.json
axes/axis-I.normalized.json
axes/axis-I.support.json
axes/axis-I.receipt.json
pairs/pair-IJ/graded-jet.compact.json
pairs/pair-IJ/integer-clearing.json
axis-I.log
regeneration-receipt.json
```

Here `I` runs from 0 to 3, and `J` runs over the three other axes. `pins.json`
contains the exact `leadingSHA256` / `normalizedSHA256` fields under `axes[I]`
and `compactSHA256` / `clearingSHA256` under `pairs[IJ]`. A successful receipt
says `ALL_32_EXACT_SOURCE_PINS_MATCH`. It explicitly records that polynomial
quotient evaluation and geometric source proof were not performed.

The normalized artifact's `input` field preserves its historical **relative**
source label, such as
`math-repair-only/scalar-local-residue-rational/leading-jets/axis-0.dag.json`.
That string is inert provenance metadata: the normalizer reads the explicit
CLI input path, not that label. No private absolute paths or required original
workspace locations are present in published inputs. Keeping the relative
labels preserves the original normalized, compact and clearing byte hashes.
No historical absolute-path configuration hash is reused or claimed here.

## Mathematical operations and assumptions

1. `leading_two_jet.js` propagates the coefficient at a conservative syntactic
   degree bound and the coefficient one below. Products add bounds; sums take
   maxima. Cancellation **does not lower** a stored bound. The concrete tag
   substitutions are the coordinate variables, their `x_i^2-1` factors,
   elementary symmetric polynomials, and the five existing F-tags.
2. The pinned numerator's bound is 273 on every axis, so the two emitted layers
   are degrees 273 and 272. The concrete normalizer uses exact rational field
   identities and cap 64, with no finite-field input or Frobenius shortcut.
3. Exact support induction on normalized output 1 exposes each of the three
   surviving coordinate factors to exponent 48, with coordinate upper bounds
   at most 212 and total-degree upper bound 449. Removing the three factors
   gives coordinate bound 164 and total bound 305. These are conservative
   enclosures, not assertions that every bounded monomial occurs.
4. `build_compact_secondary_jet.py` retains six reverse coefficients from
   second-coordinate bound 164. A summand shifted by at least six is zero in
   the formal truncated reverse variable ring. All later shifts are
   nonnegative. No remaining coordinate is set to 1 and no homogeneous
   projector is evaluated during source construction.
5. Clearing uses `Z_j = D_j F_j`, computing each `D_j` from **all original
   normalized terms**, even terms omitted by reverse truncation. Every stored
   weight `D_node * c / product(D_child^e)` is checked to be integral with
   Python `Fraction`; the root denominator and weight are similarly exact.

The degree-273 layer is not proved zero by this package. Its vanishing requires
an independently justified identification of this exact rational expression
with the regular O(272)^4 section. Likewise the geometric source, unsigned
coefficient convention, exact-Q characteristic interpretation, one explicit
J2 minus, and applicability of the degree/support/projection gates remain
source-proof obligations addressed by the separate source bridge/proof work.
Hashes identify which bytes were regenerated; they do not prove those claims.

### Historical metadata and the evaluator gap

To preserve exact source pins, compact pairs with first axis 0, 1, or 2 retain
the historical `gradedOutputs` for the m2220 projection: remaining degree
`105+r`, source first degree 272, second degree `212-r`, and original degree
685. Pair 01 also retains its historical query edge. The first-axis-3 pairs
carry all46 unfiltered-family metadata instead.

The underlying compact circuits in **all 12 pairs** retain every relevant
remaining homogeneous degree; those metadata do not execute a filter. A
subsequent general scalar evaluator must derive its homogeneous degree,
second-axis reverse layer, role permutation, and b-degree window from the
actual query. It must not mistake the historical m2220 annotation for a
universal projector.

This package deliberately stops before that evaluator. It does not construct
or evaluate the coefficient-ring polynomial products, apply rational quotient
kernels, extract all 24 ordered quotients, certify their coefficient hashes,
or replay the completed all-81 scalar result. Those need a separate audited
source-to-quotient computation and the external mathematical source proof.

## Resources, parallelism and verification

Generated source artifacts total 249,022,910 bytes (about 237.5 MiB), excluding
small logs/receipts. Historical per-stage measurements were approximately
3 seconds for one leading DAG, 12 seconds for normalization, 14–16 seconds per
compact pair, and 7–8 seconds per clearing file, with a largest stage near
0.5 GiB RSS. Budget roughly 6 minutes serial and at least 1 GiB free memory;
allow 2 GiB for comfortable overhead. Actual timing depends on the machine.

`--jobs 2` runs two independent axis processes; budget at least 2 GiB.
More concurrency is optional (`--jobs 3` or `4`) and multiplies memory needs.
The default 120-second leading/normalization timeout and 600-second whole-axis
timeout can be increased with `--stage-timeout` and `--axis-timeout`. A failed
or interrupted run is not a successful receipt; it leaves explicit-output
files for inspection and must be restarted in a fresh directory.

`regeneration-test-report.json` records the fresh full run performed for this
package, including all 32 matching hashes, versions, parallelism and runtime.
The fresh two-worker run took 161.314 seconds with Python 3.12.14 and Node
v24.19.0. The output directory used for that test is outside the package. Only compact
source code, pin metadata, fixture tests, and the small verification receipt
are published.
