# A finite index of the remaining rank-three quotient frontier

## What is counted

The six excluded maximal rank-three Gauss profiles leave only (1,1), (1,2), and (2,1). For each of these three profiles, the proved necessary quotient classifications now give a finite list. The common counting unit is

    (maximal profile, equivariant splitting type of A, equivariant splitting type of B).

There are **182 entries** in the resulting necessary frontier: 159 for (1,1), ten for (1,2), and thirteen for (2,1). Unlike nested source/endpoint records, these labels can be added: the maximal profile of an actual object is unique, and its two specified equivariant quotient splitting types are unique up to isomorphism. The lists are conservative. An entry need not have any realization, and a realized entry may contain infinitely many configurations.

This is a synthesis and reproducible indexing artifact, **not an additional exclusion theorem**. It does not establish a total number of configurations, all conceivable proof routes, remaining work, or a completion percentage. It is not an original historical denominator. Generic rank three itself remains open, and the separate original source, lifting and algebraicity obligations are not part of this count.

## Frozen sources

- (1,1): [159-pair endpoint-safe theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/4c147e95217f0900fa13f195662d95e933412c3c/research/hm/order-four-quadratic-load/ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md).
- (1,2): [ten-pair endpoint/orbit refinement](https://github.com/Akilleez-QA/read-em-and-weep/blob/857cd414252618a53a79ddce72982c6d91341db9/research/hm/order-four-quadratic-load/ONE-TWO-ENDPOINT-ORBIT-CONSTRAINTS.md), retaining the old IDs from the [initial 25-pair list](https://github.com/Akilleez-QA/read-em-and-weep/blob/c0b88ea01fa4e0ca57d8e289b236aece9258670b/research/hm/order-four-quadratic-load/ONE-TWO-FINITE-QUOTIENT-PAIRS-AND-ZERO-DEFECT.md).
- (2,1): [thirteen-pair primal-interior theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/f7071d29886c83151028576bf32e001c347cafc9/research/hm/order-four-quadratic-load/TWO-ONE-PRIMAL-INTERIOR-AND-ENDPOINT-QUOTIENT-CONSTRAINTS.md).
- The [complete (2,2) exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/c8975a41912b28938bc5b912e6637698a9652195/research/hm/order-four-quadratic-load/TWO-TWO-ENDPOINT-RANK-DROP-EXCLUDES-LAST-THREE-PAIRS.md) records the remaining three-profile frontier and its preceding exclusions.

The original transpose determinant length is always t=-6-deg(A)-deg(B). Across the 182 labels its distribution is 101 at t=0, 63 at t=12, five at t=20 and thirteen at t=24. This is the ORIGINAL determinant, not either second-interior determinant. In particular the latter may remain nonzero even where the original t is zero.

## Reproduction and stable identities

Run `python3 build_rank_three_quotient_frontier.py` beside the four pinned input JSON files. The program verifies their SHA-256 digests, constructs canonical sorted splitting labels, and emits `rank-three-quotient-frontier-182.json`. IDs include the maximal profile and a digest of its ordered quotient types, so future filtering can preserve identities without renumbering survivors.

The checks enforce rank three, central parity, determinant degree, permitted original defects, source pins, distinctness and all stated counts. Four corruption tests reject duplicated cases, inconsistent defects, wrong ranks and unknown profiles. They check data integrity, not the geometry proving necessity; that geometry remains in the frozen source theorems. No actual source coefficients, points, matrices or ranks are evaluated.

Source-type records and endpoint records are deliberately omitted from the aggregate. Their additional compatibility information remains in each source dataset and must not be added to the 182 quotient labels.
