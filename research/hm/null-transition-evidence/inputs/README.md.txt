# Ambient attribution of the original scalar residual

This package identifies the unsigned rational residual used by the original
scalar `L(X)=X02[0,0]-X13[10,0]` with the full-sign component of an explicitly
specified second-order module obstruction. It concerns the rank-two bundle
represented by the four-term Horrocks–Mumford complex on `C^4`, where
`C: y^2=x^3-x`, and the particular noncentral algebroid second jet below.

The result is an attribution and closedness statement. It does not evaluate
the scalar, prove that the full obstruction vanishes, reconstruct a
second-order module, or establish an equivalence of the entire second jet
with a different central/gerbe presentation.

## Read in order

1. [Declared ambient deformation and full module defect](ambient-second-jet.md)
2. [Exact first-order lift and source dictionary](first-order-source.md)
3. [Closure, full-sign extraction, and choice independence](closure-and-characters.md)

The first-order lift is explicit: the scalar part is an unsymmetrized Čech
transgression, and the trace-free part is a rank-two determinant-one identity.
There is no unspecified first-order primitive in the conclusion. The source
dictionary explains the normalized line-frame jets and matches the actual
PR #35 `first`, `crossResidual`, and `globalCross` formulas, including all
mixed terms and their coefficients.

## Dependencies and reproduction

Python 3.10+, SymPy (tested with 1.14.0), and Node.js 18+ are required.
The package reuses, rather than duplicates, two small sibling dependencies:

- [PR #40's geometric package](https://github.com/Akilleez-QA/read-em-and-weep/tree/dc60a859a0157b1d2d1b57b37324509abc22c600/research/hm/current-scalar-geometric-dependencies),
  at `../current-scalar-geometric-dependencies`: the exact model, physical
  frame/contraction identities, and public generator excerpts;
- [PR #34's scalar proof](https://github.com/Akilleez-QA/read-em-and-weep/tree/a100f4e0be453d6e182320b792359f8a04e32b4d/research/hm/current-scalar-proof):
  the pinned finite-model Ext¹/deck-rank implementation and scalar comparison.

Run from any working directory, using the appropriate path to this package:

```sh
python3 verify.py
```

If the sibling directories have other names, specify them explicitly:

```sh
python3 verify.py --geometric-package /path/to/geometric-package \
  --scalar-proof /path/to/scalar-proof
```

To compare the exact excerpts with the complete public generator, also give:

```sh
python3 verify.py --public-generator \
  ../current-scalar-source-bridge/public_generate_hm_mask_coefficients_reduced.js
```

No network is used. The verifier checks its manifest and dependency hashes,
executes in a temporary directory, and does not modify any input. It rejects
Python optimization mode. Child processes have 300-second wall-time limits;
Node has a 768 MiB heap limit. No generated numerator, coefficient array,
residue extraction, quotient calculation, or large source-DAG replay is run.

The checks cover:

- all 36 determinant-one transitions, by integer polynomial identities;
- universal unsymmetrized transgression and local scalar-source expansion;
- elliptic derivative/line-connection identities and rank-two trace algebra;
- the formal order-two defect expansion and the four mixed Moyal terms;
- exact source excerpt binding, including final row normalization;
- fresh rational Ext¹ ranks by deck weight, using the actual pinned source,
  with its classical differential compared to the bundled geometric model;
- rejection fixtures for altered models, source excerpts, and rank output.

The written proofs supply the descent, cocycle, and chain-map arguments.
The small algebra tests support those arguments; they are not a sampled
verification of the nonlinear residual on every overlap. The geometric
dependency's own `verify.py` separately checks contractions, pole bounds,
chart transport, and degree/factor-48 claims. This package checks the exact
files it consumes, but does not rerun that entire dependency suite.

## Boundary of the conclusion

The existing scalar comparison applies to the closed source constructed
here, together with the geometric dependency's frame and regularity proofs.
Its single `J2` minus and transpose remain those of PR #34 and the geometric
package. A zero image under this scalar is still only a zero image under a
noninjective map. No conclusion about the full Ext² class follows from it.

`pins.json` records immutable public source locations and exact dependency
hashes. `manifest.json` covers all files of this package except itself.
`certificates/verification.json` records a fresh isolated run; it is evidence
of the listed checks, not a substitute for their execution or the proofs.
