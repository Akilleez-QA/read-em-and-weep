# Mixed presentation and the equivariant extension line

**Craig Ward · 23 October 2026 · PR1055**

[Immutable full proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/168d87759e9487d415e3da2a9b174974d621297c/research/hm/source2-pure-v-original-fourth-presentation/PROOF.md).

## Actual mixed-degree presentation on ℓ₃

Assume the unknown universal gate is nonzero and lies on ℓ₃=span(R₁−2R₂). The [cubic syzygy theorem](87-pure-v-cubic-a-syzygies.md) supplies the actual inclusion S:A O(-2)→P O(1), obtained by twisting K_F=A O(-3). Together with L:D O→P O(1), it gives a genuine exact bundle presentation

    0→K_H→D O⊕A O(-2) --[L,-S]→ P O(1)→0.

The L entries are linear and the S entries cubic. S uses the abstract syzygy A in its authenticated coefficient basis; this is not an unverified identification with a standard monomial basis.

Surjectivity follows because A O(-2)→C_L is onto by the actual kernel bridge. In a compatible local normal form, three L columns give the first three target basis vectors and a column from −S gives minus the fourth, producing a local right inverse even at the rank-drop points. This is not inferred from generic rank or Chern data.

Projection (d,a)↦d identifies the kernel with K_H: the equality Ld=Sa puts d in ker H, and every such d has a unique a since S identifies its source with ker F(1). These are the determinant-target kernels of the surviving original-fourth D row, not additional specialized A-kernel classes.

## One equivariant extension dimension, ten without equivariance

Retain E=ker(A O(-2)→C_L), with C_L of length ten. Applying global Ext(-,O(-4)) and using H1(O(-2))=H2(O(-2))=0 gives canonically

    Ext¹(E,O(-4))≅Ext²(C_L,O(-4)).

At each order-three axis the full projective stabilizer is S₃, not just its cyclic subgroup. The axis line has sign character, so O(-2) and O(-4) are trivial there. A restricts as sign⊕standard. The actual one-dimensional quotient C_L therefore has sign character. The tangent representation has determinant sign. Local Koszul duality makes the local Ext² character trivial, since the two signs cancel.

The orbit of ten axes is transitive, so the global Ext representation is induced from that trivial stabilizer character. Frobenius reciprocity gives invariant dimension one. In characteristic zero finite-group invariants are exact, hence

    dim Ext¹_G(E,O(-4))=1,
    dim Ext¹(E,O(-4))=10.

The full stabilizer and the actual quotient character are essential to this conclusion.

## Precise uniqueness and retained limits

The actual extension 0→O(-4)→K_H→E→0 is nonzero because its local Koszul extension is nonsplit at every axis. It is therefore the unique nonzero **equivariant** extension up to nonzero scalar and corresponding rescaling of the line injection. This does not identify all nonequivariant extensions or select a distinguished scalar with fixed endpoint identifications.

K_H is not asserted split. Its rank four, c1=−10h and c2=46h² are consistent with the previous bridge, not a new scheme classification. The theorem does not establish that the actual gate lies on ℓ₃, select its coefficients or prove compatible-source occurrence. The completed five-stratum classification and four-pair source frontier remain unchanged.

The proof establishes the presentation, local duality and equivariant Ext calculation. Formal local right-inverse, stabilizer-character and Chern checks support those arguments without evaluating an actual quadratic direction or source.
