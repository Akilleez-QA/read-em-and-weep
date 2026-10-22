# Universal Cartan–Koszul homotopy for the ambient At multiplier

**Checked construction.** This note gives an explicit polynomial solution of all five
channel equations in `UNIVERSAL-MONAD-HOMOTOPY-HAS-FIVE-CHANNEL-EQUATIONS.md`.
The proposed, tensor-marked result is

    C_mult = -chi/g_L,                                  (0)

where `M(v)^2=chi q0(v) I` and
`tr(M(xi)[M(eta),M(zeta)])=g_L tau(xi,eta,zeta)` use the
fixed b-channel Clifford tensor and fixed a-channel volume. The trace is the
full two-dimensional trace. Here chi and g_L are defined from the fixed
ALGEBRAIC tensor `M_alg=i_v L`; the pairing-defined cross operator equals it
in the compatible frame specified below. Neither chi nor g_L is normalized
away. All three monad parameters remain arbitrary nonzero symbols throughout.

This is a universal tensor construction, not a source-instance matrix or rank
calculation. The accompanying verifier checks complete polynomial identities
with every representation coefficient free. Its normalization conventions are
explained in Section 7; the actual invariant cubic is never evaluated.

## 1. Inputs and conventions

Use the channels A, B, C and determinant markings of
`UNIVERSAL-MONAD-CLIFFORD-HOMOTOPY-AND-HAMILTONIAN-DEFECT.md`. In particular

    A(u)=u i_v tau,   B(u)=i_x(L(u) wedge omega),
    C(z)=i_x Ctilde(z),       x=(v,w),
    A*B=M(v), B*A=-M(v), A*C=B*C=0.

The displayed equality `M=i_v L` uses the compatible frame
`Omega=tau wedge omega`. A separate change of determinant frame does not
change the fixed tensors tau, omega, L; it must not silently preserve that
scalar equality. Everything constructed below is intrinsic before that
trivialization, and skewness is a determinant-valued statement.

Let `D=D_a` act on W. Write

    j=i_w omega,   H=w(Dj)=2a,   t=i_(wD)omega=-Dj.

Here a is the negative quadratic direction, not a_m. Let r be the LINEAR
polar vector of the fixed quadratic q0, with `v(r)=q0`, and put

    P_D=q0 D-r tensor (wD),       R_D=rho^2(P_D),
    r wedge i_(wD) Ctilde(z)=s_D(z) tau.

The deformation is coefficient action after natural K pullback:

    delta_D(i_x Z)=i_x rho^3(D)Z,

not merely fixed-wedge differentiation `i_(xD)Z`. The previously checked
universal identity gives

    R_D A=0,
    R_D B=-i_x[L wedge r wedge t],
    R_D C=q0 delta_D C-A s_D.                          (1)

Let P denote the four-dimensional Cartan summand in
`U tensor Lambda^2 V`, the kernel of Clifford contraction, and let Pi be
its canonical projector. The corresponding Cartan summand in `U tensor V`
is identified with its symplectic dual using the fixed volume/Clifford
markings. The actual cubic tensor supplies a conformally symplectic isomorphism

    f:Sym^3 W -> P.

Its pullback of the Cartan alternating form is a nonzero fixed scalar times
the standard cubic apolar form. That scalar is NOT set to one. It cancels
when transporting adjoints, while the actual scale of f is retained in
Ctilde and its inverse.

After f, the coefficient Ctilde is the canonical Clebsch inclusion

    i_C:Sym^2 W -> Sym^3 W tensor W,
    i_C(z)=-T z tensor S+S z tensor T.                 (2)

Any nonzero fixed scalar in this statement is incorporated in f, rather than
resetting an actual monad channel. The inverse of i_C below always means the
actual Ctilde, so its scale is retained.

The conjugated positive `sl(U)` action on P lies in the `Sym^6 W` summand
of `sp(Sym^3 W)=Sym^6 W+Sym^2 W`: its negative-sl2 component is zero because
that summand has finite-group type A, whereas the positive copy has type V.
This is the only representation-theoretic property of f used in the residual
calculation. No value of a coefficient of f is used.

## 2. A global symplectic polynomial lift of ANY Cartan operator

Let S(w) be a homogeneous quadratic polynomial with values in End(P), and
let `R_i=(1/2) partial_(w_i) S`. Its symplectic adjoint on P is denoted dagger.
For a constant endomorphism R of P, define E_R on `U tensor Lambda^2 H`:

* on the Cartan part of `U Lambda^2 V`, it is R;
* on the Cartan part of `U V tensor W`, it is `-R^dagger tensor I_W`;
* it is zero on both complementary U summands and on `U Lambda^2 W`.

Define, for `eta in E=U ker(i_x:Lambda^2 H -> H)`,

    T_S eta = sum_i i_x[e_i wedge E_(R_i) eta].        (3)

This is an O-linear polynomial degree-two operator. Derivatives are taken
ONLY on S's coefficients, never on eta. Its output lies in E because
`i_x^2=0`. Its definition is independent of the chosen W basis.

Here is the full skewness check, including the selfadjoint sector. Define
F_R on `U Lambda^3 H` to be R on the Cartan component of
`U Lambda^2 V tensor W`, `-R^dagger` on the Cartan component of
`U V tensor Lambda^2 W`, and zero on the complementary components. Then

    F_R(e_i wedge eta)=e_i wedge E_R eta,
    F_R^dagger=-E_R,                                  (4)

where the second adjoint is between the coefficient spaces Lambda^3 H and
Lambda^2 H using their determinant-valued wedge pairing. For any constant
three-form F and eta in ker i_x,

    epsilon(i_x F wedge eta)=i_x epsilon(F wedge eta).

Using (4), the coefficient pairing therefore shows that the adjoint of
`i_x F_R(e_i wedge -)` on E is `i_x(e_i wedge F_R^dagger -)`, its negative.
Equivalently the ordinary skew projection is
`(1/2)i_x[F_R(e_i wedge eta)-e_i wedge F_R^dagger eta]`, which is exactly
(3). This proves `T_S*=-T_S` for arbitrary S, not just S in sp(P).

Moreover, B has zero Cartan projection in every relevant coefficient sector,
so

    T_S B=0,
    T_S A=i_x sum_i [R_i Pi(A) wedge e_i].            (5)

Thus its V^2 component on A is `S Pi(A)` by Euler's identity. The two
Cartan blocks differ by adjoint; replacing both by S would be incorrect in
the symmetric sector.

## 3. The two negative-binary operators and their exact identities

Use binary symbols S,T for W and covector coordinates u,w. Put

    l=-w S+u T,
    D=(h S+ell T) partial_S+(k S-h T) partial_T,
    H=k u^2-2h u w-ell w^2,
    N=-2l(u partial_S+w partial_T).

Thus D(l)=Dj and N is the Hamiltonian of l^2 in these conventions.
Coordinate-free, N is the induced action of the trace-free endomorphism
`-2j tensor w` on the symmetric powers of W. On Sym^3 W define

    S_minus=[D,N],    S_plus=DN+ND,
    S_comb=2S_minus+S_plus=3DN-ND.                    (6)

S_minus is apolar-skew, whereas S_plus is apolar-selfadjoint. Both preserve
`l Sym^2 W`. Define their source actions by

    P_minus z=S_minus z+2H z,
    P_plus z=S_plus(l z)/l,
    P_comb=2P_minus+P_plus.                           (7)

The quotient in P_plus is exact polynomial division. In particular it is
regular even where l=0. On `Sym^3 W/l Sym^2 W`, both cubic operators act
by the scalar `-6H`. The following full polynomial cubic identity holds:

    (3/2)(Dl)z+(1/24)[S partial_u S_comb(z)
                          +T partial_w S_comb(z)]=0, (8)

for every cubic z; partials act on operator coefficients only.

For completeness the second identity, controlling the remaining Cartan
component, is stated with every sign. Let J be ANY endomorphism in the
Sym^6 W summand of sp(Sym^3 W). For quadratic z put

    p=-l z,  m_u=-T, m_w=S,  Z_K=J((Dl)z).

For i=u,w define

    Y_minus,i = S_minus J(m_i z)-J(m_i P_minus z)
                 +(1/2)[J,partial_i S_minus]p,
    Y_plus,i  = -S_plus J(m_i z)-J(m_i P_plus z)
                 +(1/2){J,partial_i S_plus}p.         (9)

Then `u Y_*,u+w Y_*,w=0`, so there are unique polynomial cubics Z_minus,
Z_plus satisfying `(Y_*,u,Y_*,w)=(w Z_*,-u Z_*)`. One has identically

    36 Z_K+2 Z_minus+Z_plus=0.                       (10)

The verifier represents J by the third transvectant with a completely
symbolic sextic, retaining all seven coefficients, and verifies (8)-(10)
with all cubic/quadratic, Hamiltonian and base coordinates free. These are
complete equivariant representation identities, not tests on selected
source tensors.

## 4. The explicit middle and diagonal source operators

Define the tangent endomorphism of H and its middle action by

    E_0=H pr_V-Dj tensor v,
    K=rho^2(E_0)-(3H/2) I_E.                         (11)

One has `x E_0=0`, `tr E_0=3H`, and hence `K*=-K`. Direct exterior algebra
also gives

    K A=a A,  K B=-a B,
    K C-a C=i_x[(i_v C_(wD)) wedge omega],            (12)

where `C_(wD)=i_(wD) Ctilde`.

Take S_comb on P via f. Set

    C_mult=-chi/g_L,
    M_a=(chi/g_L) R_D,
    M_b=-(3/2)K-(1/24)T_(S_comb),
    P_a=Q_a=0,
    Q_b=-(a/2) I_U,
    P_b=-(3a/2) I_A-(1/24)P_comb,
    R=-(chi/g_L)s_D.                               (13)

The source reverse block S_source is specified next. All displayed maps
are polynomial with the required degrees and equivariance. Equations
(2a), (2c), (2d) of the five-equation note follow immediately from
(1), (5), and (12). We prove (2b) and (2e) rather than omitting them.

## 5. The FULL reverse block and regularity

Put `c=C_mult g_L/(2chi)=-1/2`. The universal Clifford/volume identity is

    L wedge r=(g_L/(2chi))[A-(3/2)Pi(A)].             (14)

It is a tensor identity, with A viewed as the coefficient two-form. It is
checked in the universal sl2 realization and is equivalently a Fierz
identity with the stated full-trace volume normalization.

The entire left-hand side of (2b), before subtracting C S_source, is

    C_mult i_x[L wedge r wedge t]+2c a A
                         +T_((c/12)S_comb) A.

Inside i_x, subtract the identically contracting-zero Koszul boundary
`i_x(c tau wedge t)`. The remainder is the Cartan coefficient tensor

    Phi(z)=(3c/2) z tensor Dj
                +(c/24) sum_i partial_i S_comb(z) tensor e_i,
    z=f^(-1) Pi(A).                                  (15)

By (8), Phi lies in `ker(Sym^3 W tensor W -> Sym^4 W)`, exactly the image
of the Clebsch map (2). Define S_source uniquely by

    Ctilde S_source=f(Phi(f^(-1)Pi(A))).              (16)

This is a polynomial source map of degree one in v and one in w. Indeed,
if `Phi=F_S tensor S+F_T tensor T`, then `S F_S+T F_T=0` implies
`F_S=-T z_2, F_T=S z_2` with polynomial z_2. This uses exact divisibility
in the binary polynomial ring, not division at a selected point. Formula
(16) proves the COMPLETE equation

    M_a B+M_b A=A Q_b+C S_source.                    (17)

## 6. The last arrow residual, including its complementary component

Let

    E_C=M_b C-C P_b-B R.

Its V^2 component vanishes because S_comb preserves `l Sym^2 W` with source
action P_comb. Let P' be the Cartan summand of U V, let Pi' be its projector,
and let `h:P'->P` be the fixed dual identification used in Section 2. Define
one and the SAME operator in every residual term by

    J_v=f^(-1) h Pi' i_v f : Sym^3 W -> Sym^3 W.      (18a)

No scalar or sign is chosen separately for any occurrence of J_v. The map
`v->h Pi' i_v` is positive-SL2-equivariant and alternating-adjoint on P.
The positive adjoint representation occurs once in End(Sym^3 U), so this
map lies in the positive sl2 action (its possible overall coefficient is
already fixed by (18a)). More explicitly, in the universal Clifford
realization of Section 7, with `h=G^(-1)` on the V factor and
`G=[[0,1/2,0],[1/2,0,0],[0,0,1]]`, one has the exact identity

    h Pi' i_v|P = -(2/3) rho^3(M(v)).                 (18c)

The verifier checks (18c) with all v coordinates free. This is a universal
representation identity, not a chosen actual-source value. After
f-transport the map therefore belongs to the negative Sym^6 W summand
by Section 1. The sextic identity (10) applies
to this exact J_v, with its coefficient untouched.

Here is a direct common-normalization computation. Write
`Ctilde(z)=sum_i f(m_i z) wedge e_i`; its V^2 component after i_x is
`f(p)`, where p=-l z. Its projected V W coefficient is EXACTLY
`J_v(m_i z)`, with no proportionality symbol. On this same component,
formula (3) gives for ANY S

    (T_S C-C P_S)_i = -S^dagger J_v(m_i z)-J_v(m_i P_S z)
                     +(1/2)[J_v(partial_i S)p
                              +(partial_i S)^dagger J_v p].  (18b)

For S_minus and S_plus this is precisely (9). For the base lift, (12) has
coefficient `i_v C_(wD)`; its exact projection under h and f is
`J_v((Dl)z)=Z_K`, using `sum_i(wD)_i m_i=Dl`. Thus every term has the same
sign and normalization specified in (18a). Finally B R has zero Cartan
projection. The resulting b-type Cartan coefficient is EXACTLY

    -(3/2)Z_K-(1/12)Z_minus-(1/24)Z_plus=0           (18)

by (10).

It remains to prove regular b-type and kill its spin-U component, not to
infer its vanishing merely from (18). Write a polynomial element of E
with zero V^2 component as

    eta=Y_u wedge e_u+Y_w wedge e_w+d omega,

where Y_i is U V-valued. The V component of `i_x eta=0` says
`uY_u+wY_w=0`. Since u,w are coprime polynomial variables, there is a
POLYNOMIAL U V-valued Z such that `(Y_u,Y_w)=(wZ,-uZ)`. The remaining
contraction equation fixes `d=i_v Z`. Thus

    eta=i_x(Z wedge omega).

If eta also has zero Cartan component, then Z lies in the fixed spin-U
complement, which is exactly the image L(U). Its inverse is a constant
Clifford contraction, so `eta=B t_0` with a POLYNOMIAL source map t_0.
Apply this to E_C, obtaining `E_C=B t_0` globally, not merely after
localizing or dividing by a coordinate.

Now use (17), skew-adjointness of M_a,M_b, and A*C=C*C=0:

    A* E_C=-B* M_a C-M R.

Equation (2d), already checked, reads
`M_a C=A R-C_mult q0 delta_D C`. Since `B*A=-M` and
`B* delta_D C=0` (D preserves the Cartan coefficient condition), it follows
that

    A* E_C=0,   hence M(v)t_0=0.

The Clifford square gives `chi q0 t_0=0`. Over the polynomial domain this
forces `t_0=0`; no nonzero-leg argument or source specialization is used.
Therefore E_C=0 and (2e) holds in full.

Both middle operators are skew for the fixed determinant pairing. Taking
the prescribed determinant-dual source operator on the right therefore
supplies the SECOND monad arrow equation. Multiplying by the formal channel
coefficients exactly as in the five-equation ansatz gives the desired
chain homotopy. Finally, the already-proved actual cyclic/multiplier theorem
(`ACTUAL-AMBIENT-ATIYAH-MULTIPLIER-IS-THE-MONAD-RATIO.md`, Section 6)
asserts uniqueness of this scalar, equivalently the relevant channel
`q0 At_F(D_a)` is nonzero. Thus the exhibited homotopy identifies the actual
C_mult as (0), rather than merely producing an additional possible relation.

## 7. Normalization and verifier scope

The reproducible Clifford check uses the universal sl2 basis
`E,F,H` with `M(v)=xE+yF+zH`, `M(v)^2=(xy+z^2)I`, and
`tau=e_0 wedge e_1 wedge e_2`, giving full-trace `g_L=2`. The physical
comparison is retained as `q0=(xy+z^2)/theta` with theta arbitrary, so
`chi=theta` is not set to one. This is a universal representation identity,
not an actual source instance. Restoring the fixed volume marking yields
(14); equivalently under `L->sL`, `tau->t tau`, `chi/g_L->(t/s)chi/g_L`,
exactly the required a-channel/b-channel weight. Under a rescaling of the
physical q0 it has the inverse physical-equation weight.

The resulting numerical coefficient is the invariant `-1` in
`C_mult g_L/chi=-1`, not a convention setting C_mult to one. An independent
change of determinant frame leaves the constructed operator and (0),
interpreted through its fixed tensor markings, unchanged.

Run `python verify_universal_cartan_koszul_multiplier.py`. It verifies the
full polynomial identities, the arbitrary-End(P) coefficient-space
adjoint identity, the Clifford projector identity, and all formal channel
coefficient equations. It does not construct an actual monad matrix,
evaluate an actual cubic coefficient, compute a rank, specialize a source
parameter, or scan source instances.
