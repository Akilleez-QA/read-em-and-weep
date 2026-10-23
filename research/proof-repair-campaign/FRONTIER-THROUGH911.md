# Final bounded reconciliation: source125 gate closed

**Three labels remain, profiles 2/0/1, with 146 historical necessary pairs.** PR911 closes only `G3.11.ea6bced3bddf` (original index125). Its relation was already empty at through906, so this gate removes **zero additional pairs**. Through907 remains a distinct, unchanged four-label/146-pair source checkpoint.

## Exact exhaustion and provenance

[PR911](https://github.com/Akilleez-QA/read-em-and-weep/blob/64945ab759c313f1aa35611f91236ee7deb387dd/research/hm/profile11-source125-label-exclusion/PROOF.md) and its exact-version review were read alongside the original ten-row universe. Ordered rows are ff, ef, ee, cf, ce, cc, bf, be, bc, bb. The tuple list, decoded degree/irrep multisets, original endpoints, defect zero and stable ID agree exactly with the original catalogs at `db51525015bb7c5e825833d550d08dedf6f6ea96`.

The original endpoint-necessity note, blob `dcacf0bcdef8377c1ed7654e5b82659ea409456e`, confirms the direction required for exhaustion: an actual source must appear in the necessary overlist. No sufficiency or realization inference is used.

The direct ff obstruction is D multiplicity two versus one in Sym6+Sym18=A+2V+3P+D, using strict-top on global sections, not fiberwise injectivity. The remaining nine rows use eight exact whole-source proof files: ee PR846, ef PR860, bf PR875, cf PR882, be PR887, ce PR893, cc PR895, and bb/bc PR906. Their exact commit/path/blob associations are checked against previously authenticated campaign pins, not accepted solely from the new coverage file. PR906's proof and review hashes are independently bound. Both bc quartic cases are covered; cc is not falsely attributed to strict-top alone. The precise scope obligations and complete source definitions are recorded in the JSON certificate.

Proof assumptions remain the actual saturated source and zero-defect Gauss quotient, characteristic-zero equivariant splitting and connection arguments. The executable authenticates and reconciles the written theorems; it does not formally prove their geometry.

## Remaining source relation

| Stable ID | Profile | Remaining source tuples | Necessary pairs |
|---|---|---:|---:|
| G3.11.8ae96830fd21 | 11 | 1 | 4 |
| G3.11.cce6e3ba4eeb | 11 | 2 | 64 |
| G3.21.d610e381ed75 | 21 | 13 | 78 |

For 8ae96830fd21 the sole tuple is (0,0,0,0,0,1,1,0), with 4 pairs. For cce6e3ba4eeb the remaining tuples are c-d-f=(0,0,1,1,0,1,0,0) and a-b-c-f=(1,1,1,0,0,1,0,0), with 32 pairs each.

The profile21 label retains the following thirteen tuples, each with six pairs:

```text
(0,0,0,0,0,2,0,1)
(0,0,0,0,1,1,0,1)
(0,0,1,0,0,1,0,1)
(0,1,0,0,0,1,0,1)
(0,0,0,0,0,1,1,0)
(0,0,0,0,1,0,1,0)
(0,0,1,0,0,0,1,0)
(0,1,0,0,0,0,1,0)
(0,0,1,1,0,1,0,0)
(1,0,1,0,0,2,0,0)
(1,0,1,0,1,1,0,0)
(1,0,2,0,0,1,0,0)
(1,1,1,0,0,1,0,0)
```

These are sixteen label-specific source edges, not sixteen distinct coefficient tuples. Excluding a tuple at source127 does not exclude the same tuple at source2. The full pair lists and decoded multisets are in `frontier-through911.json`.

## Fixed campaign805 comparison and burn boundary

The unchanged historical campaign805 fixture has 17 labels, profiles16/0/1, and 1790 necessary pairs. The final checkpoint has 3 labels, profiles2/0/1, and 146 pairs: **14 label exclusions and 1644 necessary-pair removals**. Exact final pairs are checked as a subset of that original relation. This is an approximately 82.35% label reduction and 91.84% reduction of this fixed necessary relation, not a probability of success or proportion of the mathematical proof completed.

The final bounded stack is deliberately separate:

- Through906, published PR910: 228 → 178 pairs, four labels retained; source125 gate held.
- Through907: 178 → 146 pairs, four labels retained; accf source edge excluded with the coherent divisor-twelve image preserved.
- Through911: 146 → 146 pairs; source125 original ten-tuple gate closes, four → three labels.

PR869 and PR876 establish nonempty abstract families in the 8ae and c-d-f lanes, not actual HM realizations and not exclusions. Those boundaries are preserved. The profile21/source2 lane is not closed. No global rank-four, section-count, smoothing, realization or formal-proof conclusion follows. The remaining work cannot be replaced by repeated numerical failure or by treating partial branch restrictions as whole-source exclusions.

This reconciliation ends at PR911. No new production research, actual-instance evaluation, consumed experiment rerun, or external publication was performed.

## Reproduction and regressions

```sh
python verify_frontier_through911.py
python -O verify_frontier_through911.py
python -m unittest test_frontier_through911 -q
python -m unittest discover -p 'test*.py' -q
```

23 new gate tests; **339 total tests pass**. Normal and optimized verifiers pass. Regressions cover missing/duplicate/reordered tuples, wrong multisets/endpoints/labels, altered or conditional dependencies, bb/bc review mismatch, missing branch scope, hidden uncharged pairs, repeated label closure, baseline accounting and untouched residual rows.

## New files

- FRONTIER-THROUGH911.md
- frontier-through911.json
- source-pins-through911.json
- verify_frontier_through911.py
- test_frontier_through911.py
- inputs/pr911_proof.md
- inputs/pr911_review.md
- inputs/pr911_coverage.json
- inputs/pr911_original_endpoint_necessity.md
