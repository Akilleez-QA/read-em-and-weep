# Independent mathematical review

**Verdict: PASS under the stated marked invariant differential-category hypotheses and the explicitly retained literal lifting inputs.** No blocking mathematical gap was found. This is an independent mathematical source-proof review, not formal machine verification, a selected-source evaluation, or a claim of exhaustive literature novelty.

Reviewed document: `PROOF.md`.

SHA-256 of the unchanged reviewed proof:

`417dce127594121f515360a39058db5e9a6b2414ea00e52733bb621229a0ca46`

## Exact primary sources checked

- [PR436, marked formal tower proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/502c978a17cd7037d740d4d08d373c1cb8bd5829/research/hm/formal-parity-tower/PROOF.md), commit `502c978a17cd7037d740d4d08d373c1cb8bd5829`.
- [PR425, one-step relative lift proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/df433cdd359fa9c7750bf9c8b9765229eac534f6/research/hm/reversal-relative-lift-freedom/PROOF.md), commit `df433cdd359fa9c7750bf9c8b9765229eac534f6`, particularly its difference equations, transport convention, comparison, and chart 2-morphisms.
- [PR416, reversal-compatible continuation](https://github.com/Akilleez-QA/read-em-and-weep/blob/c71356722bc7bd1a426d26ea0ca6d050f4c3ed81/research/hm/parity-separated-ambient-lifting/REVERSAL-COMPATIBLE-CONTINUATION.md), commit `c71356722bc7bd1a426d26ea0ca6d050f4c3ed81`.
- The [unrestricted invariant literal small-extension proof](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6259748725), including its repair of a prescribed literal presentation and its explicit elliptic-fourfold application.

## Main checks

1. **The unrestricted automorphism argument is valid at every finite order.** At a literal top layer, normalized chart cochains satisfying `bt=0` are derivations, and `delta t=0` glues them to an invariant global vector field. Inversion makes that field zero. The remaining invariant scalar Cech 1-cocycle has zero class because `H^1(O_X)^iota=0`. An invariant primitive exists by averaging a primitive on the individually stable cover. An ordinary chart unit removes it at either parity. For a full finite automorphism, lifting the previous trivializing unit and applying the endpoint-preserving formula first makes the lower gauge literally the identity. This proves full finite relative pi_1 vanishing, rather than merely graded vanishing. No reversal hypothesis on the unrestricted lower object is used.

2. **The lower-gauge alignment has the correct orientation and scope.** Two gauges with the same endpoints differ by an automorphism of an endpoint. Its 2-trivialization can be whiskered to a chart-unit 2-morphism between those gauges. The displayed formula uses units in the unprimed source algebra and preserves both transported endpoints, as in PR425. Lifting that source chart unit therefore changes the upper gauge to have the prescribed lower reduction. The lemma assumes that some upper equivalence already exists; it does not assert lifting between arbitrary prescribed upper endpoints.

3. **The finite injectivity induction closes the missing comparison step.** After exact lower alignment, the parity lower gauge is lifted only as transport data. PR436's norm-defect correction provides invariant unitary edge units, and even chart maps lift coefficientwise. Their transport target is determined rather than separately prescribed. If this gauge is `p: x -> z` and the adjusted unrestricted gauge is `q: x -> y`, then `q` after `p^(-1)` runs from `z` to `y` and has literal identity reduction. The one-step PR425 replacement now applies legitimately. At an even top degree the scalar difference is zero, so discarding the edge coefficient preserves endpoints. At an odd top degree the product difference is alternating whereas `bt` is symmetric, and the map difference is zero; discarding the chart coefficient preserves endpoints. All corrections retain the identity marking modulo `h^M`.

4. **Both formal comparisons are justified without exchanging quotient and inverse limit.** For the unrestricted category, arbitrary coordinate data lift and transport strictifies a compatible system of finite object classes to literal presentations. Conversely, Lemma 2.2 makes available upper equivalences reduce to already chosen lower ones. Their coefficientwise limit is a formal equivalence. The parity comparison is the separately proved PR436 result. At each degree only finitely many differential operations occur, so finite differential order coefficient by coefficient is sufficient. No uniform order bound, analytic convergence, or unproved lim^1 vanishing is needed.

5. **Finite detection follows from uniqueness and coherence, not unrelated finite normalizations.** Injectivity of each `J_n` makes the parity preimages of a compatible unrestricted class system themselves compatible. The parity inverse-limit surjectivity realizes them formally, and unrestricted inverse-limit injectivity identifies its image with the original formal class. The criterion is conditional on every finite truncation being in the image and gives no fixed bound on the first possible failure.

6. **Formal non-surjectivity is established by a continued finite obstruction.** At the first new degree `n=M`, the marked gauge relation is exactly the one-step relative relation. A nonzero complementary class therefore cannot be removed by any permitted marked finite gauge. At odd `M`, an invariant derivation-valued Cech 1-cocycle realizes the forbidden `H^1(T_X)` direction. At even `M`, a global invariant bivector realizes a forbidden local-product direction; the scalar Cech 2-cocycle alternative is also valid. The displayed difference equations verify these are actual finite presentations. The unrestricted literal lifting input then continues this particular presentation while preserving it exactly. Any formal parity equivalence would contradict the finite obstruction after truncation. The complementary dimensions on a fourfold are correctly 12 at even new degree and 16 at odd new degree.

## Assumptions, contribution, and limits

The comparison results concern one fixed initial presentation and gauges literally identity on it. They do not address changing the marking, geometric or discrete automorphisms, or non-invariant gauges. Ordinary versus unitary chart 2-units do not alter the object equivalence relation when the allowed objects and 1-gauges are unchanged; they need not give equivalent 2-groupoids.

Literal continuation, especially continuation of the chosen non-parity finite class, is an essential existence premise. The cited small-extension source explicitly treats the stipulated elliptic fourfold. The general abelian statement retains the same lifting and cover hypotheses, as the proof says; this review does not replace that premise by a claim about an arbitrary cover or category.

The contribution beyond PR425 is genuine: one-step injectivity is extended to marked finite and formal continuations by exact lower-automorphism removal and compatible-equivalence construction. Beyond PR436, the proof supplies the unrestricted comparison needed for formal injectivity and finite detection, and continues a forbidden finite class to prove proper formal image. The argument remains a coefficientwise formal ambient result with adjustable higher products. It proves no module continuation, fixed-product theorem, convergence, algebraization, algebraic-cycle result, or selected-source obstruction value.

No proof changes were made during this review.
