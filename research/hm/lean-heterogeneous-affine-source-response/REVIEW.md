# Independent review: heterogeneous affine source response

Verdict: **PASS** for the exact source and check file below. The root's
compilation and separate imported-module axiom audit both succeeded. This
reviewer inspected the completed receipts, outputs, and source correspondence
without rerunning compilation. The conclusions are conditional algebraic
identities, not a construction or verification of the geometric inputs.

## Exact artifacts

Paths below are portable source paths and evidence basenames. Original
supervisor receipts are preserved separately; their host paths and process
identifiers are not reproduced here.

| Artifact | SHA-256 |
| --- | --- |
| `lean/OAI/AlgebraicGeometry/HorrocksMumford/HeterogeneousAffineSourceResponse.lean` | `8d0e2257a05d2c88b3414edf588e93ca6f98277b665f912b2772342fafa39ac3` |
| `Check.lean` | `f9409f0a141ca78ce3da4f4bda83251fc3e4f2a9c7bd03693566a2fe62ac4d17` |
| Compiled `HeterogeneousAffineSourceResponse.olean` | `834ba20e09b906bc8edb542124a26e68d2c5ae188f0ad1f692c1d95952a73565` |
| `compile-0001.json`, original supervisor receipt | `3d2cbadee3c80bb8f172d5a35933f81894b83ea1b06c584c811d8aba39d0c067` |
| `axioms-0001.json`, original supervisor receipt | `cc1945b72f9041da91e0a5c31a45922c5aa36db5a0060b87c41169adfe87e948` |
| `axioms-0001.stdout` | `b404d9d6391e6cb0d034984cd165068a1d73e4bc2bd61f62fae98ded3268ecb8` |

Compile stdout and stderr and axiom-check stderr are empty. Each has SHA-256
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
The final source and check file are byte-identical to the independently
reviewed static baseline; no proof, statement, import, or comment delta was
needed. The original draft files and static review remain preserved.

## Mathematical proof and source correspondence

The reviewer read equations (13), (14), (16), and (20)–(24) of
[PR815's proof at commit 0eaeca734b9e17142da2f1bdfd9a1721d0bb1d42](https://github.com/Akilleez-QA/read-em-and-weep/blob/0eaeca734b9e17142da2f1bdfd9a1721d0bb1d42/research/hm/affine-square-source-response/PROOF.md).
The published snapshot has SHA-256
`78a0f462ffd0710d248658aaf95926f926297b0bae43aade85eb4c7fc934d236` and Git blob
`bef4e26574b3085616c22d5fdaae4e808e3767e4`, independently authenticated through
the GitHub connector during the source-trace review. This authentication does
not turn the written source's geometric premises into Lean facts.

The modules `Ti`, `Tj` and `Ni`, `Nj` remain distinct: they motivate trace
coefficients of degree twelve/physical twist six and norm coefficients of
degree sixteen/physical twist fourteen. Multiplication by `A = a³h`, of
degree four/physical twist eight, motivates the supplied linear maps `μi`,
`μj`. No graded coefficient space is defined in the unit.

The exact source dictionary is essential. Formal `yi` denotes the already
traced lower term `τ_i(y_i)` in equation (24), and `f` denotes `τ_i(F_ij)`.
The linear map `h : Nj → Ni` is the scalar transport `λ^sc_ij`, directed from
chart `j` to chart `i`, not the polynomial source named `h` in `a³h`. The map
`g : Tj → Ti` transports trace coefficients. Equation (14) is therefore
exactly the supplied hypothesis `h Qj - Qi = μi f`. Compatibility
`μi.comp g = h.comp μj` is a separate explicit hypothesis.

Formal `Li`, `Lj` denote supplied trace rows `Λ_i`, `Λ_j`, while `s` motivates
the full corrected source `a(V_h - b Z_a) - q W_h`. The common module `P` is
supplied independently, with its own universe; no equality with `range d` or
membership of the intended source is inferred. All physical restrictions and
frame/marking factors must be supplied before an application.

Writing `ui = yi - Li s`, `uj = yj - Lj s`, the first theorem follows from

    (Qi + μi ui) - h(Qj + μj uj)
      = (Qi - h Qj) + μi ui - μi(g uj)
      = μi(ui - g uj - f).

This checks both the target-minus-transport direction and the minus sign on
the affine shift. The Lean proof expands linear-map addition/subtraction,
uses the correctly oriented transport equality, and proves the remaining
additive rearrangement using `abel`. There is no multiplication between
elements of different coefficient modules.

The second theorem proves norm equality if and only if the displayed trace
defect is in `ker μi`. It neither assumes injectivity nor cancels the map.
Only the third theorem assumes `Function.Injective μi`; then zero image
forces zero trace defect and the additive rearrangement yields

    Li s - g(Lj s) = yi - g yj - f.

No inverse or surjectivity is needed. In an application, the injectivity
must concern the regular coefficient module; fiberwise cancellation at
source zeros is not established. The theorem is correct without a field,
dimension, basis, or nonzero source assumption beyond its stated ring/module
and explicit injectivity hypotheses.

## Completed compiler and axiom evidence

The runs used Lean 4.34.1, commit
`5045d0056413266e57c625dcd7c365b10e377c52`, and mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`. The shared launcher and path
configuration match the independently inspected pinned runtime:

- Launcher: `ce5051e14a6d7b174195c9c949c91ea1c79e9c2ab49f9237c56da4eb48397a69`.
- Path configuration: `7a93dfc6d5ce598755ad214d49792c947f3a8fdc4609e424266793e46715bdad`.
- Installed Lean executable: `1b370cfcbf44e80d1b004ab1b1ab9a4c73951f9f7c242140bcff9bc577576554`.

The compile receipt records the exact source as an unchanged input. The
separate check receipt records the exact check file and compiled module
listed above as unchanged inputs. Both report success, exit code 0,
complete cleanup, and no termination signals. They attest to their listed
inputs, not to an exhaustive bundle of every dependency binary.

| Run | CPU seconds | Wall seconds | Sampled process-group peak RSS, bytes |
| --- | ---: | ---: | ---: |
| Module compile | 1.679873 | 4.722121333 | 819167232 |
| Imported-module axiom audit | 1.044308 | 1.241763834 | 756727808 |

Both used one compiler thread, Lean's `-M1200`, per-process CPU 60 seconds,
wall 75 seconds, and sampled aggregate RSS 1610612736 bytes. Sampled RSS is
not a hard address-space limit on Darwin. No cap was increased for these
passes. The reviewer performed no additional compile or mathematical run.

All three exported theorem names appear exactly once in the final axiom
output:

- `OAI.HorrocksMumford.affineSourceNormResponse_defect`
- `OAI.HorrocksMumford.affineSourceNormResponse_eq_iff_mem_ker`
- `OAI.HorrocksMumford.affineSourceNormResponse_eq_iff_of_injective`

Each depends only on `propext`, `Classical.choice`, and `Quot.sound`. There
is no `sorryAx` or unexpected custom axiom. Source inspection found no
`sorry`, `admit`, custom axiom, unsafe declaration, or native decision
procedure. Comparator and an independent second kernel were not run.

## Strict application boundary

The useful addition is a heterogeneous, conditional coefficient-overlap
criterion. Actual multiplication, regular-section injectivity, physical
transports, the affine shift, contractions, trace-response rows, complete
monad exactness, and cohomological comparison remain separate obligations.
The existing source-factorization theorem can be used only after its own
inputs and source-image identification are supplied.

The defined response has its difference from `Q` in the image of `μ`; it
does not show that an independently supplied norm coefficient satisfies
equation (16), or that this response is the actual norm. No global gluing,
source existence, source2 exclusion, actual HM coefficient/rank, or original
proof repair is established by this unit alone. The separate PR816
frame-transfer and transition-cocycle units are not silently substituted for
the physical-to-coefficient application bridge.
