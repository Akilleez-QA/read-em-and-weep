# Through842: one complete label exclusion, no repeated pair cuts

PR842 at `101a101234f3464f5d07a15669e4805cc46de3a7` discharges the separate whole-label gate for `G3.11.73682b4c817f` only. The registered frontier is now **8 labels = 7/0/1**. The necessary source relation remains **759 pairs**: all balanced pairs had already been removed in earlier source checkpoints, so this label operation removes **zero additional pairs**. The unchanged through839 record still has nine registered labels and a closed gate. These are distinct historical records, not contradictory counts.

## Independent finite coverage check

The original frontier at `db51525015bb7c5e825833d550d08dedf6f6ea96` identifies the unique stable ID, original defect zero and source index72. Its full A/B multisets agree with the original necessary-pair entry. The verifier compares the proof's ordered ten tuples with that complete original array, independently decodes their full source blocks, matches both blocks and tuples to the source catalog, and checks universal rank17/degree−54. The extra P block contributed by each e is retained.

The exact original order is ff, ef, ee, cf, ce, cc, bf, be, bc, bb. The original splitting theorem Sections2–3 and endpoint necessary-list theorem Section5 supply necessary-list completeness, not realizability. The three old strict-top prunings ff/ee/cc remain in the exhaustion and are not counted as new cuts.

Branch coverage is explicit: ef/ce/be use PR814 after the line bound and invariant-divisor minimum force onto rank two; cf additionally uses PR828. bf splits zero internal derivative (PR814) from all nonzero internal channels (PR819 and PR823). bc splits rank two (PR814) from rank one (PR839), including zero/nonzero lower T and the defective scalar-image alternatives. bb splits rank one (PR814 rank-one theorem), onto rank two with both constant-span alternatives (PR836/821), and the only nononto possibility, defect twelve (PR819/838). Rank zero is excluded by strict-top. The shared PR823 descent is used with the actual quotient target, not a silently saturated replacement.

The pinned PR842 review binds proof SHA256 `f55f5a6f1c06b0fd80db3a571f0ede56337100cd8d646a60f6cee0db768f8934`. Its complete branch analysis agrees with the retained source checkpoints. This certificate checks accounting and written theorem applicability; it is not a new formalization or independent production proof of the underlying geometric lemmas.

## Dependencies and reproduction

`source-pins-through842.json` pins PR842 proof/review and three original files. The existing through839 verifier recursively verifies the earlier checkpoint chain and pinned PR814,819,821,823,828,836,838,839 sources. The exact original pair catalog is `inputs/original-one-one-pairs-db515250.json` from through839. Keep all predecessor files alongside this checkpoint.

Run from the campaign directory:

    python verify_frontier_through842.py
    python -O verify_frontier_through842.py
    python -m unittest discover -p 'test*.py'

95 cumulative tests pass, including14 new tests. They reject missing/duplicate original tuples, incorrect source blocks, omitted branches, double label cuts and recounting pairs. Every surviving stable ID and source relation is preserved.

## Publication files added by through842

- `frontier-through842.json`
- `verify_frontier_through842.py`
- `test_frontier_through842.py`
- `source-pins-through842.json`
- `FRONTIER-THROUGH842.md`
- `inputs/pr842-proof.md`
- `inputs/pr842-review.md`
- `inputs/pr842-original_frontier.json`
- `inputs/pr842-original_splitting.md`
- `inputs/pr842-original_completeness.md`

Publish with, but do not merge into, the ten-file through839 checkpoint. No predecessor is modified. Exclude generated Python caches.

## Boundary

No Lean claim, global HM completion, Source2 closure, actual-instance computation, or realization count follows. Split low-positive retains bf/bc and38 necessary pairs; PR830's rank-two bf restriction remains a conditional branch, not a whole-source cut. Later unrelated results are outside this checkpoint.
