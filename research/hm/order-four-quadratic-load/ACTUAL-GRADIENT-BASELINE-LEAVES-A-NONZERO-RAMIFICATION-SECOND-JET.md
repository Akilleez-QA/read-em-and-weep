# The actual gradient baseline leaves a nonzero ramification second jet

The existing regular gradient baseline G does not already realize the
necessary mixed-form value. Its discrepancy is an explicit nonzero second
positive jet of the actual cubic. This identifies the value that a further
correction must supply, with the physical multiplier k retained. It does
not construct that correction or evaluate the fourth Bockstein.

## 1. Fixed conventions and actual inputs

Use G, E=dG-a h e_a and the full residual equations (10) of
ACTUAL-POSITIVE-ATIYAH-DERIVATIVE-HAS-A-SURJECTIVE-P4-TENSOR.md. Thus

    E_U=-a b_m i_x[L wedge R_h wedge t_a],
    E_A=(a b_m c_m/a_m) B s_(a,h).

Write R_h=H R_q(v), with H positive q-selfadjoint and trace-free, and
h(v)=v(R_h). Define v_H by R_q(v_H)=R_h. This is the marked polar-vector
identification; in a compatible row-coordinate convention v_H=vH. The
physical q is not replaced by an unmarked discriminant.

The negative convention from
UNIVERSAL-CARTAN-KOSZUL-MULTIPLIER-HOMOTOPY.md is

    j=i_w omega,   w(D_a j)=2a,   t_a=-D_a j.

In particular w(t_a)=-2a. The same source's Fierz identity (14), polarized
linearly in the positive covector, gives

    Pi[L(u) wedge R_h]=-(g_L/(4chi)) Abar(v_H,u).     (1)

Here g_L is the full two-dimensional triple trace and M(v)^2=chi q(v).
Neither is normalized away.

## 2. Exact residual on the distinguished ramification input

Use u,z,Y,lambda at an arbitrary actual ramification pair as in
ACTUAL-RAMIFICATION-DETECTS-A-NONZERO-MIXED-FORM-MIDDLE-VALUE.md:

    M(v)u=0,
    p_C(w,z)=A(v,u)_(VV),
    Y=C(z)-A(u)-(b_m/a_m)B(u).

The full VV coefficient of Y is zero. Extracting VV from the three-form
in E_U uses its negative contraction, with positive sign:

    (i_x[L(u) wedge R_h wedge t_a])_(VV)
       =w(t_a) L(u) wedge R_h.

Together with (1), this gives the exact equality

    lambda Pi(E_U(u))
      =-a^2 b_m g_L/(2chi) lambda Abar(v_H,u).        (2)

The A-source residual is a B-image, hence has zero Cartan-VV projection.
The full column equations for G, including its source block, now imply

    lambda Pi(k G_middle Y)
      =2k a^2 h z(w)
       +k a^2 b_m g_L/(2a_m chi) lambda Abar(v_H,u). (3)

The first term is precisely the value required of an actual primitive.
Consequently, if C_h=kG+J is the actual division primitive, its correction
must satisfy

    lambda Pi(J_middle Y)
      =-k a^2 b_m g_L/(2a_m chi) lambda Abar(v_H,u). (4)

All source blocks are allowed in deriving (3),(4): lambda kills their
projected images on this pair. The factor a_m enters by dividing the full
U-column, not by changing the marking of u. The residual source half-factor
in a differentiated homotopy is not substituted for the source block of G.

## 3. The new residual is nonzero

Write v=r^2 and u a nonzero multiple of r, only as abstract spinor lines.
At a ramification pair, the cubic functional lambda satisfies

    lambda(r^3)=lambda(r^2 m)=0,
    lambda(r m^2)!=0

for any transverse spinor m. The last assertion is exactly SIMPLE
ramification of the positive-coordinate cubic over the negative line,
proved by the reduced twelve-point ramification orbit. It is not an
assumption about an arbitrary singular cubic.

The tangent space to the positive null cone at r^2 is rU. Its normal
component for v_H is nonzero exactly when h(v) is nonzero, because
D_(v_H)q(v)=2h(v). Hence the Cartan product Abar(v_H,u), modulo r^2U,
is a nonzero multiple of r m^2 whenever h(v)!=0. Thus

    lambda Abar(v_H,u)!=0  if h(v)!=0.               (5)

For every nonzero a,h, at least six of the actual twelve pairs have both
a(w) and h(v) nonzero, by the degree-two/degree-four orbit count. Equations
(2) and (4) are nonzero there. The gradient baseline therefore requires a
genuine further mixed-form correction, even on these distinguished inputs.

This is an exact necessary value for that correction, not an obstruction to
its existence. Existence of the actual next division is already known from
third-order vanishing. Neither (4) nor the nonzero local jet alone determines
its global divided class or its final quotient.

## Verification scope

The verifier retains free positive H, free Clifford scale theta, all
positive and negative coordinates, and free spinor input. It checks the
polarized Fierz projection and the exact negative contraction sign. Actual
smoothness, simple ramification, and source markings are the cited geometric
inputs; no actual source coefficients or actual point are evaluated.
