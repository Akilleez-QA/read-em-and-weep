# Seed12/30 binding to null's v5 compiler

This adapter specializes the immutable PR79 v5 metadata graph at `ea2d1a1d2b5774984d0ad48bc15df5fa4d2e0f18`. It imports no null Python modules, runs no compiler or historical checker, and evaluates no physical polynomial. It authenticates the manifest Git blob, compiler/binder/model/source/proof bytes, the bounded archive, and its complete uncompressed graph. It substitutes only the graph's typed carrier/mask/standard owner parameters.

`binding-schema.json` supplies a shape/gate schema, while `validate_result` enforces exact source-bound AST contents. `request-schema.json` specifies the two supported exact requests. Owner tuples are `(seed, occurrence, carrier, legal_mask, standard_tag)`. Standard bits are high-first; legal bits low-first. Both requests are fixed-mask terms, with identity source-sorting orientation. Auxiliary carrier5 sorts before primary0. Prefix owners remain in the selector and outer-weight references.

Run from repository root (stdlib adapter; retain the pinned Git dependency):

```sh
git fetch https://github.com/Akilleez-QA/read-em-and-weep.git ea2d1a1d2b5774984d0ad48bc15df5fa4d2e0f18
python -B research/codex-swarm/arithmetic/compiler_v5/bind_requests.py --repo . --seed 12
python -B -m unittest discover -s research/codex-swarm/arithmetic/compiler_v5
```

The output is a reproducible binding certificate, **not a regularization certificate**. Its exact runtime schema is the result of `bind(request, authenticated_graph, authenticated_pins)`; `validate_result` compares every field to that reconstruction. Missing source references, changed owners/order/frame, different channels, collapsed prefix-mask scopes, mutated source graphs, and released gates reject. JSON numeric types are significant. `seed12-binding.json` and `seed30-binding.json` are reviewable outputs.

The four E34 branches retain source-normalized current ASTs with physical logarithmic Q terms, full owned edge denominators, selector kernel, every outer-weight reference, and compiler normal-order source/template references. Effective coefficients are `(+2,-2,+2,-2)/2` for seed12 and `(+1,-1,+1,-1)/2` for seed30. Frame cancellation occurs in the matching selector once. The original compiler ASTs are retained as provenance. Each requested contraction explicitly uses `tf(R)=R-tr(R)/2 I_2` around its raw normalized L/U AST, matching the older seed12 demand. Equivalence between this projected request and the raw v5 contraction remains unresolved and its dedicated gate stays false. The v5 numerator slots are **arbitrary edge numerators**; the adapter does not identify them with actual combined `T12 F12` branches.

## Required result from null's pending lemma

Each emitted `pending_null_lemma` record pins one exact branch, all owners, the scalar edge, complementary pairs, derivative coordinate, and global finite frame. Null must instantiate the actual inner prism/cover/tensor source map with signed source order, prove the grouped inserted-owner quotient cancellation **before** differentiating, retain Q/weight derivatives, and provide actual per-owner denominator counts and homogeneous/frame shifts. Auxiliary5's `dh` and primary0's `dh` require their actual source identities. A finite admissible Laurent predicate or equivalent regularized domain must accompany the equality. This adapter supplies none of those proofs and does not repeat null's algebra or historical-order audit.

A later reviewer must check that the lemma covers these four fixed E34 instances and binds its certificate to the same source graph and complete density. It cannot discharge the v5 group's other E12 branches or all-seed domain merely by sharing the group name. All numerator-realization, pole, Laurent, detector, execution, source-evaluation, and historical-order gates stay false. Arithmetic schedule and full Rsharp pairing remain separate requirements.

The eight tests are metadata/hash and local semantic controls, including normal and optimized Python runs; they are not physical-source or coefficient controls. Reproducing a 3.38 MB source graph or the 167172/185906-byte bindings is not an arithmetic cost certificate.

Independent isolated replay: all 58 tests in eight v5 scripts passed, with both artifacts rebuilt byte-identically. Python3.13.15, SymPy1.14.0, NumPy2.3.5, mpmath1.3.0; optimized wrapper refused as intended. See `replay-receipt.json` for observed commands/hashes and the initial missing-dependency attempt. This validates the public formal/metadata controls only.

The active selector is fixed-mask: its source `prefix_mask_merger` field is removed and replaced by an explicit no-collapse policy. The untouched original selector, including its legal-weight-one and removed-combination claims, resides only under `source_selector_provenance` and is explicitly inapplicable to this request. `fixed_mask_legal_weights` inventories the legal components already inside every existing outer weight; none is replaced by one or multiplied a second time. Local semantic controls reject omitted/changed tracefree wrappers, wrong wrapped AST/frame, forged projection equivalence, lost/replaced fixed-mask factors, applied provenance, and leaked collapse claims without relying on graph hash mismatch.

Independent V09R review accepts only the repaired metadata scope. The complete local suite passes15 tests (eight producer and seven independent), including116 rejected independent mutations per mode under normal and optimized Python. See `review-independent.md` and `test_independent_binding.py`; the original V09 findings and their disposition remain in the shared PR80 reports.
