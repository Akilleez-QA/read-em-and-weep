# An apolar representative of the actual lowest normal class

## Result and scope

The actual lowest vertex normal-class line has an explicit, fully normalized universal representative, together with the scalar lifts of its nilpotent trace shadow. All source parameters remain unassigned. The actual class is a NONZERO scalar multiple of this representative; its absolute normalization is not asserted.

This makes both inputs to the lowest secondary operation available: the adjoint cocycle eta_8 and scalar primitives n_i satisfying delta n = tr(N eta_8). It does not discard the trace-correcting adjoint lifts K_i in the subsequent operation, identify a second-normal connection, or evaluate the endpoint or fourth Bockstein.

The calculation is uniform for the whole order-five stabilizer orbit. X,Y,s,t are arbitrary normalized abstract eigenvectors. No actual coefficient is assigned and no actual-instance matrix or rank is evaluated.

## 1. The actual extension and its sextic kernel

Use z=t/s and the divisor frame of the actual two-chart quintic theorem. Put d=Bc^2/A, with A,B,c,lambda nonzero symbols. The regularizers, with the second expressed in the first coefficient frame, are

    p_x=lambda XY/(2Ac z^4)-lambda X^2/(2A z^2)
          +lambda B Y^2/(A^2 z),
    p_y^x=-lambda Y^2/(2Ac^2 z^6)-lambda X^2/(Bc^2 z^7).

Thus the actual quintic extension cocycle is e=p_y^x-p_x. Its three quadratic coefficients are

    e/lambda = X^2[-z^-7/(Bc^2)+z^-2/(2A)]
               -XY z^-4/(2Ac)
               +Y^2[-B z^-1/A^2-z^-6/(2Ac^2)].           (1)

The established actual coefficient bundle has exact sequence

    0 -> V O_L(-10) -> J_eta -> O_L(-2) -> 0,
    J_eta = P4 O_L(-8).

Its extension is twice (1), because r transforms as r+2pd for a matrix [[d,0],[r,-d]]. After twisting by eight, the connecting map from H0(O_L(6)) to V H1(O_L(-2)) is twice multiplication by e followed by the z^-1 coefficient. The factor two does not change its kernel. Formula (1) gives precisely

    R_0=1-2d z^5,  R_1=z+(d/2)z^6,
    R_2=z^2,       R_4=z^4.                              (2)

Indeed the three coefficient conditions for R=sum r_j z^j are

    r_6=(d/2)r_1,  r_3=0,  r_5=-2d r_0.

This is the actual P4 summand of Sym^6 W, not a guessed invariant four-space. Its identification follows from the exact actual extension and the known splitting J_eta=P4 O(-8).

## 2. Complete adjoint basis, including lower entries

Let K_i=[[R_i,0],[r_i,-R_i]] be the corresponding global sections of J_eta(8). In the meromorphic divisor frame their lower entries are

    r_0=lambda[A X^2 c z^2-A XY-2B Y^2 c z^3]/(A^2 c z^4),
    r_1=lambda[2A X^2 c z^2-2A XY+B Y^2 c z^3]/(2A^2 c z^3),
    r_2=-lambda XY/(Ac z^2),
    r_4=0.                                               (3)

The exact regularity checks are

    r_i+2p_x R_i is polynomial at z=0,
    z^2(r_i+2p_y^x R_i) is polynomial in w=-1/z.

The factor z^2 is the coefficient transition of V O(-2), whereas the diagonal transition is z^-6. These are the physical line factors for J_eta(8). The overlap condition is exactly the vanishing of the z^-1 coefficient of eR_i. There is no additional choice: the difference of two such lifts lies in H0(V O(-2))=0.

Consequently (3) retains the complete associated-homogeneous adjoint, not just its diagonal. This is still an associated-homogeneous object; higher actual conic-frame terms are not identified with zero.

## 3. The invariant apolar cocycle

Use the standard invariant apolar form on Sym^6 W,

    <z^i,z^j> = (-1)^i/binomial(6,i) if i+j=6,
                0 otherwise.

On the basis (2), the only nonzero pairings are

    <R_0,R_1>=5d/6,   <R_2,R_4>=1/15,

and their symmetric counterparts. The induced invariant inclusion of P4 into (Sym^6 W)^* gives the following Cech coefficients in O(-8):

    epsilon_0=3/(5z)-1/(5d z^6),
    epsilon_1=6/(5d z^7)+2/(5z^2),
    epsilon_2=z^-3,
    epsilon_4=z^-5.                                      (4)

Explicitly, the z^-1 coefficient of epsilon_i R_j is delta_ij. The apolar construction, not just this duality condition, makes the inclusion equivariant: it is the dual of the orthogonal projection Sym^6 W -> P4. Thus

    eta_8 = sum_i K_i epsilon_i                          (5)

is the canonical identity tensor on P4, viewed in H1(J_eta). It spans the invariant line. Its diagonal is

    D_eta=4/z+1/(d z^6)-d z^4.                            (6)

In H1(O_L(-2)), (6) is 4[1/z]. The coefficient four is the trace of the rank-four identity tensor in this normalization, not a numerical normalization of the actual ambient normal extension. The earlier actual nonzero-diagonal theorem proves that the actual lowest normal class is c_eta[eta_8], with c_eta nonzero.

## 4. Compatible nilpotent-shadow scalar lifts

Keep the same trace convention q(K)=tr(NK), where

    f=A X^2Y+B Y^3z+Ac X^3z^2-Bc XY^2z^3,
    g=-lambda(B XY^4 z^-3+A X^3Y^2 z^-4)/(2Ac),
    N=[[fg,-f^2],[g^2,-fg]].

Write R_eta=sum r_i epsilon_i. Then

    q(eta_8)=2fg D_eta-f^2 R_eta.                         (7)

This is a degree-eight scalar of physical twist zero, whose coefficient line is O_L(-4). Direct universal expansion shows that the coefficients of z^-1,z^-2,z^-3 in (7) all vanish. Define

    n_x = minus the nonnegative Laurent part of (7),
    n_y^x = the Laurent part of (7) of powers at most -4. (8)

Then n_y^x-n_x=q(eta_8), n_x is regular at zero, and z^4 n_y^x is regular at infinity. Thus (8) are actual compatible scalar lifts of a section of the degree-eight piece of O_(2Z), in the stated normalization. The verifier prints their complete polynomial expressions.

Their quotient classes glue because (7) is in the actual square ideal. They are unique since H0(Sym^8(Wprime) O_L(-4))=0. Their common quotient section is nonzero: otherwise (5) would be a coboundary through the actual trace isomorphism J_eta=(I_Z^2)_8, contradicting (6). Equivariance follows from (5), naturality of the trace, and this uniqueness. Hence they represent the invariant nilpotent shadow line, with the same scalar normalization as eta_8.

## 5. Exact next interface

In the lowest endpoint formula, the normalized homogeneous operation must use BOTH (5) and (8):

    tau(gamma_4)=L_4 eta_8-delta K,
    q(K_i)=T_4(n_i).

The actual scalar c_eta multiplies this entire expression. Dropping K_i is invalid, since their diagonal degree is exactly four. The formulas above do not solve this last equation or evaluate its P4 cohomology class. They do remove the former unspecified choice of lowest eta and its trace primitives.

## Dependencies and reproduction

The actual divisor and regularizers are in UNIVERSAL-DIVISOR-QUINTIC-TWO-CHART-SHADOW-CANCELLATION.md and ACTUAL-MEROMORPHIC-QUINTIC-SOURCE-CHANGE-PRESERVES-VECTOR-CLASS.md. The associated bundle and actual nonzero comparison are in ACTUAL-NORMAL-CLASS-HAS-A-NONZERO-LOWEST-VERTEX-DIAGONAL.md. The endpoint target and full secondary formula are in ACTUAL-ENDPOINT-QUOTIENT-IS-LOWEST-VERTEX-COHOMOLOGY.md.

Run python verify_lowest_normal_class_apolar_reconstruction.py. It checks every displayed universal identity, the apolar tensor, complete lower-entry chart regularity, all three forbidden scalar Laurent coefficients, and both scalar-lift transports. No source parameter is specialized.
