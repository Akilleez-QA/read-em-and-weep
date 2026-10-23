# Independent whole-proof review

Verdict: PASS for the exact author files identified below. This review checked the full mathematical argument and its immutable interfaces, not only the verifier output. It is not proof-assistant certification or an evaluation of selected HM data.

## Reviewed author bytes

SHA-256:

- PROOF.md: `9dbd2156b77263b364c522cea632c21a7867a17abce2104fa89c92281af2bea4`
- verify.py: `fb967429933e10c5a7841969d5ede74d0f36160c22961dfb4adc75f8498f4f33`
- INPUTS.json: `8470d6df4241065c0733a45710b9b19b6c33b0abb5a50ea2a98824ee019124e6`
- REPRODUCE.md: `624f27439216dcdd8cb19e855d138ca9f4b88d7161708263825c792a1d8cb6a6`

The reviewer independently retrieved both original PROOF.md files through GitHub at the exact commits in INPUTS.json, read them, and checked their returned Git blob identities against the manifest and local audit copies:

- NINE: commit `ad34e86521236df3617c5e6c26976266bf4d9b61`, blob `cac9d9c48caf3c52aa1a5449bf9a2a7d776f84b8`.
- SIXTEEN: commit `8d17ad2bae45df6078dbb50ff963228c6105c815`, blob `5c2d6599bdb1e5b5e7227cc2e3b6b4990bf6989d`.

The initial draft incorrectly located SIXTEEN's saturated-image filtration in Section5. This was corrected to Section6 before the reviewed proof hash above was frozen. There is no outstanding mathematical correction.

## Whole-proof checks

1. The scalar target is reached through its intrinsic constant quotient, without a target splitting. Positivity excludes a constant quotient of C; the fixed equivariant channels exclude O(-8) and S O(-1). The remaining nonzero multiplicity functional gives an everywhere-surjective Euler channel and the canonical line M0.
2. The actual kernel diagram gives source O(-8)+S O(-1)+L3 and target Y13, with unchanged actual map F to C. The sequence defining L3 is intrinsic. Its Ext1 vanishes, while its equivariant splitting torsor has dimension one. No complement or canonical splitting is substituted.
3. The degree-eight D subsystem is basepoint-free by the projective orbit bound. Its kernel has rank four and degree minus eight. The bound on H0(K4(1)), together with D tensor W=S+T6, excludes every degree minus-one summand. Balanced degree minus-two splitting follows, and only then is H1 vanishing used to identify its equivariant multiplicity as P. Duality yields the saturated universal O(-8) inclusion with quotient P O(2).
4. Every atom in all seven authenticated saturated-image alternatives was checked. Negative degree excludes the high atoms; the only remaining equivariant tests are against O(2), A O(2), and W O(1), and all vanish. Thus Hom_G(C,P O(2))=0 follows from the actual filtration, not a chosen splitting or a selected row. This vanishing is correctly distinguished from the nonequivariant absence of maps to constant bundles.
5. Applying Hom to the intrinsic L3 extension proves that its entire D projection is zero. If the inherited S projection also vanished, the remaining nonzero O(-8) component would force an actual surjection from C onto P O(2), contradicting the preceding filtration argument. Uniqueness of the S-to-D channel then identifies its nonzero map with universal multiplication, with saturated quotient O(4).
6. All kernel constructions retain the actual inherited maps. The endpoint is rank eight to rank thirteen, with source degree minus sixteen, target degree ten, and unchanged rank-five degree-twenty-six C. The proof does not perform another cancellation, select an actual C type, resolve the marked-line position, or import the separate conditional mixed-Q lane.

## Independent replay and scope

Both `python3 verify.py` and `python3 -O verify.py` were independently replayed successfully against the authenticated local audit copies. The verifier uses only Python's standard library and bounded fixed character arithmetic. The reproduction commands correctly reconstruct the exact immediate originals with git show before rerunning the checks.

No actual HM/source coefficient, point, parameter, matrix, derivative, instance rank, or scan was evaluated. The universal geometry and actual-map reasoning were reviewed mathematically; the small verifier is supporting evidence, not a replacement for those arguments.
