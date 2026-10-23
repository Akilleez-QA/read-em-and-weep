# Append-only frontier checkpoints through PR806

## Results and exact scope

The historical `frontier.json` remains unchanged: 17 labels, profiles 16/0/1, and 1,790 baseline paired witnesses. It was published in PR805 at commit `d79b4ed8263076476296066def7f0c5be7752707`.

Two separate executable checkpoints extend its exclusion ledger:

- `frontier-through804.json`: 12 labels, profiles **11/0/1**, exactly **1,319** baseline paired witnesses.
- `frontier-through806.json`: 9 labels, profiles **8/0/1**, exactly **1,004** baseline paired witnesses.

These are exact restrictions of the existing PR796 paired-witness relation to surviving stable IDs. They are not new realizability results. No newer geometry on surviving source edges is asserted fully encoded. The written geometric exclusions are pinned inputs, not proof-assistant-certified by these scripts. No proof review, original enumeration, consumed experiment, source-instance evaluation or external write is performed.

## Reproduce

From this directory:

```sh
python verify_frontier.py
python verify_frontier_through804.py
python verify_frontier_through806.py
python -m unittest test_frontier test_frontier_through804 test_frontier_through806
```

All 31 tests pass. The verifiers also pass under optimized Python (`python -O`). Each verifier supports `--write` to regenerate only its own JSON artifact. The later verifier checks the earlier snapshots' exact SHA256 hashes before extending them. Ordinary verification is read-only apart from Python's optional bytecode cache.

The inputs are included locally and require no network or third-party packages. Each new public proof is verified by SHA256 and Git blob SHA1; the pin manifests themselves are hash-checked. References are recorded in `source-pins-through804.json` and `source-pins-through806.json`.

## New disjoint cuts

1. PR802, `e484640a6565c278321bf6557860262c1ac1b7df`, excludes `G3.11.16ee1aa30a9c` and `G3.11.db4688c30472`. Removes 147 + 294 = 441 baseline pairs. Labels: 17 -> 15.
2. PR803, `68bb934a4fb7b059168d4081763a274e651c3a0b`, excludes `G3.11.cb71f599859d` and `G3.11.0fe2a757439f`. Removes 9 + 9 = 18 baseline pairs. Labels: 15 -> 13.
3. PR804, `ae34a9403c0c2abf00516ca35dd494723034c38a`, excludes `G3.11.64d33b6d4139`. Removes 12 baseline pairs. Labels: 13 -> 12.
4. PR806, `85a5cf8ac3a35c3ff173f544d2fcde6f2a7c893b`, excludes `G3.11.1e318198128e`, `G3.11.6795493ae8cd` and `G3.11.a5d4e292b34e`. Removes 27 + 96 + 192 = 315 baseline pairs. Labels: 12 -> 9.

Thus 1,790 - 441 - 18 - 12 = 1,319 and 1,319 - 315 = 1,004. The full cumulative label sequence is 23 -> 22 -> 20 -> 19 -> 17 -> 15 -> 13 -> 12 -> 9. All 14 exclusions since the 23-label checkpoint are distinct. Historical source-edge cuts remain separately classified and are never subtracted again as label cuts.

The final checkpoint stops at PR806. It does not silently include any later publication. The remaining source2 label is untouched. Neither SF>=4, square rank>=28, higher lifting, algebraicity nor global proof completion follows.

## Snapshot hashes

- Historical17: `3315d80f651911f87e8b12006263994cd591a4b5938e621fcf6bda111332b77c`
- Through804: `2a927b6606ec43d2b6f39a5992e4f8bc38829f09cd03842d6afcf29c60e83bca`
- Through806: `4100c591275feae312a0182511337cf4b4131901730932366bbe68ea3dcf9bbc`

## Surviving stable IDs through PR806

- `G3.11.4b6dad66f329`
- `G3.11.73682b4c817f`
- `G3.11.863639aa192e`
- `G3.11.8ae96830fd21`
- `G3.11.ad509d55173f`
- `G3.11.cce6e3ba4eeb`
- `G3.11.dc58cc54f352`
- `G3.11.ea6bced3bddf`
- `G3.21.d610e381ed75`
