# Reproduction and publication boundary

This focused packet is stacked on `null/rankfour-adjacent-plateau` at `f20373720cfb785fe3d694f51e20efeb942fa45b` (#1175). All additions are under `research/hm/rankfour-short-cubic-plateau`.

## Exact conditional claim

The actual generic rank-four ordered maximal plateau `(1,3)` is impossible under the retained actual-geometric hypotheses and physical representation marking. This removes exactly one additional coarse necessary bin: 25 become 24. With the separate exclusions `(3,3)` in #1173 and `(2,3)` in #1175, no rank-four plateau with `l=3` remains in the established coarse overlist; remaining rank-four lengths satisfy `l<=2`. The preceding exclusions are not logical inputs to this proof.

All nine bad rank values 4 through 12 remain. No generic SF rank-at-least-five theorem, square-map surjectivity, full-adjoint invertibility, or original repair is claimed. The separate `(3,2)` profile remains an investigation, not an exclusion.

## Reproduce

From the repository root:

```sh
python3 research/hm/rankfour-short-cubic-plateau/verify.py > /tmp/rankfour-short-cubic-normal.json
python3 -O research/hm/rankfour-short-cubic-plateau/verify.py > /tmp/rankfour-short-cubic-optimized.json
cmp /tmp/rankfour-short-cubic-normal.json /tmp/rankfour-short-cubic-optimized.json
cmp /tmp/rankfour-short-cubic-normal.json research/hm/rankfour-short-cubic-plateau/RESULT.json
python3 research/hm/rankfour-short-cubic-plateau/independent/verify_review.py
```

All programs use only the Python standard library and resolve inputs relative to their own files. They run from an unrelated working directory. The independent package preserves its original hash inventory and all reviewed author bytes, and cross-compares all thirteen cubic candidates, quartic decisions, and four final residuals.

The author checker gives 1,250 checks and 81 rejected mutations. The independent checker gives 3,114 checks; the portable review executes 17 additional negative controls and six normal/optimized/alternate-directory replays. `independent/CONTROLS.json` is the exact expected replay output. The complete source texts are retained in each runnable package; repeated copies are byte-identical reproducibility inputs, not additional sources.

## Frozen identities

- Author proof SHA256: `7ec277448b80a3f77300e7c7802b7ea49ef0a742e8a652270f3af9a957010a92`.
- Independent review SHA256: `b8919e739a5d938d8494d8d29ae033e6256f6cf74a6925cbb81676dd52836313`.
- Independent manifest SHA256: `f6f73933b66297705e1ab02f22c81ea423990a6281e3bf535b29b898d56c7f4e`.

`MANIFEST.json` binds every other publication file by byte length, SHA256, and Git blob identity. The author proof, code, mathematical candidate data, results, public originals, and independent review package are unchanged.

The proof supplies the actual geometric steps. Hashes authenticate retained bytes, not the truth of all transitive premises. The arithmetic is not proof-assistant certification. No actual coefficients, parameters, jets, matrices, instance ranks, historical classification reruns, or local-model experiments are evaluated.
