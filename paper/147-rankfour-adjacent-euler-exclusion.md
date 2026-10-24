# 147. Closing the forward-length-three row at rank four

**Craig Ward · 23 October 2026 · Two further coarse rank-four strata removed**

## Exact progress and counting boundary

The [adjacent-plateau theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/f20373720cfb785fe3d694f51e20efeb942fa45b/research/hm/rankfour-adjacent-plateau/PROOF.md) excludes generic SF rank four with ordered maximal plateau lengths (k,l)=(2,3), under the retained actual-geometric and fixed physical-marking hypotheses.

The [short-plateau theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/7e915f5febb13719536faadd42e94301a1b03df4/research/hm/rankfour-short-cubic-plateau/PROOF.md) independently excludes (r,k,l)=(4,1,3). Combined with the preceding (4,3,3) exclusion and the fixed [PR1171 partition](https://github.com/Akilleez-QA/read-em-and-weep/blob/8497b6e793f36c14448fecdf88d209971273e069/research/hm/remaining-rank-strata/PROOF.md), **26 necessary bad coarse bins become 24**. The rank-four group decreases from eight to six; the groups at ranks five through twelve remain 6,4,2,2,1,1,1,1. The optional source refinement decreases from 98 to 96, since only Z could occupy either removed forward-length-three bin.

Together the three checked exclusions remove the complete rank-four l=3 row: (1,3), (2,3) and (3,3). For r≥5 the rank budget already gives l≤2. Thus, under the retained hypotheses, **every remaining actual maximal plateau with r≥4 necessarily has forward length l≤2**. This does not impose k≤2: the backward direction remains distinct.

These are whole-stratum exclusions, not merely partial quotient filters. Nevertheless rank four remains possible in other bins: generic SF≥5 is not proved. The existing generic square rank≥28, kernel/positive double-hyperplane sections≤13 and cokernel≤9 bounds are unchanged. Rank thirteen would give positive-square auxiliary surjectivity, not by itself full-adjoint invertibility or the original repair.

The counts concern necessary containers, not realized examples, equally difficult tasks or a completion percentage. [Chapter146](146-remaining-rank-partition-and-first-rankfour-cut.md) remains the historical first-cut checkpoint. The new necessary forward bound does not assert that every retained bin is nonempty.

## Why the adjacent proof is shorter

Unlike the preceding corner proof, this argument needs no rank-four quotient enumeration, slope-window search or source-splitting classification. Two exact sequences contain the same quotient at different twists. Their Euler characteristics cancel that quotient and all unknown coefficient representations, leaving a contradiction between the two physically distinct three-spaces A₃=Sym²W and V.

The only actual source character used is

    χ_G(E(2))=-V,

derived from the original actual presentation. The proof does not import the rank-three pairing inequality, the preceding (3,3) theorem or its stronger quotient slope bound. Equivariant Birkhoff splitting is used for cohomology only, never as a horizontal splitting.

## Endpoint parity forces every determinant defect to vanish

The hypothetical actual saturated plateau is

    F₀ ⊂ F₁ ⊂ F₂=E ⊂ F₃ ⊂ F₄ ⊂ F₅,
    rank F_i=9+4i,       deg E=-54.

Interior derivative kernels and saturated transforms are the adjacent stages. Section persistence, including at both endpoints, gives H⁰(F_i(d))=0 for i+d<5 and the same vanishing for the reversed annihilators. At the lower endpoint, the first derivative containment follows because F₀ is the derivative kernel of F₁; its derivative rank need not equal four.

Thus all degrees of F₀ are at most -5, and the rank-one annihilator F₅⊥ has degree at most -5. Set a=deg F₀ and b=deg F₅=deg F₅⊥. The stage determinants are center-even, and the binary icosahedral group has no nontrivial one-dimensional character. Therefore their degrees are even, sharpening the bounds to

    a≤-46,       b≤-6.

This parity step is essential. The weaker ordinary bounds -45 and -5 would not force equality.

With L_i=F_i/F_(i-1) and c_i=deg L_i, the regular generically invertible derivative maps L_i→L_(i+1)(-2) give c_(i+1)=c_i+8+δ_i, where δ_i≥0 is the actual torsion-cokernel length. Eliminating c₁ gives

    3a+2b=-150+3δ₁+6δ₂+4δ₃+2δ₄.

The left side is at most -150 and the right side at least -150. Hence a=-46, b=-6 and every δ_i=0. The quotient degrees are (-8,0,8,16,24), and the stage degrees are (-46,-54,-54,-46,-30,-6). All adjacent graded derivative maps are isomorphisms, with no hidden torsion defect or assumed invariant-divisor gap.

Put B=L₂=E/F₁. The required graded identification is L₁=B(-2). This does not split the filtration or connection.

## All three low-stage tails are covered

Persistence and the exact degrees leave one unit of deficit in F₀ and two in F₁. Central parity gives

    F₀=R₈ O(-5)+O(-6),

and exactly three possibilities for F₁:

    R₁₁ O(-4)+W O(-5),
    R₁₁ O(-4)+W′ O(-5),
    R₁₂ O(-4)+O(-6).

R₈ is an unknown genuine odd representation, and R₁₁ or R₁₂ an unknown genuine even one. Their characters need not be classified. The two-dimensional odd coefficient can only be W or W′, while an even coefficient line must be trivial. These are complete small-deficit possibilities, not a chosen computational cutoff.

The two actual short exact sequences are

    0→F₀→F₁→B(-2)→0,
    0→F₁→E→B→0.

Twisting the first by four and the second by two eliminates the common B(2) in Euler characteristics:

    χ_G(F₁(4))+χ_G(F₁(2))
      = χ_G(F₀(4))+χ_G(E(2)) = -1-V.

All H¹ terms are included. No surjection on global sections is assumed.

For a doublet tail X=W or W′, the left side is -X⊗W: the R₁₁ terms cancel. The fixed physical products are W⊗W=1+A₃ and W′⊗W=P. Neither is 1+V. For the line tail, the left side is -1-A₃, again not -1-V. The trivial H¹ contribution from O(-6) at twist four has been retained, not discarded.

The three residual characters, left side minus right side, are

    V-A₃,       1+V-P,       V-A₃.

Each has ordinary dimension zero but is nonzero in the representation ring. Exact equality, not positivity or dimensions alone, is required by the actual sequences. All three tails are impossible, excluding the entire ordered (2,3) stratum.

## The short (1,3) plateau: two degree alternatives

The second proof treats the actual chain of ranks 13,17,21,25,29, with E at its second stage. Persistence gives a=deg F₀≤-52 and b=deg F₄≤-4, with both degrees even. For the three adjacent derivative defects, elimination gives

    3a+b=-168+3δ₁+2δ₂+δ₃.

Writing a=-52-2u and b=-4-2v produces

    6u+2v+3δ₁+2δ₂+δ₃=8.

Unlike the adjacent proof, here the invariant-divisor gap is used: any nonzero invariant effective divisor on the physical parameter line has degree at least twelve. The available slack is only eight, so every δ_i vanishes. Exactly two endpoint pairs remain: (-52,-12) and (-54,-6).

Persistence and the actual H¹(E(1)) character again derive E=(W′+2T₆)O(-3)+V O(-4) by the three-unit deficit argument, without historical source enumeration. Set B=E/F₀. The zero defects give the upper graded quotients B(2),B(4),B(6), not a horizontal splitting.

B has rank four and degree -2 or zero. Because B(4) is a quotient of the globally generated E(4), all its slopes are at least -4; total degree d then bounds each above by d+12. Exact cubic cohomology gives target W′+2T₆ in the degree-minus-two case and that target plus W or W′ in degree zero. The complete new abstract classification leaves five and eight cubic candidates. Exact quartic cohomology, retaining both allowed H¹ corrections, leaves two in each case.

## The full upper Euler identity removes all four survivors

The actual upper exact sequence is

    0→F₄→H O→O(-b)→0,
    H=2A₃+2V+2P+2D.

Perfectness leaves no hidden coefficient character on its quotient line. Additivity along the actual filtration gives at twist zero

    χ_G(E)+χ_G(B(2))+χ_G(B(4))+χ_G(B(6))
      +Sym^(-b)W-H=0.

This uses full Euler characteristics, not a surjection on sections or an assumed vanishing of H¹. In particular χ_G(E) is not zero. The four surviving candidates give:

| Endpoint pair (a,b) | B | Left side of the required identity |
| --- | --- | --- |
| (-52,-12) | W′ O(-3)+2O(2) | 1-A₃+D-V |
| (-52,-12) | V O(-2)+O(4) | 1+A₃-P |
| (-54,-6) | W′ O(-3)+O(2)+O(4) | V-A₃ |
| (-54,-6) | W′ O(-3)+W O(3) | V-A₃ |

All four characters are nonzero despite having dimension zero. Thus the upper exact sequence excludes every survivor and the entire (1,3) stratum. A cubic-only check would miss some of these obstructions; the twist-zero identity is essential. This proof is independent of the (2,3) and (3,3) exclusions.

## Verification and preserved scope

The frozen proof SHA256 is `de3bacb2f5a548637363e5a0f646123457c07dd5cbdaa3976c7a8e6c326db4eb`. The independent whole-proof review has SHA256 `93bbd87d4cfa7560b18a6952eda72b5c9714fc4342c8bcccf98b71ab602be5ff` and accepts the conditional exclusion. It checks both endpoint persistence arguments, the essential parity sharpening, every defect weight, the graded twist, all three tails and all cohomology corrections.

The independent verifier reconstructs exact conjugacy-class characters rather than importing the author's verifier or its McKay input. Negative controls alter source bytes, endpoint parity, defect weights, quotient twist, physical marking and the line-tail H¹ correction. Ordinary and optimized executions reproduce the frozen outputs. These universal controls support the written proof; they do not prove the inherited actual geometry or every transitive source theorem by computation.

The short-plateau proof has SHA256 `7ec277448b80a3f77300e7c7802b7ea49ef0a742e8a652270f3af9a957010a92`. Its independent whole-proof review accepts the conditional exclusion and independently reconstructs the forced-window classification: 37 degree-minus-two and 50 degree-zero abstract shapes, five and eight cubic candidates, and two quartic survivors in each case. All four exact upper residuals agree. Author controls report 1,250 checks and 81 mutation rejections. The final independent review SHA256 is `b8919e739a5d938d8494d8d29ae033e6256f6cf74a6925cbb81676dd52836313`; its controls report 3,114 checks and 17 negative controls.

No actual coefficients, parameter choices, jets, matrices or instance ranks are evaluated. The short proof derives a new bounded abstract quotient classification; no historical source enumeration is rerun. All prior chapters and the delivered v0.3 PDF remain unchanged.
