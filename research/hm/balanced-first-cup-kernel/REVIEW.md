# Independent structural review

Verdict: PASS. The proof resolves the actual first-cup kernel alternative and its ambient first-scaling corollary under the two stated authenticated inputs. No mathematical gap was found in the actual quotient identification, the two nonvanishing universal projections, or the derivative-span exclusion.

## Hash-bound scope

Reviewed files:

- PROOF.md SHA256: 8498a0652b1345c89ebf2643a9d96853e0e2c60760e674425f97c68723aebb41
- verify.py SHA256: 6bcb33df4eb195b0f264b16e5a03502a8895bee61cf26225023db9b08edda9aa
- INPUTS.json SHA256: e4a20a30c870fbcbe905e794a651a4105ba7e511ec4c44d9dda1ebb6e5a39198
- REPRODUCE.md SHA256: 42c27ee8c7d5bf35a414d2ed7197fcd4bde1f7e6245ed6c32543c82d821f2f71

The two source files were read independently. Their copied bytes, SHA256 hashes, and Git blob IDs were recomputed and match the manifest:

- TWO_TYPES: commit 8170fe31a16b2028052973157dc79a06d0d77f64, research/hm/first-cup-kernel-two-types/PROOF.md; 7603 bytes; SHA256 2659282737eac4d62801ec50d484e9768236485271f7afab6ecf8537726e88c8; Git blob 98b447138af8f1c03f809ff695adec459b0de7e5.
- FIRST: commit db51525015bb7c5e825833d550d08dedf6f6ea96, research/hm/order-four-quadratic-load/ODD-FIRST-SCALING-OBSTRUCTION.md; 18007 bytes; SHA256 e7da29f44d2d21eb18765bde1b1d52a0190c192b014fc8a735d8e32318fc04d2; Git blob 93e728fec4065ada638ce4760948952caf125cee.

This verifies byte identity to the supplied manifest, not a new independent remote fetch of the named commits.

## Mathematical checks

1. FIRST supplies the actual Leibniz cup and its quotient, not merely dimensions. The multiplicity-free decomposition A tensor D=A+V+P+D forces im(phi)=P+D to be the actual canonical isotypic subspace. The auxiliary SL2 projections therefore descend to the actual A and V quotient channels up to nonzero identifications.
2. Uniqueness of the G A-channel identifies the actual y with the universal contraction up to a single nonzero scalar. This extends the tensor used in the argument, not the symmetry of the actual geometry.
3. Pure squares span A. Thus all-parameter cup vanishing is equivalent to zero quadratic coefficient tensor, as required to identify H0(K) with ker(nu).
4. The trace-free Jordan anticommutator is nonzero as a universal polynomial and detects H4 injectively; H8 cannot contribute to A tensor A. Any constant D kernel therefore lies inside H8 rather than forming a graph between the two source D constituents.
5. The formal highest-vector contraction gives a nonzero top projection, so uniqueness identifies the H8 map with degree-(2,6) polarization. Its actual V projection vanishes precisely when all its second derivatives lie in the four-dimensional P constituent.
6. The derivative-span lemma is valid over C: a dimension drop for a proper binary-form subspace would force every derivative kernel pure power into that subspace, hence force the entire symmetric power. Iteration gives at least five independent second derivatives for any five-space in Sym8, contradicting containment in P.
7. The imported exhaustive alternatives then give H0(K)=0 and K=T6 O(-1) directsum A O(-2). The aggregate coefficient cokernel is A by the exact character identity.
8. Twisting the actual first-cup sequence by O(1) gives H0(K(1))=T6 and H1(K(1))=0. Its global map multiplies the same quadratic cup coefficients by linear normal forms, hence is precisely FIRST's ambient 30-to-24 first-scaling cup. It is surjective with kernel T6. This is not the two-root projected map and does not improve its already established twelve-dimensional image.

## Reproduction and boundary

Independently executed python verify.py and python -O verify.py; both completed with exit code zero and PASS. The checker uses explicit exceptions rather than assertions, so optimization does not disable its checks. It checks exact abstract characters, universal polynomial nonvanishing and fixed dimension consequences, and immutable source bytes. The general derivative-span lemma and actual-map identifications are textual mathematical arguments, not replaced by the checker.

The only displayed contractions and formal diagonal entries are universal representation identities. Neither the proof nor this review selects actual HM/source coefficients, points, jets, matrices, derivatives, or instance ranks. No external write was performed. The result does not determine secondary boundaries, the opposite-pencil bundle, vertex scalars, later lifting obstructions, global odd sections, or an algebraicity/frontier conclusion.
