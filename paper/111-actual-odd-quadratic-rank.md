# The actual odd quadratic has rank eighteen

**PR1089 update, 23 October 2026:** [Actual residual Koszul lifts](112-global-alternating-vanishing.md) now prove combined T-rank four and κ=0 in all remaining mechanisms. The odd radical is not nullhomotopic; K3/F3 has character 2W′+3S. The unselected rank-three/rank-four interface below records the earlier checkpoint, not the current frontier. Zero R and hence zero full bilinear transfer remain unexcluded.


**23 October 2026 · PR1086, read in full**

[Immutable proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/acb56908fd28ff019515b7ad9945f9b539f8614a/research/hm/source2-pure-v-odd-quadratic-rank/PROOF.md), blob `d3d0f0546c5b2b7d2453929364287b35f03e4d2e`.

## Exact actual map

Under actual source2 nonzero pure-V Q-compatible radical hypotheses, multiplication by the same invariant quadratic in odd degree has

    im Q3 = the full T-isotypical component of M5₋=W′+3T,
    coker Q3 = W′,
    rank Q3 = 18,
    ker Q3 ≅ 3W′+3S+3T.

The T-multiplicity map C⁶→C³ has exact rank three; its W′ component is zero. This concerns the actual invariant rank-three quadratic, not a generic smooth quadratic, a sampled source instance, or the surviving positive component.

## Why the rank is actual

The fixed-variable quotient bundle ℚ has separated part Sym⁸W⊗O(2) and residual extension 0→O(18)→R*→A⊗O(6)→0. Twisting by −3 gives H¹(ℚ(−3))=0, so the binary Euler sequence proves actual first multiplication W⊗N2→M3 is onto, without splitting the residual extension.

Literal polynomial commutation therefore gives im Q3=μ(W⊗im Q2). Combine this with the actual exact Koszul sequence 0→M3→W⊗M4→M5→0. Since ker j4=im Q2 and im j4=I4, quotienting by W⊗im Q2 identifies the odd cokernel with the exact quotient

    0 → I3 --δ--> W⊗I4 → coker Q3 → 0.

The projected Koszul map is literally δj3 by radical intertwining, so its image is the marked δI3, not a guessed copy of T. Since I3=T and W⊗I4=W′+T, the cokernel is W′. Equivariance then determines the image and kernel characters above. No semicontinuity or smooth-quadric rank theorem is substituted for these actual maps.

## Remaining odd homotopy interface at PR1086

Q3(I3)=0. An equivariant nullhomotopy k:M5→M3 of (j3,0) must satisfy

    kQ3=j3,    Q3k=0.

It exists exactly when j3(ker Q3)=0, equivalently when the combined T-multiplicity map (Q3,j3) has rank **three rather than four**. If it exists, there is a unique such k with image in the marked I3: factor j3 through im Q3 and extend by zero on W′. Without the marked-image restriction, solutions form an affine three-dimensional space, since their differences lie in Hom_G(coker Q3,ker Q3)≅C³.

**The combined row alignment is unselected in PR1086.** Its abstract rank-three and rank-four controls are not actual source2 examples. The [mixed syzygy](110-mixed-syzygy-transfer.md) gives a conditional obstruction involving the alternating coefficient, but these two publications do not decide that coefficient or the combined rank.

Endpoint sixteen remains the only necessary generated endpoint, with the nonzero-N0 and residual-large mechanisms unresolved. Four necessary source-dual pairs remain. No positive-map solution, full adjoint invertibility, actual realization, or new source exclusion is claimed. Exact finite checks support the Euler, Koszul and representation computations; they do not replace the written actual-map proof.
