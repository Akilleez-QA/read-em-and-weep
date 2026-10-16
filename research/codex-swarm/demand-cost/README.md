# CO01 bounded demand/cost preflight

Run from the repository root:

```sh
timeout 25s python -B research/codex-swarm/demand-cost/preflight.py
timeout 25s python -B -m unittest discover -s research/codex-swarm/demand-cost -p test_producer.py
timeout 25s python -O -B -m unittest discover -s research/codex-swarm/demand-cost -p test_producer.py
python -B research/codex-swarm/demand-cost/run_bounded.py
```

The CLI uses only stdlib, caps address space at 256 MiB and CPU at 15 seconds, bounds each input at 4 MB and grammar at 20,000 nodes, and uses read-only `git show` with ten-second timeouts. The outer timeout bounds wall time. No model/compiler imports, polynomial expansion, physical coefficient extraction, witness search or rank run occur. Tests use tiny synthetic DAGs and pinned metadata only. `request-report.json` is deterministic; stdout from the first command reproduces its bytes. The pins hash the current consumed request, compiler_v5 and ledger-preflight metadata plus exact PR79 proof/code bytes obtained through `git show`. Pin drift fails closed. They do not authenticate a current global ledger or prove source equations.

`run_bounded.py` applies these resource limits to both test modes too, checks byte reproduction, and records wall times plus Linux maximum child-process RSS in `run-receipt.json`. The observed maximum was 21,600 KiB; that metric is the largest individual child, not summed concurrent RSS. Each observed command completed below 0.07 seconds. Replays update the timing receipt and test logs, so a reviewer should compare deterministic report bytes separately from the delivery hash marker.

Optional producer handoff:

```sh
timeout 25s python -B research/codex-swarm/demand-cost/preflight.py --grammar /path/to/grammar.json --evidence /path/to/unverified-metadata.json
```

A grammar object has schema `co01-demand-grammar-v1`, `nodes` and `entries`. Each node has exactly `id`, `map` (`i`,`b`), `coordinate` (four Laurent exponents), `owners` (ordered five-integer tuples), `source_branch_id`, `frame`, `op`, `inputs` (earlier node IDs). Supported formal operations are leaf/add/multiply/differentiate/contract/transport; only leaf has no inputs. Every reference must have the identical complete scope. Each entry has exactly `map`, `coordinate`, `roots` and covers one of the 121 requested map/coordinates. All must be present once; roots retain the multiplicity of source summands. Distinct source branches/owners use separate nodes. This intentionally restrictive interface may forgo legitimate reuse: a broader sharing theorem would require separate review. Submitted grammar semantics remain unverified and never open admission.

Current result: 32 weighted requests, 20 maps, 127 terms, 121 map/coordinate demands, six repeated uses, absolute weight sum 149. Full-owner/source-branch traversal, physical arithmetic, occupied support and peak physical storage remain UNKNOWN pending the actual grammar and proofs. See `PROOF.md` for the partition/count argument and the retained complete-B/first-prism/second-prism formula. `producer-ready.json` hashes the producer deliverables, excluding itself and independent-review files. It means ready for review, not accepted mathematical results or execution permission.

`test_independent.py` and `review-independent.md` are reserved for the distinct root reviewer and are intentionally absent. No files in scalar-compiler/, transport-binding/ or whole-source-clearing/ are edited. Their actual source certificates remain required dependencies, rather than inferred from directory names or producer status markers.
