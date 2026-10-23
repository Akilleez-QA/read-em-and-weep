# Independent review: source2 invariant-product compatibility

Verdict: PASS, conditional on the exact imported geometric theorems and their stated actual-source hypotheses. This review does not re-prove their entire ancestry or certify them in a proof assistant.

## Frozen artifacts

SHA-256 digests of the reviewed bytes:

- PROOF.md: 5cf4b0e0a14d5c072252ec55b5e308693bd5446b630baa96c7ed8fe56c077102
- verify.py: c4e78276eb72ecc6cbc57818acef4855749106b29c5589575f6746c9f4e7add8
- INPUTS.json: 29e1e8c0ff7d0e48762acd164f1788ee716297231004d40ca3459b9a89618fff
- RESULT.json: b9110a3182102cb7aa52817418b9d9c47700e1c3ddb84775c2c2be47546b6a0c

All seven source files in INPUTS.json were independently fetched at the listed immutable commits through the repository connector. Each returned Git blob identifier agrees with the manifest. The local verifier independently recomputed both SHA-256 and Git-blob hashes from the copied bytes. This includes PR935, blob 187fe2a8c1499e11afdb5002091aa3c144e1b4a3; its exact trailing newline is included in the checked bytes.

## Mathematical checks

1. PR790 Section 6 identifies reconstructed first and second arrows simultaneously with the original fixed negative multiplications. PR791 gives the entire represented algebra, not only its units. Its duality reverses the radical direction; the candidate uses the correct direction from N0 to NC (inside NR). The isolated N8 factor exists only in the zero-coupling class. No residual horizontal splitting is inferred in the nonzero class.

2. The equation for idempotents in the square-zero triangular algebra is correct. Conjugation by 1+c with c=b/(epsilon_source-epsilon_target) has the stated sign and yields the idempotent. The conjugating unit is used only to preserve image and kernel characters, not assumed compatible with Q. Six zero-coupling and two nonzero-coupling subsets exhaust proper diagonal idempotents.

3. Independently recomputing the two endpoint constituent minima gives total image bound V+3P+3D, dimension 30, for the N0 and NC partitions. This contradicts the imported actual image 2V+3P+3D, dimension 33. The remaining N8 partition saturates exactly. Thus its Q block would be onto V+P+D with kernel the unique actual A in N2. Every negative quadratic preserves this genuine block.

4. The right-inverse argument is valid for a preserved pair of subspaces, not only for a direct summand. With Q(U)=Z and T_a(U) contained in Z, u=-sT_a k solves Qu=-T_a k and T_a u lies in im Q. The imported first-Bockstein theorem concerns exactly this q0+t a pencil and vanishes on the whole original kernel. It makes the correction independent and identifies the vanishing class with the actual second Bockstein. The pinned second theorem proves that same A-to-P family is nonzero; nonvanishing of a family, rather than at every parameter, suffices for the contradiction.

5. Absence of proper idempotents forces scalar diagonal by polynomial interpolation modulo the squared distinct linear factors. Since p(h) belongs to J and J squared is zero, the Chinese-remainder argument applies even when h is not semisimple. Consequently D_Q=C1 direct-sum J_Q. The sentence in Section 5 saying 'This proves (1)' should be read as the scalar-diagonal decomposition, since the dimension bound is explicitly completed in Section 6; this is a minor cross-reference imprecision, not a mathematical gap.

6. The stronger full-radical argument is correct for every balanced endpoint and both coupling classes. PR795 gives the intrinsic annihilator as an actual subpencil with endpoints U=A+2V+2P+3D and Z=2V+2P+2D, dimensions 32 and 24. If every j in J is Q-compatible, it preserves ker Q=A+D. Schur's lemma and square-zero nilpotence force its restriction to this multiplicity-free kernel to vanish, so ker Q is contained in U. Compatibility gives Q(U) contained in Z, and the exact kernel dimension eight forces rank 24, hence surjectivity. This contains the unique actual A and is stable under all negative quadratics. Applying the same correction argument contradicts the same nonzero second Bockstein. Thus J_Q is proper in the two-dimensional J and has dimension at most one. No complement, horizontal splitting, or extension of an endomorphism to the full HM module is needed.

## Reproduction and limits

Independent runs of python verify.py and python -O verify.py each pass 468 explicit checks. Their outputs are byte-identical to each other and to RESULT.json. The script uses explicit RuntimeError checks rather than removable assertions. Its rational algebra, representation arithmetic, and formal recurrence examples are bounded diagnostics supporting the written universal proof; they are not an actual HM instance computation or a substitute for the imported geometric nonvanishing.

The conclusion is scalar or possibly dual-number invariant-product-compatible algebra. It excludes all proper compatible idempotents and compatibility of the whole two-dimensional radical. It does not determine a remaining radical line, prove scalarity, exclude source2 or its E13/Q21 pair, decrement the four-pair frontier, or complete the original proof repair. No external publication or actual coefficient, point, tensor, or instance-rank evaluation was performed for this review.
