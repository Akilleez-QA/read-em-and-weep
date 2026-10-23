# Independent mathematical verification

## Verdict and exact bytes

The stated conditional compatibility reduction is valid for the following SHA-256 hashes:

- PROOF.md: aa2cdb4c2432947a8e3f99e8fd10486e9d58b4930513f2e78a03622cd67c2069
- verify.py: d316e252dee0cceaefed3cd3ec0a6399fc503b26d0e97d23947cb7e18e0a84a6
- INPUTS.json: 4bca701b2a13bf9d6f9df3799ea88a47f546e8948616da786928dcac6ff05458
- RESULT.json: c2983d24840caa6db7c319b2d31c744f3caf4d9f3007dc12051fa9fe98507754

The checked conclusion is D_Q=C·1⊕J_Q with J_Q contained in the two-dimensional square-zero radical. Its dimension is 1, 2 or 3. No source, quotient profile or catalogue pairing is excluded, and scalarity is not proved.

## Mathematical checks

1. The exact PR862 algebra proof was read, including covariant full faithfulness, the three residual templates, radical orientation and multiplication. Its Git blob e18035dcceb1c7e0d0d4356ee578937d3172390b was independently retrieved at commit e103e25456897a1123f9636eb20080e8641ce66a. PR856's block characters and constant separation were checked against blob 8a5522965ac861b5c4e149724782a489c5afb7cd at commit cee45480686c39a321feaa77d4b669682cc71efe.
2. The invariant-product theorem was independently retrieved at eeb1a11799ca38a60c37f6ba96f263ef8e20dd1c, blob 019c1f31773476f0a4877d88632ce5d46fbd4b9f. It states the actual image character 2V+3P+3D of dimension 33. The same-product convention was read in the pinned PR929 proof. The geometric theorem's entire ancestry was not re-proved here; it remains an explicit imported hypothesis.
3. The endpoint reconstruction uses direct constant summands, not a new quotient splitting. Global generation of the total quotient twisted by -1 descends to each direct summand. Therefore the required H1 at twist -2 vanishes. The displayed cohomology exact sequence and character subtractions are valid.
4. All fourteen proper nonempty vertex subsets were independently enumerated using the endpoint characters. The F/complement upper image is 2P+3D, dimension 23. Each X/complement and Y/complement upper image in Types I and III is V+3P+3D, dimension 30. A draft Type-I-X bound of 26 was corrected to 30: its complement has three, not two, possible P constituents. The correction does not affect the contradiction with 33.
5. Every idempotent is conjugate to a diagonal subset projector. For each arrow, equal diagonal bits force the arrow coefficient to vanish; unequal bits allow its elimination by the stated 1+c conjugation. Since that unit is a G-equivariant pencil automorphism, image and kernel characters are preserved in both endpoint degrees. No assertion that the conjugating unit commutes with Q is needed or used.
6. Compatibility with Q makes its source and target decompositions block diagonal. The constituentwise rank bound therefore applies to the actual sheared idempotent. Every bound lacks at least one required V, excluding every nontrivial compatible idempotent.
7. The polynomial lifting argument is correct without identifying the radical of a subalgebra in advance. If h has more than one distinct diagonal value, p(h) lies in J and p(h)^2=0. Hermite interpolation modulo the pairwise coprime squared linear factors gives an idempotent polynomial f(h) with nonconstant diagonal, a contradiction. Thus all compatible elements have scalar diagonal. The remaining radical intersection is square zero, and the explicit inverse for nonzero scalar part proves locality and the stated radical equality.

## Reproducible checks and limits

Both python verify.py and python -O verify.py completed with 173 checks and the same fourteen-subset result. The input SHA-256 and Git blob calculations all passed. The checker uses explicit exceptions, so optimized Python does not remove its checks. Its arithmetic and formal shear checks supplement the proof; neither these checks nor this review constitute proof-assistant verification. No selected actual tensor, coefficient, matrix, point, derivative or instance rank was evaluated. The surviving square-zero radical may be nonzero, and this result does not settle the complete proof repair.
