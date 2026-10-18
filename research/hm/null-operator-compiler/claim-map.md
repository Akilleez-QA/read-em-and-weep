# Claim map, dependencies, and generalization limits

## Complete executable statements

- `compile_actual_scalar_differential_kernel.py` enumerates 78 seeds, each with
  four E12 and four E34 branches. It preserves every weighted owner, selector
  word, deleted-prefix owner, signed terminal entry and staircase. There are
  312 branches in each derivative pair and 624 distinct branch IDs.
- `normal_order` proves the formal rational identity on arbitrary scalar P:
  C (alpha partial_i + beta)(c P/D) = A P + B partial_i P, with
  A=C[alpha((partial_i c)/D-c(partial_i D)/D^2)+beta c/D] and
  B=C alpha c/D. C is outside the derivative. `test_actual_scalar_differential_kernel.py`
  checks it against independent symbolic differentiation and sign/frame controls.
- `owned_scalar_denominator_binding.py` binds complete occurrence labels and
  denominator derivatives. Complementary input/output characters yield
  c=1, alpha=1, beta=0 in the global finite stripped frame. Noncomplementary
  character input is rejected; infinity-chart conversion is not implied.
- `physical_current_source_binding.py` binds 624 parameterized current ASTs
  using the pinned model, retaining logarithmic moving-frame terms and general
  adjugate/determinant inverses. This identifies normalized currents inside the
  matching selector contraction, not absolute physical matrix values.
- `resolution_selector_source_binding.py` binds 78 factored graded selectors
  using pinned I/P/H blocks and eta; exact abstract split-complex tests compare
  them to direct Cech-J construction. Conjugation is applied exactly once and
  repeated carriers never license merging distinct occurrence owners.
- `outer_partition_source_binding.py` supplies source-definition strings with
  typed finite index domains, owner references, and authenticated public source
  notes. These are **not executable arithmetic ASTs**. Parameterized abstract
  cancellation checks are not actual source pole certificates.
- `traverse_selected_scalar_demand.py` builds the exact 199-node selected DAG
  for row 2, staircase (3,11,15), already source-first sector, first carrier 1.
  Its derivative requests remain blocked until inserted cancellation. This
  selected graph is not a complete all-seed scalar solver.

## Runtime closure

Compiler -> seed metadata + pruning + owned denominators + current bindings +
selector bindings + outer bindings + selected DAG JSON.

Current bindings -> pinned model JSON. Selector bindings -> current bindings,
pruning, metadata, authenticated composition and prefix-pruning proof notes.
Outer bindings -> the two pinned public source notes. Selected DAG regeneration
-> selected traversal only. Formal operator tests -> rectangular jet checker.
All Python project dependencies are shipped here; third-party test dependencies
are SymPy and NumPy. `hm-pinned-source-formulas.js` is a hash-verified provenance
excerpt only and is never executed by replay.

## Unfinished general mathematics and implementation

1. Instantiate complete common-label domains, sorting orientations and full
   owner ledgers beyond the selected source-first sector without tail mergers.
2. Prove actual source pole bounds for the specific grouped expression, retain
   standard-tag ownership, and regularize inserted terms before differentiation.
3. Lower bound current/selector formulas and outer source strings to executable
   arithmetic in compatible homogeneous/finite/infinity frames. Source binding
   alone is not Laurent lowering.
4. Produce finite exact Laurent A/B multipliers, including grouped denominator
   cancellation, for every relevant seed and branch. The artifact explicitly
   records 78 unresolved regularization/Laurent groups.
5. Supply a complete equality witness to the actual detector before stencil
   admission. `check_rectangular_jet_factorization.py` still refuses unsupported
   actual metadata even when authentication flags or unresolved lists are edited.
6. Prove full arithmetic cost and live-memory feasibility independently of these
   metadata checks; no operational resource budget is included or certified.
7. To conclude anything about O2, include the full gerbe/baseline, Fk, scalar
   solver and E(TF) contributions with their global detector/domain proof.
   A selected branch or selected seed cannot establish that conclusion.

## Chronology and scope

The v5 graph's unresolved list is a conservative snapshot. Later support
certificates may improve only a specified selected seed-4 E12 domain. Consumers
must import each later proof's exact domain explicitly; do not clear this
compiler's global flags or apply selected cancellation certificates to other
seeds. The older prose kernel note describing 780 wholly unresolved source
leaves predates v5; it is intentionally not shipped as the current inventory.
