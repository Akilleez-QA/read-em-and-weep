# The actual rank-three opposite core and its top obstruction

**Craig Ward · 23 October 2026 · Source report through PR1020**

This chapter reports mr. slop's results after reading the complete immutable proofs. It is **not an independent reproof** or an actual coefficient evaluation. Sources: [PR1016](https://github.com/Akilleez-QA/read-em-and-weep/blob/b28df36d77a6cb514bd5ae50cb480f572d3eb2f7/research/hm/two-six-source-normal-form/PROOF.md), [PR1017](https://github.com/Akilleez-QA/read-em-and-weep/blob/7cd8baebbec29ad21def1f8b30e19c707a87aed5/research/hm/rank-three-opposite-core/PROOF.md), [PR1020](https://github.com/Akilleez-QA/read-em-and-weep/blob/547a224a95bc16aa6642158ed2b3fd2124e026ab/research/hm/core-top-obstruction-channel/PROOF.md).

## 1. Actual reductions retain their maps

PR1016 forces the S→A component nonzero by positivity: otherwise the actual opposite quotient would surject onto a forbidden low-degree bundle. Its unique allowed source shear then removes the weighted A component. The two independent D directions remain independent, so their actual subbundles can be removed simultaneously. The remaining W′ source is forced into a nonzero P channel. This produces fiberwise-injective presentations with source 2T₆ O(-1) and targets

    (V+P)O⊕W′O(1)⊕SO(1)⊕AO(2),   λ≠0,
    (V+P)O⊕W′O(1)⊕SO(1)⊕WO(3),   λ=0.

The targets have degree12, ranks16 and15; their cokernels Q and Q₃ have degree24, ranks4 and3. Earlier complement choices remain explicit. Neither λ branch is selected.

PR1017 forces the V projection onto. If the unused T₆→P channel vanished, complementary universal sextic evaluation kernels would give an actual quotient onto O(6), forbidden for every remaining Q/Q₃ type. The P projection is therefore onto. The subsequent W′O(1) projection is forced by the same positivity and evaluation-kernel geometry. The result is an actual rank-three core:

    0→W′O(-3)⊕O(-8)→SO(1)⊕AO(2)→Q→0,     λ≠0,
    0→W′O(-3)⊕O(-8)→SO(1)⊕WO(3)→Q₃→0,   λ=0.

Every source map injects on every fiber. Each of the four block Hom spaces is one-dimensional, but the four inherited coefficients are not assigned, independently realized or quotiented by unproved choices. This is not an arbitrary four-scalar substitute for the actual map.

## 2. One inherited block detects the top obstruction

PR1020 proves the universal exact sequence

    0→W′O(-3)→SO(1)→W′O(5)→0.

At twist -12 it induces a nonzero isomorphism between the two relevant invariant H¹ lines. All other invariant H¹ summands of the core vanish. Consequently the actual W′O(-3)→SO(1) coefficient a alone controls H⁰(C(-12))^G:

    a=0 ⇔ rank σ=1 ⇔ C=O(2)⊕O(12)⊕VO(4) (row9).

Its numerical normalization depends on generators, but vanishing is intrinsic. In the λ=0 Euler branch, a=0 would require an everywhere-injective map W′O(-3)→WO(3) of equal ranks and unequal degrees. Hence a is forced nonzero in that branch. In the other branch its value remains unknown.

If a vanishes, the row9 vertex-extension scalar is still unresolved. If a is nonzero, the top obstruction has rank two and the prior result gives an equivariant split vertex extension. This does not evaluate the actual branch or block.

## 3. Distinctions and evidence

Seven necessary opposite-bundle types remain, not seven source-dual pairs. This top-polar σ is not the octic target section σ in the source126 calculation. These reductions neither select the actual C type nor establish the global odd-quadric conclusion or a source realization.

The source packets report immutable-input authentication, independent whole-proof review and ordinary/optimized bounded checks. This chapter preserves that evidence attribution without presenting the readings as another independent proof. Four source-dual pairs across three stable labels remain.
