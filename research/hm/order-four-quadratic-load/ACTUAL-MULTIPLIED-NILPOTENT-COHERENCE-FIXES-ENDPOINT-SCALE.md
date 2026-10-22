# Canonical multiplied-nilpotent coherence fixes the actual endpoint scale

## Result in the fixed markings

Use the actual square-zero first-normal section family U_a from
ACTUAL-MULTIPLIED-NILPOTENT-HAS-A-CANONICAL-SQUARE-ZERO-LIFT.md. Thus
U_a is a section of B_(2Q)(4), U_a|Q=aN, and its q0^2-boundary is the fixed
probe zeta_a=k At_F(D_a). Put q=q0, r=a_m/b_m, r_xi=k/kappa, and retain

    kappa=-(chi/g_L)r,
    xi=delta_q(N)=r_xi At_F(D0).

For negative quadratics a,b define the UNNORMALIZED first transvectant

    {a,b}=a_s b_t-a_t b_s.

The actual induced sheaf morphisms satisfy

    aU_b-bU_a=-(kappa/2)q {a,b}N,                    (1)
    U_a U_b=U_b U_a=0 on 2Q.                        (2)

The expression q{a,b}N in (1) is the canonical square-zero-ideal image of the
section {a,b}N on Q. It does not presuppose a lift of N.

Let eta_+=c_+ eta_ap be the POSITIVE logarithmic displacement from the midpoint
to the chosen actual endpoint, with the apolar generator and physical boundary
conventions of the frozen actual Euler theorem. Then

    c_+=kappa=-(chi/g_L)r.                           (3)

The bracket-normalized displacement is its negative. With the retained vertex,
edge and normal-root markings, (3) gives the further exact identities

    C_ap/K_cup=-2chi/g_L,
    k=-theta kappa^2/(2rho_C)
     =-theta chi^2/(2C_res g_L^2).                   (4)

No channel, equation, residue or cubic normalization is set to one. These are
universal marked identities, not actual-source coefficient evaluations. They
do not compute a fourth Bockstein value.

## 1. The actual alternating coherence coefficient

Let P=P_nat and T_a=T_nat(a) be the full fixed-duality degree-two monad
cochains, with

    dP=q e0,
    dT_a=a e0-q kappa e_a,
    U_a=r_xi(aP-qT_a).

The natural deformation classes of e0,e_a are At_F(D0), At_F(D_a). The constant
Euler source gauge cancels exactly in

    L_ab=aT_b-bT_a,
    dL_ab=-q kappa(a e_b-b e_a).                     (5)

Thus L_ab mod q is a positive section of B_Q(4).

In row coordinates (s,t), the fixed Hamiltonian is
D_a=(-a_t,a_s). Binary Euler's identity, with both a,b quadratic, gives

    aD_b-bD_a=-{a,b} E_W/2.                         (6)

The projective negative-block Euler field E_W equals D0, because their ambient
representatives differ by (2/5)Euler_total. Multiplication by {a,b} does not
change the fact that this difference is vertical in the twisted Euler sequence.
The TRACE-FREE Atiyah extension is O-linear, so (6) gives the ACTUAL equality
of twisted cohomology classes

    a At_F(D_b)-b At_F(D_a)=-{a,b} At_F(D0)/2.         (7)

Equation (7) is not asserted as a literal equality of the chosen global monad
cochains; their natural K pullback and source gauges are still retained.

Apply the q-boundary to (5), using the sign convention already checked in the
first-normal lift theorem. Equations (5),(7) imply

    delta_q(L_ab|Q)=(kappa/(2r_xi)){a,b}xi.

The pinned ambient vanishing H0(B(4))=0 makes
H0(B_Q(4)) -> H1(B(2)) injective. Since delta_q(pN)=p xi for every quadratic p,
there is no uncomputed intertwiner scalar:

    L_ab|Q=(kappa/(2r_xi)){a,b}N.                    (8)

Now aU_b-bU_a=-r_xi q L_ab, which proves (1). In particular, whenever {a,b}
is nonzero, (1) is nonzero: Q is integral, N is nonzero, and multiplication
into the square-zero ideal is injective. This already prevents U_a from being
obtained as a times one globally framed lift of N.

## 2. Pairwise products really vanish

The exact cochain commutator modulo q^2 is

    [U_a,U_b]=-r_xi^2 q[P,L_ab] mod q^2.             (9)

Both P and L_ab become chain maps on Q. Their induced maps are N/r_xi and
the polynomial multiple of N in (8), so their induced commutator is zero.
Multiplication by q in (9) factors through that induced map on Q. Therefore
[U_a,U_b]=0 as an ACTUAL sheaf morphism on 2Q. No global chain null-homotopy
of [P,L_ab] is assumed.

The independently proved square-zero identity for every U_a, together with
linearity, gives U_aU_b+U_bU_a=0 by polarization. Combined with (9) in
characteristic zero this proves (2). It does not say that the raw components
of these monad products vanish.

## 3. The exact deformed negative projection

All coordinates in this section are arbitrary abstract binary frames, not
selected actual HM points or source values. On the chart s!=0 put z=t/s and
q_s=q/s^2. Equation (1) for (s^2,st) and (s^2,t^2) yields

    U_st=(z-kappa q_s)U_(s^2),
    U_(t^2)=(z-kappa q_s)^2 U_(s^2) mod q^2.         (10)

Here q U_(s^2)=q s^2 N, because U_(s^2)|Q=s^2N. Thus for every negative
quadratic a=s^2 A(z),

    U_a=A(z-kappa q_s) U_(s^2).                     (11)

This is a factorization of the actual SECTION family, including at points
where its generator vanishes. It does not assert that the image or kernel is
a globally flat line bundle.

In the opposite VOLUME-COMPATIBLE chart w=-s/t and q_t=q/t^2, the deformed
coordinate is w'=w-kappa q_t. On the overlap the equality

    w'=-1/(z-kappa q_s) mod q^2

is exact. With the unoriented coordinate s/t instead, the correction has a
PLUS sign. This distinction retains the fixed Hamiltonian volume convention.

## 4. The local boundary is the actual Euler class

On the two negative charts define actual local first-normal lifts of N by

    N_s=U_(s^2)/s^2,       N_t=U_(t^2)/t^2.

These are sections of B_(2Q)(2), not global framings of N. From {s^2,t^2}=4st
and (1),

    N_t-N_s=-2kappa q N/(st) mod q^2.                (12)

The target-minus-transport Cech boundary therefore gives, on
U=Q minus C with C=(s=t=0),

    xi_Q|U=-2kappa[N/(st)].                         (13)

The physical line here is essential. N has twist TWO, so N/(st) has twist
ZERO. In the s-trivialization its coefficient is n_s/z, where n_s=N/s^2.
If N=theta n in the fixed Serre marking, this is exactly theta n/z in the
local notation of the apolar Euler theorem. In the opposite physical t^2
frame, with w=-s/t, the same cocycle is -n_t/w after adjoint transport,
where n_t=N/t^2. This is the O(-2) Euler transition, not a new boundary
sign. There is no omitted determinant or equation-line factor.

The frozen ACTUAL-BLOCK-EULER-ATIYAH-CLASS-AND-ENDPOINT-SCALE.md, Section 2,
gives the FULL actual invariant bracket comparison

    [eta_ap,N]|U=2[N/(st)].                         (14)

Its proof uses the corrected apolar section Euler coefficient ONE and the
actual conic marking. In particular (14) is not inferred just from the raw
lowest diagonal coefficient FOUR or from two nonzero legs. The full
completion is part of that cited theorem.

## 5. Why restriction to U cannot erase this bracket

It would be insufficient to assume that a nonzero global bracket stays
nonzero on the vertex open. Here this is proved by a regular-sequence argument.
The homogeneous ring of Q has the form

    (C[V]/(q0))[s,t].

Thus s and t are a regular sequence along C: multiplication by s is injective
as a polynomial-variable shift, and multiplication by t remains injective
after quotienting by s. Equivalently, C is the codimension-two complete
intersection of the two negative coordinate hyperplanes in Q. This remains
true without any selected coefficient or smoothness test for q0.

Since B_Q is locally free, its local cohomology sheaves supported on C vanish
in degrees below two. The local-to-global support spectral sequence gives
H_C^1(Q,B_Q)=0. The localization exact sequence therefore supplies an injection

    H1(Q,B_Q) -> H1(U,B_Q).                          (15)

The actual invariant bracket [eta_ap,N] is nonzero by the pinned midpoint and
apolar comparison theorem. By (15), its restriction in (14) is nonzero as
well. Hence (13),(14) are legitimate scalar comparisons on this open set,
not an unjustified promotion from lowest coefficient to a global class.

## 6. The actual positive endpoint scalar and normalization consequences

The fixed actual boundary convention gives

    xi_Q=-[eta_+,N]=-c_+[eta_ap,N].                  (16)

Compare (13)-(16) on U. Because (14) is nonzero there, c_+=kappa. This proves
(3), including the positive-endpoint sign. The bracket-normalized tangent is
eta_b=-eta_+ and therefore has coefficient -kappa.

The previously proved marked relations are

    c_+=C_ap r/(2K_cup),
    rho_C=C_res r^2,
    c_+/k=-2rho_C/(theta kappa).

Substituting c_+=kappa=-(chi/g_L)r gives (4). Thus the normal-cup and ambient
multiplication normalizations are now related by a COMPLETE actual cochain
and boundary comparison, rather than equated because both are nonzero.

Under q0 -> nu q0, chi,kappa,c_+ are divided by nu, C_ap is multiplied by nu,
K_cup by nu^2, and k by nu^-2; every displayed scalar identity has the required
weight. Under sigma -> l sigma with N fixed, theta and rho_C are both divided
by l^2, so the k formula is unchanged. At the marked exchange mu^2=-1,
kappa and c_+ change sign while the fixed-boundary k is unchanged.

## Scope and verification

This note uses the actual endpoint monad and its canonical multiplied lift,
not a midpoint substitute for the full lower class. It does not construct the
next cochains dividing a h zeta_a by q, extend the midpoint to 3Q, supply a
flat spinor kernel, or evaluate a fourth Bockstein.

Run python verify_actual_multiplied_nilpotent_endpoint_coherence.py. The
verifier checks all six free quadratic coefficients, the projective Euler
correction, scalar and twist identities, opposite-chart signs, local boundary
factor two, and the endpoint/normal-root normalizations. The regular-sequence
and locally free restriction arguments are geometric proofs above, not
actual-instance rank computations. All prior frozen artifacts are unchanged.
