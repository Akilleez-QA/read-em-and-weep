# General Cartan Euler symbols have a regular full U reconstruction

## Result, hypotheses, and boundary

Allowing the full Cartan-input block of a negative-quartic Euler symbol
removes the principal Cartan kernel-spinor test and the subsequent
M-right-divisibility test needed for a Spin-to-Cartan-only repair. It does
not make the full U equation automatic. There is an exact regular test,
and every passing raw full-U error has a unique repair in the stated
Euler/source sectors.

Use the definitions and physical markings in
`CLEAN-SOURCE-BALANCE-TENSOR-FOUNDATION.md`, whose helper was published in
PR697, commit 715bb7c683988da6cf220f26629b92d3575a0287. The full B-source
balance agrees with public PR698,
`NEGATIVE-EULER-REPAIRS-HAVE-A-CANONICAL-FULL-SOURCE-BALANCE.md`.
For uniqueness, use the public theorem
`PURE-NEGATIVE-EULER-CARTAN-ACTION-HAS-A-FULL-U-RIGIDITY-OBSTRUCTION.md`,
published in PR709 at 28a0859a148f28c0b821663df3f84fbb07f3f31e. The new verifier imports only the
public foundation helper, not the rigidity verifier or any unpublished
actual-family computation.

Keep the actual nonzero scales a_m,b_m,c_m. Let the raw middle T0 satisfy
T0 A=0, and suppose its entire B output is i_x-closed and belongs to the
high homogeneous sector with coefficient degrees

    VV: (positive,negative)=(1,4),
    VW: (2,3),
    WW: (3,2).

It is linear in the complete U input p. No WW component is dropped.
The question is whether there are a negative-quartic six-space symbol K,
a negative-quartic source P:U->U, and a reverse source R:U->Sym^2 W of
degrees (1,3), such that

    (T0+T4(K))(a_m A+b_m B)
        =(a_m A+b_m B)P+c_m C R.                         (1)

Only these middle and U-source sectors are being classified. The result
is not an unrestricted cochain obstruction or an actual-family membership
calculation. The c column is retained below as an additional exact test
and companion, not asserted to vanish.

## 1. Canonical principal reconstruction

Normalize the full raw high error, without changing any physical marking,
by

    E=(b_m/a_m)T0 B.

There is a unique negative-quartic endomorphism Y of V6 with

    E_VV(v,p)=Y(w)A(v,p),                                (2)

because the coefficients A(v,p)=v tensor p identify V tensor U with V6.
This is ordinary coefficient extraction, not restriction to a conic or
an assignment of an actual input.

The first test is the full spin-source identity

    cliff Y A(v,p)=(M(v)P+P^dagger M(v))p.                (3)

It determines P uniquely if it holds, by the following regular
coefficient inverse. Write

    cliff Y A(v,p)=(x S0+y S1+z S2)p

in the frozen Clifford frame M0,M1,M2. Define

    P=[[S1[1,0]/2, -S1[0,0]],
       [S0[0,0],    S0[0,1]/2]],                         (4)

and check all three equations Si=Mi P+P^dagger Mi. Formula (4) uses
zero-based matrix entries. It is an exact left inverse on the allowed
image, not a replacement for the remaining equations. Equivalently,
the scalar-matrix output and the trace-pairing selfadjoint trace-free
part of the induced sl(U) map must vanish. There are eight spin tests
per negative quartic coefficient, hence forty in total; no actual
matrix or rank is needed for this statement.

If (3) passes, put

    K0=I_V tensor P-Y.                                   (5)

Then K0 cancels all principal VV terms with reverse source initially
zero, including every Cartan-input contribution. The full low equation
is already correct:

    T4(K0)B=B P.                                        (6)

Indeed the general full low identity is

    T4(K)B(p)=-3 i_x[(up adj6(K) spin p) wedge omega_W],

and (3) is exactly adj6(K0)spin=-spin P. More explicitly, if

    Gamma=cliff Y-cliff(I_V tensor P)-P^dagger cliff,

then

    3(adj6(K0)spin+spin P)=J6^(-1) Gamma^t J.

Thus (6) includes mixed and WW coefficients, not just a spin projection.

The entire remaining high error is the source-independent tensor

    D=E-T4(Y)A.                                         (7)

This follows from the full identity
T4(I_V tensor P)A=A(P), including all coefficient derivatives. In
particular no principal Cartan kernel-spinor condition survives at this
stage. That condition belonged to the smaller Cartan-annihilating repair
space, not to the general Cartan-input space used here.

## 2. The exact remaining full-tensor tests

The tensor D is i_x-closed and has VV=0. Write D3,D4 for its mixed
positive-one-form coefficients at du,dw. There is a unique regular
positive one-form L, with coefficient degrees (2,2), such that

    L=(partial_u D4-partial_w D3)/4,
    D=-i_x(L wedge omega_W).

Equivalently,

    D_mixed=L wedge j,       D_WW=-i_v L,
    j=-w du+u dw.                                        (8)

The denominator four is negative coefficient degree two plus two.
Closure gives uD3+wD4=0; the two-variable polynomial Koszul identity
and Euler homogeneity prove (8). No division by u, w, or a raw coefficient
is used.

The second test is

    D_WW=0, equivalently i_v L=0.                        (9)

This is necessary: the available principal-invisible Euler/reverse-source
combination has no WW term. Keeping the full raw WW input is therefore
essential, even though it vanishes for some narrower operator families.

There is a regular positive-Cartan inverse with which to state the third
test. Let d_v denote exterior differentiation in the positive coordinates,
acting on polynomial coefficients. For any i_v-closed positive one-form L
with positive coefficient degree two, define

    q_z=coefficient of z in cliff(d_v L),
    Q(L)=(d_v L-A(M2 q_z))/3.                            (10)

Here cliff(d_v L) means the six-space coefficient of its positive two-form,
followed by cliff. All negative coefficients and the complete input p are
retained during this coefficient extraction. Since M2^2=I in the fixed
marking and i_v A(s)=0, the positive Koszul identity gives

    i_v Q(L)=L.

The third test is exactly

    cliff Q(L)=0.                                       (11)

If it passes, Q(L) is the unique Cartan-valued positive-linear two-form
whose contraction is L. To prove uniqueness, any zero-contraction
positive-linear two-form is A(s) for a positive-constant spinor s. If it
is Cartan, M(v)s=0; its z coefficient and invertible M2 force s=0.
Formula (10) is also checked directly on every free Cartan coefficient.

Unlike the smaller Spin-to-Cartan-only test, neither (9) nor (11)
requires E M(v) to be divisible by q0. There is no M-right-divisibility
assumption, conic restriction, selected point, or curve normal form here.

## 3. The unique full correction

Let f:Sym^3 W->Cartan be the fixed invertible cubic marking, with no
rescaling. The notation f^(-1) below denotes its fixed linear inverse,
not division by a variable source coefficient. Put

    Z=-4 f^(-1) Q(L).

Thus Z has binary degree three, negative coefficient degree two, positive
coefficient degree one, and is linear in the whole U input. Define

    delta=S partial_u+T partial_w,
    Ebin=u partial_S+w partial_T,
    I2(Z)=Ebin Z-Ebin^2 delta Z/4+Ebin^3 delta^2 Z/36.

The adjacent-degree identity delta I2=I is exact on these binary and
negative degrees. Since I2(Z) is positive-linear and input-linear, there
is a unique cubic-coefficient map H:V6->Sym^2 W with

    H A(v,p)=I2(Z(v,w;p)).

Set

    ell=uT-wS,
    K=K0+f ell H,
    R(v,w;p)=-(a_m/c_m)H A(v,p).                         (12)

These are regular polynomial constructions. The fixed inverse marking
f^(-1), nonzero physical source scales, and displayed rational constants
are the only inverses used.

The full image-in-ell identity, valid for arbitrary Cartan and Spin input,
is

    T4(f ell H)A+C(H A)
        =(1/4)i_v[f(delta(H A)) wedge j],
    T4(f ell H)B=0.                                     (13)

Its right side is mixed-only. Equations (8)-(12) make it exactly -D.
Together with (6)-(7), this proves (1), with every source scale and the
entire low B companion present.

Conversely, any solution of (1) has low equation adj6(K)spin=-spin P.
Its principal equation forces

    K=I_V tensor P-Y+f ell H,
    R=-(a_m/c_m)H A,

for a unique H. Its spin projection forces (3); (13) then forces (9),
(11), and the reconstruction (12). Thus the three tests are necessary
and sufficient. The frozen pure-negative Euler rigidity theorem also
shows uniqueness directly: the difference of any two solutions has zero
raw middle and must have K=P=R=0 in precisely these sectors. No uniqueness
outside these sectors is claimed.

For orientation, the mixed-only closed space has dimension 96, while
the full H space has dimension 3*4*6=72. Injectivity follows from (10),
the fixed f inverse, and I2. The remaining exact mixed quotient therefore
has dimension 24. This replaces the 72-dimensional quotient for the
smaller Spin-input-only H=Q cliff family. These are universal coefficient
space dimensions, not actual-family ranks or computed obstruction values.

## 4. The additional low c-VV gate is not automatic

The reconstructed K preserves Cartan because cliff K=-P^dagger cliff.
It need not preserve the moving three-plane f(ell Sym^2 W). For the full
quadratic c input z define

    q_C=f^(-1)K f(ell z).

The low c-VV term of T4(K)C is -K f(ell z), of degrees (0,5). A source
S_AA=V_C(w) of negative degree four cancels it if and only if

    q_C=ell V_C.                                        (14)

No U-row source of the retained degree can cancel this low c-VV term.
The f ell H contribution already preserves this plane, so the gate can
also be checked on K0; it must still be checked.

This gate has a new regular inverse requiring no negative-coordinate
division. Let

    eps=partial_u partial_T-partial_w partial_S,
    Jell(q)=eps(q)/8-ell eps^2(q)/112+ell^2 eps^3(q)/2016.

For every q of binary/negative degrees (3,5), test

    q-ell Jell(q)=0.                                    (15)

The test is equivalent to (14), and the unique solution is V_C=Jell(q_C).
Indeed, for V of degrees (2,4),

    eps(ell V)=8V+ell eps V,
    eps^2(ell V)=14 eps V+ell eps^2 V,
    eps^3(ell V)=18 eps^2 V.

These identities prove Jell(ell V)=V coefficient by coefficient. They
are free binary polynomial identities, not curve division.

### Canonical normal form of the low-c preservation gate

There is a sharper whole-operator version of (14). Transport the Cartan
block by the fixed marking,

    T=f^(-1)K|Cartan f,
    lambda_w=(u^3,u^2 w,u w^2,w^3).

It preserves ell Sym^2 W if and only if

    lambda_w T=mu(w)lambda_w,

for a unique negative quartic mu. The scalar is recovered without
coordinate division by

    mu=(1/336) sum_(i=0)^3 binom(3,i)
          partial_u^(3-i) partial_w^i [(lambda_w T)_i].   (20)

For an arbitrary T, compute (20) and check the entire row identity; the
formula alone is not the test. Indeed applying its differential sum to
mu lambda_w multiplies every quartic coefficient of mu by 6*7*8=336.
The primitive row lambda_w guarantees that a rational proportionality
scalar forced by preservation is polynomial.

Equivalently there is the unique normal form

    T=mu I+ell H_CC,                                    (21)

where H_CC:Sym^3 W->Sym^2 W has negative coefficient degree three.
For each cubic column q of T-mu I, of binary/negative degrees (3,4), the
regular quotient in (21) is

    eps(q)/7-ell eps^2(q)/84+ell^2 eps^3(q)/1260.          (22)

The constants differ from Jell because the negative column degree is
four rather than five. Both inverses are checked with all their free
coefficients. The preserving space has dimension 5+48=53, with uniqueness
visible in (20)-(22), not established by a rank calculation. In this
normal form the forced c source is particularly simple:

    V_C(z)=mu z+H_CC(ell z).

Adding f ell H to a U repair only changes the ell H_CC summand. It never
changes whether the low-c gate passes, so the gate may be checked on K0
before performing the remaining mixed-U reconstruction. No actual family
is asserted to land in this 53-dimensional space.

## 5. The entire c companion, including its Cartan one-form

If (14) passes, set

    D_C=T4(K)C(z)-C(V_C(z)).

This tensor has VV=0. Its mixed and WW coefficient degrees are (1,4)
and (2,3). Write V3,V4 for its mixed positive-one-form coefficients and
put

    L=(partial_u V4-partial_w V3)/5,
    P_C=-(cliff low L)/3,
    L_C=up Pi low L.                                    (16)

The denominator is now five, not four. Closure and negative Koszul
reconstruction give the full identity

    T4(K)C(z)=C(V_C)+B(P_C)-i_x(L_C wedge omega_W).        (17)

In particular WW is retained in both terms on the right. The source
choices

    S_AA=V_C,             S_UA=(c_m/b_m)P_C

leave the literal c residual of this correction

    -c_m i_x(L_C wedge omega_W)
        -(a_m c_m/b_m)A(P_C).                            (18)

Including the raw middle, the full c residual is therefore

    c_m T0 C-c_m i_x(L_C wedge omega_W)
        -(a_m c_m/b_m)A(P_C).                            (19)

Equation (19) is an equality, not a claim that its terms vanish. If a
raw contribution occupies the same low degrees, it must be included in
the corresponding affine c equations rather than discarded. The
Cartan one-form L_C cannot be canceled by a B source alone, since the
spin and Cartan one-form coefficient spaces are complementary. Neither
passing the U reconstruction nor canceling the principal c coefficient
permits omitting this lower companion.

## Reproduction and scope

Run

    python verify_general_cartan_euler_reconstruction.py

The verifier uses universal free symbols for the raw six-space operator,
source endomorphism, positive-linear Cartan inverse, all cubic marking
coefficients, general H, low c quotient, and complete mixed/WW companion.
Tensor-factorized generic homogeneous coefficients span all directions
of the spaces asserted above; no coefficient is specialized to an actual
HM/source value. The standalone log records the exact checks.

The construction is complementary to actual operator-family work. It
provides no selected actual-family coefficients, actual-instance matrix
or rank, scan, forbidden spike, curve reduction, completed c solution,
fourth obstruction value, or unrestricted cochain exclusion. A particular
raw family must still pass the explicit spin, WW, mixed-Cartan, and
coupled c tests.
