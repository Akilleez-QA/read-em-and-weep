# The explicit thirty-coordinate quotient

This supplements [PROOF.md](PROOF.md), retaining all its scope and evidence boundaries. In particular, its thirty-dimensional space is not being identified with any other thirty-dimensional retained multiplicity space merely by dimension or character coincidence.

## 1. Eliminate one block without any rank computation

A global degree-two map of twist −2 has two constant blocks

    A:C₋₁→C₁,     B:C₀→C₂.

Its differential has the single block

    ev(v)A−Bγ(v):C₋₁→C₂⊗H⁰(O(1)).

The map A↦ev(v)A is the tautological isomorphism

    Hom(k⁵,k²⊗k⁵) → Hom(k⁵,k²)⊗span(v₀,…,v₄):

each of the ten output coordinates of A is exactly one coefficient of the two evaluation rows. Hence every B determines one and only one A with ev(v)A=Bγ(v). Projection onto B identifies Z²_global canonically, in the fixed displayed bases, with Hom(k¹⁵,k²). This proves its dimension thirty directly from the formal coefficient description.

The derivative relation attached to a<b has B-block r_aδ_b. Let η be the alternating coefficient array η_pq=−η_qp. The relation corresponding to η has the following entries, up to the uniform minus sign determined by P_ab=D_aD_b:

    B_{+,U_i}=−η_{i+2,i+3},       B_{−,U_i}=0,
    B_{+,V_i}=0,                 B_{−,V_i}=−η_{i+1,i+4},
    B_{+,Z_i}=−η_{i+1,i+4},      B_{−,Z_i}=−η_{i+2,i+3}.

Indices retain the displayed cyclic order. Thus each relation is the sum, with matched oriented signs, of its U-plus and Z-minus coordinate, or of its V-minus and Z-plus coordinate. Each pair is disjoint from every other relation pair. The ten independent relations eliminate ten of these twenty coordinates. The remaining ten coordinates B_{−,U_i}, B_{+,V_i} are untouched.

In particular one may choose twenty explicit quotient coordinate classes: for every i take the classes of the elementary matrices supported at

    (+,U_i), (−,U_i), (+,V_i), (−,V_i).

The ten Z entries are eliminated by the relations. This is a chosen basis from the literal coefficient decomposition, not a coordinate-free preferred basis of End-cohomology. It consists of classes of closed maps: each displayed elementary B is accompanied by its uniquely determined A from the preceding paragraph.

More explicitly, the unique representative with all Z columns zero is obtained by replacing B_{+,U_i} by B_{+,U_i}−B_{−,Z_i}, and B_{−,V_i} by B_{−,V_i}−B_{+,Z_i}, leaving B_{−,U_i} and B_{+,V_i} unchanged. This is a formal quotient formula for an arbitrary symbolic B, not an evaluated source or detector.
