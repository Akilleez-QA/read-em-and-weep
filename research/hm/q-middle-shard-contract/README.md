# q-middle shard contract

This package prepares receipt accounting for the pinned55 harmonic and10
trace coefficient maps. It contains no mathematical shard runner and does
not import the symbolic payload. Its execution lock remains disabled.

Place it at `research/hm/q-middle-shard-contract`, next to the PR810 payload
at `research/hm/q-middle-candidate-interface`. The metadata tools require
Python3.9 or later and only the standard library; SymPy is not needed.

From the repository root, run the synthetic receipt fixtures:

```sh
python3 research/hm/q-middle-shard-contract/test_receipts.py
```

To test relocation, explicit payload selection and deterministic catalogue
reconstruction using read-only byte/AST inspection:

```sh
python3 research/hm/q-middle-shard-contract/test_portability.py \
  --payload research/hm/q-middle-candidate-interface
```

To write a new catalogue, provide both paths explicitly. Relative paths are
resolved from the caller's working directory; the output parent must exist.
This example leaves the checked-in contract and disabled lock untouched:

```sh
mkdir -p work/q65-readiness
python3 research/hm/q-middle-shard-contract/q65_shards.py catalogue \
  --payload research/hm/q-middle-candidate-interface \
  --output work/q65-readiness/catalogue.json
```

`CONTRACT.json` records65 stable map IDs and8 required global IDs. Its
semantic contract digest is
`234140e8bb0eacf6e28fd015a73235265570e5dfece824eedb0d81d628d57727`.
The frozen input bundle digest is
`54b29708fbba70be9f25ef150b17db4c8d7a232d342602dcf404f11ace4bf7d8`.

For a future independently reviewed run, the accounting command is
`q65_shards.py aggregate CONTRACT.json EXECUTION_LOCK RECEIPT...`.
It verifies log bytes and final markers, rejects missing/duplicate units and
requires the reviewed initializer/helper-coverage/runtime pins. The shipped
`execution-lock.json` cannot authorize aggregation of a production run.
Relative log paths are resolved beside each receipt. Do not substitute
synthetic fixtures or inherited log lines for real execution receipts.

Read [SHARD-CONTRACT.md](SHARD-CONTRACT.md) for all per-map/global checks,
the minimal initializer API, the proposed bounded adapter, and evidence
limitations. The inherited log in `evidence/` ends after27 harmonic maps,
with zero trace checks and no process-exit receipt. Metadata fixture success
is not mathematical verification of any coefficient map.
