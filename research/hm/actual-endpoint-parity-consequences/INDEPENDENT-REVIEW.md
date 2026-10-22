# Independent review: actual endpoint parity consequences

## Verdict

**PASS, conditional on the explicitly pinned source identification and actual-input theorem.** No mathematical gap or blocking correction was found in the claimed parity, intrinsic reconstruction, all-direction full-map nonvanishing, or twelve-square restricted-rank conclusions. This review does not re-evaluate actual endpoint coefficients or certify a higher obstruction.

Reviewed `PROOF.md` SHA-256:

`3445f345a3964917ebe52cfb1555a4465f8fbc78b8b18da056d27591e08aa90c`

The review read these immutable supporting proofs:

- [PR661: square reconstruction](https://github.com/Akilleez-QA/read-em-and-weep/blob/1325647fd916bf2daa71b11efeae6d52cfefa2cd/research/hm/endpoint-square-reconstruction/PROOF.md).
- [PR662: full-map detection](https://github.com/Akilleez-QA/read-em-and-weep/blob/f75a18fd411350adda35dedf18751eee002a39bc/research/hm/endpoint-base-locus-exclusion/PROOF.md).
- [PR663: Wronskian and secant detection](https://github.com/Akilleez-QA/read-em-and-weep/blob/ad3ab59f6fbbbb3e5bde1da58b3b92a1f49c6889/research/hm/secant-detection-exceptions/PROOF.md).

The actual-input statements were compared with the [pinned actual endpoint normal-variation theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/fb574c01207099eeb63960da5cb23ad2f2498a84/research/hm/order-four-quadratic-load/ACTUAL-ENDPOINT-NORMAL-VARIATION-IS-NONZERO.md), treated here as an established conditional input.

## Checks

1. **Actual interface.** The pinned theorem identifies the zero input with a nonzero multiple of `st³` and the nonzero input with a nonzero multiple of `t⁴`, using the fixed source map. Transporting the source by that map preserves the required zero and nonzero statements. The proof correctly concerns the lower normal-variation family, not the third-Bockstein copy of P or the whole original-source endpoint family.

2. **New universal nonvanishing.** For `t⁷s`, membership in the complementary five-dimensional D inside `Sym⁸W` would give a root of multiplicity seven. The cited Wronskian lemma gives `N(7−5+1) ≤ 5(8−5+1)`, impossible because `N≥12` and hence `36>20`. The mixed symmetric-channel value is therefore nonzero. The mixed alternating-channel value is a nonzero scalar times the projection of `t⁶`, already nonzero by PR661. The pure symmetric value is likewise nonzero, while alternating parity kills the diagonal.

3. **Both parity projections.** The pure-input datum forces a nonzero symmetric component. At the mixed input, that component is nonzero by item 2. The total mixed value is zero, so it is canceled by a nonzero alternating component. This proves both line projections are isomorphisms from the one-dimensional normal space, without choosing numerical channel coefficients.

4. **C5 twist.** Take U of binary weight 1, so the parameter line U² has weight 2, `O(2)_[a]` has weight −4, and the source lines L0 and L1 have weights 4 and 2. Equivariance of a map into `P⊗O(2)` then requires P weights 8≡−2 and 6≡−4, respectively. Both occur once. Thus H0 and H1 are indeed lines with the stated twist. All objects in these Hom spaces descend to C5; the binary lift is only used to compute their characters. No trivialization of the parameter line is silently made.

5. **Canonical graph and reconstruction.** The two mixed restriction maps are isomorphisms onto the same intrinsic H1. Their composite gives the stated graph `ker r1`, a line meeting neither parity axis. The actual nonzero family lies on this line, so its image is exactly this line. Pure restriction is zero on the alternating channel and an isomorphism on the symmetric channel; consequently it is an isomorphism from the graph to H0. The displayed inverse formula follows and retains the unknown normal scale. It is invariant under all choices of generators. Equivariance transports the zero condition and the same kernel line throughout the twelve-point orbit.

6. **Every direction, full map.** A nonzero equivariant map from the irreducible parameter D has zero kernel. For every nonzero a, its trace-free square is nonzero: otherwise a nonzero rank-one tensor would equal a scalar multiple of the nondegenerate rank-three metric. This includes isotropic a, for which the proposed scalar multiple would be zero. Therefore every full endpoint map is nonzero, exactly as claimed, without asserting its rank.

7. **Rank at the twelve C5 squares.** The canonical secant input space is `K_a=L0⊕L1`. The actual restriction kills L1 and is nonzero on L0, so it has rank exactly one and kernel exactly L1. Equivariance proves the statement at all twelve square directions. This is a rank deduction from the two supplied values, not an additional selected-instance evaluation.

## Scope and minor wording

The exclusions in Section 6 are appropriate: no numerical ratio, nonsquare actual secant classification, full-map rank, fourth Bockstein, next ambient division, or higher repair follows here. In particular, the two mixed exceptional axis-kernel lines of PR663 are not identified with or distinguished from this mixed actual line merely by parity.

Non-blocking editorial suggestion: in Section 5, replace “two-dimensional kernel input space” with “two-dimensional secant input space” to avoid momentarily suggesting that K_a is the kernel of the endpoint map whose restricted rank is being computed. The subsequent sentence already makes the intended meaning unambiguous.
