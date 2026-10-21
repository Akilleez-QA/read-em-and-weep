# Uniform vertex filtration eliminates preserving positive cone excess

## Result

For the actual invariant-cone spinor filtration 0->S->E->J->0, every inversion-even tracefree section E->E(4) preserving S commutes with the canonical nilpotent N. The preserving positive space is exactly

N H0(O_Q0(2))_+ = A direct-sum D5,

of dimension eight. No claim is made yet that every positive adjoint preserves S. The lower-off-diagonal Hom/Ext lifting gate in POSITIVE-CONE-EXT-ANNIHILATOR-AND-VERTEX-GATE.md is retained.

## 1. Generic Loewy dimensions are uniform on the entire vertex

The actual pure spinor defect T_L has finite pushforward D=(A+2W-prime) O_L(2). The established universal vertex action gives generic Loewy dimensions (2,3,2), with m^3 T_L=0 generically. Here m is the ideal of the reduced vertex in the transverse cone algebra.

The positive-coordinate action is a bundle map V tensor D(-1)->D. In frames of the common O(2) twist, its entries are linear forms on L=P(W). Its generic image mT_L has rank five. A nonzero five-minor is a section of O_L(5). Any rank-drop locus is G-invariant and is contained in its zero set. Every nonempty G-orbit on L has at least twelve points. A nonzero section of O(5) cannot vanish on such an orbit. Hence the rank is five everywhere.

Likewise the double-action map Sym^2 V tensor D(-2)->D has entries of degree two and generic rank two. A nonzero two-minor has degree four. The same orbit argument makes its rank two everywhere. Triple action is identically zero because it is a bundle morphism zero at the generic point.

Thus all images and successive quotients are vector bundles and every transverse fiber has Loewy dimensions exactly (2,3,2). This argument is uniform at the exceptional orbits; it evaluates no minor at a selected point.

## 2. Relative local complete intersections and the Ext module

Locally along the base L, the transverse double cover has ring B=O_L[[a,b]], its even subring R, and its odd spinor module M. The actual locally free E gives J=Rf+Rg subset M with two odd generators. This assertion is relative, not an assumption that Ext commutes with specialization. The defect is flat over the base by its established locally free pushforward D, so J embeds in M after specialization. Also J is base-flat, being a submodule of the base-flat M over a local DVR, and therefore the exact presentation E -> J remains exact on every fiber. The two generators are consequently the actual two-generator odd quotient on each fiber. They are a regular sequence in B: fiberwise their quotient has finite length in two transverse variables, and base-flatness of the resulting relative complete intersection follows from the fiberwise regular-sequence criterion. The relative Koszul syzygy is h -> (-gh,fh) with h in M. Dual restriction then has image (f,g)M. Thus the ideal I_e defining sheaf Ext^1(J,S) is (f,g)M without invoking Ext base change; this is the relative form of VERTEX-EXT-ANNIHILATOR-LENGTH-EIGHT.md.

The uniform Loewy filtration allows a local generator choice with f of transverse order three and g of order five. To justify this relatively: the cubic relation is a line subbundle, so choose f generating it; subtract a base-function multiple of f from the second generator to remove its cubic term. The remaining quintic relation modulo f times quadratic forms is again a line subbundle, so choose g generating that quotient. No global splitting of this generator extension is asserted.

On every fiber, the same degree-seven dimension argument proves that f3 and g5 are coprime. Therefore the initial pair is a relative regular sequence, and the associated graded algebra is the relative complete intersection by f3,g5. The Koszul resolution shows its graded pieces are locally free of constant ranks. The complete local quotient B/(f,g) and its even part are consequently finite flat over the base. In particular the Ext vertex module V_e=(B/(f,g))_even has no special-fiber or finite-length base defect missing from this argument.

Its first three normal graded pieces are O_L, V O_L(-1), and the quotient G2 described next. Its fourth has rank one; no knowledge of that fourth piece is needed to prove the result below.

## 3. The actual degree-two Ext quotient

The actual annihilator is the image of J tensor S(-3) -> O_X. Indeed det(E)=O_X(3), so the rank-two wedge identification E*=E tensor O_X(-3) turns the dual restriction Hom(E,S)->O_X into the wedge quotient E->J subset S(2), followed by multiplication with S(-3). This is an image-of-multiplication identity, not an identification of J with an ideal tensor a line bundle. It also follows locally from I_e=(f,g)M, with the determinant twist retained.

The normal graded pieces of the spinor S(2) are Sym^(2n+1)(W-prime) O_L(2-n). The cubic relation is a line F in Sym^3(W-prime) O_L(1). Since its quotient is the middle Loewy bundle A O_L(2), the degrees give

F=O_L(-2).

Its equivariant cubic is the unique invariant in Sym^3(W-prime) tensor Sym^3(W). It is nonzero fiberwise. The dual spinor (S(2))*=S(-3) has lowest normal piece W-prime O_L(-3). Thus multiplication of the cubic relation by this piece gives the degree-two annihilator relation W-prime O_L(-5). The actual Ext quotient has the exact vector-bundle presentation

0 -> W-prime O_L(-5) -> D5 O_L(-2) -> G2 -> 0.

There are no lower annihilator relations, and no further degree-two relation: the other generator has order five, whose product with an odd generator starts in degree three of the even cone algebra. Uniform relative regularity from Section 2 makes this exact at every fiber.

The independently checked cubic quotient theorem identifies G2=V O_L equivariantly. Only its displayed presentation and the acyclicity used below are needed for the injectivity argument.

## 4. The twenty-dimensional vertex gate is injective

The Ext-annihilator theorem gives preserving positive excess exactly H0(I_e(4))_+. Vanishing on the reduced conic removes the pure-positive-coordinate component of an even ordinary quartic. The remaining source K20 has only normal orders zero and two:

K20 = Sym^4 W direct-sum (D5 tensor Sym^2 W).

Restriction at normal order zero is the identity on H0(O_L(4))=Sym^4 W. Thus a section of K20 vanishing in V_e(4) must have zero order-zero component.

Its remaining normal-order-two component maps by the actual quotient presentation in Section 3, twisted by four:

0 -> W-prime O_L(-1) -> D5 O_L(2) -> G2(4) -> 0.

The left bundle is acyclic. Hence its map on global sections is an isomorphism, of dimension fifteen to fifteen. A normal-order-two component whose image in V_e(4) vanishes therefore is zero. There is no remaining normal-order-four component, since vanishing on C0 already removed precisely that pure-positive polynomial component.

This proves H0(I_e(4))_+=0. The exact preserving-endomorphism sequence then gives the asserted eight-dimensional centralizer and no additional preserving positive adjoint.

The argument does not need a global quintic generator, a splitting of the full Ext module, or an assumption that all adjoints preserve the spinor subsheaf. Those would be additional claims and are not made.

## Dependencies and evidence

The actual vertex action and generic Loewy dimensions are in the companion of verify_invariant_cone_vertex_module.py. The spinor/Ext bridge is VERTEX-EXT-ANNIHILATOR-LENGTH-EIGHT.md. The preserving exact sequence and K20 identification are POSITIVE-CONE-EXT-ANNIHILATOR-AND-VERTEX-GATE.md. The independent cubic quotient calculation is supplied by the scalar-target worker; its presentation is restated and used explicitly above. The companion verify_no_preserving_positive_excess.py checks the degree bounds, uniform rank-drop exclusions, and the acyclic global-section count. No actual coefficient or selected rank is evaluated.
