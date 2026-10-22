# The unique fourth channel invisible to square restriction and six axis fibers

## Scope and inputs

Work over C. Put G=SL2(F5), with even irreducibles A (dimension3), V (the other3), P4 and D5. On P(A), let Delta be the invariant discriminant conic, with invariant equation delta. The six semisimple C5 axes are p1,...,p6. They have no three collinear and do not lie on a conic. Let C_i be the smooth conic through the five points other than p_i.

Use the reviewed second-symbol geometry from PR543 at 86e5aed779f0ff64a83cf9dbe169cb2e7283b346: Sigma is disjoint from Delta, is supported at these six points, and in regular local coordinates has I_Sigma,p=(x^2,y^2). Its resolution is

    0 -> A O(-8) -> P4 O(-6) -> I_Sigma -> 0.

The fourth reduction of PR543 at 2f81e3510505ad842fb9bb00ff3a667cd36ea17f supplies the actual corrected D5 family in

    Q = Hom_G(D5,H0(I_Sigma(10))), dim Q=4.

Its square restriction has target dimension2 and kernel delta times Hom_G(D5,H0(I_Sigma(8))), of dimension2. These facts are inputs, not new claims of this note. We do not compute the actual fourth class, its lifting correction, or its value at a selected direction. The result below is a universal structural constraint on Q. It does not describe the extra specialized A-kernel line at an axis.

## Theorem

Let Z=3p1+...+3p6 be the ordinary triple fat-point scheme, defined locally by m_p^3. Then:

1. H1(I_Z(8))=0 and H0(I_Z(8)) is the G-module P4+D5, of dimension9.
2. The subspace of Q consisting of families zero on Delta and zero in every ACTUAL ideal-sheaf fiber I_Sigma,p/m_p I_Sigma,p is exactly

       delta Hom_G(D5,H0(I_Z(8))),

   and has dimension1. In particular the cubic square-plus-six-fiber vanishing argument cannot determine the fourth gate: there is a nonzero universal equivariant channel invisible to all those tests.
3. Square restriction together with the first ideal-sheaf jet at just one semisimple axis is injective on Q. Here the jet is the class in I_Sigma,p/m_p^2 I_Sigma,p, with the appropriate line-bundle twist. Thus vanishing of those two data forces the D5 fourth family to vanish globally. Ordinary polynomial values or ordinary first derivatives are not this jet test.

## 1. An elementary calculation of the triple-octic linear series

For a smooth conic C through some of the points and a fat-point scheme with multiplicities m_i, taking the residual along C lowers each multiplicity at a point of C by one and lowers the ambient degree by two. The exact sequence is

    0 -> I_Res_C(Z)(d-2) -> I_Z(d)
      -> O_C(d)(-sum_{p_i in C} m_i p_i) -> 0.

This follows locally from (x,y)^m : (x)=(x,y)^(m-1) when x is a local equation of C; restriction to x=0 has ideal (y^m). In particular the final line bundle on C=P1 has degree 2d-sum m_i.

Apply this successively to C6, then C5, then C4. The residual degrees and multiplicities are

    (8;3,3,3,3,3,3)
    (6;2,2,2,2,2,3)
    (4;1,1,1,1,2,2)
    (2;0,0,0,1,1,1).

The three restriction degrees on P1 are respectively 16-15=1, 12-11=1, and 8-7=1. Each restriction has h0=2 and H1=0. The final space consists of conics through the three noncollinear points p4,p5,p6, so it has h0=3 and H1=0. Reading the exact sequences backwards proves H1=0 at all stages and h0=3+2+2+2=9. This proof needs only the stated general-position properties, not very-general points or a vanishing theorem on a del Pezzo surface.

Geometrically this is the complete linear series |8H-3(E1+...+E6)| on the six-point blowup of P2.

## 1a. An explicit six-conic construction of the entire series

Choose the equation c_i of C_i normalized by c_i(p_i)=delta(p_i). This means equality in the one-dimensional fiber O(2)|p_i; it is meaningful without choosing a representative of p_i. Both values are nonzero, so the normalization exists uniquely. Since delta is invariant, G permutes these six normalized equations exactly. Put P=product c_i. For every unordered pair {i,j}, define

    F_ij=P/(c_i c_j)=product_{k not in {i,j}} c_k.

This octic has multiplicity at least4 at p_i,p_j and at least3 at every other axis, so belongs to H0(I_Z(8)). These fifteen octics span that entire nine-dimensional space, as follows.

Use the same residual flag C6,C5,C4. The five forms F_6i restrict, after removal of the prescribed triple zeros on C6, to nonzero sections of O_P1(1) vanishing at the distinct points p_i (i=1,...,5). Therefore they span its two-dimensional space. Nonzero follows because no factor C_k is C6. Exact restriction degree1 also proves that the displayed additional zero is simple and the only remaining zero.

In the residual kernel divisible by c6, the four forms F_5i/c6 (i=1,...,4) similarly span the next degree-one quotient on C5: they have an additional zero at p_i beyond the required residual multiplicity2. In the kernel divisible by c6 c5, the three forms F_4i/(c6 c5) (i=1,2,3) span the degree-one quotient on C4, again with distinct additional zeros at p_i. Finally the forms F_12,F_13,F_23 divided by c6 c5 c4 are c3,c2,c1. These are linearly independent: in a relation among c1,c2,c3, evaluation at p1 kills c2,c3 but not c1, and likewise at p2,p3. They are thus a basis of conics through p4,p5,p6. Backwards induction through the exact sequences proves the spanning assertion.

Consequently the pair-permutation module on fifteen generators surjects onto the triple-octic series. Its character is (15,3,0,0,0)=1+P4+2D5, since an involution fixes three unordered pairs of axes and elements of orders3 and5 fix none. Section2 identifies the image as P4+D5, so the relation module is exactly 1+D5. This supplies an explicit, coordinate-free construction of the unique D5 channel, not merely a dimension count. No c_i coefficient or actual gate value has been evaluated.

## 2. The representation is P4+D5

The vanishing just proved makes evaluation onto the triple-point jets surjective:

    0 -> H0(I_Z(8)) -> Sym^8 A -> H0(O_Z(8)) -> 0.

Here H0(O(8)) is Sym^8(A*), identified with Sym^8 A using self-duality. All central actions are trivial, so compute A5 characters on classes (1,2,3,5a,5b). The triple jets have characters (36,4,0,1,1). Here is the full local justification, including the twist.

The axes form the six cosets of a dihedral normalizer of order10. An involution fixes two axes, an order-three element fixes none, and an order-five element fixes one. At a fixed axis an involution has tangent eigenvalues (1,-1); the trace on local polynomials of degrees0,1,2 is 1+0+1=2. The O(8) fiber action is +1: the semisimple axis has eigenvalue -1 under such a normalizer involution, acting on O(8) by its inverse eighth power. Thus the total involution trace is4.

For an order-five element the semisimple axis has eigenvalue1, so the O(8) twist again acts trivially. Tangent eigenvalues are (zeta,zeta^-1), with zeta a primitive fifth root (or its square for the other class). The degree<=2 jet trace is

    1+(zeta+zeta^-1)+(zeta^2+1+zeta^-2)=1.

Finally Sym^8 A has characters (45,5,0,0,0). They can be read from the coefficient of t^8 in 1/det(1-tg|A): for order2 use 1/((1-t)(1+t)^2); for order3 use 1/(1-t^3); for either order5 use eigenvalues (1,zeta,zeta^-1), giving coefficient zero. Subtracting gives (9,1,0,-1,-1), the sum of the P4 character (4,0,1,-1,-1) and D5 character (5,1,-1,0,0). Hence H0(I_Z(8))=P4+D5.

## 3. Exact kernel of square and axis-fiber tests

Let Phi in Q have zero restriction to Delta. The input discriminant sequence gives uniquely Phi=delta Psi, with Psi:D5 -> H0(I_Sigma(8)). Since delta is a unit at every axis, a zero actual fiber of Phi is equivalent to a zero actual fiber of Psi. Locally

    m_p I_Sigma,p = (x,y)(x^2,y^2) = (x,y)^3.

Therefore these fiber zeros mean precisely that every component of Psi belongs to I_Z(8). Conversely every section of I_Z lies in I_Sigma and has zero ideal-sheaf fiber, so this is equality of the kernels, not merely an inclusion. Taking Hom_G(D5,-) and the representation in Section2 gives exactly one dimension.

This unique line is canonical; a nonzero map on it embeds the irreducible D5 in the nine-dimensional triple-octic series. No normalization or value of its scalar is asserted. The combined square-plus-fiber test has rank3 on the four-dimensional Q. On the two-dimensional square-invisible subspace the fiber test has rank1, leaving precisely this line.

## 4. The next jet is sufficient

Suppose Phi has zero square restriction and its first ideal-sheaf jet is zero at one axis p. Equivariance and transitivity imply the same zero at all six axes. Divide by delta, a local unit. At each axis its components then belong to

    m_p^2 I_Sigma,p = (x,y)^2 (x^2,y^2) = (x,y)^4.

Every residual octic component therefore has multiplicity at least4 at all six points. Its intersection with each C_i is at least5*4=20, exceeding its Bezout intersection degree 2*8=16. Thus each of the six distinct irreducible conics divides the octic. Their product has degree12, so the octic is zero. This proves the asserted injectivity.

In particular, after square and fiber vanishing, the single remaining universal line has NONZERO first ideal-sheaf jet at every axis. Equivalently its map to m_p I_Sigma,p/m_p^2 I_Sigma,p = m_p^3/m_p^4 cannot be zero as a linear map with source D5 (the test concerns the entire family, not a single source vector). This conclusion does not select a source vector or evaluate an actual coefficient. It identifies a sufficient next local datum for the corrected quartic calculation retained by null.

## Contribution and limits

The new obstruction to repeating the cubic proof is exact, not heuristic: triple septics are zero, whereas triple octics contain one D5 copy. Indeed a triple septic meets each C_i at least15 times, exceeding14 and forcing all six conics as components, impossible in degree7. A nonzero fourth class can therefore survive all previous square and six-fiber zero tests. The next ideal-sheaf jet removes that entire ambiguity. No assertion is made that the actual class lies on this line, is nonzero, or passes/fails the additional test. No new Smith exponent bound, section count, higher-order vanishing, or algebraicity conclusion follows without actual fourth data.

Dependencies:
- https://github.com/Akilleez-QA/read-em-and-weep/blob/86e5aed779f0ff64a83cf9dbe169cb2e7283b346/research/hm/order-four-quadratic-load/THIRD-GATE-VANISHING-AT-SIX-AXES-KILLS-RESIDUAL-CHANNEL.md
- https://github.com/Akilleez-QA/read-em-and-weep/blob/2f81e3510505ad842fb9bb00ff3a667cd36ea17f/research/hm/order-four-quadratic-load/FOURTH-BOCKSTEIN-AFTER-ACTUAL-THIRD-VANISHING.md

The residual-sequence argument is proved locally above. General background: A. Gimigliano, B. Harbourne and M. Idà, The role of the cotangent bundle in resolving ideals of fat points in the plane, https://www.sciencedirect.com/science/article/pii/S002240490800131X . The proof here uses no claimed result specific to a selected coefficient instance.
