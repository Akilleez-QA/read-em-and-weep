# The twelve special hyperplane adjoint spaces are exactly squares

## Theorem

At every one of the twelve order-five parameters of the actual HM hyperplane family,

    H0(H_lambda,B_Hlambda(3))
      = Sym^2 H0(H_lambda,F_Hlambda(2)),
    h0(H_lambda,B_Hlambda(3))=3.

All three sections are inversion-even. Together with the already established result away from those twelve parameters, this holds for EVERY hyperplane containing the positive fixed plane.

The proof computes the ordinary ideal square of an actual section zero curve, retaining its ribbon parameters. The boundary to H1(F_H(2)) vanishes because its one-dimensional source is already lifted by the square of the other section. No generic ribbon choice or actual coefficient evaluation is used.

## 1. The special section and its known geometry

Write E=F_H(2), so det E=O_H(3), c2(E)=6, h0(E)=2, H0(E(-1))=0, and B_H(3)=Sym^2 E equivariantly. Choose a special parameter and coordinates on H=P3 with point weights modulo five

    (x,y,z,u)=(0,1,4,1),

where R=(u=0) and the negative vertex is v=[0:0:0:1]. Inversion fixes x,y,z and negates u. The actual determinant cubic is

    S=x^2 z.

The section two-plane has weight-4 and weight-2 eigenvectors t,w. The established results give:

- The vertex evaluation kernel is C t=C ell^4; hence w(v) is nonzero. This is NONZERO-VERTEX-EVALUATION.md, immutable pin c779b2919a36b9d45a6319d46551bd6380154bba.
- The zero scheme of w restricted to R has length two at p=[1:0:0:0], length four at r=[0:0:1:0], and no other support. Both local schemes are curvilinear. This is ACTUAL-SEXTIC-FACTOR-IMAGE-BY-CHERN-LENGTH.md.
- The zero curve C=Z(w) is regular, purely one-dimensional and locally complete intersection, of degree six, with omega_C=O_C(-1). Its unique containing cubic is S, so h0(I_C(3))=1.

In particular C avoids v, has no component in R, and is preserved by C5 and inversion.

## 2. This eigen-section has the conic-plus-double-conic type

We first justify applying the type-3 description to this specific eigen-section rather than silently calling it general.

Suppose all components of C had generic multiplicity at least two. The local intersection length (C.R)_p=2 would force exactly one reduced support component D through p, with generic multiplicity two and (D.R)_p=1. This follows from the associativity formula for intersection with the nonzerodivisor u on the Cohen–Macaulay curve C. The component D is unique through p, so it is preserved by C5 and inversion. It has degree at most three and is contained in the simple determinant plane Pi'=(z=0), since p is not on (x=0).

On Pi', the point weights are 0,1,1. An invariant plane curve of degree d<=3 has an eigen-equation. The weights attached to the possible total degrees 0,...,d in y,u are distinct modulo five. Its equation is therefore x^(d-j) times a binary form of degree j in y,u. Over C this factors into linear forms. Irreducibility forces D to be a line.

A C5-stable line through p has equation a y+b u=0. Inversion stability forces a=0 or b=0. The first possibility is a line contained in R, contrary to the finite intersection C.R. The second is a line through v, contrary to w(v)!=0. This is a contradiction. Thus C has a multiplicity-one component.

The checked Bănică–Manolache classification, as recorded in REDUCED-DETERMINANT-THREE-CONIC-PENCIL.md at pin 35fc96bebf9c771a4de481c753bb527e510cd8c1, excludes the two wholly Ferrand-double types and the triple-conic type. The three-disjoint-conic type is impossible because the product of their three distinct plane equations would be the unique containing cubic, whereas S is nonreduced. Distinctness of those planes follows from disjointness of the conics and plane Bezout, including degenerate conics.

Therefore

    C = Q disjoint-union Y,

where Q is a plane conic and Y is a Ferrand double of a plane conic Q'. Uniqueness of the containing cubic, applied to the cubic h_Q h_Q'^2, places

    Q subset Pi'=(z=0),       Q' subset Pi=(x=0).

The component of multiplicity one belongs to Q, so Q is reduced. The decomposition is preserved by both symmetries, since its two connected pieces have different degrees. Their supports avoid v.

## 3. The actual ribbon parameters have a forced weight form

First Q' cannot be a plane double line. Otherwise its reduced support would be a line preserved by C5 and inversion, since it is the reduced support of the invariant component Y. It passes through r: Q lies in z=0, whereas the nonempty length-four intersection of C with R at r must belong to Y. In Pi=(x=0), a C5-stable line through r has equation a y+b u=0. Inversion forces y=0 or u=0, respectively giving a line through the vertex or a line contained in R. Both are impossible. Thus Q' is reduced and equals Y_red canonically; in particular its equivariance does not rely on choosing an invariant Ferrand presentation.

The two conic equations have the form

    Q=(z,q0(y,u)),       Q'=(x,q(y,u)),

where q0 and q are binary quadratics with no common zero on P1. Indeed avoidance of v gives a nonzero u^2 coefficient in each equation. C5 equivariance then puts each equation in the binary quadratic eigenspace in y,u. Inversion removes its yu term. Neither y^2 coefficient can vanish, because that would give a component contained in R. Consequently both conics are reduced pairs of lines. Disjointness of Q and Q' is exactly the nonintersection of the root schemes of q0 and q in P1.

Let L be the square-zero conormal line bundle of the Ferrand double Y over Q'. The dualizing restriction formula gives

    omega_Y|Q' = omega_Q' tensor L^{-1}.

Both dualizing bundles here are O_Q'(-1), so L=O_Q'. Hence Y is specified by a surjection

    I_Q'/I_Q'^2 = O_Q'(-1) directsum O_Q'(-2) -> O_Q',

with coefficients

    a in H0(O_Q'(1)),       b in H0(O_Q'(2)),

having no common zero. Neither coefficient is zero: otherwise the other would be a nowhere-vanishing section of a positive-degree line bundle on the conic.

The equivariant linearization of L is a character, since its underlying bundle is trivial and H0(O_Q')=C. Thus a and b are eigenvectors whose weights differ by the weight of q, namely three. On Pi the linear function weights are four on y,u and one on z. If a had weight one, b would have weight four. That weight is absent in H0(O_Q'(2)): the quadratic weights before quotienting by q are three, zero and two. Therefore

    a=a(y,u),       b=kappa z^2,       kappa!=0.

The no-common-zero condition is equivalent here to gcd(a,q)=1 in C[y,u]. In particular a is a unit at every point of Q' intersect Pi'. The actual value of kappa and the coefficients of a,q,q0 are not chosen.

Put g=b x-a q. As an IDEAL SHEAF, the actual Ferrand double has

    I_Y=(x^2,x q,q^2,g).                              (1)

This follows by taking the kernel of the preceding surjection; the relation b x-a q generates its conormal kernel. Formula (1) is used sheaf-theoretically throughout, so no saturation of a polynomial square is assumed.

## 4. Restriction to the simple plane

Let F be a global section of I_C^2(6). On Pi' it is divisible by q0^2, so

    F|Pi'=q0^2 r2

for a quadratic r2. The scheme T=Y intersect Pi' has ideal

    I_T=(q,x^2) on Pi'.

Indeed (1) restricted to z=0 contains a q, and a is a unit on the zero set of q there. The equality holds as ideal sheaves. The two defining quadratics form a regular sequence. Its ordinary ideal square has the resolution

    0 -> O_P2(-6)^2 -> O_P2(-4)^3 -> I_T^2 -> 0.

In particular H0(I_T^2(2))=0.

Near T the function q0 is a unit, by disjointness. Restriction of an ordinary ideal square has image the square of the restricted ideal. It follows that r2 belongs to I_T^2, so r2=0. Hence

    F=z G,       deg G=5.

Since (I_Q^2:z)=I_Q, one has G in I_Q. Also z is a nonzerodivisor on O/I_Y^2: the latter is Cohen–Macaulay because Y is locally complete intersection, and no component of Q' is contained in z=0. Thus

    G in I_Y^2.                                      (2)

## 5. Two exact restrictions to the double plane

Let Z in Pi be the nonempty complete intersection (a,q). Restricting the generators of I_Y^2 to x=0 gives the image ideal

    q^2 (a,q)^2 = q^2 I_Z^2.

Therefore (2) implies G|Pi belongs to q^2 H0(I_Z^2(1)), which is zero. For example the complete-intersection square resolution for degrees one and two has generators in degrees two, three and four and first syzygies in degrees four and five; H1 of every line bundle on P2 is zero. Consequently

    G=x H,       deg H=4,
    H in J=(I_Y^2:x).

We claim that the image of J on Pi is exactly

    J|Pi = q^2(a,q)=q^2 I_Z.                         (3)

Here and below restriction of an ideal denotes its image in O_Pi. It suffices to work near Q', covered by a!=0 and b!=0.

On a!=0, I_Y=(x^2,g), and the regular-sequence calculation gives

    (I_Y^2:x)=(x^3,xg,g^2).

Its image on Pi is q^2 times a unit, in agreement with (3).

On b!=0, I_Y=(g,q^2), and x=(g+a q)/b. The coefficient a is a nonzerodivisor modulo every power of q because gcd(a,q)=1. Modulo g^2, write an element as h0+g h1. Its product with g+a q belongs to (g^2,g q^2,q^4) precisely when

    a q h0 is divisible by q^4,
    h0+a q h1 is divisible by q^2.

These conditions say that h0 is divisible by q^3 and h1 by q. Thus

    (I_Y^2:x)=(g^2,gq,q^3).

Setting x=0, so g=-a q, gives q^2(a,q), proving (3).

Since H has degree four, (3) gives H|Pi in q^2 H0(I_Z)=0. Hence

    G=x^2 K,       deg K=3.

Finally

    (I_Y^2:x^2)=I_Y.                                (4)

On a!=0, x^2 is a member of a regular pair of generators, so (4) is immediate. On b!=0, its conormal class in I_Y/I_Y^2 has coefficients, up to units,

    (2 a q, a^2)

relative to g,q^2. The coefficient a^2 is a nonzerodivisor on O_Y. Indeed on this chart eliminating g identifies O_Y with the plane local ring modulo q^2; gcd(a,q)=1 means that a is divisible by none of the irreducible factors of q. In the regular plane local ring it follows directly that (q^2:a^2)=(q^2), including at the node of the reduced conic. Thus multiplication by this conormal class is injective on O_Y, which is exactly (4). We obtain K in I_Y.

The earlier membership G in I_Q gives x^2 K in I_Q. Since x is a nonzerodivisor on O_Q, also K in I_Q. Therefore K belongs to I_C.

## 6. Exact square space and vanishing of the boundary

The calculation proves

    F=(x^2 z)K,       K in H0(I_C(3))=C(x^2 z).

The reverse containment is automatic. Thus

    H0(I_C^2(6))=C S^2.                              (5)

For the regular section w, the symmetric-square sequence is

    0 -> E --multiply by w--> Sym^2 E
      -> I_C^2(6) -> 0.

Its right-hand map sends t^2 to (w wedge t)^2, a nonzero multiple of S^2. Therefore the actual boundary from the one-dimensional space (5) to H1(E) is zero. Taking global sections gives

    h0(Sym^2 E)=h0(E)+1=3,
    H0(Sym^2 E)=span{w^2,wt,t^2}.

Both original sections are inversion-even. This proves the theorem, including its parity, without any assumption on the remaining H1(E) group or any evaluation of the boundary rank.

## Scope

The argument uses the actual eigen-section, its established Chern-length geometry, the already proved nonzero vertex evaluation, and the applicable primary classification. All ribbon coefficients are retained subject only to proved weights and the Ferrand surjectivity condition. The ideal-square and colon identities concern ordinary ideal sheaves, not unverified symbolic squares or unsaturated polynomial ideals. The result determines the special hyperplane adjoints; it does not assert injectivity of the subsequent global quadric smoothing gate.


## Universal symbolic companion

verify_special_ribbon_colons.py computes each ideal quotient via elimination of an auxiliary variable from I intersect (h), followed by division by h. It checks both inclusions against the claimed quotient ideals. On the formal b-unit chart it checks

    ((g,q^2)^2 : (g+a q)) = (g^2,gq,q^3),
    ((g,q^2)^2 : (g+a q)^2) = (g,q^2),
    ((g,q^2) : a^2) = (g,q^2),

and the restricted image q^2(a,q). It separately checks the a-unit chart with regular pair x,g. All checks pass; the log is special-ribbon-colon-verification.log. The variables are formal and independent, not selected HM coefficients. The proof above separately justifies applying the identities to the actual functions through the nonzerodivisor condition gcd(a,q)=1.
