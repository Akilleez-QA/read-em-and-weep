# Quadratic projector compatibility — Lean checked

For a supplied linear map `q : V →ₗ[K] W` and idempotent endomorphisms
`p : V →ₗ[K] V`, `r : W →ₗ[K] W`, this unit proves the exact criterion

```text
r ∘ q = q ∘ p
  ↔ r ∘ q ∘ (id − p) = 0 and (id − r) ∘ q ∘ p = 0.
```

It also proves that intertwining is equivalent to preserving both the image
and kernel summands, and gives the cross-term criterion for every member of a
supplied family of linear maps. The coefficient assumptions are a semiring
acting on additive commutative groups; no field, dimension, basis, or
characteristic restriction is needed. Both idempotence hypotheses are explicit.

This is the standard algebraic criterion used in the final projector paragraph
of [PR818, Section 5](https://github.com/Akilleez-QA/read-em-and-weep/blob/f4a73af666900ad2cb34a756d24b88e19dd6feaa/research/hm/negative-truncation-extension/PROOF.md).
The published source was independently authenticated. “Quadratic” refers to
the intended multiplication action; the input `q` here is a linear map.

For the intended bundled action
`q₊ : Sym²(T₊) ⊗ N₂ → N₄`, the domain projector must be `id ⊗ p₂` and the
target projector `p₄`. That tensor projector and its idempotence must first be
constructed. Alternatively, the family theorem applies to the maps
`q_s(x) = q₊(s ⊗ x)` on `N₂`, with projectors `p₂` and `p₄`, once those maps
have been supplied. This unit constructs neither the actual multiplication
action nor these tensor/family inputs, and it does not verify their cross
terms. It proves no five-variable window lift, full-module lift, splitting,
submodule-extension theorem, source2 exclusion, or actual HM value or rank.

Verified with Lean **4.34.1**, commit
`5045d0056413266e57c625dcd7c365b10e377c52`, and mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`. The final source and the importing
`Check.lean` completed with exit code 0, unchanged recorded inputs, and full
process cleanup. All three theorem axiom closures contain only `propext`,
`Classical.choice`, and `Quot.sound`. The independent review binds the exact
source, check file, compiled module, and completed verification receipts.
Comparator and an independent second kernel were not run.

The direct import is `Mathlib.Algebra.Module.Submodule.Range`. The source uses
Lean's module system with a public import and an exposed public section. Final
verification used one compiler thread, Lean's 1200 MiB internal memory ceiling,
and the external guard's 60 CPU-second per-process limit, 75-second wall limit,
and 1.5 GiB sampled aggregate RSS threshold. Sampled RSS is not a hard
address-space guarantee. No resource limit was raised to obtain these passes.

For replay in the repository after preparing its pinned dependencies, from
`lean/`:

```sh
lake build +OAI.AlgebraicGeometry.HorrocksMumford.QuadraticProjectorCompatibility
lake env lean --root=../research/hm/lean-quadratic-projector-compatibility ../research/hm/lean-quadratic-projector-compatibility/Check.lean
```

The archived successful runs used an isolated workspace with the same pinned
mathlib, source root `lean/`, output root `build/`, and `LEAN_PATH` containing
that output root and the pinned dependency libraries. The displayed repository
replay commands were not separately executed in this review. The original
draft and earlier successful draft checks remain preserved; only stale status
comments changed before the final checks.

This supporting result is not registered as a formalized main theorem in
`formalization.yaml`.
