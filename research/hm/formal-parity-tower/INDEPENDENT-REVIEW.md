# Independent mathematical review

**Verdict: PASS under the stated marked-category hypotheses and PR416's explicitly retained invariant literal lifting input.** This is an independent mathematical source-proof review, not formal machine verification, source-instance evaluation, or a claim of exhaustive literature novelty.

Reviewed document: `PROOF.md`.

SHA-256 of the reviewed proof:

`8a85cf0bee9cc3f4c2accd19f5f92de8a101caca431b01378f214017cff2e25a`

The review checked the proposed argument against these exact primary sources:

- [PR409 proof, Lemmas 2.1–2.2](https://github.com/Akilleez-QA/read-em-and-weep/blob/59fc9cdc40cf9a21fbb38549767829ff7471294f/research/hm/parity-separated-ambient-lifting/PROOF.md), commit `59fc9cdc40cf9a21fbb38549767829ff7471294f`.
- [PR416 reversal-compatible continuation](https://github.com/Akilleez-QA/read-em-and-weep/blob/c71356722bc7bd1a426d26ea0ca6d050f4c3ed81/research/hm/parity-separated-ambient-lifting/REVERSAL-COMPATIBLE-CONTINUATION.md), commit `c71356722bc7bd1a426d26ea0ca6d050f4c3ed81`.
- [PR425 one-step proof, Sections 3–7](https://github.com/Akilleez-QA/read-em-and-weep/blob/df433cdd359fa9c7750bf9c8b9765229eac534f6/research/hm/reversal-relative-lift-freedom/PROOF.md), commit `df433cdd359fa9c7750bf9c8b9765229eac534f6`.

## Main checks

1. **The additional lifting lemma is valid and has the correct scope.** Even unital chart coordinate data lift coefficientwise. For a lifted unit, its norm is fixed by reversal, so an odd top defect vanishes and an even defect is removed by the unique half-defect correction. This proves lifting of transport data and chart 2-units, not lifting of equivalences between arbitrarily prescribed upper endpoints. The distinction is maintained throughout.

2. **Vanishing of full finite relative pi_1 is proved, rather than inferred from its associated graded.** The proof lifts a lower trivializing chart unit and applies the endpoint-preserving PR425 formula. The remaining gauge is a literal top automorphism: an invariant global vector field at even degree, hence zero, or an invariant scalar Cech boundary at odd degree, hence killed by a top unitary chart unit. Successive corrections compose in the source algebra and retain the required initial identity marking.

3. **The finite class fibers really are unquotiented canonical torsors.** A lower equivalence can be lifted as transport data to place any representative over the chosen literal lower object. Conversely, a gauge between two such lifts has lower reduction 2-isomorphic to the identity; lifting its trivializing chart unit replaces it by a top relative gauge without changing either endpoint. This removes the possible lower-automorphism quotient.

   The canonical torsor assertion also passes the stronger representative-independence check. Common lifted gauge data are admissible for two different upper products because their unit-norm difference is the normalized top expression h^n u(1,1)=0. Their classical gauge parts are id and 1, so expansion preserves the top difference cochain and therefore the P_n action. Different lower gauges and different lifts give the same relative-class identification by the preceding automorphism correction. A canonical torsor action does not select an origin.

4. **The inverse-limit comparison is proved constructively in both directions.** Finite class systems are strictified to literal compatible presentations using transport. For injectivity, an available upper equivalence is corrected by a lifted chart 2-unit to have exactly the already chosen lower gauge. This gives compatible equivalences, not merely unrelated finite ones. Coefficientwise finite differential order suffices for their formal limits; no uniform order bound or analytic convergence is presumed. Thus no unproved exchange of inverse limit with quotient or hidden lim^1 assertion is needed.

5. **Formal automorphisms and the two pi_2 conventions are correctly distinguished.** Formal pi_1 is handled by a separate compatible-trivialization induction. For pi_2, compatibility C_i=F_ij(C_j) makes each successive coefficient a global regular function after lower scalar coefficients are removed. Connected properness forces it to be scalar. Unitarity then says the scalar logarithm is odd. Ordinary inner 2-units retain all scalar logarithmic coefficients from degree M. The truncated scalar restriction maps are explicitly surjective. These extra 2-morphisms change neither the objects nor their equivalence relation.

## Scope assessment

The new conclusion goes beyond the cited one-step theorem: it establishes the marked finite tower and its coefficientwise formal class set. The product parameterization is appropriately noncanonical and only a filtered-set statement. The dimensions g^2 at even degrees and g(g−1) at odd degrees follow from the stated inversion action; they give 16 and 12 in dimension four.

The proof does not eliminate automorphisms changing the initial marking, classify unrestricted non-reversal continuations, prove an algebraic moduli space, or assert a fixed-product, module, convergence, algebraicity, or source-dependent obstruction result. Its retained existence premise remains explicit. No blocking mathematical gap, gauge-orientation error, or unaccounted top pi_2 obstruction was found in the reviewed version.
