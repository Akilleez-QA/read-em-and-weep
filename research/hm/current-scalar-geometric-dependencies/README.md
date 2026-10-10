# Geometric dependencies of the original scalar numerator

This package supplies exact, reproducible certificates for the original scalar

\[
L(X)=X_{02}[0,0]-X_{13}[10,0].
\]

It adds the homogeneous primitive, carrier-merger, frame, and completed-scalar
pole evidence needed by the existing scalar comparison. It also explains the
degree-273 cancellation and the separate coordinate factor 48 in the exact-Q
leading sources. No residue, quotient, or scalar coordinate is evaluated here.
The full obstruction remains undetermined.

## What is established

- All 451 nonzero homogeneous primitive entries have the stated
  carrier-owned divisor bounds, including hidden `v0` factors.
- 3,090 exact scalar/matrix-entry identities verify the contraction,
  special rows, scalar chain map, and merged first-carrier formula.
- The actual mixed-residual operation graph, followed by its sparse scalar
  prefix, gives primary pole bound 13 and legal-line pole bound 1.
  Computed tail and prefix fields are checked independently; literal
  `completed` summary fields are not accepted as evidence.
- The physical-frame argument identifies the bounds on the other product
  charts with the same expression. Its 901 elementary frame identities
  support that argument; they are not a full infinity-chart scalar replay.
- With the pinned all-mask construction, the clearing powers are
  `(13,14,14,14)` and the numerator is a regular section of
  `O(272,272,272,272)`. Thus its syntactic degree-273 layer vanishes.
- The factor `product_(j != i) x_j^48` in the degree-272 axis source has a
  separate polynomial-circuit divisibility proof. It does not depend on
  degree-273 vanishing, residue evaluations, or a finite-field computation.

The degree statement concerns the exact declared expression. Identifying its
cohomology class with the intended deformation obstruction additionally needs
the ambient residual/first-order source attribution described in
[source identity and scope](source-identity.md). This package does not certify
that additional identification merely by reproducing hashes or pole bounds.

## Read the arguments

1. [Source identity, the geometric minus, and carrier merger](source-identity.md)
2. [Physical frames and the completed scalar pole certificate](frames-and-poles.md)
3. [Regular-section cancellation and the independent factor 48](degree-and-factor48.md)

The general ordered-prism, scalar order-change comparison, local-duality,
and finite-model arguments are already in the
[pinned scalar proof package](https://github.com/Akilleez-QA/read-em-and-weep/tree/a100f4e0be453d6e182320b792359f8a04e32b4d/research/hm/current-scalar-proof).
They are not repeated here.

## Reproduce the small certificates

Python 3.10+, SymPy (tested with 1.14.0), and Node.js 18+ are required.
Use assertion-enabled Python; optimized `-O` and `-OO` invocations are rejected.
No network, environment variable, generated numerator, or external data file
is required for the default checks. Run from this directory, or give its
absolute path from any other working directory:

```sh
python3 verify.py
```

The verifier resolves bundled files relative to its own location, runs serially,
uses a temporary working directory, and does not modify its inputs. Each child
has a 300-second timeout; the Node heap is capped at 512 MiB. It reruns the
symbolic identities, denominator allocations, actual abstract pole graph,
chart/line identities, source-formula alignment, and rejection fixtures.

To bind the bundled exact function excerpts to the complete public generator
from the bridge checkout, add:

```sh
python3 verify.py --public-generator \
  ../current-scalar-source-bridge/public_generate_hm_mask_coefficients_reduced.js
```

This checks the complete generator hash and exact function excerpts. It does
not regenerate the coefficient DAG. The bridge and numerator packages have
their own end-to-end regeneration commands.

The four normalized axis DAGs are deliberately not bundled. After regenerating
them with the pinned jet package, optionally check one with:

```sh
python3 checks/verify_factor48.py --axis 0 \
  --normalized /tmp/current-L-jets/axes/axis-0.normalized.json
```

Repeat with axes 1, 2, and 3 and their corresponding files. This is a read-only
linear traversal of polynomial syntax, not polynomial expansion or quotient
evaluation. `certificates/factor48-axes.json` records those checks for all four
exact-Q source pins. The default verifier tests the support rule on a small
fixture; it does not pretend to have reread unbundled axis files.

## Public dependencies and provenance

The model and 451-entry divisor seed table are bundled in `data/`. The model's
canonical compact-JSON SHA-256 is
`b6b532c4bab5787397a4cddde34210c12fae71853b30cb73ecbe8a9c2b4826b2`.
The original scalar numerator SHA-256 is
`0254c93650e6ca6c1e9cbbb01810704eede98d10d0b75229fcff5d8fa2123e66`.

- [Primitive/source bridge](https://github.com/Akilleez-QA/read-em-and-weep/tree/6032b64d3f748c7ac37cb283db4a527e49d06ac8/research/hm/current-scalar-source-bridge):
  1,710 exact primitive reduction identities and the unsigned residual source.
- [Scalar numerator](https://github.com/Akilleez-QA/read-em-and-weep/tree/d7efdbeb2def45af2fcfe2253f7d1eb61ab5bf1c/research/hm/current-scalar-numerator):
  prefactors, all-mask moment identities, the transpose and single-minus
  constructor check, and exact numerator regeneration.
- [Exact-Q jet sources](https://github.com/Akilleez-QA/read-em-and-weep/tree/67910d41054e5237f4dbe77fb32c3d3ad5ca6897/research/hm/current-scalar-jet-sources):
  exact leading/normalization transformations and all-axis/pair source pins.

`pins.json` records the exact public commits, paths, and source pins.
`manifest.json` binds this package's checkers and data. The homogeneous checker
and pole evaluator retain the completed algebraic formulas; the packaged
versions load their small model/seed inputs from relative files. The independent
seed audit, computed-bound wrapper, source alignment, and support traversal
make explicit what each receipt checks.

No characteristic-13 or characteristic-71 coefficient array is an input. The
global bound 73 is not used in place of the completed scalar bound 13.
