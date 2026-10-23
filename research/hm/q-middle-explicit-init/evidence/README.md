# Namespace evidence

These are publication derivatives of completed reviews and runs, plus portable
reviewer code. `PROVENANCE.json` binds the original bytes and explains each
relocation/sanitization delta. `MANIFEST.json` hashes every published package
file except itself. Original producer files remain unchanged in the working
record; the published README and receipt are documented derivatives.

`equivalence-success-receipt.json` and `namespace-smoke-success-receipt.json`
retain status, versions in associated stdout, exact input hashes, executable
hash, limits, enforcement caveats and resource measurements. Paths are replaced
by stable artifact roles and process identifiers are removed. A retained
`command_sha256` is the original command hash, not a hash of the sanitized
command display. Original receipt/stdout/stderr hashes are in PROVENANCE.

`FAILED-RUNS.json` preserves all three unsuccessful attempts, their original
artifact hashes and failure causes. The two reviewer attempts also pin every
original reviewer input snapshot. The successful run's original reviewer
scripts and pins are bound in PROVENANCE. No original failure artifact was
overwritten locally.

The static review describes the earlier static-only stage. The behavioral
review records the later completed namespace comparison. Neither certifies
sparse integration or q65 mathematics. The runtime comparison checked 150
outer and 32 nested names, 46 function bindings, 40 small probes, and two
sensitivity fixtures. The output inventory called `negative_symbol` belongs
to a deliberately rejected fixture.

## Portable verifier

`verify_namespace.py` accepts `--package DIR` and `--payload DIR`. With no paths,
the package is the parent of this evidence directory and the payload is its
sibling `q-middle-candidate-interface`. The two reference modules remain beside
the verifier with unchanged names and byte hashes, preserving their import
relationship. `--check-layout` verifies 84 pinned inputs and exits before any
symbolic import. The original guard also recorded the historical producer
receipt and guard itself; those remain historical provenance rather than
portable mathematical input dependencies.

Actual replay requires Python 3.12, SymPy 1.14.0 and mpmath 1.3.0. The reviewed
executable was Python 3.12.14; its exact hash is retained in the receipt. The
comparison program checks the Python minor version because AST serialization
differs across minors. A portable replay on a different patch/runtime is a
new run and must keep its own receipt.

Use the independently reviewed watchdog with SHA256
`6915a220408dc3bb5045b6cfaaaef8267a6516319cdb98deca5ba5717614c6fc`:

```sh
python3.12 -B research/hm/q-middle-explicit-init/evidence/replay_guarded.py \
  --guard path/to/reviewed/burn_guard.py \
  --python path/to/python3.12 \
  --out new-namespace-replay
```

The optional launcher verifies the guard and all 84 pinned inputs, includes the
portable reviewer inputs in the supervisor's hash records, and keeps default
60-second CPU / 75-second wall / 1.5-GiB sampled group RSS limits. It refuses
any existing output directory. It does not run historical entrypoints,
construct source families, initialize sparse adapters, or verify q65 shards.
The new launcher's packaging was inspected, not executed symbolically; only
the original scripts identified in PROVENANCE produced the recorded PASS.

The relocated comparison body was checked byte-for-byte against the successful
original after exactly three substitutions: passing the selected payload to
build_namespace and error_schemas, and displaying only the executable basename.
The startup changes are argument parsing, relative pin roles, version checks,
and the metadata-only early exit. Reference harness bytes did not change.
No passed mathematics was rerun just to package paths.
