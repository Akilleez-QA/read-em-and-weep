> Publication scope: Explicit two-factor pushforward splitting gives H0/H1 vanishing; mixed gauge comparison still imports actual source identities. Source-stage audit/checker references describe historical evidence, not fresh execution or bundled executable artifacts. Named source identities are hypotheses unless separately proved below.

# Independent audit: pair-character vanishing

Verdict: PASS for the stated additive cohomology and conditional linearized-gauge conclusions. No correction is required.

Audited proof: `PROOF.md`, SHA-256 `0242f767b032d85ea29c255a0fd6c952fccacdcff3a8a6375bdf5c0471d38db9`.

## Checks

1. The finite quotient is flat by the Cohen–Macaulay/regular-target criterion. Finite duality correctly gives `(σ_*L_S)^*=σ_*(L_S^{-1}⊗ω_Y⊗σ^*ω_P^{-1})=B_{S^c}(5)`. A permutation over the symmetric quotient identifies complementary pushforwards. The resulting self-duality need not be symmetric.
2. Künneth correctly leaves only the one-dimensional intermediate group `H²(B)=k`. The first Euler Hom sequence identifies `Ext¹(Ω¹,B)` with `H²(B)` using both `H¹(B(1))=0` and `H²(B(1))=0`; the second gives the required surjection from `Hom(Ω²,B)` using `H¹(B(2))=0`. Naturality of the Euler two-extension identifies its image with `H²(f)` of the generator.
3. Serre duality identifies the middle cohomology of the dual-twisted map with the dual of `H²(f)`. The chosen self-duality of B preserves nonzero middle classes, so `H²(gf)≠0`. The Euler argument for `End(Ω²)=k` is valid: `Ω²(1)` and `Ω²(2)` are acyclic; the second Hom sequence has zero terms on both sides of the connecting map. Thus `gf` is an invertible scalar, proving a genuine vector-bundle direct summand.
4. Removing that summand removes every intermediate cohomology group in every twist. Horrocks applies. The absence of sections at twist 1 forces all remaining line summands to have degrees at most −2. Twist 2 gives nine copies of `O(−2)`; twist 3 gives nine of `O(−3)`, using `h⁰(Ω²(3))=10`. Their number exhausts rank 18. There is no unproved multiplicative splitting.
5. Stability yields `H⁰(End H(t))=0` for negative t, by the slope-Hom vanishing between H and H(t). The stated published theorem supplies `H¹(End H(t))=0` for t≤−2. In the tensor Euler coresolution the kernel K is a subsheaf of `F(−1)^5`, hence has no global sections. The ensuing long exact sequence proves both required vanishings for `F⊗Ω²`, without assumptions on `H¹(F(−1))`.
6. Projection formula, exact character eigenspaces, and cancellation of the line twist give the two-factor Ext⁰/Ext¹ vanishings. Rational descent and extension to characteristic-zero base fields are correctly limited to the stipulated rational data.
7. The gauge conclusion is accurately limited to solutions of the same prescribed right-hand side. H¹ proves gauge matching conditional on existence; H⁰ proves uniqueness only in a nonnegative model, or modulo degree-minus-one boundaries otherwise. No mixed covariance or actual source primitive identity follows from the additive result alone.

## Dependency boundary

I statically read the linked exact-presentation proof and the primary-source verification note. The classical negative-twist cohomology theorem is imported as a published result, with its primary-source verification documented by that note; this audit did not independently reopen the scan. No historical source primitive receipt, rank certificate, or total Ext¹ dimension is used.

Read dependency hashes:

- `../../hm-presentation-independent/PROOF.md`: `ed549d3b6d19c1fbef269d390a6313269a369d8616a9343991e43585460915b7`
- `original-source:projective-target-directions/HM-PRIMARY-SOURCE-VERIFICATION.md (historical primary-source verification; not bundled)`: `b14f1c1c08b24c015da73ad081a462e0b100831d01db004c96c678e5fc310071`
- `../../cubic-loci/foundation-p01/INVARIANT-COHOMOLOGY.md`: `eacc48f56c970b8037b6aa5fc566eb1458161495dadd6f815348de23c11733a4`

Only formal mathematical reasoning, static document reads, and document hashing were performed. No source/model/rank/polynomial-instance/point/jet/residual evaluation or execution was performed. The forthcoming mixed-gerbe/descent argument requires its own audit.
