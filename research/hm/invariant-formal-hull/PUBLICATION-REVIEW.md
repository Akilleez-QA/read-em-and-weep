# Independent mathematical review of the invariant formal hull

**Scoped PASS, October 20, 2026.** This review addresses the full 79-variable ordinary formal-hull proof, conditional on the geometric and cohomological prerequisites.

## Hypotheses retained

The specified proper product X, fixed deck action, locally free E, characteristic-zero field, literal exact-presentation premise P, actual smooth 79-dimensional coefficient family, and injective Kodaira–Spencer map are retained as geometric inputs. The invariant tangent dimension D=79 is a separate input. README correctly points to PR179 at 2b03992b32d2f5cf0509b6f4840adf08369f54b7 for its structural cohomology proof under the stipulated characteristic-zero/base-change premises. PR125's presentation premises and the specified cohomology inputs remain explicit hypotheses. General characteristic-zero forms are not silently substituted for the stipulated models.

## Independent reasoning

1. The marked linearized-bundle groupoid has trivial special-fiber groupoid but may have infinitesimal automorphisms. Equivariant self-extensions identify its tangent with Ext^1_G(E,E). Exact invariants for the finite group, whose order is invertible, identify this with Ext^1(E,E)^G. Properness gives finite tangent dimension. No simplicity hypothesis is needed.

2. The entire coefficient family, not merely its tangent image, is equivariant: its map factors through the deck quotient, while N has the specified invariant-divisor linearization. The completed family therefore defines a genuine formal object over S=k[[t_1,...,t_79]]. Its tangent map is injective after forgetting equivariance and hence injective equivariantly. D makes it bijective. Character twists do not change conjugation on End E, but the functor nevertheless fixes the chosen special-fiber linearization.

3. Patching uses a fiber product with one projection surjective. On affine opens tensoring over k preserves that fiber product. Finite-projective patching gives the object and full faithfulness for morphisms; a basis of the special fiber lifts over the nilpotent thickening. The marking and linearization maps patch, with group law detected on the two factors. This justifies the Rim–Schlessinger condition and hence a minimal versal formal object. I consulted the stated Stacks references 06IL and 0DVP on October 20, 2026; the cited groupoid/miniversality and finite-projective-patching framework is appropriate. In 06IL the coefficient and residue field here are both k, so the separability qualification presents no obstacle.

4. Versality, not universality, yields compatible maps R to S/m^(n+1) and compatible isomorphisms to the actual family. Thus R→S exists with invertible cotangent map. For a minimal presentation P=k[[x_1,...,x_79]]→R, the composite P→S has invertible linear part and is a formal coordinate isomorphism. Its injectivity forces the whole relation ideal to vanish, including higher-order and nilpotent equations. This is a genuine higher-order conclusion relying on the full family, not an inference from tangent dimensions alone.

5. The audit's separate direct proof is sound. Across a small extension A→B with kernel I annihilated by m_A, two existing lifts with their specified B-identifications differ by Ext^1_G(E,E)⊗I. Retaining those identifications is essential. Parameter lifts differ by T_uU⊗I, and their effect on the lift torsor is the closed-point Kodaira–Spencer map. Its bijectivity corrects any discrepancy and supplies an isomorphism extending the prescribed reduction. Nonzero Ext^0_G⊗I gives automorphisms of a lift, not a failure of transitivity on fixed-reduction isomorphism classes. Iterating small extensions proves the claimed smooth groupoid map independently of the hull argument.

## Claim boundaries

The completed coefficient family is miniversal and the ordinary invariant problem is unobstructed at every Artinian order, conditional on the hypotheses above. Classification and compatible lifting are existential. Neither uniqueness of maps nor equivalence with a discrete fine-moduli functor follows. Scalar automorphisms alone also do not disprove prorepresentability of the isomorphism-class functor; the proof says this correctly.

Vanishing of each square and of symmetrized Yoneda products follows from ordinary unobstructedness in characteristic zero. It does not by itself establish individual ordered-product vanishing, Ext^2 vanishing, formality, or arbitrary Massey-product vanishing. README properly distinguishes PR179's separate ordered-product theorem. No fixed-determinant, unrestricted-character, source-varying, coarse fixed-locus, algebraicity of formal maps, or star-module lifting conclusion is claimed. All these exclusions are mathematically necessary and retained.

## Exact reviewed mathematical texts

PROOF.md SHA-256: 7ef7d8a4efc9a2db7e2573e32d9c29bafbb75fef6dfadabfc49e0a6a91c9b44f.

INDEPENDENT-AUDIT.md SHA-256: 73c8fcca6ba7ea43d8e51d45c7e309c27b44af30255e21ab8841ad2725dfd501.
