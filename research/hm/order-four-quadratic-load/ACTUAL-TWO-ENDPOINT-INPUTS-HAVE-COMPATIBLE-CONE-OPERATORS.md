# Actual compatible cone operators for the two endpoint inputs

## Result and boundary

For a=z^2 and EACH of h=X^4 and h=XY^3, the formulas below give the actual scalar inverse and a regular homogeneous degree-four cone connection on the vertex eigenextension. They have the prescribed actual symbol and physical section-line action. Natural determinant transport and uniqueness prove full chart covariance; the general conic-cocycle lemma patches them to actual cone operators without changing their degree-four parts.

Thus both inputs are licensed in the lowest endpoint secondary formula. No endpoint cohomology class, full normal connection, or fourth Bockstein is evaluated. All A,B,c,lambda,k,e are unassigned nonzero parameters; the calculation is uniform over the stabilizer orbit and uses no source specialization or instance rank.

## 1. Common actual Serre data

Use the actual divisor presentation

    f=A X^2Y+B Y^3z+Ac X^3z^2-Bc XY^2z^3,
    g=-lambda(B XY^4/z^3+A X^3Y^2/z^4)/(2Ac).

The regular target changes are

    p_x=lambda XY/(2Ac z^4)-lambda X^2/(2A z^2)
          +lambda B Y^2/(A^2 z),
    p_y=-lambda Y^2/(2Ac^2 w^2)+lambda X^2/(Bc^2 w),
    w=-1/z,
    f_y=z^-3 f,     g_y=z^5 g.

In the x and y charts use respectively (f,g+p_x f) and (f_y,g_y+p_y f_y). These are actual homogeneous, residue-normalized regular Serre pairs for the vertex eigenextension, with the physical determinant marking established by the full-frame and conic-cocycle comparisons.

## 2. Source identities for both h

For each input let h f_z=m f+n g.

For h=X^4, the already established exact coefficients are

    n=[X^2(-4Az+Bc^2z^6)+2Bc XYz^4-3B Y^2z^2]/lambda,
    m=[4Ac X^4z^2-4A X^3Y-Bc X^2Y^2z^3-3B XY^3z]
          /(2Ac z^3),
    u=4kB XY^3z^2/(Ac)+4k X^3Yz/c.                 (1)

For h=XY^3, the exact coefficients are

    n=A[AX^2cz^2+AXY+BXYc^2z^5+3BY^2cz^3]/(B lambda),
    m=XY^2(AX+5BYcz^3)/(2Bc z^4),
    u=-2kA X^3Yz^2/B-3kY^4z/c-3kA X^2Y^2/(Bc).   (2)

The verifier proves the complete polynomial identities h f_z=m f+n g in both cases. Passing to a regular quintic target changes m to m-pn and leaves n unchanged. In the oriented other chart the source transforms are

    n_y=z^-6 n,     m_y=z^2 m-3z h,
    h (f_y)_w=m_y f_y+n_y g_y.                    (3)

These derivative and line factors are checked explicitly; raw s/t derivatives would have the wrong sign.

## 3. Both u are the actual scalar inverse

The normalized actual quotient/socle map has the common formulas

    Q(X^4)=e[-B XYz^2/(2A)-B Y^2/(2Ac)],
    Q(X^3Y)=e[X^2z+(B/A)Y^2z^2]/4,
    Q(X^2Y^2)=-e XYz/2,
    Q(XY^3)=e[-(A/B)X^2+Y^2z]/4,
    Q(Y^4)=e[(A/B)XY-(Ac/B)X^2z^2]/2.             (4)

These are the actual socle/apolar map, including its coefficient line, not an arbitrary five-by-three array. Extend Q linearly in the negative-coordinate coefficients. For both (1) and (2), exact substitution proves

    Q(u)=k a [2a partial_z Q(h)-2a_z Q(h)],
    a=z^2.                                       (5)

The coefficient-line term -2a_z is retained. The actual twist-two scalar-cup map is an isomorphism, so (5) identifies u uniquely with the actual Ext/scalar correction for that input. In particular the scalar for one h has not been imported into the other. The common socle scale e cancels from (5).

## 4. Complete regular homogeneous connections

On either regular chart, with its local base coordinate v, use its regular pair (F,G), the transformed n and u, and a=z^2 on the x chart or a=1 on the y chart. Set

    H=k a h,
    D=2a partial_v+(a_v/2)(X partial_X+Y partial_Y),
    Lambda=2k a a_v h-u,
    A12=-2k a^2 n,
    mfull=(H D F+A12 G)/F,
    A11=Lambda/2-mfull,
    A21=[(Lambda-mfull)G-H D G]/F,
    A=[[A11,A12],[A21,-A11]].                       (6)

The y scalar is u_y=z^-2 u before substituting z=-1/w. Formula (6) is computed separately in BOTH regular target charts, not only in the meromorphic divisor frame.

For both h, the verifier proves that every entry of A is polynomial in the full chart variables (v,X,Y), with denominators only in the unassigned nonzero constant parameters. It also proves

    H D sigma+A sigma=(Lambda/2)sigma,
    H Dn+[A,n]=Lambda n,                           (7)

where sigma=(F,G) and n=[[FG,-F^2],[G^2,-FG]]. Its coefficient degrees are exactly

    deg(A11)=4,     deg(A12)=2,     deg(A21)=6.

Thus the weighted diagonal degree of the connection is four. Polynomiality here includes the divisibility by F in (6); it is not inferred from the displayed rational expressions or from generic regularity.

## 5. Natural full covariance follows from uniqueness

Two regular trace-free homogeneous degree-four solutions with the same symbol and equation (7) differ by a trace-free matrix T with T sigma=0. Regularity of (F,G) implies T=ell n. Since n has weighted diagonal degree eight, homogeneity requires ell to have cover degree minus four. A regular positive-coordinate polynomial has no such degree. Therefore the homogeneous solution is UNIQUE in each full chart.

To apply uniqueness to transport, one must retain the determinant scalar. Put z=Z^2. The homogeneous Serre transition has determinant Z^-4 and physical operator weight Z^-8. The base/positive derivation is

    D_root=Z^3 partial_Z+Z^2(X partial_X+Y partial_Y).

Trace-free connection transport is

    A_y=Z^-8 tf(P0 A_x P0^-1-H_x(D_root P0)P0^-1).

Its section-line scalar is therefore

    Lambda_y=Z^-8[Lambda_x+H_x D_root(log det P0)].

Since D_root(log det P0)=-4Z^2 and Lambda_x=4Z^2H_x-u_x, this is -Z^-8 u_x, exactly the transformed y scalar (a_y=1). The coordinate/root factors in u_y=z^-2u supply the additional Z^-4 from its quartic positive degree, so u_y in root variables is Z^-8u_x.

As an independent universal check, the verifier also constructs the FULL marked transition

    P0=[[Z^-9,0],[p_y(root)Z^-9-Z^5 p_x,Z^5]],

and verifies every entry of the displayed trace-free connection transport for both inputs. This check uses unassigned parameters and the actual Serre transition, not a selected-instance matrix/rank evaluation.

Thus natural transport satisfies precisely the same actual equation as the independently regular y-chart formula. It is regular on chart overlaps and has the same weighted degree. Uniqueness forces equality there. This proves complete homogeneous covariance for BOTH inputs, without inferring it from the previous h=X^2Y^2 calculation.

## 6. Actual conic patching and the endpoint interface

For the actual conic cocycle t=rho_C/z, finite transport by I-t n changes A by

    (H Dt+Lambda t)n.

For each of the two inputs the coefficient C=H Dt+Lambda t has cover degree four and physical twist two, hence coefficient bundle Sym^4(Wprime) O_L(0). Its H1 vanishes. Regular scalar cochains c_i with delta c=C exist; adding c_i n gives a genuine operator on the actual bundle. The correction begins in weighted degree twelve.

Hartogs extends the operator across C. Any fixed actual cone operator with the same symbol and prescribed physical section-line action differs by ell n, ell in H0(O_X(2)); this starts at weighted degree at least eight. Therefore both inputs have precisely the actual degree-four operator (6), with the fixed normal-equation term included:

    L4(E)=H D E+[A,E]+H rho E,
    T4(s)=H D s+u s.

The rho term belongs to the already fixed actual physical normal-equation convention; conic patching neither changes nor removes it.

Consequently the independently reconstructed actual lowest eta and scalar shadow lifts may be inserted, for EACH input, into

    tau(gamma4)=L4(eta8)-delta K,
    q(K_i)=T4(n_i).

This note supplies its actual operator/source data, not the solution for K_i or the resulting P4 value. The trace-correcting K_i remain indispensable.

## Sources and reproduction

The h=X^4 data and actual divisor/regularizers are from UNIVERSAL-DIVISOR-QUINTIC-TWO-CHART-SHADOW-CANCELLATION.md and the actual source-change theorem. The complete map (4), including Q(Y^4), is recorded in ACTUAL-CANONICAL-RAW-CUBIC-HAS-A-NONZERO-LINEAR-LIFTING-CORRECTION.md and ACTUAL-MIDPOINT-ABSOLUTE-SECTION-FOR-THE-FOURTH-SQUARE-INPUT.md. The actual scalar isomorphism is supplied by ACTUAL-QUINTIC-SCALAR-CUP-IS-A-SWAPPED-QUOTIENT-ISOMORPHISM.md and the scalar-inverse sources. Determinant/root conventions and finite conic transport are from ACTUAL-CONE-OPERATOR-PATCHING-FROM-THE-CONIC-COCYCLE.md. The general comparison is proved in ACTUAL-ENDPOINT-QUOTIENT-IS-LOWEST-VERTEX-COHOMOLOGY.md.

Run python verify_two_endpoint_input_cone_operators.py. All identities are symbolic in the unassigned parameters, and all coefficients of the regular-chart operators are checked, not selected entries. Frozen sources remain unchanged.
