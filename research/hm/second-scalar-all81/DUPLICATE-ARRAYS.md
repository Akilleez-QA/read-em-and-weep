# Why equal role-relative arrays are not interchangeable physical contributions

Among the eighteen quotients used for m=(2,2,2,0), twelve coefficient arrays are distinct. The six equal pairs are:

- 0123 and 2301
- 0132 and 2310
- 0213 and 2031
- 0231 and 2013
- 0312 and 2130
- 0321 and 2103

Equality here means equality in role-relative quotient coordinates. The roles tell which physical variable is the leading axis, reversed axis, homogeneous reference axis and low-exponent axis. Swapping those physical assignments while retaining the same array need not preserve a fixed physical target monomial.

Each listed pair is related by the even physical permutation `sigma=(02)(13)`, represented by `[2,3,0,1]`. Under this permutation the target `m=(2,2,2,0)` becomes `(2,0,2,2)`. The total degree, role-specific bounds, kernel weights and orientation sign are preserved, while each physical exponent vector is permuted. The package checks all 1,086 corresponding rows, including coefficients and weighted contributions, directly from the supplied arrays.

For example, 0123 at m2220 contributes `8655/16`. Its equal-array partner 2301 at the transformed target m2022 also contributes `8655/16`. But 2301 at the unchanged target m2220 contributes `131/2`: a different selection is applied to the same role-relative array. Equality of arrays is therefore not a reason to identify or omit these oriented contributions.

## What the binding audit establishes

The historical receipt has SHA-256 `08c16deec98059a597301700bedc986a452038bb87ba04eef451453cc968b68b`. It checked separate role/configuration, normalized-source, compact-source, pair-gate and checkpoint bindings, and reconstructed each quotient from its own terminal factors using exact integer and rational arithmetic. It found no mistaken source/checkpoint reuse. The included receipt preserves the original mathematical bindings and historical conclusion without distributing the checkpoints.

The portable check verifies array equality, distinct recorded binding hashes and target/row covariance. It does not reconstruct those historical terminal products or prove that distinct hashes by themselves establish correct execution. That stronger historical check is separate evidence.

## What is not established

No symbolic identity proving source-level symmetry under sigma was established by this audit, and no source DAG nodes were reevaluated. Selector covariance explains why the observed equality is mathematically compatible with role permutations; it is not a proof that the underlying geometric source must have that symmetry. The full obstruction remains outside this scalar computation.
