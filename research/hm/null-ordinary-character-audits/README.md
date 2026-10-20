# Ordinary formal deformation and conditional character audits

## Statement and scope

These existing October 19 audits check two distinct published arguments: ordinary formal deformation hulls (87 variables, or 83 with determinant identification) and the second-order full-sign character projection. The latter also records a conditional formal parity selection rule and synthetic counterexamples to higher-order ambient-choice independence. Neither audit proves an all-order module extension or computes an actual obstruction value.

## Exact imported sources

- PR17 ordinary hull statement: commit `55a89833a46c2b16d06e1123f8b35b82b6edaf51`, https://github.com/Akilleez-QA/read-em-and-weep/pull/17 .
- PR3 genuine family: commit `86251374e9c62528b9b9dbb35ef883bdfac30ad8`, https://github.com/Akilleez-QA/read-em-and-weep/pull/3 . Its cited Ext dimension input remains imported, not recomputed.
- PR4 order-two reduction: https://github.com/Akilleez-QA/read-em-and-weep/blob/fa9be3c2d90ffce8d864bf927ecf3d7cd8dd5de5/research/hm-order-two-reduction.md .

## Contents and review status

- `ordinary/REVIEW.md`: existing independent audit, finding no correction to PR17 and spelling out compatible hull maps and stabilizers.
- `characters/review.md`: existing bounded review, including the distinction between intrinsic quadratic support and arbitrary ambient acceleration.
- `characters/check.py`, `check-result.json`, and `check-output.txt`: preserved synthetic checker and saved passing receipts. No tests were rerun for this publication. The finite checks do not certify the imported Ext dimensions.

## Unresolved boundary

Actual obstruction values, higher-order equivariant ambient/module existence, and higher-choice independence are not established. Ordinary unobstructedness concerns a fixed variety and its sheaves; it does not imply ambient-category unobstructedness, global coarse-moduli claims, or vanishing of Ext².
