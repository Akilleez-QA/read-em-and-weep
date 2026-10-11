# Independent replay of the all-81 L_minus scalar image

Supplied-data agreement with draft #62 at `4fcc2e09aa80b77da5bc872acc1985e86bba417c`, directory `research/hm/second-scalar-all81`. Exact mismatches: none.

The selector was committed at `47e4237d6c9e6314aeec04f8266c769565f40584` before `expected.json` or `replay.py` was read. The canonical row digest was inspected only after that commit, and `selector.py` was not changed. This check does not import the package replay.

## Coordinates

All 81 coordinates are `0/1` in lowest terms. The partition is 65 nonempty selector boundaries and 16 empty ones. Emptiness was counted by enumerating orientations whose leading axis `i` satisfies `m_i = 2`. The empty indices are 40, 41, 43, 44, 49, 50, 52, 53, 67, 68, 70, 71, 76, 77, 79, 80. Each of those values is the empty sum. They were not filled in from a global source symmetry.

## Requests, rows, and binding

There are 648 oriented requests. Each sign is the sign of the orientation permutation. The census is 114,048 selected rows, 32,472 distinct physical exponents, 10,504 nonzero rows, 3,152 distinct physical exponents carrying a nonzero coefficient, and 552 nonzero signed selections. Repeated physical exponents carry equal coefficients (0 conflicts). All 648 canonical row digests match.

The 24 arrays form 12 equal pairs under the physical involution `sigma = (0 2)(1 3)`. Recorded configuration, normalized-source, compact-source, and checkpoint pins differ inside each documented pair. Selector rows match after `sigma` moves the target and the physical exponent. The six pairs named for `m = (2,2,2,0)` contribute 1,086 rows. At that fixed target the partners are not interchangeable: `0123` contributes `8655/16` and `2301` contributes `131/2`, while `2301` at the image target `m = (2,0,2,2)` again contributes `8655/16`.

## Negative controls

The constant term of `G^(-70)` is 1, and every coefficient in the window `T^0..8`, `z^0..22` is nonzero. Orientation `0123` selects slot `(r, w, ell) = (8, 41, 22)` only at coordinate 2. Adding 1 to that numerator was required to break coordinate equality. It changed coordinate 2 by exactly `1/64` and left the other 80 coordinates fixed.

The same-target identification of equal arrays `0123` and `2301` was required to break the binding check. Their signed selections are `8655/16` and `131/2`.

Slot `(4, 27, 22)` is present in the `0123` array and is selected by no target. Adding 1 there leaves all 81 coordinates unchanged, so that edit lies in the detector kernel and was not used as a control.

## Package tests

From the pinned tree, `replay.py` exits 0 under normal Python and under `python3 -O`. The two outputs are identical, with status `PASS_ALL81_SUPPLIED_QUOTIENT_REPLAY`. `test_replay.py` reports 24 passes in both modes.

## Scope

The inputs taken as given are the 24 supplied quotient arrays. `source_regeneration_reproduced` and `full_obstruction_computed` are both false in the package record. This replay does not regenerate sources and does not claim that the full obstruction vanishes.
