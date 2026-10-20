# Independent mathematical review

Reviewed text: `PROOF.md`, SHA256 `39a0a29afeafe12d767e40649e19bb660d99a63a597e086dd8551a6d339a370f`.

## Verdict

The arguments are sound, conditional on the explicitly pinned structural inputs from PR471 and PR472. No correction to this version is required. This is mathematical review, not proof-assistant verification or an independent recomputation of those prior inputs.

## Checks

1. The proper hyperplane restriction sequence identifies the degree-five Rao cokernel with the section deficiency: the required next group is H^2(I_C(4))=0. Consequently h_D(5)=r-5, with r the preceding multiplication rank. The fifth Macaulay expansion of 19 has successor 23, while that of 20 has successor 25. Monotonicity and h_D(6)=25 therefore give r>=25, not r=25 or surjectivity.

2. Projection of rank-one matrices modulo scalar identity matrices is defined and injective in dimension five. Equality of two projected points would make a nonzero scalar identity a difference of two rank-one matrices. The line argument is likewise valid: a nonzero identity term in T=alpha A+beta B+gamma Id would express a rank-five matrix as a sum of three matrices of rank at most one. Hence every lifted projective line is a rank-one ruling. The pairwise common-factor argument gives the claimed global common factor. The proof uses only projectivity, closed images and zero-dimensional fibers; it does not require an unproved scheme-theoretic embedding assertion.

3. The trace-dual functional attached to y and ell is correctly represented by y tensor ell modulo scalar identities, and has zero R_6* component. Codimension U<=5 bounds the projective annihilator W by four. If every second factor were bad, the projective incidence would have dimension at least four; its injective image would force W to be a four-space contained in the projected Segre. The fixed-second-factor ruling cannot dominate P(V*), whereas the fixed-first-factor ruling contradicts S_1 U=M_6. This proves a proper closed bad set, including possible special bad factors, rather than uniform surjectivity for every pair.

4. Commutativity and degree-zero generation justify S_1 U=ell_1 M_5=M_6. They concern the actual module multiplication throughout. A good factored quadric supplies a point of the rank-five open in the vector space of all quadrics. Irreducibility permits intersection with the nonempty smooth-and-transverse open, without claiming that the factored quadric itself is smooth.

5. For such a transverse quadric, multiplication by q gives the displayed ideal restriction sequence, and the vanishing of H^2(I_C(4)) completes the Rao-cokernel argument. Fifty reduced intersection points impose fifty independent conditions in degree six on Q. The ambient dimension is 210-70=140, so the stated ideal-section dimension 90 follows.

## Scope limitations

The result establishes a uniform lower linear rank bound and nonempty quadratic surjectivity open. It does not locate the original fixed quadratic invariant in that open, calculate a selected multiplication matrix, identify the exact bad locus or exact lower linear ranks, or settle the original fixed-pair, higher-order or algebraicity questions. No selected source-instance evaluation, numerical rank computation or coefficient search was used in this review.
