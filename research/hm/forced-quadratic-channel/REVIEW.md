# Independent final-byte whole-proof review

Result: PASS. No mathematical correction is required for the frozen author files identified below. This review covers the entire proof and its immediate-input interfaces, not only the numerical endpoint or the last modified section.

## Reviewed author bytes

SHA-256:

- PROOF.md: `8fa941de1132f4e05621493620f47688bf8350c135578c2136988336de24f245`
- verify.py: `cd91673832b69aba27bad7fd8f249c56cf094a3d21a10928f9281487fba2236a`
- INPUTS.json: `bb378c175388b0a5129ff23a10431bbbfd128c90f6f8af64483feef0f40fdfb1`
- REPRODUCE.md: `8dd9f93225a6d0bc0adef31fa552eb6689bda1326fa77055ad0299eb2e51ff3d`

These four hashes were recomputed independently after the files were frozen. Any change to these author bytes requires renewed review.

## Immutable originals

Both originals were independently fetched through the GitHub connector at the exact commits recorded in INPUTS.json. Their returned Git blob IDs agree with the reconstructed local copies:

- TWELVE, commit `b99fc50247fe8f992420d452ef359827011631aa`, blob `3cbc82ff9d3c89e2f7635bcdd721e1e2a60cf8e1`.
- SEXTIC, commit `7cd8baebbec29ad21def1f8b30e19c707a87aed5`, blob `3f65bbc68851837729aa9c20c526e3fb47ba8361`.

The TWELVE interface supplies the actual canonically decomposed source, the unsplit weighted target extension, the inherited maps, and the positive-degree filtration used in the obstruction. SEXTIC Section 2 supplies the universal exact P-evaluation sequence. Neither input is replaced by a character-only model.

## Whole-proof findings

1. The target projection to the unique V-isotypic quotient is canonical through the given target extension. It kills F without choosing a target section or complement.
2. The positive-degree filtration gives ordinary Hom(C,V O)=0 by the Hom exact sequence. No equivariant splitting of C and no selection of an actual necessary row is needed. Therefore the actual source projection cannot vanish.
3. The fixed identities V tensor W=T6 and V tensor A=P+D show that the linear source cannot reach V and that the quadratic P source has exactly one channel.
4. Dualizing the authenticated sextic evaluation sequence and twisting by O(-2) gives an everywhere-surjective P O(-2) to V O map with kernel O(-8). One-dimensionality makes every nonzero actual map in this channel a scalar multiple of that universal surjection. This justifies fiberwise, not merely generic, surjectivity.
5. The source kernel is intrinsically L plus E8 O(-1). Its canonical nature follows directly from the inherited source decomposition. The additional Hom and Ext tests are correct: H1(O(-7)) is Sym5 W=T6 equivariantly, while Sym7 W=W'+T6 excludes E8. Naming L as O(-8) only up to scalar does not choose a hidden shear.
6. The new target is the actual kernel of the canonical projection. Restricting its existing map to C is surjective because the source projection is surjective. Its kernel is exactly the computed source kernel. No false descent through a target quotient or unchosen section is used.
7. The weighted map F to C and its saturated image remain unchanged. Local freeness gives fiberwise injectivity of the new source. Ranks 9 and 14, source degree -16, target degree 10, and cokernel rank 5 and degree 26 agree.
8. The proof preserves its stated scope. It chooses no actual HM coefficient, point, parameter, matrix, instance rank, source pair, C type, or marked-subspace identification, and it does not use the separate conditional-endpoint exclusion.

## Reproduction checks

After reviewing the final verifier and reproduction instructions, the reviewer independently ran both commands successfully:

```text
python3 verify.py
python3 -O verify.py
```

Both reported:

```text
PASS: two immutable originals; unique quadratic channel; kernel Hom/Ext tests; positive filtration; nine-source rank and degree.
No actual HM/source coefficient, point, parameter, matrix, instance rank or scan evaluated.
```

The verifier uses explicit runtime checks, so optimized Python does not disable its assertions. Its bounded calculations concern fixed representations and universal degree balances only. The mathematical arguments above were reviewed independently of verifier success; this record is not a proof-assistant certification.
