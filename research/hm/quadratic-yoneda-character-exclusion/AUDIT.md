# Independent formal audit

The proof was checked against the existing pair-character proof and invariant-row/family proofs, without relying on a historical singleton Ext¹ dimension or any evaluated model.

- **Complementary duality:** Correct formula is B_S^*(−5)=B_{S^c}. For singleton and triple characters, use two independent Euler lifts; do not assert B_S is self-dual. The dual of the complementary lift gives the required retraction.
- **Euler lifting:** For each positive i used in the coresolution, all positive cohomology of B_S(i) vanishes. The Hom connecting maps therefore reach the unique intermediate class. Naturality verifies that the resulting morphism induces the desired nonzero intermediate-cohomology map.
- **Splitting:** The composite has nonzero cohomology and is scalar because Ω^r is simple. Removing it removes the sole intermediate cohomology in all twists. Horrocks applies to the vector-bundle complement. H⁰(B_S(1))=0 bounds all remaining line summands by a≥2.
- **Triple-character vanishing:** Only H⁰(FΩ²)=0 and H¹(F(−3))=0 are needed. The former follows from injection into F(−2)^10, independent of any multiplication-map rank.
- **Full character:** It has no intermediate pushforward cohomology; Horrocks and the same line-twist bound suffice. There is no need to identify its individual O(−5) summand.
- **Singleton equivariance:** The stabilizer permutes only degree-zero Künneth factors, so the unique H¹ generator is fixed. Averaging preserves the nonzero Euler lift. Cohomological identification with U is equivariant even though a chosen complement need not initially be equivariant.
- **No hidden S4 action on U:** Factor permutations act trivially on the symmetric quotient P⁴ and on its pulled-back F. Thus the stabilizer representation is a direct sum of trivial representations; induction produces exactly the ordinary four-letter permutation representation tensored with U.
- **Quadratic source:** Distinct singleton characters do not multiply to the trivial deck character. The only non-invariant source of an invariant quadratic product is the direct sum of the four same-character symmetric squares, not Sym²(U⊗k^4) without its deck grading.
- **Invariant-family use:** The family proves vanishing only of the ordinary quadratic obstruction and its polarization on invariant Ext¹. This is sufficient. It does not prove ordered products vanish.
- **Serre twist:** H⁴(O_X) has full deck character and sign permutation character. The sign twist fixes [22], so the required detector type remains invariant [22].

Verdict: the structural exclusion holds for the ordinary polarized quadratic Yoneda map, under the stated established HM/coefficient-family inputs. The ordered invariant-invariant alternating product is explicitly outside the conclusion.
