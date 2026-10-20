# Independent audit: ordinary formal deformation bases

Reviewed 2026-10-19. This is a bounded independent proof review, not a new theorem claim, an execution of the Ext certificate, or an external review submission.

## Verdict

No correction to PR17 was found. Given its cited exact tangent dimension and the genuine family constructed in PR3, the 87-variable ordinary hull and 83-variable determinant-trivial hull follow. The published statement correctly preserves stabilizers and excludes ambient-category and global coarse-moduli conclusions. The compressed phrase “versality supplies R → T” is valid; its compatible construction is supplied below.

The Ext dimensions are inputs to this audit, not independently recomputed results. No production imports, source/model/owner/jet evaluations, matrix products, or experiments were performed.

## Inspected sources and scope

- [PR17](https://github.com/Akilleez-QA/read-em-and-weep/pull/17), current head `55a89833a46c2b16d06e1123f8b35b82b6edaf51`: metadata, complete 36-line added-file patch, and discussion endpoint (no comments).
- [PR3](https://github.com/Akilleez-QA/read-em-and-weep/pull/3), current head `86251374e9c62528b9b9dbb35ef883bdfac30ad8`: actual added-file patch, family construction, the section/translation/Picard separation, fixed-determinant normalization, and relevant discussion. The source's 87-dimensional family theorem is conditional on no Ext dimension calculation; identifying its tangent with the entire Ext group additionally uses PR5.
- [Existing formal-local review](https://github.com/Akilleez-QA/read-em-and-weep/pull/3#issuecomment-6093574455) and subsequent audit `6093626348`. Both already contain the formal-ring implication and the cubic counterexample. These are existing results, not discoveries of this pass.
- [Talpo–Vistoli, Deformation theory from the point of view of fibered categories](https://arxiv.org/pdf/1006.0497), Proposition 6.36, printed p.72: directly states that a formal object over a power-series ring with isomorphic Kodaira–Spencer map is miniversal and unobstructed. Its proof uses Theorem 6.33 and Proposition 6.26, in agreement with PR17.

The review checks the formal consequence and relevant family assumptions; it does not redo the cited classical HM stabilizer literature or the independent exact Ext certification.

## Precise deformation problem

Work over local Artinian complex algebras A with residue field C. Keep the fourfold X fixed and consider locally free sheaves E_A on X × Spec A with an identification of the special fiber with E. Morphisms respect that identification. Write F for the functor of isomorphism classes, or retain the deformation groupoid when discussing automorphisms.

For the determinant version, also choose an identification det(E_A) ≅ O compatible with the chosen central determinant identification, and require morphisms to respect it. “Fixed determinant” without this convention can describe a different groupoid, even when the same local isomorphism-class base occurs.

The coherent-sheaf deformation category has the gluing property and finite-dimensional tangent Ext¹(E,E); the determinant-identified version has the same gluing property and trace-free tangent. It therefore has the required miniversal formal object. A hull is sufficient for the argument; a universal object or fine global moduli scheme is not required.

## Compatible construction of the classifying map

Let h_R → F be a hull: a formally smooth natural transformation inducing an isomorphism on tangent spaces. Let T = C[[t₁,…,tₙ]] be the completed local ring of the actual smooth family, and let ξ_j ∈ F(T_j), where T_j = T/m_T^(j+1), be its compatible restrictions.

Start with R → T_0 = C. Given φ_j: R → T_j classifying ξ_j, formal smoothness makes

    h_R(T_(j+1)) → h_R(T_j) ×_(F(T_j)) F(T_(j+1))

surjective. Thus choose φ_(j+1) above the pair (φ_j, ξ_(j+1)). The kernel m_T^(j+1)/m_T^(j+2) is annihilated by the maximal ideal, so each transition is a small extension. The homomorphisms are compatible by construction. Their inverse limit gives a continuous local homomorphism φ: R → T. In the groupoid formulation, lift the comparison isomorphisms as part of this same induction; there is no need to assume a representing scheme.

By naturality, the tangent map T_T → T_R → T_F is the family's Kodaira–Spencer map. The second arrow is an isomorphism by the hull property; the composite is an isomorphism by the reviewed family and dimension input. Hence φ induces a cotangent-space isomorphism.

Choose a minimal continuous surjection P = C[[x₁,…,xₙ]] → R, with kernel I ⊂ m_P². The composite P → R → T sends the variables to formal series with an invertible linear coefficient matrix. Successive correction in each total degree constructs a unique inverse formal substitution. Thus P → T is an isomorphism. Since I lies in its kernel, I = 0, and R ≅ P. In fact φ is then an isomorphism as well.

The formally smooth hull map now shows that every deformation lifts across every Artinian small extension: first classify it via the hull, then lift its ring map out of the power-series ring. This is ordinary formal unobstructedness to all orders, not just the existence of a separate arc for each tangent vector.

## Why the 83-dimensional family is genuinely determinant-identified

PR3 works locally on the 79-dimensional open parameter space of ordered sections modulo common scalar, trivializing its tautological line. Accordingly the universal morphism satisfies f_s*O(1) ≅ L as a family-wide identification. Because det H ≅ O(-1) and N² = L, the family f_s*H ⊗ N has trivial determinant, with an identification on the whole parameter neighborhood. Pulling that identification back by the translation map gives one for the section/translation family. A constant scalar adjustment matches the chosen central identification.

Thus the 83-dimensional family exists in the correct determinant-identified deformation problem; a pointwise claim about determinants would not have sufficed. Picard twists are deliberately omitted: for them the determinant is M².

In characteristic zero, the sheaf trace splits via a ↦ (a/2) id_E. Therefore

    Ext¹(E,E) = H¹(End₀ E) ⊕ H¹(O_X).

Here h¹(O_X) = 4, and the input h¹(End E) = 87 gives h¹(End₀ E) = 83. PR3's section/translation directions are trace-free and independent. Its Picard directions have trace 2λ. Consequently the 83-dimensional subfamily's tangent equals the entire trace-free tangent, and the same hull proof applies.

The existence of a determinant identification has no additional tangent parameter here: differences of such identifications near the central fiber can be absorbed by scalar automorphisms, since taking a square root in 1 + m_A is unique over C. This is also why the characteristic assumption matters.

## Simplicity and stabilizers

Simplicity is not needed for the power-series-hull lemma. It is relevant to PR17's stronger automorphism description. Assume its input H⁰(End E) = C. Induct along a small extension A → B with kernel J. For an endomorphism of E_A, its reduction is scalar by induction. Subtract any lift of that scalar. The remainder belongs to

    H⁰(End E ⊗_C J) = J,

which consists of scalars. The scalar map A → End(E_A) is injective because E_A is locally free of positive rank. This proves End(E_A) = A, without assuming an arbitrary endomorphism lifts across A → B.

Ordinary automorphisms are therefore A×. Those respecting the central framing are 1 + m_A and still need not be trivial. With determinant identification, they satisfy c² = 1. If c ≡ 1 modulo m_A, then c + 1 is a unit, so (c − 1)(c + 1) = 0 implies c = 1. Without central framing the geometric stabilizers are G_m and μ₂, respectively, exactly as PR17 says.

Nontrivial automorphisms prevent identification of the entire ordinary groupoid with a discrete formal scheme. They do not, by themselves, prevent prorepresentability of its isomorphism-class functor: scalar automorphisms lift across Artinian surjections. PR17 correctly makes only the miniversal-base claim and does not rely on a false inference of non-prorepresentability from scalars.

No global coarse-moduli identification, algebraization theorem, or statement about changing X follows from this local proof. In particular Ext² need not be zero, and neither the associative Ext product nor ambient-category obstruction is shown to vanish.

## Diagnostic counterexamples and a necessary nuance

1. **Existing cubic example, made explicit.** R₀ = C[[x]]/(x³) has a one-dimensional tangent and no quadratic relation. The class x ↦ ε defines a deformation over C[ε]/(ε³). Every putative lift to C[ε]/(ε⁴) has x ↦ ε + aε² + bε³; its cube is ε³ ≠ 0. Thus quadratic obstruction vanishing does not prove all-order smoothness. The abstract identity between its tangent and that of C[[t]] cannot come from a tangent-isomorphic family over C[[t]]: any ring map R₀ → C[[t]] sends the nilpotent x to zero. This illustration already appears in the cited public review and PR17.

2. **Wrong coarse target hides obstructions.** Let Z = Spec C[x]/(x²), with G_m acting by weight one on x. Its invariant ring is C, so its affine categorical quotient is a smooth point. Yet the object x = ε over A = C[ε]/(ε²) of [Z/G_m] cannot lift to B = C[ε]/(ε³). G_m-torsors over these local Artinian rings are trivial; a candidate lift, even after changing its A-trivialization by a unit, has nonzero linear coefficient in ε, and its square is nonzero in B. Hence the stack has an obstructed deformation although the coarse quotient has zero tangent and is smooth. A tangent-isomorphic family for that coarse point says nothing about the omitted stack deformation. This is a synthetic diagnostic, not a counterexample to PR17, whose target is correct.

3. **Do not overstate the tangent warning.** Surjectivity of the Kodaira–Spencer map from a *genuine smooth formal family into the correct deformation problem* already suffices for unobstructedness when a finite-dimensional hull exists. Choose a formal smooth slice of dimension dim T_F on which the tangent map becomes an isomorphism, then apply the proof above. What fails is a merely abstract surjective tangent linear map, a finite-order family, or parameter counting without the correct family map. Also, equality of actual Krull dimension and embedding dimension for a Noetherian local ring would itself imply regularity; the warning concerns counts of a proposed parameter space, not that valid regular-local criterion.

## Disposition

Keep PR17's statement. An optional expository expansion could replace “Versality supplies R → T” with the compatible small-extension construction above, but no mathematical correction or additional external comment is warranted by this audit. No numerical or novelty claim was added.
