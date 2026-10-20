> Historical mathematical review of the source manuscript. This is not a new independent review or a formal verification certificate. Original source-byte hashes refer to the archived manuscript; public-byte hashes are in SOURCE-BINDINGS.json.

# Independent audit of the scalar-retaining lower expression

A separate proof auditor checked Section 5 of PROOF.md against the canonical lower operation and confirmed all signs and coefficients, without any actual HM evaluation.

1. d q_XY=(a_Xa_Y+a_Ya_X)/2=B(a_X,a_Y). Both one-sided derivatives have the same differential, so their average is a symmetric valid trace-free primitive.
2. Graded trace gives tr(a_Ya_X)=-tr(a_Xa_Y). Scalar H2 vanishing allows a bilinear alternating t_XY, including t_XX=0. Scalar H1 vanishing makes changes exact but does not make the primitive zero.
3. The trace-free defining cocycle is B(a_X,q_Yu)+B(q_XY,u)-t_Yu a_X+t_XY u. The sign of the third term is forced by moving two odd factors. This yields equation (8) exactly.
4. Alternating (8) gives (9); symmetrizing gives (10). The q_XY contribution cancels only in the alternating expression; t_XY cancels only in the symmetric expression.
5. Closedness follows from d(a_X h_Yu+h_XY u)=-a_X(a_Yu)+(a_Xa_Y)u=0 and commutation of trace-free projection with d. Scalar H2(O(-1))=0 identifies the trace-free cocycle with the full Massey class.
6. Independence of connection and representatives is independence of the total cohomology class for fixed inputs kappa(X), kappa(Y), [u]. The lower-weight proof Section 3 establishes zero indeterminacy: all closed primitive changes contribute ordered U0·U1 products, which vanish. Pairwise exactness of selected representatives by itself would not suffice.

Important limitation: individual derivative and scalar summands need not be closed and do not have separate canonical cohomology classes. Only their displayed sum is the canonical class. The formulas prove neither symmetric nor alternating vanishing and do not eliminate any of the eight eligible lower components.

The first Cartan identity and antisymmetric commutator calculation were also checked directly in the parent proof: [a,h]=ah+ha for odd a,h; the two derivative-of-b terms in equation (5) cancel on antisymmetrizing; the remaining term is d[R_XY,b] because R_XY has degree zero. This is a bounded exclusion of that displayed manipulation, not of all Atiyah/orbit methods.

  

## Additional independent audit: global twists and unified elimination

The same separate auditor explicitly checked the stronger Section 6 reduction and the global twisted operator construction. It confirmed

    T-(1/2)dL_Xq_bc=-(1/2)B(b,L_Xc)-t_bc a_X+t_Xb c,

with all signs correct. Hence the right side is closed and represents the singleton Massey class. All freely chosen trace-free pair primitives disappear, while the End-valued derivative L_Xc remains.

The auditor confirmed that O(k) carries compatible holomorphic SL5 linearizations for all integer k. Coupling this infinitesimal line action with the smooth lift on H gives the claimed global twisted derivation and no additional scalar twist term. The local single-symbol formula in Section 1 makes the balanced tensor construction explicit. Replacing the holomorphic line action by a Chern horizontal lift would invalidate that assertion.

For 011 the scalar primitive t_bc and discarded scalar target have twist -2. The necessary H2(O(-2)) and H1(O(-2)) vanishings are now explicit alongside twists 0 and -1. Class independence still requires the full ordered cup vanishings, and individual terms of the reduced representative need not be closed.

The optional Green-operator prescription was checked directly: for a closed scalar two-form rho with no harmonic component, d d*G rho=rho, since dG rho=Gd rho=0. It is a smooth choice of scalar homotopy, not an algebraic primitive construction or a value evaluation.

## Final-byte independent audit

Verdict: PASS for the reviewed formal identities and constructions, conditional on the imported ordered cup vanishings and orbit facts.

Audited PROOF.md SHA256:
8e7c7db1bd13a1d4b2ae2350b5e5efa068220b2a52d975a1c5e4b9e8853c599a

The independent auditor checked this hash before and after its final read; it was unchanged. The normalized determinant is correctly O(-1). Its holomorphic SL5 lift exists. Adjusting a smooth lift on H to the prescribed determinant lift is a global scalar zero-order correction, preserving the induced End(H) operator while making a_X and the commutator defect trace-free. Thus the determinant normalization changes none of the proved identities.

The final-byte audit confirmed the single-symbol twist construction, absence of an extra twist scalar term, all coefficients and signs in equations (8)–(13), and the smooth scalar Green homotopy. No further edits to PROOF.md were made after this binding.
