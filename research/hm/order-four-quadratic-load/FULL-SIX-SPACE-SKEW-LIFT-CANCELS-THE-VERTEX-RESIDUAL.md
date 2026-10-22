# A full six-space skew lift cancels the vertex residual, but not the ramification defect

## Result and scope

There is a global determinant-skew extension of the Cartan coefficient lift to
EVERY endomorphism of the six-space U tensor Lambda^2 V. Its spin/Cartan
blocks give an explicit regular correction which cancels the entire U-column
residual of the natural positive derivative primitive along the negative
vertex locus. This is a genuine new polynomial cancellation.

The correction does not solve the ambient division. Its middle operator has
no mixed-form-input to VV output, so it leaves unchanged the exact nonzero
ramification second-jet defect. All claims below are universal tensor
identities: every channel marking, physical q, and scalar is retained. No
actual source coefficient, actual-instance matrix/rank, or selected-point
evaluation is used. Restriction to the entire vertex locus is a geometric
restriction, not a chosen source instance.

Sources are the frozen full Cartan-Koszul homotopy, the higher Cartan lift
and product-anomaly note, the actual positive-Atiyah interface note, and the
actual ramification obstruction and its second-jet companion. None is edited.

## 1. The full six-space coefficient lift

Put V6=U tensor Lambda^2 V, with its induced alternating form J6. The fixed
positive volume and metric identify the six-dimensional U tensor V
coefficient factor, for EACH W component of the twelve-dimensional mixed
sector U tensor V tensor W, with the determinant dual of V6. The W factor
is retained throughout; the full mixed sector is not identified with V6.
All identifications retain the compatible fixed
Delta=det(V+W) line from the monad. Let K be ANY endomorphism of V6, and let
K^dagger be its J6-adjoint. Define E_K on U tensor Lambda^2(V+W) by

    E_K|VV=K,  E_K|VW= -K^dagger,  E_K|WW=0.                 (1)

The mixed block in (1) includes the determinant-dual identification, not a
literal equality between differently framed coefficient spaces. Define F_K
on three-forms by K on VVW, minus K^dagger on VWW, and zero on VVV. Then

    F_K(e_i wedge eta)=e_i wedge E_K(eta),  i in W,
    F_K^dagger=-E_K.                                       (2)

The adjoint in the second identity is for the U-symplectic determinant-valued
pairing of three-forms with two-forms. Both identities hold for all 36 entries
of K, including both off-diagonal spin/Cartan blocks. Thus for a homogeneous
negative-coordinate polynomial K(w) of degree d>0,

    T_d^6(K)(eta)= (1/d) sum_i i_x[e_i wedge E_(partial_i K)(eta)] (3)

is a global polynomial map E -> E(d), skew for the actual middle pairing.
Contraction squared is zero, proving K-valuedness. The proof of skewness uses
(2) exactly as in the frozen Cartan construction. The derivative and inserted
W vector are contracted naturally, so (3) is basis independent. All coefficient
endomorphisms are determinant neutral. The only remaining twist is d.

Unlike its Cartan-only predecessor, (3) need not kill the b-channel. This is
precisely the extra freedom used below. At v=0 it acts on mixed coefficients
by minus K^dagger, by homogeneous Euler. The Cartan-spin determinant-dual
block cannot be omitted.

## 2. The exact full positive derivative baseline

Keep the fixed right-commutator differential dT=[T,d_M], natural Euler
D0=diag(-2/5 on V,3/5 on W), and the complete natural primitive

    dT_nat(a)=a e0 -q kappa e_a,   Z_a=k e_a.

For q-selfadjoint trace-free positive H set h=(1/2)D_H q. Every moving K
frame and both monad-end actions are differentiated naturally. Then

    d(delta_H T_nat)-[e_H,T_nat]
       =a delta_H e0 -2 kappa h e_a -q kappa delta_H e_a.

Consequently the explicit global degree-zero cochain

    C0= -k a/(2 kappa) delta_H T_nat                         (4)

has exact defect

    dC0-a h Z_a
       =-k a/(2 kappa) K_H +q k a/2 delta_H e_a,
    K_H=a delta_H e0+[e_H,T_nat].                           (5)

Equation (5), not q-divisibility of K_H, is what differentiation proves.

The frozen gradient part differentiates with two DIFFERENT factors:

    delta_H R_D=2 R_h,  delta_H s_D=s_h,  delta_H K0=0.       (6)

Here R_D=rho^2(qD-R_q tensor wD), R_h=rho^2(hD-HR_q tensor
wD), and s_D is the full scalar wedge with the actual Ctilde. The first
factor includes both coefficient variation and output transport. The scalar
wedge has the compensating two-form transport and has factor ONE. The full
base tangent K0 has zero natural derivative. Thus the middle gradient in
(4) agrees with kG_(a,h), but its gradient A-to-U source is one half that
of kG. Replacing it by the old G source would change the actual cochain.
The Cartan coefficient part is differentiated with all spin/Cartan blocks
and the nonmultiplicative quartic lift correction retained.

For comparison, the natural negative-Euler coefficient alone produces no
new division: its apparent -a e_a/5 term cancels the exact source-gauge
contribution. No constructive claim is based on that coefficient.

## 3. The exact vertex U residual

Write P=Cartan(V6), Pi its projector, Pi_spin=1-Pi, and Hhat=rho^2 H on V6.
Let B_H=delta_H B. Trace-free positive H sends the mixed spin coefficient
of B entirely into the mixed Cartan coefficient. In particular its spin
projection is zero. This uses the full tensor, not merely a compression.

Transport the actual negative cubic endomorphism

    S_c=3 D N-N D,  N=-2 l(w) times the negative contraction

through the actual conformally symplectic cubic f. Its conformal scalar
cancels in transported adjoints and is not normalized away. Write S for
its extension by zero on the spin summand of V6. At v=0 the full old middle
operator on mixed Cartan coefficients is

    (3a/2) I + S^dagger/24.

The natural source UU entry is 7a/10, not the reduced -a/2; the natural
Euler b derivative is 4b_m B_H/5. All off-diagonal source entries vanish
along this entire locus. Since 4/5+7/10=3/2, equation (5) gives

    (K_H)_U|_(v=0)= -b_m S^dagger B_H/24,
    (dC0-a h Z_a)_U|_(v=0)
          = k a b_m S^dagger B_H/(48 kappa).                 (7)

There is no omitted source or right-arrow term in this calculation. The
right-arrow result follows from determinant skewness of the middle operator
and the negative-adjoint source convention.

For reference, the universal negative cubic identity is

    det(t I-S_c)=(t+18H_b)^2(t+10H_b)(t-6H_b), H_b=2a(w).    (8)

The verifier keeps all three Hamiltonian coefficients free. It computes a
universal representation identity, not an actual evaluated characteristic
polynomial. In particular S_c is invertible where a(w) is nonzero. The
vertex term in (7) is not something one may simply discard as q-divisible.

## 4. A literal global cancellation of (7)

Define the quartic full-six-space symbol

    K_vertex= -k a/(48 kappa) Pi_spin Hhat S,
    J_vertex,m=T_4^6(K_vertex),
    J_vertex,s=0, J_vertex,r=0.                             (9)

Its VV block goes from Cartan to spin; its mandatory mixed determinant-dual
block goes from spin to Cartan. Hhat is J6-selfadjoint. The mixed coefficient
of B_H is the negative Hhat transport of the mixed spin coefficient of B.
Therefore homogeneous Euler in (3) gives exactly

    (J_vertex,m B)|_(v=0)
        =-k a S^dagger B_H/(48 kappa).                      (10)

Combining (7)-(10) proves

    (d(C0+J_vertex)-a h Z_a)_U|_(v=0)=0.                    (11)

No channel coefficient is reset: multiplication by b_m in the U arrow is
what cancels (7). In fact the verifier checks (10) for EVERY quadratic
End(P)-valued S, every quadratic a, and every trace-free H simultaneously.
The negative symbol S_c is only one application of that general identity.

The full residual away from the vertex, including the c column and all
neighboring bidegrees, remains part of the unsolved division equation.

## 5. Why this correction leaves the ramification defect

For any mixed VW input eta, E_K eta is still mixed. In (3), negative wedging
produces VWW. Contraction by i_v produces WW; contraction by i_w produces
VW. Neither produces VV. Thus, for every K and d,

    [T_d^6(K)(eta_VW)]_VV=0.                               (12)

At a distinguished ramification shared input Y, the full VV coefficient is
zero, not just its Cartan projection. It follows that (9) has zero forced
ramification functional. The non-gradient part of delta_H T_nat has the
same filtration property: H preserves the positive/negative splitting, and
differentiating its coefficient lift does not introduce a mixed-to-VV map.
Consequently C0 and kG have exactly the same required mixed-interface value.

For the fixed signs t_a=-D_a j and w(t_a)=-2a, the independent complete
free-H Fierz calculation reads

    Pi(E_U(u))=-a^2 b_m g_L/(2 chi) Abar(vH,u).               (13)

Therefore their excess over the required ramification value is

    +k a^2 b_m g_L/(2 a_m chi) lambda Abar(vH,u),            (14)

and (9) does not change it. At u=ker M(v), simple ramification identifies
lambda Abar(vH,u) with h(v) times the nonzero positive second jet. This
geometric nonvanishing is the separate actual second-jet theorem; no source
instance is used here. It proves that (11) is useful but insufficient.

A successful continuation must change the actual mixed-form-input to
Cartan-VV interface while preserving the solved vertex balance, and must
then check both full monad arrows. Neither C_h,V_h nor beta4 is determined.

## Reproduction

Run `python verify_full_six_space_vertex_correction.py`. The script reuses
the frozen universal exterior helper and checks all 36 coefficient symbols,
all free H and Hamiltonian coefficients, the characteristic identity, the
literal vertex cancellation, the filtration screen, and (13). It does not
assign any actual HM coefficient or evaluate an actual matrix or rank.
