# Exact third elliptic pushforward from rational cyclic-cover cohomology

## Result

For the actual modular surface S=S(5), with C the sum of its twenty-five disjoint five-torsion sections and O(C)=O(5I),

 E_3=q_*O_S(3I)=O_P1(-5)^5 directsum O_P1(-3)^10.

Equivalently,

 h0(S,3I+3F)=10,   h1(S,3I+3F)=5.

This resolves the two previously possible splitting types. The proof is an exact Hodge-theoretic argument on a smooth cyclic cover, not a vanishing assertion on the contraction of C.

## 1. The smooth cyclic cover and its eigenspaces

Form the cyclic cover rho:B->S associated to the line bundle O(I) and the section of O(5I) with reduced zero divisor C. It is finite of degree five and

 rho_*O_B = directsum_(j=0)^4 O_S(-jI).

Each component of C is smooth and the components are disjoint. Locally the cover is z^5=x at a branch point, hence smooth. Away from C it is etale. It is connected: the branch valuation is one, so the defining section is not a fifth power in the function field; equivalently the local branching has the full cyclic monodromy of order five. The resulting B is a smooth projective surface with a deck automorphism sigma of order five.

Choose a primitive fifth root zeta. Up to reversing the generator convention, H1(S,O(-jI)) is the zeta^j eigenspace of H1(B,O_B). Write its dimension as a_j. The following argument is unchanged by that reversal.

## 2. Four known dimensions

The surface has K_S=3F and chi(O_S)=5. For positive j, H0(O(-jI))=0 by intersection with the nef fiber. Riemann–Roch and Serre duality give

 chi(O(-jI))=5+5j(3-j)/2,
 a_j=h0(S,jI+3F)-chi(O(-jI)).

Also a_0=q(S)=0. The already established pushforward splittings imply:

 j=1: E_1=O(-2)^5, so h0(I+3F)=10 and a_1=0.
 j=2: either E_2=O(-2)^5+O(-4)^5 or E_2=O(-3)^10;
       both give h0(2I+3F)=10, so a_2=0.
 j=4: E_4=O(-5)^5+O(-4)^15, so h0(4I+3F)=0;
       chi(O(-4I))=-5, hence a_4=5.

For j=3 one has chi(O(-3I))=5, and a_3 is the remaining unknown.

## 3. Rationality forces the missing eigenspace

The deck automorphism acts on the rational vector space H1(B,Q). Since its order is five, its characteristic polynomial is a product of powers of X-1 and the irreducible cyclotomic polynomial

 Phi_5(X)=X^4+X^3+X^2+X+1.

Therefore its four nontrivial complex eigenvalues all have the same multiplicity in H1(B,C).

Hodge decomposition is sigma-equivariant. Complex conjugation identifies the zeta^j eigenspace in H^(1,0) with the conjugate of the zeta^(-j) eigenspace in H^(0,1). Thus the multiplicity of zeta^j in H1(B,C) is

 a_j+a_(5-j).

For j=1 this is a_1+a_4=5. For j=2 it is a_2+a_3=a_3. Equality of these multiplicities proves a_3=5. Consequently

 h0(S,3I+3F)=a_3+5=10.

The two splitting alternatives for E_3 follow from its rank fifteen, degree minus55, fivefold Heisenberg multiplicities, and vanishing H0(3I+2F):

 O(-5)^5+O(-3)^10, or O(-4)^10+O(-3)^5.

After twisting by O(3), these have ten and five sections respectively. The first is therefore the actual splitting. It also gives h1(3I+3F)=5 directly, with h2=0.

As a check, q(B)=sum a_j=10. The cyclic pushforward gives chi(O_B)=25, hence p_g(B)=34. These are consequences, not inputs to the proof.

## 4. Immediate corrections to the exact trace and kernel presentations

The structure-sheaf summand in the third-twist cusp-jet kernel is now explicitly

 E_3(6)=O(1)^5 directsum O(3)^10.

Thus the previous exact third-twist presentation remains valid with this known direct summand, without resolving the separate trace-free elementary-transform splitting.

The normalization-side bundle E_3^dual(-7), if used in the twist-four elementary presentation, is now exactly

 O(-2)^5 directsum O(-4)^10,

rather than one of two possibilities. This is rank fifteen, degree minus50 and has h1=35. Its fifty-point elementary modification has degree minus100 as before. This fixes a source splitting, not the rank of the remaining connecting map.

## Sources and scope

The primary modular inputs and the relation C=5I are supplied by BHM, 'Shioda's Modular Surface S(5) and the Horrocks–Mumford Bundle', Sections4.2–4.4, with the project normalization pinned at PR570 e5e55594ef2b99cefb81c4c02b22cb45e1ff0025. The E1/E2/E4 deductions are written out in ELLIPTIC-PUSHFORWARD-SPLITTING.md and the first trace-twist note at 41ab0df75f47e8979fdc06d9357c1c495dd0e1a4. Hirzebruch's 'Arrangements of Lines and Algebraic Surfaces', Section3.2, printed page134, independently describes this cyclic five-cover and contraction of the twenty-five exceptional branch curves:
https://hirzebruch.mpim-bonn.mpg.de/244/1/hirzebrucharr.pdf

No numerical irregularity of the cyclic cover is imported from the literature; it is proved above from rational cohomology. No identification of 3(I+F) with the dualizing sheaf of a singular contraction is used, and no selected coefficients or rank experiments occur.
