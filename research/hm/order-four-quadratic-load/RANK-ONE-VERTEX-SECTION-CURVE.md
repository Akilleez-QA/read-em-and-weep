# Conditional rank-one vertex evaluation forces a nonreduced sextic curve

## Theorem and hypothesis

Let H=P3 be an actual inversion-invariant HM hyperplane through the positive plane, let p be its negative vertex, and put E=F_H(2). The established actual inputs are

    det E=O_H(3),   c2(E)=6,
    h0(E)=2,       H0(E(-1))=0.

The two sections are inversion-even, and their nonzero determinant is the cubic cone c3 through p. The fiber E_p has one positive and one negative eigendirection, and affine coordinates centered at p are inversion-odd.

ASSUME that evaluation H0(E)->E_p has rank one. Let s be the nonzero section, unique up to scalar, whose value at p is zero, and let C=Z(s). Then:

1. C is a pure locally complete-intersection curve of degree six, with omega_C=O_C(-1) and arithmetic genus -2.
2. Its multiplicity at p is exactly six. In equivariant local coordinates its tangent cone has ideal (f2,c3), where f2 is a nonzero quadratic relatively prime to c3. Thus the tangent cone is a complete intersection of degrees two and three.
3. The reduced support of C is a union of lines through p. The curve C itself is necessarily nonreduced. It is not asserted to be a scheme-theoretic cone.
4. H0(O_C) has dimension three and H1(O_C)=0. Its global nilpotent ideal has dimension exactly two, and its algebra is isomorphic either to C[t]/(t^3) or to C[x,y]/(x,y)^2.
5. H0(I_C(2))=0 and h0(I_C(3))=1. The unique containing cubic is the actual determinant cone.

These consequences do not contradict the rank-one hypothesis and do not prove that vertex evaluation has rank zero.

## 1. The local parity presentation

Choose a second global section s0 with nonzero value at p. In an inversion-equivariant local frame with fiber signs positive and negative, write

    s0=(a,b),       s=(f,g).

Here a is an even unit, b is odd, f is even with f(p)=0, and g is odd. Replacing the positive local frame vector by s0 changes the expression for s to

    (f/a, g-bf/a).

The second component is the determinant of s0 and s divided by the even unit a. The determinant cone has the exact homogeneous cubic equation c3 in the odd affine coordinates. A change of determinant trivialization only multiplies it by a unit. Therefore

    I_(C,p)=(h,c3),       h even, ord_p(h)>=2.         (1)

This is a change of bundle frame, not replacement of the global section by a locally varying linear combination. Both components remain in the zero ideal. Regularity below ensures h is not identically zero in the local ring.

## 2. Regularity, degree and duality

A divisorial zero of a nonzero section of E would divide out to a section of E(-d) for an integer d>=1. Multiplying by a nonzero form of degree d-1 would give a nonzero section of E(-1), contrary to the actual vanishing. Thus s has no divisorial zero.

Its two local equations consequently form a regular sequence wherever they vanish. Since p is a zero, its zero scheme is a nonempty pure codimension-two locally complete-intersection curve. The second Chern class gives degree six. Adjunction gives

    omega_C=(omega_H tensor det E)|C=O_C(-1).

Duality and Riemann-Roch for a projective Gorenstein curve give

    2p_a(C)-2=deg omega_C=-6,

so p_a(C)=-2 and chi(O_C)=3. None of these calculations assumes reducedness or connectedness.

## 3. Multiplicity and the exact tangent cone

Choose a general linear parameter ell through p. Since C is Cohen-Macaulay of dimension one, this parameter computes its multiplicity:

    e_p(C)=length O_(H,p)/(h,c3,ell).

For a general choice, restriction to the plane ell=0 preserves the orders of h and c3. The plane local Bezout inequality gives

    e_p(C)>=3 ord_p(h)>=6.

On the other hand, a general projective plane through p meets C properly with total intersection length deg C=6, so e_p(C)<=6. All inequalities are equalities. In particular ord_p(h)=2.

Equality in local Bezout says the two initial plane forms are relatively prime. If h2 and c3 had a common homogeneous factor in the three-dimensional tangent space, its restriction to a general plane would remain a common positive-degree factor, contradicting that equality. Hence h2 and c3 are relatively prime.

Their initial forms are thus a regular sequence. The initial-regular-sequence criterion, or the elementary cancellation of leading syzygies using their Koszul relation, yields

    gr_m O_(C,p)=C[x1,x2,x3]/(h2,c3).                 (2)

This proves the exact tangent-cone assertion, not merely an inequality of multiplicities. Its projectivization is a length-six complete intersection in P2.

## 4. What multiplicity equal to degree actually implies

Let C_i be the reduced irreducible support components, with generic lengths n_i. Purity gives the degree and multiplicity associativity formulas

    deg C=sum_i n_i deg C_i,
    e_p(C)=sum_(p in C_i) n_i e_p(C_i).

For each reduced irreducible projective curve, e_p(C_i)<=deg C_i. Since both displayed sums equal six, every component passes through p and has e_p(C_i)=deg C_i.

For a REDUCED irreducible curve, this equality forces it to be a line through p. One proof blows up p: the degree of the projection-from-p linear system on its strict transform is deg C_i-e_p(C_i). Degree zero makes the projection constant, so the original curve lies in one line through p.

It follows that the support of C is a connected union of such lines. This conclusion is only about the reduced support. Nonreduced structures on those lines need not be invariant under radial scaling, and the assertion that C itself is a cone is neither used nor proved.

If C were reduced, connectedness would give h0(O_C)=1 and p_a(C)=h1(O_C)>=0, contradicting p_a(C)=-2. Thus C is nonreduced. Since it is Cohen-Macaulay, it cannot be generically reduced with nonreduced structure supported only at isolated points. At least one n_i is therefore greater than one, and there are at most five distinct supporting lines.

In particular, the length-six projectivized tangent cone in (2) is not six reduced distinct points. This is a necessary degeneracy of the tangent-direction intersection, not a choice of its quadratic equation.

## 5. The exact global section algebra from the actual monad

The normalized HM monad has terms

    5O(-1),    2 Omega^2(2),    5O

on P4. After twist -1 all terms are acyclic. After twist -2 only the middle term contributes, with H2(Omega^2)=C. Therefore

    H*(F(-1))=0,
    H^i(F(-2))=0 for i!=2,      h2(F(-2))=2.

These actual primary groups and their Bott derivation are also recorded in LOWER-TWIST-EVEN-QUADRIC-PARITY.md, Section 2. Hyperplane restriction gives

    H^i(F_H(-1))=0 for i!=1,    h1(F_H(-1))=2.

The Koszul sequence of any regular section of E is

    0 -> O_H(-3) -> E* = F_H(-1) -> I_C -> 0.

The first term is acyclic on P3. Hence I_C has precisely two-dimensional H1 and no other cohomology. The ideal sequence then gives

    h0(O_C)=3,       h1(O_C)=0.                       (3)

For the conditional vertex curve, connectedness of the support makes this finite-dimensional section algebra local, with residue field C. Its maximal ideal is its nilradical and has dimension two. A length-three local complex algebra has either one generator with nonzero square, giving C[t]/(t^3), or two generators and square-zero maximal ideal, giving C[x,y]/(x,y)^2. No choice between these two algebras follows here.

## 6. The unique cubic and the absence of a quadric

The section sequence is

    0 -> O_H -> E -> I_C(3) -> 0.

Since h0(E)=2 and H1(O_H)=0, it gives h0(I_C(3))=1. The determinant with s0 is a nonzero member of this one-space, so the unique containing cubic is exactly the actual cone.

Twisting once down, the vanishing H0(E(-1))=0 and H1(O_H(-1))=0 give

    H0(I_C(2))=0.

Thus the quadric in the tangent-cone ideal is not a global containing quadric for the nonreduced curve. This makes explicit why replacing the actual curve by its homogeneous tangent cone would be invalid.

## 7. A safe corollary for reduced section curves

Statement (3) holds for every regular section, without the vertex-rank hypothesis. If its zero curve is reduced, it has exactly three connected components, each of arithmetic genus zero. Adjunction restricts to each disjoint component; hence 2p_a-2=-degree forces each component to have degree two. Each is therefore a plane conic, possibly a pair of intersecting lines, not necessarily smooth.

Their three planes are distinct, since two disjoint degree-two plane curves cannot lie in the same plane. The product of the three plane equations is a cubic containing C. Uniqueness of that cubic forces the actual determinant cone to be the product of these three distinct planes. Equivalently, its plane base cubic is three distinct lines.

Consequently, whenever the actual determinant base cubic is not three distinct lines, every nonzero section of E has a nonreduced zero scheme. This is a conditional geometric consequence; it asserts neither existence of a reduced section nor generic smoothness of three conics.

## Scope

INVARIANT-HYPERPLANE-DETERMINANT-CUBIC-CONES.md supplies the section dimensions and determinant cone. NEGATIVE-VERTEX-EVALUATION-SCALAR.md, Section 1, supplies the actual split F|L=O(3)_- directsum O(-4)_+ and hence the one-positive/one-negative vertex fiber; this is used only for (1). Its source pins are BETA-IMAGE-DIMENSION-DROP at f5b50172bd65d1772d1af3d4a511decc8363183e, ALPHA-EXCLUSION at 212f18bb3afb52171068d1aaf8a0dbfbf9954d2b, and PR541 at 9ce30d8d783da881be68548d158ebcb48e122850, Section 3. The monad supplies the exact cohomology in Section 5. The proof is independent of newly announced primary conductor claims and does not settle the vertex evaluation scalar. No selected HM coefficients, evaluated actual matrices or ranks, scans, or experiments are used.
