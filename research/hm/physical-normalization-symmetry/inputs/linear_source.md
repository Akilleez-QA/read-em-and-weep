# An explicit canonical square-zero first-normal lift of aN

## Result and conventions

Let B=End_0(F), q=q0, Q=(q=0), and 2Q=(q^2=0), for the actual marked HM
bundle and the fixed physical equation. Let N be the fixed invariant nilpotent,
xi=delta_q(N), and zeta_a=k At_F(D_a), with a xi=q zeta_a. Retain the fixed
Hamiltonian, determinant, channel and boundary conventions of the frozen
Cartan--Koszul multiplier theorem. Put r=a_m/b_m and

    kappa=-(chi/g_L)r,     r_xi=k/kappa,
    xi=r_xi At_F(D0).

There is an EXPLICIT global degree-zero monad cochain U_a of twist four such that

    d U_a=q^2 zeta_a^coch,
    U_a|Q=aN,
    (U_a mod q^2)^2=0                                 (1)

on the actual rank-two bundle F|2Q. Its induced section in H0(B_(2Q)(4)) is the
UNIQUE equivariant linear physical-positive family lifting a -> aN.

This is a lift of the MULTIPLIED nilpotent aN on the actual endpoint. It is not a
lift of N itself, a spinor lift, an extension to 3Q, or the further division
q v_h=a h zeta_a. The square-zero assertion follows from a separate exact trace
calculation below; it is not inferred merely from nilpotence on Q.

## 1. The two global primitives and the determinant source gauge

Use the monad with source N_src=A+U, middle E=U tensor Omega^2(2), and right
term N_src^* tensor Delta. Here U=Wprime, and A is the negative quadratic
three-space. Use the differential convention

    (d T)_left=T_middle alpha-alpha T_source,
    (d T)_right=T_right beta-beta T_middle.

A fixed-duality degree-zero cochain has T_middle skew and
T_right=-T_source^dagger. The natural trace-free block Euler field is
D0=diag(-2/5 I_V,3/5 I_W). Its derivative e0_nat has left channel coefficients
(-6a_m/5,4b_m/5,-c_m/5). Define the constant degree-zero gauge

    G_source=diag(-1/5 I_A,-6/5 I_U),
    G_middle=0,     G_right=-G_source^dagger.

Then EXACTLY, on both arrows,

    e0_red=e0_nat+dG,
    (e0_red)_left=(0,2b_m B,0).                       (2)

Let P_red be the complete Clifford annihilator from the frozen Clifford note:

    (P_red)_middle=-(2/(r chi)) B M B^*,
    (P_red)_source=(P_red)_right=0,
    d P_red=q e0_red.                                (3)

Let T_red(a) be the complete Cartan--Koszul homotopy AFTER dividing the
five-channel b_m-cleared expression by b_m. In particular

    (T_red)_middle=r M_a+M_b,
    (T_red)_source,AA=P_b,
    (T_red)_source,UU=Q_b,
    (T_red)_source,UA=(c_m/b_m) R,
    (T_red)_source,AU=(a_m/c_m) S,
    (T_red)_right=-(T_red)_source^dagger,
    d T_red=a e0_red-q kappa e_a,                     (4)

where e_a is the NATURAL Hamiltonian deformation cochain, including the K
pullback action. Its class is At_F(D_a). All five coefficient tensors in (4)
are the fixed explicit tensors in the frozen complete proof; no new channel
choice or unknown source scalar is introduced here.

The natural, rather than source-reduced, primitives are

    P_nat=P_red-qG,       T_nat=T_red-aG.              (5)

They both have twist two and satisfy dP_nat=q e0_nat and
dT_nat=a e0_nat-q kappa e_a. Thus the first-division homotopy for the fixed
classes is r_xi T_nat, since

    d(r_xi T_nat)=a(r_xi e0_nat)-q(k e_a).             (6)

The right arrows and determinant line are retained throughout (2)-(6).

## 2. Exact identification with the fixed N and the boundary sign

The global chain map P_nat mod q induces an invariant physical-positive section
of B_Q(2). Every tensor in (3),(5) is equivariant, and the constant source gauge
commutes with the group and inversion. The pinned square sequence gives
H0(B_Q(2))_+=C N and delta_q(N)=xi!=0. Stability gives H0(B)=0. The restriction
LES therefore gives H0(B(2))_+^G=0 and makes the invariant boundary injective.

For completeness, the convention delta_q[P_nat|Q]=[e0_nat] agrees with the
actual target-minus-transport Cech boundary, rather than silently changing its
sign. Locally choose S_i with e0_nat=dS_i. Such choices exist since the monad
locally resolves a vector bundle. Then P_nat-qS_i is closed and supplies a local
ambient lift of P_nat|Q. Its target-minus-transport difference divided by q is
- delta_Cech S. The natural deformation cochain e0_nat represents that same
- delta_Cech S: I+epsilon S_i identifies the reference monad with its naturally
deformed local monad, and the coordinate transition derivative is the negative
Cech difference of these local identifications. Thus the connecting sign is
exactly the one fixed in the actual boundary/Atiyah theorem.

It follows by the invariant injection, with no freely selected scale, that

    r_xi P_nat|Q=N.                                   (7)

The displayed cochains r_xi e0_nat and k e_a are explicit representatives of the
fixed ACTUAL classes xi and zeta_a. This does not assert that every previously
chosen Cech representative is literally identical to these representatives.

## 3. The global first-normal lift and its uniqueness

Define

    U_a=r_xi(aP_nat-qT_nat)
       =r_xi(aP_red-qT_red).                          (8)

The common Euler source gauge cancels exactly. Equations (3)-(6) give

    d U_a=r_xi q^2 kappa e_a=q^2(k e_a).

Hence U_a mod q^2 is a genuine global chain map on the RESTRICTED ACTUAL monad,
not a hypothetical spinor monad on 2Q. Since F is locally free, restriction
preserves the exactness of its locally free monad at both ends. Fixed duality
makes the induced rank-two endomorphism trace-free. Equation (7) gives its
restriction aN, and its boundary for the equation q^2 is exactly zeta_a.
Equivalently S(a)=(aP_nat-qT_nat)/kappa satisfies dS=q^2 e_a and U_a=kS(a).

For uniqueness use

    0 -> B_Q(2) --q--> B_(2Q)(4) -> B_Q(4) -> 0.

Two equivariant linear physical-positive families lifting a -> aN differ by an
element of Hom_G(A,H0(B_Q(2))_+)=Hom_G(A,C N)=0. Therefore the SECTION family in
(8) is canonical, even if other equivariant primitive choices are used.

There are two distinct statements here. The common gauge in (5) cancels
LITERALLY as a cochain. Arbitrary separate closed changes Z_P,Z_T change (8) by
r_xi(aZ_P-qZ_T); they need not cancel literally. If those changes still define
equivariant linear physical-positive families with the same restriction, their
induced SECTION changes vanish by the preceding exact sequence.

## 4. The extra square-zero calculation

Write P=(P_red)_middle and T=(T_red)_middle. Use the algebraic Clifford tensor
in the compatible determinant frame, so M^2=chi q I_U. The exact channel
identities and the COMPLETE homotopy give

    B^* B=0,
    B^* M_a B=-aM,
    M_b B=(3/2)aB.

The compression B^*M_aB=-aM also follows by applying B^* to the full
second channel equation, using Q_b=-a/2, M_bB=3aB/2 and B^*C=0. Thus it does
not depend on an independently guessed compression factor. Consequently

    P^2=0,
    B^* T B=-r aM,
    tr_E(PT)=-(2/(r chi)) tr_U(M B^* T B)
            =(2a/chi) tr_U(M^2)=4a q.                (9)

The last trace is the full trace of the TWO-dimensional U. Equation (9)
retains chi; it does not set the physical Clifford quadratic equal to q.
All contractions are intrinsically determinant-valued, with the Delta factors
canceling exactly as in the frozen Clifford primitive.

The source and right components of U_a are both divisible by q. Therefore their
squares have traces divisible by q^2. On the middle component, cyclic trace and
(9) give

    tr_E((U_a)_middle^2)
       =r_xi^2[-2a q tr_E(PT)+q^2 tr_E(T^2)]
       =r_xi^2 q^2[tr_E(T^2)-8a^2].                 (10)

More precisely, retaining BOTH endpoint terms gives the exact global identity

    Str(U_a^2)=r_xi^2 q^2[Str(T_red^2)-8a^2],
    Str(T_red^2)=tr_E(T^2)-2tr((T_red)_source^2).

Thus the alternating monad trace of U_a^2 is zero modulo q^2. Because the
restricted monad is locally split at its ends, its alternating trace equals
the trace of the induced rank-two cohomology endomorphism. This trace identity
holds over O_(2Q), not merely over its reduced quotient. Fixed duality also
gives tr(U_a)=0. Rank-two Cayley--Hamilton, valid over this nonreduced ring in
characteristic zero, now yields

    U_a^2=(1/2)tr(U_a^2) I=0 on F|2Q.                (11)

This proves the last assertion in (1) by a full trace certificate. It does not
assert that any raw monad component squares literally to zero, supply a
global chain null-homotopy of that square, or imply that a chosen spinor line
extends. By polarization the induced family also satisfies
U_a U_b+U_b U_a=0 on 2Q for every pair of negative quadratic directions.

## 5. Physical equation covariance and scope

If q is replaced by nu q with N fixed, then chi -> chi/nu, kappa -> kappa/nu,
k -> k/nu^2 and r_xi -> r_xi/nu. The explicit primitives obey
P_nat -> nu P_nat and T_nat -> T_nat. Hence U_a itself is unchanged, whereas
its divided q^2 boundary changes by nu^-2, exactly like zeta_a. This is a
physical equation check, not a choice to suppress the normal-equation factor.

The original next division q v_h=a h zeta_a requires a further cochain or
cohomological comparison. Neither (6) nor the actual nilpotent lift (8)
performs that division. No fourth Bockstein value is inferred here.

## Sources and verification

The full polynomial homotopy is
UNIVERSAL-CARTAN-KOSZUL-MULTIPLIER-HOMOTOPY.md; its complete independent audit is
UNIVERSAL-CARTAN-KOSZUL-HOMOTOPY-INDEPENDENT-AUDIT.md. The annihilator and
Delta-factor cancellation are in
UNIVERSAL-MONAD-CLIFFORD-HOMOTOPY-AND-HAMILTONIAN-DEFECT.md. The fixed boundary
normalization and Cech sign are in
ACTUAL-BLOCK-EULER-ATIYAH-CLASS-AND-ENDPOINT-SCALE.md. The positive cone section
line and fixed equivariant probe are in
POSITIVE-FIRST-BOCKSTEIN-VANISHES-BY-CYCLIC-RAO.md.

Run python verify_actual_multiplied_nilpotent_square_zero_lift.py. It checks
the full source-gauge signs, natural/reduced homotopy algebra, literal common
gauge cancellation, every scalar and twist in the trace certificate, the
universal rank-two Cayley--Hamilton identity, and physical equation covariance.
No actual source values, actual-instance matrices, ranks or scans are used.
