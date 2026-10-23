# Independent review of the determinant correction

Review date: 2026-10-23 UTC. Verdict: **PASS for the bounded code correction and synthetic regression artifact.**

The publication target is `research/hm/type-four-radical-filtration/independent/`. The target's existing `REVIEW.md` and `REVIEW-RESULT.json` remain historical records. This review covers the corrected checker, the new determinant tests and result, and `DETERMINANT-CORRECTION.md`; it does not retroactively change the historical review's hash binding. The supplied historical checker was compared directly with the corrected checker. Remote publication state and the linked comment were not independently fetched in this review.

## Findings

1. The historical sign loop omitted every inversion whose second index was at least three. The replacement uses `n = len(matrix)` consistently in permutation generation, inversion counting, and the product, and rejects nonsquare matrices. This is the standard Leibniz formula for a small square matrix over exact scalars. The empty matrix correctly returns one. Factorial cost remains intentional and documented.
2. The oracle in `test_determinant.py` uses exact `Fraction` row elimination, independently of permutation inversion counting. Its pivot swaps change the sign, row replacements preserve the determinant, and the product of pivots gives the determinant. This provides a structurally distinct oracle.
3. All 720 six-dimensional permutation matrices agree with that oracle. These matrices individually isolate each permutation-product coefficient, making them particularly suitable for this sign defect. The old implementation disagrees on exactly 360 of them in the recorded execution. A transposition of zero-based coordinates 3 and 4 gives the reported concrete witness: corrected determinant -1, historical formula +1.
4. The 746 explicit runtime checks comprise 720 permutation comparisons, one old-implementation rejection check, one explicit transposition witness, one historical-input preservation check, 21 additional exact cases in dimensions zero through six, and two nonsquare-input rejections. The additional cases include singular matrices and rational entries. No check relies on an `assert` that optimization could remove. The test requires at least one old-implementation mismatch rather than hard-coding 360; the independently reproduced result artifact records the exact observed count.
5. Beyond reading the embedded negative control, this reviewer actually mutated a temporary copy of the final checker: its unique `for j in range(i+1,n)` was replaced by `for j in range(i+1,3)`. The unchanged regression suite rejected that mutant in both normal and optimized execution, with exit code 1 and `RuntimeError: permutation (0, 1, 2, 3, 5, 4)`. The reviewed checker and test files were not modified by this mutation experiment.
6. The original sole determinant input is minus the six-dimensional identity. Only the identity permutation has a nonzero product, and its product is +1. The historical defect therefore does not invalidate that determinant value. Normal and optimized runs of both the historical and final checker produce exactly the same 51-check output, byte for byte, as the retained `REVIEW-RESULT.json`.
7. The accompanying correction note accurately limits the claim. The final comment's description of minus identity on two copies of V is a clarification, not a new mathematical conclusion. This correction does not advance the geometry, select or exclude a type, establish source compatibility, or retract the previous conditional Euler nonsplitting result. All new test inputs are synthetic; no geometric instance or actualHM/source data were evaluated. The broader mathematical result was not independently re-proved in this code review.

## Executed verification

Python 3.12.14 was used. The final checker and regression suite were each run normally and with `-O`; all four runs exited 0. The historical checker was likewise run in both modes and exited 0. The checker outputs all matched the retained 51-check baseline exactly. Both regression outputs matched `DETERMINANT-RESULT.json` exactly: PASS, 746 checks, 720 permutation matrices, 360 old-formula mismatches, and historical determinant +1. Both actual-mutant runs failed as specified above. Input hashes were rechecked after execution to detect intervening changes.

To reproduce the positive checks from the repository root:

```sh
cd research/hm/type-four-radical-filtration/independent
python check_euler_overlap.py > /tmp/euler-check-normal.json
python -O check_euler_overlap.py > /tmp/euler-check-optimized.json
cmp REVIEW-RESULT.json /tmp/euler-check-normal.json
cmp REVIEW-RESULT.json /tmp/euler-check-optimized.json
python test_determinant.py > /tmp/determinant-normal.json
python -O test_determinant.py > /tmp/determinant-optimized.json
cmp DETERMINANT-RESULT.json /tmp/determinant-normal.json
cmp DETERMINANT-RESULT.json /tmp/determinant-optimized.json
```

For the actual-mutant control, copy the corrected checker and unchanged test into a fresh temporary directory, make only the unique sign-loop replacement described in finding 5, and run that temporary test normally and with `-O`. Both must fail. Do not modify the reviewed originals.

## SHA-256 binding

Paths below are relative to the publication target. The historical checker digest identifies the supplied pre-correction bytes, not an additional file to publish.

| Artifact | SHA-256 |
| --- | --- |
| Corrected `check_euler_overlap.py` | `241fb2cb77a8f73b0eb2bbd874b4a3e35f37a6622443f765dc99451d6a89f7ce` |
| `test_determinant.py` | `1d36d132d21021d2669b1b4aea0bbd4d62f42259cc63d47ea52619442acebd72` |
| `DETERMINANT-RESULT.json` | `361e67fccdf53e197e41c9f9e0ec7e79451dfedd74b20561e4695e4065b886b2` |
| `DETERMINANT-CORRECTION.md` | `92effefc8e53ac78a2aac987b390098545df6d11e9390f1e2eaa55e0f3fcc3e5` |
| Retained `REVIEW-RESULT.json` | `e69a11cde9128e9d1f70d78e0d3fd8f8d3abc638d0e4482aa498d82bc3bfafc8` |
| Historical `check_euler_overlap.py` | `7ebcdbb05fc96c30d19ead73be921297f64373227319f79d854b0bf20ee72748` |

The corrected checker and tests are approved only at these bytes. No unrelated repository files or external service state were changed by this review.
