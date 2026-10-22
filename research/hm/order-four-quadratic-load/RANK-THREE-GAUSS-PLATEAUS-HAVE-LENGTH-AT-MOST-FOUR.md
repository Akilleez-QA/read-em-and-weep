# Rank-three Gauss plateaus have length at most four

## New conclusion

For the actual equivariant inclusion E in H O considered in the pinned
Gauss arguments, any hypothetical generic rank-three maximal plateau
has backward and forward lengths k,l satisfying

    k+l <= 4.

In particular the entire adjacent profile (k,l)=(3,2) is impossible.
This is stronger than a reduction in the number of its formal splittings:
none of its twenty-eight necessary primal types survives. It is not an
exclusion of every rank-three plateau. The extremal profiles (3,1),
(2,2), and (1,3) are not excluded by this theorem.

The established generic SF rank bound remains three and the positive
square rank bound remains twenty-seven. No smoothing or complete repair
claim follows.

## 1. Exhaust the last adjacent profile

The exhaustive character recursion in
ADJACENT-RANK-THREE-GAUSS-EXCLUSION-AND-CONSTRAINTS.md gives twenty-eight
necessary primal splittings for (3,2). It is a necessary overlist, not
an assumption that any splitting is geometrically realized.

The frozen chain ending in
FOUR-MIXED-P4-D5-TYPES-EXCLUDED-BY-OCTIC-EVALUATION.md excludes twenty-three
of these types and leaves exactly the following five tuples:

    (0,1,1,0,0,0,0,1),
    (0,0,2,1,0,0,0,0),
    (1,0,2,0,1,0,0,0),
    (1,0,2,0,0,1,0,0),
    (1,2,1,0,0,0,0,0).

The first three, with quadratic section module V+P4, are excluded in
THREE-V-P4-TYPES-EXCLUDED-BY-BACKWARD-GAUSS.md. Both zero and nonzero
cubic-pairing branches are treated there; saturation is proved where
used, including the potentially high-line case.

The fourth, with quadratic section module V+D5, is excluded in
V-D5-TYPE-EXCLUDED-BY-BACKWARD-GAUSS.md. The parity-improved degree bound
on the quadratic kernel is essential to the split low-line quotient
and the final multiplicity contradiction.

The last, with no quadratic sections, is excluded in
ZERO-QUADRATIC-TYPE-EXCLUDED-BY-BACKWARD-GAUSS.md. Rank three of its cubic
image contradicts persistence; rank two forces three exact quotients.
Two fail representation multiplicities and the third fails the frozen
rank-one endpoint ramification obstruction.

These five exclusions are disjoint and exhaust the frozen remainder.
Consequently (3,2) itself is excluded. No assumption equating absence
of quadratic sections with a longer forward plateau is needed.

## 2. Bound the whole plateau length

The geometric persistence theorem in
ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md gives

    1 <= k,l <= 3.

EXCEPTIONAL-CUBIC-GAUSS-CORNER-EXCLUSION.md excludes (3,3), and
ADJACENT-RANK-THREE-GAUSS-EXCLUSION-AND-CONSTRAINTS.md excludes (2,3).
Section 1 excludes the remaining pair (3,2). These are exactly the
pairs in the stated range with k+l greater than four. The claimed
bound follows.

The six pairs not excluded by this combined argument are

    (1,1), (1,2), (1,3), (2,1), (2,2), (3,1).

This list is another necessary overlist, not a realization claim.
It keeps the distinction between eliminating one entire branch and
settling the full second-fundamental-form problem explicit.

## Reproduction

Run python3 verify_rank_three_plateau_length_four.py. It executes the
three new terminal exclusions and their unchanged frozen dependencies,
checks that their disjoint tuple sets exhaust the five-type remainder,
and checks the resulting length inequality. The mathematical image,
saturation, and persistence arguments are in the cited proofs.

Only universal representations, hypothetical bundle degrees, and finite
integer bookkeeping are used. No actual coefficient values, selected
actual points, source-instance matrices, rank experiments, or scans occur.
