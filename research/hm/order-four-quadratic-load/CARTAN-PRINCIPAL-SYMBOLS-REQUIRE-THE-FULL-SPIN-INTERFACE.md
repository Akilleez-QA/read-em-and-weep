# Exact quadratic Cartan-symbol factorization and the missing spin interface

## Result and precise scope

The pure right-Clifford-factor family is not the full space of quadratic
Cartan symbols that annihilate the a-channel modulo q. There is an explicit
additional spin-interface term. Every such symbol has, uniquely modulo q,

    S(v)=B(v) Abar(v)^dagger,
    B(v)=R Abar(v)+Z M(v),                                 (1)

where B is linear in v, R is a constant endomorphism of P, and Z is a constant
map U -> P. Thus the missing sector is Hom(U,P)=V+D5, not merely an unexplained
eight-dimensional complement. The ACTUAL positive off-diagonal derivative
has an explicit nonzero D5 component in exactly this sector.

The corresponding global Cartan lift has an explicitly q-divisible FULL
A-column, with all mixed coefficients retained. This is a concrete component
for a coupled next-division ansatz, not a solution of the remaining c-column.
It does not make the earlier no-go an obstruction to the actual division.

## 1. Marked adjoints and a polynomial Clifford identity

Let Abar(v):U -> P be Pi(A(v)) in the actual Cartan identification. The dagger
uses the fixed alternating forms on U and P. To retain their relative
normalization, define the nonzero scalar c_A by

    Abar(v)^dagger Abar(v)=c_A q(v) I_U.                       (2)

The universal compatible tensor conventions in the verifier give c_A=2chi/3.
This checks that convention; the formulas below retain c_A and do NOT silently
normalize an independently changed relative pairing. In particular rescaling
one alternating form changes the dagger and c_A together.

With J_v=rho^3(M(v)) and F_v=J_v^2-chi q I, the exact identity is

    F_v=8chi q I-(8chi/c_A) Abar(v) Abar(v)^dagger.            (3)

Both sides are genuine polynomial tensors. The verifier checks (2)-(3) with
all three positive coordinate coefficients free. This is not a computation
at an actual positive point. Transport through the actual conformally
symplectic f retains its scale and the adjoint convention.

## 2. A global proof of factorization, not pointwise divisibility

Consider the positive null conic C={q=0}, parametrized by P(U). A positive
linear coordinate pulls back to O_C(2). The image of Abar(v) is the tangent
line plane ell_positive^2 U in Sym^3 U, transported to P. In bundle notation,

    Abar: U O_C(-2) -> P O_C

is everywhere injective. Multiplication by the square of a nonzero linear
form proves its rank directly. Its image is Lagrangian for the cubic apolar
form. Consequently the adjoint gives an exact bundle sequence

    0 -> U O_C(-2) -> P O_C -> U O_C(2) -> 0,                (4)

where the last map is Abar^dagger with the fixed symplectic identification
of U and its dual. Its kernel equals the first image because that image is
Lagrangian, not because one guessed a factor from fiberwise kernels.

A quadratic positive symbol modulo q is a morphism S:P O_C -> P O_C(4).
The condition S Abar=0 on C says that it kills the first term of (4). By the
UNIVERSAL PROPERTY OF THE QUOTIENT BUNDLE in (4), it factors uniquely through
Abar^dagger, by a global map

    B:U O_C(2) -> P O_C(4).

Such maps are exactly Hom(U,P) tensor H0(O_C(2)). Since H0(O_C(2)) is the space
of positive linear forms, B is the restriction of a unique linear polynomial
B(v). This proves the first factorization in (1), globally and uniquely
modulo q. Adding q times a constant endomorphism to S is precisely the
unseen choice of polynomial representative. This classification applies to
the Cartan principal symbol; it is not a classification of all possible
middle-bundle homotopies.

## 3. The exact missing term

The fixed Clifford/Clebsch splitting gives

    V tensor U=P plus U.

Its two projections on the universal tensor v tensor u are Abar(v)u and
M(v)u, with the pinned Cartan and spin injections. Therefore EVERY linear
B(v):U -> P has a unique decomposition

    B(v)=R Abar(v)+Z M(v).                                  (5)

The verifier checks the two inverse projection/inclusion identities, and
(5) for all 24 independent coefficients of B. No actual-instance matrix
or rank is computed. Combining (3) and (5) gives, modulo q,

    S=-(c_A/(8chi)) R F_v+Z M(v) Abar(v)^dagger.              (6)

The old pure right-F family is exactly the first term. The second is
parametrized by Hom(U,P), which decomposes as V plus D5 under the positive
SL2 and hence under the fixed finite-group marking. This is an explicit
structural decomposition, not only a dimension count.

The actual positive derivative enters this term directly. If H is positive
trace-free and q-selfadjoint, let Hhat=rho^2(H), let j be the fixed spin
injection, and define

    C_H=Pi Hhat|P,      Z_H=Pi Hhat j:U -> P.

In the fixed positive-volume convention one has the entire polynomial identity

    Z_H M(v)+C_H Abar(v)+Abar(vH)=0.                         (7)

Indeed Hhat acts as -H^t on the two-form coefficient, while
v tensor u splits into its Cartan and spin parts. The already-checked
opposite off-diagonal block c Hhat|P is nonzero on every nonzero H; selfadjointness
of Hhat shows the same for Z_H. Thus Z_H realizes the actual D5 summand of the
new term in (6), with its coefficient and relative adjoint markings retained.
Keeping only C_H would omit it.

## 4. The complete q-divisible A-column

Allow B(v,w) to be linear in v and quadratic in w, and set

    S(v,w)=B(v,w) Abar(v)^dagger.

The total degree is four. Use the canonical Cartan lift, differentiating
ONLY its negative-coordinate degree:

    T_2(S) eta=(1/2) sum_i i_x[e_i wedge E_(partial_(w_i)S) eta].

Because Abar and its adjoint are w-independent, (2) gives

    (partial_i S) Abar=c_A q (partial_i B).

The A-channel has only a VV coefficient, so this equality holds before the
outer contraction and proves the FULL global identity

    T_2(S) A=q L_B,
    L_B(u)=(c_A/2) sum_i i_x[e_i wedge (partial_i B)(v,w)u].   (8)

The P-valued coefficient on the right is included into U Lambda^2 V using
the fixed Cartan inclusion. In addition T_2(S)B_channel=0 exactly. The symbol
B(v,w) is not the b-channel B_channel; (8) deliberately distinguishes them.

The verifier checks (8) with all 24 linear tensor coefficients and all three
quadratic negative coefficients free; linearity covers the complete
72-coefficient family. Both VW and VV contributions are checked. The full
right-arrow statement is supplied by fixed determinant duality, not by
forgetting source-end actions.

If this middle term were part of a valid complete next-division cochain
with no further U-column corrections, its forced quotient would include
V_h|U=-k a_m L_B. It is only a component identity: closedness and the actual
full V_h cannot be claimed before the other arrow equations are solved.

## 5. The coupled equation and the necessary neighboring terms

Retain a source-AA operator P_src and an off-diagonal source A -> U operator
Q_src, both of twist four. The literal c-column divisibility target is

    T_2(S) C-C P_src
      -(a_m/c_m) A Q_src-(b_m/c_m) B_channel Q_src
      -a h delta_(D_a) C =0 modulo q.                       (9)

All monad coefficients remain unassigned. Equation (9) is the full expression,
not just its Cartan projection. Its positive principal equation contains
Abar Q_src. That term must not be omitted, but it cannot be inserted in
isolation either.

For the indicated bidegree of S, the necessary principal part of Q_src has
positive/negative coefficient bidegree (1,3). The mixed coefficient of
B_channel Q_src then has bidegree (1,4). No term of this bidegree occurs in
the single displayed T_2(S), in C P_src when P_src is restricted to its
principal (2,2) bidegree, or in a h delta_D C. A FULL twist-four P_src may
also have a (0,4) component; its mixed C coefficient DOES contribute (1,4).
Since q has
positive degree two, that coefficient cannot merely be q-divisible. It
requires cancellation by additional middle/source terms of the neighboring
bidegrees, including the legitimate source-AA term P_src^(0,4). This is a
genuine coupled-source problem. The decomposition (6)
and full identity (8) organize it, but do not solve it.

All nonmultiplicative quartic-lift terms from the frozen higher-Cartan note
remain present when multiplying or rebuilding symbols. No changes have been
made to any frozen predecessor, and no actual fourth value is inferred.

## Reproduction

Run `python verify_cartan_principal_symbols_with_coupled_sources.py`.
The test verifies the complete polynomial factor identities, the full
Cartan/spin splitting, (7), and both complete arrow statements in (8), with
all representation coefficients free. The bundle quotient argument in
Section 2 supplies the global factorization missing from a pointwise test.
