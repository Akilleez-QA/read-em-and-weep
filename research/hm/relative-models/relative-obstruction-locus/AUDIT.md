> Publication scope: Rank352 obstruction bundle and relative zero scheme; P and S remain imported. The original D table is now independently supplied by cubic P01, not newly recalculated here. Source-stage audit/checker references describe historical evidence, not fresh execution or bundled executable artifacts. Named source identities are hypotheses unless separately proved below.

# Independent structural audit

The argument in `PROOF.md` is sound with its stated, separated premises P, D, and S. This audit used static reading and formal reasoning only. No source/model, matrix, rank, polynomial instance, point, jet, residual, or detector was evaluated.

## Bundle construction

- The sparse Kodaira–Spencer proof genuinely extends to every independent generating tuple: the line-bundle cohomology, strict lifting, singleton-row reduction, and coefficient-only sparse argument are unchanged. The fixed deck-equivariant family makes these 79 directions invariant classes.
- Central dimensions D, upper semicontinuity, the scalar endomorphism, and this uniform lower bound give invariant dimensions `(1,79,352,0,0)` on an open neighborhood. Euler characteristic 274 follows from D and local constancy; no additional historical rank certificate is used.
- On the reduced smooth base, constant dimensions in every degree give local splitting of the perfect invariant complex. This establishes locally free cohomology and arbitrary, including nonreduced, base change. The same conclusions for the full-sign summand follow from Serre duality with the full-sign volume character. In particular its degree-two bundle has rank 352 and its degree-one cohomology vanishes.

## Relative class and zero scheme

Under S, the source-family theorem supplies an actual regular relative cocycle, not merely fiberwise closed values. A finite affine refinement over affine B converts it into the asserted algebraic relative class. Projection on cohomology requires no equivariant choice of source frames. A deck-stable refinement also permits cochain projection. No additional gluing premise is needed on this fixed normalized chart; descent across different parameter normalizations is not established or used.

The zero-scheme and arbitrary-base-change claims are correct. For nonaffine test schemes the relative-section formulation is the appropriate claim. The formal zero locus through the original parameter can be empty; membership of the original point is not proved.

## Corrected derivative in §7

The sign is correct: differentiating `T(Q)=G⁻¹QG` gives `dotδ(Q)=[T(Q),a]`. Subtracting the lifted coboundary before differentiating gives the closed cochain

    D = dot R − dotδ(Q) − δ(dot Q).

Its class is the intrinsic derivative of the section at a zero. The derivative of a varying character projector must be included in `dot R`, as the proof explicitly requires. Changing the lift changes D by a boundary. Changing the full-sign primitive changes it by a boundary because full-sign H¹ vanishes and differentiation of δ²=0 gives `dotδ·δ=−δ·dotδ`.

One useful precision: an arbitrary non-equivariant lift of Q need not make D itself a full-sign cochain. Its cohomology class is full-sign; the other components are boundaries. Alternatively, average the lift in the first-order family to obtain a full-sign cochain D. The stated tangent-space criterion concerns its class and is valid either way.

## Exact remaining premises

P must concern the specified literal presentation; D must concern this same bundle and its induced deck action; S must include the actual homogeneous source identification, determinant normalization, and complete raw recipe. These inputs have not been independently certified here. Identification with the entire mixed-obstruction vanishing locus additionally requires full-sign purity of the entire relative mixed class. A pointed formal locus at the original parameter additionally requires vanishing there. None of these statements supplies higher-order lifting or algebraization.
