# Narrow source-stratum checkpoint through PR823

## Exact accounting result

This is a new source-edge integration, not a new proof or a full current-publication frontier. It preserves all nine labels in `frontier-through806.json`, with profile counts **8/0/1**, and restricts its 1,004 historical paired witnesses to **980 necessary pairs**.

Exactly 24 additional pairs are removed:

- `G3.11.8ae96830fd21`: four E0 pairs and four E18 pairs are removed. Four E10 pairs remain. Its only surviving source type is `(P+2D) O(-2)+O(-8)+W O(-9)`, not an asserted realization.
- `G3.11.73682b4c817f`: sixteen bf pairs are removed, leaving 96 pairs from the previous 112. The full balanced label is not excluded.

All three targeted source edges were present in the pinned prior relation. Thus none of these 24 deletions duplicates an earlier removal. The already-known ten-to-seven low-positive source pruning is not counted again. The other seven labels and every retained pair on them are unchanged.

## Why each source deletion is unconditional within its label

For `G3.11.8ae96830fd21`, PR813 pins the complete source overlist E0/E10/E18 and divisor alternatives 0,12,20. Its theorem excludes divisor12 for all sources and divisor20 for this label. PR817 Section6 excludes E0 in the remaining basepoint-free case; PR822 excludes E18 there. Therefore only E10 remains across all divisor strata.

For balanced bf, **PR823 alone is not a complete source exclusion**. Its proof and review explicitly concern nonzero internal J. Complete coverage requires:

1. PR814 Section2 (also PR819 Section1): the top rank-nine P+D system has rank two and is onto.
2. PR814 Sections3/5: J is either zero or O(-10), and J=0 is impossible in that rank-two case.
3. PR819: nonzero J forces the actual quartic subsystem.
4. PR823's third-backward quotient and finite descent: that nonzero-J case is impossible.

The immutable zero-J input is PR814 at `1f94be65b3a470a1b594e61d56df7f6057c9d907`; the subsystem is PR819 at `03fee9278072f9ac00a5fcee5deb04b7fce61ae5`. The PR823 reviewed proof files and reviews are included to preserve the precise conditional scope and exact-version review evidence. Their text is not silently rewritten to appear unconditional.

## Reproduce

```sh
python verify_source_frontier_through823.py
python -m unittest test_frontier test_frontier_through804 test_frontier_through806 test_source_frontier_through823
```

The 44 cumulative tests pass, including 13 new tests. Optimized Python replay also passes. Use `python verify_source_frontier_through823.py --write` to regenerate only the new artifact, `frontier-source-through823.json`. Previous snapshots remain unchanged and their hashes are checked through the verifier chain.

The package is self-contained using its included inputs and earlier verifiers. It requires no network or third-party packages. The source-pin manifest is SHA256-pinned, and every included new source file is checked against its immutable Git blob. `source-pins-source-through823.json` contains public commit/path URLs, including PR813, PR814, PR817, PR819, PR821, PR822 and PR823.

Source matching uses both complete degree/irreducible multisets (including repeated blocks) and source multiplicity tuples. Local E catalog IDs are references only. Reindexing and block ordering do not change the result. Existing correlated pairs are filtered directly; no Cartesian product is constructed. A regression test confirms that already absent target edges contribute zero additional deletions.

## Explicitly unencoded results

The JSON retains an unencoded/deferred ledger. In particular:

- Other O26 divisor conditions from PR813 and basepoint-free-only corollaries from PR817 do not authorize deleting those entire source edges.
- PR814's bc rank-two obstruction does not eliminate its rank-one branch. Forced cf and split-ce constant systems are not exclusions.
- PR819's balanced bb cubic subsystem assumes a rank-two non-onto top. PR821 classifies the onto bb constant spans and excludes split bb torsion, without excluding the whole bb source. Neither is broadly deleted here.
- PR814 also contains genuine complete ef/be source exclusions in both low-positive labels and balanced ce. These are **explicitly deferred**, not claimed conditional and not integrated in this narrow requested checkpoint. Thus 980 is not advertised as the fully integrated frontier after all public source theorems.

All geometric theorems are written-input assumptions. This finite verifier does not reproduce proof review, run old enumeration experiments, evaluate actual-source matrices/coefficients/points, infer realizability, or prove SF>=4, higher lifting, algebraicity or the global research goal.

Artifact SHA256: `54068156ebad88ac4dce3b4c03ce7e7c3ad7e0ec1d5940c6ff001f8d48fcc47c`.
