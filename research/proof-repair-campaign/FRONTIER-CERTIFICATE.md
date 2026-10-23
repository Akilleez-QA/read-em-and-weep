# Campaign frontier certificate

This is a new executable dependency for planning parallel proof work. It composes the supplied 23-label frontier, the pinned PR796 source-pair certificate, and the immutable written label exclusions in PR798, PR799 and PR800. It does not relabel a review as new research.

## Reproduce without network or third-party packages

From this directory, run:

```sh
python verify_frontier.py
python -m unittest -v test_frontier
```

To regenerate the deterministic output, run `python verify_frontier.py --write`.
The verifier uses explicit checks rather than Python assertions, so optimized Python does not disable the validations. No original enumeration or consumed experiment is rerun.

## Exact result

- Label frontier: 17 labels, profile counts `(1,1)/(1,2)/(2,1) = 16/0/1`.
- Stable IDs are inherited unchanged from `inputs/quotient-frontier-23.json`.
- Pair relation: exactly 1,790 `(label,E_id,Q_id)` tuples, obtained only by restricting the prior 1,996 PR796 paired witnesses to these 17 labels.
- These tuples are necessary formal possibilities, not realizations. Newer geometry on surviving source edges has NOT been fully encoded. Neither SF>=4, square rank>=28, higher lifting, algebraicity nor global proof completion follows.

## Exclusion accounting

Full-label cuts are disjoint and counted once:

1. PR796 removes `G3.12.34bc2083d563`: 23 -> 22, profiles 19/2/1.
2. PR798 removes `G3.12.37914c53373c` and `G3.12.eed6acb13f3e`: 22 -> 20, profiles 19/0/1.
3. PR799 removes `G3.11.003c6b04f1cc`: 20 -> 19, profiles 18/0/1.
4. PR800 removes `G3.11.18ad6075be86` and `G3.11.86279023dea2`: 19 -> 17, profiles 16/0/1.

PR796's two source-edge restrictions remove 32 pairs on each of its two then-surviving profile-(1,2) labels. Those 64 source-edge removals are not two additional label exclusions. Its full-label cut removes a separate 78 pairs: 2,138 - 78 - 64 = 1,996. The later full-label cuts remove 32, 78 and 96 pairs respectively: 1,996 - 206 = 1,790.

The two exclusions already incorporated by the supplied 23-label frontier are recorded separately and are NOT subtracted again. The old 182-label baseline is historical context, not the executable starting set of this certificate.

## Trust and provenance boundary

`source-pins.json` identifies the exact public mathematical proof path, commit, URL and Git blob for each exclusion. All four proof texts are included byte-for-byte. `verify_frontier.py` pins each input by SHA256 and checks those proof Git blobs.

The supplied local `pr796-same-source-witness-intersection.json` is a derived prior certificate, not a newly retrieved public proof. Its exact bytes are pinned. Its upstream dependency hashes are retained in the output for provenance, but the old enumeration is not rerun here. The verifier replays PR796's constraints by full multisets of degree/irreducible blocks against the supplied relation, not by assuming PR catalog numbers are universal.

The written geometric theorems are explicit inputs. This verifier checks their finite consequences and bookkeeping, not proof-assistant correctness. It neither evaluates actual-instance coefficients, points or ranks nor assumes arbitrary abstract splittings carry the original connection.

## Regression coverage

Thirteen tests cover exact replay; duplicate cuts both across and within stages; source-edge versus full-label distinction; profile accounting at baseline and row levels; preservation of stable IDs; unknown cuts; E-catalog reindexing and block-order invariance; preservation of the correlated pair relation without Cartesian completion; duplicate pairs; inherited cuts; and per-stage arithmetic.

## Surviving stable IDs

- `G3.11.0fe2a757439f`
- `G3.11.16ee1aa30a9c`
- `G3.11.1e318198128e`
- `G3.11.4b6dad66f329`
- `G3.11.64d33b6d4139`
- `G3.11.6795493ae8cd`
- `G3.11.73682b4c817f`
- `G3.11.863639aa192e`
- `G3.11.8ae96830fd21`
- `G3.11.a5d4e292b34e`
- `G3.11.ad509d55173f`
- `G3.11.cb71f599859d`
- `G3.11.cce6e3ba4eeb`
- `G3.11.db4688c30472`
- `G3.11.dc58cc54f352`
- `G3.11.ea6bced3bddf`
- `G3.21.d610e381ed75`
