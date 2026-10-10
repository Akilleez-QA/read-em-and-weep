# The current scalar map: comparison, residues, and detection limits

This package isolates the scalar map

\[
L(X_{02},X_{13})=X_{02}[0,0]-X_{13}[10,0]
\]

for the four-term Horrocks–Mumford model of ranks `(5,15,10,2)`.
Matrix indices are zero-based throughout. Coordinate names `x_1,...,x_4`
are one-based. After projection to the full-sign sector, the scalar target is

\[
H^4((\mathbf P^1)^4,\mathcal O(-4,-4,-4,-4)),
\]

of dimension 81.

The completed exact-rational computation of the specified geometric class
has zero image under this map: 46 coordinates are computed by exact rational
extraction and 35 are supplied by integer differential identities. That
numerical computation is a separate certificate; the tests here do not
reevaluate its geometric numerator. **The full obstruction remains
undetermined.** The current map has rank 34 on the 352-dimensional full-sign
finite-model cohomology, so its zero image is not a boundary certificate.

## Contents

- [Map and scalar comparison](map-and-comparison.md): the global chain map,
  signs, carrier merger, and precise source hypotheses.
- [Residue theorem](residue-theorem.md): the all-mask projection and its
  ordered prism, local-duality interpretation, and nonreduced support.
- [Integral boundary functional](integral-boundary-functional.md): an
  explicit characteristic-independent formula using six integer kernels.
- [Structural relations and detection boundary](structural-relations.md):
  all 47 integer relations and an exact test of what scalar maps cannot see.
- `data/`: the small algebraic model and compact integer relation witnesses.
- `finite-model/`: a pinned exact finite-model implementation, bundled so
  the checks have no dependency on unpublished files.

## Reproduce the focused checks

Python 3.10 or newer and Node.js 18 or newer suffice; no third-party package,
network connection, environment variable, or external data path is needed.
From this directory run:

```sh
python3 checks/verify_scalar_maps.py
python3 checks/verify_projection.py
python3 checks/verify_integer_kernels.py
node checks/verify_finite_model.js
```

The first three checks use exact integer/rational arithmetic. The last
reconstructs the outgoing finite differential, verifies all relation
witnesses over the integers, computes rational ranks, and verifies an
explicit nonzero cohomology class invisible to every constant scalar map.
It additionally checks current-map ranks in characteristic 13 and combined
ranks in characteristic 29. No modular result substitutes for a rational
rank or rational coefficient calculation.

These are proof-supporting checks, not a replacement for the general
arguments. In particular, the small projection regression does not prove
geometric pole bounds, and the relation test does not identify an arbitrary
input polynomial with the geometric class.

## Model provenance and mathematical dependencies

The bundled finite model has basis identifier `hm-pr5-full-sign-harmonic-v1`
and source commit `add03476d9055aa00e1e00778eea6332cf8e01cc`. Its mathematical
context is the [finite-model description](https://github.com/Akilleez-QA/read-em-and-weep/blob/add03476d9055aa00e1e00778eea6332cf8e01cc/research/hm/ext-model.md).
The unchanged bundled oracle has SHA256
`29bbe778ed43ce91b52390d27fd78678879bb39c877982afb8063676b3fe1558`.
The compact polynomial model has canonical JSON SHA256
`b6b532c4bab5787397a4cddde34210c12fae71853b30cb73ecbe8a9c2b4826b2`.

The comparison and residue arguments below are self-contained under their
explicit source hypotheses. Verifying those hypotheses for the actual
geometric numerator requires the separate exact-source construction and
pole certificates. No assertion here derives them from sampled points,
a modular coefficient array, or a rank computation.

General background, rather than certificates of this particular source:
[Čech refinements](https://stacks.math.columbia.edu/tag/09UY),
[Nayak–Sastry, traces and residues](https://arxiv.org/abs/1903.01783), and
[Cattani–Dickenstein–Sturmfels, multidimensional residues](https://arxiv.org/abs/alg-geom/9404011).
