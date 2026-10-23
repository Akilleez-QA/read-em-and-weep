# Frame transitions and defect cocycles — Lean checked

This unit formalizes three universal linear-algebra statements from section 2 of [null's PR816](https://github.com/Akilleez-QA/read-em-and-weep/blob/eed6010347fcebc21aef30413b0e1da3be68a9b4/research/hm/nonclosed-frame-transfer/NONCLOSED-FRAME-TRANSFER-EXACT-DEFECT.md):

- `frameTransition_comp`: the middle-frame homotopy, closed inclusion, and closed projection imply transition composition.
- `frameTransition_inversePair`: a homotopy and retraction in each frame imply both inverse identities.
- `frameTransfer_defectCocycle`: arbitrary transfers between six independent source/target frame modules satisfy the typed defect law
  `D_ca = D_cb ∘ gC_ba + gD_cb ∘ D_ba`, provided the two transition families satisfy their cocycle equations.

The scalars form an arbitrary ring, and the modules have additive commutative group structures. The inverse theorem supplies both retraction and homotopy hypotheses explicitly. No dimension, basis, characteristic restriction, homotopy normalization, or commutation of compositions is used. Source and target types remain distinct.

These are conditional algebraic identities. The unit does not construct actual contractions or physical HM frames, prove actual gluing or sheaf descent, or assert that the defect vanishes. It does not formalize the section 1 nonclosed-transfer formula; that is a separate unit. No actual coefficient, source row, global primitive, rank, model solve, or algebraicity theorem is supplied.

Verified with Lean **4.34.1** and mathlib **`d13f23b723b8a846827a245b89c10fc7d3f11612`**. The unchanged original source compiled with exit code 0 and empty stdout/stderr. A separate importing `Check.lean` resolved all three theorem names; each reports exactly `propext`, `Classical.choice`, and `Quot.sound`. Both runs recorded unchanged inputs and complete cleanup. See `AXIOMS.txt`, `VERIFICATION.json`, and `REVIEW.md`. Comparator and an independent second kernel were not run.

The sole import is `Mathlib.Algebra.Module.LinearMap.Defs`. Module mode and public exports load exported dependency information while preserving kernel checking and transitive axiom reports. Verification used one compiler thread, Lean's `-M1200` internal limit, and the existing 60-second CPU, 75-second wall, 1.5 GiB sampled-RSS guard. Sampled RSS is not a hard address-space guarantee. No limit was increased.

For replay in the repository after preparing its pinned dependencies, from `lean/`:

```sh
lake build +OAI.AlgebraicGeometry.HorrocksMumford.FrameTransferCocycle
lake env lean --root=../research/hm/lean-frame-transfer-cocycle ../research/hm/lean-frame-transfer-cocycle/Check.lean
```

These repository commands are distinct from the archived successful isolated-workspace run, which used the `lean/` source root, `build/` output root, and a dependency search path containing that output root and the pinned library artifacts. The entire upstream library was not built.

The authenticated source is commit `eed6010347fcebc21aef30413b0e1da3be68a9b4`, path `research/hm/nonclosed-frame-transfer/NONCLOSED-FRAME-TRANSFER-EXACT-DEFECT.md`, SHA256 `5f2069fe845df87caa3a4bdb1c2bd7434ff6513bddda5bc21f54f042a04a4e84`. The original UNCOMPILED SCOPE and static review remain historical records; this README gives the completed verification status. This supporting unit is not registered as a formalized main result in `formalization.yaml`.
