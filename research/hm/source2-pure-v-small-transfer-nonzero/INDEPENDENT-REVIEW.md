# Independent review: all-branch Q-image transversality and nonzero small transfer

## Verdict and reviewed artifacts

**PASS** for the expanded all-branch statement. Under the retained compatible pure-V actual-source hypotheses, the unique D_C in NC4 cannot lie in Q(NC2). Consequently the intersection with NC4 is I4 in endpoint nine and zero in every endpoint-sixteen branch. In endpoint nine the canonical transfer scalar is therefore nonzero. This selects no branch and establishes no source realization.

Reviewed SHA256:

- `PROOF.md`: `ce9a0cc3c56c83d46396cccc1c26b4b638a24bf3315d2d4b8ce53f26e78c9ad0`
- `verify.py`: `5e64f21e8b386dbd9a659f05635535669cacc9f7d90554e4192b03bcdff23e30`

## Authentication and all-branch premises

All six retained originals were freshly retrieved at their exact immutable repository paths and commits in `INPUTS.json`. Retrieved bytes equal the retained files, and independently computed SHA256 and Git blob hashes match the manifest:

| Input | Commit | Git blob |
|---|---|---|
| PR794 | `7fd254100b83bb03f41b776ea3119690aa51f671` | `3ad30b9aa1920408cc34778e78405f544b5adc8e` |
| PR795 | `3f811311d76914a555c7e7d0c5b887b41805aa6c` | `9358ec81c552913fac20f3a92d7b9f7c58105656` |
| PR1065 | `fd75633464cd587856287cc7866520fb4105ef5b` | `41f7dada9c1606c4a2a47b330b676b1f090ec1b4` |
| PR1068 | `05e8b33eb87e9f36aa30500145cc42bc0ea00df8` | `5ae07c02624d70c0ccd33d7ec34202504173ff83` |
| PR1069 | `41bc20cade3198306c492c0c46399d71eb0d51c4` | `827cd956e2eb574fd7d40d408e0450c8581fd7d2` |
| PR1074 | `7b7d6aad86dbd99ab476a1aa1fb7f43ec62afec3` | `7fd908be35e63b73df44133647638f96da2e545b` |

This authenticates these six originals, not all historical dependencies recursively.

The expanded theorem does not import its polynomial interface from a theorem conditional on endpoint nine. PR794 Section 1 supplies the actual pure-V quotient map f12 q_V, surjectivity after the two relevant twists, and injective residual inclusions for every coupling and balanced endpoint. PR795 supplies the actual polynomial endpoint system and its characters. Together these establish I2=f12 Sym⁴W, I3=f12 Sym⁵W, and ordinary multiplication inside NC2=Sym¹⁶W and NC3=Sym¹⁷W in every branch. The nonzero invariant f12 is not evaluated.

PR1068 proves equality of the **full ambient** degree-four joint-negative kernel with the embedded NC4, through the actual kernel-bundle and multiplication identifications. Mere terminality of NC4 would not suffice for the final contradiction. Its hypotheses retain both generated-endpoint branches.

## Independent prolongation audit

The polarization Delta(f)=(x⊗f_x+y⊗f_y)/5 is a section of multiplication on Sym⁵W and is equivariant. It gives the stated six recurrence equations for an arbitrary linear map j:Sym⁴W→Sym¹⁶W. Starting with the highest monomial equation and using that polynomial multiplication by x is injective proves successively that all five values of j vanish whenever its prolongation vanishes. This works for every linear j, not merely an equivariant one.

Independently, the full prolongation coefficient operator was constructed directly as a 108-by-85 sparse rational matrix, without taking the production Jacobian. Its exact rank is 85. A separate symbolic check with all thirteen coefficients of an arbitrary degree-twelve form free confirms that prolongation sends multiplication by that form on Sym⁴W to multiplication by the same form on Sym⁵W. This verifies the normalization used with f12 without selecting f12 itself.

For an equivariant nonzero j, its prolongation is a nonzero map from irreducible T=Sym⁵W. If its image were contained in I3, Schur's lemma would make it a scalar multiple of multiplication by f12. Injectivity of prolongation then forces j to be the same scalar multiple of multiplication by f12, and its image would equal I2. Therefore a D complement J to I2 has a distinct T image. The two T images have zero intersection and fill the entire two-copy T-isotypical component of NC3. Matching images alone would not establish this without the injectivity lemma; the proof supplies that missing argument.

## Actual contradiction, degrees, and parity

Assume only D_C⊂Q(NC2), without assuming endpoint nine. The restriction kernel I2 and the multiplicity-one D image supplied by PR1065 give an equivariant complement J in the actual D-isotypical part of NC2 that Q_2 maps isomorphically onto D_C. This is a consequence of actual containment and kernel data, not an arbitrary identification of repeated D copies.

Write Q_2:M2_+→M4_+ and Q_3:M3_-→M5_- for multiplication by the same invariant quadratic. Commutativity with the fixed negative linear forms gives Q_3(lv)=lQ_2(v). This is the original cohomology module's polynomial action in the stated degrees and parities. It does not extend h or a truncated radical map and does not require Q to preserve NC or NR.

Since D_C lies in the full joint-negative kernel, Q_3 kills WJ. Since Q_2 kills I2, it also kills WI2=I3. The prolongation argument therefore forces Q_3 to annihilate all of the T-isotypical component of NC3.

The unique V_C in NC2 has W⊗V=T, so its complete negative-linear image is contained in that same T-isotypical component. No rank or nonvanishing assumption about this image is required. Commutativity then gives WQ_2(V_C)=0. The full ambient joint-kernel theorem puts Q_2(V_C) in NC4. But Q_2 is injective on V_C, as its NC2 kernel is I2 of type D. Its image would be a nonzero V inside NC4=P+D, an impossibility. This establishes the all-branch exclusion of D_C incidence.

## Intersections and scalar corollary

NC4 is multiplicity-free P+D, so every invariant intersection with it is a sum of its two inequivalent constituents. Exclusion of D_C means the intersection equals the intersection with I4. PR1065 computes that intersection as I4 in endpoint nine and zero in endpoint sixteen, including the nonzero-N0-projection branch. No equality of this direct-sum character with NR4, or preservation of NR by Q, is inferred.

Only the final scalar corollary uses the endpoint-nine incidence theorem PR1074: the established intersection forces gamma≠0. The proof does not use that endpoint-nine hypothesis in the preceding all-branch contradiction and does not assign a numerical gamma. Neither endpoint is excluded by this theorem.

## Reproduction and limits

Both `python verify.py` and `python -O verify.py` passed all 37 checks with byte-identical output. The independent sparse prolongation and arbitrary-multiplier checks also passed. The six exact inputs, their all-branch hypotheses, and the actual degree-five commutation were reviewed in the written proof.

No actual coefficient, parameter, direction, point, jet, source matrix, or instance rank was evaluated. The universal rank-85 calculation concerns all linear maps between polynomial representations. It is not a computation of an actual HM map. The result is a conditional mathematical deduction, not proof-assistant certification or source realization.
