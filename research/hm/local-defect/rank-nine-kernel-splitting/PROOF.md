> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# Generic rank nine forces a split kernel of degrees three and eight

Under the hypotheses and notation of ../global-linear-image-plucker/PROOF.md, generic rank(Q)=9 implies

    k=4, d=0, e=9,
    ker(b) ≅ O(-3) ⊕ O(-8).

The O(-3) summand is the canonical cubic square relation. The splitting can be chosen equivariantly for the full HM normalizer. These statements concern kernel sheaves. They do not assert that the inclusion of this kernel is a subbundle at every point or that b has constant rank.

## 1. Representation input and elementary consequences

Set S=Sym²V. The audited identities in ../../cubic-loci/canonical-cubic-extension/cubic-massey-module-reduction/PROOF.md, Section 4, and ../../full-hm-image-symmetry/PROOF.md give

    V⊗V = A⊗(Sym²W′ ⊕ W),   Λ²V=A⊗W.

Therefore S=A⊗Sym²W′. Here A restricts irreducibly to H5, and W′ is an irreducible two-dimensional representation of G=SL₂(F5).

G is perfect. Indeed, for upper unipotents U(t) and D=diag(2,2⁻¹), the commutator is [D,U(t)]=U(3t); these give every upper unipotent. The analogous calculation gives every lower unipotent. Upper and lower unipotents generate SL₂(F5). Hence every one-dimensional complex character of G is trivial, and det W′=1.

The representation Sym²W′ has no invariant vector: via the determinant-one alternating identification W′≅W′*, Schur's lemma says the invariant bilinear form on W′ is unique up to scalar and alternating. If the semisimple three-dimensional representation Sym²W′ were reducible, it would have a one-dimensional summand. Such a summand would be trivial, a contradiction. Thus Sym²W′ is irreducible. The usual Heisenberg-isotypic correspondence then shows S is N-irreducible, so End_N(S)=C.

Also N=H5⋊G is perfect. The center of H5 is already in [H5,H5]. The quotient H5/Z(H5) is the natural two-dimensional F5-module, whose coinvariants under G vanish (already the central element −I has g−1 invertible). Thus the commutators with G generate H5 modulo its center; together with perfectness of G this generates N. In particular there is no character ambiguity in N-linearizations of a given line bundle on P(V).

## 2. A general rank-two kernel splitting lemma

Untwist b and let

    B:S⊗O → J⊗O(1),   K=ker B.

For generic rank(Q)=9, K has rank two. The identity B(u²)=0 gives a globally defined line subbundle O(-2) of S⊗O contained in K. Its ambient quotient E is locally free. Hence

    K/O(-2)=ker(E → J⊗O(1)).

This kernel is reflexive: a kernel of a map between locally free sheaves on a smooth variety is torsion-free and satisfies S₂. Explicitly, the image is torsion-free; at a local ring of dimension at least two it has depth at least one, so the depth lemma gives depth at least two for the kernel. At codimension one the kernel is free. Since its rank is one, it is a line bundle on the smooth factorial variety P⁴.

The saturated kernel K has determinant O(-e). One way to see this is to take its determinant inclusion into Λ²S⊗O: its primitive Plücker coordinates have degree −c₁(K); saturation makes them primitive at every codimension-one point. They are precisely the residual kernel coordinates defining e. Equivalently the image of B has determinant O(n−k−d).

Consequently K/O(-2)=O(2−e), and

    0 → O(-2) → K → O(2−e) → 0.

Its extension class lies in H¹(O(e−4))=0 on P⁴. Therefore

    K ≅ O(-2) ⊕ O(2−e).

All maps and sheaves are equivariant. Any splitting can be averaged over the finite group N, so the splitting can be equivariant. The quotient line's linearization is its natural one, because N has no nontrivial characters.

## 3. Degree four is impossible

The previous necessary-condition table permits e=4 or e=9 at rank nine. Suppose e=4. The equivariant splitting above would give two independent equivariant inclusions O(-2)→S⊗O.

But the vector space of equivariant such maps is

    Hom_N(Sym²V,S)=End_N(S)=C.

The canonical square inclusion spans it. The second summand's inclusion must therefore be a scalar multiple of the first, contradicting the generic rank-two inclusion K→S⊗O. Hence e≠4.

Thus e=9. The table then forces (k,d)=(4,0), and Section 2 gives K=O(-2)⊕O(-7). Twisting by O(-1) gives the claimed ker b=O(-3)⊕O(-8).

## 4. Exact resolution and its scope

Writing G=im b for the actual image sheaf, there is the exact resolution

    0 → O(-3)⊕O(-8) → O(-1)⊗S → G → 0.

The saturation F has determinant O(-4); d=0 says G and F agree at every codimension-one point. It does not identify them in codimension two or higher. The displayed resolution concerns G, not automatically F. Fiberwise injectivity of the left map and local freeness of G are not claimed.

This proves a conditional restriction, not generic rank nine itself. Only existing representation identities, universal bundle geometry, and finite-group averaging are used. No actual operation product, source matrix, input, rank instance, polynomial instance, jet, or residue is evaluated.
