# Exact determinant parity correction

This correction addresses [the independent review comment](https://github.com/Akilleez-QA/read-em-and-weep/pull/1132#issuecomment-6374496840) on PR1132 at cb9e9b4f8abda70e6d43b9f9ac319afe1fa60004.

The previous six-by-six Leibniz expansion counted inversions only with second index below three. This gave incorrect signs on general inputs. The replacement `exact_determinant` consistently uses the matrix dimension and rejects nonsquare inputs. It is a small-matrix exact-number helper, not an efficient large-matrix algorithm.

The historical sole input was minus the six-dimensional identity. All nonidentity permutation products vanish there, so its determinant remains +1. The original 51-check output is unchanged byte for byte. The type IV conditional Euler nonsplitting result is not retracted or strengthened; no type is selected or excluded and no Gauss, Q, or full source compatibility is inferred. The original REVIEW.md remains the historical hash-bound review of the original bytes; CORRECTION-REVIEW.md covers this correction.

## Reproduce

From this directory run `python test_determinant.py` and `python -O test_determinant.py`, comparing both outputs with DETERMINANT-RESULT.json. Run `python check_euler_overlap.py` and its optimized counterpart and compare with REVIEW-RESULT.json.

The new regression suite has 746 explicit runtime checks (not disabled by optimization). It checks every one of the 720 six-dimensional permutation matrices against independent exact rational row elimination. A literal implementation of the old defect disagrees on 360. The matrix interchanging zero-based coordinates 3 and 4 is a concrete witness: true determinant -1, old result +1. Additional controls cover exact integer and rational matrices in dimensions zero through six, singular cases, the historical minus identity, and nonsquare rejection. All inputs are synthetic, not geometric instance data. These are reproducible code regressions, not a new geometric theorem.
