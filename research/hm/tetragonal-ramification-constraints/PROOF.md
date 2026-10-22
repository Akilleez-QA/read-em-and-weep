# Exact five-torsion and the two ramification orbits of the Gram tetragonal curve

Status: mathematical proof conditional on the pinned inputs, independently reviewed in REVIEW.md; not formally checked by a proof assistant. All arguments are uniform representation theory and curve geometry over C. No selected source coefficient, point, matrix or rank is evaluated.

## Inputs and conventions

Use the smooth genus-nine Gram curve C of [PR656, commit 561f4cf5e4ad23a9f384936816d7a6ef0bd07dd6](https://github.com/Akilleez-QA/read-em-and-weep/blob/561f4cf5e4ad23a9f384936816d7a6ef0bd07dd6/research/hm/tetragonal-canonical-model/PROOF.md). Its actual equations are b(v,v)=b(v,Mv)=0. Here V=Sym^2 W', b is invariant, and M is the equivariant actual Gram operator from [PR654, commit f0c94ff7979652c094da3efaa11fea4629dbf59a](https://github.com/Akilleez-QA/read-em-and-weep/blob/f0c94ff7979652c094da3efaa11fea4629dbf59a/research/hm/gram-spectral-geometry/PROOF.md). The fixed conic in P(V) is the Veronese P(W'). Therefore C is the smooth invariant divisor of bidegree (4,4) on P(W') times P(W), with both projections p_i of degree four and canonical line O_C(2,2). The representations W,W' are the two inequivalent two-dimensional representations of G=SL_2(F_5). Write L_1=O_C(1,0), L_2=O_C(0,1), and T=L_1 tensor L_2^{-1}.

Equivariance of M and invariance of b give an actual diagonal A5 action, not just an action on numerical data. It is faithful since p_2 is surjective and equivariant for the faithful action on P(W). The equation of C is invariant: its one-dimensional span is G-stable and G has no nontrivial characters. Likewise all linearizations below use the natural G-actions. On O(1,-1) the central involution acts trivially, so T is honestly A5-linearized.

## 1. The two twelve-point triple-ramification orbits

A cyclic subgroup of order five in A5 has two fixed points in each projective line. For an order-ten lift choose a primitive tenth root alpha so that the tautological weights on W are v=+1,-1, and those on W' are u=+3,-3. At one of the four fixed pairs, the fiber of O(4,4) has weight -4(u+v) modulo ten. These four weights are nonzero. An invariant section must therefore vanish at every fixed pair: all four lie on C.

The tangent weights on the ambient surface are -2u and -2v. The differential of the defining section at a zero is equivariant into its fiber. Exactly one of these tangent weights equals -4(u+v). For example, at (u,v)=(3,1), the differential can only be nonzero on the first tangent factor; at (3,-1), only on the second. Simultaneous sign reversal gives the other cases. Smoothness ensures the allowed derivative is nonzero. Thus the tangent to C is one factor, one projection is unramified and the other is ramified.

At (3,1), the tangent to C has weight -2v, while the tangent of the first projection's target has weight -2u. If its local degree is e, equivariance implies e v=u modulo five, so e=3 modulo five. Since the projection has degree four, e=3 exactly. At (3,-1), the analogous congruence e u=v modulo five again gives e=3. This is a uniform stabilizer-weight argument, not evaluation at a selected actual point.

There are six order-five subgroups of A5. Their fixed pairs are disjoint: any stabilizer of a point in a faithful finite group action on a smooth complex curve is cyclic (it injects into the tangent character), and A5 has no cyclic group containing two distinct subgroups of order five. Consequently there are exactly twenty-four points with C5 stabilizer, twelve ramified for each projection. Let R_i be the reduced divisor of the twelve points ramified for p_i. They are disjoint, each is a single A5 orbit, and

    Ram(p_i)=2R_i.

Indeed the displayed points already contribute 24, equal to the full ramification degree 2g(C)-2+2deg(p_i)=16+8=24.

Let Omega_i be the twelve-point orbit in the ith target. Over every point of Omega_i, the fixed pairs supply one triple point of R_i and one unramified point of R_j, exhausting degree four. Hence, as actual divisors,

    p_1^*Omega_1=3R_1+R_2,
    p_2^*Omega_2=R_1+3R_2.

## 2. Quotient signature and a first torsion bound

The twenty-four C5 points contribute 24(5-1)=96 to Riemann--Hurwitz for C->C/A5. The only other possible nontrivial stabilizers are C2 or C3, contributing respectively 30 or 40 per orbit. If a,b count these orbits and q is the quotient genus, then

    16=60(2q-2)+96+30a+40b,
    30a+40b=40-120q.

Nonnegativity gives q=0, and the only solution is a=0,b=1. Thus C/A5 has signature (3,5,5): two twelve-point C5 orbits and one twenty-point C3 orbit, with no C2 fixed points.

In additive Picard notation the fiber identities give

    12(L_1-L_2)=2(R_1-R_2).

Riemann--Hurwitz for the two tetragonal projections gives

    2R_i=K_C+2L_i,
    2(R_1-R_2)=2(L_1-L_2).

Therefore 10T=0. This bound alone would not distinguish order five from order ten; the next argument does.

## 3. Equivariant cohomology forces exact order five

The divisor sequence twisted by O(1,-1) is

    0 -> O(-3,-5) -> O(1,-1) -> T -> 0.

Both ambient H^0 groups vanish and H^1(O(-3,-5))=0 by Kunneth, since each potential summand contains H^0 of a negative-degree line on P1. Hence H^0(C,T)=0, and T is nontrivial.

For its fifth power the sequence is

    0 -> O(1,-9) -> O(5,-5) -> T^5 -> 0.

Again both ambient H^0 groups vanish. Equivariant Serre duality on the second P1 and Kunneth give, using self-duality of these representations,

    H^1(O(1,-9)) = W' tensor Sym^7 W,
    H^1(O(5,-5)) = Sym^5 W' tensor Sym^3 W.

The relevant binary-icosahedral representation identities are

    Sym^7 W = W' plus U_6,
    Sym^5 W = Sym^5 W' = U_6,
    Sym^3 W = U_4,

where U_6 and U_4 are irreducible and inequivalent. Thus the first H^1 space has exactly one invariant and the second has none. Taking invariants is exact in characteristic zero. The cohomology sequence therefore gives dim H^0(C,T^5)^G=1, independent of the multiplication map defined by the actual equation of C. A degree-zero line bundle on a smooth connected projective curve with a nonzero section is trivial: its effective zero divisor has degree zero. Hence T^5 is trivial. Combined with T nontrivial, this proves

    O_C(1,-1) has exact order five in Pic^0(C).

For reproducibility, these representation identities can be verified solely by characters. For SU2 trace t the character chi_n of Sym^n satisfies chi_0=1, chi_1=t, chi_{n+1}=t chi_n-chi_{n-1}. On the positive trace classes t=2,0,1,phi,phi^{-1}, chi_5 is (6,0,0,-1,1) and chi_3 is (4,0,-1,1,-1); negative lifts change signs for odd powers. Their character norms are one and their inner product is zero. Replacing W by W' swaps phi with -phi^{-1}, and phi^{-1} with -phi; chi_5 is unchanged, while chi_7-chi_5 is exactly the character of W'. These checks involve only abstract conjugacy classes, never values of the actual Gram operator.

## 4. A connected cyclic five-cover and its quotient signature

The exact torsion order produces the connected etale cyclic cover

    r:Z=Spec_C(O_C plus T^{-1} plus ... plus T^{-4})->C,

using a nowhere-zero trivializing section of T^5. This section is invariant: its one-dimensional space carries a character of A5, which must be trivial. Therefore the A5-linearization of T acts on the entire cover algebra, commuting with its deck group C5. It gives an honest A5 times C5 action on Z. Connectedness follows from exact order five, or from H^0(C,T^{-j})=0 for j=1,...,4. Etale Riemann--Hurwitz gives g(Z)=5(9-1)+1=41.

At a C5 fixed pair the T-fiber character has weight -u+v, one of +2,-2,+4,-4 modulo ten, so is a nontrivial fifth root of unity. Thus the chosen lifted A5 has no C5 fixed point on Z. At a C3 fixed point downstairs, the T-fiber character has cube one, and its fifth power is one by the invariant trivialization of T^5. It is consequently trivial. Each of the twenty C3 points has five fixed lifts. No other nontrivial A5 stabilizers occur.

The lifted A5 action thus has one hundred C3 points and no C2 or C5 points. For its quotient genus q_Z,

    80=60(2q_Z-2)+100(3-1),

so q_Z=0. The hundred points form five orbits of size twenty. Consequently Z/A5 is P1 and the signature of Z->Z/A5 is (3,3,3,3,3).

## Contribution and boundaries

The actual genus-nine Gram model has two distinguished disjoint triple-ramification orbits and A5 quotient signature (3,5,5). Its two tetragonal pencils differ by exact five-torsion, strengthening the geometric ten-torsion bound without any coefficient calculation. That class gives a connected genus-forty-one etale five-cover with an honest commuting A5 action and quotient signature (3,3,3,3,3).

This T on C is distinct from the spectral two-torsion line on the genus-ten curve in PR654. Nothing here evaluates the actual R-class, its quotient by a second-symbol image, the third Bockstein, any selected HM/source instance, or an algebraicity obstruction. Those dependencies remain separate.
