# Structural quotient projection on the six pinned carriers

## Result and exact boundary

For all six pinned rational carriers, the stored projection satisfies

    P_i = J_i^(-1) E_Di^t (Id15-gamma H0_i),
    P_i gamma = 0.

Here D_i is the two-coordinate normalization set and J_i=I_i[D_i,:]. The proof uses the independently established sparse retraction H0_i gamma=Id5, then identifies every actual P numerator with a handwritten universal projection formula. It does not assume primitive A, any A-dependent contraction identity, transition determinant normalization, or a historical computation receipt.

Together with the already structural support facts, this reduces the remaining A defect from four blocks with 130 scalar positions to three blocks with 120 scalar positions per carrier. None of those remaining blocks is proved zero here. This is a structural advancement, not a conclusion about the global obstruction.

All executable checks are immutable-byte and literal-record comparisons. No actual source matrix product, polynomial product or expansion, source specialization, source jet, production import was performed. The algebra below is a handwritten derivation in an abstract sparse linear system; the code only checks the signed factor-label templates against existing inert records.

## 1. Data and prior independent retraction

The input is the pinned `hm-pinned-model.json`, Git blob `fcd48a9a22d40d55ce7a08b8aefcb4eaa2fdf761`, SHA256

    635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926.

The included local model is byte-identical to the previously authenticated input. This package does not independently fetch a newer remote source. The decoder means I=N_I/di, P=N_P/dp, H0=N_0/dh, H1=N_1/dh. All three denominator records di,dp,dh coincide on each carrier; the checker verifies that literal fact.

Use the exact six sets

    F0=(1,4,7,8,10), D0=(0,5),
    F1=(0,2,8,9,11), D1=(1,6),
    F2=(1,3,5,9,12), D2=(2,7),
    F3=(2,4,5,6,13), D3=(3,8),
    F4=(0,3,6,7,14), D4=(4,9),
    F5=(4,7,8,10,11), D5=(5,14).

S_i is the increasing eight-coordinate complement of F_i union D_i. Work over Q(v1,v2,v3,v4), with v0=1, or the polynomial ring localized at the stored denominator. The preceding retraction theorem, proved by four-cycle and triangular elimination and all-entry literal comparison, gives

    G_i=E_Fi^t gamma invertible,
    H0_i=G_i^(-1)E_Fi^t,
    H0_i gamma=Id5.

That theorem is independent of A. Its proof and local independent review are included as inert evidence snapshots. The literal normalization is

    J_i=diag(1,v_i), i=0,...,4,
    J_5=diag(1,-v4/v1^2).

The current checker independently verifies the relevant I[D,:] records as well as all P records. No equality about the full I arrays is inferred from cyclic symmetry.

## 2. Universal primary projection

Take formal labels t,a,b,c,d and denominator

    Delta=t*a*b*c*d-t^5.

Given the five selected coordinates yA,yB,yC,yD,yE, let x=(x0,...,x4) be the unique solution of

    yA=b*x3+t*x4,  yB=t*x1+c*x2,
    yC=-d*x1-t*x3, yD=-t*x2-a*x4, yE=t*x0.

The independent sparse inverse theorem gives

    Delta*x1=-a*c*t^2*yA-t^4*yB-a*b*c*t*yC-c*t^3*yD,
    Delta*x2= a*t^3*yA+a*b*d*t*yB+a*b*t^2*yC+t^4*yD,
    Delta*x3= a*c*d*t*yA+d*t^3*yB+t^4*yC+c*d*t^2*yD,
    Delta*x4=-t^4*yA-b*d*t^2*yB-b*t^3*yC-b*c*d*t*yD.

Let z0,z1 denote the two coordinates in D. The two additional selected gamma equations are

    z0=a*x2+d*x3,
    z1=-c*x1-b*x4.

Consequently the coordinate projection along im(gamma), normalized by J=diag(1,t), is

    q0=z0-a*x2-d*x3,
    q1=(z1+c*x1+b*x4)/t.                           (1)

This is precisely J^(-1)E_D^t(Id-gamma H0), defined on the whole ambient space. Inserting the four inverse formulas into (1) gives the following explicit numerator coefficients over Delta:

    Delta*q0 = Delta*z0
       -(a^2*t^3+a*c*d^2*t)*yA
       -(a^2*b*d*t+d^2*t^3)*yB
       -(a^2*b*t^2+d*t^4)*yC
       -(a*t^4+c*d^2*t^2)*yD,

    Delta*q1 = (a*b*c*d-t^4)*z1
       -(a*c^2*t+b*t^3)*yA
       -(c*t^3+b^2*d*t)*yB
       -(a*b*c^2+b^2*t^2)*yC
       -(c^2*t^2+b^2*c*d)*yD.                       (2)

There is no yE term. This table is a handwritten consequence of the universal inverse; no stored physical numerator was multiplied by another.

For primary carrier r, substitute the label map

    (t,a,b,c,d)=(v_r,v_(r+1),v_(r+2),v_(r+3),v_(r+4)),

with indices modulo five and v0=1. The domain labels x0,...,x4 mean actual coordinates (r,...,r+4) modulo five; the selected ambient coordinates are

    (yA,yB,yC,yD,yE)
       =(u_(r+1),u_(r+4),u_(5+(r+2)),u_(5+(r+3)),u_(10+r)),
    (z0,z1)=(u_r,u_(5+r)),

where within-block indices are reduced modulo five. Literal gamma_D entries give exactly the two extra equations above. The stored dp is exactly Delta. All 30 stored P cells for each of the five primary carriers agree with (2), including every empty coefficient. The metadata comparison counts formal factor labels after relabeling and discards label v0; it constructs no products of stored polynomials.

Thus the actual P_r equals the projection (1) on every primary carrier, on the entire ambient vector space.

## 3. Auxiliary projection

Write a=v1,b=v2,c=v3,d=v4 and Delta5=-a^2*c*d. For the auxiliary selected coordinates (y4,y7,y8,y10,y11), the independently established inverse gives

    x0=y10, x1=y11/a,
    x2=y4/c-y11/(a*c),
    x3=-y7-d*y11/a,
    x4=-y4/(a*c)-y8/a+y11/(a^2*c).

Here D=(5,14), z0=u5,z1=u14, and the additional gamma equations are

    z0=-c*x1-b*x4,  z1=d*x4.

Since J=diag(1,-d/a^2), the normalized projection is

    q0=z0+c*x1+b*x4,
    q1=-(a^2/d)*z1+a^2*x4.                         (3)

In the actual common denominator normalization, its nonzero numerator coefficients are

    Delta5*q0=Delta5*z0+a*b*d*y4+a*b*c*d*y8
                         -(a*c^2*d+b*d)*y11,
    Delta5*q1=a^4*c*z1+a^3*d*y4+a^3*c*d*y8-a^2*d*y11.  (4)

Every one of the 30 stored auxiliary P cells agrees with (4), and the selected gamma_D and I_D entries match the equations and J. This proves P_5=J_5^(-1)E_D5^t(Id-gamma H0_5) on the whole ambient space.

## 4. Immediate consequences

Equations (1)–(4), bound to all six source records, prove

    P=Q:=J^(-1)E_D^t(Id-gamma H0).                  (5)

Using the already proved H0gamma=Id5,

    Pgamma=J^(-1)E_D^t(gamma-gamma H0gamma)=0.

This calculation is formal algebra from the newly established projection identity; it is not evaluation of the source product Pgamma.

The literal support facts I_F=0, H1_(F union D)=0 and P_S=0, together with I_D=J and H0=G^-1E_F^t, also give

    PI=Id2, PH1=0, H0I=0, H0H1=0.

Hence the map gamma H0+IP is an idempotent with image im(gamma) direct-sum im(I). More explicitly,

    ker(H0) intersect ker(P)=span(E_S),
    Id-gamma H0-IP is the projection onto span(E_S)
       along im(gamma) direct-sum im(I).

To see the kernel statement, H0u=0 forces u_F=0; then (5) gives Pu=J^-1u_D, so Pu=0 forces u_D=0. This identifies the geometric meaning of the remaining eight-dimensional complement without invoking A or delta.

## 5. Exact remaining A obligation: three blocks, 120 positions

Set N=[gamma,I,E_S]. It is invertible independently of A: in ambient row order (F,D,S), it is block lower triangular with invertible diagonal blocks G,J,Id8. The new identity (5) means that its first two block rows are exactly H0 and P. Write its final block row as

    Z=E_S^t(Id-gamma H0-IP).

Then

    N^-1=[H0;P;Z].

Define the primitive defect R=gamma H0+IP+H1delta-Id15. Since H1 is supported on S, exact abstract block algebra gives

    N^-1 R N =
        [ 0             0          0               ]
        [ 0             0          0               ]
        [ H delta gamma H delta I  H delta E_S-Id8 ],

where H=E_S^tH1. This is unconditional after the newly proved retraction/projection and support data. It has 8x5+8x2+8x8=120 possible scalar positions per carrier. This is an equivalent block presentation, not an independence or minimal-generator claim.

Retain the independently proved pivot splitting and C: ev delta=0. They give delta=W L delta. Put

    T=E_S^tH1 W, M=L delta E_S.

The lower row becomes

    [T L delta gamma, T L delta I, T M-Id8].         (6)

The direct sparse-minor identities, independent of A, are

    det M=-v_r^3*dh_r on primary chart r,
    det M=-v3*v4 on the auxiliary chart.

They make M invertible on the same denominator localizations. The already literal B, H1eta=0, makes T readable directly as the selected nonpivot columns of H1, although B is not needed for delta=W Ldelta.

It follows that A is equivalent to the three remaining families

    L delta gamma=0      (8x5),
    L delta I=0          (8x2),
    T M=Id8              (8x8).                     (7)

Necessity uses TM=Id8 to infer T=M^-1 and hence T invertible; sufficiency follows directly from (6). Under C, the first two identities are equivalent to delta gamma=0 and delta I=0 respectively. No claim is made here that any of (7) has been independently proved. In particular delta gamma=0 must not be imported from the A-dependent contraction theorem.

## 6. Evidence and limits

`check_projection_metadata.py` checks all 180 P cells, 60 selected gamma_D cells, 24 selected I_D cells, 18 denominator records, 60 I_F zero cells and 420 H1_(F union D) zero cells. Ordinary and optimized Python outputs are byte-identical. The checker has no polynomial arithmetic, matrix multiplication, evaluator, source specialization, jet code, production imports or disabled-under-optimization assertions. Its fixed hash rejects altered input bytes.

The invented control uses unrelated small rational matrices to check the projection and block formulas and demonstrate that the new identities can all hold while A fails. It is not a sample of the pinned model and is not a physical execution receipt.

This artifact proves the quotient annihilation family and identifies the exact residual obligations. It does not prove full A, geometric frame/localization premises, exact implementation semantics, retained-test values, or the global obstruction. The prior determinant-volume theorem retains its remaining A premise.
