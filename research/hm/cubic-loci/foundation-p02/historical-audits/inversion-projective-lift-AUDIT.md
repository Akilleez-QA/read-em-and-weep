# Historical scope-limited review receipt

This review concerns the original source, possibly a larger scope than the excerpt in this unit. It is not a review of normalized publication bytes.

# Independent audit

## Verdict

The theorem and its main proof are correct, conditional on the exact four-term HM presentation and the full-chain monomial symmetry result supplied by the two referenced proof packets. The argument proves an order-four global regular projective lift and vanishing of the untwisted Hom space. It makes no unsupported source-level or scalar-covariance inference.

## Checks

1. **Global extension and order.** The rational translation formula is the elliptic addition-law identity for the nonzero two-torsion point T. Composing it with τ gives the stated inversion formula. Since τ fixes T, translation commutes with τ, yielding a²=[−1] and exact order four in characteristic zero. This also resolves the apparent affine poles globally.

2. **Reversal compatibility.** The reciprocal elementary-symmetric identity gives f a=R f on the indicated dense open, hence globally by separatedness. The reversal permutation has affine index rule π(j)=−j+4. The supplied monomial proof gives a full-chain isomorphism, not merely a first-differential intertwiner, so H≅R*H is justified.

3. **Nontrivial two-torsion twist.** The automorphism exchanges O and T, so a*O(O)=O(T), a*P_T=P_T⁻¹≅P_T, and a*N≅N⊗Q. The identification C≅Pic⁰(C) proves P_T is nontrivial two-torsion; restriction to a factor proves Q is nontrivial. Consequently a*E≅E⊗Q holds over Q(i), without a trivialization of Q.

4. **Projective cyclic coherence.** Tensoring by N disappears canonically on projectivization. The monomial proof’s one-dimensional Hom spaces give a coherent projective lift r of R with r²=id. The fiber-product map (z,p)↦(a(z),r(p)) is therefore global and regular, squares to ([-1]z,p), and has exact order four. Its exact order follows already from the induced base map.

5. **Hom vanishing.** For the bounded locally free presentation A, degree-r terms of Hom•(A,A⊗Q) are sums of N^(2r)⊗Q, with −3≤r≤3. Elliptic cohomology and Künneth put positive-r terms in row q=0 and negative-r terms in row q=4. The r=0 column is acyclic because P_T is nontrivial of degree zero. All nonzero E₁ entries thus have strictly positive total degree. The bounded hypercohomology spectral sequence proves Hom(E,E⊗Q)=0, hence Hom(E,a*E)=0. No chain-map classification or computed rank is needed for this final vanishing.

6. **Uniqueness and endomorphism algebras.** The added §6 is sound. A vertical projective automorphism determines a self-twist E≅E⊗P; taking determinants forces P²≅O_X. Over C, torsion lines on this product of elliptic curves belong to Pic⁰. The same spectral-sequence argument excludes every nontrivial Pic⁰ self-twist, since a nontrivial external degree-zero factor makes the entire r=0 column acyclic. For P trivial, the degree-gap argument gives constant strict chain representatives. Dominance of f transfers their initial equation to the formal downstairs coefficient equation; the identity case of the monomial theorem bounds its solution space by one. An initial pair with zero degree-zero block induces zero on E, so End(E)=C. Thus vertical projective automorphisms are trivial and the lift is unique. The endomorphism-algebra isomorphism follows canonically from invariance of End under tensoring by a line. Base change proves the asserted uniqueness over Q(i).

## Notation correction verified

The initially read §4 omitted the two-block multiplicity in the third chain block. The revised file now correctly writes the four blocks as

    P_π, M_π, −I₂⊗P_π, −I₂.

The third block has size 10×10. Every block squares to the appropriate identity. This correction is complete; no outstanding mathematical correction was found.

## Scope of audit

Only static reading of the three supplied proof files and abstract mathematical reasoning were used. The foundational exact-presentation premise was checked for consistency with the supplied CM packet, not independently reconstructed from its external references. No source/model execution, rank calculation, polynomial-instance or point evaluation, jet/residual evaluation, external write, or local Codex operation was performed.
