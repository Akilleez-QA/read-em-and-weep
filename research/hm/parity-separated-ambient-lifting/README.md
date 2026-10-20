# Parity-separated ambient lifting

## New results

- At an even lifting order, reversal-unitary scalar units make the pentagon automatic. Under invariant H^2(T_X)=0, prescribed associative parity local products admit a literal ambient lift. No H^3(O_X) vanishing is needed at even order.
- The fourth scalar coefficient is e=b^4/24+bc+mu_2(b,b)/2, explicitly in the already supplied c.
- At an odd order, the fixed-product map defect is an actual bivector that a new map coefficient cannot repair. The exact fifth defect is derived, with a structural counterexample to arbitrary fixed fifth-product gluing.
- If top odd products may vary by bivectors, the defects form a Cech 1-cocycle. Their precise repair class is in H^1(wedge^2 T_X)^G, which has no inversion-invariant part on an abelian variety. Given local associative parity extensions, this repairs odd gluing while preserving the even lower maps.

## Files and review

PROOF.md contains the full even/odd theorems, canonical fourth coefficient, exact fifth equation, and exclusion. ODD-BIVECTOR-REPAIR.md proves the subsequent global repair lemma. CURRENT_REVIEW.md is independent mathematical proof review with exact theorem hashes, not a formal proof-checker run or selected-source evaluation. No mathematical proof bytes were changed after that review.

## Exact antecedents

- Base: [PR401](https://github.com/Akilleez-QA/read-em-and-weep/pull/401), commit `1dfcd736ed29bee9467e8ff822f383156097f648`, [fourth-order global-gluing proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/1dfcd736ed29bee9467e8ff822f383156097f648/research/hm/bounded-ambient-deformations/fourth-order-global-gluing/PROOF.md).
- [Genuine third-order construction, PR115](https://github.com/Akilleez-QA/read-em-and-weep/blob/2f4427fcec1b807cfdacacdbe8525fbc516c2f86/research/hm/null-order-three-ambient/third-order/RESULT.md), commit `2f4427fcec1b807cfdacacdbe8525fbc516c2f86`. Its scalar c is regular and existential under its stated equivariant acyclic hypotheses.

## Retained hypotheses and boundaries

The general theorem requires a smooth characteristic-zero scheme, the stated G-invariant affine acyclic cover, normalized regular differential associative local products with reversal parity, genuine literal lower descent, even lower maps, and reversal-unitary lower scalar units. The latter is checked explicitly for the fourth-order application, not inferred from geometric inversion. Geometric inversion fixes h and is distinct from reversal h -> -h.

The even theorem uses H^2(T_X)^G=0. The odd fixed-map theorem requires the literal local defect to vanish and uses H^3(O_X)^G=0 for the scalar repair. The adjustable-product addendum additionally uses H^1(wedge^2 T_X)^G=0. Each vanishing is verified for geometric inversion on an abelian variety.

The fixed-product theorem and odd repair lemma themselves assume local associative parity extensions. The separate REVERSAL-COMPATIBLE-CONTINUATION.md now resolves their existence input existentially using the [prior literal lifting proof](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6259748725), followed by averaging only the new local product coefficient. The result selects an all-orders continuation with parity products, even overlap maps, and reversal-unitary units, preserving every supplied finite coefficient. It allows higher local products to vary and does not classify or normalize every preselected full continuation.

No explicit fifth local coefficient, arbitrary fixed-product all-orders extension, module lift, period, actual HM source value, algebraicity, or six pure diagonal condition vanishing is supplied. The fixed fifth-product counterexample remains valid and does not evaluate the selected source.

## Continuation dependencies and review

The continuation uses the complete parity-separated proof and repair lemma at [PR409](https://github.com/Akilleez-QA/read-em-and-weep/pull/409), commit `59fc9cdc40cf9a21fbb38549767829ff7471294f`, plus the exact literal lifting source linked above. The old source repairs any preceding invariant literal presentation, not merely its equivalence class. Its explicit application is the elliptic fourfold, and the general abelian statement retains the same regular differential, affine-acyclic, and inversion hypotheses. CONTINUATION-REVIEW.md records independent verification of this premise and the top-only averaging induction. The earlier proof files are unchanged.
