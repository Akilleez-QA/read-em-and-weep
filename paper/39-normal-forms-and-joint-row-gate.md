# Negative-pencil normal forms and a joint-row determinant gate

**Historical checkpoint superseded in part by PR959.** The rank-zero Type I 36→32 alternative recorded below is no longer live: the joint P row is now proved nonzero. Under hypothetical full-radical Q compatibility, only rank one and the 32→28 annihilator reduction remain. The original checkpoint is retained for provenance; see [chapter40](40-conditional-reductions-and-finite-neighborhood.md).

**Craig Ward · 23 October 2026 · Update through PR954**

The new deductions refine the remaining multiplication problems without removing another source-dual pair. **Four necessary pairs remain across three stable labels.** No actual source realization or complete repair is claimed.

## Regular source2 quotients have one fixed negative-pencil type

[PR953](https://github.com/Akilleez-QA/read-em-and-weep/blob/9c12c02a601cc380e2e2cf233e7b37dddd46d563/research/hm/source2-radical-quotient-normal-form/PROOF.md) takes any nonzero radical element j that is neither pure V nor the unique exceptional mixed direction. For every balanced endpoint and both residual coupling classes, its actual vertexwise image I gives a fixed-variable G-equivariant pencil isomorphism

    N/I ≅ N0 ⊕ N8 ⊕ (V+D)[2].

The final summand has V+D only at vertex two; its later spaces and arrows are zero. The quotient dimensions are **(32,36,28)**. N0 and N8 are the complete first block and degree-eight core, not placeholders for matching characters.

The proof uses the embedded endpoint pencil NC. The regular image equals NC at vertices three and four, leaving NC/I=(V+D)[2]. In the genuine quotient sequence

    0 → (V+D)[2] → NR/I → N8 → 0,

the maps at vertices three and four are isomorphisms. An equivariant section at vertex two, together with their inverses, necessarily commutes with every original pencil arrow. This proves an arrow-level splitting without splitting the original residual bundle or claiming a canonical section.

**Q-compatibility is not needed for this normal form.** If j is additionally Q-compatible, the normal form identifies the negative-arrow system underneath PR950's 32-to-28 obstruction quotient. It does not force the induced Q to preserve these summands: off-diagonal mixing remains. Nor does the theorem assert a compatible j exists.

The exceptional mixed direction leaves a six-dimensional T at vertex three, so the section argument does not apply. Pure V is also outside this theorem. Both remain possible conditional directions; neither is excluded. The package's independent review and 745 checks in ordinary and optimized modes support the proof over its pinned inputs. No actual endpoint or slope is evaluated.

## Type I source126 has a conditional joint P-row gate

[PR954](https://github.com/Akilleez-QA/read-em-and-weep/blob/1dfd8f6b2b7d39d41de2619737b6cf4cfb951e75/research/hm/source126-typeI-joint-annihilator/PROOF.md) assumes an actual Type I source126 and asks what follows if **every element of its two-dimensional radical J is Q-compatible**. Define the joint map

    R_P : J → Hom_G(2P,P).

Both sides are two-dimensional. The rank r and determinant-vanishing condition are intrinsic under basis changes; no actual row matrix is selected or evaluated. The theorem proves **r ≤ 1**, and its exact common-annihilator subpencil has only the following footprints:

| Joint P-row rank | U = Ann_J N2 | Z = Ann_J N4 | Endpoint dimensions | Acyclic quotient endpoints |
|---|---|---|---|---|
| r=1 | A+2V+2P+3D | 2V+3P+2D | 32→28 | P+D → P+D |
| r=0 | A+2V+3P+3D | 2V+4P+2D | 36→32 | D → D |

In each row Q restricted to U has kernel A+D and cokernel P. The quotient Q is invertible, not merely between spaces of equal character. Consequently the inclusion of the annihilator subcomplex in Q+tT_a is a filtered chain-homotopy equivalence over C[[t]]. The acyclic **quotient** is removed; the annihilator subcomplex is retained. The actual successive t-adic Bocksteins of this specified two-term family are preserved.

The argument first proves that the joint D action cannot vanish, using the genuine coefficient span and natural Serre-duality action. It does not infer common rank from separate individual ranks. Character comparison then lists the possible annihilator footprints. If r=2, the annihilator restriction would be Q-surjective and contain the actual A kernel, contradicting the same nonzero second-Bockstein theorem by the exact first-correction comparison. A second surjective possibility at r=1 is excluded similarly.

The two surviving rows have a nonzero cokernel P, so that contradiction does not eliminate them. Invertibility of the complementary quotient follows instead from Q's P-injectivity and D-surjectivity. The displayed formal contraction proves the filtration statement without introducing negative powers of t.

The independent review records 11,872 supporting checks in both Python modes, including nine immutable inputs and a negative control against confusing individual rank-one rows with joint rank two. The theorem **does not** establish det R_P≠0 on the actual balanced locus, prove dim J_Q≤1 in Type I, or exclude full-J compatibility. Types II and III cannot inherit this gate. No pair count changes.

## Collaborator source report on the opposite bundle and vertex extension

The complete immutable proof texts of [PR948](https://github.com/Akilleez-QA/read-em-and-weep/blob/d1d5ca5915b734d018665c2b02a4426c8225d799/research/hm/opposite-bundle-classification/PROOF.md) and [PR952](https://github.com/Akilleez-QA/read-em-and-weep/blob/13d0e53e0a64ec6935a2ca83af776942e201c4e9/research/hm/exceptional-polar-obstruction/PROOF.md) were fetched and read for this update. The following reports their stated deductions and limitations. It is not an independent reproof of their geometry or exhaustive enumerations, and their recorded reviews are not proof-assistant certification.

PR948 uses the torsion-free rank-five degree-26 opposite bundle C and its complete-evaluation characters to prove

    dim Ext¹_G(C,O(10)) ≤ 1.

It lists exactly twenty-one abstract bundle types satisfying that interface. Sixteen force equivariant splitting of the vertex extension; five admit a one-dimensional extension space with explicit split and nonsplit middle-bundle possibilities. All twenty-one have abstract fiberwise-injective pencils with the required characters. Thus those interface data alone do not select the actual bundle row or extension class. This is a separate abstract classification, **not twenty-one additions to the four-pair ledger**.

For an extension-capable row, splitting is decided by the actual invariant lifting functional

    δ : H0(C(-12))^G → H1(O(-2))^G = C.

The twist is on the parameter line, not a physical normal-order statement.

PR952 constructs an actual canonical nonzero map σ between two-dimensional invariant spaces, using the exceptional-polar filtration. Its kernel is H0(C(-12))^G, so its rank is **one or two**, not yet selected. Rank two would exclude all five extension-capable types; rank one leaves a candidate line on which δ decides the extension. Lower actual transgressions α and β satisfy rank α + rank β = 1, without selecting which is nonzero. The filtration is retained as exact sequences rather than replaced by a direct sum.

The vertex functional is identified with a Leray differential, equivalently the dual of a codimension-three vertex Gysin map. The source does not prove that scalar is nonzero, select the actual σ rank, or determine the actual PR948 row. These statements narrow the geometric target but do not establish source realization, full mixed-map solvability or algebraicity.

## Unchanged frontier and remaining work

The [four-pair ledger](https://github.com/Akilleez-QA/read-em-and-weep/blob/3cd8a620e7268cf86fb8cc019d35f04d3cb6b448/research/proof-repair-campaign/four-pair-composition/README.md) and all historical figures remain unchanged. Source2's compatible line, if any, is still unselected; its induced Q can mix the regular quotient summands. Type I source126's determinant gate still needs actual geometric information to exclude the surviving rows. The opposite-bundle row and vertex scalar remain undetermined. None of these unresolved branches supplies a justified total-completion estimate.
