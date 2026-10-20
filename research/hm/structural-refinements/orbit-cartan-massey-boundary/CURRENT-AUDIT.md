# Current independent mathematical review

Independent mathematical review, 20 October 2026. This is a check of the written derivation and the stated immediate prerequisites, not a formal verification certificate. Earlier audits are treated as historical evidence, not as a substitute for this review.

Reviewed PROOF.md SHA256: e4458c89169e811aee29f86f6926dd4e763b2fded6f42ffbfa56cbfcee637f82

Reviewed Git blob SHA1: 92c406381b1bc41211562f7eddab8ef7c23a0d93

## Verdict and dependency resolution

PASS for the displayed formal identities and representative reductions, conditional on the explicitly stated ordered cup vanishings, zero indeterminacy, and orbit identification. The family-extension, structural-formality, and rank-two-primitive manuscripts are historical comparisons only. No premise from their unbound full claims is necessary for this proof.

The direct weight-specific source is [WEIGHT-TWO-TRANSFER, sections 2-3](https://github.com/Akilleez-QA/read-em-and-weep/blob/721fdc556714bb40f0a805f01fae51cf6d555fd5/research/hm/cubic-loci/foundation-p04/WEIGHT-TWO-TRANSFER.md). It proves the ordered products U0.U0, U0.U1, U1.U0, U1.U1 vanish and supplies H1(End H(-2))=0 for upper indeterminacy. LOWER-TRANSFER section 3 gives the lower 001 zero-indeterminacy argument. UPPER-TRANSFER is an image/lift excerpt that imports this upper-operation theorem; it must not be mistaken for its independent proof. The invariant-DGA theorem alone is not used as a replacement for these twist-specific facts.

## Premise closure

1. Smooth Atiyah lifts exist from a smooth connection. The standard holomorphic sl5 linearizations of O(k) give a single-symbol twisted derivation. Adjusting the lift by a global scalar zero-order term makes its determinant lift the holomorphic one on O(-1), without changing its induced End operator. This constructs all operators used in sections 1-3; it imports no formality or family-extension conclusion.
2. The graded Jacobi identity for bundle operators gives the stated curvature equation, including a_[X,Y]. PR144 supplies injectivity, indeed the ambient isomorphism, of the orbit Kodaira-Spencer map. No restriction-to-quintic premise is used.
3. For odd trace-free rank-two forms, the trace-free part of xy is (xy+yx)/2. Projective-space scalar H1 and H2 vanish in twists 0,-1,-2. These elementary facts supply the primitive decomposition and scalar homotopies without any additional rank-two-primitive theorem.
4. Fixed-coordinate pullback obeys T_g(fu)=g*(f)T_g(u), proving the semilinearity caution directly. No triviality or structural-formality theorem is assumed.

## Sign and coefficient checks

- The first identity produces m(a,b,c)+m(b,a,c)+m(b,c,a)=0 after the closed primitive-error terms are killed by the ordered cups. Outer reversal turns this into the established cyclic relation, not an additional equation.
- In the two-direction antisymmetrization, the two first-derivative-of-b terms cancel at cochain level. The remainder is d[R_XY,b] and agrees with the commutator defect itself. Dropping a_[X,Y] would be invalid.
- The symmetric trace-free primitive is (L_Xa_Y+L_Ya_X)/4. A one-sided primitive differs by a closed cochain, not by zero. Graded trace makes t_XY alternating, while scalar H1 vanishing makes changes exact without making t_XY itself zero.
- In (8), a_X t_Yu=-t_Yu a_X. Alternating gives precisely (9); symmetrizing gives (10). The scalar t_XY term cancels only in the symmetric expression, while the q_XY term cancels only in the alternating expression.
- For (11), dL_Xq_bc=B(L_Xb,c)+B(b,L_Xc)+2B(a_X,q_bc). Subtracting half this differential leaves exactly -(1/2)B(b,L_Xc)-t_bc a_X+t_ab c. Thus this total expression is closed and represents the canonical singleton operation in either allowed weight pattern. It removes freely chosen End-valued pair primitives but not the covariant derivative or scalar terms.
- The Green prescription gives dt_pq=tr(pq)/2 by Hodge decomposition and H2(O(k))=0. It is a smooth homotopy, not an effective algebraic primitive or a value calculation.

No individual displayed summand is assigned a canonical class. No extra vanishing, actual component value, fixed-fiber PGL action, or exclusion of all possible orbit methods follows. Later component nonvanishing results are compatible with this bounded statement.
