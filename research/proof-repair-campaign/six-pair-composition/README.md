# Exact six-pair composition

This is a new reproducible integration certificate, not a new geometric exclusion theorem. The pinned historical frontier has 114 necessary catalogue pairs. The existing source2 structural specialization removes 77 pairs; the c-d-f quotient corollary removes 31 different pairs. Their label-scoped cuts are disjoint. Six necessary pairs survive, distributed 4+1+1 over the same three stable labels (profile counts 2/0/1).

Run with Python standard library only:

    python verify.py
    python test_verify.py
    python -O verify.py
    python -O test_verify.py

`frontier.json` is checked against its replay rather than trusted. The four immutable input snapshots are preserved in `inputs/`, authenticated against SHA256 pins. `verify.py --write` regenerates only the new frontier, never its predecessors. E catalogue IDs and Q catalogue indices are matched by exact bundle multisets and coefficient tuple; the tests transport all references through a nontrivial catalogue reindexing. Duplicate, missing, mis-scoped, wrongly oriented, and double-applied cuts are rejected. Reordering bundle blocks preserves identities; multiplicity is not discarded.

## Exact accounting argument

Let B be the set of labelled pairs in the pinned 114-pair checkpoint, A the 37-pair source2 result, and D the 31 c-d-f pairs in the targeted filter. The verifier establishes A ⊆ B, |B\A|=77, every pair of B\A has label G3.21.d610e381ed75, D ⊆ A, and every pair of D has distinct label G3.11.cce6e3ba4eeb. Thus B is the disjoint union of B\A, D, and A\D. The last set has six members. Four source126 pairs are unchanged, and each of the other two labels retains precisely its forced semantic pair. No full stable label is excluded.

## Sources and limits

- Historical frontier: commit e1fdea58bed32ec552b003dbfb097e60d410f1f7, research/proof-repair-campaign/frontier-source-through917.json.
- Source2: PR937, commit359475bea8dced5a6b12cc008f18bd81588fce41, research/hm/source2-bundle-specialization/specialization.json. Its 77-pair change propagates existing structural theorems into an overinclusive historical ledger; it is not 77 newly discovered geometric exclusions.
- C-d-f: targeted quotient certificate derives from the normal form at commit1528ff8ea56b21e03f7501a962bdaa6728a75904, research/hm/profile11-source127-cdf-normal-form/PROOF.md. The exact targeted-filter.json is included and hash pinned. Published as PR939 at commit9c43c9b3bb9cb99c809c37a8fe8f8429f4b3a79e, research/hm/cdf-quotient-specialization/targeted-filter.json.

Both prerequisite checkers were separately replayed normally and with Python optimization: source2 has 21 tests; c-d-f has 351 checks and 10 negative controls. The integration has 18 tests in each mode. This certificate composes those mathematical prerequisites; it does not independently establish them from Python arithmetic alone.

No actual-instance evaluation, actual realization, horizontal splitting, complete proof repair, or percentage of remaining mathematical work is asserted. Six counts necessary catalogue pairs, not six equally difficult geometric cases or a finite measure of all possible proofs.
