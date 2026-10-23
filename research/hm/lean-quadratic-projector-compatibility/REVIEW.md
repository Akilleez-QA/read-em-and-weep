# Independent review: quadratic projector compatibility

Verdict: **PASS** for the exact source and check file below. The root's final
source compilation and imported-module axiom audit both succeeded. The reviewer
read the completed receipts and outputs, checked their binding to the final
files, and did not rerun compilation. The result is the universal conditional
algebra in the file; no actual quadratic multiplication or geometric lift is
certified.

## Exact artifacts and final delta

Portable source paths and evidence basenames are used below. The original
supervisor receipts are preserved separately; this review does not reproduce
their host paths or process identifiers.

| Artifact | SHA-256 |
| --- | --- |
| `lean/OAI/AlgebraicGeometry/HorrocksMumford/QuadraticProjectorCompatibility.lean` | `1bc07ce1ca444f822abc5a6c344d099475c9b6e45cc024ae2985878bb5b7ba32` |
| `Check.lean` | `6c62e0050b693989860e243cb74d015f7b8c257d165db82091230d3d7eeee2e5` |
| Compiled `QuadraticProjectorCompatibility.olean` | `e158122df3c4f2104061e5a322870d0817b549db632c22a4f356d55c8b2b001c` |
| `compile-0002.json`, original supervisor receipt | `72d06df30b9268f987023053d30501bccbae329d96877037599eb204ac537b65` |
| `axioms-0002.json`, original supervisor receipt | `2878840cea19452d0b1b9e4997fd50ab641e1d617731f3ea3c6782e2287e4661` |
| `axioms-0002.stdout` | `ef5224a1abeb62de34fdd7883425d2e0b18c4659087fbbbef98b14cd859001d6` |

Compile stdout and stderr and axiom-check stderr are empty, each with SHA-256
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

The original independently reviewed source had SHA-256
`e3fdda53ec7db0935ec43d2a51a4eee614f25eafdd6dc1b65e8e190e8096f761` and its
check file had SHA-256
`5af1c6d45c05aaa83a61535397f49811c818a21a9d171750e2e8b2a2565d8547`.
The final source replaces only the introductory words “UNCOMPILED draft” with
“Supporting algebra”; the check file replaces only its stale uncompiled-status
comment with a neutral axiom-audit description. The statement and proof bodies,
imports, module/export declarations, and three axiom requests are unchanged.
The original draft and its static review remain preserved.

## Mathematical and API review

The cross-term equivalence has the correct fixed-map typing. For a linear
`q : V → W` and idempotents `p`, `r`, intertwining makes the first cross term
zero by `p² = p` and the second by `r² = r`. Conversely, the first zero equation
gives `r(q x) = r(q(p x))`, and the second gives
`q(p x) = r(q(p x))`. Together they give intertwining at every `x`. Both
cross terms are retained; preservation of only one summand is not promoted to
intertwining.

The second theorem is also exact. Intertwining sends the image and kernel of
`p` into those of `r`. Conversely, `p x` is sent to an element fixed by `r`
using image preservation and `r² = r`; `x − p x` is in the kernel of `p`
using `p² = p`, so its image is killed by `r`. These two facts give
`r(q x) = q(p x)`. There is no hidden chosen complement, dimension argument,
or division. Semiring scalars with additive-group modules are sufficient.

The family theorem applies the first equivalence to every supplied map, with
correct universal quantifiers. It assumes no linearity in the family index
and is valid even when the index type is empty.

Before compilation, the reviewer checked the pinned mathlib signatures for
`comp_apply`, `congr_fun`, `sub_apply`, `zero_apply`, `mem_range`,
`mem_range_self`, and `mem_ker`. The sole direct import
`Mathlib.Algebra.Module.Submodule.Range` publicly imports the kernel API;
the required subtraction instance exists with the stated scalar assumptions.
No extra import or stronger coefficient hypothesis was needed.

## Final compiler and axiom evidence

Both final runs used Lean 4.34.1, commit
`5045d0056413266e57c625dcd7c365b10e377c52`, and the pinned mathlib checkout
`d13f23b723b8a846827a245b89c10fc7d3f11612`. The shared launcher and path
configuration hashes are unchanged from the independently inspected runtime:

- Launcher: `ce5051e14a6d7b174195c9c949c91ea1c79e9c2ab49f9237c56da4eb48397a69`.
- Path configuration: `7a93dfc6d5ce598755ad214d49792c947f3a8fdc4609e424266793e46715bdad`.
- Installed Lean executable: `1b370cfcbf44e80d1b004ab1b1ab9a4c73951f9f7c242140bcff9bc577576554`.

The compile receipt records the final source hash as an unchanged input. The
separate axiom audit records the final check file and the compiled module hash
above as unchanged inputs. Both report success, exit code 0, complete cleanup,
and no termination signals. These receipts bind their listed inputs; they are
not exhaustive attestations of every dependency binary.

| Run | CPU seconds | Wall seconds | Sampled process-group peak RSS, bytes |
| --- | ---: | ---: | ---: |
| Final module compile | 1.236467 | 1.332895917 | 804126720 |
| Final imported-module axiom check | 0.990632 | 1.017032625 | 775700480 |

The unchanged limits were one compiler thread, Lean's `-M1200`, per-process
CPU 60 seconds, wall 75 seconds, and sampled aggregate RSS 1610612736 bytes.
RSS sampling is not a hard address-space limit on Darwin. No resource cap was
increased for these passes.

All three exported theorem names appear exactly once in the final output:

- `OAI.HorrocksMumford.quadraticProjectorCompatibility_iff_crossTerms`
- `OAI.HorrocksMumford.quadraticProjectorCompatibility_iff_range_ker`
- `OAI.HorrocksMumford.quadraticProjectorCompatibility_family_iff_crossTerms`

Each depends only on `propext`, `Classical.choice`, and `Quot.sound`. There is
no `sorryAx` or unexpected custom axiom. Source inspection found no `sorry`,
`admit`, custom axiom, unsafe declaration, or native decision procedure.
Comparator and an independent second kernel were not run.

## Authenticated source and application boundary

The reviewer independently fetched
[PR818's proof at commit f4a73af666900ad2cb34a756d24b88e19dd6feaa](https://github.com/Akilleez-QA/read-em-and-weep/blob/f4a73af666900ad2cb34a756d24b88e19dd6feaa/research/hm/negative-truncation-extension/PROOF.md)
through the GitHub connector. Git blob
`2ba0a7eee6ef2eb5413683e85618d7902dca3970` matches the local source with
SHA-256 `7525df1e58ac8683a5a0b828209f4f35cc79a09527307ee47b35025d5c2ad636`.
The earlier independent written review, SHA-256
`4f989434cea20d2d451c2fcf429065e3f0c266d0a276e2f8e37b1aa8f3c606d2`, was
read for its projector consequence and strict non-exclusion boundary. Neither
the source citation nor that written review imports geometric facts into Lean.

To apply the bundled statement to
`q₊ : Sym²(T₊) ⊗ N₂ → N₄`, the domain projector must be `id ⊗ p₂`, with its
idempotence proved, and the target projector must be `p₄`. Alternatively, one
can supply the family `q_s(x) = q₊(s ⊗ x)` and use `p₂`, `p₄`. The present
file constructs none of these actual tensor or family inputs. Its word
“quadratic” denotes the motivating action; its theorem input is linear.

Thus the unit supplies an exact compatibility criterion only. It does not
evaluate either actual cross term, identify the actual positive quadratic
action, prove a window/full-module lift or splitting, formalize the
minimal-submodule extension theorem, or exclude source2. No actual coefficient,
point, tensor, rank, or model solve was evaluated in this review. The failed
full-module extension route and the distinct submodule-filtration route in the
written source remain separate from this supporting formal lemma.
