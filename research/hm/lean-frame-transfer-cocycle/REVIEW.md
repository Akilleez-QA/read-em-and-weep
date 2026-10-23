# Independent review: frame transition and defect cocycles

**PASS for the three stated algebraic theorems.** The reviewer independently checked the source mathematics and pinned APIs, authenticated the written source, and inspected the completed root-run compiler and importing axiom evidence. No compilation was rerun and no producer proof file was edited by this reviewer.

## Exact artifact bindings

All digests are SHA256. Portable names omit private host paths and process identifiers.

| Artifact | Digest |
| --- | --- |
| `lean/OAI/AlgebraicGeometry/HorrocksMumford/FrameTransferCocycle.lean` | `18c6271fd13b70806e15ce0a71bb80ebbfbc778c0ea38178a98236a1ecc97e35` |
| `Check.lean` | `96c56c821fc62f237d4ae99d040a605feaedc85cf5b1c2b251ecd524f160f614` |
| Imported `FrameTransferCocycle.olean` | `10011192a932019fb05d5cfd15694a62cb4ef9f7870b5b1711c24cb05257472b` |
| `FrameTransferCocycle.olean.private` | `ee8a22426e870e68d9e40e15f0462228c341437e19f8e37fba3a0d5b0324f28b` |
| Original `SCOPE.md` | `c2a9050ac79109b8cf03b9fbceeba16ac92e21a9acb287ba31bdb0b19e32f8d4` |
| Original static review | `0350a3944487bc5217f00c8c67d1b810bade8cee1bfcbe31803d3c1ffda53a5a` |
| PR816 source text | `5f2069fe845df87caa3a4bdb1c2bd7434ff6513bddda5bc21f54f042a04a4e84` |

The proof source and Check remain byte-identical to the original independently reviewed draft. No statement, proof, import, option, or comment changed before the successful verification. The original SCOPE's UNCOMPILED status describes its delivery time and remains historical; the publication README supplies current status.

The written input is section 2 of null's PR816 at `eed6010347fcebc21aef30413b0e1da3be68a9b4`, path `research/hm/nonclosed-frame-transfer/NONCLOSED-FRAME-TRANSFER-EXACT-DEFECT.md`. A primary GitHub fetch at the exact reference returned Git blob `575004321d185de506573a1baad97bdf046b215f`, matching the independently hashed complete local text. No unverified geometric fact from that document is imported as a Lean axiom.

## Mathematical review

For the first theorem, applying `pc` and `ia` to the middle homotopy `dm ∘ h0 + h1 ∘ d0 = id − ib ∘ pb` kills its two left terms by `pc ∘ dm = 0` and `d0 ∘ ia = 0`. The remainder is `pc ∘ ia − pc ∘ ib ∘ pb ∘ ia = 0`, exactly the claimed transition composition after additive cancellation. The three complex components and three frame modules have independent types. No homotopy normalization or extra complex identity is needed for this conclusion.

For the inverse pair, `g_ab ∘ g_ba` uses frame b's middle homotopy followed by frame a's retraction; the opposite product uses frame a's homotopy followed by frame b's retraction. Both closed inclusions and closed projections are supplied. This establishes both inverse identities without dimension assumptions or a one-sided-inverse shortcut.

The defect theorem uses six independent frame modules `Ca`, `Cb`, `Cc`, `Da`, `Db`, `Dc`, with correctly directed transitions and arbitrary transfers. Expanding its right side cancels the two terms `gD_cb ∘ Mb ∘ gC_ba`. The remaining two terms become the left side using the supplied source and target cocycle equations. No compositions are commuted, and no defect is assumed zero. The theorem is valid for arbitrary transition maps satisfying those two equations; invertibility is not needed for this identity.

All three statements use arbitrary ring scalars and additive commutative module groups. There is no hidden field, dimension, basis, or characteristic hypothesis. At pinned mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`, the single imported `LinearMap.Defs` module supplies the required composition, evaluation, subtraction, and additive-group APIs with the exact rewrite orientations used. No broad import was added.

The source has exactly three theorem declarations and Check requests exactly those three names. Static inspection found no `sorry`, `admit`, custom axiom, unsafe declaration, native decision procedure, or oracle. The module does not duplicate the separate section 1 transfer-formula unit.

## Completed compilation and axiom evidence

`compile-0001` succeeded with exit code 0 and empty stdout/stderr, unchanged inputs, full cleanup, and no termination signal. It recorded 1.519587 CPU seconds, 3.894183750 wall seconds, 733102080 bytes sampled process-group peak RSS, and 744226816 bytes child `wait4` peak RSS. Its raw receipt SHA256 is `c11e49f572c17016e6da4c11995b3e5b2280800fff32ff7a3b31bbe531346b8c`.

`axioms-0001` separately imported the compiled module and succeeded with exit code 0, empty stderr, unchanged inputs, complete cleanup, and no termination signal. It recorded 0.970767 CPU seconds, 1.018882250 wall seconds, 700252160 bytes sampled group peak RSS, and 716046336 bytes child peak RSS. Its raw receipt SHA256 is `4e12e21e748314ddfbe3d68707940f0ae1101dda0c0b4371bb79d6561c84139f`; complete axiom stdout SHA256 is `c1bc2d74f5456bc9c20087fef481ac25a040e6ee6f1fb8d01ea5d6fc714d5f12`.

Each of these public names appears exactly once and reports exactly `[propext, Classical.choice, Quot.sound]`:

- `OAI.HorrocksMumford.frameTransition_comp`
- `OAI.HorrocksMumford.frameTransition_inversePair`
- `OAI.HorrocksMumford.frameTransfer_defectCocycle`

The theorem declarations, Check requests, and output names match exactly. No `sorryAx` or unexpected axiom is present. The current source, Check, imported olean, wrapper, and path-manifest hashes match the successful receipts. There are no compiler warnings or recorded failed proof attempts for this unit.

## Runtime and trust boundary

The runs used Lean4.34.1 and mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`. The explicit Lean executable SHA256 is `1b370cfcbf44e80d1b004ab1b1ab9a4c73951f9f7c242140bcff9bc577576554`; the common launcher is `ce5051e14a6d7b174195c9c949c91ea1c79e9c2ab49f9237c56da4eb48397a69`, and its recorded dependency search path is `7a93dfc6d5ce598755ad214d49792c947f3a8fdc4609e424266793e46715bdad`. The launcher selects one thread and `-M1200`, with no trust override.

The guard, SHA256 `6915a220408dc3bb5045b6cfaaaef8267a6516319cdb98deca5ba5717614c6fc`, retained its 60-second per-process CPU limit, 75-second wall watchdog, and sampled process-group RSS threshold of 1610612736 bytes at 0.1-second intervals. No resource limit increased. Darwin address-space enforcement remains unavailable, and RSS sampling provides no finite between-sample overshoot bound.

Module mode preserves kernel checking while importing exported dependency data. Lean4.34.1 computes exported axiom dependencies from full private bodies, so the importing axiom audit retains the transitive trust check. This review nevertheless trusts the pinned compiler and its imported artifacts; it is not exhaustive rechecking of every dependency binary. Comparator and an independent second kernel were not run.

## Application and publication scope

No blocker remains within the three-theorem conditional algebraic scope. Actual contractions, frames, transition identifications, and overlap compatibility must still be supplied in an application. A valid defect cocycle need not vanish and does not prove ordinary sheaf descent. The unit constructs no actual HM coefficient, physical tensor, source row, primitive, rank, or model solve, and proves no algebraicity theorem.

The accurate publication README replaces the historical uncompiled status and provides repository replay commands distinct from the archived isolated run. Final package assembly must preserve the source/Check hashes, copy exact axiom stdout, and normalize receipt evidence accurately; this review does not claim to have inspected evidence files that were not yet staged when it was written.
