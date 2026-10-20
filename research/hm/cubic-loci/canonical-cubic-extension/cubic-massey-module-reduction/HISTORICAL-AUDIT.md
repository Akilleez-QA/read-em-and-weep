# Historical review receipt

This review concerns its original manuscript version, not the normalized publication bytes. It is not a final publication-scope approval.

# Independent audit of the cubic module reduction

## Verdict

The proof is sound, conditional on its explicitly imported ordered-product vanishing, coherent-cohomology dimensions, Euler/Kodaira–Spencer identification, full canonical Massey identities, and HM representation identities. No mathematical correction is required. In particular, the conclusion is an at-most-one-dimensional common parameter family for the two mixed channels; no nonvanishing claim has been established.

## Checks

1. **Canonical cubic and scalar linearity.** The pair products of twist-one classes are exact in twist two. Both indeterminacy summands for the triple operation contain H¹(End H(-2))=0. The representative-change identities respect all twists. For closed central scalars p,q,r, the primitives pq h_ab and qr h_bc give precisely pqr times the original Massey cocycle. This compares the already canonical operations directly, without a module-linear contraction or a choice of minimal model. The imported canonicality of the mixed operations makes the comparisons unambiguous.

2. **Coefficient leading-symbol transfer.** The imported generation filtration has split underlying O-module inclusions, so its cohomology is strict and a boundary in filtration two has a primitive in filtration two. Lift a⊗u,b⊗v,c⊗w from gr₁K to K. Projecting the two adjacent primitives to gr₂ gives defining systems in C₂⊗A^(0,*)(End H(-2)). Their differences from the coefficient-factorized primitives are closed degree-one cochains; H¹(End H(-2))=0 makes these differences exact. Their contribution to the degree-three output is consequently a boundary. This proves gr₃M=abc⊗f(u,v,w). Changing a lift by filtration zero changes the output only in filtration at most two, so the symbol is independent of lifts. Standard gradedness implies that products of three degree-one elements span the nonzero C₃. Thus at least one abstract triple product is nonzero. Cancelling that coefficient by a linear functional validly transfers reversal and cyclic zero. Coefficients have cohomological degree zero and commute, so argument permutations introduce no coefficient sign. No multiplicative splitting is used.

3. **Equivariant Serre duality.** The trace pairing gives the N-equivariant self-duality of End H. For the convention P(V) used here, the canonical bundle is O(-5)⊗det(V)*; N lies in SL(V), so the determinant factor is trivial. Since dim P(V)=4, Serre duality pairs H²(End H(-3)) perfectly with H²(End H(-2)). Therefore J₃≅J₂*. The determinant-one alternating form on W induces a nondegenerate equivariant pairing on Sym³W, so S is self-dual. It follows that J₃=A*⊗S, with no hidden determinant character. This is a downstairs N-equivariant statement and does not use the separate sign-valued pairing on the coefficient cover.

4. **Cubic source and multiplicity.** Reversal and cyclic zero give one copy of Schur_(2,1)V, of dimension forty, rather than the entire standard-isotypic component of V³. An independent derivation avoids reliance on the primary source's mixed-product citation: Galois conjugation gives A⊗A≅V*⊗(Sym²W⊕W′). For any G-module M, equivariant tensor-Hom adjunction identifies Hom_N(A*⊗M,V⊗A) with Hom_N(V*⊗M,A⊗A), hence with Hom_G(M,Sym²W⊕W′). Thus V⊗A≅A*⊗(Sym²W⊕W′). Subtracting Λ³V=A*⊗W from V⊗Λ²V gives Schur_(2,1)V≅A*⊗(S⊕W′⊗W). The G-central involution distinguishes S from W′⊗W. Irreducibility of S then proves that the required Hom space has dimension one.

5. **Euler-balanced descent.** For any eligible cubic map and the actual cohomological multiplication V*⊗J₃→J₂, contracting any input slot against the invariant identity tensor gives an N-map V⊗V→J₂. The source is A⊗(Sym²W′⊕W), while the target is A⊗S; their Hom space is zero. Hence all three Euler contractions vanish. Since V*⊗V→Z has exactly the scalar identity as kernel, these are every relation needed for descent to one Z slot. Multiplying the identities by another linear form proves descent to two Z slots, using associativity of genuine cohomological scalar multiplication. No additional degree-one relation can remove the cubic line.

## Limits and evidence boundary

The cubic parameter may be zero for the actual operation. A nonzero abstract cubic parameter may also be killed after one or two cohomological scalar multiplications; their nonvanishing is not supplied by this argument. Higher geometric identities are not claimed to be exhausted.

This audit used static proof reads and abstract DGA, filtered-cohomology, Serre-duality, and finite-group representation reasoning. No literal source/model matrices or products, ranks, polynomial instances, points, jets, residuals, or Massey values were constructed or evaluated. The only write was this local audit deliverable.
