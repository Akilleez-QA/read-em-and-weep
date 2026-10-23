# 143. Three source branches excluded; a three-pair necessary D frontier

**Craig Ward · 23 October 2026 · Frozen source-coverage checkpoint through PR1161, PR1162 and PR1164**

## Combined result

Three independently checked deductions now combine under the original actual-geometric and profile-(1,1) necessity hypotheses:

- [P-source closure, PR1161](https://github.com/Akilleez-QA/read-em-and-weep/blob/0dfc26b49b18fb60dce58e95f1d74c7d06d16378/research/hm/p-source-profile11-closure/PROOF.md) excludes P throughout this maximal profile.
- [V/Z-source closure](https://github.com/Akilleez-QA/read-em-and-weep/blob/49c8d0226a7e79928a016783553fa8c29c2c6b9a/research/hm/v-z-profile11-closure/PROOF.md) excludes V and Z throughout the same profile.
- [D-source reduction](https://github.com/Akilleez-QA/read-em-and-weep/blob/54f5a5b76932e56714dfc74730e175271701dfc2/research/hm/d-source-profile11-frontier/PROOF.md) leaves exactly three necessary ordered quotient pairs, with two A shapes.

The four-source theorem therefore reduces any actual maximal profile-(1,1) occurrence, under these imported hypotheses, to D and the table below. This is genuine source-branch coverage, not a percentage of global proof completion. It does not assert realization of any residual pair, freedom from every other obstruction, or complete profile closure. Other-profile exhaustion and the original proof repair remain separate obligations.

This chapter freezes the combined source-closure/frontier checkpoint through PR1161, PR1162 and PR1164. It is not the current residual frontier after later exclusions. The subsequent checked closure is recorded separately in [chapter 144](144-maximal-profile11-closure.md). [Chapter 142](142-complete-rank-one-flag-exclusions.md) and the delivered PDF remain unchanged historical snapshots.

## Exact necessary ordered pairs

Let K=E⁻, S=Q*, L=S⁻, A=E/K and B=S/L. The actual E and S have ranks 17 and 13 and degrees -54 in their constant ambients; K and L have ranks 14 and 10. The original ambient H has dimension 30, not the dimension-54 coefficient presentation. The only source not excluded by these combined results is

    E = D O(-2) + (W′+T) O(-3) + V O(-4) + O(-8).

Here W is the standard doublet and D=Sym⁴W. The determinant defect is t=-6-deg A-deg B.

| Original zero-based identifier | A | B | Defect t |
| --- | --- | --- | ---: |
| 32 | O(-8)+O(2)+O(4) | O(-18)+O(-4)+O(6) | 12 |
| 50 | O(-8)+O(2)+O(4) | O(-6)+O(-4)+O(6) | 0 |
| 52 | W O(3)+O(-8) | W O(-5)+O(6) | 0 |

The numbers 32, 50 and 52 are immutable historical identifiers. The **three-pair necessary frontier** is a mathematical consequence of the original written necessity theorem together with source-specific exclusions; it is not inferred merely from those identifiers or a JSON count. It is necessary only, not a construction of three actual configurations.

## Common geometric tool: the complete dual-endpoint capacity

For maximal profile (1,1), L is the lower endpoint of the reversed dual plateau, so its derivative has rank at most two. The dual S is negative, with top degree at most -1. No stronger profile-(2,1) bound top S≤-2 is imported.

Successive actual Gauss kernels F₀=S, F₁=L, F_(j+1)=F_j⁻ remain saturated and negative in the constant ambient. A nonzero horizontal saturated subbundle would be constant, contradicting negativity; hence the flag terminates at zero. With G₀=B and G_j=F_j/F_(j+1), the actual derivative gives injections

    G_j → G_(j−1)(-2) → B(-2j).

No saturation of these images and no horizontal Birkhoff splitting is assumed. Their positive ranks are nonincreasing, at most two, and sum to ten. If h₁ counts the nonzero ranks and h₂ those equal to two, then h₁≥h₂≥0 and h₁+h₂=10. There are six possibilities, h₁=5,...,10.

For the ordinary degrees λ₁≥λ₂≥λ₃ of B, determinants and degree additivity give

    deg L ≤ h₁λ₁−h₁(h₁+1) + h₂λ₂−h₂(h₂+1).

The maximum of these six integers is an upper bound for deg L=-54-deg B. In particular top B≤-1 forces deg L≤-70. This works for rank-one as well as rank-two endpoints and for unsaturated derivative images. It is the common final obstruction in the three eliminated source branches and an important filter for D.

## P, V and Z: complete source-conditioned exclusions

The source compatibility tests come from E→A and B→E*(-2): for every prescribed twist u=-10,...,10, H1(A(u))≤H1(E(u)) and H0(B(u))≤H1(E(-u)). They are necessary only. Each proof recomputes them on the immutable original 159 records and checks agreement with stored source tuples; it does not regenerate the old candidate classification.

For P, the 35 compatible records have a disjoint covering:

    35 = 16 cubic visibility + 6 doublet-endpoint exclusions
            + 2 complete-flag exclusions + 11 dual-capacity contradictions.

The six and two groups are the four A-shape exclusions recorded in chapters 141 and 142. The last eleven B bundles all have negative top degree, but require deg L=-38, -36 or -34, exceeding even the uniform capacity -70. Their exact capacities range from -125 to -70. Thus every actual P-source occurrence in this profile is impossible.

For each of V and Z, there are 34 compatible historical records. PR1140 gives cubic-kernel vanishing unconditionally in these two sources. Strict-top then injects H0(K(4)) into H0(A(2)), making the signed quartic envelope

    H0(A(2)) + χ_G(A(4)) − (3V+3P+2D)

 genuine. The disjoint covering for each source is

    34 = 16 cubic visibility + 7 quartic contradictions + 11 dual capacity.

The seven quartic contradictions have V multiplicity -1; no P-source forced-endpoint alternative is needed. The final eleven records are the same negative-top dual-capacity cases. This excludes each source throughout maximal profile (1,1), including positive-defect possibilities, under the pinned original necessity theorem.

These are exact covering certificates for fixed source-conditioned overlists. Their category counts are not additive totals of newly live exclusions. The closures follow because every actual occurrence must be covered by that original necessity theorem and must pass the relevant necessary tests.

## D: complete reduction, but not closure

D has 102 compatible historical records. Cubic visibility eliminates 32, and the complete dual capacity eliminates 62 of the remaining 70. Eight records pass those two tests. The full pinned theorems PR1135 and PR1142 each remove two by their actual D-source A-shape exclusions; PR1145 removes the remaining O(-8)+O(2)+O(16) record by its full profile-(1,1) argument, not by capacity equality alone.

The disjoint sequential certificate is

    102 = 32 cubic + 62 capacity + 2 PR1135 + 2 PR1142
             + 1 PR1145 + 3 necessary residual pairs.

The other 57 of the original 159 are D-incompatible. Again these are historical certificate categories, not fresh live-cut totals.

For the residual pairs, the six capacities for h₁=5,...,10 and the required degrees are:

| Identifier | Six capacities | Required deg L |
| --- | --- | ---: |
| 32 | -50, -42, -38, -38, -42, -50 | -38 |
| 50 | -50, -42, -38, -38, -42, -50 | -50 |
| 52 | -55, -46, -41, -40, -43, -50 | -50 |

Pair 32 reaches equality only at height pairs (7,3) and (8,2); equality does not itself exclude it. Pairs 50 and 52 also pass this capacity necessity. No further residual-map or jet conclusion is asserted at this checkpoint.

## Evidence and remaining boundary

Each complete proof and its independent written review were read. The frozen proof hashes are:

- P: `d3e4714dc5808474ae664824c36a2d81975e29d40a6f2c99309542afdba8713a`.
- V/Z: `b344bb861ac283d1f997de2ac7d281938913a4a9e471a0c7545e81ed2e6d8e61`.
- D: `7a21b3efdd1326266623093f3b1d2c6f95c13027c73c8d3ccb005134b9ed443e`.

P has eleven authenticated originals and 839 explicit author controls plus 81 character controls, with 4,733 independent controls. V/Z has eight originals, 1,135 plus 81 author controls and 5,248 independent controls. D has nine originals, 1,204 plus 81 author controls and 6,676 independent controls. Normal and optimized Python outputs match. Independent class-character calculations reproduce every source decision, signed witness and capacity; the geometry and transfer scopes were checked separately from arithmetic.

These are written proofs relative to explicit pinned inputs, not proof-assistant verification or a new proof of the entire historical dependency chain. No actual coefficient, selected point, parameter, jet, matrix, instance rank, regenerated historical enumeration or stopped experiment was used. Three source branches are excluded within profile (1,1), and D has the stated necessary three-pair frontier. Full profile closure, broader coverage, full-adjoint invertibility and the original theorem repair are not claimed.
