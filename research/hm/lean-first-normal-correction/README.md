# First normal correction — Lean checked

This unit proves four universal matrix identities supporting [PR815 equations (10) and (15)](https://github.com/Akilleez-QA/read-em-and-weep/blob/0eaeca734b9e17142da2f1bdfd9a1721d0bb1d42/research/hm/affine-square-source-response/PROOF.md):

- `referenceFrame_mul_inv`: the lower triangular frame times its displayed inverse is the identity.
- `referenceFrame_inv_mul`: the reverse product is also the identity.
- `conjugated_commutator`: conjugating the full first-normal commutator gives all four displayed matrix entries, including the upper entry and both lower terms proportional to `y`.
- `trace_mul_commutator`: `trace (L * (Z * L - L * Z)) = 0` for arbitrary 2×2 matrices over a commutative ring.

The first three results use actual `Matrix (Fin 2) (Fin 2) K` values over any field `K`. The frame is `[[alpha, 0], [c, delta]]`, with inverse `[[1/alpha, 0], [-c/(alpha*delta), 1/delta]]`; exactly `alpha ≠ 0` and `delta ≠ 0` are assumed. These are frame units. The geometric source `a` is not inverted, and no characteristic restriction is needed. The fourth result needs neither a trace-zero matrix nor an invertible frame. It states the underlying cancellation in equation (15); the scalar `q` factors out by trace linearity and is not a separately declared corollary.

This formalizes the matrix algebra only. Applying it to the physical HM transition still requires the actual frame, generator, and coefficient identifications. It does not prove affine gluing, harmonic coefficient extraction, source solvability, or sheaf/cohomology claims, and it does not evaluate an actual HM coefficient, source, rank, rho16, or beta4. Trace cancellation does not justify removing the normal commutator from matrix transport. No algebraicity theorem is claimed.

Verification used Lean **4.34.1** and mathlib **`d13f23b723b8a846827a245b89c10fc7d3f11612`**. The exact source compiled successfully, and a separate importing `Check.lean` resolved all four theorem names and printed their transitive axioms. Each uses exactly `propext`, `Classical.choice`, and `Quot.sound`. Source compilation emitted two `linter.unnecessarySeqFocus` style warnings at lines 44 and 52 and no errors; the warnings were retained. See `AXIOMS.txt`, `VERIFICATION.json`, and `REVIEW.md`. Comparator and an independent second kernel were not run.

The module uses public imports and an exposed public section. This retains kernel checking and public definitions while loading the exported dependency information. The successful proof run used one thread, Lean's `-M1200` internal limit, and the existing 60-second CPU, 75-second wall, 1.5 GiB sampled-RSS guard. Sampled RSS is not a hard address-space limit. No resource cap was increased for this unit.

For replay in the repository after preparing its pinned dependencies, from `lean/`:

```sh
lake build +OAI.AlgebraicGeometry.HorrocksMumford.FirstNormalCorrection
lake env lean --root=../research/hm/lean-first-normal-correction ../research/hm/lean-first-normal-correction/Check.lean
```

These are repository replay commands. The archived successful run used a targeted isolated mathlib workspace with a `lean/` source root, a `build/` output root, and `LEAN_PATH` containing that output root and the pinned dependency libraries. It did not build the entire upstream library.

The manuscript reference is commit **`0eaeca734b9e17142da2f1bdfd9a1721d0bb1d42`**, path `research/hm/affine-square-source-response/PROOF.md`, SHA256 `78a0f462ffd0710d248658aaf95926f926297b0bae43aade85eb4c7fc934d236`. An initial draft accidentally prefixed the commit with the PR number `815`; the original draft remains historical evidence, and this README supplies the corrected reference and completed verification status.

This supporting unit is not registered as a formalized main result in `formalization.yaml`.
