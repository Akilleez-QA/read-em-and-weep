# Universal source2 commutant template

Preparation only: this Python 3 standard-library compiler constructs formal
equations, not an actual evaluator or authenticity verifier. No actual HM
tensor, selected actual source values, rank scan, rank, or source2 exclusion
is supplied or computed. The bounded integer/rational test fixtures are
synthetic and are neither actual nor abstract-source2 realizations.

Mathematical contract: [PR808 at3c2d80d5bbae109f810b1919fb0adbc2a1d0e392](https://github.com/Akilleez-QA/read-em-and-weep/tree/3c2d80d5bbae109f810b1919fb0adbc2a1d0e392/research/hm/source2-commutant-gate), `PROOF.md` equations
(3)–(6), (12)–(13) and `SPEC.md`. Immutable mathematical dependencies in
Akilleez-QA/read-em-and-weep:

- [#790, af0e03d26da5e47d18ae732291aca46f4d448dc5](https://github.com/Akilleez-QA/read-em-and-weep/blob/af0e03d26da5e47d18ae732291aca46f4d448dc5/research/hm/source2-first-constant-block/PROOF.md)
- [#791, 2cd033a4a5ba549d07330427cd779364cb83c0fb](https://github.com/Akilleez-QA/read-em-and-weep/blob/2cd033a4a5ba549d07330427cd779364cb83c0fb/research/hm/source2-pencil-endomorphism-algebra/PROOF.md)

From this directory:

```sh
python3 -B -m unittest -v
python3 -B template.py emit-json > /tmp/source2-template.json
```

Only the explicit `emit-json` command emits an artifact, to stdout. Import
defines constants and functions without constructing or writing artifacts.
`compile_template()` returns a fresh JSON-compatible object. No field
specialization is exposed in the production CLI or module.

The compiler uses M2=(A1,V2,P3,D4), M3=(Wp3,S3,T6), M4=(V2,P4,D3).
Each allowed W tensor edge has multiplicity one; absent target irreducibles
contribute no channel (in particular A→W). Each channel C has shape
(target multiplicity, source multiplicity), with distinct formal entries.
It emits every entry of `Xtarget*C - C*Xsource`. The 78 alpha and 75 beta
coordinates give 153 rows in 113 full square-matrix unknowns. Three ordinary
trace rows weighted by irreducible dimensions give 156 rows. No pencil
variable transformations are unknowns.

JSON uses zero-based indices throughout. Columns follow vertex order 2,3,4,
then the displayed block order, then row-major matrix entries. Channels
follow alpha then beta, source block order then target block order; symbols
and channel rows follow row-major order within each channel. Metadata records
the channel endpoints, rectangular shape, starting row/symbol offsets, symbol
names and coordinates, column coordinates, and each row's kind/coordinates.
The final rows are traces at vertices 2,3,4.

Each sparse entry is `[column, constant, [[symbol_index, integer], ...]]`:
its coefficient is the constant plus the indicated formal linear combination.
Entries and symbol terms are sorted, repeated terms combined and zero terms
removed. Channel coefficients have constant zero; trace coefficients have
no symbols. JSON keys are sorted with compact separators and one final newline.
No generated JSON is checked in.

A later fixed assignment over any characteristic-zero splitting field can
instantiate this universal template. Exact bases of **Hom(W⊗r,s) must be
fixed exactly**, together with all isotypic bases, the common W basis and
coordinate changes, to give these formal coordinates a tensor meaning.
This template does not impose tensor compatibility or authenticate assignments.
An actual source package is still required: pinned paths/commits/hashes and
cohomology derivation, exact field and denominators, G actions and isotypic/Hom
bases, simultaneous identification with the original negative tensors of #790,
and the equivariance/common-pencil checks in the gate's SPEC. Matching these
dimensions or passing linear conditions cannot establish source authenticity
or realization. The conditional rank and radical theorems in the gate remain
conditional on their pinned hypotheses.

Tests compare every unknown coordinate under three bounded synthetic assignments
against independent rectangular block multiplication, including fractional
values and negative entries. They check all channels and metadata, formal
identity cancellation, ordinary identity traces (41,54,37), coefficient
canonicalization, deterministic CLI output, fresh construction, and silent import.

Independent formal replay (`test_formal_replay.py`) compares all17,628 row/unknown coefficient entries with separately implemented polynomial block multiplication, keeping all153 tensor coordinates independent. Deliberately corrupted signs, symbol indices and trace weights must fail the verifier. This checks universal compiler correctness, not any actual-source statement.
