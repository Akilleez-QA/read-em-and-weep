# Proof repair: current status

**Craig Ward · 23 October 2026 · Mathematical checkpoint through PR1008**

**The original proof repair is open. Four necessary catalogue pairs across three stable labels remain.** Recent work restricts compatible radical actions and obstruction maps; it does not yet establish an actual source or complete the required lifting/algebraicity argument.

[Latest mathematical update](paper/60-cdf-duality-complement-barrier.md) · [Paper index](paper/README.md) · [Detailed status](paper/01-current-status.md) · [Archived checkpoint history](paper/52-root-status-archive-through993.md)

## What is established now

- **c-d-f cubic reduction:** assuming only Q(X_B)⊂Y_B, the preserved block's internal second vanishes globally and its internal third lies in a raw three-dimensional space. Its nonvanishing is equivalent to generic original-fourth nonvanishing; neither value nor the preservation hypothesis is selected. No κ restriction or secondary ν is imported. [Actual interface and cubic](paper/59-cdf-preserved-b-cubic.md) Duality, endpoint characters and scalar commutant do not automatically give complementary preservation; an exact formal counterfamily blocks that shortcut, without realizing an actual HM map. [Duality boundary](paper/60-cdf-duality-complement-barrier.md)

- **Whole octic generator geometry:** its zero scheme has length46: six triple fat points and ten simple points, with no square-conic zeros. The target factor alone still has length34. This computes the canonical nonzero generator, not its actual scalar, which remains unknown. [Full generator](paper/58-full-octic-generator-zero-scheme.md) · [Target factor](paper/56-octic-target-zero-scheme.md)

- **A proposed octic test is ruled out:** every equivariant quartic covector kills ρκ, so secondary naturality is automatic on the octic line even if ν≠0. It cannot select the remaining scalar. A different actual-complex relation is needed; no new symbol vanishing follows. [Exact zero restriction](paper/54-secondary-octic-zero-test.md)

- **New full-radical Type II restriction:** the internal fourth through seventh symbols vanish globally. The eighth lies in a canonical one-dimensional rank-one line satisfying quotient-kernel naturality; its actual scalar remains unselected. This is internal progress, distinct from the already known all-orders original generic vanishing. It does not extend to the single-line cubic cases. [Octic gate and scope](paper/53-internal-octic-gate.md)

- **Single compatible radical line:** its endpoint ranks have four necessary possibilities in Type I, six in Type II and three in Type III. The rows (9,4) and (14,9) force generic original rank 36 and every original generic Bockstein after the second to vanish. Four other abstract endpoint-module rows admit surjections, so rank data alone cannot exclude them. No row is asserted to occur. [Classification and limits](paper/50-compatible-line-footprints.md)
- **Single-line non-acyclic reduction:** for u=0,k=1, the internal second vanishes and the internal third lies in a canonical two-dimensional cubic space. Its nonvanishing is equivalent to generic original-fourth nonvanishing. **The cubic is unselected here.** No secondary scalar ν or full-radical conclusion transfers automatically. [Exact applicable rows and interfaces](paper/51-single-line-symbol-transfer.md)
- **Entire radical compatible, Type II only:** collective-image quotients have dimensions 27<28, forcing generic original rank exactly 36, all original generic Bocksteins after the second zero, and internal cubic r=0. This does **not** exclude the hypothesis itself or prove all later internal symbols vanish. The secondary scalar ν remains unselected. PR995 now resolves internal orders four through seven, but not the octic scalar or all later internal orders. [Conditional theorem](paper/48-collective-radical-images.md)
- **Opposite bundle:** mr. slop reduces its necessary splitting types from 21 to nine to seven and identifies a canonical quotient C→O(2). The actual row and vertex scalar remain open. This seven-type list is not the four-pair source catalogue, and its top-polar σ is not the octic target section σ. [Scoped source report](paper/55-opposite-bundle-seven-types.md)
- **Collaborator geometry:** mr. slop determines the ninth hyperplane-neighborhood gate's constant rank as twelve and its square-dual image. Its image splitting and conditional secondary D-row geometry are now described. The secondary coefficients remain unselected; finite-neighborhood results are not global opposite-bundle or quadric-survival conclusions. These summaries are complete source readings, not independent reproofs. [Ninth gate](paper/49-ninth-neighborhood-rank.md) · [Image splitting and secondary row](paper/51-single-line-symbol-transfer.md#4-collaborator-source-report-square-quotient-and-ninth-gate-image)

## Fixed necessary frontier

| Source | Stable label | Retained catalogue pairs (E,Q*) |
|---|---|---|
| Source126 | G3.11.8ae96830fd21 | (10,129), (10,157) |
| Source127 c-d-f | G3.11.cce6e3ba4eeb | (14,148) |
| Source2 | G3.21.d610e381ed75 | (13,21) |

These indices identify pinned catalogue entries, not intrinsic bundle names. The count is **2+1+1**, with profiles **2/0/1**. It is neither a count of actual realizations nor a completion percentage, probability of success, difficulty estimate or measure of all possible proofs.

![Necessary relation at full baseline scale, with a separately labeled residual zoom](paper/figures/current-four-pair-frontier.svg)

The ledger changes have different meanings: source2's 78→1 corrects overdue propagation of older structure; c-d-f's 32→1 and source126's 4→2 are new quotient restrictions. Do not count the 77 corrected source2 entries as 77 new geometric discoveries. [Six-pair checkpoint](paper/35-six-pair-specialization.md) · [Four-pair specialization](paper/36-source126-dual-specialization.md)

## What remains unresolved

1. Select or exclude actual compatible sources and radical-line footprints. Necessary catalogues and abstract models do not certify realization.
2. Determine the unselected cubics in the applicable single-line rows and the conditionally preserved c-d-f block, and the separate full-J octic scalar. For the latter, find a different actual-complex relation: the secondary ν test is now proved identically ineffective. Neither reduction establishes actual occurrence; the full-J results cannot silently settle single-line rows.
3. Match the actual physical construction and its mixed multiplication constraints, then complete the required higher lifting/algebraicity argument. Conditional rank bounds are not a complete repair.

The last established broader section count is [four or five sections on a general smooth inversion-even quadric, with no odd sections](https://github.com/Akilleez-QA/read-em-and-weep/blob/72aa6fb732a803eb9201f45f1f82e60f54d296b4/research/hm/order-four-quadratic-load/POSITIVE-GENERIC-FOUR-OR-FIVE-SECTIONS.md). Specialized extra kernel classes at exceptional directions are not computed by the generic-symbol statements above.

## Evidence, history and provenance

Written results retain their pinned geometric premises. Exact Python tests support the arguments; they are not proof-assistant certification of the entire dependency chain. The burn produced 66 distinct checked supporting Lean declarations in 13 focused draft packages, not a formalization of the original theorem. A published draft PR is not a merge.

The burn ended at PR911 on **23 October 2026, 04:52:27 UTC (00:52:27 EDT)**. Its historical 146-pair endpoint and figures remain preserved. The proof-repair project remains open; this report does not restart the burn.

- [Full chronological root snapshot through PR993](paper/52-root-status-archive-through993.md), preserving all previous caveats and provenance
- [Burn assessment](paper/31-spike-burn-closeout.md) · [Execution and Lean evidence](paper/32-burn-execution-and-verification.md)
- [Physical construction dependencies](paper/33-burn-physical-construction.md) · [Campaign work gates](research/proof-repair-campaign/README.md)
- [Upstream OpenAI collection and original attribution](upstream/openai-math/README.md)

The readability reorganization itself is supporting documentation, not mathematical progress. The new mathematical results are separately pinned in chapters 53–60. The complete through-PR993 root snapshot and all historical figures are preserved.
