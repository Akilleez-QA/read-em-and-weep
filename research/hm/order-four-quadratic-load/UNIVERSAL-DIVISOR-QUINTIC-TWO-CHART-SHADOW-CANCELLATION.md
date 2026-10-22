# Universal cancellation for the divisor-defined quintic in two charts

## Status and exact scope

This note proves a universal polynomial identity for the FULL previously established vector cochain R. It does not assign values to actual HM/source coefficients, construct an actual-instance matrix, or evaluate a rank. All A,B,c,lambda,k below are arbitrary nonzero symbols, with the sole cubic symplectic relation absorbed by C=Ac and D=-Bc.

The identity is stronger than a cancellation of one isolated scalar term: it retains the source m, the actual scalar correction Gamma, the Gram primitive, every quadratic transition term, and the opposite-chart orientation. Its resulting two principal parts become globally removable after cup by the square a.

The geometric comparison in Section5 identifies the precise actual-class input. It has now been independently checked in ACTUAL-MEROMORPHIC-QUINTIC-SOURCE-CHANGE-PRESERVES-VECTOR-CLASS.md, and ACTUAL-THIRD-BOCKSTEIN-VANISHES-ON-SQUARE-DIRECTIONS.md records the resulting actual square-channel vanishing. In particular this note is not a complete original proof repair, and it says nothing about the other cubic channel which vanishes on every square.

## 1. An actual divisor formula and a universal rational lift

Use an arbitrary order-five stabilizer and its abstract eigenspace lines, as in the C5 correction theorem. The cubic tensor is

    f=A X^2Y s^3+B Y^3 s^2t+Ac X^3 st^2-Bc XY^2 t^3.

On the product of the two projective lines set z=t/s, r=Y/X and u=r/z^2. On the actual cubic support,

    z^5=-(A/B)(u+c)/(u^2(u-c)).

The four ramified corners P0,P_infinity,P_c,P_-c have orders of (z,r)

    (-2,1), (2,-1), (-1,-2), (1,2), respectively.

Thus div_D(X)=2P_c+P_infinity and div_D(s)=P_c+2P0. The rational section

    (X/s)^5 u^2/(u-c)

of O_D(5,-5) has zero divisor. Since the actual quintic gives a nowhere-zero section of the same line and H0(O_D)=C, it agrees with that section up to a nonzero lambda. This is a divisor identity, not a choice of an actual coefficient.

On s=1, the universal relation

    f=(Y-cXz^2)(BzY^2+AX^2)+2AcX^3z^2

gives the following rational polynomial representative of that section:

    g0=-lambda/(2Ac) [B XY^4 z^(-3)+A X^3Y^2 z^(-4)].     (1)

It is a meromorphic lift in the actual quintic ideal extension, with poles only at the two fixed base points. Equality on D shows that any other lift differs by f times a quadratic; no split replacement of the quintic extension is made.

## 2. Exact relation coefficients, regular targets, and Gram primitive

For h=X^4, polynomial division gives the exact identity

    h f_z = m0 f+n g0,

where

    n=lambda^(-1)[X^2(-4Az+Bc^2z^6)+2Bc XYz^4-3B Y^2z^2],

    m0=(4Ac X^4z^2-4A X^3Y-Bc X^2Y^2z^3-3B XY^3z)
        /(2Ac z^3).                                      (2)

Define

    q_x=-lambda/(2Ac) XYz^(-4)
         +lambda/(2A) X^2z^(-2)-lambda B/A^2 Y^2z^(-1),
    p_x=-q_x.

Then g_x=g0+p_x f is regular on the entire s-chart. At the other point use the VOLUME-COMPATIBLE coordinate v=-s/t, so z=-1/v. The actual coefficient transforms are

    f_y=z^(-3)f,  g0_y=z^5 g0,  n_y=z^(-6)n.

Define

    p_y=-lambda/(2Ac^2) Y^2v^(-2)+lambda/(Bc^2) X^2v^(-1).

Then g_y=g0_y+p_y f_y is regular on the entire t-chart. The source relation there is

    h (f_y)_v = m0_y f_y+n_y g0_y.

The sign in this equation is the one for v=-s/t, not the raw derivative in s/t.

Use the fixed quadratic transvectant

    tau(P,Q)=P_XX Q_YY-2P_XY Q_XY+P_YY Q_XX.

The actual unique scalar primitive in the meromorphic g0 frame is

    v0=2B/A,     v0_y=z^2 v0=2B/(A v^2).                 (3)

Indeed the local target primitives are regular:

    v0+tau(p_x,n)=2B(-5A+2Bc^2z^5)/A^2,
    v0_y+tau(p_y,n_y)=-20v^3/c^2.

Their difference is the required actual transition cocycle. Uniqueness follows from H0(O_L(-2))=0, exactly as in the Gram-primitive theorem. Thus (3) is not the unjustified choice v0=0.

The actual global scalar correction in the s-chart is

    u=4kB/(Ac) XY^3z^2+4k/c X^3Yz.

For a=z^2, its effective local value is

    Gamma=u+4k z^3 X^4.

In the oriented other chart a=1 and Gamma_y=z^(-2)u. These are the actual scalar-correction and frame formulas, not a divided or locally substituted correction.

## 3. Evaluate the complete universal transition identity

For a source relation m,n, source primitive v0, and transition p, use the established formula

    R=k a^2[-2 tau(p,m)/15+2p tau(p,n)/5+tau(p,p)n/5
             -tau(h,p_z)/15+(2/3)p v0]-tau(p,Gamma)/30. (4)

Use (1)-(3) as SOURCE data. In the opposite chart replace z-derivatives by v-derivatives and use its transformed source m0_y,n_y,v0_y,Gamma_y. No target m is silently substituted for source m.

A universal expansion gives, with

    alpha=B k lambda/(10A^2c^2),

    principal_part_x(R_x)=alpha Y^2 z^(-2),
    principal_part_y(R_y)=-4alpha Y^2 v^(-4).            (5)

There are NO other polar terms. In particular the cubic and simple polar coefficients cancel only after all terms in(4) are retained. This is checked symbolically with A,B,c,lambda,k left unassigned in the companion verifier.

For reproducibility the complete expressions are

    R_x=B k lambda/(10A^4c^2z^2) [
      -33A^2c^2 X^2z^4-10A^2c XYz^2+A^2Y^2
      -16ABc^4 X^2z^9-8ABc^3 XYz^7-8ABc^2Y^2z^5
      +16B^2c^4Y^2z^10 ],

    R_y=-2k lambda/(5A^2Bc^4v^4) [
      28A^2X^2v^6-16ABY^2v^5+B^2c^2Y^2 ].

The scale alpha is nonzero but its value is not chosen.

## 4. Exactness after cup, and the final local tests

As a statement about the vector principal parts in H1(V O_L(-6)), (5) has the following consequence. Cup by a has local expressions z^2 at x and1 at y. The x part becomes regular. The remaining y part is

    -4alpha Y^2 v^(-4).

This is the y expression of the GLOBAL MEROMORPHIC section of V O_L(-4) whose x expression is the constant -4alpha Y^2, because the coefficient transition is multiplication by z^4=v^(-4). That section is regular on the x-chart and has exactly this principal part on the y-chart. Hence the cup of the principal-parts class is zero in H1(V O_L(-4)), before quotienting by the connecting D5 or second-symbol image.

There is a compatible direct final-test check. The actual P4-complement of the quartic quotient tensor gives

    i^t c_x proportional to Y^2s^2-2c XYt^2.

One can obtain the ratio by pairing with Q(Y^4) in the invariant tensor-product apolar form; this is not a matrix evaluation. Thus, up to one common nonzero scale,

    zeta_x=Y^2z^2-2c XYz^4,
    zeta_y=Y^2v^2-2c XY.

Both full pairings tau(R_x,zeta_x) and tau(R_y,zeta_y) are regular, not merely of zero residue. The vector exactness above does not require this ratio.

The physical equation factor must remain. In fixed global positive Gram coordinates q0=nu q, nu is one fixed nonzero scalar; the physical cochain is R/nu, so every displayed exactness statement is unchanged. On induced relative frames q0 and q transform together, preserving that ratio. If a different equation frame is used, it must be transported rather than inserting an arbitrary nonconstant scalar into(5).

## 5. The actual-class comparison

The finite transition identity proved in ACTUAL-POLAR-VECTOR-PARTS-DO-NOT-DEPEND-ON-REGULAR-QUINTIC-LIFTS.md is

    R(p+q;m,v)-R(p;m,v)=R(q;m-pn,v+tau(p,n)).            (6)

Take the common meromorphic source to be g0 and the two regular targets to be g_x,g_y. On their overlap, (6) identifies the actual target-to-target cochain with the difference of the two meromorphic expressions R_y and R_x, in their transported coefficient frames. Thus their principal parts represent that actual cochain. This argument does NOT assert that the original orthogonal polar principal parts glue to a global differential.

The required full-frame input is precisely the published harmonic-transition theorem: diagonal base/root-line frame discrepancies have zero harmonic correction, source m and target trace frames are kept distinct, normal centralizers do not change the square shadow, and the physical nu is retained. The separate source-change theorem explicitly checks the affine m and Gamma terms under v=-1/z and proves R_y=z^6 R_x. Thus with that input applied to the meromorphic section g0, no additional transition term remains. The actual scalar primitive is fixed by(3), and the actual u by the C5 theorem.

With this actual Serre/normal-frame comparison, Section4 proves prequotient cup vanishing for the detectable input at every square rooted at a point of E. The companion actual theorem uses character detection for the other inputs, followed by the existing basepoint exclusion, to prove vanishing of the entire square channel. It does NOT exclude the separate discriminant-divisible cubic channel, which remains open at this package cutoff. The promotion is recorded separately so the universal algebra is not mistaken for the full geometric comparison.

## Reproduction

Run python verify_divisor_quintic_two_chart_cancellation.py. It checks the exact polynomial relation, both regular quintic targets, both regular Gram primitives, the entire R expression in both oriented charts, the absence of every other polar term, and the global removal after cup. All parameters remain formal. No HM coefficient selection, source-instance matrix, rank test, scan, or local-model replacement occurs.
