# Source-family multiplier — Lean checked

This unit proves the polynomial-family cancellation step in
[PR889, Section 5, S10](https://github.com/Akilleez-QA/read-em-and-weep/blob/72ac7ecc5447415fa8452f12ed6ec16921a600f4/research/hm/physical-normalization-symmetry/PROOF.md).
Over a field k, `BinaryForm k n` is the actual submodule of homogeneous
degree-n polynomials in two variables. For a linear map L from quartics to
degree-twelve forms, it constructs the polynomial-valued quadratic map

```text
sourceFamilyObservation(L)(h) = h * L(h).
```

The quartic multiplier varies with h. Equality of these entire quadratic
maps forces equality of L: nonzero h cancels in the polynomial integral
domain, and linearity handles h=0. Multiplying the observation by `-(c^3)`
preserves injectivity when the supplied scalar c is nonzero. No physical
source or base point is selected.

There are **four checked declarations: one evaluation formula and three
results**:

- `sourceFamilyObservation_apply`: the defining product formula.
- `sourceFamilyObservation_mem_homogeneous16`: every output belongs to the
  homogeneous degree-sixteen submodule, including a possible zero output.
- `sourceFamilyObservation_injective`: whole-family cancellation with the
  varying quartic multiplier retained.
- `weighted_sourceFamilyObservation_injective`: cancellation after the
  explicitly nonzero cubic scalar weight.

The codomain remains the binary polynomial ring, with degree sixteen proved
separately. The unit does not identify quadratic maps with a symmetric-square
Hom space or construct a polarized coefficient left inverse. Its only direct
imports are the pinned mathlib homogeneous-polynomial and quadratic-map APIs;
no earlier OAI supporting unit is a source dependency. The publication is
based on `main`.

## Verification and replay

The final source compilation and separate importing axiom check passed under
Lean 4.34.1 and mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`.
All four axiom reports contain exactly `propext`, `Classical.choice`, and
`Quot.sound`. The final source compile emitted no warnings or other output.
See `REVIEW.md`, `AXIOMS.txt`, and `VERIFICATION.json` for hashes and evidence.

The original CLI delivery is preserved. Export names were made descriptive;
the first compile then required `noncomputable` on the observation definition
because its polynomial algebra instance is noncomputable. That failed attempt
is retained. Adding this marker changed no formula, hypothesis or proof.

The successful runs used one compiler thread, Lean's `-M1200`, a 60-second
per-process CPU limit, a 75-second wall watchdog, and a sampled 1.5 GiB
process-group RSS threshold. Sampled peaks were 1,157,267,456 bytes for source
compilation and 1,151,565,824 bytes for the importing check. Recorded inputs
were unchanged and cleanup completed. Sampled RSS is not a hard address-space
limit or a guarantee against between-sample overshoot. The independent reviewer
inspected these runs without recompiling; Comparator and a second independent
kernel were not run.

With this source installed in a checkout containing the repository's pinned
Lean configuration and prepared dependencies, replay from the repository root:

```sh
cd lean
lake build +OAI.AlgebraicGeometry.HorrocksMumford.SourceFamilyMultiplier
lake env lean -j1 -M1200 --root=../research/hm/lean-source-family-multiplier ../research/hm/lean-source-family-multiplier/Check.lean
```

These are repository replay instructions, not commands separately executed
in the recorded verification. The archived runs used an isolated source/build
layout with the pinned compiler and dependency search path; their bounded
commands and results are recorded in `VERIFICATION.json`.

## Application boundary

The result concerns equality of entire binary-polynomial-valued h-families,
not one h value or a numerical evaluation of the binary variables. The scalar
c represents a supplied a(x) at the current parameter/base fiber; it must be
nonzero and is not asserted constant across parameter generators.

Actual coherent G-equivariance, the positive representation identification,
cubic-a/linear-h family structure, prior globality, physical extraction,
full corrected-source `S-qW` image membership, and independent reference values
remain application certificates. No group action, dimensions 10/12/13,
axis/square separation, orbit geometry, selected calibration, actual HM
exclusion or repaired main theorem is established. This supporting unit is
not a formalized main-theorem entry in `formalization.yaml`.
