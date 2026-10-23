# Heterogeneous affine source response — Lean checked

This unit proves a conditional overlap criterion with distinct trace and norm
coefficient modules. For supplied linear maps

```text
μi : Ti → Ni       μj : Tj → Nj
g  : Tj → Ti       h  : Nj → Ni
Li : P → Ti        Lj : P → Tj
```

assume `μi ∘ g = h ∘ μj` and `h Qj − Qi = μi f`. Define

```text
ρi = Qi + μi(yi − Li s)
ρj = Qj + μj(yj − Lj s).
```

The exact target-minus-transport defect is

```text
ρi − h ρj = μi(yi − Li s − g(yj − Lj s) − f).
```

Therefore norm overlap equality is equivalent to this trace defect belonging
to `ker μi`. With the additional explicit assumption `Function.Injective μi`,
it is equivalent to

```text
Li s − g(Lj s) = yi − g yj − f.
```

All five module types `P`, `Ti`, `Tj`, `Ni`, `Nj` are independent, including
their universes, over a supplied ring. No multiplication map is assumed
invertible, and the kernel criterion needs no injectivity assumption.

## Correspondence with PR815

The motivating source is
[PR815, equations (13), (14), and (20)–(24)](https://github.com/Akilleez-QA/read-em-and-weep/blob/0eaeca734b9e17142da2f1bdfd9a1721d0bb1d42/research/hm/affine-square-source-response/PROOF.md).
Its exact published snapshot was independently authenticated. On a fixed
overlap, after restriction and with the physical normalizations supplied:

- `Ti`, `Tj` represent degree-twelve, physical-twist-six trace coefficients;
  `Ni`, `Nj` represent degree-sixteen, physical-twist-fourteen norm
  coefficients. These actual graded spaces are not constructed here.
- `μi`, `μj` represent multiplication by `A = a³h`, of degree four and
  physical twist eight.
- Formal `h : Nj → Ni` is the scalar transport `λ^sc_ij` from chart `j` to
  chart `i`. It is unrelated to the source polynomial named `h` in `a³h`.
  Formal `g` is the corresponding trace-coefficient transport.
- Formal `yi`, `yj` are **already traced** lower terms `τ_i(y_i)`,
  `τ_j(y_j)` from equation (24). Formal `f` is `τ_i(F_ij)`. Thus equation
  (14) has exactly the direction and sign `h Qj − Qi = μi f`.
- `Li`, `Lj` represent the supplied trace rows `Λ_i`, `Λ_j`. The intended
  source is the full corrected expression `s = a(V_h − b Z_a) − q W_h`.
  `P` is supplied independently; identifying it with the actual differential's
  range and proving membership of this source remain separate obligations.

This gives a typed criterion for the remaining source-row overlap test. It
does not construct physical multiplication, transports, affine shifts,
contractions, source rows, or regular-section injectivity. It does not prove
monad exactness, a cohomology comparison, source existence, global gluing, or
an original proof repair. The defined norm expression has its difference
from `Q` in the image of `μ`; this does not establish equation (16)'s image
condition for an independently supplied actual norm coefficient. No division
by a source or cancellation on fibers at its zeros is used.

## Verification and replay

Verified with Lean **4.34.1**, commit
`5045d0056413266e57c625dcd7c365b10e377c52`, and mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`. Source compilation and the separate
importing `Check.lean` both completed with exit code 0, unchanged recorded
inputs, and full process cleanup. All three exported theorem axiom closures
contain only `propext`, `Classical.choice`, and `Quot.sound`. The independent
review records the exact files and completed evidence. Comparator and an
independent second kernel were not run.

The direct imports are `Mathlib.Algebra.Module.Submodule.Ker` and
`Mathlib.Tactic.Abel`. The module uses public imports and an exposed public
section. The successful runs used one compiler thread, Lean's 1200 MiB
internal memory ceiling, and an external guard with a 60-second per-process
CPU limit, 75-second wall limit, and 1.5 GiB sampled aggregate RSS threshold.
Sampled RSS is not a hard address-space guarantee. No cap was raised for these
passes, and this review did not rerun compilation.

For replay in the repository after preparing its pinned dependencies, from
`lean/`:

```sh
lake build +OAI.AlgebraicGeometry.HorrocksMumford.HeterogeneousAffineSourceResponse
lake env lean --root=../research/hm/lean-heterogeneous-affine-source-response ../research/hm/lean-heterogeneous-affine-source-response/Check.lean
```

The archived successful runs used an isolated workspace with the pinned
mathlib, source root `lean/`, output root `build/`, and `LEAN_PATH` containing
that output root and the pinned dependency libraries. The displayed repository
replay commands were not separately executed in this review.

This supporting result is not registered as a formalized main theorem in
`formalization.yaml`.
