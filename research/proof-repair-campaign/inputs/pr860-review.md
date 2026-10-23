# Final independent review: PASS

## Exact reviewed artifacts

This review applies to the following exact SHA-256 versions:

- `PROOF.md`: `f73132ccbdaf1e4db28197a6ea1a180a0216a46295c105f16623aed08e9e3bff`
- `verify.py`: `ef635a9083fda7bf4cba0ee22b8aa78926a065640dd8fd3cb095745e92467d2f`
- `REPRODUCE.md`: `3f7968e1d534b1d8678d7ccdc8ccb8c4e0b197942559ebb6627ba17e1410c6db`

The full final proof, verifier, reproduction instructions, and earlier independent review were read. The final proof was independently checked against the immutable dependencies below, not merely accepted from the earlier review. No mathematical gap was found within the stated claim and hypotheses.

The conclusion is exactly the exclusion of original source125 tuple `(0,0,0,0,1,1,0,1)` for `G3.11.ea6bced3bddf`. It is neither a whole-label exclusion nor a current frontier count.

## Mathematical checks

1. The kernel of the lower P multiplicity row contains a P line even when that row is zero. Together with D this gives a saturated rank-nine quadratic subblock whose derivative lands only in the saturated O(16). Strict-top supplies nine independent degree-eighteen sections. A nonempty invariant base divisor would have degree at least twelve and leave at most seven independent sections, so the quotient is everywhere onto.

2. The twist-two genuine H1 budget, central parity and dimension bound give precisely the six listed negative kernel atoms. The negative W in the twist-three Euler character forces O(-6); the remaining V+P budget gives precisely the three displayed kernels, each of rank eight and degree -34. The j=12 trivial atom contributes `Sym8 W=P+D` and is correctly rejected. The classification is exhaustive, not just a check of candidate kernels.

3. All internal maps have the stated Hom spaces. The P scalar image, tensor-Wp tautological image, and degree-six covariant or scalar-graph O(-10) image are saturated in every nonzero case. The saturated internal/external image lemma therefore applies to the actual raw derivative, without a torsion correction.

4. First-polar generation and the exact Euler characteristics give the three stated constant/linear decompositions. Their constant parts are actual subspaces of the original constant ambient space. Constant projection consequently commutes with differentiation; it does not install a connection on an abstract complement.

5. The expanded O(8) to O(16) argument is valid. If the D-to-T component vanished in the rank-six constant case, the saturated first span of D would be the entire constant six-space. Its quotient by D is O(10), so the D derivative factors through O(8) and is generically onto that line. Its composite into Q(-2) lies in O(16). Projecting the induced O(8) map to Q(-2)/O(16) gives zero generically. That quotient is locally free because O(16) is saturated, so the projected map vanishes identically. Thus the induced map factors through O(16). The equivariant Hom is `H0(O(8))^G=0`, contradicting strict-top. This explicitly justifies the final clarification and does not require the intermediate O(8) image itself to be saturated in Q(-2).

6. The P projection is also nonzero: it cannot map injectively into the constant A+V block because its A channel vanishes and V has smaller rank. The tautological D-to-T sequence, tensor-Wp Euler sequence, and the degree-six and degree-seven invariant-divisor arguments exhaust all zero/nonzero P-channel alternatives. Each alternative forces an entire nonzero linear summand into the projected image. Local lifts then put that summand's first span, a nonzero constant coefficient space, inside a pure negative linear bundle. This is impossible.

7. For zero internal image, the first span is an actual constant ten-space. Its quotient by F maps isomorphically to the saturated O(18) in Q, proving the exact intersection with E and the saturation of the constant-projected E/F. The projected derivative has the exact saturated image O(-10)+O(4). Its top P block maps onto O(4), with exact kernel V O(-4); every internal derivative component of that kernel vanishes by degree. The first quotient is therefore O(6). The profile-free quadratic rank-one gap excludes rank four and b=6, since b is neither eight nor at most three.

These steps use neither an interior-stage no-section assertion nor a horizontal equivariant bundle splitting.

## Immutable dependency checks

The original actual-bundle, strict-top and endpoint notes were retrieved at commit `db51525015bb7c5e825833d550d08dedf6f6ea96` of `Akilleez-QA/read-em-and-weep`, under `research/hm/order-four-quadratic-load/`. Their Git blob hashes are respectively:

- `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`: `b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3`
- `NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md`: `d7506dae49b4be43230450c4132bd5db91f137ef`
- `ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md`: `dcacf0bcdef8377c1ed7654e5b82659ea409456e`

The derivative-image and quadratic-gap arguments were read in Sections 3 and 8 of the [PR796 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md), Git blob `46a0de762000f21182f6d3168f3ecfd63adaf75f`. First-polar generation and constant projection were checked in the [PR802 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/e484640a6565c278321bf6557860262c1ac1b7df/research/hm/profile11-o16-constant-span-exclusion/PROOF.md), Git blob `98a1bd6123e148476da0b997d879aecbf885ec97`. The source decoding and separate ee scope were checked in the [PR846 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/1644b5221fe6f8c23f30401fd6f2dc64230c0f5f/research/hm/profile11-o16-six-source-exclusions/PROOF.md), Git blob `c62eb6cc2e5368f9a5364121fd9df4e67198f8d0`. The separate ee exclusion is not needed here.

## Reproduction and verifier audit

The verifier was inspected before execution. It uses only the Python standard library, exact rational arithmetic in Q(sqrt(5)), the fixed binary-icosahedral character table, bounded kernel eligibility checks, and exact reads of the two pinned original JSON files. It performs no network operation, source/model evaluation, or frontier recomputation.

Both JSON paths in `REPRODUCE.md` were independently fetched at the specified immutable commit. Their returned Git blob hashes match `fe0afa410d89340d3082dc814277f89fbb582c19` and `8b5971092f9ef762584912609fd5e9301c4e271d`. The supplied local files pass the verifier's byte-sensitive Git-object hash checks. The source125 A and B quotients, original defect zero, exact tuple membership, and stable-label association are checked directly.

Running the documented `python3 verify.py` command with Python 3.12.14 exited successfully and produced exactly:

```text
PASS: six kernel atoms, three kernels, 40 fixed internal Hom checks, polar and Euler-channel identities, original source125 ef identity.
No source/model evaluation, support search, all-twist envelope, or current frontier count was performed.
```

The reproduction instructions provide the complete external input list and correctly distinguish Git blob hashes from plain file SHA1 hashes. The verifier's three-kernel checks confirm their characters, ranks and degrees; exhaustiveness additionally uses the written budget argument. Its arithmetic output is not represented as a substitute for the connection and saturation proof.

No selected actual HM/source coefficients, parameters, points, derivative evaluations, matrices, instance ranks, scans, or large computation were used in this review. No publication action was taken. This is independent written mathematical review, not proof-assistant certification.
