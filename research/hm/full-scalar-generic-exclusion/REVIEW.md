# Independent mathematical review

Status: PASS, conditional only on the explicitly pinned mathematical dependencies.

Reviewed artifact: PROOF.md
SHA-256: 9ee3e9524af55ac2dc0153f5fea2051ac7417f31303254efee2afe77da4c8a24

The reviewer independently fetched and read PR696 at 958244d6d9d3b326f66c073a9d669717c953ec32, PR747 at 0a0ee30a5142477e54245b7c6f22d561abb4f5f1, PR713 at 5b3943980ecaef78ee7f56fbc015d40955fb24f0, and PR760 at d798dceb77b94b5dbb9457fb303984e595ce1874, then read this entire artifact.

## Checks

1. PR696 supplies the actual intrinsic polynomial family, not merely a possible equivariant representation space. Its bidegree (3,1), target T, and irreducible negative representation A are used correctly.
2. The transported-source equality rho4(g a0,h)=g rho4(a0,g^-1 h) is valid for every h. Thus a universal full-scalar zero produces a full orbit of zeros at the same fixed h. Passing afterward to the fixed-chart necessary modular gate requires no Gamma action on that quotient.
3. Every nonzero global quadratic is nonzero as a rational section, so cancellation of its square over k is valid. Only Phi_h, not rho4, is required to be linear in a. Orbit span is all of irreducible A, contradicting the nonzero Phi_h theorem for every nonzero h.
4. The one-way modular implication is preserved. PR713 identifies the scalar's leading square-ideal class; its degree-eight relation space maps to the modulo-f3 quotient used in PR747. The proof never treats the weaker modular zero as sufficient for full-scalar vanishing.
5. Both exhaustive PR760 alternatives are handled. In the common-direction case, outside the conic E_h is precisely C a0. The nonzero linear source map has proper kernel, and the union of that projective kernel with a conic cannot cover irreducible P4. Cubic homogeneity handles every scalar multiple of a0.
6. The full zero incidence is closed because the equations are bihomogeneous. Projectivity of P(A) makes its image closed. Existence from the preceding argument makes this image proper. Full equivariance gives invariance of the incidence and image.
7. The quantifier strengthening is justified rather than inferred by interchanging quantifiers. Nonzero global section is explicitly distinguished from a nowhere-vanishing physical section. The separate beta4 boundary and algebraicity are not inferred.

8. The added conditional dimension bound is valid. Each translate of an irreducible component of dimension at least two must lie in the proper linear kernel because it cannot lie in the conic. The common intersection of all translated kernels is an invariant proper subspace of irreducible H=D5 and therefore zero. This contradicts a nonempty projective component. No assumption that the modular quotient itself is equivariant enters this argument.

No mathematical correction is required. This is an independent written deductive review, not formal proof-assistant checking. No selected actual HM coefficients, source instances, points, ranks, or scans were evaluated.
