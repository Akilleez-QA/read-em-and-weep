# Independent review: complementary secondary branch

## Verdict and exact scope

APPROVED for the conditional claims stated in PROOF.md. This is an independent mathematical review of the entire proof, its three immutable immediate inputs, and the bounded character checker. No unresolved mathematical gap was found. Approval does not select the actual branch `a_D=0`, `a_V a_P != 0`, or any residual coefficient value; it does not establish the global open goal.

This review is bound to the following exact SHA256 hashes:

- PROOF.md: `ef31ed280432e7cbb8a73911c30df94d323b10040fd8782cd81fb4ce3151020e`
- INPUTS.json: `7285d936e943c62f388d2f7cac125119961e5fb0e8b84dfab85f9c749dd42cde`
- verify.py: `b0297eb3186958557d756a34303c5af6b33ba92c2f004ca0e3444e88c36f2b88`
- REPRODUCE.md: `c290ad21cd194a3c6f2c031221c0a95f01a4cfb81ee1e0cb6fedac04522ca5df`

No selected actual HM/source coefficient, point, parameter, derivative, jet, matrix, rank, or large computation was used in the review.

## 1. Exact-input audit

All three immediate originals were independently fetched through the GitHub connector at their exact immutable commit and path, requesting base64 rather than reconstructed line text. Decoded remote bytes matched the local audit-inputs files exactly. Their metadata blob identities, recomputed Git blob hashes, byte counts, and SHA256 hashes matched INPUTS.json:

- FIBER, commit `0b9a8505e71951cf54950f54458c96cae0520146`, 11620 bytes; SHA256 `2ec9f71862bad628ee1663fa91c6bb511db9232355143a3a51e067362ebca575`; Git blob `e30df9cc67b9c2a13b8b55e9d23b9523db713e3f`.
- DROW, commit `1ac03caea0564db40acabf8d8d5a0a39984216a2`, 11118 bytes; SHA256 `59756d7dac77cfe0f91c323e9d9bf88ef1b4947923beac0f5af5c50ed360099b`; Git blob `7aad606b3d435208ed8590ea3764090730c115ab`.
- FORCEDW, commit `f96962f2219e096821c3dec50712cc0108abea8f`, 9376 bytes; SHA256 `ca7b2dade4fca80b5e6fc729f4a95ee56a828558fc4e28b3f08f607b1a524b00`; Git blob `c4a42690aa45b980f098120ff623d682d97822ea`.

The full immediate proofs were read. The new proof correctly separates the unconditional channel constructions in FIBER and DROW from their separate two-D-channel hypothesis. FORCEDW identifies the actual canonical W-preimage, rather than an arbitrary bundle of the same rank and degree. Earlier recursively cited inputs remain established dependencies; this review does not claim a fresh recursive audit of all of them.

## 2. Joint P-source block and its actual quotient

The P-to-V channel is onto with kernel O(-4). The P-to-P channel has kernel W' O(1). If its restriction to O(-4) vanished, the inclusion O(-4) into P O(2) would factor through W' O(1), contradicting

    Hom_G(O(-4), W' O(1)) = Hom_G(W', Sym^5 W) = 0.

The nonzero restriction has no common-zero divisor because its forms have degree8 and every orbit has at least12 points. Hence the joint actual P-source map is an everywhere-injective subbundle map, not merely a sheaf injection.

The quotient by that joint block is correctly identified through the surjective V projection, without pretending that the P-to-V exact sequence globally splits. Its remaining injection O(-4) into P O(4) is the unique P8-dual evaluation channel.

For the P8 evaluation kernel M, the Euler subbundle W' O(-1) lies in M because its composite to O(8) belongs to Hom_G(W',Sym^9 W)=0. This explicitly proves the forced degree-one syzygies form a fiberwise-injective subbundle. The descended W' O(1) -> O(8) is onto and has kernel O(-6). The extension splits because H^1(W' O(5))=0, and the equivariant splitting is unique because W' is absent from Sym^5 W. Thus the quotient is O(10) plus W' O(5). Both off-diagonal equivariant Hom spaces vanish, so its summands are intrinsic up to their scalar identifications.

## 3. Residual coefficient correspondence and graph lifts

Applying equivariant Hom from W O(-1) to the actual joint-block sequence gives an isomorphism on W-channel spaces: the preceding Hom into P O(2) vanishes by P tensor W=W'+T6 and Sym^3 W=S, while the following Ext vanishes already non-equivariantly as H^1(P tensor W O(3))=0.

Consequently the new x,y coefficients are an invertible linear recombination of b_V,b_P for the retained nonzero a_V,a_P. The proof does not improperly assert that this change of coordinates is independent of a_V,a_P over the entire parameter family. Since a_D=0, the D target is untouched and z=b_D after normalization.

The kernel identification is through the unique P-component graph lift associated to the quotient diagram. The proof correctly retains that distinction rather than assigning a zero P-component to every residual kernel. Cokernels are genuinely identified as sheaves.

## 4. Universal channels and every fiber case

The O(10) channel is the unique Hamiltonian-gradient channel of f12. Its two first partials cannot have a common projective zero, since Euler's identity would force a multiple zero of the reduced binary form. Hence it is onto with kernel O(-12).

The W' O(5) channel cannot have generic rank1. Saturating its hypothetical image gives an equivariant O(d), with d=0,2,4; the source factor permits only d=0, while the target factor at d=0 is excluded by W' not occurring in Sym^5 W. Its determinant is therefore a nonzero invariant section of O(12), hence a nonzero multiple of f12. Reducedness forces rank exactly1, not0, at each orbit point.

At the C10 stabilizer the source characters are0,4 and W' O(5) target characters1,4. Its kernel on the orbit is thus character0. Both the onto gradient and Euler maps have character0 target, so each is nonzero on that kernel. This supplies actual nonvanishing, rather than only permission by characters, and proves the constant-rank case when y and either x or z are nonzero.

When y=0 and xz is nonzero, the determinant of gradient plus Euler is, up to row-order sign, 12 f12. The earlier harmless sign ambiguity was corrected in the hash-bound proof. The quartic Veronese target line is a subbundle, so it does not alter the rank or determinantal ideal. The single-channel and zero cases are constant rank. The table exhausts all coefficient patterns without selecting one.

## 5. Scheme structure and original kernel sheaves

In each jumping case, the residual generic-rank minor ideal is exactly (f12). Locally splitting off the P-source identity block preserves that ideal in the full reduced map. Passing from Q to the original K adds locally zero columns; the zero A target adds zero rows. Thus the generic-rank minor ideal, fiber-rank increment of four, and torsion identification remain valid for the original map. Local Smith normal form gives exactly one length at each of the twelve reduced points.

The original kernel conclusions are sound:

- Generic residual rank2 gives A O(-6), including the two cases with exceptional fiber kernels.
- The gradient-only case gives A O(-6) plus O(-12), using ordinary Ext vanishing and the equivariant Hom vanishing that makes its splitting unique.
- The Euler-only case is the nonzero one-dimensional equivariant extension with middle bundle S O(-5); a split would contradict Hom_G(O(-2),K)=0 for the actual balanced K.
- For zero residual, invertibility of the coefficient recombination forces all three original W-channel coefficients to vanish. Only in this case is the reduced kernel literally the canonical W summand before elimination. FORCEDW then identifies its actual preimage as D O(-4).

The final warning correctly distinguishes kernel sheaves from larger exceptional fiber kernels.

## 6. Checker and reproduction audit

Both `python verify.py` and `python -O verify.py` were independently run on the final files and passed. The script uses explicit exceptions rather than Python assertions, so optimization does not remove its tests. It uses only nine-class character arithmetic over Q(sqrt(5)), bounded symmetric-power recurrences, abstract stabilizer weights, bundle-degree arithmetic, and exact input hashing. No source-instance construction or evaluation is hidden in the checker.

The checker supports the stated fixed character facts and arithmetic. It does not purport to prove the quotient diagram, structural nonvanishing, reduced local ideals, or graph-lift assertions; those are supplied by the proof and independently checked above. REPRODUCE.md accurately describes this division of responsibilities and reconstructs the exact omitted immediate input bytes from immutable raw locations.
