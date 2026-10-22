# Positive noncommuting cone adjoints: an exact Ext annihilator and vertex gate

Retain the actual equivariant filtration on the invariant cone X=Q0:

0 -> S --i--> E --p--> J -> 0, with E=F_X(2),
0 -> J -> S(2) -> T -> 0,
T=O_C0(5) direct-sum T_L.

Here S is rank-one reflexive and not invertible on the vertex L; T_L is the actual pure generic-length-seven vertex module whose finite pushforward is (A+2W-prime) O_L(2). We do not replace J by an ideal tensor S(2). Let e be the actual extension class in Ext^1_X(J,S).

## 1. The correct annihilator ideal

Apply sheaf Hom(-,S) to the first exact sequence. Since E is locally free and End(S)=O_X, its connecting map gives a surjection

O_X -> sheaf Ext^1_X(J,S),   1 |-> e.

Let I_e be its kernel. Equivalently I_e is the image of Hom(E,S) -> Hom(S,S)=O_X by restriction along i. Thus

sheaf Ext^1_X(J,S)=O_X/I_e.

This is an actual ideal and cyclic Ext module, not an assumption that the defect T has an ordinary ideal description. In particular I_e is not identified with Ann(T).

On the smooth locus where S is invertible, the inclusion is locally a pair (f,g). The dual restriction image is the ideal (f,g). The established transverse reduced-conic result therefore gives I_e=I_C0 near C0. Off C0 union L, the defect is absent and the extension is locally an extension of line bundles, hence splits locally; there I_e=O_X. Consequently

O_X/I_e = O_C0 direct-sum V_e,

where V_e is supported set-theoretically on L. Its possible nonreduced structure and finite defects are retained. Its support is finite over L under the negative projection, but no splitting or purity of V_e is asserted merely from purity of T_L.

## 2. Exact filtration-preserving positive excess

Let P be the vector space of tracefree maps phi:E -> E(4) preserving S, meaning phi i factors through S(4). Such a map induces endomorphisms on S and J with twist four. Rank-one reflexivity and normality imply

Hom(S,S(4))=O_X(4),
Hom(J,J(4))=O_X(4),
Hom(J,S(4))=O_X(2).

For the last identity, J agrees with S(2) in codimension one and morphisms to the reflexive target S(4) extend uniquely across codimension two; Hom(S(2),S(4))=O_X(2). This is a Hom identity and does not tensor J by a noninvertible inverse.

The induced diagonal pair has the form (a,-a), with a in H0(O_X(4)), because phi is tracefree. A morphism of the two extensions with this pair exists exactly when the pushout and pullback extension classes agree, namely

2 a e = 0 in Ext^1_X(J,S(4)).

The local-to-global Ext sequence and H1(O_X(2))=H2(O_X(2))=0 identify Ext^1_X(J,S(4)) with H0(sheaf Ext^1_X(J,S)(4)). The vanishings follow directly from the hypersurface sequence for O_X(2). Hence the compatibility condition is exactly a in H0(I_e(4)). If it holds, the standard extension-morphism construction supplies phi; two such choices differ by Hom(J,S(4)). We obtain the exact sequence

0 -> H0(O_X(2)) -> P -> H0(I_e(4)) -> 0.

The left term consists precisely of polynomial multiples of the canonical nilpotent N. Indeed the composition E -> J -> S(4) -> E(4) has zero diagonal and is generically the nilpotent direction; normal extension identifies its coefficient with an ordinary quadratic function. Taking inversion-even parts is exact. Therefore

dim(P_+) = 8 + h0(I_e(4))_+.

Thus the positive filtration-preserving noncommuting excess is EXACTLY H0(I_e(4))_+, not merely bounded by it. Any nonzero element already obstructs rank33 at q0.

## 3. A twenty-dimensional actual vertex restriction gate

The weighted cone description gives H0(O_X(4))_+ dimension 29. Restriction to C0 is onto its degree-eight binary forms, dimension nine. The kernel has the canonical representation

K20 = (Sym^4 W-prime tensor Sym^2 W) direct-sum Sym^4 W
    = (D5 tensor A) direct-sum D5
    = A direct-sum V direct-sum P4 direct-sum 2D5.

The first term contains two positive coordinates and two negative coordinates; the second contains four negative coordinates. The relation q0 has already been imposed by the weighted description. The conic summand corresponds to four positive coordinates and is removed by restriction.

Using O_X/I_e=O_C0 direct-sum V_e, we therefore obtain the exact criterion

H0(I_e(4))_+ = ker[ K20 -> H0(V_e(4))_+ ],

where the displayed map is actual restriction to the Ext-annihilator vertex module. No evaluation of that map is performed. This is a finite-dimensional geometric reduction of the preserving-excess question.

The known vertex defect enters through the long exact sheaf Ext sequence of 0->J->S(2)->T_L->0 on X minus C0. Its relevant exact segment is

sheaf Ext^1(S(2),S) -> V_e -> sheaf Ext^2(T_L,S)
    -> sheaf Ext^2(S(2),S).

Both outer terms must be retained: the spinor is not locally free at L. The rank-seven pushforward and Hilbert polynomial of T_L alone do not determine this Ext segment or the actual restriction map K20 -> H0(V_e(4))_+. No unjustified equality V_e=T_L is made.

## 4. Non-preserving maps have a separate exact two-stage obstruction

To retain all positive noncommuting adjoints, not merely the preserving part, define the lower off-diagonal component of phi by

r=p(4) phi i in Hom_X(S,J(4)).

The candidate sheaf Hom(S,J(4)) is exactly the kernel of the actual map

O_X(6)=Hom(S,S(6)) -> Hom(S,T(4)).

For a global candidate r, the first necessary and sufficient condition to extend it to a map q:E -> J(4) is that the connecting class vanish:

r_* e = 0 in Ext^1_X(J,J(4)).

This follows by applying Hom(-,J(4)) to 0->S->E->J->0. If it vanishes, the possible q form a torsor under Hom(J,J(4))=H0(O_X(4)). A chosen q lifts through E(4)->J(4) to an endomorphism phi:E->E(4) exactly when

q^* e(4)=0 in Ext^1_X(E,S(4)).

Thus r is actually realized exactly when the first obstruction vanishes and some allowed q has vanishing second obstruction. The ambiguity in q is not discarded. Any resulting phi can be made tracefree by subtracting half its trace times the identity, without changing r. All constructions are equivariant, so the same criteria apply to even r and even lifts by averaging with the involution.

Consequently rank33 is equivalent to BOTH: the K20 vertex gate is injective, and no nonzero even r survives this exact two-stage lifting test. This is a precise Hom/Ext reduction, not a proof of either vanishing. The canonical eight-dimensional centralizer is already accounted for by the left term in Section 2.

## Verification and scope

The spinor filtration, reduced conic, vertex support, and rank-seven pushforward are read from the four existing cone notes. The new arguments use exact extension-morphism compatibility, reflexive Hom extension, and the actual annihilator of the extension class. The companion verify_cone_ext_vertex_gate.py checks the universal twenty-dimensional source character and degree counts. No actual coefficients, selected ranks, experiments, or external writes occur.
