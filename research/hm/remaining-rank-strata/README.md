# Remaining actual Gauss-rank strata

Conditional on the actual-geometric inputs and the generic lower bound
`r >= 4`, maximal plateau ranks and actual cubic persistence place every
configuration into 28 necessary ordered `(r,k,l)` bins. There are 27 bad
labels with `4 <= r <= 12`, and one rank-13 label `(13,1,1)` where the
positive square map is generically surjective, if attained.

The actual-source refinement has 99 bad labels and four rank-13 labels,
103 in all. These are necessary containers, not realized configurations,
not all branches of the original repair, and not a completion denominator.

Read `PROOF.md` for the complete frozen conditional theorem. `INPUTS.json`
authenticates the four complete immutable source originals in `inputs/`.
`PUBLICATION.md` pins the separately reviewed conditional lower-bound
theorem and explains the exact publication scope. `independent/REVIEW.md`
contains the independent mathematical review and its scope limits.

## Reproduce

From this directory, with standard-library Python:

    python3 verify.py > normal.json
    python3 -O verify.py > optimized.json
    cmp normal.json RESULT.json
    cmp optimized.json RESULT.json
    python3 independent/independent_check.py > independent-normal.json
    python3 -O independent/independent_check.py > independent-optimized.json
    cmp independent-normal.json independent/RESULT.json
    cmp independent-optimized.json independent/RESULT.json
    sha256sum -c SHA256SUMS

Both scripts also work when invoked from another working directory.
These checks evaluate universal integer representation arithmetic and
bounded abstract rank budgets only, not actual coefficients, parameters,
jets, matrices, ranks, or historical enumerations. Geometric premises
remain premises; this is not proof-assistant verification.
