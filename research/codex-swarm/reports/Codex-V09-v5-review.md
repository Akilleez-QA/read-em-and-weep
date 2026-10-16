Codex-V09: accepted as a pinned metadata specialization only. Two source-binding gaps remain:

- **Trace-free projection is unaccounted for.** The existing seed12 contract explicitly contracts `tf(current)` and forbids inferring zero trace ([contract](../arithmetic/seed12/demand_seed12_e34.py:118)). All four v5 branches carry raw normalized L/U ASTs without that projection. Exact equivalence needs the projection or a source-bound proof that removing it preserves the contraction.
- **Fixed-mask output retains collapsed-mask claims.** The selector records still declare `legal_weight: "1"` and 16/256 removed combinations ([seed12](../arithmetic/compiler_v5/seed12-binding.json:2722), [seed30](../arithmetic/compiler_v5/seed30-binding.json:2951)), despite fixed-mask requests and retained full prefix weights. These fields need an explicit provenance-only qualification or consistent specialization.

Accepted checks:

- Four E34 branches have the expected edges, coordinates, L/U order and `+,-,+,-` signs; effective coefficients are `(±2)/2` and `(±1)/2`.
- Exact owners, auxiliary5-first ordering, selectors, prefix weights and both logarithmic Q terms survive.
- Missing combined-inner realization, grouped cancellation before differentiation, actual owner pole counts, derivative suffix bounds and finite/infinity Laurent predicates remain unresolved. All admission gates stay false; global-finite conversion supplies no infinity regularity proof.
- Provenance authenticates pinned manifest → source/model/proof bytes and archive → bounded graph → reconstructed outputs. Both checked-in bindings reproduce exactly. This establishes byte identity, not source coefficient equality or proof correctness.

Five supplied tests passed normally and under `-O`; 68 additional adversarial controls rejected in each mode, covering branch/weight omissions, frame/order changes, forged discharge, released gates and provenance corruption. The metadata-semantic gaps above still pass reconstruction.

No physical source arithmetic, monolithic execution, edits or GitHub mutations were performed.

Publication note: this report records its inspection snapshot; subsequent corrections and review dispositions are recorded in STATUS.md and the relevant package README.
