# The actual absolute midpoint section for the fourth-square input

## Result and scope

For the sole order-five square-direction detecting input of the fourth gate,

    a=t²,   h=X²Y²,

we calculate the ACTUAL unmultiplied midpoint normal-error section in

    H0(M_-)/A,   M_-=M8(-2),

not only its image in the effective twelve-space. In particular this fixes the previously lost polynomial nine-space for this input, without choosing a splitting of that nine-space. Its double-cubic coordinate is the explicit r0/(nu g0²) below. This calculation is uniform over the entire order-five stabilizer orbit: s,t and X,Y are arbitrary normalized abstract eigenvectors, and all A,B,c,lambda,k,nu remain symbolic and nonzero. There is no selected actual coefficient value, actual-instance matrix/rank evaluation, source instance, or local-model experiment.

The result is the full MIDPOINT negative-involution class. It is not the actual endpoint class in C/J: the latter can additionally have its normal-variation P4 component. Nor is this the corrected fourth source, or a fourth-Bockstein value. A different normalized dual route may bypass these additional reconstruction data.

Dependencies are the actual cubic/quintic divisor trivialization and regular-target theorem; MIDPOINT-HESSIAN-SYMBOL-MATCHING-BY-FULL-FRAME-COVARIANCE.md; UNIVERSAL-FIRST-NORMAL-HARMONIC-PRODUCT-AND-OPERATOR-RESIDUE.md; ACTUAL-CONE-DIAGONAL-IS-CANONICAL-RESIDUE-INVERSE.md; and the actual double-cubic/global-boundary identifications.

## 1. Convert the ACTUAL matched Hessian lift to harmonic splitting

Write tau for the unnormalized second positive transvectant. If f,g have odd degrees p,q, and their even Euler-gradient entries are lifted harmonically, the Euler-Gram product is

    (grad f/p)^t Cmat (grad g/q)
      = L(fg)+qcone L(tau(f,g)/(2pq(p+q-1))) mod qcone².       (1)

This is an equivariant bilinear identity. Its first-normal component lies in the unique second-transvectant summand; the universal highest/lowest monomials fix the displayed constant. The verifier independently checks all 76 pairs in the COMPLETE abstract monomial bases for degrees (3,3),(3,5),(5,5). These are representation identities, not actual-source evaluations.

Add the matched Hessian correction, including its unique gluing primitive. With physical q0=nu qcone and v=nu u_H, the actual midpoint nilpotent is, modulo local normal conjugation,

    Ncorr=L([[fg,-f²],[g²,-fg]])+qcone L(t),
    t11=tau(f,g)/112+v f,
    t12=-det(Hf)/20,
    t21=det(Hg)/144+2v g.                                  (2)

The three constants follow from 1/210+1/240=1/112,
-1/45-1/36=-1/20, and 1/225+1/400=1/144. The v term is the HESSIAN gluing primitive, not the earlier scalar Gram primitive used to remove K11.

A local normal conjugation changes the absolute error by a commutator. Explicitly replacing the qcone correction by t+[B,N] changes it by

    [H D B+[Aconn,B]+H rho B,N],

using H DN+[Aconn,N]=Lambda N and Dqcone=rho qcone. It therefore has zero image in M_-. This licenses (2) for the absolute section, not merely for the transition shadow.

## 2. The actual Hessian primitive in the divisor frame

On z=t/s take the actual meromorphic quintic representative

    f=A X²Y+B Y³z+Ac X³z²-Bc XY²z³,
    g0=-lambda/(2Ac) (B XY⁴z^(-3)+A X³Y²z^(-4)).             (3)

Here C=Ac,D=-Bc are the universally forced symplectic relations for the actual cubic tensor. The divisor theorem identifies g0 with the actual quotient-line trivialization, not with a replacement model.

The actual regular target changes g_x=g0+p_x f and g_y=g0,y+p_y f_y are

    p_x=lambda XY/(2Ac z⁴)-lambda X²/(2A z²)
          +lambda B Y²/(A²z),
    p_y=-lambda Y²/(2Ac²w²)+lambda X²/(Bc²w),
    w=-1/z,   f_y=z^(-3)f,   g0,y=z^5g0.

The corrected Hessian primitive transforms as v_target=v_source+tau(f,p)/16. Direct universal identities give

    tau(f,p_x)/16=-lambda X/(8cz⁴)+7B lambda c Xz/(8A),
    tau(f_y,p_y)/16=lambda X/(8cw)+7lambda Yw/(8c²).

Consequently the source primitive is EXACTLY

    v0=lambda X/(8cz⁴),                                    (4)

because its regular target values are

    v_x=7B lambda c Xz/(8A),   v_y=7lambda Yw/(8c²),

where v0,y=z^5v0. Regularity holds on both complete standard charts. Since the coefficient bundle Wprime O(-5) has no global sections, two such primitives cannot differ. Together with the actual gluing/matching theorem this identifies (4) with the unique actual primitive, rather than choosing a convenient local correction.

## 3. The actual scalar inverse and corrected cone operator

Let e be the nonzero actual socle scale. In s=1 coordinates its apolar tensor identities give

    Q(X⁴)=e[-(B/(2A))XYz²-(B/(2Ac))Y²],
    Q(X³Y)=(e/4)[X²z+(B/A)Y²z²],
    Q(XY³)=(e/4)[-(A/B)X²+Y²z],
    Q(h)=-(e/2)XYz.

The correct coefficient-line action on O(2) is

    Lie_a=2a d/dz-2a_z.

For a=z² it sends z to -2z². Therefore the actual inverse of
Q(u)=k a Lie_a(Q(h)) is

    u=-(2kA/B)X⁴z²-(2kA/(Bc))X³Y-(2k/c)XY³z.               (5)

Substitution verifies this identity. The actual H0(Q(2)) is an isomorphism, so (5) is THE actual u. In particular u is not zero.

Set H=k a h, D=2a d/dz+(a_z/2)Euler, and

    Lambda=2k a a_z h-u.

The exact section-line identity h f_z=m_h f+n_h g0 has

    n_h=(Az/lambda)(c²z⁴X²+4cz²XY-Y²).

Define

    m=2k a²m_h+(3/2)k a a_z h,
    A12=-2k a²n_h,   A11=Lambda/2-m,
    A21=((Lambda-m)g0-H Dg0)/f.

In this input the last expression is the polynomial in positive coordinates

    A21=-lambda k X²Y²(2AX²+3BY²z)/(2ABc²z⁴).               (6)

Both rows of H D sigma+Aconn sigma=(Lambda/2)sigma hold identically. This verifies the full corrected connection, including the lower end action, rather than only its diagonal.

## 4. Physical scalar and absolute normal error

The natural determinant O(2) connection contributes -2a_z H. Thus the PHYSICAL nilpotent-line scalar is lambda_line=-u, while its local effective coefficient is Lambda=2a_zH-u. Choose the global physical harmonic lift -L(u). Since a_z is a base scalar, the effective local lift is exactly L(Lambda), with zero first-normal coefficient Lambda1. This is a globally compatible scalar choice, not the deletion of an arbitrary local scalar term.

Keep rho=2a_z in Dqcone=rho qcone. Then H rho-Lambda=u. In the universal harmonic normal-error formula the degree-eight diagonal is

    r0= tau(H,D(fg0))/462
          +tau(A12,g0²)/198+tau(A21,f²)/550
          -tau(Lambda,fg0)/462
          +H D(t11)+u t11+A12 t21-A21 t12.                (7)

All harmonic multiplication terms and both operator end actions are present. The arbitrary first-normal operator connection contributes K12g0²+K21f², which vanishes in the intrinsic canonical-module quotient. The PHYSICAL error is r0/nu, because (7) divided by qcone rather than q0.

For the fixed globally compatible positive Gram coordinates nu is constant; induced physical equation frames scale the numerator and q0 together. Nothing here sets nu=1 or ignores its physical factor.

## 5. Explicit absolute section and its global verification

Formula (7) simplifies to

    r0=-lambda k P/(30ABc²z⁴),                            (8)

where

    P=6A³c²z⁴X⁸+12A³cz²X⁷Y+6A³X⁶Y²
       -18A²Bc²z⁵X⁶Y²-2A²Bcz³X⁵Y³+21A²BzX⁴Y⁴
       +18AB²c²z⁶X⁴Y⁴-32AB²cz⁴X³Y⁵+24AB²z²X²Y⁶
       +4B³c²z⁷X²Y⁶-18B³cz⁵XY⁷+9B³z³Y⁸.

The actual double-cubic coordinate of the section is

    r0/(nu g0²) on (f²=0), in O_(2D)(-2,10).                (9)

The following STRONGER checks establish globality, instead of inferring it from a local formula:

1. In the oriented opposite chart, a_y=1, u_y=z^(-2)u, v0,y=z^5v0. Direct recomputation of (7) gives the EXACT coefficient identity r0,y=r0,x after w=-1/z. Hence (9) has precisely the required base factor z^(-10).
2. Recompute (7) in each ACTUAL regular target using g_i and v_i. The resulting r_i is polynomial in the chart coordinate and in X,Y on both charts.
3. On both charts the entire finite difference

       (r_i g0²-r0 g_i²)/f²

   is polynomial in X,Y, with meromorphic base coefficients. Thus r_i/g_i² and r0/g0² agree in the actual double-cubic line, not merely after a cup product or after taking cohomology. This is the full canonical-module source-change comparison from the intrinsic regular-pair quotient. It does not replace g by g_i in a fixed denominator ideal.
4. The full error, including its off-diagonal entries, satisfies the exact tangent equation 2fg0 r0+g0²R12-f²R21=0. Its off-diagonal entries are respectively divisible by f and g0. Thus it is genuinely the tangent error used in the global boundary sequence.

The full-frame midpoint matching, normal-conjugacy calculation in Section1, actual scalar choice, and these regular-target identities identify (9) with the ACTUAL midpoint normal-error section. A different compatible odd midpoint scalar lift changes it only by the scalar A image. The actual global quotient

    H0(M_-)/A = Cminus

therefore determines the full midpoint class, including information lost by the coefficient boundary to H1(P4 O(-4)). No subtraction of the polynomial nine-space is allowed.

This calculation has not reconstructed the endpoint normal-variation P4, subtracted the nonzero canonical third source correction, or carried out the next normal division. It proves no value for beta4.

## Verification

Run python verify_midpoint_absolute_square_error.py. It checks the complete harmonic conversion bases, the actual scalar-inverse identity with its full coefficient-line action, both exact section-line equations, the unique Hessian primitive, the explicit numerator, exact opposite-chart covariance, both full regular-target double-cubic transition identities, regularity, and the full tangent equation. All actual tensor parameters remain symbolic throughout.
