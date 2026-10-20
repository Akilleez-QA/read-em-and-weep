# Historical mathematical audit receipt

This is a preserved review of the source mathematical manuscript, not a fresh review of the publication bytes. Hashes quoted below identify the historical source versions. See [hm-generic-restrictions-PUBLICATION-CHECK.md](../hm-generic-restrictions-PUBLICATION-CHECK.md) for the final-publication review.

# Independent audit: generic restriction unobstructedness

## Verdict

**Pass, with the explicitly imported classical HM and restriction-cohomology inputs.** The proof establishes actual formal unobstructedness, not merely a tangent-space count. For each fixed smooth quintic off the determinant quadric, the completed group family is miniversal of dimension 24 for ordinary bundle deformations and for fixed-determinant deformations. The ambient HM bundle has the analogous conclusion. Nonzero Ext² groups remain compatible with this result.

This audit checked the intrinsic wedge stabilizer, infinitesimal base change, the full small-extension induction, determinant identifications and scalar inertia, and the passage to algebraic stacks. The clarification about lifting near the identity from PGL₅ to SL₅ correctly avoids an unjustified global PGL₅-linearization of O(3). No remaining mathematical correction is required.

Audited PROOF.md SHA-256: `261c57bde9ce8bad8b04e511a08dc3eae40d4746c34592e4195979f4d64ef21f`.

## 1. Dependencies and primary-source checks

I read the restriction proof and NONZERO-COROLLARY, and the scalar-propagation audit. The on-disk scalar-propagation proof hash is `35a93234687c5d79533f8fc55a7589b3cae6546e683dd3e4c192adbbc3d89c4c`, matching its recorded independent audit. Thus the restriction input is the actual nonzero branch, not a conditional assumption that the scalar might vanish. Off Q, the restriction long exact sequence gives an isomorphism H¹B → H¹(B|X); both sides have dimension 24. Simplicity, the scalar H¹/H² vanishings, and the stated Ext² dimensions are supplied by that dependency.

I checked the [Horrocks–Mumford primary paper](https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf): printed p.66 establishes irreducibility of the trace-zero endomorphism representation under the normalizer; §2 gives the equivariant construction; printed pp.73–74 give the needed section vanishing and four-dimensional section space. The historical bundle is the present F(3). The numerical h¹End F=24 remains an imported theorem with its separately verified Decker–Schreyer provenance in ../hm_primary_source_verification.md; it is not re-proved here.

## 2. Intrinsic wedge image and finite stabilizer

The wedge image W is independent of a choice of determinant isomorphism because any two such isomorphisms differ by a nonzero scalar. Its dimension bound is simply dim Λ²C⁴=6.

The proof that W is nonzero is sound. If all wedges vanish, the evaluation image has generic rank one, since some section is nonzero. Saturation L has torsion-free quotient in the locally free G. At every local ring of dimension at least two, the depth lemma gives depth L at least two: the quotient has depth at least one, and G has full depth. Together with torsion-freeness, this makes L reflexive. A rank-one reflexive sheaf on smooth projective space is invertible, so L=O(a). All four sections factor through L, and the three cases a<0, a=0, a>0 yield exactly the contradictions stated. No assertion that arbitrary torsion-free rank-one sheaves are invertible is being used.

The degree-five representation descends from SL₅ to PGL₅ because the central μ₅ acts trivially. The Grassmannian stabilizer K of W is a genuine closed finite-type subgroup. Containment of the finite normalizer makes Lie K an invariant subspace of the irreducible adjoint representation. If Lie K were all sl₅, characteristic-zero smoothness of algebraic groups and connectedness of PGL₅ would force K=PGL₅. That contradicts irreducibility of Sym⁵(V*) and the strict dimension bounds on W. Hence Lie K=0 and K is finite. The bundle stabilizer is contained in K by intrinsic functoriality. Crucially, this proves finiteness of the full stabilizer; the presence of a known finite subgroup alone would not do so.

## 3. Infinitesimal orbit and section base change

Set-theoretic finiteness alone is not used to establish KS injectivity. A zero KS class gives an actual trivialization of the dual-number deformation, respecting the chosen special-fiber marking after adjustment. The dual-number group element lifts uniquely near identity to SL₅, which supplies the required identification of the pullback O(3) with O(3).

For the pullback of G, the associated automorphism of the product is an automorphism over the Artinian parameter base. Its pushforward of sections therefore agrees with the constant family. Constant-family cohomology is H⁰G tensored with the base, so the section module and its wedge image commute with this base change. The wedge image is consequently the translate of W as a direct-summand submodule. Under the bundle trivialization it is the constant W, up to a unit on the determinant line; H⁰(O) over the base consists of base scalars. Thus the first-order group element lies in the scheme-theoretic stabilizer K, forcing its tangent vector to vanish.

This gives a KS isomorphism because both dimensions are 24. Restricting the family to the original fixed X gives the composite with H¹B → H¹(B|X), so the restriction KS map is also an isomorphism. No preservation of X by the group element is necessary.

## 4. Small-extension induction and minimality

The induction uses more than matching dimensions. For a small extension with kernel I annihilated by the maximal ideal, two lifts of the same deformation, with specified identification over the quotient, differ by a class in Ext¹(E₀,E₀)⊗I. The fixed identification is essential: it is the category of identified lifts whose isomorphism classes carry the lift-difference torsor. The proof supplies precisely that identification by its induction hypothesis.

Smoothness of the parameter scheme provides one lift. Changing the parameter lift is a derivation with values in I, hence an element of T_tT⊗I; the resulting difference class is KS⊗I. Surjectivity cancels any difference. Repeating this argument with a prescribed lower parameter proves smoothness of the map of deformation functors, rather than mere objectwise surjectivity. Representing an arbitrary deformation and lifting its parameter then proves unobstructedness across every small extension. General Artinian surjections factor into these.

The [Stacks lift-difference lemma 91.4.3](https://stacks.math.columbia.edu/tag/08L7) supports the torsor assertion, with flatness as in its deformation-theory applications. The transition-function calculation in the proof is also a sufficient direct verification for vector bundles. The tangent isomorphism makes this versal family minimal. The power-series-ring cross-check is valid: a continuous endomorphism of a formal power-series ring with invertible linear term is an automorphism, forcing the minimal hull's defining ideal to vanish.

## 5. Determinants and inertia

The H¹O and H²O vanishings ensure that determinant deformations have one isomorphism class, and an identification can be chosen compatibly with the special fiber. Two choices differ by a base unit. A unit congruent to one has a unique square root congruent to one in an Artinian C-algebra, so a scalar bundle automorphism corrects that difference. This proves equivalence of the relevant deformation parameter spaces; it does not assert equality of the automorphism groupoids.

Simplicity persists in the needed formal sense: induction on small extensions shows every endomorphism of an Artinian deformation is scalar. Indeed subtract a scalar lifting its scalar reduction; the remainder lies in H⁰End(E₀)⊗I=I. Thus automorphisms are base units, determinant-preserving automorphisms are their square-one subgroup, and a determinant-preserving automorphism reducing to identity is trivial. This justifies all inertia statements, including μ₂ for the unmarked fixed-determinant stack and G_m for the unrestricted stack.

Replacing PGL₅ with SL₅ for an actual determinant-identified algebraic family is correct. The standard linearization of O(−1) identifies determinants, and the finite étale central quotient induces an isomorphism on identity completions. The miniversal dimension is 24 in both problems. The unrestricted stack dimension is 24−1=23; the determinant-identified stack dimension is 24 because its inertia is finite.

## 6. Algebraic meaning and scope

For these fixed projective varieties, bundles form an open substack of the algebraic coherent-sheaf stack. The [Stacks coherent-sheaf discussion](https://stacks.math.columbia.edu/tag/08KA) and [Lemma 108.4.2](https://stacks.math.columbia.edu/tag/0DLX) supply algebraicity and local finite presentation. The precise upgrade from unobstructed deformation category to smoothness at the point is [Lemma 107.2.7](https://stacks.math.columbia.edu/tag/0DQT); Lemma 107.2.6 there also upgrades the algebraic versal family to a smooth morphism after shrinking near identity. Thus the proof's stack-smoothness assertion is justified and need not be weakened to a purely formal statement.

The local rigidified simple-bundle parameter space has the same smooth 24-dimensional germ. Neither stability of the restriction nor a global GIT coarse moduli construction is needed. The stable ambient case may use its usual coarse moduli space. The proof correctly distinguishes algebraicity of the miniversal family from algebraicity or convergence of every formal arc.

At Q=0 the group directions are still independent, but are no longer tangent-complete, so this proof yields no unobstructedness claim there. The conclusion concerns all ordinary commutative-base bundle obstructions, not every ordered Yoneda or Massey expression, dg-algebra formality, or a mixed/source-constrained problem.

## Scope of this audit

Only static proof reads, abstract deformation and representation arguments, primary-source web reads, and this local audit write were performed. No selected source/cofactor/HM matrix, numerical rank, polynomial instance, or coefficient evaluation was performed; no external service was modified and no user-computer task was created.

## Additional audit: JUMP-STRATA.md

**Pass.** For every smooth quintic the restriction sequence preserves the injection of the 24 orbit tangent directions. A compatible classifying map from the minimal hull into the orbit power-series ring exists by the hull lifting property, successively modulo powers of the maximal ideal. It need not be unique. The tangent injection makes the induced cotangent map surjective. Selecting 24 elements whose images have independent linear terms and applying the formal inverse-function theorem supplies target coordinates and proves surjectivity of the ring map. Completing these elements to source coordinates is possible because their cotangent classes are independent. Replacing each remaining coordinate by itself minus its target-image power series then puts the map in projection form. Consequently its kernel is exactly the ideal generated by the transverse coordinates, and the defining hull ideal is contained in that ideal and in the square of the maximal ideal.

This proves the claimed closed embedded smooth 24-dimensional formal subgerm and Krull-dimension lower bound. It does not imply that the embedding splits as a product, that all equations depend only on transverse variables, that there are at most r equations, or that a jump-stratum point is singular. The complement correctly states all of these limits. This is an abstract formal-coordinate argument, with no selected polynomial or matrix evaluated.

Audited JUMP-STRATA.md SHA-256: `dd698b95c1cdec3d1b01824785ce06beaac93c90667a2a03f34c852a3003cdca`.
