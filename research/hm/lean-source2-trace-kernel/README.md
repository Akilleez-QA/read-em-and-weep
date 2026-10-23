# Source2 trace coordinates — Lean checked

This unit fixes the uncoupled trace columns `(9,18,16)`, `(15,18,12)`, `(17,18,9)` and the coupled columns `(9,18,16)`, `(32,36,21)`. It proves all five integer-scaled reconstruction identities over any field. In characteristic zero it proves both maps injective, and hence `ker (traceMap.comp diag) = ker diag` for every compatible linear map `diag`. A general injective-postcomposition kernel lemma is included.

Triples are `K × (K × K)`, ordered by vertices2,3,4. The input coordinates are `a0,a8,aC` or `a0,aR`. Cancellation of180 or-252 is confined to the characteristic-zero injectivity proofs; the reconstruction identities themselves do not require characteristic zero.

The exact columns and scope come from independently authenticated [PR808 section4](https://github.com/Akilleez-QA/read-em-and-weep/blob/3c2d80d5bbae109f810b1919fb0adbc2a1d0e392/research/hm/source2-commutant-gate/PROOF.md). These are universal coordinate identities. No actual HM tensor is evaluated. The normal-form identification with the actual endomorphism algebra, radical identification, ranks and geometric application are not supplied. In particular, no arbitrary-pencil trace kernel is called its Jacobson radical, and no source2 exclusion or original theorem repair follows from this unit alone.


Verified with Lean4.34.1 (commit5045d0056413266e57c625dcd7c365b10e377c52) and mathlibd13f23b723b8a846827a245b89c10fc7d3f11612. The isolated verification workspace used exactly the repository's eight mathlib dependency pins. Both the source and importing `Check.lean` completed with exit0, unchanged inputs and full process cleanup. All 10 exported theorem axiom closures are contained in `propext`, `Classical.choice`, `Quot.sound`; see `AXIOMS.txt` and the portable command/output evidence in `VERIFICATION.json`. Comparator and an independent second kernel were not run.

The source uses Lean's module system, public imports and a public exposed section. This imports exported dependency information while retaining kernel checking of these proofs and transitive axiom reports. Earlier import-memory failures are preserved in the local run history; no memory-cap escalation was used. Final source compilation used one thread, Lean's1200MiB internal ceiling, and the external60CPU-second/75wall-second/1.5GiB sampled-RSS guard. Sampled RSS is not a hard address-space limit.

For replay in the repository after preparing its pinned dependencies, from `lean/`:

```sh
lake build +OAI.AlgebraicGeometry.HorrocksMumford.Source2TraceKernel
lake env lean --root=../research/hm/lean-source2-trace-kernel ../research/hm/lean-source2-trace-kernel/Check.lean
```

The archived successful run used a targeted isolated mathlib workspace, the module root `lean/`, output root `build/`, and `LEAN_PATH` containing that output root plus the pinned dependency libraries. Its exact normalized command and source hashes are recorded in `VERIFICATION.json`. It did not build the entire upstream library.

This supporting result is deliberately not registered as a formalized main theorem in `formalization.yaml`.
