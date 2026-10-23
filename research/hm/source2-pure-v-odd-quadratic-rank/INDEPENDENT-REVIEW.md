# Independent review: exact odd quadratic rank

## Verdict and frozen files

The exact-rank deduction and the conditional odd-nullhomotopy criterion are sound under the retained actual-source hypotheses. The proof does not determine the remaining row alignment or realize an actual source.

- `PROOF.md` SHA256: `65678e937f4d4f9de0261c6d4734707296d06fe916931460776751dba636f078`.
- `verify.py` SHA256: `3c98aa7a4e7a483c1a21edd2e9d27295185d06e30803290f190b160f329e1cb1`.

## Independent mathematical audit

**Actual generation in degree three.** The PR795 reconstruction identifies the first arrows with multiplication on sections of the same quotient bundle. Twisting its exact residual sequence by −3 gives end terms O(15) and A O(3), both with vanishing H1; the separated first block contributes Sym8 W tensor O(−1), also acyclic. The resulting Euler sequence proves W tensor N2 maps onto M3 without a horizontal residual splitting. This is the necessary input for the equality im Q3=mu(W tensor im Q2), rather than just one containment.

**Parity and commutation.** Q is the same central-even invariant polynomial in both degrees. Its multiplication commutes with each fixed negative coordinate and maps the odd degree-three source to the odd degree-five target. This does not extend the canonical homotopy or infer mixed homotopy commutation.

**Exact cokernel, with the embedded map retained.** The actual Koszul presentation of M5 gives the quotient by delta M3+W tensor im Q2. The first isomorphism theorem for j4 identifies M4/im Q2 with the actual I4. The inherited radical intertwining identifies the projected Koszul map with delta j3, so its image is exactly delta I3. Restricting the injective ambient delta proves that this image has character T, not merely dimension six. Hence coker Q3 is (W tensor P)/T=W′. Since the entire target is W′+3T, equivariance makes im Q3 the full T-isotypical component, of rank eighteen. The kernel character is consequently 3W′+3S+3T. No assertion that Q preserves NR or NC is needed.

**Odd homotopy criterion and normalization.** The equality I3=W I2 and Q2 I2=0 imply Q3 I3=0 literally. Thus (j3,0) is a chain endomorphism. Necessity of j3|ker Q3=0 follows from kQ3=j3. Conversely, that vanishing defines the factor im Q3→I3, and extending by zero on the canonical W′-isotypical complement gives both homotopy identities. Hom(W′,I3)=0 makes this image-in-I3 normalization unique. Without that normalization the ambiguity is Hom(coker Q3,ker Q3), of dimension three, as stated. On the T multiplicity spaces the criterion is exactly combined rank three rather than four.

**Limits of the controls.** The two abstract matrix controls verify that rank, square-zero, and image-in-kernel statements alone do not imply row alignment. They do not realize the full actual source, prove realizability of either alignment branch, or decide the geometric interface. The proof correctly does not promote these controls to actual examples.

## Authentication and reproduction

All four complete originals were independently retrieved from the repository at the precise commits and paths in `INPUTS.json`. Their bytes matched the retained files exactly; independently computed SHA256 and Git blob hashes matched the manifest. The authenticated commit/blob pairs are:

| Input | Commit | Git blob |
|---|---|---|
| 795 | `3f811311d76914a555c7e7d0c5b887b41805aa6c` | `9358ec81c552913fac20f3a92d7b9f7c58105656` |
| 1019 | `3fb2475ffb275c5789acbaa8f9f84ed272713785` | `bf63c14f76933d59fa7e3ac61aecb3366ac1b442` |
| 1052 | `64e4fdd771a14a764c6e119d2eb25b0237d83622` | `b0be6d47a234bbfc3e49f94c8cc295d8b5129a7d` |
| 792 | `2f01f18960ce56b8b2a0c1260c277de3c5f916bf` | `76bee93507d1a2d0840926d4e4e27edadfebb7d7` |

Independent runs of `python verify.py` and `python -O verify.py` each passed all 28 checks. Both outputs were byte-identical to one another and to `RESULT.json`. The verifier uses explicit exceptions, not optimization-sensitive assertions. Its representation and synthetic controls supplement, rather than replace, the actual-map audit above.

This review authenticates the immediate inputs and their interfaces; it does not claim a recursive reproof of every ancestral geometric result. No actual coefficient, direction or source-instance rank was evaluated.

Independent mathematical review completed 2026-10-23.
