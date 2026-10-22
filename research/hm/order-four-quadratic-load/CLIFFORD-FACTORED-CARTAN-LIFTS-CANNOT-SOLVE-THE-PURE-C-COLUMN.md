# A checked Clifford-factor construction and its exact principal obstruction

## Result

A useful family of global skew twist-four middle operators annihilates BOTH
full U-source channels A and B, not only their positive Cartan coefficients.
Nevertheless this family cannot, by itself, solve the next actual division.
The obstruction already occurs in the positive two-form coefficient of the
c-column, and is uniform for every nonzero negative direction a and positive
trace-free quadratic h. No actual source coefficient or point is evaluated.

Thus the valid annihilation construction does not license the conclusion
that its remaining c-column can always be absorbed by a source endomorphism.
A successful next-division primitive must go beyond this pure right-factor
ansatz. This result does not obstruct the unrestricted actual division.

## 1. Fixed tensor markings and the exact factor

Keep the actual channel coefficients, physical quadratic q=q0, compatible
determinant frame, and actual conformally symplectic cubic identification
f:Sym^3 W -> P of the frozen universal Cartan homotopy. The Clifford tensor
satisfies M(v)^2=chi q(v) I_U. Write

    J_v=rho^3(M(v)) on P,
    F_v=J_v^2-chi q I_P.                                      (1)

The action and all adjoints are transported through the actual f, without
rescaling it. The universal cubic characteristic identity gives

    (J_v^2-chi q I)(J_v^2-9chi q I)=0,
    F_v^2=8chi q F_v.                                        (2)

The Cartan projection of the a-channel is an exact intertwiner:

    J_v Pi(A(v,u))=Pi(A(v,M(v)u)),
    F_v Pi(A(v,u))=0.                                        (3)

This is a polynomial identity for every v and u, including q=0. It follows
because the positive adjoint action fixes v and acts on the U factor by M(v).
The verifier also checks the entire free-coefficient identity directly.

For a positive q-selfadjoint trace-free H, put h=(1/2)D_H q and use the full
Cartan compression C_H=f^(-1) Pi rho^2(H) f from the preceding positive-interface
note. Its normalization gives

    tr(C_H F_v)=8chi h,
    C_H F_v+F_v C_H=4chi h I+8chi q C_H.                       (4)

In particular (4), not an unmarked scalar multiple, is the Clifford relation
available modulo q. The off-diagonal positive derivative remains a separate
actual tensor; (4) does not discard it.

## 2. The full annihilation, including the mixed coefficients

Let R(w) be any End(P)-valued quadratic polynomial in the negative coordinate
coefficients, and set

    S(v,w)=R(w)F_v.

Its negative-coordinate degree is two and its TOTAL projective degree is four.
Use the same global lift as before, differentiating ONLY in w:

    T(S)(eta)=(1/2) sum_i i_x[e_i wedge E_(partial_i S)(eta)].   (5)

The construction and determinant-valued skewness remain valid when the
coefficients of S depend polynomially on v. Formula (5) therefore defines a
regular global skew map E -> E(4).

Since F_v is w-independent, differentiating the exact second identity of
(3) gives

    (partial_i S) Pi(A(v,u))=(partial_i R)F_v Pi(A(v,u))=0.

The a-channel has only a positive VV coefficient. Thus E_(partial_i S)A=0
BEFORE contraction in (5), and the WHOLE operator satisfies T(S)A=0. Its
mixed VW coefficient is not being inferred from the vanishing VV coefficient.
The b-channel has zero Cartan coefficient in every sector on which E_R acts,
so E_(partial_i S)B=0 as well. Consequently

    T(S)A=T(S)B=0                                             (6)

as literal global polynomial arrow identities. These derivative statements
are w-derivatives, not an assertion that a full natural positive pullback
may keep the moving Cartan projector or f fixed.

## 3. The sufficient ansatz and its necessary principal equation

The hoped-for restricted construction would choose R(w), with the required
parameter dependence on a,a,h, and a source endomorphism P_src of A of twist
four, such that

    T(S)C-C P_src-a h delta_(D_a)C is divisible by q.           (7)

The corresponding degree-zero cochain would have middle kT(S), source-AA
block kP_src, all other source blocks zero, and right component the negative
adjoint. By (6), its U-column is exactly zero. If (7) held, its quotient would
supply the desired closed V_h. This is only a sufficient ansatz, not a
normal form for all possible primitives.

We now prove that (7) cannot hold for nonzero a,h. Work uniformly over a
negative covector w where a(w) is nonzero. No particular actual covector is
chosen or evaluated. Set ell=i_w omega. In the actual f identification the
positive coefficient of the c-channel is

    p_C(w,z)=-ell z,             z in Sym^2 W.

Its source endomorphism contribution is divisible by ell and disappears in
P/(ell Sym^2 W). This quotient is evaluation at w. The natural negative
coefficient derivative, with the frozen Hamiltonian convention, is

    [delta_(D_a) C]_(VV)=(D_a ell)z,
    (D_a ell)(w)=2a(w).                                      (8)

Equation (8) follows from the exact Clebsch identity, not from replacing the
natural derivative by a derivative of the contracted coefficient alone.
The full lift's positive coefficient is S p_C. Hence (7), on q=0 and after
quotienting by ell, would imply

    -ev_w R(w) F_v(ell z)=2a(w)^2 h(v) z(w)                   (9)

for every v on q=0 and every z in Sym^2 W. All fixed nonzero channel/cubic
scales occur on both sides under the actual f marking and cancel in this
necessary equation. No determinant convention changes (9).

## 4. A coefficient-free contradiction

The operators F_v with q(v)=0 span the full selfadjoint trace-free five-space
in End(P). Indeed J_v^2-5chi q I is the nonzero positive-SL2 equivariant map
from harmonic positive quadratics to that five-space. Both are irreducible
five-dimensional representations. Restricting v to the null conic still
spans the harmonic quadratic space: its only quadratic relation is q.
Actual conformally symplectic transport by f identifies this five-space with
the full negative Sym^4 W summand. No value of f is needed.

The following universal binary fact is decisive:

    span { F(ell^2 b): F in Sym^4 W, b in W }=Sym^3 W.         (10)

Here Sym^4 W acts by its nonzero second-transvectant realization. To verify
(10) with every coefficient free, use an arbitrary abstract basis in which
ell=S. For g=sum_(i=0)^4 g_i S^(4-i)T^i and b=alpha S+beta T,

    (g,S^2 b)_2
      =(12alpha g_2-12beta g_1)S^3
       +(36alpha g_3-12beta g_2)S^2T
       +72alpha g_4 ST^2+24beta g_4 T^3.                    (11)

A row annihilating (11) for all free coefficients has all four components
zero, detected successively by alpha g_2, alpha g_3, alpha g_4, beta g_4.
Any nonzero marked intertwiner scalar multiplying this transvectant multiplies
all four coefficients together; it is retained and does not change their
common annihilator. No actual intertwiner is rescaled by (11).
This is a complete representation identity, not an actual-source matrix,
rank test, or selected-point calculation. Covariance proves it for every ell.

In (9), first take z=ell b. Then z(w)=0, so its right side is zero. Since the
F_v span the five-space, (10) forces the row ev_w R(w) to be zero. Returning
to (9) for arbitrary z now gives

    2a(w)^2 h(v) z(w)=0

for every v on q=0. This is impossible: a(w) is nonzero, some z has nonzero
evaluation, and a nonzero trace-free quadratic h does not vanish identically
on the null conic. A quadratic vanishing there would be a multiple of q,
whose trace-free component is zero. This proves the obstruction to (7).

The proof is independent of any equivariance assumption on R(w). Allowing
additional finite-group intertwiners in R therefore does not remove it.
Adding source-AA terms also cannot remove it, since those vanish in the same
quotient. Extra middle/source blocks or symbols outside the pure right-factor
family are genuinely required.

## Reproduction and limitation

Run `python verify_clifford_factored_cartan_principal_obstruction.py`.
It checks the complete marked Clifford identities (2)-(4), both full arrow
annihilations in (6), and the free-coefficient tensor identity (11). The
spanning and quotient arguments above then prove the impossibility result.
All source and channel parameters remain unassigned, and all frozen files
are unchanged. The unrestricted next-division cochains and the actual fourth
Bockstein remain unresolved.
