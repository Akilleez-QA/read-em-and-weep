# Explicit universal Clifford and source-balance context

This cut implements the common dynamic-loader replacement at PR810
`ad780e4a14cf7ac9c9f33140c05803b4c156fde8`. Only this new directory is owned.
Both factories are working ordinary Python implementations. Independent static
review and the bounded one-factory source-balance smoke have passed; see
[the review](INDEPENDENT-REVIEW.md) and [execution evidence](PUBLICATION-EVIDENCE.md).
Downstream graded construction, q65 maps and sparse integration remain unverified.

Add this directory to the downstream application's ordinary import roots, then:

```python
from safe_context import load_source_balance_api
api = load_source_balance_api()  # symbolic construction: supervised use only
# Explicit downstream bindings, for example:
x, y, z, quartic = api.x, api.y, api.z, api.quartic
```

`load_clifford_api()` constructs the full earlier Clifford context.
`load_source_balance_api()` constructs that entire context followed by all
helper initialization in one shared frame. Each call creates a fresh context;
consumers needing shared object identity must share one returned API. There
is no hidden cache, caller-supplied namespace, sys.modules replacement, runtime
source extraction, compilation, exec, prefix slicing or historical entrypoint.
Import itself uses only the standard library and constructs no symbolic objects.
Input/provenance checks precede the deferred SymPy import.

The namespace exposes all 144 mathematical/helper/import bindings inventoried
in provenance, including initialization temporaries, `s`, `comb` and
`combinations`. Loader plumbing (`Path`, `StringIO`, `redirect_stdout`,
`__file__`, `__builtins__`) is deliberately excluded. Every named helper import
in every frozen candidate Python file is checked statically against these
exports. Wildcard consumers receive the full mathematical namespace through
explicit API bindings in their next ordinary-module cut; frozen callers are
not patched or silently redirected here.

The extraction retains all mathematical statements of the entire Clifford
checker, excluding only its docstring and five print reports. The helper block
starts at `G` and ends at `mixed5`, retaining every projector, inverse, H/rh/abase
statement, representation matrix, five-entry `s.solve` quartic recovery and
recovery assertion. The helper's historical `__main__` diagnostics are excluded.
This fixed universal representation recovery is retained literally; no source
feasibility solve is introduced.

Binding equivalence is checked against the concatenated historical execution
namespace, not explicit-init's final locals. In these two blocks the only shared
assigned name rebound by the helper is the loop target `j`; it remains in the
same frame and order. Matrix names, coordinate symbols, nonzero `nu`, `theta`,
`a_m,b_m,c_m,chi`, and all free coefficients retain their exact constructors.
Every function, lambda and comprehension body is AST-identical. The recursive
symbol-table comparison verifies historical global references become closure
references to the same shared initialization frame, including free variables
threaded through intermediate scopes. Locals and built-ins retain their scope.
Python 3.12's inlined comprehensions are handled by comparing within one runtime.
This proves static extraction/binding correspondence, not symbolic equivalence.
Mutating returned API attributes does not rebind a function's closed dependencies;
namespace mutation was never an authorized downstream operation.

All 20 lexical assertions are inventoried with source scope and line. Eighteen
are directly in initialization; the `eq` assertion also runs transitively for
all original initialization checks. `eq` remains an obligation on every later
call; `zero_matrix`'s assertion is deferred until called. Other helpers retain
calls to `eq`/`eqvec` and all original exceptions. The excluded main-only tests
are diagnostics, not discharged verification. No assertion is replaced by a
four-matrix shortcut. Full `graded_module()` construction, its `build_module`,
`_eliminate`, pairing assertions, determinant/inverse and reconstruction checks
remain required in their entirety in the next downstream ordinary-module cut;
this API supplies their common helper dependency and does not fabricate their
results or replace their implementation.

Run the static suite:

```sh
python3 -B research/hm/q-middle-safe-context/test_static.py
```

Six tests cover hashes, exact ordered AST extraction, recursive scope binding,
complete named caller exports and assertion inventory, import guards, and
negative assertion/dependency/tampered-input fixtures. The suite imports only
this inert module, never a factory or frozen module. It passes on system
Python 3.9 and the parent's isolated Python 3.12.14. AST fingerprints normalize
only the empty `type_params` field added by newer Python versions.

After independent review, minimal namespace smoke requirements are: use the
parent's CPU60s/wall75s/sampledRSS1.5GiB supervisor; construct one source-balance
API; verify all 144 exports, symbol assumptions, `coords` identity/order and
`Ms`/`M0,M1,M2` identities; check Clifford square, projector/inclusion identities,
J4 skew/nondegeneracy, and `quartic(OG)==gen4` using exact symbolic expansion.
Compare small formal exterior fixtures and representative calls against a
separately approved reference. The factory already retains all original
initialization assertions. Record code/input hashes, exit status, CPU/wall and
sampled peak RSS. No Darwin hard address-space claim is made. The independent source-balance smoke passed with all retained initialization
assertions; its exact scope and remaining obligations are recorded in the
publication evidence. The sibling failed-smoke record is untouched.

Natural next cuts are explicit physical/degree-one/graded modules sharing this
API, followed by the coefficient namespace and sparse adapter wiring with both
legacy-call tripwires. Those must preserve the distinct physical binary symbols
and full graded construction. Frozen q65's disabled loader and sparse adapter
remain unchanged. No per-map work, constructor execution, actual HM data,
columns, rank, historical generator, commit, push or publication occurred.
