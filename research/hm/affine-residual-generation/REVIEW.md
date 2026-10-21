# Independent review: actual global generation from the twelve pentagons

Reviewed `hm-affine-residual-system/ACTUAL-GLOBAL-GENERATION.md` on 2026-10-21. Verdict: the proof is correct, provided its separately stated exact primary-surface dictionary is established. This review does not independently establish that dictionary. The proof removes the global-generation hypothesis once that dependency is available.

## Source and geometric inputs

The cited Barth–Hulek–Moore chapter, §§4.2–4.3, explicitly supplies a smooth modular elliptic surface over P1, twelve I5 fibers, 25 disjoint torsion sections, five sections meeting each pentagon component in distinct points, component self-intersection -2, fiberwise torsion translations, and the compatible SL2(F5) action. I checked those passages in the chapter text. The additional exact identification of this surface as the normalization of the primary S, with the correct line labels and pullbacks H=I+2F and C=5I, is an essential independent dependency. Merely knowing an abstractly isomorphic or Galois-related configuration would not suffice.

## Directions and multiplicities

The torsion group G acts on the five-cycle dual graph through D10. Its odd-order image is trivial or C5. Transitivity on the 25 sections, together with five nonempty equal component-incidence classes, forces transitivity on components, ruling out the trivial image. The kernel therefore has order five. For a fixed component its five section labels are exactly one coset of this kernel: the action on section labels is regular and the kernel is the component stabilizer.

The assignment from the twelve singular fibers to six directions is SL2(F5)-equivariant. Transitivity of that group on directions forces all fibers of the assignment to have equal cardinality, namely two. No faithfulness of its action on the twelve fibers is required.

Since M=10F, every effective R_A has zero intersection with F and is vertical. For a pentagon component E, C.E=5 implies I.E=1, hence H.E=1. In the two pentagons of A's direction, all five sections indexed by A meet one component. In every other pentagon, the affine line A meets each incidence coset once. This establishes exactly the two asserted intersection patterns.

For the matching pentagons the cycle intersection equations are solved by (3,1,0,0,1), centered at the distinguished component. Direct substitution gives (-4,1,1,1,1). The cycle Laplacian has one-dimensional kernel consisting of constants, so every integer solution differs by an integer full-fiber multiple. Effectivity forces that integer to be nonnegative. The minimal contribution has H-degree five and self-intersection -10.

The two required minimal contributions have total degree ten, which is already H.R_A=15-5. Every other possible vertical component has strictly positive H-degree: one for a pentagon component and five for a smooth fiber. Thus no additional component or whole-fiber summand is possible. This also excludes any issue of hidden effective contributions; the model here is the smooth modular surface itself, not a further resolution containing unspecified exceptional curves of H-degree zero.

## Section divisors and descent

As the five cosets vary, the distinguished component cycles through all five components in each associated pentagon. Summing the five multiplicity vectors gives coefficient five on every component. Therefore div(nu^*s_U)=5(F_U^+ + F_U^-).

The six pairs partition the twelve distinct fibers. Two residual sections for different directions already have disjoint zero loci upstairs; in particular the six have no common zero. This is stronger than merely having zero common divisorial part.

The descent argument is valid even when S is nonnormal. For an invertible sheaf, the value of a section in a residue-field fiber is zero if and only if its value after any field extension is zero. Pullback to a point over x therefore detects vanishing at x. Surjectivity of normalization excludes any basepoint downstairs. Equivalently, the common zero subscheme is empty upstairs and hence has empty support downstairs.

## Boundaries

This is an independently reviewed proof, not a formal proof-assistant check. It uses no selected actual HM/source evaluation. It proves global generation of the actual residual sections only with the exact primary dictionary included. It does not by itself prove that the elliptic fibration descends through the nonnormal identifications, establish independence of the six restricted sections or resolve unrelated higher-order/algebraicity questions. Those limitations in the author's final section are appropriate.

## Addendum: degree-ten image

I also reviewed the added image-degree argument in §4. The normalizer-stable system induces an equivariant finite map from the elliptic base P1 to the normalization of the image. The chosen torsion section is preserved by its binary stabilizer and maps isomorphically to the elliptic base, transporting the established faithful projective A5 action to that base. Thus the ramification divisor is A5-invariant there. Its degree is 2e-2, where e times the image degree equals ten. Orbit sizes 12,20,30,60 exclude e=2,5,10, so e=1 and the image degree is ten. This argument is correct and does not require independence of the restricted six sections.

## Final dependency and construction audit

Re-reviewed the publication version of ACTUAL-GLOBAL-GENERATION.md with SHA256 `33b1dc22da535032ef0ba7eb32dea1e3cbbf431957a5a4eee3a486e3ab4727f5`. It now explicitly pins the exact identification to PR570 commit `e5e55594ef2b99cefb81c4c02b22cb45e1ff0025`, and the Schrödinger dictionary to PR562 commit `86b643fe2adecbd321d1c8f98be84fe2082bcd10`. The identification remains a cited dependency, not something independently re-proved in this review.

The added projective-group compatibility argument is valid. In the specified Schrödinger coordinate basis, a primitive Galois transform changes the diagonal generator to a primitive power while keeping the cyclic permutation unchanged. These generate the same projective subgroup. Passing to a dual convention also preserves that subgroup. I checked the explicit cyclic-permutation and diagonal formulas in BHM §3.1 and the module/dictionary statements in the PR562 proof. Consequently the coordinate-copy identification is compatible with the translation subgroup; affine changes of torsor labels preserve precisely the blocks and parallel classes used here. No identification of incompatible linear central characters is needed.

The new construction of all thirty hyperplanes and six sections is correct. Uniqueness of the spanning hyperplane for a cyclic block makes its translate independent of the coset representative. Since S spans P4, its hyperplane section is a nonzero effective Cartier divisor. Near each distinguished line S is smooth and the line is Cartier, so subtracting the contained disjoint lines is effective Cartier; away from them subtraction changes nothing. Multiplying the five hyperplane sections and dividing by the canonical section of C therefore produces the asserted nonzero section of 5H-C. This supplies the actual sections without requiring the separate ambient-independence lemma. The publication additions introduce no new gap.
