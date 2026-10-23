# Source frontier through PR917

This checkpoint appends PR917's original-source127 a-b-c-f exclusion to the
unchanged through911 checkpoint. It preserves historical results rather
than overwriting them.

| Stable label | Remaining necessary pairs | Remaining source |
|---|---:|---|
| G3.11.8ae96830fd21 | 4 | Original E10 source |
| G3.11.cce6e3ba4eeb | 32 | c-d-f only |
| G3.21.d610e381ed75 | 78 | 13 source tuples,6 pairs each |
| Total | 114 | 3 labels, profile counts2/0/1 |

The previous146 pairs partition into114 survivors and32 newly excluded
pairs. The exact IDs are in the JSON ledger. No stable label is newly
excluded. Relative to the fixed campaign805 baseline,1676 of1790 necessary
pairs and14 of17 labels have been removed. These are finite ledger counts,
not a percentage of proof completion or of all mathematical possibilities.

## Reproduce

Place these append-only files alongside the existing through911 chain.

```sh
python3 verify_source_frontier_through917.py
python3 -m unittest test_source_frontier_through917
python3 -O -m unittest test_source_frontier_through917
```

The verifier replays the predecessor, authenticates source files and six
proof dependencies, matches the source by its tuple and block multiset,
and computes the exact disjoint set difference. The independent review
records the mathematical scope. The inherited actual-instance and formal
verification boundaries remain unchanged. No experiment was restarted.
