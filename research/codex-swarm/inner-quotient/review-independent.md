# QH-R independent review

**Accept the narrow generic synthetic coefficient algorithm and unexecuted actual-N14 formula metadata.** No blocking mathematical defect found in this scope. This is not acceptance of actual HM coefficient evaluation, full fiber integration, a physical cost certificate, or an obstruction conclusion.

## Immutable review inputs

All four producer file hashes matched `producer-ready.json` before and after review; the producer marker itself remained SHA256 `8da1b311ea9de9515c6b95a1fd89c5dd4f31430c18b8c130a387f45d4d069a34`.

| Producer file | SHA256 before = after |
| --- | --- |
| `quotient.py` | `08a0e51912e5afab249fa6accc759a03023ee5def7e400e3654ce84dbd4f2b91` |
| `README.md` | `0ed34c36c87d437f12f7605f00555c873b351c2a30c4c7bdbde7252c169b18f5` |
| `source-pins.json` | `bda2226ce1c4154b3c304da3ce13a98e35985bd9d66f343c45c85973ac6aecce` |
| `test_quotient.py` | `97e5f68f3508969a672242449c289c42a552f18664b9866f948d8c2fc8be0ae3` |

Consumed shared dependencies at review: INS01 `interfaces.py` SHA256 `9ba74c9e328c38083c4f8d49a04818d8a67216aa0a0b477563523ed4728f72fa`; `polynomial_coefficients.py` SHA256 `c826bc5379910222bb962288581a9e5fec64d3b956c03cefdfc4566567cf19ee`. Acceptance depends on these bytes; QH01's own producer marker does not bind them.

Read both source texts at commit `10810ee877fdaf291399198ad60d7dd0c316a42d` using `git show`, without importing a public source module. Independently verified their SHA256 and Git blob hashes in the controls: partition binding blob `f5a33e325e1eee6b801c94613093d1cd4686ca54`, combined-pole proof blob `9d7a5a400b48d9b8b46008fbd9fb3d79be601920`. Production authentication checks SHA256 rather than the informational blob field; the recorded bytes satisfy both.

## Mathematical audit

The actual metadata specializes the parameterized partition formula to N14/legal1, not the separate outer54/legal29 construction. Standard bits are high bit `3-i`; legal mask bits are low bit `i`. ActualCatalog's local v/H/h/a definitions match the pinned formulas, including H0=1 with an empty finite alphabet.

`first_hit` enforces sum n=L, n_j>=T and every earlier n_i<T; later slots remain unrestricted. The recursion enumerates the constrained compositions exactly once, and chained integer binomials give the multinomial. For L=(s+1)(T-1)+1, every composition has a unique earliest threshold crossing. Powers of the selected v_j are nonnegative. Primary Cbar includes k=N and k=M; auxiliary Dbar includes k=0 and k=N-1. Primary j>s returns zero; auxiliary sums all j<=s.

The infinity Qline factors `(t,1)` for pair axes and raw weights `(t²,1-t²)` for complementary axes agree with combined-pole §2. The shift is exactly `-N*d-owner_pair_legal_degree`, with d=5/4, and exponent reversal is shift-minus-local exponent. No additional pair twist is appended. Full five-field owners and ordered pair are required by the stream interface; no owner sorting/merging occurs.

Degree enclosures are conservative: L times the maximum c_i/v_i combined coordinate degree safely discards the threshold subtraction. Nonnegative polynomial convolution uses the full compatible finite exponent ranges. A stream covers the entire enclosure and returns all nonzero entries or raises before enumeration for volume>4096; it does not return a truncated stream. This does not certify occupied support or the sharper physical degree bounds from the source proof.

Physical refusals precede support checks at program coefficient/stream and ring coefficient entry points. The tiny tests also check a physical finite-mask structural-zero branch; it is refused rather than promoted to an evaluated source value.

## Independent controls

Seven new controls passed under both ordinary and optimized Python. Seven producer controls also passed in both modes: **14 tests per mode, 28 runs total**. No actual HM polynomial coefficient, actual fiber enumeration, or physical first-hit composition sum was evaluated. ActualCatalog construction only built bounded unexecuted formula metadata.

Independent tests compare all coefficients of three signed rational polynomial first-hit expressions against a separate rectangular composition enumeration with factorial multinomials and sparse polynomial multiplication; establish unique earliest-hit coverage on the tiny domain; test both N2 Cbar/Dbar endpoints with independent values; check complete two-infinity-axis streams for both pairs, five separate owner-field mismatches, and pair mismatch; reject oversized streams before querying coefficients; check shared query/index cap failures; and authenticate both immutable source texts and physical refusals.

Replay from the repository root:

```
python -B -m unittest discover -s research/codex-swarm/inner-quotient -p test_independent.py -v
python -BO -m unittest discover -s research/codex-swarm/inner-quotient -p test_independent.py -v
python -B -m unittest discover -s research/codex-swarm/inner-quotient -p test_quotient.py
python -BO -m unittest discover -s research/codex-swarm/inner-quotient -p test_quotient.py
```

## Exact boundaries and one resource-claim clarification

This supplies a missing generic partition coefficient algorithm, not actual physical coefficient streams or a multi-owner quotient/fiber adapter. Remaining work is to bind the actual homogeneous/frame theorem and complete owner fibers, integrate exact coefficient data with STD/INS, provide static complete resource accounting, and obtain independent physical admission. Existing finite-clearing and transport proofs remain completed at their published scope; this package does not reopen them. PH01's new frame proof is separate and must be accepted/integrated rather than replaced by these syntactic formulas.

The README's shared-budget wording must not be read as an aggregate metadata/memory bound across programs: query/split counters are shared, but node count and cache cardinality checks are **per Ring**, and index visits are per FiniteRing. A future multi-owner adapter needs explicit aggregate node/cache/index accounting in addition to retaining the shared query/split budget. Intermediate arithmetic and Python object overhead are not a hard memory supervisor. This limits the accepted resource claim; it does not invalidate the finite algorithm or authorize physical execution.

Only reviewer-owned `test_independent.py` and this report were written. No producer edits, Git mutations, posts, or commits.
