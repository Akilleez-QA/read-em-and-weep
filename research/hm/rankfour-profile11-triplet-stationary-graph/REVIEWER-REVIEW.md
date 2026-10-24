# Independent whole-proof review

## Verdict and exact binding

**PASS: the entire conditional geometric proof is valid under its explicitly retained actual-geometric and transitive assumptions.** No mathematical flaw requiring a change was found. This is an entire-proof verdict, not merely a checker verdict.

The reviewed frozen file is `PROOF.md`, exactly **12,872 bytes**, with:

- SHA256: `96c3a9dea9260bcc34435220e00ad78a721bb18423d38b3a9aae3b7124eab7b7`
- Git blob SHA1: `f27519105e0ff214cd6b7f78b6c24ee1acfe7f7c`

I read the full statement, Sections 1–6, every displayed implication, and all scope limitations. I also read the complete sole direct input, all of `verify.py`, all of `characters.py`, `INPUTS.json`, and `REPRODUCE.md`. The six selected files were not edited. No GitHub write, selected actual HM/source-instance evaluation, broad scan, or large computation was performed.

## Independent authentication of the complete direct original

I made two new read-only connector requests, independently of the author's local fetch records:

1. `github.fetch_file` at repository `Akilleez-QA/read-em-and-weep`, immutable commit `f7abba83fedd46a9d91f5abbd9e40d3b02ae65f1`, path `research/hm/rankfour-profile11-triplet-nonsplit-quotient/PROOF.md`, requesting the complete base64 content.
2. `github.fetch_blob` at Git blob `1974a5c3b20546dcb414539096511388f495cdab` in the same repository, receiving the complete UTF-8 text.

The complete decoded path bytes, complete blob bytes, and selected `inputs/nonsplit-quotient.md` bytes are identical. Each has 13,619 bytes, SHA256 `d4ff280dc943c2a112ea68ff4d9c4750fe5f93b3892d8a104fa9c08aa5960568`, and independently recomputed Git blob SHA1 `1974a5c3b20546dcb414539096511388f495cdab`. The path response also reports that same Git SHA1. These match every corresponding `INPUTS.json` field. Full results are in `REVIEWER-AUTHENTICATION.json`; raw fresh fetch records are excluded from publication/replay.

Canonical original: https://github.com/Akilleez-QA/read-em-and-weep/blob/f7abba83fedd46a9d91f5abbd9e40d3b02ae65f1/research/hm/rankfour-profile11-triplet-nonsplit-quotient/PROOF.md

The original is PR1222's complete nonsplit-quotient proof, not an excerpt or mutable-branch substitute. Its statement and Sections 1–8 provide the actual symmetric pairing, low-order pairing vanishings and reduced norm divisor, actual quotient identification, unique splitting adapted to `U5/U4`, actual saturated `L10` embedding, nonzero `F6/G6` graph, and retained scope used here. I checked these handoffs against the complete input. Its transitive hypotheses are retained assumptions: this review does not silently claim fresh authentication of every earlier transitive document or independent realization of that geometry.

## Statement and boundary

The claim is correctly conditional on the residual simultaneous rank-seven, lower-column `k=2` configuration. The splitting `B6/G6=A8 direct-sum C4` is the one induced by the unique actual splitting relative to `A8=U5/U4`, not an arbitrary abstract decomposition or the earlier splitting adapted to `F6/G6`.

The conclusion `phi=-psi/2` is meaningful as an equality in the actual sheaf `Hom(A8,C4)`. It does not choose a value for a source parameter, an invariant normalization, or a graph scalar. The claimed converse is expressly limited to first-order vanishing of the intrinsic derivative on the reduced divisor, equivalently at least simple divisibility of that morphism by the divisor. It does not assert its exact coherent image, generic rank, higher-order vanishing, algebraicity, occurrence, or branch exclusion.

## Section 1: retained geometry and derivative kernels

The ranks, degrees, inclusions, symmetric constant `h`, auxiliary flags `Uj=h(Tj)`, reduced norm divisor, and vanishing pairings are consistent with the complete input and its retained flag hypotheses. In particular, `U4` annihilates `T7` and `U5` annihilates `T6` because the relevant total orders are at most eleven.

The assertions `B6^-=B7` and `d(B7) subset B6 tensor Omega^1` are actual statements in the constant ambient bundle. For a local section `b` of `B6`, differentiating `<b,v^(i)>=0` for `i<=6` gives `<b',v^(i)>=-<b,v^(i+1)>`. The only new condition is annihilation of `v^(7)`, and jet separation identifies the kernel exactly with `B7`. The same identities give the derivative inclusion for all sections of `B7`. No horizontal quotient splitting is needed.

The final normal line for `B7` is therefore `(B6/B7) tensor Omega^1=O(4-2)=O(2)`. This is the correct cotangent twist, rather than `O(4)` or a tangent twist.

## Section 2: both graph descriptions, the unit, and fibers

`B7/G6` is a saturated degree-minus-eight line in `B6/G6`. A zero projection to `A8` would place it wholly in `C4`; a nonzero map `O(-8)->O(4)` has a nonempty zero divisor, so that cannot be a subbundle inclusion. Its nonzero projection to `A8` is an isomorphism. Thus `psi` is an actual globally defined graph map.

The complementary `C4` maps isomorphically, everywhere, onto `B6/B7`: a graph over `A8` has zero intersection with the vertical complementary summand. Moreover, annihilator duality identifies `B6/B7` with `(T7/T6)^*`, since the jet inclusions are saturated. Pairing a lift of a `C4` frame with the local generator `v^(7) modulo T6` consequently gives a unit `rho`. A merely generically nonzero factor would not suffice; the proof has the stronger everywhere assertion needed here.

The formal identities have the correct signs and factors. Differentiation of `p56=0` gives `p66+p57=0`, hence `p57=-s`. Symmetry gives `s'=p76+p67=2p67`. The `B7` graph then satisfies `-s+b rho=0`, so `b rho=s`. Because `rho` is a unit, the graph `psi` is nonzero with precisely the simple norm divisor `D12`.

Both graphs vanish on `D12`. As full preimages of their quotient lines, `F6` and `B7` therefore have equal rank-seven fibers there. This does not identify their sheaf intersection with those fibers: the retained intersection sheaf is `G6`, of rank six. The proof explicitly preserves this failure of intersection to commute with restriction and does not infer false fiberwise transversality.

## Section 3: the full generator check

The five `U4` generators, one `L10` generator, and the graph generator give all seven local generators of `F6`.

Before taking the last normal component, every derivative of a section of `F6` lies in `B6` along `D12`. This follows from the second fundamental form of `B6`, whose fiberwise kernel is `B7`, and the equality of restricted `F6` and `B7` fibers. This step justifies discarding all other ambient normal directions; testing only the pairing with `v^(7)` without it would not have sufficed.

For `U4`, differentiation lands in `U5`, and `U5` lies in the common `F6=B7` fiber on `D12` because both graphs vanish there. For `L10`, its derivative is in `B6` since `L10 subset B7`. Its remaining normal component is the equivariant morphism `O(-10)->O(2)`. Its section space is the degree-twelve invariant space, which is one-dimensional and generated by the universal invariant whose divisor is `D12`. Thus this component vanishes there, including the possibility that the morphism is identically zero. The argument neither assumes nonzero image nor replaces an exact coherent image by its saturation.

These checks also justify the use of arbitrary local sections rather than isolated generators: after taking the normal quotient, the derivative defines an `O`-linear second fundamental form; coefficient-derivative terms stay inside the bundle. All non-graph generators are genuinely covered.

## Section 4: the remaining derivative identity

Local lifts through `R` exist because `R->C4` is a surjective bundle map. The section `sigma=u5+a r` is in the full inverse image defining `F6`, and its image generates `F6/G6`.

In the constant ambient bundle its derivative pairs with `v^(7)` as `p67+a' rho+a<r',v^(7)>`. The last term vanishes modulo the divisor because `a` does. Differentiation of `b rho=s` gives `s'=b' rho` there because `b` also vanishes. The resulting last normal component is exactly `rho(a'+b'/2)`, with no missing derivative of a quotient connection or of a chosen horizontal splitting.

The preceding full-generator and ambient-normal checks, together with invertibility of `rho`, establish both directions of (17). In particular, the local computation is not only a necessary test on one chosen vector.

## Section 5: invariance, double divisibility, and converse

The section `eta=phi+psi/2` already lies in `I_D Hom(A8,C4)`. Its leading class in `(I_D/I_D^2) tensor Hom(A8,C4)|D` is intrinsic. At each point of the reduced divisor on the smooth characteristic-zero curve, differentiation of a local equation is nonzero. Hence vanishing of the local coefficient differential is precisely membership in `I_D^2 Hom(A8,C4)`.

All listed choice changes are harmless:

- Frame and coordinate changes multiply the relevant first-order class by units; extra differentiated-unit terms contain the section already vanishing on `D12`.
- Two lifts of the same `C4` frame through `R` differ by `L10`, and ambient lifts further differ by `U4`. In the graph generator such changes carry the vanishing factor `a`; differentiation contributes only a vector already in `F6` along the divisor, or a term multiplied by `a`.
- Changing a representative modulo `U4` contributes a `U4` section, whose derivative has already been checked.

No connection on `Hom(A8,C4)` is introduced. Double divisibility forces a global section of `O(12)(-2D12)=O(-12)`, which has no nonzero sections. Thus `eta=0` and the stated actual graph equality follows. Conversely, that equality makes the last normal component zero; the other six generators were already checked, so the whole intrinsic derivative vanishes on `D12`. This does not establish equality with any proposed exact coherent image.

Rescaling `h` by a nonzero constant leaves the subbundles `Uj`, the specified subline `A8`, the quotient, and the unique actual complement unchanged. Thus it leaves the graph morphisms themselves unchanged. In the displayed local formulas it scales `u5`, `s`, and the corresponding graph coefficients compatibly, preserving both equations and the vanishing criterion. The factor `-1/2` is therefore not a normalization artifact.

## Section 6: contribution and limits

The nonzero graph is uniquely determined relative to the actual original `B7` graph. Since `psi` is nonzero and the ground field has characteristic zero, `-psi/2` is nonzero and distinct from `psi`, so the result is compatible with the retained sheaf intersection. This is a new necessary embedded condition, not a contradiction or realization of the residual case.

All stated exclusions are appropriate: the argument supplies no original tenth jet, higher-order ramification data, algebraicity, selected source instance, or whole-profile conclusion. The cyclic alternative, local defect alternatives, independent `e9` endpoint, and both `F18` forms remain outside the theorem. No boundary statement in the proof turns the conditional result into an occurrence or branch-exclusion claim.

## Checker inspection and selected-only replay

I inspected every executed operation and unused helper in `verify.py` and `characters.py`. The checker uses explicit `RuntimeError` guards rather than optimization-removable assertions. It checks full input and frozen-proof hashes, fixed universal invariant multiplicity, degree/rank arithmetic, formal symmetry/Leibniz coefficients, and the conormal degree obstruction. The imported module performs 81 fixed exact-rational McKay character identities. Its recursion used here is bounded at degree twelve; its unused helper functions do not execute a scan. None of these operations selects or evaluates an actual HM/source coefficient, parameter, point, jet, tensor, matrix, instance rank, or invariant normalization.

Exactly the six files listed in `REPRODUCE.md` were copied, with relative paths preserved, into a newly empty isolated directory. Both prescribed commands were run with `PYTHONDONTWRITEBYTECODE=1` and empty `PYTHONPATH`. Normal Python and `python -O` each returned `PASS` with 31 explicit checks. Separate same-mode imports of the unchanged selected character module confirmed 81 executed imported checks in each mode. Thus each mode performed 112 explicit-plus-imported checks.

The two checker stdout byte strings and parsed result objects are identical. The selected source and copied bytes, their lengths and hashes, and the six-file listing were unchanged after all runs. No cache, extra replay input, installation, or network action was needed in the replay. Full before/after manifests, commands, outputs, counts, and proof binding are recorded in `REVIEWER-REPLAY.json`.

The arithmetic replay supports but does not replace the independent geometric reasoning above. The final PASS is bound only to the exact whole-proof bytes stated at the start and to the explicitly retained hypotheses and first-order scope.
