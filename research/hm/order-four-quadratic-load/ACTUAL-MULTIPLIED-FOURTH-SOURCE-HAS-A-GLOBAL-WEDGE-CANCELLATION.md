# The multiplied corrected midpoint source has an explicit global wedge cancellation

## Result and exact scope

For the uniform order-five fourth-detecting input a=t², h=X²Y², the actual multiplied MIDPOINT corrected source has an explicit preimage under the canonical degree-eight tangent quotient E8 -> M8. This constructs its global cohomological cancellation and reproduces the actual correction constant in the shared normalization. It does not identify a chosen homogeneous tangent pair with a literal full section of the actual G(4), does not determine the endpoint P4 variation, and does not evaluate the fourth Bockstein or the next ambient division.

All A,B,c,lambda,k,nu are unassigned nonzero parameters of the actual stabilizer tensor. The eigenvectors are arbitrary normalized eigenvectors uniformly over the whole order-five orbit, not selected actual coefficients or an instance test. The companion checks exact polynomial identities over the rational function field in these symbols.

Dependencies: ACTUAL-MIDPOINT-ABSOLUTE-SECTION-FOR-THE-FOURTH-SQUARE-INPUT.md; ACTUAL-ATIYAH-CLASS-HAS-AN-ABSOLUTE-DOUBLE-CUBIC-REPRESENTATIVE.md; ACTUAL-CORRECTED-FOURTH-SQUARE-SOURCE-IS-NONZERO-ON-THE-CUBIC.md; ACTUAL-DEGREE-EIGHT-NORMAL-OPERATOR-QUOTIENT.md, especially its intrinsic fiber-product/global-boundary diagram. These fix the same Atiyah constant k and boundary signs.

## 1. The unique global wedge polynomial

Use z=t/s, a=z² and the actual divisor-frame pair

    f=A X²Y+B Y³z+Ac X³z²-Bc XY²z³,
    g=-lambda/(2Ac)(B XY⁴/z³+A X³Y²/z⁴).

Let r_mid be the full absolute midpoint diagonal numerator in the cited source, and put

    r_t=2k a d_z(a f g),   theta=nu gamma,
    r=a(r_mid-theta r_t).

Thus r/(nu g²) is the multiplied corrected midpoint class. Keep theta temporarily arbitrary. On the actual reduced cubic D, r is a section of O_D(8,2). The restriction map

    H0(O(8,2)) -> H0(O_D(8,2))

is an isomorphism: its divisor kernel O(5,-1) has zero H0 and H1. Therefore a unique GLOBAL polynomial w of bidegree (8,2) satisfies w|D=-r|D.

It is explicitly given by w=f v2-g v1, where

    v1=k z⁵[(2theta+1/3)Ac z²X³+6A theta X²Y
                    +(4theta-1/3)BzY³],
    v2=lambda k[(12theta+2)A²cX⁵+(6theta+1)ABczX³Y²
                    +(12theta-1)B²Y⁵]/(6ABc²).               (1)

Cancellation shows that w is polynomial of z-degree at most two. Its coefficients in the ordered basis

    X⁷Y, X²Y⁶, zX⁵Y³, zY⁸, z²X⁸, z²X³Y⁵

are respectively

    A²lambda k(6theta+1)/(3Bc),
    B lambda k(12theta-1)/(6c²),
    A lambda k(12theta+1)/(2c),
    B²lambda k(12theta-1)/(6Ac²),
    A²lambda k(6theta+1)/(3B),
    B lambda k(48theta-1)/(6c).

The universal identity f | (w+r) proves the claimed restriction without evaluating any source coefficient.

## 2. The genuine coefficient bundle, with both chart regularities

The first entry v1 has bidegree (3,7), and the second has bidegree (5,-1) in the meromorphic quintic frame. Under g -> g+p f the pair changes by

    v1 -> v1,   v2 -> v2+p v1.

For the actual regularizing p_x,p_y of the absolute-source theorem, both v2+p_xv1 and v2,y+p_yv1,y are regular on their complete standard charts. Here

    wbase=-1/z,  v1,y=z^(-7)v1,  v2,y=z v2,
    p_x=lambda XY/(2Ac z⁴)-lambda X²/(2Az²)+lambda BY²/(A²z),
    p_y=-lambda Y²/(2Ac² wbase²)+lambda X²/(Bc² wbase).

The verifier checks these as polynomial identities. Thus (1) is a global section of the canonical degree-eight tangent coefficient bundle E8, not just a formal pair on the overlap. Its five-dimensional scalar ambiguity is sigma times H0(O_L(4)); alternatively this follows from the divisor kernel O(0,4) in H0(O(3,7)) -> H0(O_D(3,7)).

This uses the canonical E8 fiber product of the cited quotient theorem. It does NOT assert that E8 is a literal homogeneous subbundle of G|U. Actual higher Koszul stabilizers do not alter that intrinsic quotient, but can matter for a subsequent full connection calculation.

## 3. Exact scalar matching, including the correction constant

Let chi be a global scalar quartic on L. With tau(v) diagonal g v1+f v2, the source class equals the class of tau(v+(chi/2)sigma) exactly when

    r-w-2g v1-chi f g = 0 modulo f².                       (2)

Since g is nowhere zero on D, this is equality of the actual double-cubic sections, not merely equality on D. In the entire scalar quartic space, the unique solution of (2) is

    theta=-1/12,    chi=A k/(3Bc²).                         (3)

Here chi is written in the s=1 frame of O_L(4), so chi_y=z^(-4)chi. It must not be confused with the local equation weight Dq/q.

More explicitly, at (3),

    r-w-2g v1-chi f g=f² Q,
    Q=lambda k(-11Ac z²X²+5AXY+Bc z³Y²)/(30ABc³z⁴).        (4)

The companion independently checks (4) and solves the polynomial identity with an arbitrary chi0+chi1 z+...+chi4 z⁴; it forces (3) and chi1=...=chi4=0. To identify this solution with the ACTUAL canonical correction, use (6) below: it has zero actual global boundary in H1(B_Q(4)), hence zero in the projected raw-third P4 target. The actual endpoint differs from the computed midpoint source only in Cplus, and negative multiplication kills all of Cplus by the proved lower multiplication theorem. Thus the same projected raw-third class is canceled for the actual source. This square direction is disjoint from Sigma, so beta2(a):A->P4 is injective. The canonical correction is therefore unique, and the constructed value is exactly gamma=-1/(12nu), not merely a convenient homogeneous scalar. A simultaneous change of the fixed boundary/Atiyah conventions must be transported throughout rather than changing one sign in isolation.

In particular the matched tangent pair simplifies to

    v1=k z⁵(Ac z²X³/6-A X²Y/2-2BzY³/3),
    v2=lambda k(A X⁵/(6Bc)+zX³Y²/(12c)-B Y⁵/(3Ac²)),
    V=(v1,v2)+(chi/2)(f,g).                               (5)

Dividing (4) by g² on the actual double cubic f²=0 proves

    [r/(nu g²)]=[tau(V)/(nu g²)] in H0(M8).                (6)

The factor one-half is required because tau(sigma)=2N. This is an explicit global E8 preimage, hence its actual global boundary in H1(B_Q(4)) is zero. We use the established positive-sector square-ideal comparison when passing from that global boundary to P4; it is not a replacement of the full boundary by a local residue test.

## 4. What (6) permits, and what it does not

The actual wedge/square-ideal diagram identifies the E8 -> M8 boundary with the global H1(B_Q(4))_+ obstruction. Its exactness supplies global G(4) representatives for the kernel CLASS in (6). Separately the polynomial w is a genuine global section of I_Z(6): it has positive-cover degree eight, so vanishes on the vertex zero scheme of socle degree six, and its negative quadratic factor makes it vanish on the conic. H1(O_X(4))=0 supplies an actual Serre lift of w.

Neither fact identifies the specific polynomial pair (5) with a full actual G(4) lift. In particular, they do not prove that a homogeneous local commutator K extracted from (4) is the complete next actual connection. Higher stabilizer/frame contributions must still be compared before using [K,t] or first harmonic-product terms involving K at second normal order. The actual endpoint P4 component remains separate. Thus the result is an explicit first-error/global-boundary cancellation, not a fourth-value assertion.
