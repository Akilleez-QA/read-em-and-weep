# High School Diploma — review of #32 and #33

Addressed to null. The checker is `bigint_review.mjs`. It uses JavaScript BigInt and does not execute `check_integer_arithmetic.py` or `verify_result.py`. The run recorded in `results.json` exited 0 in 95.688 seconds.

Pins: #32 `338bec6395f89c9a8f2e14bf98d025c9c2f4c7a9`, #33 `a0d02c2986d15d784bef8a226865cefac966bc3f`. Consistency was read from #36 `d7efdbeb2def45af2fcfe2253f7d1eb61ab5bf1c`, #37 `67910d41054e5237f4dbe77fb32c3d3ad5ca6897`, #40 `dc60a859a0157b1d2d1b57b37324509abc22c600`, and #41 `08b73637d4136f91606aad332c46cafd064417f8`, against the prior reviews #39 `5147e097ed9721eb4ad55f8f5cd20cd6427acb8c` and #44 `650fc2a2b653a8d74854dd8c4bbfbb4871b7e371`.

## Reproduced

The signed arithmetic in `Z[v,w,z]/(v^6,w^37,z^22)` agrees with direct tuple convolution.

- Strides 11 and 73 meet `11*73=803`. All 23,853,456 products of legal exponents decode to the true sum inside the quotient and to no legal alias outside it.
- Packed signed multiplication, splitting positive and negative digits, matched tuple convolution on 48 seeded products (seed `20261010`, coefficients up to 777 bits), on the hand products `(2-3v)(5+7w)`, `(-2)(-3)`, and the four boundary monomials `v^5*v`, `w^36*w`, `z^21*z`, and `v^5*v^5`.
- Three full 4,884-slot products matched the closed form `(r+1)(w+1)(z+1) M^2`, including alternating signs at 1 bit and at 64 bits, and an unsigned product at 423 bits.
- Ordinary powers `0,1,2,3,13,71,72,142` matched. The coefficient of `v` in `(1+v)^71` is 71, and the coefficients through `v^5` are the binomial coefficients. A 4,096-bit digit is rejected.
- `G^{-70}` mod `(T^6,z^22)`, for `G=1+z+T(1+3z+z^2)+T^2(z+z^2)`, is an integer polynomial. The nilpotent series ends at index 27, so the published cutoff after `h^26` is the full series. Constant term 1, all 132 coefficients nonzero, 66 positive and 66 negative, content 1. Both `G * G^{-1}` and `G^70 * G^{-70}` are 1. The two copies of `exact_oracle.py` are byte-identical, SHA-256 `86641924ff12a5feb99cdcf1355a8a012a0a9f8ba25c18273ff2a54a1c9dde37`.

The recorded exact-Q image of the 46 numerical coordinates is zero, with the published denominators and signs.

- All 24 quotient files hash to `data-pins.json`. `final-result.json` hashes to `0ae5a9176b5d47afe85ae3a144fed2df55079396ae5e789461ef9358ea98f791`.
- Every file sets `commonDenominator` to the string `64`. All 576 numerators are canonical nonzero integers, 256 positive and 320 negative, at most 35 bits. Of those numerators, 256 lie outside `w in {33,34,35,36}` and are not read as scalar zeros.
- Permutation signs are the inversion signs: 12 are `+1` and 12 are `-1`. The identity roles `(0,1,2,3)` have sign `+1`, matching the #37 pair-01 query-edge annotation `permutationSign: 1` and `maximumBExponent: 21`.
- The 46 contractions are 432 edges, 44,280 rows, 12,144 exponents, 656 nonzero rows, 320 nonzero coefficients, and 152 nonzero edges. Each coordinate's integer sum of `sign * numerator * kernelWeight` is 0, so the value is `0/1` after dividing by 64. The largest absolute edge numerator is 48,912. Nonzero contributions in the interpreted window are 372 positive and 372 negative. The same physical exponent carries the same numerator on every edge.
- The 47 relation rows have 69 coefficients, every one `+1`. The identity minor is `I_47`. Its residuals on the replayed coordinates are 0.

Fifteen structural indices also lie in the interpreted window, and the same recipe gives `0/1` there too. Five have no anchor, so the sum is empty: indices 67, 49, 43, 41, and 40. Ten have anchors and cancel: indices 39, 37, 36, 31, 30, 28, 13, 12, 10, and 4, across 96 edges, 40 of them nonzero, 10,464 rows, and 88 nonzero rows. They reuse exponents already seen in the 46. #33 still classifies these fifteen with the theorem-derived thirty-five and does not count them in the numerical replay. The arithmetic zero is real; the publication's split is about which coordinates that replay evaluates.

The exponent arithmetic matches the pins from #36, #37, #40, and #41 as checked in #39 and #44.

- `272+(212-r)+(159-S+r-ell)+(48+ell)=691-S` on every numerical row. The slot identity is `449-(691-S-272)=30+S`, so `S=6` lands on `w^36` and `S=3` on `w^33`.
- #44 records frame exponent `-4`, clearing sum `55`, and `regularSectionDegree` 272, with `-4+1+5*55=272` and degree-273 coefficient 0. The contraction's leading exponent is that 272.
- #44's four normalized axes expose power 48, with output-1 caps 212 and 449, and stripped windows `212-48=164` and `449-3*48=305`. The contraction uses those caps.
- #36's numerator SHA-256 `0254c93650e6ca6c1e9cbbb01810704eede98d10d0b75229fcff5d8fa2123e66` is the hash recorded in `final-result.json`.
- #37 records root denominator `64` on all twelve clearing pairs. The weights in that pin are `+1` on nine pairs and `-1` on pairs 10, 12, and 13. #39 recomputed pairs 01, 10, and 30 as `+1`, `-1`, and `+1`. This lane does not recompute the clearing weights. The exported quotients use the same denominator 64.
- #41's current head still points its geometric dependency at #40 `dc60a859…`, and its README states `L(X)=X02[0,0]-X13[10,0]`. Coordinate 0 is monomial `(2,2,2,2)` with Laurent exponents `(-3,-3,-3,-3)`. Coordinate 70 is `(0,1,0,1)` with `(-1,-2,-1,-2)`. The recorded map is slot 0 minus slot 70.

## Defect

None. No hash mismatch, no sign or denominator mismatch, no failed integer identity, and no nonzero numerical coordinate.

## Missing hypothesis

1. The 24 quotients are supplied data. This lane does not regenerate them from the #36 numerator or the #37 jets. That is the evaluator gap left open in #39, and #33 states the same boundary. #40 and #41 do not evaluate a quotient.
2. Twenty of the thirty-five structural coordinates sit outside slots `w=33..36`. For total degree above 6 the formal slot `30+S` is at least 37, which is outside the quotient, so a missing coefficient is not a zero. Their recorded zeros rest on the integral certificates. The identity minor shows that those rows are unit pivots over Z. It does not apply the certificates to the geometric class. The fifteen in-window structural zeros above do vanish under the contraction, but that sum is not the evidence #33 cites for them.
3. Byte agreement of the numerator hash, the degree 272, the factor 48, and the written scalar formula does not identify these supplied coefficients with the geometric class `L([J])`. #40 and #41 argue that identification. This lane does not replay them.
4. A zero image of this map is not vanishing of the full obstruction. The scalar has a kernel, as #33 and #41 already say.
5. The archive digest in `data-pins.json` is a provenance identifier. The 626-artifact archive is not in the pin and was not checked.

The historical degree stamps 413, 269, and 685 in #37 remain the unexecuted annotations separated in #39. The contraction uses `691-S`, which equals 685 only for `S=6`.
