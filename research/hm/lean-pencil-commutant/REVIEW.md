# Final independent review

Verdict: **PASS**, limited to the exact generic unit and root-run evidence below. This is an independent mathematics/evidence review of the root run, not a second kernel run or Comparator. No compilation, cache/build command, physical mathematical run, producer change, or worker spawn was performed by this reviewer.

## Mathematics and source binding

The supplied PR808 snapshot authenticates against the requested SHA-256 and Git blob `cd5adb3b98fc3df08154d2cb7dbd578e125f187f`, for [commit 3c2d80d5bbae109f810b1919fb0adbc2a1d0e392, section 2, equation (4)](https://github.com/Akilleez-QA/read-em-and-weep/blob/3c2d80d5bbae109f810b1919fb0adbc2a1d0e392/research/hm/source2-commutant-gate/PROOF.md). Authentication here is to the supplied immutable pin; the prior static review records its independent remote fetch. The final source and Check are byte-identical to that static review's exact original baseline.

`D0` includes all three unrestricted endomorphisms, with projections X2, X3, X4 in the correct order. `T0` includes both independent tensor-map channels. `pencilDelta` is a genuine `LinearMap`, with additive and scalar laws proved on each component by tensor extensionality. Its components are precisely X3 ∘ α − α ∘ (id_W ⊗ X2) and X4 ∘ β − β ∘ (id_W ⊗ X3). Both use id_W; the middle endomorphism participates in both channels. The commutative-ring/module hypotheses suffice, including subtraction; no basis or field is required.

All four theorems and their Check entries were inspected:

- `mem_pencilCommutant_iff`: kernel membership is exactly both intertwining equations, by product equality and subtraction equal to zero.
- `mem_pencilCommutant_iff_tmul`: quantifies over every w and every source vector in each channel. Evaluation proves necessity; tensor extensionality proves sufficiency, with no finite sampling or unsupported spanning premise.
- `pencilIdentity_mem`: the simultaneous identity triple satisfies both equations definitionally.
- `pencilCompose_mem`: componentwise X ∘ Y acts with X after Y. Each channel rewrites first by Y's equation, then X's; the source composition order agrees.

The kernel supplies additive/scalar closure; identity and composition supply unital composition closure, without constructing a bundled subalgebra. No invertibility restriction, scalar-block restriction, omitted channel, `sorry`, `admit`, custom axiom, unsafe declaration, or native decision procedure appears in the unit.

**Equivariance boundary:** this uses unrestricted `End`/`Hom`. Actual PR808 `End_G`/`Hom_G` requires restriction to equivariant triples, supplied group actions and equivariant tensors, and the corresponding equivariant target spaces. This restriction is not constructed. There is no claim of 113/153 dimensions, ranks, classifications, actual HM data, source2 exclusion, or full repair.

## Root-run evidence and limits

Both raw receipts have status success, child return code 0, unchanged-input checks true, cleanup complete true, CPU limit applied true, no signals, and zero observed RSS/wall overshoot. Compilation stdout/stderr and import-check stderr are empty. Import-check stdout reports exactly `[propext, Quot.sound]` for each of the four names above: permitted foundational closures, with no `sorryAx`, custom axioms, or native-computation axiom.

| Root phase | Wall seconds | Child CPU seconds | Sampled group peak RSS bytes | Child peak RSS bytes | Samples |
| --- | ---: | ---: | ---: | ---: | ---: |
| compile-0001 | 4.201414375 | 2.070767 | 875167744 | 882032640 | 39 |
| axioms-0001 | 5.429381292 | 1.471408 | 838221824 | 841449472 | 50 |

Each run allowed 75 seconds wall, 60 seconds soft/hard CPU per process, and 1610612736 bytes sampled group RSS at 0.1-second intervals. Warnings/limitations: address-space enforcement was false; CPU is per process, not aggregate group CPU; RSS sampling has no finite guaranteed overshoot bound; watchdog detection can lag with scheduling/process-inspection latency; process-group containment is not a sandbox. Child CPU covers the direct child's wait4 usage including descendants it waited for. Cleanup and run-time unchanged inputs are receipt assertions, independently read here, not reconstructed process history.

The launcher selects the isolated Darwin arm64 Lean 4.34.1 installation, uses `-j1 -M1200`, sets one Lean thread, prepends the unit build directory to LEAN_PATH, and compiles only the target module before importing it through Check. The dependency checkout HEAD is mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`; its toolchain is `leanprover/lean4:v4.34.1`. This is normal isolated pinned validation, not an entire upstream build. All current receipt-listed executable, supervisor, launcher, search-path, source, Check, and imported olean bytes match their receipt hashes. The module receipt does not separately bind an output hash; the subsequent import receipt binds the current olean. Compiler/dependency hashes below are current inspection bindings, not extra fields retroactively attributed to the receipts.

## Portable SHA-256 bindings

Labels are logical artifact names; raw JSON files retain their original bytes. No host paths or process identifiers are reproduced here.

| Artifact | SHA-256 |
| --- | --- |
| `PencilCommutant.lean` | `71ed8339d4ffa55cbc0a6d22e488cd1f0e411a065ede0eb938e365a30443eeda` |
| `Check.lean` | `d6c4c9d3c121875b5bb7ed23e4cab70a434f6d17d1ceaabcd0a933fb27a8fe25` |
| `SCOPE.md` | `cb2d43aaea90bf5c9dbe8201fc5218ad6019aaea0b73f9c7c6d97198fa00f482` |
| `PencilCommutant.olean` | `c99cacbe534c89b7fce52cb41a220210f872c2cf372c3d118498c0bb8c137b8f` |
| `PR808 snapshot` | `316ef592bc74f29de4698e740b90ad760ef7ad6cc09777ae3d913fc69043a5d2` |
| `STATIC-REVIEW.md` | `e918c90bfa4a242ac31f24e5460d9d959d8b3230fbd54c3ace26aecc6b851ef7` |
| `Lean compiler binary` | `1b370cfcbf44e80d1b004ab1b1ab9a4c73951f9f7c242140bcff9bc577576554` |
| `mathlib lean-toolchain` | `d5edba4e4b8faad9c1baeadb265716d20d03be4d1a2647dc5e35b0c0325bea7b` |
| `mathlib lake-manifest.json` | `8f67b2cf24143ac091cdb425e886c2164b2fc2d6fbccd6db9454b697f9541a67` |
| `python3` | `5b1ddb7e9c11b87a034fc88b212e8ac243cfe2b4db696d767aa44c79595fc09a` |
| `burn_guard.py` | `6915a220408dc3bb5045b6cfaaaef8267a6516319cdb98deca5ba5717614c6fc` |
| `run-module.py` | `ce5051e14a6d7b174195c9c949c91ea1c79e9c2ab49f9237c56da4eb48397a69` |
| `lean-path.txt` | `7a93dfc6d5ce598755ad214d49792c947f3a8fdc4609e424266793e46715bdad` |
| `compile-0001.json` | `9b3d44ec04b9681d0af6210a21e6126a2fc0f930a9a6d8ae5a1b15dc7d9ce4e4` |
| `compile-0001.stdout` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `compile-0001.stderr` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `axioms-0001.json` | `2addfd0852be117ad5bdb474114a73bd513754689be50c75d07ddc3b82cbc36c` |
| `axioms-0001.stdout` | `685fd3b20eadf2c39a6d62f31479213e100c4963499243adb030e9a2565511a0` |
| `axioms-0001.stderr` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

Receipt command SHA-256 values are `0422632c76c2a4a6372f7befde7bdf4d53dc2a03b9adf51e10ac176e1b1bc123` (module) and `6c5093f8ef23f7a35502d8bb17623aae54cb522d797324696d1a43b7cee91c9e` (check). The raw receipts and streams remain in the parent review directory. README supplies portable repository replay commands; those commands were not executed in this review.
