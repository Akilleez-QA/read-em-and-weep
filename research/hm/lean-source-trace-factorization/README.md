# Source trace factorization — Lean checked

For arbitrary ring modules and linear maps `d : C0 → C1`, `ell : C0 → T`, this unit proves that `ker d ≤ ker ell` is equivalent to a unique linear response on `range d` whose value at `d X` is `ell X`. It constructs that response and proves independence under changes of primitive with the same differential. A preceding-map corollary derives the kernel inclusion from explicit `range delta = ker d` and `ell.comp delta = 0` hypotheses.

The two corrected-response corollaries allow a separate scalar action on a common ambient coefficient module. They are ambient-coefficient specializations: they do not construct the actual multiplication between degree/twist-graded targets. Changes to lower data, physical frames or normalization are not covered.

This is the standard algebraic interface behind [PR815 equations20–21](https://github.com/Akilleez-QA/read-em-and-weep/blob/0eaeca734b9e17142da2f1bdfd9a1721d0bb1d42/research/hm/affine-square-source-response/PROOF.md). The published source was independently authenticated. Physical monad exactness, the cohomology comparison, contraction, trace response and its kernel vanishing remain separate obligations. Uniqueness is only on the differential's range; there is no canonical extension to the full target. No actual HM instance, rho16, beta4, fifth boundary or algebraicity theorem is evaluated or established.


Verified with Lean4.34.1 (commit5045d0056413266e57c625dcd7c365b10e377c52) and mathlibd13f23b723b8a846827a245b89c10fc7d3f11612. The isolated verification workspace used exactly the repository's eight mathlib dependency pins. Both the source and importing `Check.lean` completed with exit0, unchanged inputs and full process cleanup. All 7 exported theorem axiom closures are contained in `propext`, `Classical.choice`, `Quot.sound`; see `AXIOMS.txt` and the portable command/output evidence in `VERIFICATION.json`. Comparator and an independent second kernel were not run.

The source uses Lean's module system, public imports and a public exposed section. This imports exported dependency information while retaining kernel checking of these proofs and transitive axiom reports. Earlier import-memory failures are preserved in the local run history; no memory-cap escalation was used. Final source compilation used one thread, Lean's1200MiB internal ceiling, and the external60CPU-second/75wall-second/1.5GiB sampled-RSS guard. Sampled RSS is not a hard address-space limit.

For replay in the repository after preparing its pinned dependencies, from `lean/`:

```sh
lake build +OAI.AlgebraicGeometry.HorrocksMumford.SourceTraceFactorization
lake env lean --root=../research/hm/lean-source-trace-factorization ../research/hm/lean-source-trace-factorization/Check.lean
```

The archived successful run used a targeted isolated mathlib workspace, the module root `lean/`, output root `build/`, and `LEAN_PATH` containing that output root plus the pinned dependency libraries. Its exact normalized command and source hashes are recorded in `VERIFICATION.json`. It did not build the entire upstream library.

This supporting result is deliberately not registered as a formalized main theorem in `formalization.yaml`.
