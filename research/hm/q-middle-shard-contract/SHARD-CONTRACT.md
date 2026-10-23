# SC-01: bounded q65 shard contract

Readiness only. No symbolic payload module has been imported, no historical
prefix/job has run, and none of the65 coefficient maps has been rechecked.
The executable provided here performs static catalogue generation and receipt
accounting only. Mathematical shard execution remains disabled.

## Frozen input and preserved evidence

- Pinned PR810 commit: `ad780e4a14cf7ac9c9f33140c05803b4c156fde8`.
- Payload: `research/hm/q-middle-candidate-interface`, a sibling of this
  `research/hm/q-middle-shard-contract` package. The catalogue CLI requires
  `--payload` explicitly; no checkout location is inferred.
- Verifier SHA256: `cee8781a4b9419d9fcc9cdd4c06e284356ad719f517025e5a55300c3e7424745`.
- Full80-file payload manifest SHA256: `cbfb28f36c5a6b92281e3d6e7dca811c67077e99f52c7143677dd747134d1394`.
- `Q-MIDDLE-55-PLUS-10-AUDIT-INPUT.sha256`: `a05dd6e00a203cafa908b611c002824072d3109da16b3103ac1c038eb1ecdb56`.
- Frozen completion manifest: `8a51729d04e922910d8b5e61e7651fbc7b006ae2a0f6a5597335660e3636e2d2`.

`evidence/inherited-coefficients-partial.log` is a byte-exact copy of the
inherited2754-byte log, SHA256
`c6f9186df81b8a9d199987becd0e9e3329d3e72d71d66955ecd45963fe1c6ba1`.
It contains27 harmonic CHECKED lines, zero trace lines, no final report and
no process-exit receipt. Its final line is
`CHECKED harmonic a2h_tv1_A__AA22_cg0_D5_outer0_B6_A`.
These lines remain historical partial evidence; no new shard result inherits
their status. The original log and all frozen files remain untouched.

## All65 deterministic map IDs

The exact catalogue is in `CONTRACT.json`. IDs are
`q65-shards-v1/{harmonic|trace}/{source}__{target-route}`; they do not depend
on worker count, scheduling or runtime. Labels are derived statically from
the pinned literal12-pair and13-outer route tables. All36 target labels
remain distinguished, including repeated irreducible copies.

| Source | Type | Target copies / map checks |
|---|---|---:|
| harmonic `a2h_tv0_D5` | D5 |10|
| harmonic `a2h_tv0_P4` | P4 |9|
| harmonic `a2h_tv1_A` | A |8|
| harmonic `a2h_tv1_P4` | P4 |9|
| harmonic `a2h_tv2_D5` | D5 |10|
| harmonic `a2h_tv3_V` | V |8|
| harmonic `a2h_tv4_1` |1|1|
| trace `a_trace_h_D5` | D5 |10|

Each map shard must retain the original whole-tensor tests:

1. Extract the signed positive-linear intrinsic tensor from K and compare
   with the independently assembled target inclusion I times the typed source
   coefficient. Signs/order are `(y,−1),(z,+1),(x,+1)`.
2. Check K=Kᵀ on the full9×9 ordered-entry matrix.
3. Form physical=F K Fᵀ using the regular section and check
   Finv physical Finvᵀ=K, with both indices retained.
4. Check physical=physicalᵀ on12×12.
5. For every nonzero entry, use Poly in exactly x,y,z,d,k,l,h0,…,h4;
   every monomial has tridegree(1,2,1). This also rejects denominators in
   those polynomial variables; Laurent units in the formal marking remain
   coefficients, as in the original verifier.
6. Check Δ_a(entry)=0 for harmonic maps, or
   entry=ρΔ_a(entry)/6 for trace maps, where Δ_a=∂d²+4∂k∂l and ρ=d²+kl.

No point, numerical marking, coefficient assignment, rank or source solve is
part of these checks. A zero-entry loop is not a nonzero-witness certificate;
the direct-sum/template global checks supply that missing assurance.

## Eight global jobs which per-map success cannot replace

| Global ID suffix | Checks retained |
|---|---|
| `primitive-cg` | All15 CG inclusions for(2,2),(4,4),(2,6),(2,4),(2,0); nonzero apolar Gram constants; exact left inverses; all cross-zero identities; reconstruction of entire tensor spaces, including antisymmetric legs. |
| `cauchy-pairs` | All12 routes; constant nonzero typed Gram factors; LI=P and IP=I; both cross directions; symmetric image; sum IL=Sym₉; type counts1:2,A:1,V:1,P4:3,D5:5. |
| `outer-routes` | All13 routes; exact typed Gram/left inverses; both cross directions; every I₃⊗P_pair reconstruction. |
| `target-templates` | All36 templates literally equal pair/outer composites; LI=P; every ordered distinct-target cross-zero block; sum IL=I₃⊗Sym₉; counts1:1,A:8,V:8,P4:9,D5:10. These prove the135-dimensional target decomposition. |
| `harmonic-sources` | All7 projections on25 coordinates; nonzero constant Gram factors; typed right inverses; both cross directions; reconstruction I₂₅. |
| `physical-section` | Literal positive covector, quotient-frame inverse, DR=I₉, RD+CΖ=I₁₂, DC=0, FinvF=I₉, and both234-free-coefficient C-factor projection identities. |
| `formal-source` | All a,h and marking symbols remain formal; Δ(a²)=0 and −tv(a,a,2)/8=ρ. |
| `iterator-completeness` | Actual producer iterator's unique source/target label registry equals the independently expected set; exactly55+10; source/target type agreement; matrix-unit counts55 and10. |

Every process also checks the frozen input bundle before and after its work.
The final aggregator requires all8 global receipts and all65 map receipts.
It cannot infer completeness from65 successes, a rank, separate map ranks,
matching characters, or log lines alone.

## Minimal initializer API and blocked execution edge

A later initializer must provide an import-safe factory, for example
`load_q65_api()`, with a frozen code hash and construction provenance. It
must expose the exact functions/classes/constants needed by the verifier:

- Coherent `s,S,T,x,y,z`; `mon,coeff,polynomial,tv,typed_outputs`.
- `cg_matrix,apolar_metric,J2,CANONICAL_DEGREE,PAIR_OUTER_CHOICES`.
- `typed_projection,QLegTargetRoute,outer_binary_tensor`.
- `middle_pair_routes,middle_target_routes,QMiddleQuotientCoefficientBuilder`.
- `POSITIVE_COVECTOR,QUOTIENT_FRAME` and the same free nonzero marking units.
- Either a legacy-free `graded_module()` with its original construction
  checks, or an explicitly reviewed factory for D(9×12), R(12×9), C(12×3),
  Ζ(3×12), together with a separate certificate for omitted helper assertions.

The four matrices suffice for every assertion *written in the verifier*.
They do not automatically reproduce the additional graded-relation and
determinant assertions inside the old `graded_module()` helper. A shortcut
must disclose that distinction. No initializer may silently import
`universal_source_balance_helpers.py`, whose frozen top level execs a
historical verifier; no prefix extraction or runpy execution is permitted.
The current sparse initializer's `build_namespace`/`initialize_sparse`
interface alone is not yet this q65 API.

The execution lock must carry a `helper_assertion_coverage` certificate with
exactly three reviewed scopes: `graded_module:all_assertions`,
`build_module:all_assertions`, and
`transitive_initialization_helpers:all_assertions`. Each scope must be
`preserved-transitively` or `separately-certified`, with the coverage manifest
and independent review hashes recorded. Missing scope/certificate fields are
rejected. The coverage manifest must enumerate the concrete assertions,
including ΖC=I, ΖR=0, the Laurent-unit determinant, both graded relation
reconstructions, and every nested constructor/elimination assertion actually
invoked; an opaque initializer hash alone is insufficient. Certificate hashes
bind reviewed evidence, not a new symbolic replay by the aggregator.

## Safe executable adapter plan

1. Freeze and independently review the initializer above, including symbol
   identity/assumptions and helper-assertion coverage. Pin Python/SymPy,
   adapter and initializer hashes in an explicit execution lock.
2. Extract the original global assertion bodies into named functions,
   preserving comparisons and whole-domain loops. Do not exec a file prefix.
   Construct dependencies as data; verify them in their global jobs.
3. Preserve the literal coefficient producer: subclass the safe builder so
   `middle_apply` numbers its calls and returns a descriptor for unselected
   ordinals, delegating to the original implementation only at the selected
   catalogue ordinal. The method does not receive the source label, so do
   not infer it from a polynomial or target type. Iterate the original
   `iter_coefficients(a,hp,frame='intrinsic')`; cross-check the full ordered
   label registry and every returned descriptor ordinal against the frozen
   catalogue, including the selected map. Verify exactly that returned
   tensor. A changed producer order must fail the registry check. This avoids
   generating all preceding coefficients merely to reach a late shard.
4. The global iterator job uses descriptor-only `middle_apply` to check the
   entire registry without constructing65 tensors. Each map receipt binds
   the same registry and bundle digest. Target I and source p remain computed
   independently, preserving the original comparison.
5. A runner owns wall-time/resource limits and atomic final receipts. Write
   the completed receipt only after all checks, post-input hashes and a
   zero process exit; preserve logs for failed/timed-out jobs. Repeated runs
   go into separate run directories. The aggregator rejects duplicate IDs,
   rather than silently picking a newer successful retry.

## Receipt and aggregation rules

`q65_shards.py` uses only the standard library. Its `catalogue` command reads
bytes/AST literal values and verifies all80 frozen payload entries; it never
imports them. Its `aggregate` command requires a ready execution lock, all73
unique IDs, identical contract/runtime/input digests, exact per-unit check
sets, assertions enabled, no timeout/termination, exit0 and a matching final
log marker as the final nonblank line with verified log bytes. A marker
followed by an error or later work is rejected. `execution-lock.json` is deliberately
disabled until implementation review.

This is evidence accounting, not independent replay of the algebra. A
malicious or incorrect producer can report false checks; the producer needs
its own review. The initial fixture tests exercise missing/duplicate shards,
missing global completeness, wrong/changed inputs, failed/skipped checks,
interruption, disabled assertions, runtime drift and fixture/production
mixing. Synthetic fixture success is never mathematical q65 success.

Acceptance for a later run is “all65 universal coefficient maps and all
global decomposition checks completed under the pinned implementation”. It
still makes no claim of actual-source solvability, operator independence,
trace freedom, an equivariant regular section or an obstruction value.
