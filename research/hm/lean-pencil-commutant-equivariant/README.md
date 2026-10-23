# Equivariant pencil commutant — Lean checked

This unit restricts the generic pencil defect from
[PR879](https://github.com/Akilleez-QA/read-em-and-weep/blob/634ca192ab8f64cf3d779a9194382e1458cdad7a/lean/OAI/AlgebraicGeometry/HorrocksMumford/PencilCommutant.lean)
to genuine equivariant domain and target submodules. It formalizes the
conditional restriction step behind
[PR808, section 2, equation (4)](https://github.com/Akilleez-QA/read-em-and-weep/blob/3c2d80d5bbae109f810b1919fb0adbc2a1d0e392/research/hm/source2-commutant-gate/PROOF.md).

The inputs are independent modules over a commutative ring, a monoid, four
bundled monoid actions on `W`, `M2`, `M3`, `M4`, and supplied maps
`alpha : W ⊗ M2 → M3` and `beta : W ⊗ M3 → M4`. Both tensor maps must be
equivariant. The unit constructs the diagonal tensor actions and the linear
Hom submodules. No actual HM representation or tensor is inferred from these
abstract inputs.

The domain `D` contains all three equivariant endomorphism channels. The
target `T` contains both equivariant tensor Hom channels. The restricted map
is a genuine linear map `Delta_G : D →ₗ[R] T`, whose underlying value is

```text
(X3 alpha − alpha(id_W ⊗ X2),
 X4 beta  − beta (id_W ⊗ X3)).
```

The action on W remains in both diagonal tensor actions. The identity on W
in the defect does not require its action to be trivial. Equivariance of
both `alpha` and `beta` is retained as a hypothesis of the restriction.

The kernel in the domain subtype is the comap of the generic commutant along
`D.subtype`. Its image in the ambient triple space is exactly the intersection
of that commutant with D. For an ambient triple, the final theorem spells this
out as both pencil equations for every W and vertex input, together with all
three equivariance equations for every monoid element and vertex input.
Zero and singular triples are allowed; no inverse, unit, or scalar-on-isotypic
assumption is imposed.

There are **12 new explicit theorems**, including the essential action and
membership helper equations. `Check.lean` checks all 12 plus the four existing
PR879 dependency theorems, for 16 axiom reports. Those four are not new results.
The only direct public import is `PencilCommutant`.

## Verification and replay

The final source compile and separate importing check passed under Lean
4.34.1 and mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`.
Five new theorem closures use only `propext` and `Quot.sound`; seven also use
`Classical.choice`. The four dependency closures use `propext` and
`Quot.sound`. No unfinished proof or custom axiom appears. The source compile
retains two nonblocking unused-bound-variable warnings, for `X` and `F` in
submodule closure definitions. See `REVIEW.md`, `AXIOMS.txt`, and
`VERIFICATION.json` for exact evidence.

The final source differs from the producer draft by one
`include hAlpha hBeta in` line before the maps-into theorem's documentation
comment. This makes Lean retain both intended section hypotheses. Earlier
failed attempts are preserved: omitted hypothesis parameters, a misplaced
`include` after the documentation comment, and an import configuration
rejected before launch because no compiled module yet existed.

The successful runs used one compiler thread, Lean's `-M1200`, a 60-second
per-process CPU limit, a 75-second wall watchdog, and a sampled 1.5 GiB
process-group RSS threshold. Source and import-check sampled peaks were
895,647,744 and 840,941,568 bytes. Recorded inputs were unchanged and cleanup
completed. Sampled RSS is not a hard address-space limit or a guarantee
against between-sample overshoot. The reviewer inspected the root's evidence
without rerunning compilation. Comparator and an independent second kernel
were not run.

With PR879's source present and the pinned dependencies prepared, replay
from `lean/`:

```sh
lake build +OAI.AlgebraicGeometry.HorrocksMumford.PencilCommutantEquivariant
lake env lean --root=../research/hm/lean-pencil-commutant-equivariant ../research/hm/lean-pencil-commutant-equivariant/Check.lean
```

The archived runs used the isolated source/build layout with exact reviewed
dependency artifacts. These repository replay commands were not separately
executed. The unit constructs no actual action/tensor identification, Schur
decomposition, dimensions 113/153, numerical rank, trace-radical classification,
family membership, source2 exclusion, or repaired main theorem. It is not
registered as a formalized main theorem in `formalization.yaml`.
