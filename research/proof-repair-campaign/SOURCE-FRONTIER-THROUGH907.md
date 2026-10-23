# Source checkpoint through PR907

From published PR910 (`988037951c759459fbed3e87c1bed4210125450d`, tree `e88028eb247b6089f8bb65b499e8c7996b5aeb54`), the exact necessary relation changes **178 → 146 pairs**. The sole new source cut is index127 tuple **(1,0,2,0,0,1,0,0)** for `G3.11.cce6e3ba4eeb`, removing 32 pairs. All **four registered stable labels (3/0/1)** remain; source125 stays registered with its empty relation and whole-label gate held.

Remaining row counts: 8ae96830fd21: 4; cce6e3ba4eeb: 64; ea6bced3bddf: 0; d610e381ed75: 78. Index127 retains two source tuples, a-b-c-f and c-d-f, each with 32 pairs. Necessary witnesses do not assert realizability.

## Exact mathematical dependency and scope

[PR907 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/35930c4e87a3cc3274e886b59821ee99ae8f43b4/research/hm/profile11-source127-accf-exclusion/PROOF.md) imports only the stated accf interface from [PR901](https://github.com/Akilleez-QA/read-em-and-weep/blob/12d7fbb02ffbfd920bd5133c197ca9166cbabc5a/research/hm/profile11-source127-wp-scalar-reduction/PROOF.md), Git blob `8734e450297032410ac5625efeddd3cea34fd654`. Both complete proofs and exact-version reviews are included and authenticated. PR901 alone is a partial reduction, not a source cut.

The assumed source is the actual saturated full-span bundle with original defect-zero Gauss quotient, not an abstract bundle having matching degrees. The original actual presentation, strict-top note and two catalogs are pinned at `db51525015bb7c5e825833d550d08dedf6f6ea96`, through the immutable predecessor chain. Their Git blobs respectively are `b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3`, `d7506dae49b4be43230450c4132bd5db91f137ef`, `fe0afa410d89340d3082dc814277f89fbb582c19`, and `8b5971092f9ef762584912609fd5e9301c4e271d`.

PR901 retains every kernel channel, excludes the zero-internal and V-only accf cases by actual coherent projection and saturated universal quadratic injections, and forces the nonzero scalar row with full cubic coefficient span V+D. The additional internal V row remains unrestricted. The imported first span is P(-2), with exact image **f12·O(6) inside O(18)**. The final cubic flag and any unspecified intersection with E-plus are not imported.

For PR907's top V(-2), the high row factors through the exact O(4) image with divisor twelve. The kernel Wp(-5) has only its original equal-degree Wp internal channel. Both possibilities are covered:

- Nonzero internal image: the raw first span is T(-1), its invariant saturation defect is at most six and therefore zero, and its intersection with E is exactly the preimage B plus the original R. Its coefficient span P+D cannot contain R's full V+D span.
- Zero internal image: the raw first span is a genuine constant P, disjoint from V+D. Its sum with the cubic first span is P plus P(-2). Both map onto the **same coherent** f12·O(6) image, including at the divisor, by the one-dimensional invariant degree-twelve space. No division by f12 or replacement with the saturated O(18) is allowed. The exact kernel has rank seven and degree -14, hence pure degree -2, impossible as a subrepresentation of the multiplicity-free top V+D whose subrepresentation dimensions are 0, 3, 5, 8.

This is an accounting certificate conditioned on those written proofs, not an executable certification of the geometric arguments or a Lean claim. No actual-instance evaluation or production experiment is run.

## Reproduction

With the predecessor files unchanged, run:

```sh
python verify_source_frontier_through907.py
python -O verify_source_frontier_through907.py
python -m unittest test_source_frontier_through907 -q
python -m unittest discover -p 'test*.py' -q
```

24 new tests and 316 total tests pass. The executable verifies pinned bytes and review bindings, exact original tuple plus decoded multiset, endpoints, defect, unchanged stable IDs, disjoint cuts, and remaining pairs. Runtime checks remain enabled under `-O`. Regressions reject omitted branches, saturated-image substitution, treating PR901 alone as a cut, dropped original intersections, duplicate cuts, mismatched endpoints/blocks, and arbitrary source-ID assumptions.

The source125 whole-label gate remains held pending a separate immutable original-ten-tuple certificate. PR869's abstract 8ae family and PR876's abstract c-d-f family are unchanged, neither excluded nor asserted realized. Every later result is deferred.

## New publication files

- SOURCE-FRONTIER-THROUGH907.md
- frontier-source-through907.json
- source-pins-source-through907.json
- verify_source_frontier_through907.py
- test_source_frontier_through907.py
- inputs/pr901_proof.md
- inputs/pr901_review.md
- inputs/pr907_proof.md
- inputs/pr907_review.md
