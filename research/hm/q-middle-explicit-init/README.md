# Explicit universal initialization

Status: static extraction, bounded universal namespace smoke, and independent
namespace behavioral equivalence PASS. Sparse initialization/API integration,
q-middle adapter integration, and q65 coefficient verification remain UNVERIFIED.

The frozen payload is the sibling `q-middle-candidate-interface` from
[PR810](https://github.com/Akilleez-QA/read-em-and-weep/pull/810), commit
`ad780e4a14cf7ac9c9f33140c05803b4c156fde8`. `initializer.py` and
`test_initializer.py` are byte-identical to the reviewed producer files.
`receipt.json` is a sanitized derivative of the original receipt with current
evidence pointers; its static comparison sections are unchanged. This README
updates the completed gates and records their limits. Original and publication
hashes are separated in `evidence/PROVENANCE.json` and `evidence/MANIFEST.json`.

`initializer.py` uses explicit Python: no runtime source loading, prefix
splitting, AST compilation, historical import or historical entrypoint.
Import uses only pathlib/hashlib/json. `build_namespace(root=None)` validates
all 80 frozen payload hashes and constructs the universal tensors with all
original assertions. `error_schemas(root=None)` returns the complete 26-sector
schema. The optional root selects a different payload location.

`initialize_sparse(instance, api)` copies the remaining frozen
`SourceMap.__init__` statements using an explicitly supplied sparse API. Its
static extraction is checked; its runtime behavior is not certified by this
namespace-only evidence. It installs an instance-local legacy `source_map`
tripwire. The frozen verifier's class-level tripwire remains separately
necessary, including for explicit class-method calls.

## Exact extraction and namespace comparison

| Frozen source | Original AST statements, stop exclusive | Retained scope |
| --- | --- | --- |
| verify_universal_monad_clifford_homotopy.py | 2:80 | All mathematical initialization and assertions; five print reports omitted |
| verify_full_six_space_vertex_correction.py | 7:35 | Projector, pairing, exterior and six-space definitions |
| verify_w_action_mixed_interface_one_ninth.py | 6:19 | H, rh, abase and W-action definitions |
| universal_complete_w_action_symbols.py | 2:end | Separate complete-W namespace, including build_symbols definition; never called |
| derive_c_only140_unfiltered_principal_quotient.py | 10:36 | Frame, cubic convention, D/N and H0; before family construction |
| universal_unconditional216_source_map.py | SourceMap.__init__, 2:end | Sparse conversion, columns, inverses, polar data, q and affine targets; static comparison only |

Constructor changes are `self` to `instance`, sparse API names to `api.<name>`,
explicit namespace construction replacing loader statements, and the added
legacy-call guard. The receipt records all 16 API names. The internal
19-variable/public 17-variable orders, nonzero FB/FC/FD/theta units, binomial
cubic normalization, endpoints, defects and coefficients are retained.

The complete-W helper retains its fixed five-entry quartic recovery `s.solve`.
No source feasibility solve or family builder is called. Returned functions
close over the explicit frame, while the reference uses global bindings.
Mutating the returned dictionary is not supported as a way to rebind those
functions. The independent comparison checks that intentional distinction:
150 outer names, 32 complete-helper names, all 46 function dependencies
including nested code objects, and 40 small formal probes. Symbol assumptions,
all matrix entries and all container values agree; no algebraic fallback was
needed. Two negative fixtures reject changed symbol assumptions and a changed
global tensor. The `negative_symbol` inventory is a rejected fixture.

## Completed validation

Six static tests pass without SymPy or frozen payload imports. Their recorded
AST metadata uses Python 3.9; reproduce with Python 3.9 from the repository root:

```sh
python3.9 -B research/hm/q-middle-explicit-init/test_initializer.py
```

The later namespace smoke and independent equivalence worker used Python
3.12.14, SymPy 1.14.0 and mpmath 1.3.0. The equivalence worker completed in
2.159163 child CPU seconds, 2.413820 wall seconds and 75,825,152 bytes direct-child
peak RSS. All 89 supervisor-recorded inputs remained unchanged; cleanup
completed. Both successful receipts/stdout are in `evidence/` with full original
hashes and sanitized publication hashes. Detailed reviews are
`evidence/STATIC-REVIEW.md` and `evidence/BEHAVIORAL-REVIEW.md`.

The reviewed watchdog used 60 CPU seconds per process, 75 wall seconds and a
sampled process-group RSS threshold of 1,610,612,736 bytes at 0.1-second intervals.
It does not enforce an address-space cap on this host. Sampled RSS has no
between-sample overshoot guarantee; CPU is not an aggregate process-group
budget. It is not a sandbox. These are the actual limits, not an RLIMIT_AS claim.

The original `test_initializer.py --smoke` attempt failed at RLIMIT_AS setup
before symbolic import. That unchanged legacy option still requires host
RLIMIT_AS support and appends its receipt in place; it is not the replay command
for this evidence. Two later reviewer attempts failed due to AST-version
metadata and shallow binding inspection, respectively. Both reviewer defects
were corrected without changing the initializer. `evidence/FAILED-RUNS.json`
retains their status, diagnostics, original receipt/log hashes and reviewer
snapshot hashes. No failed attempt is represented as PASS.

## Portable evidence and remaining gate

The portable verifier accepts `--package` and `--payload`; defaults locate this
package and its frozen sibling. Its two reference harnesses are byte-identical
to the ones executed. The comparison body is unchanged except explicit payload
arguments and sanitized executable display. Path/configuration scaffolding was
reviewed and metadata-checked after relocation; the relocated verifier was not
rerun symbolically. The original executed and relocated hashes remain distinct.

```sh
python3 -B research/hm/q-middle-explicit-init/evidence/verify_namespace.py --check-layout
```

This command checks hashes only and imports no symbolic libraries. Optional
bounded replay instructions and the required reviewed watchdog hash are in
`evidence/README.md`; a replay creates a new output directory and never replaces
published evidence.

Before scheduling mathematical shards, independently authenticate the sparse
API and its dependency closure, compare every initialized sparse attribute
and function against a frozen reference, retain all 26 sectors, and test both
legacy tripwires. Preserve the q-middle constructor's direct
OrthogonalSourceMap initializer call, which bypasses unwanted raw8 family
construction, and preserve its later q-middle statements and symbol renames.
The existing dense reference import closure still performs bounded universal
work and needs separate integration review. This result does not certify any
sparse adapter, q65 coefficient, source feasibility claim or actual obstruction.
Inherited empty and partial logs remain unchanged.
