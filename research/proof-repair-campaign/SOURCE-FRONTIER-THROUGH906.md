# Source checkpoint through PR906: label gate held

From published PR899 (`3cde13b41962d494da61131bc84fbf8b82442b9d`, tree `01bec44088df5e40767d2bdccc09f3a9bb534553`), the exact necessary relation changes **228 → 178 pairs**. All **four registered stable labels (3/0/1)** remain. Three have nonempty relations. The empty index125 relation is not promoted to a whole-label exclusion here: that gate awaits a separate immutable original ten-tuple exhaustion certificate.

| Proof | Original index | Full original tuple | New pair cuts |
|---|---:|---|---:|
| PR905 | 127 | (1,0,1,0,0,2,0,0) | 32 |
| PR906 | 125 | (0,2,0,0,0,0,0,1) | 9 |
| PR906 | 125 | (0,1,1,0,0,0,0,1) | 9 |

The residual counts are 4 for `G3.11.8ae96830fd21`, 96 for `G3.11.cce6e3ba4eeb`, 0 for retained `G3.11.ea6bced3bddf`, and 78 for `G3.21.d610e381ed75`. Index127 has three remaining source tuples, each with 32 necessary pairs. No double cuts occur; any later index125 label closure must remove zero additional pairs.

## Exact proof scope and assumptions

[PR905 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/2db172b32dc014c06521a3fcba20261db5bb00fa/research/hm/profile11-source127-acff-exclusion/PROOF.md) uses the original actual saturated full-span source, zero-defect actual Gauss quotient, strict-top lemma, and original catalogs. It does not rely on partial PR901. Strict-top forces the high-only D block; all invariant-divisor possibilities are excluded. The unique kernel O(-6)+Wp(-5)+O(-10) has exactly four saturated internal images, including an arbitrary scalar multiplicity line in two O(-10) targets. The positive-degree first spans are impossible. The constant seven-space branch and the constant-A/linear-T branch both capture the actual saturated high quotient before projection. In the latter, the allowed Wp(-3) injection into T(-1) is retained: its actual coefficient span V gives the contradiction, not false whole-source Hom vanishing or a presumed horizontal splitting.

[PR906 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/d679aa09811f821505254572a51e65b2904d03c9/research/hm/profile11-source125-bb-bc-exclusion/PROOF.md) forces an actual constant A from the positive preimage's Euler character. Its high map is onto. The rank-two kernel alternatives include W(-9), Wp(-9), and all four scalar pairs; the character-compatible (8,10) pair is excluded by its actual injection into A. The scalar O(-10) tail remains through every projection. Genuine constants of R are exactly P, and the possible linear T top is excluded using the negative-only residual target. For bc, a nonzero quartic component induces a genuinely nonzero cohomology map by Serre duality, while a zero component preserves the actual quartic summand. These lead respectively to P(-2)+T(-3) and (V+P)(-2)+V(-4), with the scalar retained. The quadratic increment gap and complete-Sym6 coherent-image obstruction close both alternatives.

The pinned reviews bind the exact proof SHA-256 values. PR906's universal dependencies are PR882 at `ef8ed8d457494608472a2c07de776e9162b2c20f` and PR875 at `01f835fda6e771351555f0af1fa11647c27eb01e`, already authenticated by the predecessor chain; both proof hashes are checked against the new review. The four original inputs are at `db51525015bb7c5e825833d550d08dedf6f6ea96`: actual presentation blob `b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3`, strict-top blob `d7506dae49b4be43230450c4132bd5db91f137ef`, source catalog blob `fe0afa410d89340d3082dc814277f89fbb582c19`, and stable-label catalog blob `8b5971092f9ef762584912609fd5e9301c4e271d`.

## Replay and boundary

Run in the campaign directory, with all predecessor files unchanged:

```sh
python verify_source_frontier_through906.py
python -O verify_source_frontier_through906.py
python -m unittest test_source_frontier_through906 -q
python -m unittest discover -p 'test*.py' -q
```

Result: 23 new regression tests, 292 total tests pass. Runtime checks remain active under `-O`. The verifier authenticates exact proof/review bytes and immutable predecessor JSON, matches both original coefficient tuples and decoded degree/irrep multisets, verifies original endpoints and defect, and checks disjoint pair partitions. Tests reject omitted branches, false channel vanishings, duplicate cuts/pairs, wrong endpoints/blocks, and premature label deletion; arbitrary catalog renumbering preserves the accounting.

This is finite accounting conditioned on the pinned written mathematical proofs, not a formal proof checker or a realization theorem. PR869's abstract 8ae family and PR876's abstract c-d-f family remain unchanged and are neither excluded nor claimed realized. No actual-source coefficients, parameters, points, derivatives, matrices or instance ranks are evaluated. All later results and whole-label exhaustion are deferred.

## New publication files

- SOURCE-FRONTIER-THROUGH906.md
- frontier-source-through906.json
- source-pins-source-through906.json
- verify_source_frontier_through906.py
- test_source_frontier_through906.py
- inputs/pr905_proof.md
- inputs/pr905_review.md
- inputs/pr905_original_strict_top.md
- inputs/pr906_proof.md
- inputs/pr906_review.md
