# Close only the original index113 label gate

PR884 at **75d3a9bb5287ddc3dc22bf4651602b257d6507fb** closes the complete original ten-source gate for G3.11.ad509d55173f. This separate certificate changes **five registered labels to four**, profiles **3/0/1**. The necessary-pair total remains **351**: the last17 index113 pairs were already removed by PR881 in the through882 source record. Additional pair cuts here are **zero**.

The through877 and through882 snapshots remain unchanged, including their historically closed label gate. The stage sequence is:

- published PR863 baseline: five labels,501 pairs;
- through877 source cuts: five labels,377 pairs;
- through882 source cuts: five registered labels,351 pairs, index113 relation empty;
- through884 original-universe certificate: four labels,351 pairs.

Remaining labels and necessary pairs: G3.11.8ae96830fd21=4, G3.11.cce6e3ba4eeb=224, G3.11.ea6bced3bddf=45, G3.21.d610e381ed75=78. Their records are copied unchanged.

## Independent exact coverage reconciliation

The proof and independent review were read at the immutable commit. Both original catalogs at db51525015bb7c5e825833d550d08dedf6f6ea96 were independently matched to the stable label, index113, defect zero and A=(-10,2,16), B=(-18,-4,8). The original ordered list, not the empty filtered relation, is exactly ff,ef,ee,cf,ce,cc,bf,be,bc,bb. Every tuple is decoded into its full degree/irreducible block multiset.

The two direct exclusions are ee and cc: the original strict-top target is A+V+2P+2D; their top coefficients are respectively3P and2V+P. A separate integer McKay recurrence in this verifier checks the target decomposition. It is fixed universal representation arithmetic, not an actual source computation.

The eight whole-source rows are ff→PR848; ef/ce/be→PR846; cf→PR861 plus PR868; bc→PR874; bb→PR877; bf→PR881. The seven exact theorem documents, including the essential PR861 divisor0 dependency, match both their prior locally authenticated blobs and the new PR884 theorem manifest byte-for-byte. Full source scopes were rechecked: PR848's conditional index127 branch is not imported; PR846's three distinct index113 rows each exhaust their internal images; PR868 uses both divisor alternatives only with PR861; PR874/877/881 include every divisor/kernel/internal-image case and establish saturation before the terminal obstruction.

`source-pins-through884.json` authenticates the new proof, review, coverage and theorem-byte manifest. `complete_original_source_coverage` records every exact original tuple, decoded blocks and case obligation. The code checks finite coverage and accounting; geometric arguments remain the pinned written premises. It does not certify Lean, reconstruct underlying HM inputs or infer realization from nonempty relations.

PR869 and PR876 remain explicit nonempty abstract-family boundaries. Neither source2 nor8ae nor the remaining index125/index127 rows is closed. Later results are deferred. No production experiment, actual-instance coefficient/point/derivative/matrix/rank evaluation or external publication is performed.

## Reproduce

Using the unchanged predecessor stack and Python standard library:

```sh
python3 verify_source_frontier_through877.py
python3 verify_source_frontier_through882.py
python3 verify_frontier_through884.py
python3 -O verify_frontier_through884.py
python3 -m unittest test_source_frontier_through882 test_frontier_through884 -v
python3 -m unittest discover -p 'test*.py' -q
```

The new gate verifier's `--write` regenerates only `frontier-through884.json`. The13 new gate tests reject missing/duplicate original tuples, wrong source lemmas, missing divisor dependencies or branch scope, nonempty uncharged relations, and any extra label/pair change. The shared source package adds22 tests. All210 stack tests pass.
