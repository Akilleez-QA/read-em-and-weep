# Current independent mathematical review: S209

Review date: 2026-10-20.

**PASS within the stated hypotheses and bounded scope.** This review covers the complete proof, historical audit, dependencies, and current-scope text. It checks the mathematical argument and directly cited public prerequisites; it is not formal verification or an evaluation of an actual HM/source instance.

## 4. S209: secondary-map dependency and countermodels

The PR164 source supplies the genuine normalization sequence and the natural projection identity. For the two connecting maps, a lift in `H¹(K)` defines `σ` modulo the primary `H¹(L)` image; exactness gives `im Δ=ker σ`. This is a map identity, not dimension matching.

For `A=V∩W`, rank-nullity gives exactly

    rank(pr_U|ker σ)=(v−s)−(a−b)=d−s+b.

The conditions `b≤min(a,s)` and `s−b≤d` give the stated sharp interval. Splitting `V=A⊕C` and choosing disjoint image directions realizes every integer in it whenever rank `s` is feasible. At `v=16`, `a=6`, `d=10`, `s=10`, the interval is precisely 0 through 6.

The cones have the claimed cohomology:

    H¹(K)=Q⊕V, dim Q=418, dim H¹(K)=434,
    H⁰(D_σ)=ker T⊕ker σ, dim H⁰(D_σ)=3+6=9.

The other D cohomology groups vanish. The fixed maps `E→L` and `L→P` do not depend on `σ`; the dependence resides in the compatible extension/homotopy datum. The explicit cylinder differential squares to zero, its displayed kernel contraction is correct, and splicing its two short exact sequences produces a genuine degreewise exact four-term complex. The two boundary signs cancel. The proof correctly states that the enlarged strict middle map varies, even though the primary maps in the homotopy/derived category remain fixed.

The Euler arithmetic and conditional cohomology totals are correct. The chosen hypothetical positive table is expressly stronger than established data, and granting it is legitimate for the countermodel's logical purpose. These complexes do not prove the existence of corresponding coherent sheaves or actual geometric HM maps.

The current endpoint correction is essential and is supplied in the packet's opening qualification, dependencies, and scope. PR167 §2 proves `H²(End₀(F)(t))=0` for all `t≥2` from the tensor section-resolution diagonal vanishings. Its endpoint argument gives only `h²(End₀(F)(1))≤30`. The bound comes from a quotient of `15H²(F(−2))`; it supplies neither injectivity of an incoming map nor equality nor vanishing.

**Accepted conclusion:** the given numerical and abstract primary-map data need not determine the projected rank. No actual normalized restriction rank or physical value is deduced. The twist-one endpoint remains unresolved; twist two is closed.

Nonblocking editorial observation: the preserved source's last paragraph still says both positive-twist values “remain unevaluated.” Read literally as a current statement, that is stale for twist two. The prominent current qualification and SCOPE already resolve it. Replacing that final historical sentence with the current status would improve readability, but would require new byte hashes and a small explicit editorial diff; it is not required to repair the countermodel.

## Reviewed file SHA-256 bindings

The four files below are the exact texts reviewed before this review was added.

- `AUDIT.md`: `58b9f3904138933a9b78e9b204d3e38ee29c769d145340b3c3e6713f34e7bf55`
- `DEPENDENCIES.md`: `bec8f06ca33bf42ac558cc6471a81626b7c8dd00812b5c6dbc2b59040ffbe799`
- `PROOF.md`: `d7b613d20d5713a1b0e9a7e334520c547e654f245166bfa794b427e1753c39bd`
- `SCOPE.md`: `c20d4db801712ac8073d9928f1cd63a1b9c2cfe7847b895371366587371cc212`

## Immutable public prerequisites

- [normalization: PR164, 9a7637be2a384cfb784b7e97d6655f1c65a83ef9](https://github.com/Akilleez-QA/read-em-and-weep/blob/9a7637be2a384cfb784b7e97d6655f1c65a83ef9/research/conductor-normalization/normalization-module-resolution/PROOF.md): The exact four-term normalization sequence and secondary-map criterion; B=End₀(HM).
- [regularity: PR167, 063da90fc4543304e87e701cdefcc08225412f17](https://github.com/Akilleez-QA/read-em-and-weep/blob/063da90fc4543304e87e701cdefcc08225412f17/research/conductor-normalization/sharper-hm-regularity/SHARPEST-BOUND.md): Section 2 proves H²(End₀(F)(t))=0 for t≥2; endpoint section leaves h²(End₀(F)(1))≤30 unresolved.
