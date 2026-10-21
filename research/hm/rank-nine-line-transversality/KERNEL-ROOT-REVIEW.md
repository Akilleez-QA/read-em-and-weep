# Independent review of the line-kernel splitting

The argument in KERNEL-SPLITTING.md is correct relative to PR562 and the pinned full-normalizer representation identities. It is an additional proof, not merely a review of the main first-order calculation.

The representation mismatch is deduced, not guessed: the invariant rank-two tensor identifies the odd part of V with W'; odd parts of Sym^2 A=V tensor U give the irreducible six-dimensional B tensor R; the beta net identifies B with U'. The remaining two-dimensional R must be the other faithful binary representation, with Sym^2 R=U. The central signs on A are + on the three-space and - on the two-space: the reflection has these multiplicities, and perfectness forces determinant A=1, excluding its negative.

Restricting Q(-1) to P(R) gives B O(-1) plus O. The rank-nine hypothesis forces the even block to be an isomorphism and the odd block to be surjective. Its trivial coefficient channel vanishes by the two-versus-six representation mismatch. Both remaining irreducible channels are nonzero by the target rank, so their maps on global sections after twisting are injective with disjoint images. The splitting-type proof then correctly excludes all unbalanced possibilities by the central character and the absence of Hom(U,U' plus J5). Hence the ordinary bundle is O(-1) plus two copies of O(-4). No trivial linearization is claimed for the balanced rank-two summand.

The intrinsic derivative factors through the normal bundle because evaluation has constant rank on the line. Its dual kills the distinguished O(-1) by absence of invariant vectors in B*. Once the independently proved exact rank two in PROOF.md is used, its balanced restriction is a subbundle injection; the degree computation gives quotient O(5), and dualization gives the missing normal line O(-5). All bundle twists and ranks agree with the separate Clebsch-contraction derivation.

This is independent mathematical verification, not formal proof checking. It does not infer smoothness or integrability from the first-order tangent calculation and uses no selected actual source evaluation.
