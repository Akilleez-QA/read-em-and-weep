# Source checkpoint through PR839: whole-label gate held closed

## Exact relation result

The recorded necessary relation decreases from **810 to 759 pairs**:

- Split `G3.11.863639aa192e`, bb: 19 pairs removed, leaving bf/bc with 38 pairs.
- Balanced `G3.11.73682b4c817f`, bb: 16 pairs removed.
- Balanced `G3.11.73682b4c817f`, bc: 16 pairs removed.

The balanced label's recorded relation is now empty. This checkpoint deliberately distinguishes **nine registered labels**, profile counts **8/0/1**, from **eight labels with nonempty recorded relations**. It records **no newly adjudicated whole-label exclusion**. An empty retained relation is not silently substituted for the separately required full-exhaustion theorem.

## Complete source-branch coverage

Split bb:

- PR814's separate rank-one-top exclusion rules out generic rank one.
- PR821 Section5 rules out split-target rank-two torsion, so the top is onto.
- PR836 excludes both onto constant-span alternatives.

Balanced bb:

- Strict-top rules out rank zero.
- PR814's separate rank-one-top exclusion rules out generic rank one.
- PR836 excludes the onto branch only.
- PR819 forces every rank-two non-onto branch to have exactly length-twelve defect; PR838 excludes that branch.

Balanced bc:

- Strict-top rules out rank zero.
- PR814 excludes rank two.
- PR839 excludes rank one, including both lower-T quotient-channel cases and the defective intermediate image.

None of PR836, PR838 or PR839 alone is promoted beyond its stated scope. The new verifier checks all required cases and pinned dependencies; tests explicitly reject onto-only balanced-bb coverage and rank-one-only balanced-bc coverage.

## Independently checked original tuple coverage

The original public `one-one-endpoint-necessary-pairs.json` was fetched at commit `db51525015bb7c5e825833d550d08dedf6f6ea96`. Its exact Git blob is `fe0afa410d89340d3082dc814277f89fbb582c19`; its bytes are included in `inputs/original-one-one-pairs-db515250.json`.

Entry72 has defect zero and the correct A/B targets. Its ten tuples are exactly a=d=g=0, h=1, b+c+e+f=2. The artifact records all ten full tuples and source block multisets, including repeated blocks.

Against the historical PR796 relation:

- ff, ee and cc were already absent, contributing zero pairs. Their absence is not recounted as a new result.
- ef, cf, ce, bf, be, bc and bb each had sixteen historical pairs, totaling 112.
- Earlier source checkpoints removed ef/be/ce via PR814, cf via PR828, and bf using PR814+819+823.
- This checkpoint removes the final sixteen bb and sixteen bc pairs.

This verifies the complete original **tuple list and its relation accounting**, not the missing independently published mathematical exhaustion theorem. The whole-label gate has two separate conditions: original tuple coverage is now independently checked; the immutable full-exhaustion publication remains unverified and absent. The gate stays closed until that publication is pinned and its scope checked. No production exhaustion proof is duplicated here.

## New immutable sources

- PR836: `c6b6ec427e5690055c18c181fad39efd6624cc83`, `research/hm/profile11-onto-bb-exclusion/ONTO-BB-SOURCE-EXCLUSION.md`.
- PR838: `8b9e7affe6906ead2927fb251e6b64b886020030`, `research/hm/profile11-balanced-bb-torsion-exclusion/BALANCED-BB-TORSION-DESCENT-EXCLUSION.md`.
- PR839: `5951b547d07afe052bc6f823a3ac2b5f29963114`, `research/hm/profile11-balanced-bc-exclusion/BALANCED-BC-BACKWARD-EXCLUSION.md`.
- PR814 separate rank-one proof: `1f94be65b3a470a1b594e61d56df7f6057c9d907`, `research/hm/profile11-low-positive/RANK-ONE-TOP-EXCLUSION.md`.

The new manifest is SHA256-pinned and every proof is checked by Git blob hash. Existing PR814/819/821 proof copies and previous snapshots are rechecked through the verifier chain. All public URLs are retained in the artifact. The through834 snapshot published in PR837 at `cf17981333f34548226d87c7146a78167d44ac04` remains unchanged.

## Reproduce

```sh
python verify_source_frontier_through839.py
python -m unittest test_frontier test_frontier_through804 test_frontier_through806 test_source_frontier_through823 test_source_frontier_through828 test_source_frontier_through834 test_source_frontier_through839
```

All 81 cumulative tests pass, including 12 new tests. Optimized Python replay passes. `--write` regenerates only the new checkpoint. The tests cover the label gate, exact original ten-tuple coverage, missing branch cases/dependencies, catalog renumbering, duplicate cuts, historical snapshot preservation and untouched labels.

## Limits

Source types are matched by full block multisets and multiplicity tuples, never arbitrary catalog numbers. Existing paired witnesses are filtered; their survival is not realization. No actual coefficient, matrix, point, derivative or rank is evaluated. No production proof or independent proof review is duplicated, and no consumed experiment is rerun. Pinned written mathematical claims remain assumptions of this bookkeeping verifier.

Artifact SHA256: `daf5e3724ce2086d559da081155166680ed5024cf865a04d03650c96df9722e2`.
