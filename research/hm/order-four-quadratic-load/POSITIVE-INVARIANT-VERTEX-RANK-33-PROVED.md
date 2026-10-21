# The actual positive invariant-vertex map has rank 33

Let q0 be the invariant rank-three positive quadric and E=F_Q0(2). The actual positive multiplication map H1(B(2))_+ -> H1(B(4))_+ has rank exactly 33.

The ambient H0(B(2)) and H0(B(4)) vanish. Its kernel is therefore H0(B_Q0(4))_+. The cone-spinor construction provides the invariant nilpotent N. The moving-line theorem proves that every positive adjoint preserves its saturated spinor S. The uniform Ext-annihilator theorem then proves that every such preserving adjoint is a polynomial multiple of N. Consequently

    H0(B_Q0(4))_+ = N H0(O_Q0(2))_+ = A + D5,

with dimension eight. The source has dimension41, so the rank is41-8=33.

Subtracting this kernel from the source character A+2V+3P4+4D5 gives image 2V+3P4+3D5. The target is 2V+4P4+3D5, so the cokernel is exactly P4, dimension four.

Thus the rank hypothesis in POSITIVE-INVARIANT-VERTEX-ONE-SCALAR-GATE.md and POSITIVE-GAMMA-TWO-LINEAR-STEP-CRITERION.md is now established, not assumed. The remaining first-smoothing map is the scalar gamma times the universal A tensor D5 -> P4 channel. The uniform multiplicity-leg theorem proves its two selected legs are nonzero, but their pairing remains unproved. If gamma is nonzero, the prior smoothing theorem gives positive generic surjectivity and exactly four positive sections. This note does not claim gamma nonzero or generic positive surjectivity.

The generic odd sector is separately proved to vanish by SPECIAL-D5-OCTIC-NONEXTENSION-EXCLUDES-A12.md. Neither that theorem nor this invariant-vertex theorem alone completes the original source/lifting/Weil-class algebraicity objective.

## Checked dependencies

- INVARIANT-CONE-SPINOR-FILTRATION-AND-NILPOTENT.md: actual saturated spinor, nilpotent and its exact centralizer.
- INVARIANT-CONE-UNIQUE-VERTEX-MODULE.md: actual unique module and Loewy dimensions2,3,2.
- NO-PRESERVING-POSITIVE-CONE-EXCESS.md: uniform Ext filtration and vanishing preserving excess.
- POSITIVE-CONE-MOVING-LINE-OBSTRUCTION-VANISHES.md: every positive actual adjoint preserves S.

All inputs have independent mathematical checks and exact universal verification artifacts. This is not a formal proof-assistant certificate. No actual coefficient selection, selected matrix-rank evaluation, or previously consumed experiment is used.
