# Safe-context factory: independent static review and bounded smoke

Verdict: PASS for the four exact files below and the narrowly authorized
one-factory universal namespace smoke. No blocker was found. This is not
a source-completion result or approval of a downstream graded construction.

Reviewer: source2_constraints, separate from the CLI producer. No producer
file was edited. Review outputs are confined to this review directory.

## Frozen artifact and source identity

Paths in the first table are relative to
`work/swarm/qmiddle-adapter/research/hm/q-middle-safe-context/`.

| File | SHA-256 |
|---|---|
| safe_context.py | 4f94b6268202179babcbf705cdbe221e8c57c12686b5ffffe3c6ba22ea36f5b1 |
| provenance.json | b0d8dfec8abec5290128c2def4eb21bbd35f9ae1f483fa67f8e3de555f54b0ab |
| test_static.py | d899cc367540c563bd5af634a37504eba58d39dac7d5fbe5476235e4ec8a5935 |
| README.md | 55b0cbefbe908014188e9499e679457fc4804f561b16d61a061ee95412b48498 |

Both mathematical inputs were independently fetched from public immutable
PR810 commit `ad780e4a14cf7ac9c9f33140c05803b4c156fde8`, under
`research/hm/q-middle-candidate-interface/`. Their fetched UTF-8 bytes match
the local files exactly, including their terminal newline:

| Input | SHA-256 | Git blob |
|---|---|---|
| verify_universal_monad_clifford_homotopy.py | 4e71b3c14ad9a85b099a9ee4261e4ebccd61e5aca1760462069bfe939982317b | ceeaf3c2deaee4d40cef35d1b3a68fbff29a7fef |
| universal_source_balance_helpers.py | 15069fcc8138d2742bfdebd3db650efb84bd74abf1c2909585d2b6e988b276c3 | 93c6ef7053c806ed72c1f79c87fb8e6441090d2e |

## Static findings

The reviewer read the entire factory and both frozen inputs. The ordered
AST of the copied Clifford statements matches the frozen checker after
excluding only its docstring and five print calls. The helper block matches
every statement from G through mixed5, excluding the historical loader and
main-only diagnostics. No assertion or mathematical assignment was removed,
replaced with a shortcut, or reordered.

The sole solve call is AST-identical to the frozen five-equation symbolic
quartic representation recovery. It is not a selected source-feasibility
system. All coordinate and coefficient symbols, nonzero assumptions, matrix
constructors, inverses, projectors, H/rh/abase definitions, and recovery
assertion are retained. All twenty lexical assertions remain, including
the nested eq and zero_matrix obligations. Initialization reaches its
original eq calls; zero_matrix remains a callable obligation.

The 144-export inventory equals the combined historical mathematical
namespace, including loop temporaries and imports comb/combinations/s.
Loader infrastructure alone is excluded. The common function frame preserves
the source execution order and late shared bindings, including the helper's
rebinding of j. The recursive symbol-table test checks global-to-closure
correspondence through function, lambda, and comprehension scopes. This is
important: function bodies being AST-identical alone would not establish
correct binding after moving code into a factory.

Both public factories validate provenance and input hashes before invoking
construction. Ordinary module import is inert and uses only the standard
library. The implementation contains no exec/eval/compile path, source-prefix
slicing, historical module import, hidden whole-checker execution, caller
namespace injection, sys.modules replacement, or source generator. Retaining
the universal mathematical initialization statements explicitly is intentional;
it is not a call to the historical checker entrypoint.

All six producer static tests passed under the isolated Python 3.12.14 in
0.132 seconds. They include assertion tampering, dependency-name tampering,
input tampering, named caller exports, and import tripwires. The reviewer
also independently compared the complete ordered AST blocks, counted the
144 unique exports and twenty assertions, and checked the sole solve AST
against the frozen source. None of these static checks called a factory.

## The one authorized factory smoke

After static review passed, exactly one source-balance factory call ran in
`smoke.py` through the independently reviewed burn_guard at its unchanged
defaults: CPU soft/hard 60 seconds per process, wall watchdog 75 seconds,
sampled aggregate RSS threshold 1,610,612,736 bytes, nominal interval 0.1 s.
The worker used isolated Python 3.12.14 and SymPy 1.14.0. No -O mode was used;
the harness explicitly required assertions to be enabled.

The smoke checked all 144 actual exports, nonzero assumptions, coordinate
ordering and object identity, all three Ms object identities, Clifford square,
the Cartan inclusion/projector identities, J4 skewness/nondegeneracy, and
quartic(OG)==gen4. It checked 116 actual nonlocal closure bindings against the
returned shared API objects. Tiny free-symbol exterior fixtures independently
checked wedge signs, repeated-factor vanishing, cancellation, contraction and
zero action. All original factory initialization assertions also executed.
A runtime import tripwire rejected historical universal_/verify_/derive_
modules. There was no second reference-factory or historical checker run.

The guard receipt reports:

- status success; worker exit 0; cleanup complete; no termination signals;
- direct-child CPU 0.575766 seconds;
- supervisor runtime 0.7577938329995959 seconds;
- sampled group peak RSS 66,813,952 bytes (63.71875 MiB), across eight samples;
- separate wait4 child peak RSS 66,846,720 bytes;
- no observed RSS or wall overshoot; all recorded input hashes unchanged.

Only one worker process was launched. The supervisor's short synchronous ps
samples were its monitoring operations. No source feasibility solve, actual
HM coefficient assignment, per-map evaluation, family loop, graded_module(),
historical generator, or downstream sparse adapter run occurred. The literal
universal five-equation quartic recovery did run, as required by the factory.

The receipt explicitly records that RLIMIT_AS is not enforced. RSS is a
sampled process-group sum with no finite guaranteed inter-sample overshoot
bound; its measured peak is not a hard address-space guarantee. The earlier
failed Darwin address-space receipt was not touched.

## Evidence hashes and limits

| Evidence | SHA-256 |
|---|---|
| burn_guard.py | 6915a220408dc3bb5045b6cfaaaef8267a6516319cdb98deca5ba5717614c6fc |
| smoke.py | 2b592af1564ad927fb0b1716129e23e684b08745efa949826656fd4965b15c4c |
| run-0001/receipt.json | 9c478acfbd213a4ac3647a4a13880c01c1dc08dfa8eac4aeb67b470ca4aac8e1 |
| run-0001/stdout.txt | 0020a0c89d8e3d96bb20b2fda600b2f0e602a75fde0103455ba58f166b57c6e7 |
| run-0001/stderr.txt (empty) | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |

The receipt contains the exact command, executable hash, every candidate/input
hash, limits, process-group information, and unchanged-input result.

The verdict covers ordinary calls using the returned shared context. It does
not certify mutation of API attributes as a way to rebind closed dependencies,
preservation of historical function metadata or arbitrary global introspection,
or substitution into still-dynamic downstream modules. Main-only diagnostic
checks and complete graded-module construction remain separate obligations.
No source-completion, rank, proof-repair, or algebraicity conclusion follows.
