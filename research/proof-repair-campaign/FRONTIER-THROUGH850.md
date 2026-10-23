# PR850: two full O(26) label exclusions after published PR851

The complete proof and review at `eed466e78efb572db42ebbe76bd0176cd47efe3a` exclude exactly G3.11.dc58cc54f352 and G3.11.4b6dad66f329. Applying those conclusions to the PR846 source checkpoint published as PR851 at `2738f7fa7c3a6e4b9f90ec98ca8886c40c74c9b4` gives **5 labels, profiles4/0/1**, and **591 necessary pairs**.

Each excluded label had exactly3 correlated necessary pairs, all on its matching E6 or E13 source. Thus597−3−3=591. These six pairs are counted once as part of the whole-label cuts, not again as source-edge exclusions. All five surviving records and stable IDs are identical to their predecessor. G3.11.8ae96830fd21 retains its4 pairs. No Source2 or global completion conclusion follows.

## Exact original source coverage

The immutable original catalog/frontier at `db51525015bb7c5e825833d550d08dedf6f6ea96` identifies indices112 and115, profile11, original defect0 and the exact A/B multisets. The full ordered source arrays, not merely selected memberships, are checked independently against the certificate:

- Index112: E0,U6,E3,E6.
- Index115: E0,U6,E3,E6,E10,U13,E12,E13.

Each name is resolved by its complete multiplicity tuple and decoded degree/irreducible multiset, not a catalog number. All twelve entries have explicit coverage:

- Index112 E0 and index115 E10: divisor0 by PR817 Section7; divisor12 and20 by PR813.
- Index115 E0 and E6: divisor-independent negative W-tail rank mismatch, explicitly pinned in PR817 Section7 and PR813/840 Section1.
- Every U6/U13 entry: PR829, including nonzero-divisor alternatives.
- Every E3/E12 entry: PR834 with PR813 divisor reduction.
- Matching E6/index112 and E13/index115: divisor12 by PR813, divisor0 by the complete PR840 argument, divisor20 by PR850 using PR825 and PR845.

PR813 proves that0/12/20 are all possible top-divisor alternatives. No other source, divisor, or mismatch is removed by a numerical count or a presumed realization status.

## New geometric scope and prerequisites

The full PR840 basepoint-free proof was read, including its exceptional internal Hom channel, the unsaturated first-span possibility with defect0/12, all polar rows, and its final exact-intersection contradiction. It is used only to remove divisor0, not the degree20 branch.

PR825 supplies the actual degree-ten constant block and exact sheaf intersections E∩C=F and E+∩C=F+. It does not assert that the entire projected residual is saturated. PR845 supplies all six necessary cubic-plane templates, their full constant spans of dimension7–9, and saturation defect0/12. The length20 elementary modification is not identified with T O(-3). PR845 is now used as a prerequisite, never treated alone as an exclusion.

PR850 retains the defect12 cubic case: its support is the orbit D12, disjoint from reduced D20. The actual ambient character and E's full-span hypothesis force the constant tail quotient B to have dimension at least10 and a P constituent. Both tail forms have generic rank two: rank zero contradicts full span, and rank one is excluded separately for W O(-9) and O(-8)+O(-10). On every point of D20, the exact fiber inclusion F+⊂E supplies a kernel vector with nonzero tail component, since the cubic part is fiber-injective there. Hence the tail exterior square vanishes on D20. Its source determinant is O(-18); vanishing on a reduced degree20 divisor forces the map to vanish identically, contradicting generic rank two.

These are written geometric inputs and applicability checks, not selected point evaluations. The certificate validates identity, complete source/divisor accounting, and pair partitions. It is not a formal proof of saturation or fiber arguments.

## Pins and reproduction

`source-pins-through850.json` includes PR850 proof/review and these newly included immutable prerequisites:

- PR840: `a69b5a8b9a7c4cb673a89c6465e152fcf699840a`.
- PR845: `3078ec876065f772aa10ef9d8478505035f71db8`.
- PR825: `ea94799a3b1e1c18a4d83061b92d7e7e2f1c631e`.

The predecessor chain already pins the original source/frontier files and PR813/817/829/834, including the mismatch scope quotations. PR850 review binds proof SHA256 `f2874bb3a6b90ef7742ac9f8014ddf532667745c63e8c630dfab70301fda4264`. All included Git blob hashes are checked. The upstream tiny character verifier was inspected, not rerun; no consumed experiment is repeated.

From the campaign directory:

    python verify_frontier_through850.py
    python -O verify_frontier_through850.py
    python -m unittest discover -p 'test*.py'

148 cumulative tests pass, including14 new tests covering all original4/8 tuples, full block matching independent of numbering, all source/divisor and tail premises, exact3+3 cuts, no pair recount, unchanged predecessor and survivors, and boundaries.

Certificate SHA256: `9dd0642fa5a74b86f0b57682d63b65b13ae0c3ce21a4629b4a3a7a2790d8f844`.

## Exact ten-file publication list

- `frontier-through850.json`
- `verify_frontier_through850.py`
- `test_frontier_through850.py`
- `source-pins-through850.json`
- `FRONTIER-THROUGH850.md`
- `inputs/pr850-proof.md`
- `inputs/pr850-review.md`
- `inputs/pr840-proof.md`
- `inputs/pr845-proof.md`
- `inputs/pr825-proof.md`

Prepared locally, with no publication or predecessor modifications. Exclude generated caches. PR848 at `77ef1c43e58ca05937ad878f81840274a3a9c064` remains deferred, including its conditional index127 branch. No Lean claim, Source2 closure, 8ae exclusion, realization count, actual-instance computation, or global completion is asserted.
