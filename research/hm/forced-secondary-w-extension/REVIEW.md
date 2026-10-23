# Independent mathematical review

Verdict: PASS, conditional on the imported actual-map and exact-sequence theorems recorded in INPUTS.json.

Reviewed PROOF.md SHA256:

    ca7b2dade4fca80b5e6fc729f4a95ee56a828558fc4e28b3f08f607b1a524b00

Reviewed verify.py SHA256:

    61a416175e523c770516c8bfc2070ac5a990ccf85134fcc8efab2a9d36e9f6c2

## Mathematical checks

1. The invariant inverse form contracts the actual symmetric Leibniz formula to a nonzero scalar multiple of the actual coefficient tensor. The invariant self-duality of D identifies Hom(D,A) with A tensor D equivariantly. The coefficient A therefore survives the actual quotient by im(phi)=P+D. This proves nonzero cup on the trivial constituent without evaluating a selected coefficient or substituting a dimension-matched map.
2. The only equivariant homomorphisms W O(-1) to H O are invariant-line inclusion after Euler evaluation. Evaluation is surjective, so none of the nonzero homomorphisms can land in K. Exactness then makes the boundary of the canonical W-complement inclusion nonzero in the one-dimensional equivariant Ext group. The argument uses the actual inclusion K into H O.
3. Dualizing the established y sequence and twisting by O(-4) gives the correct equivariant extension with middle bundle D O(-4). Its nonsplitting follows from H0(O(-3))=0. The one-dimensional Ext group identifies the actual pulled-back middle bundle up to endpoint scalars, not a canonical named isomorphism or a constant coefficient embedding.
4. The residual sequence has rank nine and degree -12. Its class cannot split even nonequivariantly, because a positive O(2) summand cannot inject into H O. The two vanishing cross terms give the claimed isomorphism on equivariant Ext groups. The addition map from K_P plus K_W has the anti-diagonal common A O(-6) as its kernel, so the pushout identifies the actual residual class, not merely its ambient parameter space.
5. The cohomological source and target in Section 6 have the stated characters. H0(K) injects into H, which has no V constituent. Thus the unique source V maps injectively, and hence isomorphically, to the unique target V. Linearity of the connecting homomorphism in an extension class supplies the stated nonzero V-channel functional and excludes its kernel for the actual class. This does not select the P or D channels or a projective residual direction.
6. The scope statements correctly retain the unknown secondary boundary and residual class. The proof makes no claim to split the full K, evaluate an actual secondary rank, or settle the global odd-section problem.

## Reproduction and source checks

Both `python verify.py` and `python -O verify.py` passed independently. The verifier uses explicit exceptions, checks abstract character orthogonality and completeness, checks the required character identities and Hom/Ext dimensions, and validates byte counts, SHA256 and Git blob hashes of both input files. The two checked input copies also matched byte-for-byte the previously supplied local QUOTIENT and FIRST source files. Their full text was read for the actual-map premises. No new remote retrieval or independent reconstruction of the prior theorems is claimed.

The checker is arithmetic and source-integrity verification, not a proof assistant and not an actual tensor or extension evaluation. The inverse-form argument, nonsplitting, actual pushout and V-channel exclusion were checked mathematically against the displayed exact sequences. No selected actual coefficients, points, jets, matrices, derivatives or instance ranks were used.
