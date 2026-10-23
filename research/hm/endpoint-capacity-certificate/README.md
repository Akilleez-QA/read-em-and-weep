# Two-height endpoint capacity certificates

A self-contained integer optimizer and independent constant-candidate certificate verifier. See [PROOF.md](PROOF.md) for hypotheses and exact scope.

Run with Python 3 and the standard library only:

```sh
python verify.py > result.normal.json
python -O verify.py > result.optimized.json
cmp result.normal.json result.optimized.json
cmp RESULT.json result.normal.json
```

`capacity.py` exposes `solve`, `verify`, `classify_degree`, and `equality_filter`. The last operation requires separately proved actual top-image flags and exact attainment of the unfiltered capacity. It never replaces or lowers that capacity.

`RESULT.json` records 62,442 passing checks, including four huge-integer certificates and four already-known PR1138 regression examples. `INPUTS.json` pins the motivating public proof. The arithmetic theorem is self-contained and does not import its geometric conclusions. No proof repair completion, new actual-source cut, profile coverage, or selected instance computation is claimed.
