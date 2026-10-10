# High School Diploma — independent review of #34

Pinned head: `a100f4e0be453d6e182320b792359f8a04e32b4d`.

The notes under `research/hm/current-scalar-proof/` were read line by line. Every executable identity and integral residue check below was recomputed with separate exact integer and rational arithmetic in this directory. The package verifier programs were not executed. Rerun with

```sh
python3 research/hsd-review/34/run_review.py
```

The machine log is `results.json`. No arithmetic defect was found. This does not regenerate the geometric numerator and does not resolve the full obstruction.

## Proof hypotheses

Stated, and not certified by this review:

1. The geometric residual is closed and is included in `End(K)` by a contraction with `H^2 = HI = PH = 0` and `1 - E = d_K H + H d_K`.
2. Physical-frame transport supplies the stated line-bundle transition. A reordered tuple is the same cochain, alternated and transported.
3. In the auxiliary-first order, degree `-3` has injective vertical differential, so two lifts of one residual leave no bottom vertical class.
4. The completed scalar has primary pole bound 13, first-open pole bound 1, legal-0 pole bound 1 along `Y_i = 0`, and legal-1 pole bound 1 along `x_i = 0` and `x_i^2 - 1 = 0`, including original-frame transport.
5. `(H0)` and `(H1)`: `deg_{x_i} A ≤ 272` with denominator `h_1^{13} h_2^{14} h_3^{14} h_4^{14}`, and each boundary coefficient `A_i` is divisible by `∏_{j≠i} x_j^{48}` with `deg_{x_j} A_i ≤ 212`.
6. The separate exact-rational package supplies the 46 coordinates outside the 35 forced zeros. Those coordinates were not recomputed here.
7. Applying the 35 zeros to the geometric scalar requires identifying that scalar with this closed finite-model class.

Justified in the notes, and matched by the checks below where the step is executable:

- `L d_End = 0`, because both selected entries of `(W ev, γ W)` equal `v_0 W[0,0]`.
- On the two pivot-0 charts, `I[10] = 0`. Each stored `H_0[0]` row equals that chart's denominator in column 10 and is zero elsewhere, so the normalized row is `e_10`. On the chart `v_0 = 1` this is `e_10^t / v_0`. The two stored numerators are different; the normalized rows agree. The scalar formula `c = -Z[10,0] / v_0` uses the normalized row.
- `h_j = v_j^5 - v_0 v_1 v_2 v_3 v_4`, so `D(v_0)` and `D(h_1),…,D(h_4)` cover `P^4`.
- The ordered prism is a chain homotopy on increasing tuples, and the weighted projection preserves alternating cochains, including repeated coarse labels.
- The degree count `1 + 5·55 - 4 = 272`.
- The 47 integral relations are the full scalar image over `Q`, because they have rank 47 and the image has dimension 34.
- The pure-positive quotient `ker C / (T ker A)` is the full 20-dimensional common kernel of the constant scalar maps over `Q`.
- The integral formula is an identity of universal integer functionals under `(H0)` and `(H1)`. Agreement modulo every prime greater than 5, through the checked kernels and the checked coefficient extraction, gives the rational identity. It is not a lift of one modular zero.

## Executable identities

Reproduced:

- `γ[10,:] = (v_0,0,0,0,0)` and `ev[:,0] = (v_0,0)^t`.
- All ten bottom units `ev[b, 5b+k] = v_k`.
- Normalized first-carrier rows as above, on charts 0 and 5.
- The 50 constant-map equations have a permutation matrix in the first 50 columns, so the constant scalar maps are 30-dimensional over every field. The current scalar is `-L_(10,0)`.
- Prism identities: 251 on the stated weights, and the same identity on a second rational weight system. Chain comparisons: 25. Left inverses: 19.
- Alternating projection on all 27 coarse triples, including repeats.
- Legal-line partition: 256 divisibility checks; the mask weights of each `h_j` sum to `h_j`. Nonzero mask counts are 5, 11, 15, 16.
- The `P^1` example has weighted value `x^{-1} - x^{-3}` and residue 1.
- All 125 points with fifth-root coordinates and product 1 have Jacobian determinant 125. A zero coordinate forces `p = 0` and then every fifth power to vanish. Leading terms `a_j^5` are pairwise coprime, so the quotient length is `5^4 = 625` and the origin has length `625 - 125 = 500`.
- All 10,000 monic monomials with exponents in `0,…,9` satisfy the stated normal-form residue rule.
- `Res(z_1^2 z_2 dz / (e_1 e_2 e_3)) = 1`. On coordinate degree at most 2, the residue is the signed sum of the six `(2,1,0)` coefficients, with no factor 6.
- Both constructions of `G^{-70}` in `Z[T,z]/(T^6, z^{22})` agree, multiply with `G^{70}` to 1, match the six displayed coefficient rows, and reduce at primes 7, 13, 29, and 71 as stated. All 132 truncated coefficients are nonzero. Modulo 71 the series is `G`.
- `q = e_1 e_2 e_3` matches the stated factorization. For every slot type and for `N = 1,2,3`, the monomial coefficient in `A_i q^N` equals `[z^{L-ℓ}][T^{d-r}] G^N` (8,505 comparisons, no failure).
- All 648 edges have the stated sign, and all 68,040 slots have total degree `691 - S` and the stated reversal.
- Infinity orders are `t^{1-m}`. Poles are simple and occur only for `m_i = 2`. For every tested prime power `P ≥ 71`, the Cartier output degree is 2.
- Numerator degree 272, and the four-form sign `(-1)^6 = +1`.
- The elementary-symmetric fibers at `0`, at `e_1 = 1`, and at `e_4 = 1` have length 24 through degree 8. The products `625·24 = 15000` and `500·24 = 12000` follow.
- The sixteen multi-indices with every `m_i ≤ 1` are among the 35 single-coordinate zeros. The other 19 zeros are exactly the remaining forced coordinates.
- Rebuilt matrices match the published fingerprints `b3b74b9b39b8c6c034028d79f37af352d0b94d50941dbc24e41a9cdea2b9ecc3` and `c22c0750a701d8172f3e2a0e4d0515b86ea13ac98f164ced241c12fc5ce7784e`.
- All 47 witnesses (221 terms, every row in the pure-negative block) match over `Z`. The 47-by-47 minor is the identity. The prose relation list matches the certificate, with every coefficient `+1`.
- The current scalar and all 2,430 constant-scalar rows kill the incoming boundary matrix.
- `D_2 D_1 = 0` on all 2,560 source columns.
- Over `Q`: outgoing rank 3,648, augmented current rank 3,682, current image rank 34, combined rank 3,980, cohomological rank 332, incoming rank 2,550, transferred rank 10, and `dim H^2 = 352`. The current kernel dimension is 318 and the common constant-scalar kernel dimension is 20.
- The positive differential has rank 50, so `dim ker C = 30`.
- The control cycle `n = 0`, `p[7] = p[23] = p[50] = 1` is closed. Its keys are the three published basis keys. The functional `-p[7] + p[25]` pairs to `-1` and kills the ten transferred kernel vectors, so the class is not a boundary. Every constant scalar output vanishes because `n = 0`.
- Over `F_13` the outgoing rank is 3,648 and the current rank is 34, both on the full outgoing matrix and on its pure-negative part (that part has rank 3,488). Over `F_29` the outgoing rank is 3,648 and the combined rank is 332.

Defects: none.

## Scope limits

- No geometric numerator, quotient export, or the 46 non-forced scalar coordinates was recomputed. A zero current-scalar image is not a conclusion of this review.
- Pole bounds, contraction axioms, frame transport, and bottom injectivity remain source hypotheses.
- `(H0)` and `(H1)` were not tested on a source polynomial. The integral formula was checked as a universal functional.
- The global Serre trace is used as cited background. The local residue normalizations above were recomputed; those papers were not rederived.
- Length 24 was recomputed for three fibers through degree 8, not by a general freeness certificate for every fiber.
- Rank 34 in characteristic 13 and rank 332 in characteristic 29 are checks in those fields. The identity minor gives the relations in every characteristic; it does not give image dimension 34 in every characteristic.
- The integer control cycle is a finite-model class. It is not a geometric obstruction witness.
- The lanes of #24, #27, #14, and #20 were not rerun.
