# Historical mathematical audit receipt

This is a preserved review of the source mathematical manuscript, not a fresh review of the publication bytes. Hashes quoted below identify the historical source versions. See [hm-normalizer-foundations-PUBLICATION-CHECK.md](../hm-normalizer-foundations-PUBLICATION-CHECK.md) for the final-publication review.

## 1. Coefficient representations and dual conventions

The original paper gives the normalizer, its semidirect-product description, the extension of the five-dimensional Heisenberg representations, the multiplicity module W with character χ2, its invariant alternating form, and the equivariant monad. Its general multiplicity-space criterion (2.2) is exactly the normal-subgroup argument used here.

The normalized left endpoint is V1 O(−1), and the right monad coefficient is its representation dual V3. The invariant volume identifies Λ³V with Λ²V*, without a determinant character because N lies in SL5. Accordingly the Euler coefficient space is Λ²V* ⊗ W. Dualizing Λ²V = V1 ⊗ W and using W* ≅ W gives

    Λ²V* ⊗ W ≅ V3 ⊗ (W ⊗ W).

The right monad contraction is nonzero on the trivial alternating factor and zero on Sym²W. Thus its kernel is V3 ⊗ Sym²W. This is a representation identification, not a dimension argument.

The copy-space basis in the literal presentation must be understood through the alternating identification W* ≅ W. The proof explicitly transports the action from the historical monad rather than assigning a naive action to the two named copies. Therefore there is no hidden dual/sign mismatch. Its reference to the already fixed right-map uniform sign is sufficient: that sign does not change the kernel representation.

As a separate check, under a central scalar ζ, every term of the normalized equivariant complex has scalar ζ³: O(t) has scalar ζ^(−t), V1 has ζ², V3 has ζ³, and V* has ζ^(−1). Hence End H(−2) has scalar ζ², precisely matching the asserted final module.

## 2. Global cycles: why projection is an isomorphism

For Hom(K,K(−2)), the internal degree-r terms have line degree r−2. In global internal degree two the two blocks are

    A ∈ Hom(V1,V* ⊗ W),
    B ∈ Hom(C0,W).

The only degree-three global block is Hom(V1,W) ⊗ V*. Natural evaluation identifies the A-space isomorphically with this whole block. The cycle equation therefore determines A uniquely from arbitrary B. Its sign depends on the standard Hom differential convention, but neither existence, uniqueness, nor equivariance does. Projection to B is thus an actual N-equivariant isomorphism of global cycles with Hom(C0,W).

There are no global degree-one boundaries, since those terms have degree −1. Using the self-duality of W and Sym²W consequently gives

    Z²_global ≅ V1 ⊗ (Sym²W ⊗ W)
               ≅ V1 ⊗ (W ⊕ Sym³W).

The tensor decomposition is valid for determinant-one two-dimensional modules and remains valid after restriction to the finite quotient group.

## 3. The higher-row correction and cancellation

Line-bundle cohomology on P⁴ leaves precisely one higher-row entry: internal degree −3 and sheaf degree four. It is

    Hom(W,V1) ⊗ H⁴(O(−5)).

The top cohomology factor is trivial on SL5 by equivariant Serre duality. The entry is therefore V1 ⊗ W. It has total degree one. There are no incoming differentials, and its only possible outgoing differential is d5 to bidegree (2,0). The imported vanishing H¹(End H(−2)) = 0 forces this map to be injective. Total degree two has no other surviving filtration piece, giving exactly the short exact sequence in the proof.

The vanishing provenance is the Decker–Schreyer proposition, printed p.218, recorded in ../pairing-foundation-inputs/COHOMOLOGY.md and the primary-source verification notes. It is not being inferred from the desired irreducibility or from a finite-model rank.

In the appendix's class order, applying t³−2t to the displayed W character gives

    (4, −4, 0, 1, −1, −1, −1, 1, 1),

the spinorial irreducible four-dimensional row χ4#. The Heisenberg multiplicity-space criterion then makes both V1 ⊗ W and V1 ⊗ Sym³W irreducible and nonisomorphic. Consequently the injected source is precisely the unique ten-dimensional irreducible summand of Z²_global. There is no possibility of a graph into the twenty-dimensional summand, by Schur's lemma. Its quotient is exactly the asserted irreducible module.

