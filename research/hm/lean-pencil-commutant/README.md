# PencilCommutant Lean unit

Status: **CHECKED** for the exact generic unit bound in [REVIEW.md](REVIEW.md). The root module compilation and import/axiom check succeeded. This publication is an independent mathematics/evidence review of that root run, with no second kernel run or Comparator.

The unit defines a linear fixed-pencil defect on three unrestricted endomorphism spaces, its kernel submodule, both tensor and all-pure-tensor membership criteria, identity membership, and componentwise composition closure.

This uses unrestricted `End`/`Hom`. Actual PR808 `End_G`/`Hom_G` requires restriction to equivariant triples and the corresponding equivariant targets; that restriction is not constructed. No actual HM data, dimension or rank result, classification, source2 exclusion, or full repair is claimed.

Replay from the repository's `lean/` directory with pinned Lean 4.34.1 and mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`, after checking out this PR and preparing its pinned dependencies:

```sh
lake build +OAI.AlgebraicGeometry.HorrocksMumford.PencilCommutant
lake env lean --root=../research/hm/lean-pencil-commutant ../research/hm/lean-pencil-commutant/Check.lean
```

These are replay instructions, not commands executed by this reviewer. Root validation used a normal isolated pinned environment and targeted dependencies, without an entire upstream build. The producer's unchanged `SCOPE.md` records its earlier uncompiled handoff; the receipts and this review establish the subsequent checked status.
