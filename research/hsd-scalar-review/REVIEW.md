# High School Diploma — arithmetic and dependency review of #36 and #37

Pins reviewed, and not moved:

- #36 `d7efdbeb2def45af2fcfe2253f7d1eb61ab5bf1c` on `research/hm-current-scalar-numerator`
- #37 `67910d41054e5237f4dbe77fb32c3d3ad5ca6897` on `research/hm-current-scalar-jet-sources`
- Parent bridge #35 `6032b64d3f748c7ac37cb283db4a527e49d06ac8`

The numerator package and the source bridge are byte-identical between the two pins. #37 only adds `research/hm/current-scalar-jet-sources/`. This review did not rerun #24, #27, or #14/#20, and it did not run a quotient evaluator.

Environment: Python 3.12.3, Node v22.14.0, four cores. Jet regeneration used `--jobs 1`, `--stage-timeout 300`, `--axis-timeout 1200`. The package text says the jet scripts were tested with Node 24; these hashes still matched on Node 22. Generated DAGs stayed in `/tmp` and are not in this branch.

## Reproducibility

| command | exit | wall clock | result |
|---|---:|---:|---|
| `current-scalar-numerator/verify_numerator.py --output-dir /tmp/current-L-numerator` | 0 | 3.648 s | bridge 1,710 identities; numerator SHA-256 `0254c93650e6ca6c1e9cbbb01810704eede98d10d0b75229fcff5d8fa2123e66`, 4,186,496 bytes, 207,925 retained nodes |
| `current-scalar-numerator/test_source_checks.py` | 0 | 3.647 s | fresh reproduction plus 12 rejected corruptions, including overwrite refusal |
| `current-scalar-jet-sources/test_sources.py` | 0 | 0.063 s | 5 fixture tests |
| `node current-scalar-jet-sources/test_leading_two_jet.js` | 0 | (with the Python fixtures) | 160 exact coefficient checks, 4 axes |
| `current-scalar-jet-sources/regenerate.py --numerator …/local-numerator.dag.json --jobs 1` | 0 | 156.587 s | `ALL_32_EXACT_SOURCE_PINS_MATCH` |

An independent SHA-256 walk of the 32 jet artifacts matched `pins.json`, including byte lengths. Their total size is 249,022,910 bytes. Carrier DAG `31cd62eb3062801ca19073464c276fbe016fa4024fbcdcf48d3893358e3fcc18` (3,533,626 bytes, 178,251 nodes) and reduced model `635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926` matched the pins. Each leading DAG reports `rootDegreeBounds = [273]`.

`research/hsd-scalar-review/independent_exact.py` and `independent_jet_sample.py` use this review's own `fractions.Fraction` arithmetic. They do not import the package validators. Both exited 0 on the regenerated files.

## Stage #36 inputs

Present in the pin and discharged by generation or by an exact identity:

1. The #35 bridge sources, hash-pinned in `expected.json` at commit `6032b64d3f748c7ac37cb283db4a527e49d06ac8`.
2. The original MODEL object embedded in the bridge. Its canonical JSON SHA-256 is `9e808b52f263679a548656fa57bcb3a621f5264c20873621208b06acf4003614`. Outside the pin, that object equals the MODEL in #31 at `5d9ddb2a1e85b3bd6b43111e25e97cfe59d8cc86` (`research/hm/generate-hm-second-order-dag.js`).
3. Reduction of chart matrices `I`, `P`, `H0`, `H1` by cancelling tag factors. The bridge runs 1,710 cross-multiplications. The same count was recomputed here: for every entry, `new·oldDenominator = old·newDenominator`, and `gamma`, `delta`, and `ev` are unchanged. The embedded reduced MODEL equals the emitted `reduced-model.json`.
4. The unsigned carrier set `[2, 3, 4]` and the regenerated coefficient DAG.
5. Sixteen tag polynomials in `inverse_seeds.json`. They match `X_i`, `X_i^2-1`, `e_1,e_2,e_3`, and `F_j = v_j^4 - ∏_{k≠j} v_k` with `v_0 = 1` and `v_j = e_j(x)`.
6. Eighteen inverse seeds. Expanding each inverse's source node in the regenerated DAG, with no nested inverse, reproduced the claimed tag product.
7. Eighteen reduced-model denominator ties. Substituting `e_1,…,e_4` into each chart's `di`, `dp`, and `dh` reproduced the claimed tag monomial. On the unreduced MODEL all 18 substituted denominators are strictly larger (for example chart 0 has 240 terms against a 39-term factorization). That is the cancellation the cross-multiplications account for.
8. Scalar prefactors on reduced charts 1 and 2 (pivots 1 and 2). The package's 23 identities hold: two rows of `I_1 P_1 I_2`, two columns of `P_2 H^1_1`, the fifteen-entry `H1` column, and the four denominator-factor matches. Three further identities also hold: after the elementary substitution, reduced chart-1 `di`, `dp`, and `dh` agree, so dividing the `a`-numerator by `di` cancels the `dp` factor from the matrix product. The same row identities fail on the unreduced chart polynomials (9 differing rows), again because the common factors are still present.
9. Sixty-four feature moments for carriers 1–4, including the eight-row sample `(carrier, subset) = (3,12), (1,14), (3,10), (4,3), (1,2), (3,14), (4,5), (2,0)` from seed `20261010`. Each nonempty row matches the leading-coefficient formula and the operator `T_i(P) = (x_i^5 - x_i^3)[x_i^5] P`.
10. All 4,096 mask triples on all 256 feature codes: 160,000 accepted incidences, and the coordinate rule agrees with the three-factor moment product. The same seed's 32 codes (`168, 102, 83, …, 21`) contribute 25,856 of those incidences, and 128 further drawn triples agree. Zero products do not drop mask choices; the builder still visits every code.
11. The constructor contraction. The executed update is `Σ_{r,c} a_r M_{c,r} b_c`, then one negation, which is `-a M^T b`. Their fixture also rejects a missing minus and a doubled minus. The regenerated numerator records `explicitScalarJ2MinusCount = 1`, `sourceUnsigned = true`, and nonnegative output tag powers `[11,11,11,11,0,0,0,0,12,8,7,0,12,5,4,7]`.

`weighted_mask_moments.js` exports `contractResidualMoments` and `prefixContributions`. The numerator builder calls only `maskBasis`.

## Stage #37 inputs

Present in the pin and discharged by the regeneration or by the sample below:

1. The numerator DAG pin above, and `tagged_ring.js` SHA-256 `6e1c284cb3ba081c1b6447ec53b63ab115a82f2ee3ef34d01211f963fff2eba1`.
2. Four leading jets. Products add syntactic degree bounds and sums take maxima. Cancellation does not lower the stored bound. Each axis emits degrees 273 and 272.
3. Concrete-tag normalization at cap 64. The normalized `input` string is the historical relative label from `pins.json` (axis 3 uses the `all46-leading` label). The normalizer reads the CLI path.
4. Support enclosures, recomputed here on all four normalized circuits. They match `pins.json`. Output 1 exposes each surviving coordinate to exponent 48. Measured coordinate maxima are 212 and measured total maxima are 449, so the sharp factored windows are `212-48 = 164` and `449-3·48 = 305`.
5. Twelve compact reverse jets with `K = 6`, removed factor 48, and target degree 164. On the regenerated circuits `normalizedSyntaxDegree = 164`, `normalizedFactoredTotalDegreeBound = 305`, and the root reverse shift is 0. `homogeneousProjectionEvaluated` is false.
6. Integer clearing on pairs `01`, `10`, and `30`, recomputed from the normalized terms, including terms the reverse jet drops. Every stored weight is integral. Roots are denominator 64 with weights `+1`, `-1`, and `+1`, matching the pins. Pair `01` has 141,389 weights, pair `10` has 141,104, and pair `30` has 141,105.

## Missing hypotheses

These are used or cited by the two stages and are not generated or proved inside the pinned trees.

1. Geometric identification of the constructed numerator with `L(X_02, X_13) = X_02[0,0] - X_13[10,0]`, the carrier merger, and the chain-map rows `γ[10,:] = (v_0,0,0,0,0)` and `ev[:,0] = (v_0, 0)^t`. Those arguments are in #34 (`map-and-comparison.md`). The builder hardcodes charts 1 and 2, carriers `(2,3,4)`, and one J2 minus. This pin shows that the code does that, and that the resulting bytes match. It does not prove that this is the geometric class.
2. The chart rule `v_0 = 1`, `v_j = e_j(x_1,x_2,x_3,x_4)`. Every denominator and prefactor substitution uses it. The six-chart transition cocycles are outside this pin.
3. Pole and regular-section hypotheses from the #34 residue note: primary pole order at most 13, first-open pole order at most 1, and the legal divisor bounds. The clearing orders `(13,14,14,14)` are constants in the builder. The regenerated numerator has nonnegative tag powers, so these orders clear this DAG. The residue note's degree bound `deg A ≤ 272` needs those pole hypotheses. It is not proved here.
4. Vanishing of the degree-273 layer, equivalently identification of this expression with a regular section of `O(272)^4`. Each support receipt sets `degree273VanishingProved` to false. The leading files keep both layers and point the degree-273 gate at that identification.
5. Historical compact annotations, written by `compact_metadata` so the bytes match and not computed from the circuit:
   - first axis 0, 1, or 2: total-degree stamps 413, 269, and 685; pairing monomial `[2,2,2,0]`; six `gradedOutputs` with remaining degree `105+r`, source first degree 272, source second degree `212-r`, and original degree 685
   - pair `01` only: `queryEdges` with roles `[0,1,2,3]`, `maximumBExponent` 21, permutation sign 1
   - first axis 3: `targetFamily = nonvacuous46_scalar_coordinates` and the all46 flags

   The computed factored degree is 305 and the computed syntax degree is 164, so the stamps 269 and 413 are different numbers. The stamp `sourceFirstDegree = 272` assumes the degree-273 layer has already cancelled. `homogeneousProjectionEvaluated` is false, and `test_sources.py` checks that this metadata is not executed. A later evaluator has to take its degree, reverse layer, and b-window from the query.
6. The normalized-label strings, the cap 64, the reverse length 6, and the factor 48. The regenerated circuits do satisfy exponent 48 and degree 164. Why 48 is the geometric factor is part of the external source argument. `verify_support.py` then returns the literals 164 and 305 whenever the maxima are at most 212 and 449. On these four axes the maxima are exactly those caps, so the literals agree with the sharp enclosure.
7. `implementation-provenance.json` records `originalSHA256` values for five historical files. Those files are not in the pin, so the provenance hashes were not checked. The adapted sources in the pin are the ones that ran.
8. The quotient evaluator, the 24 historical coefficient hashes, and the 81 scalar coordinates. #33 and #37 both leave that stage unpublished. It was not run. Byte regeneration of the 32 sources does not identify those coordinates with the geometric class, and it does not decide the full obstruction.

The numerator builder also writes `all4096MaskChoicesRetainedByExactMoments: true` as a constant. The separate incidence check covers all 4,096 triples, so the constant matches the identity that was proved. It is not itself computed from the DAG.

## Errors

No hash mismatch and no failed identity turned up in the runs above. The unreduced MODEL denominators differ from the tag products; the 1,710 cross-multiplications are the identity that connects them, and those held. The degree stamps in item 5 of the missing-hypothesis list are a real numerical discrepancy with the computed windows 164 and 305, and the stamp 272 is one less than the syntactic bound 273. They are unexecuted annotations, not a failed pin.

prediction: #36 regenerates numerator `0254c936…` and its exact input identities; #37 regenerates 32 source pins; geometric vanishing stays outside both pins
oracle: `expected.json`, `pins.json`, and this review's Fraction arithmetic
delivery_state: both pinned regenerations exited 0 (3.648 s and 156.587 s); independent identities, 1,710 reductions, four support enclosures, and clearing on pairs 01, 10, and 30 agreed
outcome_state: arithmetic and byte regeneration agree; the eight missing hypotheses above remain unproved in the pinned trees
