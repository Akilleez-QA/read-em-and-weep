# Homotopy changes and literal compensation

Changing a homotopy while fixing the differentiated kernel requires a paired connection change. The complete correction is invariant modulo genuine regular boundaries. Projected compensation exists exactly when the relative cochain is closed; actual auxiliary-homotopy compensation requires the stronger closed-cochain image condition, not merely equality in relative cohomology.

Read [HOMOTOPY-CHOICE.md](HOMOTOPY-CHOICE.md) before [COMPENSATION-LIFTING.md](COMPENSATION-LIFTING.md). The latter preserves the prescribed-compensation obstruction and three finite counterexamples.

## Precise dependencies

- [Complete remainder normal form](https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-complete-remainder-normal-form/RESULT.md), especially §§2 and 5, at PR #79 commit `4659e4425c6b5ab6b1899e6af93656ac03ff0862`. Its fixed complexes, chain maps, regular domains and differentiated identities remain premises.
- [Existing normal-form review](https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-complete-remainder-normal-form/REVIEW.md).
- [Additional historical boundary/sign audit](DEPENDENCY-REVIEW.md), retained with its original [formal control](dependency_formal_control.py). This is a review of the input normal form, not a separate independent review of these new compensation theorems.

## Review and saved checks

No distinct independent review of the two new results is available in this packet; review is pending. The historical dependency audit and all its domain qualifications are preserved. [test_synthetic.py](test_synthetic.py) and [TEST_OUTPUT.txt](TEST_OUTPUT.txt) are the original exact-rational synthetic checks and saved output. The audit reports its original normal/optimized checks; those are historical claims, not newly executed checks. No test was rerun for publication.

## Open boundary

Literal geometric realization, common regular domains, and closure when asserting a cohomology class remain separate requirements. Erasing the displayed defect can transfer its contribution into the connection term. No physical detector value, cancellation or new vanishing follows.
