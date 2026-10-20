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

## 2. All twenty diagonal characters

Use the exact diagonal chain lifts from [diagonal classification](https://github.com/Akilleez-QA/read-em-and-weep/blob/97190240fa87b8ed68f2a90f701bda0e7236f0e7/research/hm/cubic-loci/foundation-p02/DIAGONAL.md), §§4,6. Put s_i=αⁱβⁱ² with α⁵=β⁵=1 and w_i=(i,i²) in F₅². Set κ_U=4, κ_V=1, κ_Z=0 and κ_+=2, κ_−=3. The degree-zero chain factor on a type-T coordinate with index i has character 3w_i+(0,κ_T); the degree-two chain factor on output plane p has character (0,κ_p).

Use the cochain action f(v)↦T⁻¹ f(Sv)T, with the prescribed O(−2) twist linearization. On a constant B-entry its character is source minus target:

    3w_i+(0,κ_T−κ_p).

There is no additional factor from substituting variables into a constant entry. Write a=3i. Since 2a²=3i² in F₅, the six offsets δ=κ_T−κ_p, in order (+U,−U,+V,−V,+Z,−Z), are

    (2,1,4,3,3,2).

For each a, offsets 2 and 3 therefore occur twice, while offsets 1 and 4 occur once. The derivative class D_i has character −w_i: differentiate the chain identity T d(v)=d(Sv)T. An exterior pair has character −w_i−w_j. With a=−i−j and h=i−j, its second coordinate is

    −i²−j²=2a²+2h².

An unordered distinct pair has h²=1 or 4, giving offsets 2 or 3. For each a there is exactly one unordered pair for each choice h², since 2 is invertible in F₅. Thus the ten relations remove exactly one copy of offset 2 and one copy of offset 3 for each a. The quotient has all twenty distinct characters

    (a,2a²+δ),   a∈F₅, δ∈{1,2,3,4}.

The concrete twenty classes at the end of §1 realize these four offsets once each. This is an abstract character decomposition for the diagonalizable group scheme μ₅²; over a splitting field these are ordinary eigencharacters. It is not the evaluation of any selected roots of unity or a polynomial instance.

## 3. Reversal and a concrete positive basis

For reversal π(i)=4−i, the degree-zero coefficient lift permutes U,V,Z indices with sign +1, while the degree-two lift is −I₂. Hence the action on the B coordinates is minus the index permutation, with no exchange of output planes or row types. The quotient relations respect this action.

The chosen quotient basis of §1 is stable under reversal with the same minus sign. Its fixed index is i=2, giving four negative fixed classes. The other four indices form two pairs, {0,4} and {1,3}, for each of the four chosen types. Thus the eight differences

    [E_{p,T,i}]−[E_{p,T,4−i}],
    (p,T)∈{(+,U),(−,U),(+,V),(−,V)}, i∈{0,1},

form an explicit positive basis of H²(End H(−2)). Here E denotes an elementary B-entry accompanied by its unique closed A-block. The corresponding sums and the four fixed-index classes are negative, giving twelve negative dimensions.

On the character labels this reversal sends (a,δ) to (2−a,δ): a=3i becomes 3(4−i)=2−a, and the offset remains unchanged. The four fixed character lines have a=1 and are negative. The remaining sixteen lines form eight exchanged pairs. This proves the same positive dimension eight without confusing fixed character lines with invariant vectors.

## 4. Limits

These are formal coefficient and representation statements for the exact literal presentation. They provide explicit target coordinates and relations, not a construction or evaluation of a Massey defining system, not an identification with an independently occurring thirty-dimensional space, and not detector values.
