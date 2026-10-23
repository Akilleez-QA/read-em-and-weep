# Source-edge checkpoint through PR834

## Result

The exact necessary pair relation decreases from **840 to 810**. All **nine stable labels** remain, with profile counts **8/0/1**. No whole-label exclusion or realization is inferred.

The three O26 labels now have one source type each:

- `G3.11.dc58cc54f352`: matching E6, three pairs; top-divisor degrees 0 or 20 remain possible.
- `G3.11.4b6dad66f329`: matching E13, three pairs; top-divisor degrees 0 or 20 remain possible.
- `G3.11.8ae96830fd21`: E10, four pairs; top system must be basepoint-free.

These are necessary source restrictions, not constructions of the sources or certification of either surviving divisor stratum.

## Disjoint accounting and complete scope

PR829 removes U6 on dc58 and U6/U13 on 4b6d: three pairs each, subtotal nine. PR834 removes E3 on dc58 and E3/E12 on 4b6d: three pairs each, subtotal nine.

Four older source edges were still present in the through828 relation. They are now removed only after explicitly completing all cases:

1. dc58/E0: PR817 Section7 excludes divisor0. PR813 excludes divisor12 for all sources; its divisor20 theorem allows only the matching P+D sources, not E0's P+2D top.
2. 4b6d/E10: the same complete divisor coverage, with its divisor0 exclusion supplied separately in PR817 Section7.
3. 4b6d/E0: PR817 Section7 explicitly states that, even before internal-image analysis, only the single O(-10) source can map to W O(-9). A line cannot surject onto that rank-two negative quotient. This is independent of the top divisor.
4. 4b6d/E6: PR813 Section3 gives the identical explicit source/negative-target mismatch for E6, reused in Section7. Again the degree argument has no top-divisor hypothesis.

Each older edge contributes three additional deletions, subtotal twelve. Thus `840 - 9 - 9 - 12 = 810`. No targeted edge was already absent; no deletion is counted twice. Every pair outside dc58 and 4b6d is unchanged, including the four E10 pairs on 8ae9 and all split-bf pairs.

The machine-readable coverage certificates retain the alternatives {0,12,20}, the exact source-dependent arguments, and their pins. Exact scope quotations from PR813/817 are checked against the pinned proof bytes. Tests reject missing divisor cases, missing dependencies and attempts to promote a conditional branch to a whole-source cut.

## Immutable dependencies

New proofs, included byte-for-byte:

- PR829, `5e713ff925335b7fb08b5a5768fb558e81fc3575`, `research/hm/profile11-o26-two-p-polar-exclusion/PROOF.md`.
- PR834, `71e3d3671474e2990c55ee67fec6d2c65e288649`, `research/hm/profile11-o26-vpd-polar-exclusion/PROOF.md`.

Earlier case-completion proofs:

- PR813, `3f99ecf539a3a3da61743df0dff409e54270c865`, `research/hm/profile11-o26-divisor-reduction/PROOF.md`.
- PR817, `a0b7cbd7a53c1603f284cf0e1a29fff106d02cb3`, `research/hm/profile11-o26-basepoint-free-top/PROOF.md`.

The verifier checks the new SHA256-pinned manifest and all four proof Git blobs. Public commit/path URLs are embedded in the output. Earlier snapshots and their inputs are verified through the existing replay chain. The through828 snapshot, published in PR833 at `226a27bf255cbeea3c3d057bf111fcf90597b7d1`, remains unchanged.

## Reproduce

```sh
python verify_source_frontier_through834.py
python -m unittest test_frontier test_frontier_through804 test_frontier_through806 test_source_frontier_through823 test_source_frontier_through828 test_source_frontier_through834
```

All 69 cumulative tests pass, including 13 new tests. Optimized Python replay also passes. `--write` regenerates only `frontier-source-through834.json`.

Complete block multisets and multiplicity tuples identify sources; local catalog numbers are never mathematical identities. Reindexing, repeated-block, duplicate-cut, already-absent-edge and untouched-label regressions pass. Existing correlated pairs are filtered rather than reconstructed as a Cartesian product.

## Boundaries and deferred work

PR830 at `620d5598ccc19e5e1c458a4cddb0d3a0709d83c3` is retained only as a reported, unencoded split-bf rank-two restriction. Its rank-one branch remains, so no whole bf source is removed. PR836 and later publications are not fetched or encoded. Other residual branch conditions are not declared fully encoded.

Pinned written mathematical theorems are assumptions for this finite accounting, not re-proved or independently reviewed here. No production proof is duplicated, no consumed experiment is rerun, and no actual-instance coefficient, point, matrix, derivative or rank is evaluated. Necessary witness counts do not prove realizability, SF>=4, algebraicity or the global research goal.

Artifact SHA256: `735b1f248e1acb067fc4f63b57f23be92293140dc607a59e4d7c18af189a9da9`.
