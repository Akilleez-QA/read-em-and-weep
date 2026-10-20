# Historical independent audit: explicit quotient continuation

The complete relevant original audit sections 6–8 follow. Sections 6–7 retain the limitations and explicit projection prerequisite needed by section 8. This is an audit of the mathematical coefficient/character statements, not a certificate of a geometric obstruction value.

## 6. Canonicity and limitations

The edge sequence and kernel are canonical relative to the specified complex, twist, and symmetry linearization. The derivative generators use its chosen homogeneous linear presentation; under a constant coordinate/basis change they transform naturally. The kernel itself is intrinsically the kernel of that presentation's edge map. No splitting of the edge sequence is supplied or canonical in general.

The 30-dimensional global-Hom kernel has the same inversion eigendimensions as the retained multiplicity space M in the earlier inversion proof. This numerical agreement alone does not give a canonical identification, or any particular identification, of their geometric constructions. Likewise the quotient's eight-dimensional positive part cannot automatically be declared an eight-dimensional remaining actual-source obstruction target. Such a claim requires a separately proved comparison map carrying the relevant class and the derivative-product subspace to the intended target. Neither product vanishing nor a spectral-sequence transgression proves that the actual source class lies in, or is killed by, that subspace.

Subject to these boundaries, all requested degree, sign, twist, edge-map, independence, dimension, and equivariant-quotient claims pass the independent audit.

## 7. Explicit projection to the last block

The additional coefficient lemma also passes. A constant degree-two map has precisely two blocks A:C_{−1}→C_1 and B:C_0→C_2. Its closure equation is

ev(v)A−Bγ(v)=0.

There are no other degree-three blocks. Since C_1=(V*)² and ev(v) is paired evaluation, the map

A ↦ ev(v)A

is the tensor-coefficient isomorphism from Hom(C_{−1},(V*)²) to Hom(C_{−1},k²)⊗H⁰(O(1)). Thus every B gives a unique A satisfying closure. Projection to B supplies an explicit isomorphism

Z²_global ≅ Hom(C_0,C_2).

It is equivariant because the established chain action preserves the two blocks and the closure equation. Its trace is therefore directly 3·(−2)=−6, and its dimension is directly 15·2=30. This is an abstract coefficient identification, not a rank calculation. Under it the derivative relations are exactly B_ab=r_aδ_b, so their independently checked injection gives the explicit quotient Hom(C_0,C_2)/⟨r_aδ_b⟩.

The main derivative-transgression PROOF.md was subsequently read and agrees with the audited theorem, including the distinction between globally constant maps and hypercohomological primitives. Its reference to the separate weight-two Massey theorem is a dependency, not an independently re-audited Massey computation here.

## 8. Full audit of the explicit coefficient quotient

The subsequently available [explicit coefficient note](EXPLICIT-COEFFICIENT-QUOTIENT.md) was read in full, together with the diagonal and monomial symmetry proofs supplying its lifts. Its twenty quotient classes, diagonal weights, and eight positive differences all pass.

For clarity, denote an elementary B-entry by E_{p,T,i}. A bivector coefficient on the oriented pair (i+2,i+3) occurs in precisely the U_i plus component and the Z_i minus component, with the same contraction and evaluation sign. Its relation is therefore a nonzero scalar multiple of

R_i^U = E_{+,U,i}+E_{−,Z,i}.

The oriented pair (i+1,i+4) similarly gives

R_i^V = E_{−,V,i}+E_{+,Z,i}.

Changing from a displayed cyclic orientation to a<b changes the common sign of the entire corresponding relation, never its relative sign. These ten pairs of positions are disjoint, and their Z projections form the elementary basis of the ten-dimensional Z-entry space. Hence the twenty U/V elementary classes are independent and spanning in the quotient. Equivalently every class has exactly one representative with all Z entries zero. The four surviving coefficient coordinates for each i are explicitly

(B_{+,U_i}−B_{−,Z_i}, B_{−,U_i}, B_{+,V_i}, B_{−,V_i}−B_{+,Z_i}).

These are quotient coordinates; the original U/V entries alone would not define functions on arbitrary representatives with nonzero Z entries. The note correctly presents U/V elementary classes as a basis rather than making that mistaken stronger assertion.

For the diagonal action, normalize the common scale and chain scalar to c=t=1 in the cited diagonal proof. Its degree-zero weights are 3w_i+(0,4), 3w_i+(0,1), 3w_i, and its degree-two weights are (0,2),(0,3). Conjugation T⁻¹f(Sv)T gives source minus target on constant entries. The six resulting offsets are exactly (2,1,4,3,3,2) in the note's order. Since a=3i implies 2a²=3i² in F₅, the twenty selected U/V classes have, once each, the characters

(a,2a²+δ), with a∈F₅ and δ∈{1,2,3,4}.

One can check the matching relation characters directly, without counting exterior pairs. For the U relation the derivative-pair weight is

−w_{i+2}−w_{i+3} = (3i,3i²+2),

which equals the weights of both E_{+,U,i} and E_{−,Z,i}. For the V relation it is

−w_{i+1}−w_{i+4} = (3i,3i²+3),

which equals the weights of both E_{−,V,i} and E_{+,Z,i}. Thus the diagonal identification respects each individual relation, including its index, rather than merely matching total multiplicities. Alternatively, the note's formula −i²−j²=2a²+2h² for a=−i−j and h=i−j is correct, and the two possible nonzero square classes h²=1,4 give offsets 2,3.

For reversal, the coefficient lifts from the monomial proof give T_0=M_π with π(i)=4−i and T_2=−I₂. Therefore T_2⁻¹BT_0 sends each elementary B-entry to minus the same type and plane at index π(i). There is no hidden exchange of U and V or of the two output planes. The relation subspace and the chosen Z-zero complement are both stable. The fixed index i=2 contributes four negative basis vectors; the two index pairs {0,4} and {1,3}, for each of four types, contribute one positive difference and one negative sum. This proves the stated eight positive differences are genuinely independent cohomology classes and span the positive eigenspace. The twelve specified negative vectors similarly form its negative basis.

Finally a=3i transforms to 3(4−i)=2−a and δ remains fixed because the type and output plane remain fixed. Thus the character labels in the note transform exactly as claimed. This is an affine permutation of the displayed labels; no unproved assertion of an untwisted linear semidirect-product character action is needed. In particular a=1 labels precisely the four negative fixed character lines.

The full explicit coefficient supplement therefore requires no correction. All statements remain relative to the fixed presentation and prescribed twist linearizations and retain the limitations in section 6 above.
