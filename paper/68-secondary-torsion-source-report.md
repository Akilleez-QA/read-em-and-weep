# The completed secondary torsion alternative

**Craig Ward · 23 October 2026 · Source report through PR1024**

This chapter reports mr. slop's full immutable proofs, **not an independent reproof**. Sources: [PR1021](https://github.com/Akilleez-QA/read-em-and-weep/blob/cbeaab81e4d6b08f6ffdf9e743b0cfc600119999/research/hm/secondary-v-only-branch/PROOF.md), [PR1024](https://github.com/Akilleez-QA/read-em-and-weep/blob/e9ded1144a4eb199196e8e86201bfb1245f9e2cd/research/hm/secondary-universal-torsion/PROOF.md).

## 1. Actual six-channel problem

The actual first-cup kernel K=T₆O(-1)⊕AO(-2) has square subbundle AO(-6), with quotient Q=PO(2)⊕WO(-1). The reduced secondary boundary b:Q→(V+P+D)O(4) has six inherited coefficients (a_J,b_J) in the two channels for each J=V,P,D. The original β is its composite with K→Q and has an additional zero A target row. Actual quartic transition corrections remain in these coefficients.

Without assuming which coefficients vanish, PR1024 proves that, for generic rank r,

    I_r(β)=O or I_Ω,

where Ω is the reduced twelve-point orbit and I₀=O. The cokernel torsion is correspondingly zero or exactly twelve simple residue-field factors, one at each orbit point. There is no other support or higher local multiplicity. **The actual alternative is unselected.**

These ideals use r-by-r matrix minors. For the original rank15 target they are Fitt_(15-r)(coker β), and for the reduced rank12 target Fitt_(12-r)(coker b). They are not a single fixed Fitting index across changing-rank branches.

## 2. V-only branch: constant rank but changing kernel type

PR1021 assumes a_D=a_P=0 and a_V≠0. The actual V-row pullback kernel surjects onto WO(-1); the remaining rows therefore give constant ranks5,4,3 according as b_P≠0, only b_D≠0, or both vanish. There is no torsion in this branch.

Two actual nonzero maps on the canonical AO(-2) summand determine a unique nonzero cancellation ratio η. Its numerical coordinate is unselected, but Δ=b_V−ηa_V=0 is intrinsic. The original kernels are:

| Remaining rows | At Δ=0 | At Δ≠0 |
|---|---|---|
| b_P≠0 | AO(-6)⊕O(-4) | AO(-6)⊕O(-4) |
| b_P=0, b_D≠0 | AO(-6)⊕WO(-3) | O(-4)⊕SO(-5) |
| b_P=b_D=0 | AO(-6)⊕AO(-2) | (1+D)O(-4) |

Actual pullback extensions and graph lifts are retained, including b_V=0. Thus the splitting discriminant can change the kernel type without changing fiber rank. No actual Δ or branch is chosen.

## 3. Exhaustion and the final torsion mechanism

PR1024 combines the previously proved two-D-channel and mixed V/P strata with the V-only case and three new strata:

1. a_D≠0, b_D≠0: prior two-D-channel case.
2. a_D≠0, b_D=0: constant rank6 or4.
3. a_D=0, a_Va_P≠0: prior complementary-channel case.
4. a_D=a_P=0, a_V≠0: V-only case above.
5. a_D=a_V=0, a_P≠0: P-only case.
6. a_D=a_V=a_P=0: constant rank2,1 or0.

The partition is disjoint and exhaustive, with no restrictions silently imposed on the remaining b coefficients. In the new P-only case, quotienting the P target by its actual image leaves a W-source map with V, W′ and D target components. Its W′ component is a nonzero scalar multiple of b_P times the unique determinant-f₁₂ map WO(-1)→W′O(5). The pure determinant subcase has local Smith form diag(1,t) at Ω. Mixed determinant/Euler components have distinct kernel characters there and retain full rank. This proves simple torsion rather than merely detecting a rank drop.

Whenever the P-only residual map is sheaf-injective, the generic-rank-four original kernel is VO(-2)⊕WO(-5), derived through its actual nonsplit extension, not assigned from characters. The zero-P-source cases instead give T₆O(-1)⊕O(-4), T₆O(-1)⊕WO(-3), or K, respectively. Adding the zero target row and the locally split kernel columns does not change the relevant minors or torsion.

## 4. What is finished and what remains

This completes the secondary rank-drop support/multiplicity question across all coefficient branches. It does not select zero versus length12 torsion, the full torsion-free quotient, the next obstruction, top-polar σ, vertex scalar, global quadric conclusion or a source-dual pair. At a torsion point the fiber kernel is one dimension larger than the kernel sheaf's fiber, so those must not be equated.

This secondary torsion alternative is distinct from the already proved **zero actual opposite-pencil torsion** in PR945. It is also distinct from source2's pure-V secondary chain endomorphism and its quotient-third gate. Similar terminology does not identify these maps.

The sources report independent mathematical reviews, exact-input authentication and ordinary/optimized bounded checks; PR1024 reports two independent reviews. No selected actual coefficient or instance rank is evaluated. Four necessary source-dual pairs across three stable labels remain.
