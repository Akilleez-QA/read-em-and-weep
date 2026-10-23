# Six PR846 source edges after the published PR849 checkpoint

This append-only integration applies PR846 at `1644b5221fe6f8c23f30401fd6f2dc64230c0f5f` to the through847 certificate published in PR849 at `8d279e1816025b4c2103e4ebbd698cd94ac419f7`. File names use `pr846`, rather than a misleading chronological “through846”. The predecessor is unchanged.

## Exact accounting

The six full source-edge matches remove124 additional necessary pairs:

- Original index113, G3.11.ad509d55173f: ef17, ce17, be17. Remaining85.
- Original index125, G3.11.ea6bced3bddf: ee9. Remaining72.
- Original index127, G3.11.cce6e3ba4eeb: ef32, eg32. Remaining352.

Thus721−124=597 necessary pairs remain. All seven registered labels remain nonempty, profiles6/0/1. No label is removed. None of these six edges was already absent from the input relation, and no pair is counted twice. Four unaffected label records are identical.

Source names are shorthand only: ef=(0,0,0,0,1,1,0,1), ce=(0,0,1,0,1,0,0,1), be=(0,1,0,0,1,0,0,1), ee=(0,0,0,0,2,0,0,1), eg=(0,0,0,0,1,0,1,0). The verifier decodes the complete original eight-coordinate formula and matches full degree/irreducible multisets plus tuples, independently of local E numbering. It verifies original stable IDs, indices113/125/127, zero defects and full A/B arrays against immutable original files. The tuples belong to their respective necessary source lists.

## Whole-source coverage, not a basepoint-free restriction

The full proof and exact-version review were read. The common O(16) interface uses strict-top to supply eight or eleven independent sections. Any positive invariant divisor has degree at least12 and would leave at most seven sections, so the high-line map is necessarily onto. This proves absence of a divisor branch rather than assuming it. Both possible exact small kernels are retained.

For index113 ef and both index127 edges, the complementary-D argument includes internal image zero, O(-8), and W O(-7). Nonzero images are shown saturated by universal multiplication maps. The zero case has positive first-span degree; O(-8) gives a nongenuine polar character; W O(-7) forces a genuine constant V and two linear multiplicity rows. Both dependent and independent row cases contradict the actual inclusion/connection. No projected-image saturation is assumed.

For index113 be both kernels have zero internal image and positive first-span degree. For index113 ce the full V+2P top has zero internal image and exact quotient O(18), violating the profile-free rank11 quadratic Gauss gap. For index125 ee the required two-P block is intrinsically the kernel of the lower positive row in the three-P multiplicity isomorphism; both possible kernels have zero internal image and positive first-span degree. No actual coefficients are selected.

These are complete six-source exclusions under the pinned actual-bundle hypotheses. They say nothing about other sources in the10/10/13 necessary overlists. The original catalogs are necessary, not realizability statements.

## Pins and reproduction

`source-pins-source-pr846.json` pins the proof and review. The review binds proof SHA256 `e1c5bdad0cfe1f989ba1d325d35cd80d69dafc961da7710691a173c235b0af9a`. The existing recursive checkpoint chain checks the original catalogs at `db51525015bb7c5e825833d550d08dedf6f6ea96`, PR796 derivative-image/gap input at `d2b43060c83328dd5118aee6b9288fcfa0c873ac`, and PR802 first-polars input at `e484640a6565c278321bf6557860262c1ac1b7df`.

The upstream fixed character verifier was inspected, not rerun: this deliverable is current-relation integration, not a repeated production experiment or a new proof of the geometric lemmas. The independent local replay uses finite exact tuple bookkeeping only.

From the campaign directory:

    python verify_source_frontier_pr846.py
    python -O verify_source_frontier_pr846.py
    python -m unittest discover -p 'test*.py'

134 cumulative tests pass, including13 new tests. Tests cover six exact cuts, duplicate rejection, each branch requirement, the divisor argument, multiset matching under renumbering, unchanged predecessor/other records, and retained labels.

Certificate SHA256: `d51a2df425026dba304e3a0c9ce2f4f14b173500d3bceeaedb09c932fc06991d`.

## Exact seven-file publication list

- `frontier-source-pr846.json`
- `verify_source_frontier_pr846.py`
- `test_source_frontier_pr846.py`
- `source-pins-source-pr846.json`
- `SOURCE-FRONTIER-PR846.md`
- `inputs/pr846-proof.md`
- `inputs/pr846-review.md`

Prepared locally only, with no external writes. Exclude generated caches. Later results are not integrated. PR845 remains deferred as a necessary-form refinement, not an exclusion. No Lean, Source2 closure, actual-instance evaluation, realization count, or global completion is claimed.
