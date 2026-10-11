# Original-cover certificate control

Pinned commit `6b69eefd57098d9a0c1d9f43ed993d36e1e54bcb`. Package directory `research/carrier/formal-five-parameter-chart/`. The original-cover checker under `audit_original_cover/` is imported and is not modified.

Arithmetic is exact over `Q`: the producer uses `fractions.Fraction`, and the control compares matrices of `sympy.Rational` entries. SymPy 1.14.0, Python 3.12. Replay commands are the four commands in `audit_original_cover/README.md`, run from the package directory.

The raw order-three lambda cochains are exact, so a zero image under the reducer is the correct value of those cochains. They are not used as a non-vacuity probe.

## 1. Replay and seven regression tests — PASS

| command | exit | result |
| --- | --- | --- |
| normal `--verify-certificate` | 0 | stdout matches the shipped replay log |
| `python -O --verify-certificate` | 0 | stdout matches the normal replay and the shipped optimized log |
| `unittest discover -s audit_original_cover -p 'test_*.py' -v` | 0 | 7 tests, all ok |
| `sha256sum -c SHA256SUMS` | 0 | 8 files ok |

Normal and optimized runs print the same 15 coefficient lines and the same five lambda lines, then both success lines. The seven tests are `test_c_d_raw_terms_not_silently_discarded`, `test_corrupted_preimage_detected`, `test_exact_all_fifteen_matrix_witnesses`, `test_lambda_inverse_and_each_matrix_witness`, `test_nonregular_primitive_rejected`, `test_wrong_character_rejected`, and `test_wrong_relation_rejected`.

Coefficient lines from the replay:

| coefficient | mixed BCH | relation | projected relation | obstruction nonzeros |
| --- | ---: | ---: | ---: | ---: |
| 1 | 995 | 232 | 39 | 10 |
| a | 906 | 194 | 26 | 12 |
| b | 898 | 185 | 26 | 7 |
| c | 84 | 10 | 2 | 0 |
| d | 84 | 10 | 2 | 0 |
| a*a | 425 | 73 | 7 | 4 |
| a*b | 535 | 107 | 12 | 0 |
| a*c | 43 | 3 | 0 | 0 |
| a*d | 43 | 3 | 0 | 0 |
| b*b | 389 | 71 | 6 | 4 |
| b*c | 41 | 3 | 0 | 0 |
| b*d | 41 | 3 | 0 | 0 |
| c*c | 0 | 0 | 0 | 0 |
| c*d | 0 | 0 | 0 | 0 |
| d*d | 0 | 0 | 0 | 0 |

Lambda preimages, each a length-9 vector over `Q`: `1` has 248 graded terms and preimage `0`; `a` has 100 and preimage `0`; `b` has 94 and preimage `0`; `c` and `d` have 0 graded terms and preimage `0`.

## 2. Rebuilt D3 block — PASS

The control reruns `project(alpha * lifted source)`, then `reduce_target`, then the producer's row extraction, on all nine prescribed-character source columns. The resulting matrix equals `producer.rebuilt_block` on `data/order_3.json` and equals `lambda_order_three.D3_hom` in the pinned certificate entrywise.

| check | value |
| --- | --- |
| shape | 9×9 |
| determinant over `Q` | 1 |
| certificate match | entrywise |
| singular | no |

Negative control: a reducer that returns the empty coordinate dict on every input produces the 9×9 zero matrix, determinant 0. The invertibility check raises `rebuilt D3 is singular`. Calling `producer.rebuilt_block` with that reducer installed raises `Geometrically regenerated D3 block differs from supplied entries.`

## 3. Basis lists — recorded input, completeness not established

`rebuilt_block` reads the supplied source and target label lists. A source label `[ch, b, [p0, p1, p2]]` has relative character `2b - p0 - p1 - 2 - d_ch`. A target label `[[i, j], b, [p0, p1, p2]]` has relative character `2b + p0 + p1 - d_i - d_j`, with `d = (3, 0, 2, 2)`. Order `k` keeps character `k - 4`. At order 3 the index sets from this count are exactly the column and row sets returned by `rebuilt_block`. The order-2 counts use those same formulas on `data/order_2.json`.

These multiplicities are counts of labels present in the files. They do not show that the lists are the full geometric character spaces.

| character | D2 source | D2 target | D3 source | D3 target |
| ---: | ---: | ---: | ---: | ---: |
| -12 | 0 | 0 | 26 | 38 |
| -11 | 23 | 32 | 23 | 32 |
| -10 | 20 | 26 | 46 | 64 |
| -9 | 40 | 52 | 40 | 52 |
| -8 | 34 | 40 | 60 | 78 |
| -7 | 51 | 60 | 51 | 60 |
| -6 | 42 | 43 | 51 | 66 |
| -5 | 41 | 47 | 41 | 47 |
| -4 | 31 | 32 | 31 | 39 |
| -3 | 22 | 25 | 22 | 25 |
| -2 | 15 | 16 | 15 | 16 |
| -1 | 9 | 9 | 9 | 9 |
| 0 | 5 | 5 | 5 | 5 |
| 1 | 2 | 2 | 2 | 2 |
| 2 | 1 | 1 | 1 | 1 |
| list size | 336 | 390 | 423 | 534 |

The order-2 block uses character `-2`: 15 source columns and 16 target rows. The order-3 block uses character `-1`: 9 source columns and 9 target rows. The target lookup is built from the full target list; the extracted vector keeps only those rows.

## Reproduce

From the package directory, the four README commands above. From the repository root:

```sh
python research/hsd-review-61/original_cover_control.py
python -m unittest discover -s research/hsd-review-61/tests -p 'test_original_cover_control.py' -v
```

The control script exits 0 only when the rebuilt block has nonzero determinant, matches the certificate, and the zero reducer fails that check. The three unit tests cover the same statements and the multiplicity table.
