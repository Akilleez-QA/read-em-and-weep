# Verdict on the selected L_minus m2220 aggregate

Reviewed head: `b1fdcdd666ed188250d6def3616733f1417fca81` (#57).

Revision: the six identical coefficient arrays are the orbits of the carrier
involution `iota(i)=i+2 (mod 4)`, not a packaging defect. The paired signed
readings do not cancel. See `symmetry/README.md`.

`contributions.json` SHA-256
`72b08646afaf3a493243698583ee1f434a9dd78707d775d4fd0206593a5b87f0`.

Evidence class: **supplied-quotient replay**. This is not source regeneration.
The package sets `whole_scalar_map_computed`, `full_obstruction_computed` and
`source_attribution_reproduced` to false, and its provenance records
`historical_source_nodes_reevaluated_by_comparison = 0` with neither terminal
checkpoints nor new-map source regeneration distributed. Every edge likewise
records zero source-node reevaluations.

## Reproduced

For `L_minus(X) = X02[0,5] - X13[10,1]`, `m = (2,2,2,0)` and Laurent exponents
`(-3,-3,-3,-1)`, the displayed selector applied to the eighteen supplied
coefficient arrays reproduces every recorded sign and every recorded signed
value. Their sum is **0/1**.

Both kernel expansions agree, every kernel coefficient is an integer, and both
satisfy `G^{70} G^{-70} = 1` modulo `(T^9, z^{23})`, where

`G = 1 + z + T + 3Tz + Tz^2 + T^2 z + T^2 z^2`.

The active orientations are exactly the 18 permutations whose first role has
monomial weight 2, in lexicographic order. No signed contribution is zero.
The file contains 4,014 quotient terms, 3,258 selector rows, 3,258 distinct
physical exponents and 288 nonzero selected coefficients. The worked identity
for 1302 holds: the unsigned contraction is `-407/8` and the orientation sign
is `-1`, so the signed value is `407/8`.

| Orientation | Sign | Recomputed signed value | Quotient array |
| --- | ---: | ---: | --- |
| 0123 | +1 | 8655/16 | published in #43 |
| 0132 | -1 | -2817/16 | published in #46 |
| 0213 | -1 | 18831/8 | published in #46 |
| 0231 | +1 | -21601/8 | published in #46 |
| 0312 | +1 | 1457/8 | published in #50 |
| 0321 | -1 | -803/4 | published in #50 |
| 1023 | -1 | 15705/16 | published in #50 |
| 1032 | +1 | -5667/16 | published in #51 |
| 1203 | +1 | 1953/4 | published in #51 |
| 1230 | -1 | -4313/4 | published in #51 |
| 1302 | -1 | 407/8 | published in #55 |
| 1320 | +1 | -353/4 | published in #55 |
| 2013 | +1 | -41517/16 | same array as 0231 |
| 2031 | -1 | 42869/16 | same array as 0213 |
| 2103 | -1 | -22917/16 | same array as 0321 |
| 2130 | +1 | 21869/16 | same array as 0312 |
| 2301 | +1 | 131/2 | same array as 0123 |
| 2310 | -1 | -169/2 | same array as 0132 |

The thirteen previously published edges agree with the pinned packages in both
the signed rational and the SHA-256 of the compact coefficient list:

- #43 `b29c6aec939e4ee270da1bdadd8b3e2469b6e5cc`: 0123 = 8655/16
- #46 `99c271053c98f50633a3d4dd7927fb8c8d9852a8`: 0132 = -2817/16, 0213 = 18831/8, 0231 = -21601/8
- #50 `abc79ba07db1a36883547528c59ba9609bb412fa`: 0312 = 1457/8, 0321 = -803/4, 1023 = 15705/16
- #51 `cc094c174a2ae3d5bd2abc99b95e0a8366d599ae`: 1032 = -5667/16, 1203 = 1953/4, 1230 = -4313/4
- #55 `60daad77179e93b2eb4adf7c2c77cfe298053fc5`: 1302 = 407/8, 1320 = -353/4, 2013 = -41517/16

The five edges first supplied here were recomputed from the coefficient lists
in this package, not taken from an earlier review. Those recomputations equal
the recorded rationals above. They are selector readings of copied lists, as
recorded in the defect.

## Defect

Reclassified by `symmetry/README.md`: this pattern is the involution
`iota(i)=i+2 (mod 4)`. It is not a copied-file defect. The description below
is the array identity that the involution predicts.

The eighteen edges carry **12** distinct coefficient arrays, not 18. The pairs
related by adding 2 (mod 4) to every role index have identical integer lists,
including order and sparse slots. A witness: 0123 and 2301 both open with the
term `[4, 27, 22, "-600"]` and share

`dfc8ee5bbabef051a9c18708f0b93b758ed34943ace9ee7ee448a0b33640da71`.

| Copied pair | Shared coefficient SHA-256 |
| --- | --- |
| 0123 = 2301 | `dfc8ee5bbabef051a9c18708f0b93b758ed34943ace9ee7ee448a0b33640da71` |
| 0132 = 2310 | `40cf406681bbeedad3681da604300dd99ff9975b6a6fd3b403dcee5a3d92d9af` |
| 0213 = 2031 | `cae19babdc6803c0c161f93ff2ff61221c108e23ecdb1808df0c701d3bf5bf4f` |
| 0231 = 2013 | `862a4435777b4e5ab98b8dd5000bcccab4d8b83dcd0203af14531fda9b47eaf6` |
| 0312 = 2130 | `5691e1144b4eab9fbddcd249f4d8675faf50cac382864c0c1b9f4d116ae7fd05` |
| 0321 = 2103 | `3277c1d8a6ca67a8b69f2d0a29007e47f6d7287679e75339fae0fa99fd3dd7cc` |

The 0231 = 2013 copy is already present in the pinned #46 and #55 packages.
This package preserves it and adds the other five copies. Those five are the
orientations that #57 presents as newly supplied quotients. Their signed
values differ from their partners only because the selector `(d, L)` and the
permutation sign differ. For example, 0123 uses `(d, L) = (8, 22)` and sign
`+1`, while 2301 uses `(6, 20)` and sign `+1` on the same polynomial.

Inside each pair the recorded `original_quotient_sha256` values differ. Those
hashes name artifacts that are not in the package. #43's provenance says the
exported quotient omits metadata, so a hash difference does not prove the
historical coefficient lists differed. The defect that this review can see is
in the distributed lists: six orientations do not have their own quotient
polynomial here.

No contribution was zero-filled. The replacement is a nonzero copy.

## Missing hypothesis

These are outside the finite contraction, and they are not repaired by summing
the supplied arrays.

- The complete L_minus source, including the column-5 right prefactor, the
  unchanged carrier tail and the frames that produce each orientation's
  numerator.
- Fresh support enclosures 47/215/454, legal-line comparison, all-entry pole
  bounds, safe reversal and integer clearing for this map. The original
  scalar's window and zero list do not discharge them.
- Source-node evaluation that would produce eighteen quotients. The historical
  anchors reevaluated zero source nodes.
- Public terminal reconstruction. The checkpoint archives are not in the
  package.
- Source-to-obstruction attribution for the ambient geometric problem.

## What the total establishes

The total establishes one arithmetic statement: under the displayed selector,
the eighteen supplied arrays — twelve distinct polynomials, six of them
inserted again under the shifted orientation — have signed sum `0/1` in `Q`.
Each of those eighteen signed readings is nonzero, and the thirteen published
partial edges match their earlier packages.

The total does not establish that the full L_minus image vanishes, that any
other monomial coordinate vanishes, or that the full obstruction vanishes. It
does not establish a theorem. It also does not establish that eighteen
independent orientation quotients cancel. A geometric reading of even this one
coordinate stays conditional on the missing source hypotheses above.
