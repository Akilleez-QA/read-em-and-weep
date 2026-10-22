# The fixed quotient frontier: 182 labels, 34 excluded, 148 remaining

Keep the [frozen 182-case index](https://github.com/Akilleez-QA/read-em-and-weep/blob/9b85030822b86ce6a304dd6fd886107404c8c5d7/research/hm/order-four-quadratic-load/RANK-THREE-QUOTIENT-FRONTIER-182-CASES.md) unchanged. The unit is a maximal-profile-labelled ordered pair of equivariant quotient splitting types, not a configuration, source-record witness or proof task.

Two subsequent checked necessary constraints exclude 34 labels:

| Maximal profile | Frozen baseline | Newly excluded | Not excluded |
|---|---:|---:|---:|
| (1,1) | 159 | 33 | 126 |
| (1,2) | 10 | 0 | 10 |
| (2,1) | 13 | 1 | 12 |
| Total in this unit only | 182 | 34 | 148 |

The [unrestricted dual-source theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/0b55b84466c62c24f05f7e691f3e7a3d528b7ebf/research/hm/order-four-quadratic-load/UNRESTRICTED-DUAL-SPLITTINGS-AND-SAME-SOURCE-PAIR-CONSTRAINTS.md) proves the complete 260-type necessary Q* list, retaining degree-minus-one summands. Requiring one dual type to satisfy every applicable quotient, transpose and endpoint condition excludes 33 of the 159 shortest-profile pairs. It leaves all ten (1,2) pairs.

The [rank-eleven endpoint theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/0b55b84466c62c24f05f7e691f3e7a3d528b7ebf/research/hm/order-four-quadratic-load/TWO-ONE-RANK-ELEVEN-ENDPOINT-SPLITTINGS.md) excludes the entire (2,1) pair A=O(-10)+2O(6), B=2O(-8)+O(8). It does not assume the endpoint derivative has rank three.

The remaining original-determinant distribution is 80 at length zero, 53 at twelve, two at twenty and thirteen at twenty-four. These lengths must not be confused with the separate second-interior defects. The stricter second-defect and endpoint data remain in the source records and are not additional labels in this total.

`verify_rank_three_frontier_pruning.py` reads strictly hashed baseline and refinement data, checks source-index correspondence and the actual ordered splitting labels where supplied, and writes `rank-three-quotient-frontier-148.json`. Every baseline ID remains present with status `excluded` or `not_excluded`. It verifies all counts and requires nonempty dual-source witness lists for retained dual-filter cases. It never regenerates or renumbers the baseline.

This is an audited synthesis of the two exclusion theorems and a data-integrity artifact, not another exclusion argument. The scoped reduction is 34 of the fixed 182 labels; that fraction is not a proof-completion percentage or a measure of geometric volume. The baseline begins at its stated snapshot, not at the beginning of the project. All three maximal profiles, the original repair, and actual realization of the surviving necessary labels remain open.
