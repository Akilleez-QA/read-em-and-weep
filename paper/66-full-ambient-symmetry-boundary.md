# The full ambient symmetry boundary for the octic scalar

**Craig Ward · 23 October 2026 · PR1023**

Sources: [initial normalizer proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/102d3bf0291539557baf75a46ac3701b517e94a6/research/hm/source126-typeII-normalizer-boundary/PROOF.md), [full-symmetry closure](https://github.com/Akilleez-QA/read-em-and-weep/blob/102d3bf0291539557baf75a46ac3701b517e94a6/research/hm/source126-typeII-normalizer-boundary/FULL-SYMMETRY-CLOSURE.md). The closure explicitly supersedes the initial proof's outside-normalizer qualification.

## 1. Exact fixed-quadric stabilizer

The projective Heisenberg normalizer N̄ has order3000 and contains the existing embedded G=SL₂(F₅), of order120. The chosen negative line L has 25 distinct Heisenberg translates. Since G fixes L, orbit–stabilizer bounds its N̄ orbit above by 25; the known translates bound it below by 25. Hence Stab_N̄(L)=G.

The fixed invariant rank-three quadric Q₀ has vertex L. Any automorphism preserving [Q₀] must preserve that vertex, and all G preserves Q₀. Thus Stab_N̄([Q₀])=G, also the stabilizer of Q₀ together with the fixed negative pencil. The canonical octic line is G-fixed, so this group supplies no additional character that could force its scalar to vanish.

## 2. Decker closes the full ambient loophole

W. Decker, Math. Z.188 (1984), 101–110, [DOI10.1007/BF01163877](https://doi.org/10.1007/BF01163877), Definition4.1 (p106) and Theorem4.2.3 (p109), identifies the **full** SL₅ ambient pullback stabilizer of the normalized HM bundle with the Heisenberg normalizer. This is credited published mathematics, not a new group discovery. The source packet records verification against primary page images and exact locators in the [public primary scan](https://gdz.sub.uni-goettingen.de/download/pdf/PPN266833020_0188/PPN266833020_0188.pdf).

Every projective transformation lifts to SL₅ and the lift ambiguity is μ₅. Therefore

    Aut_proj(F)={s∈PGL₅:s*F≅F}=N₅/μ₅,
    Stab_Aut_proj(F)([Q₀])=G.

The inverse-pullback convention and normalization twist do not change the stabilizer; coordinate change conjugates both groups together. Vertical scalar automorphisms are different and act trivially by conjugation on End₀(F).

The new application is that **no extra ambient same-bundle, same-Q₀ symmetry outside the normalizer exists** to reopen this proposed octic-character route. Merely knowing finiteness or “15000 symmetries” would not have justified this conclusion; the full-group theorem is essential.

## 3. Remaining boundary

The tempting order-four block scaling changes the actual ambient bundle, even though it preserves a cone restriction. It cannot be inserted into same-object naturality. Cone-only automorphisms, formal-neighborhood symmetries and nonambient complex automorphisms are not classified here and require their own compatibility arguments.

The actual octic scalar remains unknown. Its [coefficient extraction formula](62-octic-normal-lift-and-scalar-address.md) still requires an actual lift. No ninth or higher internal symbol, source exclusion or complete repair follows. Four necessary pairs across three labels remain.

The packet reports independent reviews, 33 finite-group checks and 19 closure checks, in ordinary and optimized execution. These verify dependencies and group arithmetic, not Decker's theorem by machine or a new actual HM instance. The full-volume primary scan is not redistributed.
