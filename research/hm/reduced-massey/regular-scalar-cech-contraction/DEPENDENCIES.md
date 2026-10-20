# Mathematical dependencies

The Laurent contraction and its regular correction formulas need no bundle-specific input. Only the Massey comparison uses the following conditional inputs.

- [weight-two-massey](https://github.com/Akilleez-QA/read-em-and-weep/blob/721fdc556714bb40f0a805f01fae51cf6d555fd5/research/hm/cubic-loci/foundation-p04/WEIGHT-TWO-TRANSFER.md), commit `721fdc556714bb40f0a805f01fae51cf6d555fd5`, `research/hm/cubic-loci/foundation-p04/WEIGHT-TWO-TRANSFER.md`. Direct source for all ordered U0/U1 cup vanishings, upper 011 zero indeterminacy, and H1(End H(-2))=0; §§2–3 SHA-256 `7c2d6c63d4580a30452f98d52f57ca05afd9cceffaad1104434d9fa362fb91bb`.
- [lower-weight-image-symmetry](https://github.com/Akilleez-QA/read-em-and-weep/blob/292d59b1e28c33968537a5f13700e7c45dc9214f/research/hm/cubic-loci/foundation-p05b/LOWER-TRANSFER.md), commit `292d59b1e28c33968537a5f13700e7c45dc9214f`, `research/hm/cubic-loci/foundation-p05b/LOWER-TRANSFER.md`. Lower ordered cups, zero indeterminacy and symmetry SHA-256 `897e3ebeeacca60280c19aa6caf57631a9b6c48ae6610fcc195fbba5cbfb6976`.
- [canonical-massey-detector](https://github.com/Akilleez-QA/read-em-and-weep/blob/721fdc556714bb40f0a805f01fae51cf6d555fd5/research/hm/cubic-loci/foundation-p04/CANONICAL-MASSEY.md), commit `721fdc556714bb40f0a805f01fae51cf6d555fd5`, `research/hm/cubic-loci/foundation-p04/CANONICAL-MASSEY.md`. Canonical singleton Massey convention and cyclic identity; weight-specific assumptions retained separately SHA-256 `1887d2fa2bb470e887cd12eb34343d1bff3c4602ddf7c9adaaf6cd6ce6055415`.
- [orbit-cartan-smooth-reduction](https://github.com/Akilleez-QA/read-em-and-weep/blob/ff24ff1120ce9f1bb2dc25f692dda1dd43e1d473/research/hm/structural-refinements/orbit-cartan-massey-boundary/PROOF.md), commit `ff24ff1120ce9f1bb2dc25f692dda1dd43e1d473`, `research/hm/structural-refinements/orbit-cartan-massey-boundary/PROOF.md`. §6 smooth reduced representative only; its regular algebraic analogue is proved independently in the TW slice. Full first- and two-direction exclusions are not strengthened. SHA-256 `e4458c89169e811aee29f86f6926dd4e763b2fded6f42ffbfa56cbfcee637f82`.

## Reduced-form chain

- The smooth orbit-Cartan formula is identified through the exact public orbit-Cartan pin above. It is comparison context, not a constructive algebraic inverse.

## Hypothesis boundary

Use the full twist-graded endomorphism algebra. Pair-product exactness and zero indeterminacy are separate hypotheses; neither follows from scalar H² vanishing. The ordered 001 lower and 011 upper operations use the explicit twist-specific theorems above. A trace-free bundle model requires rank two and det(H)≅O(−1). The comparison preserves Massey sets; it is not a multiplicative inverse to analytification.
