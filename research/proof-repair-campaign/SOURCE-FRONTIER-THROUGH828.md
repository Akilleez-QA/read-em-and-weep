# Source-edge checkpoint through PR828

## Exact result

`frontier-source-through828.json` extends, rather than replaces, the through823 checkpoint. All nine original stable labels remain, with profiles **8/0/1**. The exact retained necessary witness relation has **840 pairs**, down from 980 by **140 distinct pair deletions**.

These counts describe formal necessary pairs from the pinned historical relation. They do not assert realizability, exhaust every current geometric condition, or establish any whole-label exclusion or global rank theorem.

## Append-only accounting

The previously deferred complete PR814 source cuts remove:

- Split `G3.11.863639aa192e`: ef and be, 19 pairs each.
- Balanced `G3.11.73682b4c817f`: ef, be and ce, 16 pairs each.
- PR814 subtotal: 86 new pair deletions.

PR826 excludes split ce, removing 19 pairs.

PR828 excludes cf in both labels, removing 19 split pairs and 16 balanced pairs, subtotal 35. PR828 also independently excludes split ce, but that exact source edge has already been removed under PR826. Its second proof is recorded as corroboration with **zero additional deletion**, not counted twice.

Thus `980 - 86 - 19 - 35 = 840`.

The surviving low-positive source sets are checked by their exact multiplicity tuples:

- Split label: bf, bc, bb; 57 pairs.
- Balanced label: bc, bb; 32 pairs.

The other seven labels and every pair on them remain unchanged. The earlier singleton E10 source on `G3.11.8ae96830fd21` still has its four necessary pairs. Historical through806 had 1,004 pairs, so the two source checkpoints together remove 164 distinct pairs.

## Exact sources and matching

PR814 remains pinned at `1f94be65b3a470a1b594e61d56df7f6057c9d907`; its complete source-exclusion scope was read directly from its included proof, not inferred from its conditional branch results.

New immutable proof pins:

- PR826: `96734783c561c2baca8f91d69772318446898f06`, `research/hm/profile11-split-ce-constant-span-exclusion/SPLIT-CE-CONSTANT-SPAN-EXCLUSION.md`.
- PR828: `ae077cbe42d65cde27d65ce88923dc35851b6952`, `research/hm/profile11-horizontal-quotient-exclusion/HORIZONTAL-CONSTANT-QUOTIENT-EXCLUSION.md`.

Their public URLs and Git blob identifiers are in `source-pins-source-through828.json`. Both proof copies are included under `inputs/`. The manifest is SHA256-pinned and the proof bytes are verified by Git blob hashing. All earlier dependencies are checked through the previous verifier chain.

Source matching requires agreement of the complete degree/irreducible block multiset and source multiplicity tuple. Repeated P blocks in ef/ce/be are preserved. Local E numbers are references only; permuting all catalog IDs preserves the result. Existing correlated pairs are filtered without Cartesian completion.

## Reproduce

```sh
python verify_source_frontier_through828.py
python -m unittest test_frontier test_frontier_through804 test_frontier_through806 test_source_frontier_through823 test_source_frontier_through828
```

All 56 cumulative tests pass, including 12 new tests. Replay also passes with `python -O`. `--write` regenerates only `frontier-source-through828.json`. The prior through823 checkpoint is hash-checked and unchanged.

New tests include overlap deduplication, duplicate-cut rejection, conditional-cut rejection, source catalog permutation, block multiplicity, already-absent edges contributing zero new cuts, preservation of untouched labels and pair holes, and exact low-positive source sets/subtotals.

## Remaining limits

Other O26 divisor conditions, bc branch restrictions and bb subsystem classifications remain explicitly unencoded where they do not exclude an entire source edge. The old cf/split-ce forced-system entries and deferred complete PR814 cuts are marked resolved by omission from the new unencoded ledger; their historical descriptions remain intact in the previous checkpoint.

No production proof or proof review is duplicated. The written geometric theorems are explicit input assumptions of this finite bookkeeping verifier. No actual-source coefficients, points, matrices, derivatives or ranks are evaluated, and no consumed experiment is rerun.

Artifact SHA256: `22583c253816f9ef9e6a45a525dd10869870c45d1277fe184e102839e6a1755c`.

## Later publications explicitly deferred

This checkpoint stops at PR828. The following later results have been reported but are not fetched, verified or encoded by this checkpoint:

- PR829, `5e713ff925335b7fb08b5a5768fb558e81fc3575`: reported O26 U6 exclusion at source index112 and U6/U13 exclusions at index115. These require a separate pinned-scope and existing-edge intersection before changing any count.
- PR830, `620d5598ccc19e5e1c458a4cddb0d3a0709d83c3`: reported split-bf rank-two top restriction. The rank-one branch remains; this must not be treated as an entire bf source exclusion.

No pair is removed here on the basis of either report. The preceding through823 snapshot was published in PR832 at commit `84c46ecf5ba3b29d27fedad7a036a7c6402a9053`; this extension preserves its exact local bytes.
