# Independent audit of conditional invariant formal smoothness

## Verdict and bound documents

**Pass, conditional on the separately stated inputs P and D. No mathematical correction is required.** The completed coefficient family is a miniversal family for the precisely defined marked, deck-equivariant ordinary bundle deformation groupoid. The argument does not require simplicity, a fine moduli space, or disappearance of automorphisms.

This audit binds these SHA-256 digests:

    INVARIANT-FORMAL-SMOOTHNESS.md: 945e7982a0d10870d896a0ec4004408ce7beb2d7b16664c7a696c506eb296e46
    FULL-COEFFICIENT-FAMILY.md: 7d0b36952133976e30a039538238b56cd0e80455d67f2f49e34c113276efdf6e
    FULL-COEFFICIENT-FAMILY-AUDIT.md: ef28e10647b00c47db779e06fcb2e3b67a4e0242b7760c156bea891934af86b3

All three documents were read in full. The beginning of the bundled historical Ext document was inspected only to identify the provenance and deck-character meaning of D; its calculations and certificates were not rerun or independently certified. The substantive mathematical audit below is a structural proof audit, not a numerical verification of D or of the historical exactness premise A contained in P.

## 1. The groupoid and its tangent space

The definition fixes X, its deck action, a particular linearization on E, and a special-fiber identification. Morphisms must respect that identification but need not be the identity over the whole Artinian base. This is the appropriate marked deformation groupoid, not a fixed-point set in coarse moduli. Its fiber over k is equivalent to the terminal groupoid: the marking determines the unique compatible special-fiber isomorphism. That fact is compatible with nontrivial automorphisms over larger Artinian rings.

Equivariant first-order extensions identify its tangent space with Ext¹_G(E,E). Since the group is finite and its order is invertible in k, averaging is exact; equivariant Ext therefore identifies with the invariant part of ordinary Ext. Local freeness reduces ordinary Ext to cohomology of End E, and properness makes these groups finite-dimensional. These statements neither assume nor reproduce any historical rank result.

## 2. The geometric family and the two distinct premises

The actual universal map factors through the deck quotient on X. Pullback of H consequently has its canonical deck linearization, and the fixed origin-divisor linearization on N supplies the required linearization of the tensor product family. This works for the entire family and its completion, not merely for its tangent vectors. The family at the base point has the stipulated linearization and marking.

P supplies the actual smooth 79-dimensional parameter space and ordinary Kodaira–Spencer injection. The equivariant tangent map forgets to that injection, so it is also injective. D, and only D, supplies equality of dimensions with the invariant tangent space. Together they make the equivariant Kodaira–Spencer map an isomorphism. No inference from the exact-presentation premise alone establishes D. Twisting the fixed linearization by a character does not change the conjugation action on End E, but the theorem correctly specifies one linearized object rather than varying its equivariant structure silently.

## 3. Patching and the groupoid hull

For an Artinian fiber product with one map surjective, tensoring with any affine coordinate ring of X preserves the fiber-product diagram: all rings involved are k-vector spaces and tensoring over k is exact. Finite-projective patching therefore applies to the rings of the corresponding affine thickenings. On a small enough affine neighborhood where the special-fiber bundle is free, a basis lifts over a nilpotent thickening and remains a basis. A change-of-basis matrix over the common quotient lifts to an invertible matrix across the surjection. This proves the claimed local freeness of the patched module.

The construction is fully faithful on morphisms and compatible with restriction. Thus the local objects glue, the linearization maps glue, and their group-law identities hold by faithful restriction to the two factors. The marking glues as well. This establishes the groupoid equivalence required by Rim–Schlessinger, including the specified identification over the common quotient.

The finite-projective patching mechanism is exactly the one cited in [Stacks, Lemma 93.4.2](https://stacks.math.columbia.edu/tag/0DVP). The relevant existence result is genuinely groupoid-valued: [Stacks, Theorem 90.15.5 and Remarks 90.15.6–7](https://stacks.math.columbia.edu/tag/06IL) give a minimal versal formal object with tangent isomorphism and the resulting isomorphism-class hull. Here the base coefficient ring and residue field are both k, so the separability qualification causes no problem. No algebraic closure or simplicity assumption is needed.

This distinction matters: merely knowing that a set-valued hull exists would not, without further argument, establish that previously chosen bundle isomorphisms lift. The audited proof invokes the stronger groupoid formal object, which does give the required compatibility.

## 4. The map from the hull and elimination of relations

Write S for the completed parameter ring. Its Artinian quotients have small successive kernels, annihilated by the maximal ideal. Formal versality of the groupoid object over R gives compatible maps R to these quotients and compatible isomorphisms to the geometric family. Their inverse limits define R→S and an isomorphism of formal objects. The direction of the ring homomorphism is correct; it is not S→R.

The tangent triangle identifies the derivative of this map with an isomorphism, since both family and hull have the same tangent space. Dualizing gives the cotangent isomorphism. A minimal power-series presentation P→R then has 79 generators and no linear relations. The composite P→R→S has an invertible linear part and is a formal coordinate isomorphism. Every relation in the kernel of P→R is killed by this injective composite, so that kernel vanishes. This excludes all higher-order relations, including nilpotent or embedded ones, without any calculation in the original geometric model.

Transport of the versal object along R≅S proves miniversality of this particular completed family, not merely existence of some abstract smooth hull.

## 5. Independent direct small-extension proof

There is a second proof of formal smoothness of the coefficient-family transformation that does not begin with hull existence.

Let A→B be a small extension with kernel I and m_A I=0. Fix a parameter map t_B:S→B, an equivariant bundle D_A over A, and a specified equivariant isomorphism between D_A restricted to B and the family at t_B. Choose arbitrary lifts in m_A of the 79 parameter values. They define t_A⁰:S→A lifting exactly t_B, because S is a power-series ring. The family at t_A⁰ and D_A are now two existing lifts of the same B-object, each equipped with the fixed reduction identification.

The isomorphism classes of such lifts **with their B-identifications retained**, and with morphisms inducing the identity on that B-object, form a torsor under

    Ext¹_G(E,E) ⊗_k I = Ext¹_X(E,E)^G ⊗_k I.

One can see this by choosing local trivializations and comparing lifted transition maps and linearization maps. Their differences lie in End(E)⊗I; products of two differences vanish. The compatibility equations are additive cocycle equations, and changes of local gauges give coboundaries. A cover closed under the finite group action, together with the group-cochain differential, computes the equivariant version. Averaging removes higher group-cohomology contributions and leaves invariant sheaf cohomology. Equivalently, this is the usual square-zero deformation comparison for vector bundles in the equivariant category.

The identification with the *special-fiber* End E is legitimate because m_A kills I. The torsor assertion concerns two existing lifts and does not assume that arbitrary B-objects are unobstructed. Infinitesimal automorphisms of any lift inducing identity on B form Ext⁰_G(E,E)⊗I. They may be nonzero, but do not prevent the torsor statement for isomorphism classes with fixed reduction identification. Forgetting those identifications too early would lose precisely the compatibility needed here.

The set of parameter lifts of t_B is a torsor under T_u U⊗I. Changing t_A⁰ by a parameter difference changes the bundle-lift class by the Kodaira–Spencer map tensored with I. This is its derivative at the closed point: all higher coefficients multiplying I vanish because m_A I=0. Since that derivative is an isomorphism under P and D, choose a parameter difference that cancels the discrepancy with D_A. The resulting parameter map still restricts to t_B, and equality of the fixed-reduction lift classes supplies an equivariant isomorphism extending the prescribed B-isomorphism.

This is exactly groupoid formal smoothness. General Artinian surjections factor into small extensions, so iteration proves the full lifting statement. The tangent isomorphism then makes the family miniversal and its isomorphism-class transformation a hull. This independently confirms the conclusion reached by the ring argument.

## 6. Meaning and limits of the conclusion

The result gives existence of classifying maps and compatible lifts of maps and isomorphisms. It does not assert uniqueness. Scalar automorphisms reducing to identity already preclude identifying the whole marked groupoid with a discrete parameter functor. Their existence alone does not disprove prorepresentability of the isomorphism-class functor, as the audited text correctly warns.

Smoothness implies that invariant tangent classes have compatible ordinary lifts and hence their quadratic Yoneda obstruction vanishes. Polarization gives vanishing of a∘b+b∘a, not of each ordered product separately. No vanishing of the entire Ext² invariant space, no associative higher-product table, and no general Massey-product assertion follows.

The statement concerns ordinary bundles with the fixed deck action and chosen linearization. It does not prove unrestricted smoothness or an unrestricted tangent-dimension assertion, add a determinant trivialization, supply star-module admission, identify a coarse moduli chart, or algebraize arbitrary formal maps. Neither the older exactness premise nor the separate historical invariant-rank premise has been promoted to freshly verified evidence.
