# Historical mathematical audit receipt

This is a preserved review of the source mathematical manuscript, not a fresh review of the publication bytes. Hashes quoted below identify the historical source versions. See [hm-lowest-generation-PUBLICATION-CHECK.md](../hm-lowest-generation-PUBLICATION-CHECK.md) for the final-publication review.

# Independent audit: abelian-surface endpoint

A separate auditor checked the proof independently and confirmed the following.

1. The Serre sequence for a regular section of normalized F(3) is 0→O(−3)→F→I_A(2)→0. Tensoring by F∨(t)=F(t+1) gives the terms F(t−2), EndF(t), I_A⊗F(t+3), with no Tor issue.
2. The normal bundle is F(3)|A, so restriction of F(t+3) gives N(t), not a shifted normal bundle.
3. For t≥1, the restricted Euler sequence kills H¹(T_P⁴|A(t)); tangent-normal then kills H¹N(t), using the trivial abelian tangent bundle and positive Kodaira vanishing.
4. Two exact cohomology segments prove vanishing without any assumption about an incoming map's rank. In particular no surjectivity is inferred from dimensions.
5. The proof only needs H²F supported at −2. The full H¹ table is needed for the optional isomorphism but not for the vanishing result. This dependency reduction was identified by the auditor and incorporated in the main proof.
6. The endpoint t=1 has t−2=−1 and t+3=4, both different from −2. There is no missing endpoint assumption.
7. Trace splitting is valid over C. The result concerns the actual fixed HM bundle, not a deformation or an arbitrary bundle with the same Hilbert function.

Primary-source check by the proof author: HM 1973 Theorem 5.1 is on printed p.75 and concerns their unnormalized bundle; their c₁=5,c₂=10 computation is on p.70. Normalization translates that bundle to F(3). The theorem yields a regular smooth abelian zero surface for a general section. An origin on the surface is not needed; choosing one identifies its tangent bundle as trivial. Decker's independently verified H²F support theorem supplies the sole remaining HM-specific cohomology input.

The argument does not extend to t=0 by this chase: H²F(t−2)=H²F(−2) is nonzero, and O_A(t) is no longer ample. This is consistent with h²B=2. It makes no claim about H⁰B(1), lowest multiplication, socle vanishing, or secondary-map ranks.

## Consequence and low-section audit

The separate auditor subsequently checked §§4A–D against their referenced exact criteria and found no error. The low-section sequence in §5 uses H²F(−1)=0 in addition to the stated H⁰/H¹ vanishings, already supplied in §3. It is exact with dimensions 35→85. Under the rank-two identification, scalar endomorphisms map to s·S₁ up to an immaterial common sign. Hence the induced 30→85 injectivity criterion is correct; it is not an evaluated rank.

For precision about §4A, let I be the image of H²(C)→H²B(−4). Dualizing the inclusion-image factorization identifies I∨ canonically with H²B(−1)/im δ_N. Since im δ_N=ker σ and σ now has the full ten-dimensional domain, the first-isomorphism theorem identifies this quotient canonically with im σ. No choice of a complement or pairing basis is needed.
