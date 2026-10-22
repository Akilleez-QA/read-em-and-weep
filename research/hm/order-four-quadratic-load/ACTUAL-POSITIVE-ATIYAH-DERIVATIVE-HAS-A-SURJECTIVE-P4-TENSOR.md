# The positive Atiyah derivative has an exact, nonzero off-diagonal P4 tensor

## Checked result and next-division scope

Let H be an arbitrary positive q0-selfadjoint trace-free endomorphism of V,
and put h=(1/2)D_H q0. Thus H ranges over the actual D5 of positive trace-free
quadratics. All five coefficients of H remain free.

The full natural positive derivative of the actual c-channel has an exact
spin/Cartan off-diagonal coefficient

    B^* delta_H C = -c Hhat p_C(w).                    (1)

Here c is the Clifford contraction, Hhat=rho^2(H) on Lambda^2 V, and
p_C(w)=i_w Ctilde lies in the actual Cartan four-space P. Formula (1) is in
the compatible determinant frame of the frozen Clifford theorem. Its right
side retains the actual scale of Ctilde, not merely its isomorphism class.

As an equivariant tensor, (1) is a NONZERO map

    D5 tensor A -> U tensor W = P4,

and consequently is onto P4. This is a statement about the actual coefficient
tensor, NOT about its image in a cohomology quotient. It isolates a part which
would be lost by keeping only the Cartan compression.

That compression has a useful additional exact identity. If f identifies the
actual P with Sym^3 W, set C_H=f^(-1) Pi Hhat f. Then

    C_H^dagger=C_H,    tr(C_H)=0,
    C_H^2=(tr_V(H^2)/6) I4,
    C_H C_K+C_K C_H=(tr_V(HK)/3) I4.                 (2)

Thus the five-space is a Clifford subspace of End(Sym^3 W). Its full
spin/Cartan off-diagonal blocks are nevertheless essential. Equations (1)-(2)
do NOT yet supply a cochain C_h or a closed V_h with

    d C_h=a h Z_a-q0 V_h.                            (3)

Section 4 gives a concrete global partial primitive and the exact remaining
polynomial equation, rather than claiming that the compressed identity solves
(3).

## 1. All moving tensors and the derivative sign

Use q=q0, r=a_m/b_m, the fixed algebraic Clifford tensor M(v)=i_v L, and
M(v)^2=chi q(v) I. Choose the physical polar vector R_q(v) with
v(R_q)=q. Positive q-selfadjointness gives

    R_h=H R_q,   v(R_h)=h,
    {M(v),M(vH)}=2chi h(v) I.                        (4)

The actual infinitesimal deformation uses NATURAL K pullback. For an arbitrary
constant coefficient three-form Z,

    delta_H(i_x Z)=i_x rho^3(H)Z,

not merely i_(xH)Z. Since H is trace-free on the positive block, the a-channel
volume is fixed; the only left-arrow derivatives are b_m B_H and c_m C_Harr,
where B_H=delta_H B and C_Harr=delta_H C. The notation C_Harr is distinct from
the compressed endomorphism C_H in (2).

For an endomorphism cochain the natural derivative includes both its moving
coordinate coefficients and its K-frame conjugation. In particular the
Cartan projector is NOT frozen:

    delta_H Pi=[Hhat,Pi].                            (5)

Its two diagonal blocks vanish, but its off-diagonal blocks need not vanish.
The actual conformally symplectic f also moves by Hhat f. Its conformal scalar
cancels in transported adjoints; its actual scale remains in (1).

With the fixed right-commutator differential dT=[T,d_M] and e_H=delta_H d_M,
differentiating dU_a=q^2 Z_a gives

    d(delta_H U_a)-[e_H,U_a]
       =4q h Z_a+q^2 delta_H Z_a.                   (6)

All markings in (6) are transported naturally in the positive SL(V) orbit.
One must not set delta_H Z_a to zero just because the positive and negative
vector fields commute. Nor can (6) be divided by q without treating its full
commutator term.

## 2. The exact spin/Cartan computation

Identify Lambda^2 V with V^* using the fixed positive volume tau. Then
Hhat=-H^t. Let

    c:U tensor Lambda^2 V -> U,
    j:U -> U tensor Lambda^2 V,
    c j=I,   Pi=I-jc,
    P=ker c.

The maps are the fixed universal Clifford/Clebsch maps. To make the constants
in (1)-(2) reproducible, use the COMPLETE abstract Clifford representation
M0=[[0,1],[0,0]], M1=[[0,0],[1,0]], M2=diag(1,-1). This is not an actual HM
coefficient choice. In these representation coordinates the quadratic has
matrix G=[[0,1/2,0],[1/2,0,0],[0,0,1]], while q=(xy+z^2)/chi retains its
physical normalization. Every q-selfadjoint trace-free H has the form

    H=[[A,B,C],[D,A,F],[2F,2C,-2A]],

with all five letters independent. On the same frozen Cartan basis used in
the full homotopy, its complete compressed tensor is

    [[-A, 2F, -D, 0],
     [2C/3, A, 0, -D/3],
     [-B/3, 0, A, -2F/3],
     [0, -B, -2C, -A]].

Direct universal multiplication gives its square as
(A^2+BD/3+4CF/3)I4, which is exactly tr(H^2)I4/6. It is selfadjoint for the
Cartan apolar form. Polarization proves the second identity in (2). Since the
actual f is conformally symplectic, transport to the negative binary cubic
preserves these identities and identifies the compression with the full
selfadjoint trace-free Sym^4 W summand.

The spin diagonal block is zero, c Hhat j=0. In contrast, the COMPLETE
spin-from-Cartan block in the same universal basis is

    c Hhat|P = [[-C,-3A,-3F,-D],[-B,3C,-3A,F]].       (7)

Every H coefficient occurs here. Thus (7) vanishes only when H=0. This is a
universal intertwiner identity, not an actual-instance rank computation.

For arbitrary Cartan coefficient tensors Ctilde_i in P, write
Ctilde=sum_i Ctilde_i wedge e_i and p_C(w)=sum_i w_i Ctilde_i. Full exterior
pairing of B with i_x rho^3(H)Ctilde gives precisely (1), including its minus
sign. The verifier checks all eight Cartan-W coefficient symbols and all five
H symbols, and checks the WHOLE determinant-valued four-form identity rather
than just one chosen component.

The actual Ctilde factors through the surjective Cartan map
A tensor W -> Sym^3 W and the actual isomorphism f:Sym^3 W -> P. For H!=0,
(7) is nonzero, so precomposition by this SURJECTION and this ISOMORPHISM
cannot annihilate it. This proves the injectivity of the coefficient map
H -> B^*delta_H C and the asserted nonzero P4 tensor. Irreducibility of
U tensor W=P4 then proves surjectivity. This argument explicitly supplies the
surjective and invertible legs needed for the conclusion; it is not an
inference from two merely nonzero maps.

If Omega alone is rescaled relative to tau wedge omega, the pairing-defined
B^* acquires the corresponding inverse factor. The right side of (1) must
then use the same pairing-framed contraction, not the unchanged algebraic c.
The algebraic projector and compression in (2) do not thereby change.

## 3. The literal sparse commutator with the annihilator

Use the source-reduced annihilator P_red, with middle component

    P_middle=-(2/(r chi)) B M B^*,
    P_source=P_right=0.

Two b-type tensors pair to zero, even after varying L, so B^*B_H=0.
Differentiated isotropy gives B^*C_Harr=-B_H^*C. The left arrow of the full
commutator therefore has only its A-column:

    [e_H,P_red]_left|U=0,
    [e_H,P_red]_left|A
      =(2c_m/(r chi)) B M(B^*C_Harr)
      =-(2c_m/(r chi)) B M c Hhat p_C(w).             (8)

The right arrow is its fixed-duality partner. The physical chi and every
channel coefficient are retained. The moving-projector term in (7) is
exactly the coefficient which enters (8). A compression-only replacement
would erase it and cannot be asserted to recover the full lower class.

## 4. A concrete partial primitive for the next division

Fix the negative Hamiltonian D_a and t_a=i_(wD_a)omega. Define

    P_(a,h)=hD_a-R_h tensor(wD_a),
    R_(a,h)=rho^2(P_(a,h)),
    R_h wedge i_(wD_a)Ctilde=s_(a,h) tau.

Then x P_(a,h)=0 and tr(P_(a,h))=0. Thus R_(a,h) is a GLOBAL polynomial,
determinant-skew degree-two endomorphism of K. The universal exterior identity
holds for every constant three-form Z:

    h i_x rho^3(D_a)Z-R_(a,h)i_x Z
      =i_x[R_h wedge i_(wD_a)Z].                    (9)

Let G_(a,h) be the fixed-duality degree-zero cochain of twist four with

    G_middle=a R_(a,h),
    G_source|A->U=-a(c_m/a_m)s_(a,h),
    all other source blocks zero,
    G_right=-G_source^dagger.

Then E_(a,h)=dG_(a,h)-a h e_a has the EXACT left-arrow residual

    E|U=-a b_m i_x[L wedge R_h wedge t_a],
    E|A=(a b_m c_m/a_m) B s_(a,h).                  (10)

These are the only residual columns; the two-arrow determinant convention is
the same one as the complete first homotopy. All tensors in (10) are regular
polynomials. Since e_a is closed, E_(a,h) is closed.

The unsolved polynomial equation is now precisely

    k E_(a,h)+dJ_h=-q V_h,
    C_h=kG_(a,h)+J_h.                               (11)

Here J_h has degree zero and twist four. If the left side of (11) is made
literally q-divisible, its quotient is automatically closed: multiplication
by q is injective on the locally free chain-Hom terms. Thus (11), with (1),
(2), (7) and the actual Ctilde retained, is a concrete tensor target for the
next actual division, not another statement of its abstract existence.
No J_h or V_h is supplied by this note.

## Reproduction and scope

Run python verify_positive_atiyah_cartan_offdiagonal_interface.py. It checks
the complete five-symbol compression and off-diagonal tensor, all eight free
Cartan-W coefficients, the natural derivative pairings and all ten free
three-form coefficients in (9). It also checks the graded derivative sign
and the physical Clifford anticommutator. No actual source values, actual
monad matrix, evaluated rank, selected-point test or source scan is used.
All previously frozen artifacts are unchanged. No fourth value is inferred.
