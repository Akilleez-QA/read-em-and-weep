# Three whole source edges from PR848/854 after published PR855

This separate append-only checkpoint removes **81 necessary pairs:17+32+32**, giving **591→510**. All **five labels, profiles4/0/1**, remain registered and nonempty. The predecessor published in PR855 at `4f1ed662a7124379900d1bb39942a5cd4537066a` is unchanged.

The exact new whole-source cuts are:

- Index113, G3.11.ad509d55173f, ff=(0,0,0,0,0,2,0,1):17 pairs, by PR848 at `77ef1c43e58ca05937ad878f81840274a3a9c064`. This label retains68 pairs.
- Index127, G3.11.cce6e3ba4eeb, the same ff tuple:32 pairs, by PR854 at `d45ae57e54ccd6d8929aecda77176b98507157e1`.
- Index127, fg=(0,0,0,0,0,1,1,0):32 pairs, by PR854. This label retains288 pairs.

The other three records remain identical. PR848's index127 scalar-nonzero argument was conditional and previously deleted no full edge. It is not counted as an additional cut now. PR854 independently covers ff and supplies complete scalar-zero/nonzero coverage for fg.

## Proof scope checked

Both full proofs and exact-version reviews were read. The common high-line construction uses the D multiplicity isomorphism to select a saturated P+D subsystem. Nine independent sections exclude a positive common divisor, rather than assuming basepoint-freeness. All three exact PR802 kernels and zero/nonzero saturated internal-image alternatives are retained. The nonzero case is excluded by the profile-free three-channel polar argument; the zero case gives the genuine constant ten-space and saturated projected residual. The residual D block supplies the actual M=T O(-1), constant seven-space C1 and locally free quotient O(6).

For index113 ff, removal of the forced nonzero O(-10) endpoint yields the exact degree−22 first span. The preserved coherent sum is shown saturated, not assumed so, and forces the impossible onto map O(6)→O(22).

For index127 ff, a kernel line of the two-dimensional scalar row supplies an actual O(-8) summand. Both external derivative components vanish, including the positive component by the degree10 invariant vanishing. Only the internal D channel can remain.

For index127 fg with scalar zero, the Euler endpoint is nonzero, but the proof uses the distinct O(-8) line with zero full external derivative. It does **not** discard the Euler kernel's possible O(-10) internal channel. For scalar nonzero, the actual graph kernel and split extension imply vanishing of that internal target in this different branch, giving the exact degree−24 first span and impossible O(6)→O(24) surjection.

The new scalar-line obstruction requires D0+L to be a direct summand of saturated Z. Both applications satisfy that premise. Constant projection gives a preserved image sheaf before saturation; the horizontal-lattice argument excludes a nonzero degree−8 image. The degree14 invariant vanishing places L inside M. Only then does saturation of D0+L justify equality with the same-rank M, contradicting degrees−18 and−6. These actual-connection and saturation premises are explicitly encoded in the coverage ledger and regression tests.

The verifier checks exact original labels, indices, zero defects, A/B arrays, source membership and full decoded block multisets. Local catalog numbers may be arbitrarily changed without changing cuts. This is current necessary-relation accounting, not a new production proof or a realization claim.

## Dependencies and reproduction

`source-pins-source-through854.json` pins the four new proof/review files. Review-bound proof hashes are:

- PR848: `70a85a7fc501598cfd81d8ee91a4c3244cb195a463a05eaf2a3a43ff93f17ca4`.
- PR854: `1f2c7ffb18c9a4e74b1f398c0edc5da87f08a6cd3d94acb0eea53b3836501218`.

The recursive predecessor chain provides immutable original catalog/frontier inputs at `db51525015bb7c5e825833d550d08dedf6f6ea96`, PR796 at `d2b43060c83328dd5118aee6b9288fcfa0c873ac`, PR802 at `e484640a6565c278321bf6557860262c1ac1b7df`, and PR828 at `ae077cbe42d65cde27d65ce88923dc35851b6952`. No whole-label conclusion from those inputs is imported into the new source proofs. Upstream production verifiers were not rerun.

From the campaign directory:

    python verify_source_frontier_through854.py
    python -O verify_source_frontier_through854.py
    python -m unittest discover -p 'test*.py'

163 cumulative tests pass, including15 new tests. These cover exact cuts, no conditional double count, every scope premise, direct-summand saturation, zero full external derivative, preservation of the Euler-kernel channel, full source matching, duplicate rejection, unchanged predecessor and retained labels.

Certificate SHA256: `c56375860d238bab5d171f4798025e09f4943406b899dc2aed7c78fef05945d4`.

## Exact nine-file publication list

- `frontier-source-through854.json`
- `verify_source_frontier_through854.py`
- `test_source_frontier_through854.py`
- `source-pins-source-through854.json`
- `SOURCE-FRONTIER-THROUGH854.md`
- `inputs/pr848_proof.md`
- `inputs/pr848_review.md`
- `inputs/pr854_proof.md`
- `inputs/pr854_review.md`

Prepared locally only. No predecessor modified, no external publication. Exclude generated caches. PR856 remains deferred as a non-exclusion fixed-window decomposition. No Lean certification, Source2 closure, actual-instance evaluation, whole-label removal, or global completion is claimed.
