# PR860: one complete index125 source cut

PR860 at `cdf1d9ae5e477ef5f541d92888059ceedb4fd9b4` excludes exactly index125 ef=(0,0,0,0,1,1,0,1) on G3.11.ea6bced3bddf. This append-only integration removes **9 additional necessary pairs**, giving **510→501**. All **five labels, profiles4/0/1**, remain nonempty and registered. Index125 retains63 pairs. The other four records and all stable IDs are unchanged.

The predecessor published as PR857 at `17c102303f6fa130b68eb91e8e17c0208d486b09` is preserved byte-for-byte. The source is matched using its full tuple and block multiset, not its local catalog number:

    E=(2P+D) O(-2)+Wp O(-5)+O(-8)+O(-10).

The immutable original catalog/frontier at `db51525015bb7c5e825833d550d08dedf6f6ea96` confirms source index125, original defect0, A=O(-10)+O(4)+O(16), B=O(-18)+O(-6)+O(8), and exact tuple membership.

## Complete proof scope

The full proof and final exact-version review were read. The lower P-row kernel supplies a saturated P+D subsystem even if that entire row vanishes. Nine independent high-line sections rule out every positive invariant base divisor. The genuine character budget gives all three possible kernels, not merely candidate examples.

All four saturated internal images are covered: zero, P O(-4), Wp O(-5), and O(-10). The O(-10) case includes every scalar/covariant combination and graph, without selecting coefficients. In the three nonzero cases, first polars give actual constant/linear parts. The proof forces nonzero D-to-T and P projections, then treats T alone and all a=0, b=0, a,b≠0 alternatives for Wp+T. Each forces a full linear summand into a negative linear bundle via the actual connection.

The delicate D-in-constant-(A+V) alternative uses the expanded O(8)→O(16) argument: the composite is generically in O(16), and its quotient target is locally free because O(16) is saturated, so factorization holds as sheaves. The degree8 invariant vanishing then contradicts strict-top. This does not assume the intermediate O(8) image is saturated.

For zero internal image, exact intersection and saturated constant projection give the residual P system onto O(4), with exact V O(-4) kernel and zero internal derivative. Its O(6) first quotient violates the profile-free rank4 quadratic gap. The separate PR846 ee exclusion is not used as a premise for ef.

This artifact verifies finite accounting and complete written-theorem scope, not the geometric lemmas in a proof assistant. No actual coefficients, points, matrices, derivative evaluations or instance ranks are used; upstream production experiments/verifiers are not rerun.

## Pins and reproduction

`source-pins-source-through860.json` pins the proof and final review. The review binds proof SHA256 `f73132ccbdaf1e4db28197a6ea1a180a0216a46295c105f16623aed08e9e3bff`. Existing recursive predecessor dependencies provide original inputs, PR796 derivative-image/gap lemmas at `d2b43060c83328dd5118aee6b9288fcfa0c873ac`, PR802 first-polars input at `e484640a6565c278321bf6557860262c1ac1b7df`, and PR846 source conventions at `1644b5221fe6f8c23f30401fd6f2dc64230c0f5f`.

From the campaign directory:

    python verify_source_frontier_through860.py
    python -O verify_source_frontier_through860.py
    python -m unittest discover -p 'test*.py'

175 cumulative tests pass, including12 new tests for exact counts, every scope premise, all four internal images, the saturated-target factorization, full block matching under renumbering, duplicate rejection, unchanged predecessor/survivors, and boundaries.

Certificate SHA256: `8c9703f6f91bd92cf96053f498d7caab9c248d9a9339ea5a2666b3ee3ac7f77c`.

## Exact seven-file publication list

- `frontier-source-through860.json`
- `verify_source_frontier_through860.py`
- `test_source_frontier_through860.py`
- `source-pins-source-through860.json`
- `SOURCE-FRONTIER-THROUGH860.md`
- `inputs/pr860-proof.md`
- `inputs/pr860-review.md`

Prepared locally only; no publication or predecessor modification. Exclude generated caches.

## Explicit deferrals

PR858 at `d3b3134e23d0aa4c4b58fd1457f040856d2d0655` supplies abstract residual templates, not HM realization; no deletion or realization inference is made. PR859 at `6129e92a26572779003f3295227f688b77ed881c` contains only degree12 high-P branch restrictions and is not promoted to a whole-edge cut. PR856's non-exclusion fixed-window decomposition remains deferred. No Lean, Source2 closure, whole-label exclusion, realization count, or global completion is claimed.
