# Review of the five-parameter formal chart

Reviewed package commit `ca9226569ddb5ed29d2809f1f4e4e1ae7c646ea8` (draft PR #61), directory `research/carrier/formal-five-parameter-chart/`. This branch adds `review.py`, `tests/test_replay_status.py`, and this note. The package tree is unchanged.

`review.py` uses exact rational arithmetic (`fractions.Fraction`, a Hadamard bound plus the Chinese remainder theorem for determinants, and SymPy polynomials). It does not import the package checkers. Matrix inputs are the JSON files in `data/`. Certificate files are used only as the supplied witness.

## 1. Package replay and regression tests — PASS

`python replay.py` exited 0. It verified 21 package files and regenerated all four certificates with an exact match. `python -m unittest discover -s tests -v` ran 9 tests, all ok:

- `test_complete_late_relation_columns`
- `test_constant_higher_right_inverses`
- `test_four_plus_one_coordinates`
- `test_integrity`
- `test_integrity_rejects_tampering`
- `test_regenerated_outputs`
- `test_section_units_are_rational_units`
- `test_symbolic_quadratic_preimage`
- `test_uniform_all_order_bounds`

This step executes the package. It is not an independent derivation.

`review.py --replay` records `replay_exit` and `tests_exit`. A nonzero status on either stage makes the command exit nonzero and prints `replay stage failed` or `tests stage failed`.

## 2. Inverses of D3..D6 — PASS

Homogeneous blocks were cut out of `data/order_3.json` through `data/order_6.json` by the character weight `k-4`. Every nonzero entry of each full `D` map is weight-homogeneous. Gauss–Jordan over `Q` produced a two-sided inverse.

| block | shape | det | `D R = I` and `R D = I` | inverse denominators | parameter symbols |
| --- | --- | --- | --- | --- | --- |
| D3 | 9×9 | 1 | yes | {1} | none |
| D4 | 5×5 | 1 | yes | {1} | none |
| D5 | 2×2 | 1 | yes | {1} | none |
| D6 | 1×1 | 1 | yes | {1} | none |

Blocks, index sets, and inverses match `certificates/higher_certificate.json` entrywise. No discrepancy.

For orders 5 and 6 the row coordinates are the free columns of `C`. Recomputed pivots are `[336, 338, 340]` and `[423, 424, 425, 426, 427, 428, 429, 431, 433]`, matching the files. The weight-selected raw columns are `[532, 540]` and `[664]`.

Entries lie in `Z`. The identity is an equality of constant matrices, so it remains true after base change to `Q[a,b,c,d,lambda]`. There is no parameter denominator.

## 3. Maximal minors of N2..N4 — PASS

The ordered maximal minors stored in the data files were recomputed. Entries are integers (denominator 1) with no parameter symbols, so each determinant is a constant in `Z`.

| minor | ambient shape | minor | determinant | factorization | denominator |
| --- | --- | --- | --- | --- | --- |
| N2 | 114×84 | 84×84 | 16 | 2^4 | 1 |
| N3 | 176×112 | 112×112 | −512 | −2^9 | 1 |
| N4 | 252×144 | 144×144 | −16384 | −2^14 | 1 |

The only prime is 2. N2's file stores the value only modulo 65521, and that residue is 16, which matches. N3 and N4's stored exact determinants match. No discrepancy.

## 4. Order-two scalar and preimage — PASS

`D2` from `data/order_2.json` is 16×15, column rank 15, and agrees with the certificate matrix. Its left kernel is one-dimensional. The primitive generator is

`(0,0,0,0,0,0,0,0,1,0,0,0,0,-1,0,1)`,

the same as `left_cokernel_detector`. It annihilates every column.

The supplied obstruction uses only `a` and `b` (total degree at most 2; the last component is 0). The scalar pairing of that witness is the zero polynomial in `a` and `b`. The same holds for the certificate detector.

`lambda` is the order-2 lift choice (`delta kappa_2 = 0`), first enters at order 3 (`lambda^2` at order 4), so order-two `lambda` cross terms are absent by normal degree. Viewing the shipped quadratic in `Q[a,b,c,d,lambda]` is scalar extension, not a test.

The supplied preimage was recomputed from a rank-15 minor of this constant matrix and matches the certificate entrywise. Both satisfy `D2 y = obstruction` with residual the zero vector. No discrepancy.

The obstruction polynomial itself is the shipped witness. This check does not rebuild the bracket, relation division, or Čech cochain. Coefficients of `c` and `d` are zero in that witness; the review does not reconstruct them. The `a,b` scalar cancels.

## 5. Order ≥ 7 weight bound — PASS

Cutoffs are derived from the fixed bidegrees `(P,E0,E1,E2) = (3,-3), (0,0), (4,-4), (3,-4)`, frame weights `(3,0,2,2)`, and `L^{-1} = O(-4,2)`. A line of base degree `b < 0` has no `H^2`. For `b ≥ 0` the secondary weight is at most `2b-2`, and the required weight at order `k` is `k-4` plus the frame weight, so the line can contribute only for `k` at most the cutoff below.

W cutoffs: `P^2: 0`, `PE0: none` (base −1), `PE1: 3`, `PE2: 1`, `E0^2: none` (base −4), `E0E1: 0`, `E0E2: none` (base −1), `E1^2: 6`, `E1E2: 4`, `E2^2: 2`.

U cutoffs: `AP: 3`, `AE0: none` (base −1), `AE1: 6`, `AE2: 4`.

The largest finite cutoff is 6. At order 7 the required weight is strictly larger than the maximum on every line (the tight cases are `E1^2`, maximum 6 against required 7, and `AE1`, maximum 4 against required 5). The same strict gap holds for every larger order. No step uses `a,b,c,d,lambda`. The derived table matches `certificates/weight_certificate.json`. No discrepancy.

The same weight lemma gives maximum weight `2·3-2 = 4` on the section line of base degree 3, so that line is empty for order ≥ 5. That is a companion of the order-7 bound, not a substitute for it.

## 6. Scope

Independent recomputation from the supplied coefficient maps: the homogeneous blocks and their inverses, the `C5`/`C6` pivots, the three section minors, the `D2 y = obstruction` identity, and the weight inequalities.

Replay only, not redone here:

- `replay.py` and the nine unit tests.
- Assembly of the order-two obstruction cocycle. Section 4 checks the shipped polynomial witness against `D2`.
- The omitted ancestor plane model: the rank-five symplectic presentation, earlier transition matrices, and any carrier or hull. The note treats those as inputs. Nothing in this review reconstructs them.

No numerical discrepancy with the shipped witnesses was found.
