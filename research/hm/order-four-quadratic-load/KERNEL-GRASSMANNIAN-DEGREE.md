# The kernel map has degree one hundred

## Inputs and scope

Let C be the disjoint union of the twenty-five evaluation lines in P4. The six maximal evaluation minors generate I_C(5) scheme-theoretically. Let Y=Bl_C(P4), H the pulled-back hyperplane and E_i its exceptional divisors. Thus the six minors give a basepoint-free morphism g:Y -> Gr(2,U) inside P5, with Plucker line bundle

    D=5H-sum E_i.

The Grassmannian parametrizes the projective kernel lines in P(U*). No selected source evaluation or numerical rank experiment is used below.

## 1. Intersection computation with signs fixed

For a line C_i, its normal bundle is O_P1(1)^3. Consequently E_i is P1 x P2. Write h and t for the respective hyperplane classes. The normal line of E_i in Y is the tautological subline of that normal bundle, hence

    H|E_i=h,     E_i|E_i=h-t.

This directly yields H E_i^3=1 and E_i^4=3. The intersections H^3 E_i and H^2 E_i^2 vanish. Exceptional divisors from different lines are disjoint. Therefore

    D^4=5^4-4*5*25+3*25=200.

Since D is the pullback of an ample line bundle, a morphism with image dimension below four would have D^4=0. Hence g is dominant onto the four-dimensional Grassmannian and generically finite. The Plucker degree of Gr(2,4) is two, so the projection formula gives

    deg(g)=100.

## 2. Every exceptional divisor dominates the Gamma Chow divisor

Let Gamma be the smooth rational sextic traced by the evaluation images along C. Its Chow divisor T in Gr consists of lines meeting Gamma. Its class is 6 times the Plucker class, and its degree in P5 is 12.

The exceptional fiber P2 over p in C_i parametrizes the transverse normal directions. The local evaluation normal form shows that g maps this P2 isomorphically onto the family of lines through κ(p) in P(U*). Since κ:C_i -> Gamma is an isomorphism and a general line meeting Gamma meets it at exactly one point, E_i -> T is birational. This agrees with the independent intersection calculation

    D|E_i=4h+t,     D^3 E_i=12.

In particular T is NOT a divisor whose inverse image can be treated as an automatically reduced proper transform: all twenty-five E_i are already components of g^*T.

## 3. Multiplicity constraint and what remains open

Heisenberg symmetry makes the generic multiplicity e of E_i in g^*T independent of i. Since E_i -> T has degree one, projection of cycles gives

    100 = 25 e + sum_j m_j deg(Z_j -> T),

where the sum runs over other components dominating T. Components mapping to lower-dimensional subsets do not contribute. Thus 1 <= e <= 4. In characteristic zero e is also the generic ramification index along E_i.

If P is the degree-thirty polynomial obtained by substituting the six quintic minors in the degree-six Chow equation, then on the blowup

    div(P)=g^*T+6 sum E_i.

Therefore P vanishes to order 6+e along the generic point of every C_i. In particular its order is between seven and ten, not merely six. The polynomial is nonzero because g is dominant and T is a proper divisor.

Neither g's dominance nor generic etaleness proves that the non-exceptional Gamma-incidence component dominates T. Consequently this note does not assert e=2, that the off-C Chow hypersurface is reduced, that its degree is thirty as a reduced hypersurface, or that the canonical incidence map is birational onto that reduced hypersurface. Those conclusions require additional local ramification or component-degree information.
