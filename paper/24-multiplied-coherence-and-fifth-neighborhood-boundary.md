# 24. Multiplied coherence, actual fifth-neighborhood boundary, and top-kernel pruning

**Current supersession (09:08 UTC):** [Chapter 25](25-complete-two-two-exclusion-and-actual-third-neighborhood-square.md) closes the entire (2,2) profile and proves square-zero for the existing actual J3 on 3Q. Dated candidate counts and open (2,2) statements below are historical. The fourth value, stronger global rank bounds, midpoint 3Q extension and original repair are not established.


**Checked-source cutoff: 22 October 2026, 08:30 UTC.** This chapter adds the published actual multiplied-lift coherence, its exact endpoint normalization, an actual-neighborhood interpretation of the fourth gate, and a further necessary (2,2) exclusion. The fourth value is not computed. General sections remain four or five; the original source, higher-lifting and Weil-class algebraicity goals remain open.

## 24.1 Coherence determines the positive endpoint scalar

Retain the actual family U_a of Chapter 23, q=q₀, r=a_m/b_m, κ=−(χ/g_L)r, r_ξ=k/κ, and ξ=δ_q(N)=r_ξ At_F(D0). For negative quadratics use the unnormalized first transvectant {a,b}=a_s b_t−a_t b_s. The actual induced sheaf morphisms satisfy

    aU_b−bU_a=−(κ/2)q{a,b}N,
    U_a U_b=U_b U_a=0 on actual 2Q.

Here q{a,b}N is the canonical square-zero-ideal image from Q; it assumes no lift of N. The first identity is nonzero whenever {a,b} is nonzero. Thus U_a is not a times a globally framed lift of N. Pairwise zero products strengthen the earlier polarized anticommutator identity; they are statements about induced sheaf maps, not raw monad components. [Coherence proof][COH]

Indeed, with P=P_nat, T_a=T_nat(a), set L_ab=aT_b−bT_a. Its differential is −qκ(a e_b−b e_a). Binary Euler and the projective negative-block Euler field give the actual trace-free Atiyah-class equality

    a At_F(D_b)−b At_F(D_a)=−{a,b}At_F(D0)/2.

The pinned H⁰(B(4))=0 makes the q-boundary injective and yields L_ab|Q=(κ/(2r_ξ)){a,b}N without an unknown scalar. Since aU_b−bU_a=−r_ξqL_ab, coherence follows. The cochain commutator modulo q² is −r_ξ²q[P,L_ab]. The induced commutator on Q is zero because both factors are multiples of N; multiplication by q factors through this induced map. Combining commutativity with polarization of U_a²=0 proves both products zero in characteristic zero. No global chain null-homotopy is asserted.

On s≠0, write z=t/s and q_s=q/s². For a=s²A(z), coherence gives the exact section-family factorization

    U_a=A(z−κq_s)U_(s²) mod q².

The volume-compatible opposite coordinate w=−s/t has w'=w−κq_t=−1/(z−κq_s) modulo q². In the unoriented coordinate s/t the correction instead has a plus sign. This factorization does not assert a globally flat kernel or image line bundle.

The local lifts N_s=U_(s²)/s² and N_t=U_(t²)/t² satisfy N_t−N_s=−2κqN/(st). Consequently ξ_Q=−2κ[N/(st)] on Q minus C, where C=(s=t=0). The full actual apolar comparison gives [η_ap,N]=2[N/(st)] there. Restriction cannot erase this class: s,t form a regular sequence along C, B_Q is locally free, and H¹_C(Q,B_Q)=0 makes H¹(Q,B_Q)→H¹(Q minus C,B_Q) injective. This is a full-class comparison, not inference from a lowest diagonal coefficient.

For the positive displacement η_+=c_+η_ap, the fixed boundary ξ_Q=−[η_+,N] therefore determines

    c_+=κ=−(χ/g_L)r,
    C_ap/K_cup=−2χ/g_L,
    k=−θκ²/(2ρ_C)=−θχ²/(2C_res g_L²).

The bracket-normalized displacement has coefficient −κ. Equation, volume, residue, edge and normal-cup markings remain fixed; no constant is set to one. Under q₀↦νq₀, c_+,χ,κ divide by ν and k divides by ν². Marked endpoint exchange changes the signs of c_+,κ but not the fixed-boundary k. These identities do not evaluate a fourth coefficient.

## 24.2 The exact actual 4Q-to-5Q boundary comparison

Let Z_a represent ζ_a and dU_a=q²Z_a. Fix a, h∈D5 and the established Schur/Bockstein choices, with b=L_can(a,h). The proved second and third vanishings give actual classes v_h,w_h∈H¹(B(2)) satisfying

    qv_h=ahζ_a,
    qw_h=a(v_h−bζ_a).

For every t≥2 the full monad endomorphism-complex terms have vanishing positive cohomology. The only less immediate term is End(K)(t): its Schur summands have largest partition part at most two and twist t+1≥3, so the pinned Bott-dominance argument applies uniformly. Hence global cochains compute H¹(B(t)); the fixed-duality projection retains trace-free primitives.

Choose global closed representatives V_h,W_h and global degree-zero twist-four primitives C_h,E_h with

    dC_h=ahZ_a−qV_h,
    dE_h=a(V_h−bZ_a)−qW_h.

Their existence is justified, but their explicit evaluation is not supplied. Define

    J3=(ah−qb)U_a−q²C_h,     twist eight,
    J4=aJ3−q³E_h,            twist ten.

Then dJ3=q³(V_h−bZ_a) and dJ4=q⁴W_h exactly. These induce trace-free sections on actual 3Q and actual 4Q, restricting to a²hN and a³hN on Q. The neighborhoods are restrictions of the actual ambient bundle, not a hypothetical extension of the midpoint bundle. Local splitting at the monad ends justifies restriction to these nonreduced bases. [Actual boundary proof][BOUNDARY]

For the actual sequence

    0 → B_Q(4) —q⁴→ B_(5Q)(12) → B_(4Q)(12) → 0,

the section aJ4 has boundary

    ∂5(aJ4)=[aW_h|Q] ∈ H¹(B_Q(4))₊=P4,
    β4_a(h)=[∂5(aJ4)] modulo im(β2_a).

Thus the particular section extends to 5Q exactly when its raw boundary is zero. Vanishing of the fourth quotient is weaker: a nonzero raw boundary may lie in the second-symbol image. The generic quotient is a line; no constant target dimension at the six exceptional axes is assumed. Closed changes of C_h,E_h with V_h,W_h fixed do not alter this boundary. Other representative changes retain the usual Bockstein indeterminacy, not automatic zero before quotient.

This is an exact actual-neighborhood comparison, not the value of the boundary. Constructing/evaluating the primitives or equivalent full actual geometric data remains necessary. It does not identify a truncated vertex transport with the fourth gate or construct a 3Q midpoint extension.

## 24.3 Top-kernel multiplicities leave 24 necessary pairs

Chapter 23's 1,880 records and 34 quotient pairs refine to **1,221 records and 24 pairs**: 1,064 defect-zero and all 157 defect-twelve records. The ten newly excluded pairs have defect zero. The (2,2) profile itself remains open. [Top-kernel proof][TOP]

Write K=E⁻, L=(Q*)⁻, with full derivative quotients A_q=E/K and B_q=Q*/L. For either kernel N and corresponding quotient C_q, write N=⊕_(j≥d) R_j O(−j), with R_d nonzero and d≥3. The second fundamental form factors N→C_q(−2). Strict top-slope decrease, applied at the kernel's own top degree, forces an injection of representations

    R_d=H⁰(N(d)) → H⁰(C_q(d−2)).

A killed constant coefficient would select a saturated top-degree line O(−d). Its derivative modulo N vanishes, and its derivative within N lands in a bundle of degrees at most −d−2, hence also vanishes. Such a horizontal line in a constant bundle has degree zero, contradicting d≥3. This is global-section injectivity, not fiberwise derivative injectivity. The earlier twist-three constraint was empty for a kernel whose actual top index is four; the new test covers that case and every higher top index.

Every compatible L splitting for each excluded pair has top degree −4 and two V copies in H⁰(L(4)), but H⁰(B_q(2)) has only one. All ten satisfy B_q=A_q*(−2); their A_q are

1. O(−10)⊕O(2)⊕O(4).
2. O(−10)⊕O(2)⊕O(6).
3. O(−10)⊕W O(3).
4. O(−10)⊕2O(4).
5. O(−10)⊕O(4)⊕O(6).
6. O(−10)⊕W O(5).
7. O(−10)⊕2O(6).
8. W′ O(−3)⊕O(4).
9. W′ O(−3)⊕O(6).
10. V O.

The target characters are respectively Sym¹⁰W, W′⊗Sym³W, or V, each with V multiplicity one. The common certificate is checked for every compatible candidate, not one example. All 659 newly removed records fail on the L side; both towers are tested. Before discarding records, candidate occurrences change from 5,478 to 5,318 on K and 4,266 to 2,455 on L. These are occurrences, not distinct bundle types. A record survives only with a passing candidate on each side.

The fixed histories are pairs 35→34→24 and records 2,947→1,880→1,221. Surviving entries are necessary formal possibilities, not realizations or a moduli count. Four maximal profiles remain possible: (1,1), (1,2), (2,1), (2,2). SF≥3 and square rank≥27 are unchanged.

## 24.4 Evidence and project-wide perspective

The new proofs were read in full, independently audited and checked against exact immutable published readbacks before integration. Companion verifiers passed. They check universal identities, twists and abstract character multiplicities, not selected actual-instance coefficients or numerical ranks; they are not proof-assistant certificates.

The [progress map](progress-map.md) displays whole-project scopes, completed early lanes and the fixed-denominator Gauss refinements. The underlying inventory has 26 separately scoped universes. Neither these overlapping universes nor the editorial eight-objective roadmap define a natural global family count or a percentage complete. The exact fourth value, original source recovery, required higher lifting and Weil-class algebraicity remain unresolved.

## Immutable source ledger and reproduction

All paths are under research/hm/order-four-quadratic-load in PR543. Run the scripts with their published imported helpers.

- At `2e20281e6eb850904093af3a6c737f3ee0ed28f2`: [coherence and endpoint scale][COH]; [coherence verifier][COHV]; [actual fifth-neighborhood boundary][BOUNDARY]; [boundary verifier][BOUNDARYV].
- At `1c00faf07673db5b2e1cf2cbf23984f4a31503b1`: [top-kernel proof][TOP]; [multiplicity verifier][TOPV]; [compact 24-pair summary][SUMMARY]. Running the latter verifier with --full regenerates its separately named survivor-record file. Its input digest check preserves the frozen exact-kernel record file.

[COH]: https://github.com/Akilleez-QA/read-em-and-weep/blob/2e20281e6eb850904093af3a6c737f3ee0ed28f2/research/hm/order-four-quadratic-load/ACTUAL-MULTIPLIED-NILPOTENT-COHERENCE-FIXES-ENDPOINT-SCALE.md
[COHV]: https://github.com/Akilleez-QA/read-em-and-weep/blob/2e20281e6eb850904093af3a6c737f3ee0ed28f2/research/hm/order-four-quadratic-load/verify_actual_multiplied_nilpotent_endpoint_coherence.py
[BOUNDARY]: https://github.com/Akilleez-QA/read-em-and-weep/blob/2e20281e6eb850904093af3a6c737f3ee0ed28f2/research/hm/order-four-quadratic-load/ACTUAL-FOURTH-BOCKSTEIN-AS-A-FIFTH-NEIGHBORHOOD-ADJOINT-BOUNDARY.md
[BOUNDARYV]: https://github.com/Akilleez-QA/read-em-and-weep/blob/2e20281e6eb850904093af3a6c737f3ee0ed28f2/research/hm/order-four-quadratic-load/verify_actual_fourth_normal_neighborhood_boundary.py
[TOP]: https://github.com/Akilleez-QA/read-em-and-weep/blob/1c00faf07673db5b2e1cf2cbf23984f4a31503b1/research/hm/order-four-quadratic-load/TWO-TWO-TOP-KERNEL-MULTIPLICITY-EXCLUDES-TEN-PAIRS.md
[TOPV]: https://github.com/Akilleez-QA/read-em-and-weep/blob/1c00faf07673db5b2e1cf2cbf23984f4a31503b1/research/hm/order-four-quadratic-load/verify_two_two_kernel_top_multiplicity.py
[SUMMARY]: https://github.com/Akilleez-QA/read-em-and-weep/blob/1c00faf07673db5b2e1cf2cbf23984f4a31503b1/research/hm/order-four-quadratic-load/two-two-kernel-top-multiplicity-summary.json
