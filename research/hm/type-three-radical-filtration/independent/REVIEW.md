# Independent review: conditional type III radical filtration

Verdict: PASS, conditional on the pinned PR1127 theorem and its dependencies. This is a review of the written mathematical proof and reproducible formal algebra, not proof-assistant verification or a new actual-source computation.

## Immutable reviewed packet

The reviewed companion packet is `type-three-radical-filtration`. SHA256 hashes:

- `PROOF.md`: `853418a2feb1acd138725a0a5ba494f29fd56bebf92f304e632e3be95248c3e7`
- `verify.py`: `83da89cc0e4dea19e7cdceb1540a09b570fa15c01c2b1e21df6f34ca7b029a84`
- `RESULT.json`: `742314cc16c40b79a6d017586f9f56c4d2691e7392e68fcdf4a9376f7b2dbee8`
- `INPUTS.json`: `55293661f9ad680ca876f7bd253ad421e43563ff4618e12cc91773eb066e8719`
- `README.md`: `e7a026f4e01671df49d325748826a3ed8e5a967e42a61cab8132bd482f5b5155`
- `inputs/PR1127-PROOF.md`: `3101157347802226a3b2638e76375854944d7a41d503b75b1591bc3eb66b1577`

The complete PR1127 proof was read, including its canonical retraction and conditional algebra calculation. Its public pinned source is https://github.com/Akilleez-QA/read-em-and-weep/blob/60dda5a940d5ba7ee081a86cd1b1a783a5952a39/research/hm/primary-quotient-composition/PROOF.md .

## Mathematical checks

1. The type III radical has precisely the three stated channels. The additional doublet L is isolated: all cross Hom spaces involving L vanish in type III. Thus the radical of End_G(E) agrees with that acting on K. This must not be generalized to other types without their Hom calculations.
2. With T=W tensor V and the fixed determinant identification, a is the tautological map and b is determinant contraction. They are equivariant. Their nonzero one-dimensional Hom channels fix them up to nonzero scalar. No actual source coefficient formula is required.
3. The two chart identities are identities over the coordinate localizations, not evaluations. They show a is a subbundle inclusion and b a bundle quotient at every point. Consequently image(a)=kernel(b) as sheaves and on every fiber.
4. The three independent radical operators kill precisely B plus image(a), and their images span precisely the same bundle. The common-kernel conditions on the two bottom summands are separate conditions; no cancellation between them is being assumed. The full stacked/concatenated matrix factorizations in the verifier correctly implement these assertions.
5. The quotient is locally free. The ranks and degrees are S:(6,-18), K/S:(9,-30), and Ann_E(J):(8,-24). Therefore saturation is established, not inferred from generic rank.
6. Evaluation image and common annihilator depend only on the intrinsic radical ideal. For any global equivariant endomorphism f, fJ is contained in J and Jf is contained in J, proving stability of image and annihilator. This gives canonical subbundles, not chosen canonical trivializations or arbitrary additional-operator compatibility.
7. Nonsplitting holds even for ordinary bundles: h0(K(2))=3, whereas the direct sum of the stated subbundle and quotient has h0=6. Square-zero composition of global equivariant operators does not imply splitting of their sheaf filtration.

## Independent overlap control

The separate standard-library `check_euler_overlap.py` uses its own one-variable Laurent arithmetic. In the x chart with t=y/x, a=(1,t)^t, b=(-t,1), and right inverses rho_x=(0,1)^t, rho_y=(-t^-1,0)^t satisfy

    rho_y-rho_x = a(-t^-1).

For Hom(O(-2),O(-4))=O(-2), the Cech quotient is C[t,t^-1]/(C[t]+t^-2 C[t^-1]). The exponent -1 cannot appear in either coboundary summand. Thus the extension class is nonzero. Tensoring with V gives coefficient matrix -Id_3, whose determinant is -1. This independently corroborates the nonzero Euler extension; the finite monomial controls supplement the stated exact support argument rather than replacing it.

## Reproduction

In the reviewed packet, `python verify.py` and `python -O verify.py` both reproduce `RESULT.json` byte-for-byte: 68 checks. In this review directory, `python check_euler_overlap.py` and `python -O check_euler_overlap.py` reproduce `REVIEW-RESULT.json` byte-for-byte: 51 checks. The added checker has no path dependencies and is relocatable.

No mathematical defect was found in the reviewed scope. No actual type is selected or eliminated; no positive-coordinate, invariant-quadratic, Gauss, source-coverage, full-adjoint, algebraicity, or complete original proof-repair assertion follows.
