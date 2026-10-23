# Independent whole-package review

Verdict: PASS. No mathematical correction or publication blocker found.

This review is independent of the package author. The reviewer first completed a separate universal square-quotient proof, then freshly read this entire final package, including the added finite-group uniqueness statement and actual-image application. The earlier review of the standalone universal proof is not being substituted for this final review.

## Exact final reviewed bytes

SHA256:

- PROOF.md: 16c1e503c03a1d3741d42f4016e585598ba0ff1844e3ff875c73dc4a1988b110
- verify.py: 9e39769b4c439439575cab9db4812691b64022889600f453edb71b1994742897
- INPUTS.json: 2ef770d7db2a5fdd9430e384e261a2b1590a9ec672e34abe99e24213f2d1e68c

The reviewer independently retrieved both inputs through the connected GitHub tool at their exact immutable commits and compared the returned decoded bytes with the corresponding audit-inputs copies. Both comparisons were byte-for-byte equal:

- SQUARE, commit db51525015bb7c5e825833d550d08dedf6f6ea96, research/hm/order-four-quadratic-load/HYPERPLANE-SQUARE-SURVIVORS.md: 11420 bytes; Git blob fb8a25eb2c7ef571f9a570fd5d1ee8a4ea17327a; SHA256 036a45ff8998e84c9a967808faed91d6ce9283cc686e2fbb8c378b095beb7b2d.
- RANK, commit 2f3eb11a6f55582e17f56c8bc9b310db9a37424d, research/hm/ninth-neighborhood-rank/PROOF.md: 9126 bytes; Git blob 1bd120e8ff07143d4f65d307f820c252daa18082; SHA256 24ccacc3e8da0c6cb8e9fdc73bc07c92e6f50bdeb36ee7e0cca1af22e8415c2f.

## Mathematical findings

1. The square inclusion is the actual symmetric square of l^3 W inside Sym4 W, rather than an arbitrary degree-six coefficient map. Its multiplication and second-transvectant components are nonzero; the invariant fourth-transvectant component vanishes.
2. The untwisted dual map therefore has kernel 1 and cokernel Sym6 W. The twist-one map is correctly obtained by multiplication on the base-section factor. All three required irreducible channels, Sym9, Sym7 and Sym5, are explicitly nonzero. In particular the Sym7 image has the displayed coefficient 1/4.
3. Global generation, the two dual section dimensions, rank 12 and degree 18 force the ordinary splitting O+4O(1)+7O(2). Serre duality and the degree-one kernel identify the coefficient representations as 1, Sym3 W and Sym6 W. Reductivity supplies equivariant splittings of the HN extensions because the underlying Ext1 groups vanish.
4. The new uniqueness claim after restriction to the binary icosahedral group is valid. The upward ambiguity targets are respectively A+D, V+2P+2D, and Wp+2T. They contain neither the required trivial representation in the first two cases nor S in the last. Downward homomorphisms vanish by degree. This proves unique equivariant complementary subbundles, not scalar-normalized identifications with abstract named modules.
5. The actual transfer uses matching maps, not dimensions alone. SQUARE Sections 5-6 identifies the actual section inclusion with the cubic-tautological inclusion and the actual plane product space with Sym2 D. RANK Sections 3-4 identifies the quotient of the target by im Theta with the transpose of that very square restriction. Hence im Theta is the dual actual square quotient with twist O(8), and the stated O(8)+S O(7)+(V+P) O(6) splitting follows. The rank 12 and degree 78 agree independently with RANK.
6. Identifying P(W) with the actual direction line P(W*) uses the fixed determinant form. This preserves the standard SL2 linearizations used throughout. Duality and twisting preserve the asserted equivariant degree-piece splitting, with degrees reversed as appropriate.

## Verification performed

The reviewer inspected verify.py and independently ran both:

    python verify.py
    python -O verify.py

Both returned PASS with 44 checks and identical output. The checks use explicit runtime failures, not optimization-removable assertions. Their mathematical content is bounded universal symbolic transvectants, exact highest-weight identities, abstract characters, numerical rank/degree bookkeeping, and input-byte authentication. No selected HM point, actual coefficient, actual jet, instance rank, source sample, or large computation was introduced.

The verifier supports but does not replace the written cohomological argument or the geometric input theorem. No proof-assistant certification is claimed.

## Scope and limits

This review certifies the final square-quotient and image-bundle splitting, the uniqueness of its equivariant degree-piece complements, and the stated transfer from the two pinned actual inputs. It does not independently reconstruct all earlier dependencies of SQUARE or RANK. It does not determine ker Theta's splitting, split the source-to-image sequence or the original first-cup kernel extension, identify the opposite bundle C, select a scalar of Theta, determine sigma or delta, or change the source/frontier ledger. Those boundaries are accurately retained in the authored proof.
