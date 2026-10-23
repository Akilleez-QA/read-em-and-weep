# Independent mathematical and verifier review

Disposition: approved. No mathematical blocker remains.

This review binds exactly to:

- PROOF.md SHA256 fef4d2a93596a51c83594c9073313e8549dcd13e336f0327ad19ef490d8bc96f
- INPUTS.json SHA256 fec20e5bf0158fbcbca16ab6a3e8283dd37ec6885092a7697b2b7b07557264e8
- verify.py SHA256 c1b1916b06a84c68cff9f0048a564a65ef972d904923717a75587a22f9add3d0

## Mathematical checks

1. The statement concerns ordinary ambient codimension-two ideal powers I_R^m in P4. It does not identify these with the ordinary neighborhoods inside individual hyperplanes. Finite normal projection computes actual sheaf cohomology, and does not split the bundle or replace it by its associated graded.
2. Central-inversion eigensheaves are exact in characteristic zero. The displayed positive and negative parts are full eigensheaves, not G-invariants. At 3R the even boundary is the complete actual quadratic coefficient map from BALANCED. Its injectivity kills every even section. The odd part is canonically W tensor B_R(2), giving all six sections W tensor A.
3. The fourth-neighborhood odd boundary has been authenticated by a morphism of actual extensions: multiplication by normal linear forms maps W tensor E_3(2)^+ to E_4(3)^-. Its quotient map is the identity and its kernel-layer map is symmetric multiplication W tensor Sym2 W to Sym3 W. Naturality therefore identifies the complete mixed-normal boundary with H0(c(1)). This is stronger than a directionwise check and needs no formal pullback assumption or selected transition coefficient. Left exactness of H0 applied to the actual bundle injection c(1) proves injectivity.
4. The new layers have no sections because H0(B_R(t))=0 for t<=1. Thus restriction on H0 remains injective at every subsequent ambient order, proving vanishing for all m>=4. Nonzero H0 on 3R proves sharpness.
5. The draft originally attributed H1(B_R(3))=0 directly to an input that explicitly supplied only H1(B_R(2))=0. The final proof repairs this provenance gap: self-duality gives H2(B_R(1))=H0(B_R(-4))*=0, so B_R is 3-regular on P2 and regularity propagation gives H1(B_R(3))=0. The listed H2 vanishings also follow directly by self-duality. This closes the only issue identified during review.
6. Exact cohomology yields H1(3R)^+=A, H1(3R)^-=0 and H2(3R)=0. At 4R the positive H1 remains A; the negative H1 is H0(coker(c)(1))=(V+P) tensor Sym3 W + W tensor Sym6 W. Its decomposition 2W'+2S+5T6 has dimension 42, hence total H1 dimension 45, while H2 remains zero. These are consequences of actual exact sequences, not Euler-characteristic substitutions.

## Replays and source identities

Independently ran both `python verify.py` and `python -O verify.py` against the final files. Both passed. The checker uses explicit runtime conditions, exact abstract character arithmetic, source byte counts, SHA256 digests, and Git-blob digests; its mathematical checks remain active with optimization enabled. It does not evaluate actual HM/source coefficients, points, jets, matrices, or instance ranks.

The local audited BALANCED proof has SHA256 8498a0652b1345c89ebf2643a9d96853e0e2c60760e674425f97c68723aebb41, and UNIFORM has SHA256 351d8906b3401365d61731c8db439488abc05e5871d8111c120289822aa961e7. The final manifest records immutable public commits f23f8b9972d459c7c3ab532937964ef7f543b157 and 5ce277d0476224f9f3fdbc79d1750210a2169708, respectively, with no pending publication flag. Public raw-fetch equality was reported by the author; this review independently checks the corresponding local exact bytes and final manifest, not network availability.

The verifier certifies fixed representation arithmetic and recorded local source identities. The actual-map and geometric identifications were reviewed mathematically above. No later secondary boundary, source/frontier cut, global odd-quadric survival, or algebraicity conclusion is inferred.
