# Audit of the twist-two vanishing proof

## Version and verdict

This review covers the complete [PROOF.md](PROOF.md), with SHA-256:

    278e89116e55f35db50380b7f76336a85c6d728760995b8f782daeda9a5def6f

No substantive mathematical gap was found in that version. The argument proves the stated twist-two vanishing and companion cohomology, subject to its explicitly stated twist-one prerequisite. That prerequisite is published in [PR #91](https://github.com/Akilleez-QA/read-em-and-weep/pull/91), pinned to [commit ee7c4d4627c2efa07ea167a535cf1582002ef335](https://github.com/Akilleez-QA/read-em-and-weep/commit/ee7c4d4627c2efa07ea167a535cf1582002ef335); neither this review nor the proof represents it as merged or independently accepted.

This is a mathematical review, not a formal verification or an assertion of novelty. Any change to the proof requires a new version check.

## Checks

1. **Primary numerical inputs and resolution.** Decker's printed pages 15–16 identify the section-module resolution with the appropriate summands of the first-cohomology resolution. Their comparison gives precisely the shifts and multiplicities in (R), not a resolution of an endomorphism module. Tensoring by the locally free F*(2)=F(3) is exact. The normalization and duality used for the HM cohomology table are consistent.

2. **The zero-or-five reduction.** The only nonzero sheaf-cohomology entries of the tensor resolution are the three displayed terms, of dimensions 20, 70, and 20 in positions (−3,3), (−1,2), and (0,1). The first is the unique total-degree-zero term and has no incoming differential; hence H⁰End(F)(2) has dimension at most 20. The scalar summand contributes h⁰O(2)=15. The nontrivial central character forces the remaining dimension to be a multiple of five. No refined representation decomposition or claim about a particular differential is needed. The total degrees and alternating sum also give χB(2)=−85 and the higher vanishings.

3. **Central symmetry and line bundles.** The center acts by ζ³ on both the evaluation source and target. The proof that N has no characters is sufficient: a character kills [H₅,H₅]=μ₅, its restriction to H₅/μ₅ must be SL₂(F₅)-invariant, and the remaining quotient is perfect. Thus comparisons with standard line-bundle linearizations are valid. HM Theorem 3.5 supplies the asserted absence of an N-invariant quintic.

4. **Generic rank.** Saturating the image preserves its generic rank and gives an equivariant determinant O(a). A nonzero wedge of the generating sections implies a≥0. The determinant inclusion extends across codimension two into the locally free exterior power of B(2). Its central character gives a≡2r mod 5. For rank one, twist-one vanishing forces a≤0; for rank two, it forces a≤2. Neither interval contains the required congruence class. Rank zero is impossible for evaluation of a nonzero section space, so the generic rank is three.

5. **No divisorial defect.** The common divisorial part of the maximal minors has degree at most six and is N-invariant. Its defining line is a character, hence trivial; the center therefore forces its degree to be divisible by five. The only positive candidate is excluded by the quintic invariant calculation. At each codimension-one local ring, the maximal-minor criterion for surjectivity shows that the cokernel has no divisorial support. This excludes the whole divisorial defect, not just a selected invariant component.

6. **Reflexivity and semistability.** The evaluation kernel K is torsion-free and satisfies S₂ by the depth lemma applied to its torsion-free image quotient. Therefore it is reflexive. The absence of divisorial cokernel gives c₁K=−6H, so E=K(3) is rank two with c₁E=0 and trivial central action. If E were unstable, its unique maximal destabilizing saturated line subsheaf would inherit equivariance. It is reflexive, again by the depth lemma, and thus equals O(a). Positive slope gives a>0; its inclusion in 5O(3) gives a≤3; the central action gives 5|a. These conditions are incompatible. Uniqueness is used only in the unstable case.

7. **Bogomolov and the equality case.** The leading codimension-two Chern character of the cokernel is effective, say tH² with t≥0. Additivity and twisting give ch₂E=tH² and c₂E=−tH². Langer's Theorem 3.13 applies to this semistable torsion-free sheaf and forces t=0. Since every nonzero effective codimension-two cycle on P⁴ has positive degree, the cokernel is now supported in codimension at least three. Ou's Theorem 3.1 expressly applies to reflexive sheaves and concludes that E is a numerically flat vector bundle, including local freeness. All its numerical hypotheses are satisfied. The compatible flat connection supplied by Theorem 3.5, together with simple connectedness of P⁴, then gives E≅O² and K≅2O(−3).

8. **Final Chern-character contradiction.** The roots 0, α−β, β−α give ch₂B=−15H² and ch₃B=0. Hence ch₃B(2)=−26H³. The exact sequence and K≅2O(−3) give

       ch₃T=−26H³+2(−27/6)H³=−35H³.

   A coherent sheaf supported in codimension at least three has an effective leading codimension-three cycle, or zero if its support has higher codimension. Its degree cannot be negative. This contradiction eliminates the five-dimensional alternative.

The numbered sections, equation references, and final cohomology deduction are consistent. The proof makes no assertion about twists three or four, and does not infer a value for an evaluated matrix, section, or multiplication-map instance.

## Primary references checked

- [W. Decker, *Monads and cohomology modules of rank 2 vector bundles*](https://www.numdam.org/article/CM_1990__76_1-2_7_0.pdf), Compositio Mathematica 76 (1990), 7–17, especially printed pp. 15–16.
- [G. Horrocks and D. Mumford, *A rank 2 vector bundle on P⁴ with 15,000 symmetries*](https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf), Topology 12 (1973), 63–81, §2, Theorem 3.5, and §4.
- [A. Langer, *On boundedness of semistable sheaves*](https://ems.press/content/serial-article-files/26645), Documenta Mathematica 27 (2022), 1–16, Theorem 3.13.
- [W. Ou, *Foliations whose first Chern class is nef*](https://ems.press/content/serial-article-files/34043?nt=1), DOI 10.4171/JEMS/1426, Theorems 3.1 and 3.5.
