# Independent review: trace-free first-current selector equivalence

Reviewed 2026-10-16 UTC. Verdict: **PASS within the explicitly imported determinant-proof dependency.** No mathematical correction to the reviewed proof is required.

## What was independently checked

- Read the entire proof and abstract control script, all eight stored source-evidence files, and the certificate/source pins. Ran `python test_tracefree_equivalence.py`: all seven methods passed (0.497 seconds). Ran `sha256sum -c SHA256SUMS`: all fourteen entries passed. The tests also recomputed the Git blob IDs of all eight source files and matched every declared pin.
- This review ran only the abstract test file and byte/hash operations. It did not import or execute the physical-current binding, compiler, physical polynomial model, determinant checker, or request binder. It did not generate/evaluate a physical source graph. No external communication or repository change was made.
- Commit references are supplied provenance. This review verifies stored bytes against the supplied blob pins, but does not independently fetch the remote commits to re-establish blob membership. It neither reruns nor independently reconstructs the earlier determinant calculation.

## Mathematical and source-binding findings

1. **Correct current ASTs.** The stored v5 `core(a,b)` is exactly `(P_a I_b)^t`; its tangent is `partial A + Q_b A - A Q_a`. `normalized_current` gives `A^-1 T_ab` for L and `A^-1 B^-1 T_bc A` for U, retaining a general inverse. Physical conjugation is by the first owner's D. The proof uses precisely these orders, including U's final A. It does not silently replace the normalized current by the physical matrix.
2. **Actual determinant dependency, not an assumed SL2 jet.** The stored first-order proof states all 36 exact rational identities `det(P_i I_j)=1`; its receipt records ordered pairs 0..5 squared, integer-polynomial cross multiplication over Z[v1,v2,v3,v4], PASS, and no point samples as proof. Its model hash matches the v5 binding, and the attribution pin matches both model and source-excerpt hashes. Transposition and elementary-symmetric substitution preserve determinant one. Thus, accepting this explicit prior exact result, Jacobi's formula yields `tr(A^-1 partial A)=0` as a function identity. This is stronger than a determinant-one value at one point.
3. **Both frame terms are necessary and present.** The source's Q is diagonal `(ell,-ell)`, hence has zero trace. Cyclicity gives `tr(A^-1 Q_b A - Q_a)=0`. U's conjugation cancels in its trace, leaving the identical argument for B. The conclusion holds for the full physical moving frames and for every correctly bound first L/U current in this source. No choice of the x-independent frame constant is needed.
4. **Selector transpose is correct.** `selector_matrices` feeds a row l and column r; `bind_seed` contracts `l Rbar^t r` and defines `K=(r l)^t`. Direct entry expansion gives `tr(K Rbar)=l Rbar^t r`. K need not be traceless. Because D is diagonal, `D (D Rbar D^-1)^t D^-1=Rbar^t`. The compiler checks matching first-tail owners before storing the normalized current. The proof's cancellation uses the exact source convention once.
5. **Projection and arbitrary weights.** For every 2-by-2 K,R, the omitted central term is exactly `tr(K) tr(R)/2`. Vanishing comes from the first current's trace, not from a claim that rank-one K has trace zero. Scalar multiplication preserves the identity for arbitrary scalar functions, including zero weights. The request binder retains all weighted owners, forbids replacing legal weights by one, and removes the prefix merger from active fixed-mask requests. The proof neither divides by a weight nor duplicates one.
6. **Differentiation and normal order.** `normal_order` explicitly keeps C outside `alpha partial + beta`; its displayed A0 and A1 match the proof, including the derivative of conversion and denominator. `compile_term` includes the signed coefficient, every outer weight, and the selector contraction in C. Replacing projected C by the equal raw C therefore preserves both coefficients without differentiating C. Any subsequent differentiation of the identity must retain the full product rule; nothing here licenses dropping frame, weight, selector, or current derivatives.
7. **Concrete request scope.** Static inspection of `bind_requests.py` confirms seed12/30 owners, four E34 branch signatures per seed, signs (+,-,+,-)/2, and effective seed coefficients 2 and 1. The trace-free wrapper's input is exactly the normalized source AST. The proof closes this projection-equivalence proposition branchwise, without cancellation between branches or seeds. This review did not regenerate the specialized graph or assert that an arbitrary edge numerator realizes T12F12.
8. **Scope exclusions are sound.** The argument does not extend to a general raw baseline or raw normalized second jet. `H^2=I` and `A(t)=diag(exp(t),exp(-t))`, with `A^-1 A''=I`, are valid negative controls. A nontraceless selector detects the central component of I. The same-coordinate second-jet example is a general counterexample, not a physical-source obstruction calculation. No detector/null identity, Laurent admission, pole cancellation, T12F12 realization, historical ordering, finite support, cost bound, or release gate is established.

The seven numerical/rational control methods are regressions and negative controls, not the proof of universal identities. Universality follows from the displayed trace/Jacobi argument and scalar linearity under the stated source-backed hypotheses. The imported exact determinant proof remains a declared dependency.

## Exact reviewed hashes

Reviewed manifest SHA256: `c130081b603825dbe0df449aa215587f1b01649bc734c763473f76d551103f0b`.

The exact fourteen SHA256 entries verified at review time follow. This review file is intentionally outside that original manifest, so the original artifact remains unchanged.

```text
e77328364f7d738430d5ef4ebcde16ae1aa827ce59cd48f9300c1ad5319407b3  PROOF.md
70f77ff04c11116f5dfacde21026f365e193e811f15a1d6ea717bad9508de015  README.md
24b17fae822929bbac7b621154235ad02af7b325b1052a5db6cd395ba7defd17  certificate.json
dfba29eb6cc4c8edb3d33afa8b4bf6afd327d7f01604c80cbf8955c0d3de1f70  source-pins.json
7022fa34776de07b6f62a21882585f6f0d5fda52ef4513942d35243a66c3bdcc  test_tracefree_equivalence.py
e5b7eb0b355d6be3a707a1aca18f116dd848dbb392cc3ae012ce5f4b52b76037  test-results.txt
9305cd1f70518d06f710901da86817c86101d241ae212d8867c962dde625da72  sources/attribution-pins.json
5b09d7d478608c74c495c59239bf6e96935408cb4ab9bc1956731395cf56a36b  sources/bind_requests.py
d12dbdfe90a42dc97b6ecf31b239ce74e278ef549a6828447f454852315bbaa6  sources/compile_actual_scalar_differential_kernel.py
e608a0652bbce571e345489125d71c7dd35c0da77de8712b6d9265bf86da7bd0  sources/determinant-verification.json
502baffafd3e0d271f6a83e2eaf0c847b023a2bcc7e81273fbb438269492a8d6  sources/first-order-source.md
876cad001a8f96bb207ca246873e3efe67afd9a394cc4d2a0796992596b84916  sources/outer-pinned-frames-and-poles.md
8cc3f3be47c6944e983a8b1922470a27c1a413b3fe9059f97c75b7a2cd967d3d  sources/physical_current_source_binding.py
3f57b8408ca6fd54a6fb243c57121dfbb7f0c4c10976e0c044c7e5ffe3f63e60  sources/resolution_selector_source_binding.py
```

Request commit: `fc7563595b8fd0aeed1675d886b178d43c385bdf`.
V5 source commit: `ea2d1a1d2b5774984d0ad48bc15df5fa4d2e0f18`.
Determinant dependency commit: `08b73637d4136f91606aad332c46cafd064417f8`.
Model SHA256: `635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926`.
Source excerpt SHA256: `c4f65ff831092d0e56b3e33a0357f44182169fda45943ea780c8c551b4023f94`.

Verified Git blob IDs, in source-pins order:

```text
ba0a962abf9a284950d140247676e5ff55e969e3  bind_requests.py
558516485e0df8b7375b6d34224b2045d51184d7  physical_current_source_binding.py
805428b4c32214ce6c945fa3f88ebf47b75f7188  compile_actual_scalar_differential_kernel.py
5f4e56252cd9a8a6eb218aceb911c95a1c330ebc  first-order-source.md
d36f2f1f0f84e1aae4412ae346487d6663e1d6d4  determinant-verification.json
4e672c77e0d0ea233a07cb45c9da466e5cd32868  attribution-pins.json
07b5c3403e50c2de8ac658d30b82580fb625acc1  resolution_selector_source_binding.py
46470b5a7198be2f8c39f9cb5f5a904ae355ec97  outer-pinned-frames-and-poles.md
```
