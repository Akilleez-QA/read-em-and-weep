# Historical mathematical audit receipt

This is a preserved review of the source mathematical manuscript, not a fresh review of the publication bytes. Hashes quoted below identify the historical source versions. See [hm-normalizer-foundations-PUBLICATION-CHECK.md](../hm-normalizer-foundations-PUBLICATION-CHECK.md) for the final-publication review.

# Stability, duality and the HM cohomology rows

Mathematical excerpt of the historical audit, items 4–6; the primary proposition is recorded in ../hm_primary_source_verification.md.

4. **Stability and Hom vanishing.** The classical monad gives H⁰(H) = 0. For rank two with c₁ = −1, a destabilizing saturated rank-one subsheaf has double dual O(d), d ≥ 0. The resulting map extends over codimension at least two because H is locally free. A section of H(−d) multiplied by a nonzero section of O(d) contradicts H⁰(H) = 0. Stability gives simplicity. Twisting preserves stability and reduces slope when t < 0, so Hom(H,H(t)) = 0 for t < 0. Thus the claimed h⁰ values follow.

5. **Serre duality.** The trace pairing identifies End H with its dual, and K_P⁴ = O(−5). For t = 0,−1,−2,−3 the dual twists are −5,−4,−3,−2. Negative-twist h⁰ vanishing implies h⁴ = 0; the primary proposition implies h³ = 0 at all four twists. There is no missing negative twist or cohomological shift.

6. **Riemann–Roch.** The formal root difference satisfies (x₁−x₂)² = c₁²−4c₂ = −15h², giving ch(End H) = 4−15h²+(75/4)h⁴. With td₁ = 5h/2 and td₂ = 35h²/12, the Euler polynomial is

   χ(End H(t)) = 4 binom(t+4,4) − (15/2)t² − (75/2)t −25.

   Its values at 0,−1,−2,−3 are −21,5,20,20. Together with the verified h¹ values, h⁰ and the vanishing h³,h⁴, this yields the complete rows

   (1,24,2,0,0), (0,5,10,0,0), (0,0,20,0,0), (0,0,20,0,0).

