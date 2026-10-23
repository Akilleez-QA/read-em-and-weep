# Through844: two split source edges, whole-label gate closed

The pinned PR844 bundle at `c86ed140ecd1371d2881727094f56230bdd04b85` excludes the bf and bc source strata on `G3.11.863639aa192e`. Exact full block-multiset and multiplicity-tuple matching removes **19 + 19 = 38** additional necessary pairs: **759 − 38 = 721**. Earlier rank-branch restrictions had not deleted either source edge, so none of these38 cuts is a duplicate.

There remain **8 registered labels, profiles7/0/1**. Seven have a nonempty recorded relation; the split label now has an empty relation but is deliberately retained in the registered set. No whole-label exclusion is recorded. A separately pinned complete original ten-source exhaustion must be checked before discharging that gate. This is not a realization count or a global proof-completion claim.

The predecessor `frontier-through842.json`, published in PR843 at `b23fdc1a66fde80d1bbf74f4fdee7ddefb7af772`, remains byte-identical, with759 pairs. All seven other label records remain identical. No historical checkpoint is overwritten.

## Exact sources and complete scope

The immutable original frontier and necessary-pair catalog at `db51525015bb7c5e825833d550d08dedf6f6ea96` identify source index69, original defect0, A=O(-10)+O(4)+O(6), B=O(-8)+O(-6)+O(8). Both tuples occur in the exact original list:

- bf=(0,1,0,0,0,1,0,1): (P+D) O(-2)+T O(-3)+O(-8)+O(-10).
- bc=(0,1,1,0,0,0,0,1): (V+P) O(-2)+T O(-3)+V O(-4)+O(-10).

For bf, strict-top excludes rank zero. Rank two is necessarily onto because nine independent sections force determinant defect at most7, below the positive invariant-divisor minimum12. PR814 Section5 excludes zero internal derivative; PR830 Sections1–4 exclude every nonzero internal combination, for the same split target. PR830 alone never excluded rank one. PR844's exact bf interface proves the rank-one complete O(6) top and actual quotient K1/K2=O(2)+O(4); the companion corollary checks that its twist is a genuine subbundle of the actual ambient quotient and preserves the derivative kernel and raw image. The split-specific descent then applies.

For bc, PR814 Section6 excludes rank two and strict-top excludes rank zero. PR844's bc proof covers rank one: complete direct O(4) top, lower T zero/nonzero, both nonzero top rows, only the O(2) row with P and scalar alternatives, and only the O(4) row with both sextic possibilities. It explicitly retains the f12 defective image and the relevant Ext degree−1. Every surviving branch reaches the same exact actual-connection interface.

The source-free descent retains initial rank one and defective rank two, all four K3 types, and the split-specific IV/d branch. Both terminal length12 defects use their raw quotient targets rather than saturated substitutes. The full bundle review binds all companion versions by SHA256; the separate bf-interface review is included. This ledger checks scope and finite bookkeeping against those written geometric inputs, not a new production proof or formal proof verification.

## Dependencies and reproduction

`source-pins-source-through844.json` pins all six PR844 files and PR830 at `620d5598ccc19e5e1c458a4cddb0d3a0709d83c3`. Existing predecessor dependencies supply the original source/frontier files, PR814 at `1f94be65b3a470a1b594e61d56df7f6057c9d907`, PR819 quartic input, and PR823 support/evaluation identities. Their immutable bytes are checked through the predecessor chain. PR823 balanced quotient conclusions are not transferred to the split target.

From the campaign directory:

    python verify_source_frontier_through844.py
    python -O verify_source_frontier_through844.py
    python -m unittest discover -p 'test*.py'

107 cumulative tests pass, including12 new tests. They check exact19+19 cuts, stable IDs, unaffected records, no double cuts, complete branches, source-block matching independent of local numbering, unchanged predecessor, and the closed gate.

Certificate SHA256: `914da79fc3b871448477fd9283643b8e1bc30ae9b45c5cbf5c31c3d75125c5ee`.

## Exact new publication file list

- `frontier-source-through844.json`
- `verify_source_frontier_through844.py`
- `test_source_frontier_through844.py`
- `source-pins-source-through844.json`
- `SOURCE-FRONTIER-THROUGH844.md`
- `inputs/pr830-proof.md`
- `inputs/pr844-SPLIT-BACKWARD-DESCENT.md`
- `inputs/pr844-SPLIT-BC-SOURCE-EXCLUSION.md`
- `inputs/pr844-SPLIT-BF-BACKWARD-INTERFACE.md`
- `inputs/pr844-SPLIT-BF-INTERFACE-REVIEW.md`
- `inputs/pr844-SPLIT-BF-SOURCE-COROLLARY.md`
- `inputs/pr844-SPLIT-DESCENT-BUNDLE-REVIEW.md`

These12 files are prepared locally, not published. Exclude generated Python caches. PR845 is deferred: its necessary O26 forms and length20 modification are not exclusions and cause no deletion here. No selected actual coefficients, points, matrices, derivative evaluations, or instance ranks are used. No Lean, Source2 closure, or global HM completion claim is made.
