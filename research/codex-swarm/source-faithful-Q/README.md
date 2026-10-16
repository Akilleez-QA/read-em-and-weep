# QB01 fixed actual Qhat/C definition binding

`q_binding.ActualQBinding(repo=None).describe(full_owner,pair)` binds the reviewed QH01 N14 constructor to the actual local catalog and owned finite/local C definitions, without evaluating actual coefficients. It returns JSON-compatible metadata including ASTs, divisor degrees, full-owner ledger, chart reversal and support enclosure. `coefficient(owner,e,pair)` and `factor_terms(owner,pair)` always refuse, even for structurally zero inputs. No status or arbitrary catalog can authorize execution.

`ClearingDefinition(owner,pair,local=False)` builds the owned C polynomial AST. `ArtificialBinding(owner,explicit_artificial_catalog,N=1,p=pair)` exposes tiny synthetic coefficient controls only. The accompanying proof derives the constructor's local partition and frame identities; hashes alone do not prove them. Descriptors are definitions, not admission capabilities. Source-P identity, primitive/harmonic bindings, actual fibers and execution resources remain external. QH caps are per Ring and do not provide aggregate accounting.

Replay from the repository root:

    python -B -m unittest discover -s research/codex-swarm/source-faithful-Q -p test_binding.py -v
    python -B -O -m unittest discover -s research/codex-swarm/source-faithful-Q -p test_binding.py

Seven controls pass in each mode. They compare all16 actual chart expression constructors without coefficient arithmetic, check full-owner/mask/pair/C/frame metadata, reject physical calls including structural zeros, exercise an artificial coefficient18, reject owner/pair/catalog changes, and check formal homogeneous monomial frame laws. Independent reviewer files `test_independent.py` and `review-independent.md` are reserved.

Repository constraint: `repo` is either None or a path resolving to the canonical workspace repository containing this module. Other paths are rejected before any authentication. All construction and description therefore consume the same canonical source repository; alternate repository loading is unsupported.
