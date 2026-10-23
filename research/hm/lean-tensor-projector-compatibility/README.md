# Tensor projector compatibility — Lean checked

This supporting unit constructs the genuine tensor endomorphism
`P = TensorProduct.map LinearMap.id p` on `W ⊗[R] V` over a commutative ring.
It connects the supplied bundled map `q : W ⊗[R] V →ₗ[R] N` to the existing
quadratic projector criterion. The modules `W`, `V`, and `N` are independent;
no field, basis, finite dimension, or nonzero-module assumption is required.

The three exported theorems prove:

- `tensorProjector_idempotent`: `p.comp p = p` implies `P.comp P = P`.
- `tensorProjectorCompatibility_iff_slices`: `r.comp q = q.comp P` is
  equivalent to `r.comp q_w = q_w.comp p` for every `w : W`, where the genuine
  linear slice is `q_w(v) = q(w ⊗ v)`. The reverse implication uses pure-tensor
  spanning; it does not assume every tensor is pure.
- `tensorProjectorCompatibility_iff_crossTerms`: under explicit idempotence
  of `p` and `r`, bundled intertwining is equivalent to both equations
  `(r.comp q).comp (LinearMap.id - P) = 0` and
  `((LinearMap.id - r).comp q).comp P = 0`.

The last theorem imports and applies
[PR865's quadratic criterion](https://github.com/Akilleez-QA/read-em-and-weep/blob/80f241711bcd3a053268de6a83c8aee68403ebbf/lean/OAI/AlgebraicGeometry/HorrocksMumford/QuadraticProjectorCompatibility.lean).
The written motivation is
[PR818, section 5](https://github.com/Akilleez-QA/read-em-and-weep/blob/f4a73af666900ad2cb34a756d24b88e19dd6feaa/research/hm/negative-truncation-extension/PROOF.md).
The tensor adapter proves the domain projector's idempotence instead of
assuming it. The slice equivalence itself needs no idempotence hypotheses.

The actual quadratic action `q` remains supplied. This unit constructs no
symmetric square, actual HM module, physical multiplication, or vanishing
cross term. Applying it to a proposed extension still requires those inputs
and their compatibility proofs. It establishes no actual extension, lift,
splitting, source2 exclusion, rank, or repair of the original theorem.

## Verification and replay

The final source compile and separate importing `Check.lean` both succeeded
under Lean 4.34.1 and mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`. The first two theorem axiom closures
are `[propext, Quot.sound]`; the cross-term theorem's closure is
`[propext, Classical.choice, Quot.sound]`. There are no unfinished proofs or
custom axioms. The successful compile emitted no warnings. See `REVIEW.md`,
`AXIOMS.txt`, and `VERIFICATION.json` for exact evidence.

Two earlier attempts are preserved: one failed to locate the already-built
dependency under the selected namespace root; the next found a rewrite
presentation mismatch between `(p.comp p) v` and `p (p v)`. Copying the exact
reviewed dependency artifacts resolved lookup. An explicitly typed local
equality resolved the rewrite without changing any theorem statement.

The runs used one compiler thread, Lean's `-M1200`, a 60-second per-process
CPU limit, a 75-second wall watchdog, and a sampled 1.5 GiB process-group RSS
threshold. Source and import-check sampled peaks were 853,295,104 and
838,729,728 bytes. Recorded input hashes were unchanged and cleanup completed.
Sampled RSS is not a hard address-space bound or a guarantee against
between-sample overshoot. The independent reviewer inspected these root-run
receipts without rerunning the compiler. Comparator and an independent
second kernel were not run.

This unit depends on PR865's source being present. After preparing the pinned
repository dependencies, replay from `lean/`:

```sh
lake build +OAI.AlgebraicGeometry.HorrocksMumford.TensorProjectorCompatibility
lake env lean --root=../research/hm/lean-tensor-projector-compatibility ../research/hm/lean-tensor-projector-compatibility/Check.lean
```

The archived runs used the isolated source/build layout with the exact
reviewed dependency artifacts. These repository replay commands were not
separately executed. This supporting result is not registered as a formalized
main theorem in `formalization.yaml`.
