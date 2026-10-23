# Independent review: source trace factorization

Verdict: **PASS** for the exact Lean source and check file below. The root
compiler run succeeded, and its separate imported-module axiom check succeeded
for all seven exported theorems. This reviewer inspected those completed runs
and their inputs without rerunning compilation. The conclusions are the
universally quantified conditional algebra statements in the source, not the
geometric premises needed for an actual Horrocks–Mumford application.

## Exact reviewed artifacts

Paths below are portable source paths or evidence basenames. This report omits
local host paths and process identifiers; original supervisor receipts remain
preserved separately and are identified by their exact hashes.

| Artifact | SHA-256 |
| --- | --- |
| `lean/OAI/AlgebraicGeometry/HorrocksMumford/SourceTraceFactorization.lean` | `cccb896a48cb8226a5c7ba68d16cee21f5786d1521263329fd8fa4a17e24da7c` |
| `Check.lean` | `1541afcfb66d7cbf58679fc254e9bc01cb1287c423f44b6f609561d81eaa5bb2` |
| Compiled `SourceTraceFactorization.olean` | `e164cc01c83e6d7fe76818e85897485bc6a71fa66560b00d065dfd50ba550df7` |
| `compile-0002.json`, original supervisor receipt | `10d2d832664cfe55f0ef4f8a17d3cf7e3ff993e8b3f036d3d4c4c6c7d652e634` |
| `axioms-0001.json`, original supervisor receipt | `6e4edd28bd7214dc7b9fd6bc6c163ede406543a063ca78c3b2061b9cd22c1d2f` |
| `axioms-0001.stdout` | `2f80bc609e4b40b15cdcd356404286fd135818641e746016c8cb84aae0346dba` |

The compile stdout and stderr and the axiom-check stderr are empty. Each has
SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

The source delta from the previous independently reviewed version is exactly
the leading `module`, `public import`, and `@[expose] public section`
declarations. Removing those adaptations reconstructs the prior source hash
`ab129122adb5cb64c23ddb7f5b135bfb3b68d6102c6c5f7a0570955b4642b414`.
Removing only the new leading `module` from the check file reconstructs its
prior hash `775758bc066cfa083007b4f0205b167c35b48dcf6ec2e222e4ddaafef86e32c8`.
Thus no theorem statement, construction, or proof body changed in this delta.

## Compilation and axiom evidence

The root launcher uses Lean 4.34.1, single-threaded (`-j1`) with internal memory
option `-M1200`, and the fixed mathlib import path. This reviewer independently
read the launcher and path configuration, checked the compiler version, and
confirmed mathlib HEAD is
`d13f23b723b8a846827a245b89c10fc7d3f11612`, with no tracked changes. The installed
Lean reports commit `5045d0056413266e57c625dcd7c365b10e377c52`; its executable
SHA-256 is `1b370cfcbf44e80d1b004ab1b1ab9a4c73951f9f7c242140bcff9bc577576554`.

The unchanged launcher has SHA-256
`ce5051e14a6d7b174195c9c949c91ea1c79e9c2ab49f9237c56da4eb48397a69`.
The compile receipt records the exact final source as an unchanged input.
The subsequent check receipt records the exact check file and the compiled
module hash above as unchanged inputs. Both runs report success, exit code 0,
complete cleanup, and no termination signals. The raw receipts hash the
launcher, path configuration, and listed inputs; they are not exhaustive
dependency-bundle attestations.

| Run | CPU seconds | Wall seconds | Sampled process-group peak RSS, bytes |
| --- | ---: | ---: | ---: |
| Module compile | 1.666798 | 3.434130292 | 900956160 |
| Imported-module axiom check | 1.129852 | 1.232511417 | 846266368 |

Both used the reviewed supervisor's limits: per-process CPU 60 seconds, wall
75 seconds, and sampled aggregate RSS 1610612736 bytes. RSS is sampled and is
not a hard address-space guarantee on Darwin. No limit was increased to obtain
these passes. Earlier failed attempts remain preserved; the verdict here is
bound to the final successful attempts, not to partial earlier output.

The check output lists each of the following seven names exactly once, and
every list contains only `propext`, `Classical.choice`, and `Quot.sound`:

- `OAI.HorrocksMumford.sourceTraceResponse_apply`
- `OAI.HorrocksMumford.sourceTraceFactorization_iff`
- `OAI.HorrocksMumford.sourceTrace_ker_le_of_exact`
- `OAI.HorrocksMumford.sourceTraceFactorization_of_exact`
- `OAI.HorrocksMumford.sourceTrace_same_source`
- `OAI.HorrocksMumford.correctedResponse_factorization`
- `OAI.HorrocksMumford.correctedResponse_same_source`

There is no `sorryAx` or unexpected custom axiom in that output. Source
inspection found no `sorry`, `admit`, custom axiom, or `native_decide`.

## Source authentication and mathematical scope

The reviewer independently fetched
[PR815's proof at immutable commit 0eaeca734b9e17142da2f1bdfd9a1721d0bb1d42](https://github.com/Akilleez-QA/read-em-and-weep/blob/0eaeca734b9e17142da2f1bdfd9a1721d0bb1d42/research/hm/affine-square-source-response/PROOF.md)
through the GitHub connector. The returned Git blob is
`bef4e26574b3085616c22d5fdaae4e808e3767e4`. The locally fetched snapshot has the
same Git blob and SHA-256
`78a0f462ffd0710d248658aaf95926f926297b0bae43aade85eb4c7fc934d236`, exactly
matching the source note read for the preceding static review. This
authenticates the source correspondence; it does not formalize that note's
geometric arguments.

The main theorem proves the correct module universal property: `ker d ≤ ker ell`
is equivalent to the existence of a unique linear response on `range d`
taking `d X` to `ell X`. The quotient construction supplies the response and
requires no assumed factorization, finite-dimensionality, basis, rank, or
surjectivity of `d`. Uniqueness is confined to the actual range, with no
canonical extension to all of `C1` and no interpretation as a map on `H1`.

The exactness corollaries derive the kernel inclusion from the explicit
equality `range delta = ker d` and the explicit identity `ell.comp delta = 0`.
They do not replace exactness by the weaker identity `d.comp delta = 0`.
The same-source theorem proves independence under `d X = d Y`. The two
corrected-response corollaries keep `Q`, `A`, and `y` fixed and require only
an independent action `[SMul S T]`; congruence suffices for their rewrites.

The corrected expressions are specializations in a common ambient coefficient
module. The actual graded multiplication from degree-twelve/twist-six trace
coefficients to degree-sixteen/twist-fourteen norm coefficients is not
constructed. Neither are the physical projection, complete monad complex,
cohomological comparison, ambient vanishing, or authenticated trace row.
Those geometric premises must be proved independently before application.
No actual rho16, beta4, affine reconstruction, or fifth-boundary value follows
from this unit alone. The earlier Python diagnostics do not discharge these
Lean hypotheses.

This review binds the theorem source and check file above. Subsequent
documentation-only packaging may explain the same limits; it must not enlarge
the theorem's established scope. A change to a statement, proof, or check file
requires another exact-byte review and the corresponding compiler check.
