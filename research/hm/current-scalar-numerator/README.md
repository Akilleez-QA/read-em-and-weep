# Exact current-L scalar numerator regeneration

This package regenerates the exact rational numerator for the current scalar map

\[
L(X_{02},X_{13})=X_{02}[0,0]-X_{13}[10,0].
\]

It extends the unsigned source bridge in [PR #35](https://github.com/Akilleez-QA/read-em-and-weep/pull/35).
It contains only small source files and exact input data, not a committed
coefficient DAG, numerator DAG, quotient checkpoint, or coefficient array.

## Dependency and reproduction

Python 3.10+ and Node.js 18+; standard libraries only. Check out the stacked branch
with both public sibling directories:

```
research/hm/current-scalar-source-bridge/
research/hm/current-scalar-numerator/
```

The bridge files are pinned to PR #35 commit
`6032b64d3f748c7ac37cb283db4a527e49d06ac8` in `expected.json`.
From `current-scalar-numerator`, run:

```sh
python3 verify_numerator.py
python3 test_source_checks.py
```

For a different checkout layout, pass `--bridge /path/to/source-bridge` to either
command. Run assertion-enabled Python, without `-O`. The complete verifier first
runs the bridge's 1,710 primitive rational-function identities and generator
checks, then regenerates the reduced model, unsigned carrier (2,3,4) DAG, and
current-L numerator. It reads no precomputed DAG. All generated files live in a
temporary directory by default; neither source package is modified.

To retain generated data, use a new directory:

```sh
python3 verify_numerator.py --output-dir /tmp/current-L-fresh
```

Outputs are `reduced-model.json`, `carriers-234.json`, `verification.json`, and
`numerator/local-numerator.dag.json` plus its `local-representative.report.json`.
An existing output directory is rejected. Each Node subprocess has a 1,536 MiB
old-space limit and a 300-second timeout; the bridge verifier has a 900-second
outer timeout. These are resource guards, not mathematical truncations.

For a previously regenerated, pinned carrier DAG, the construction-only command
is:

```sh
node build_local_representative.js --source /path/to/carriers-234.json --output-dir /tmp/new-numerator
```

This shorter command checks the carrier hash and exact denominator clearance. It
does not run the independent input-identity checks; use the full verifier for
those checks. Its output directory must not already exist.

## Exact expression and mask coverage

On the affine chart `v0=1`, let `vj=e_j(x1,x2,x3,x4)`, with `e0=1`, and set

\[
F_j=v_j^4-\prod_{k\ne j}v_k,\qquad h_j=v_jF_j.
\]

The 16 exposed factors are `x1,...,x4`, `x1^2-1,...,x4^2-1`, `v1,v2,v3`, and
`F0,...,F4`. Every inverse used by the unsigned C234 DAG is checked by exact
sparse polynomial expansion against these factors. All 18 chart denominator
identities are independently checked against the freshly regenerated MODEL.

The exact scalar prefactors are

\[
a=\operatorname{row}_{10}(I_1P_1I_2),\qquad
b=\operatorname{column}_{0}(P_2H^1_1).
\]

Their four numerator contractions and denominator factors are verified directly
against MODEL by 23 integer polynomial identities. The prefactors are supplied
small algebraic data, not the output of a claimed historical generator.

For carrier `j` and nonempty subset `S`, the feature moment is

\[
\mu_{j,S}=\frac{\prod_{i\in S}x_i^3(x_i^2-1)}{h_j}
\left[\prod_{i\in S}x_i^5\right]h_j,
\qquad \mu_{j,\varnothing}=1.
\]

The bracket means simultaneous leading coefficient in the selected coordinates,
leaving the unselected coordinates as polynomial variables. The checker
reconstructs all 64 moments for carriers 1 through 4 and proves 128 integer
identities from the coordinate operators
`T_i(P)=(x_i^5-x_i^3)[x_i^5]P`. The constructor uses carriers 2, 3, and 4.

The source is group-multilinear, so there are 256 feature codes. For each code the
verifier exhaustively compares the monomial incidences in the 4,096 independent
mask triples with those in the product of the three feature sums. This is a
universal identity in formal mask weights, not a numerical sample. The actual
mask-basis routine used by the constructor is included unchanged and compared
against an independent definition. Exactly 242 feature products are nonzero;
zero products do not discard mask choices.

Writing `Mbar` for the four contracted C234 entries, the constructed expression
is

\[
f=-a\,\overline M^{\mathsf T}b,
\qquad N=f\,h_1^{13}h_2^{14}h_3^{14}h_4^{14}.
\]

C234 is unsigned. The constructor applies exactly one explicit J2 minus.
`test_constructor.js` executes the actual scalar contraction block over an
independent exact BigInt ring on all four matrix basis entries, checks the
transpose and one minus call, and rejects missing and doubled-minus mutations.
Rational arithmetic fixtures check the tagged ring's reduced BigInt fractions
and refusal of unproved inverses. No modular lift or floating-point coefficient
arithmetic is used.

## Pinned result and adaptation

Fresh execution reproduces:

- Carrier C234: SHA-256
  `31cd62eb3062801ca19073464c276fbe016fa4024fbcdcf48d3893358e3fcc18`.
- Numerator N: 4,186,496 bytes; 207,925 retained nodes from 208,871 constructed
  nodes; SHA-256
  `0254c93650e6ca6c1e9cbbb01810704eede98d10d0b75229fcff5d8fa2123e66`.
- Output factor powers:
  `[11,11,11,11,0,0,0,0,12,8,7,0,12,5,4,7]`.

The numerator graph is division-free; all exposed output factor powers are
nonnegative. Numerical coefficients remain exact rational numbers. The verifier
also checks graph ordering, permitted operations, reduced constant fractions,
output roots, metadata, and the absence of remaining denominator tags.

`tagged_ring.js` and `weighted_mask_moments.js` are unchanged source copies. The
historical constructor is adapted only for its helper import and explicit input
and fresh-output paths; its mathematical operations and JSON emission are
unchanged. The inverse-seed file is narrowed to C234 (18 inverse seeds); its tags
and six model-denominator rows are unchanged. The three other small JSON inputs
are unchanged. Historical input hashes and publication-file hashes are retained
in `expected.json`. The historical full inverse file covered other carriers;
this package does not claim to check those unused entries.

`test_source_checks.py` performs a fresh complete reproduction and verifies
rejection of altered tag definitions, inverse factors, omitted seeds, MODEL
factorizations, prefactors, moments, feature assignments, missing features,
nonmatching output bytes, and attempted overwriting of completed outputs.

## Proof boundary

There are two distinct claims here:

1. **Byte regeneration:** small scripts and inputs plus the pinned PR #35 bridge
   reproduce the named numerator DAG exactly.
2. **Algebraic source checks:** independent exact identities establish the tag
   formulas, inverse factorizations, MODEL denominator ties, prefactors, and
   all-mask moment contraction used in the declared expression.

A hash match proves byte identity, not geometric source attribution. The checks
above provide explicit algebraic evidence beyond hashes, but identifying the
expression with the geometric class still uses the carrier-merger, scalar
comparison, and pole/regular-section hypotheses in
[PR #34](https://github.com/Akilleez-QA/read-em-and-weep/pull/34). This package does
not prove those hypotheses just by constructing N, and it does not perform a
tensor-simplex comparison.

No leading-axis window, normalized circuit, secondary reverse jet, quotient
coordinate, or residue is evaluated here. The downstream 81-coordinate scalar
result and its independent terminal reconstruction remain separate certificates.
The full obstruction is undetermined. No additional scalar map or new-map source
is included.
