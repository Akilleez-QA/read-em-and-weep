# Independent review of the radical-square image geometry

Verdict: accepted as a conditional theorem for the two named necessary bundle types, relative to the explicitly pinned representation and radical-algebra dependencies. This is not a type-occurrence, case-exclusion, geometric-coverage, or complete proof-repair result.

## Reviewed immutable inputs

The complete retained proofs of PR1127 (commit `60dda5a940d5ba7ee081a86cd1b1a783a5952a39`) and PR1031 (commit `7150cf97eeebe473bcd7c61c1f968c73625d92ef`) and PR1031's universal `model.py` were read. Their byte hashes and Git blob hashes pass the author's manifest checks. The displayed projection in the new verifier agrees entrywise with PR1031. The review uses only its universal representation model, not its actual-source hypotheses.

The reviewed packet's SHA256 hashes are:

- PROOF.md: `959fb186dc1e5975c33cc879a57d08080e00f9b5abd2749e67d78663fc74c995`
- verify.py: `a34695c8e7c995b82aa8157abd4d6cbfd60f244b30ede882063f7084a336d72d`
- RESULT.json: `ab91988859615ebb813efb7195a95a8d23e509a0b0f09f86d467d7f2c21d27c8`
- INPUTS.json: `7c0a7b599ae0b62eac314d3962058bbd8f081c812ca8e0ff2343c76cee96b40f`

## Mathematical checks

1. The maps are the two channels identified by PR1127, with no change of parameter line: second polarization on ker Pi, and Pi composed with determinant multiplication and first polarization. Nonzero scalar normalization does not change image or cokernel.
2. All maximal minors are checked, not a selected minor or sampled point. For type I their coefficient span is the entire sextic space. The separate review checker uses successive polynomial extended gcd computations to establish Bezout identities on BOTH complete symbolic charts for each type. Thus there is no common projective zero, including at infinity and over C. The chart normalizations are coordinate descriptions, not actual-direction rank experiments.
3. Constant rank three makes each map an injection of vector bundles with locally free cokernel. The image is consequently saturated and isomorphic to its source V O(-4). Its rank and degree are three and minus twelve.
4. For the type-I cokernel C, dualizing the twisted sequence gives kernel C*(-2) of the transpose map 5O to 3O(2). Degree-two polynomial syzygies are exactly H0(C*). The independently assembled 15-by-15 convolution matrix has full rank. Therefore, if C=O(a)+O(b), then a+b=2 and a,b>0, forcing a=b=1. This does not infer balancing from degree alone.
5. After balancing, the cohomology sequence identifies H0(C) with the kernel of V tensor Sym2 W onto D, hence P using the pinned tensor identity. The equivariant coefficient doublet R of C=R O(1) therefore satisfies R tensor W=P, uniquely giving W'. Finite-group semisimplicity and the two doublet characters exclude the reducible alternative.
6. The type-II cokernel has rank one and degree four. Its equivariant linearization is the standard O(4), since SL2(F5) has no nontrivial one-dimensional character. Neither this argument nor the type-I argument asserts a positive subbundle of E.
7. The square of the Jacobson radical is intrinsic and a two-sided ideal of End_G(E). Its evaluation image is independent of generator, scalar, and chosen catalogue identification, and is preserved by every equivariant endomorphism. The source identification is not claimed canonical. The pinned retraction to W' O(-3) kills this image, placing it inside K.
8. Section 4 now correctly RETAINS the original source V O(-4) in all four quotient decompositions: the image being divided out lies in the top D/P block. The displayed E/S bundles have rank fourteen and degree minus forty-two; K/S has rank twelve and degree minus thirty-six. Abstract quotient types are not canonical direct-sum splittings.

## Reproduction and independent controls

Run the author's `verify.py` normally and with `python -O`; both outputs agree byte-for-byte with the reviewed RESULT.json.

The accompanying `check.py` is relocatable: run `python check.py PATH_TO_PACKET`, and repeat with `python -O`. It constructs the two full matrices independently via coefficient-index differential and multiplication matrices, compares every recorded entry and maximal minor, verifies both symbolic-chart Bezout identities, builds independent transpose convolution matrices, and checks all four quotient ranks/degrees. Its 30 checks pass identically normally and with optimization. The accompanying RESULT.json binds its findings to the hashes above.

No actual HM/source matrix, coefficient selection, sampled direction, jet, or consumed experiment was evaluated. Review and synthetic/universal checks do not establish the underlying geometric dependency theorems anew. The result is a new conditional intrinsic filtration and exact quotient geometry, not elimination of either remaining type.
