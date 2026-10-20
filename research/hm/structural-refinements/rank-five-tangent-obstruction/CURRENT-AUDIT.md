# Current independent mathematical review

Independent mathematical review, 20 October 2026. This is a check of the written derivation and the stated immediate prerequisites, not a formal verification certificate. Earlier audits are treated as historical evidence, not as a substitute for this review.

Reviewed PROOF.md SHA256: 9338b901fa4dfb5e71a80dbe938e2b283d3639d7eca9ecf28b6fec5aaf3a53c1

Reviewed Git blob SHA1: 5a800b97a04cf6c4bf43dd55463bd79103dab695

## Verdict and scope

PASS as a fixed-global-quotient countermodel to a universal one-dimensional bound for the determinantal first-variation kernel. This is not an integrated surface construction, a tangent-space claim for reduced support, or an equivariant example for the actual operation.

## Checks

- The universal tensor space has dimension 40, middle image F_u dimension 14, and closed repeated-input tensor variety X dimension seven. The imported square-avoiding correction and two-dimensional compatible rank-two locus follow from intersecting two nonempty opens; the second uses an actual differential dominance witness, not dimension counting alone.
- For D=span(e,z), projection to the no-u tensor summand separates B_e(K) from B_z(K). B_z is injective on Sym2(E0), and ker(B_e)=Ce^2 misses K because e is nonisotropic. Hence the ten variations are independent modulo F_u.
- Splittings over their ten-dimensional image form an affine space of dimension 90 with residual fiber F_u/L of dimension nine. A fixed repeated-input point with nonzero eligible projection imposes nine independent affine equations; its projective scaling contributes no free parameter because its projected representative fixes the same scaling. The bad incidence has dimension at most 7+81=88. Points with zero projection are already excluded by N intersect F_u=L.
- In Gr(5,25), avoiding the nine-dimensional middle image is nonempty open. Avoiding the projected repeated-input variety is also nonempty open, since the bad incidence has dimension at most 7+dim Gr(4,24)=87<100. Their intersection gives one fixed quotient of dimension 20 preserving every repeated-input injection and M intersect F_u=L exactly.
- Therefore the residual rank at u is five, its kernel is the specified trace-free ternary hyperplane, and the independent-zero fiber remains the finite double cover of the compatible rank-two locus, of dimension two.
- The derivative on u^2 is -2A_u(xi), already in the middle image; the derivative on q-u v(q) is the specified variation. For xi in D it lies in N+F_u and hence maps into that image. Locally splitting the repeated-input block identifies the full rank-at-most-nine and residual rank-at-most-five determinantal ideals, not merely their supports. The tangent conclusion is therefore scheme-theoretically valid.

No argument shows that the two-plane integrates, remains on the ternary-support/metric stratum, or is tangent to reduced support. No generic residual rank, global support-dimension bound, or normalizer equivariance is inherited from the earlier quotient construction.
