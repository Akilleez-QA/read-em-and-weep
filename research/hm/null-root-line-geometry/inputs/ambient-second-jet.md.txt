# The declared ambient second jet

## 1. Problem and conventions

Work over a characteristic-zero field containing the coefficients, or over
the complex numbers. Put `R=k[h]/(h^3)` and let `X=C^4`, where `C` is the
smooth projective completion of `y^2=x^3-x`. The bundle in question is the
sole degree-zero cohomology `E` of

\[
K=[5N^{-1}\xrightarrow{\gamma}15N\xrightarrow{\delta_K}10N^3
\xrightarrow{\mathrm{ev}}2N^5],\qquad N=\mathcal O_X(\Theta),
\]

in degrees `(-1,0,1,2)`. Shifting all four degrees by one, as in the scalar
proof, leaves End degrees and the scalar labels unchanged. The actual
matrices and local contractions are those in the geometric dependency.
The signed determinant exponent is `5+15-30+10=0`, and `E` has rank two.

The task is to lift this classical bundle, with the explicit first-order
lift in [the source proof](first-order-source.md), to a left module for the
specific ambient algebroid through order `h²`. This is a declared deformation
problem; it does not identify every alternative presentation of an earlier
deformation problem with this one.

Set
\[
V_i=y_i\partial_{x_i}+\tfrac12(3x_i^2-1)\partial_{y_i},\qquad
\pi=V_1\wedge V_2+V_3\wedge V_4.
\]
The commuting global vector fields define the Moyal second jet
\[
f\star g=fg+h\mu_1(f,g)+h^2\mu_2(f,g),\qquad
\mu_1=\tfrac12\pi^{rs}(V_rf)(V_sg),\quad
\mu_2=\tfrac18\pi^{rs}\pi^{ab}(V_rV_af)(V_sV_bg).
\]
Indices are summed with `π12=π34=1`, `π21=π43=-1`. Matrix products preserve
the written order. Commutativity of the derivations proves associativity
by the exponential bidifferential construction, also for matrices.

Use ordinary Čech differential and Alexander–Whitney cup. On Čech–forms
the total product has sign `(-1)^(form_degree * next_Cech_degree)`.
Contraction by `Vr wedge Vs` means `i_Vs i_Vr`.

## 2. Explicit noncentral gluing

On the two original charts of one factor put `q=y/x` on the overlap and
`a0=-x/2`, `a∞=1/(2x)` on the respective charts. Then
\[
V(q)=(x+x^{-1})/2=\delta a.
\]
Pull back to the product cover and any refinement. Define
\[
b=\lambda(q_1\smile q_2+q_3\smile q_4),\qquad\lambda=15/4,
\]
\[
T=\lambda[(a_1\smile q_2)V_2+(q_1\smile a_2)V_1
 +(a_3\smile q_4)V_4+(q_3\smile a_4)V_3].
\]
Since `δ(q cup a)=-q cup δa`, `δb=0` and `δT={b,-}` with the displayed
Poisson sign. On each double/triple intersection set
\[
F_{ij}=1+h^2T_{ij},\qquad
A_{ijk}=1+hb_{ijk}+\tfrac12h^2b_{ijk}^2.
\]
These satisfy, modulo `h³`,
\[
F_{ij}F_{jk}=\operatorname{Ad}_\star(A_{ijk})F_{ik},\qquad
A_{ijk}\star A_{ikl}=F_{ij}(A_{jkl})\star A_{ijl}.
\]
Indeed `Ad_star(A)=1+h²{b,-}`, and the quadruple identity reduces to
the ordinary additive cocycle identity for `b`, exponentiated to order two.
Star corrections between two `hb` factors start in order three. Because
`T` is an ordinary derivation, `1+h²T` is a star-algebra map to this order.
This is an ambient second jet with verified descent, not just an arbitrary
Hochschild cochain. No all-orders extension is asserted.

The cocycle sign can also be calibrated without a citation convention:
for line transitions `l`, the normalized defect is
`μ1(ljk,lij)/lik = (1/2)i_π(At(l)^2)`, with the total-product sign above.
The triple unit contributes `-b`. Thus the first obstruction is
`ev_E(π)-b id`. With `Π=i_π(θ²)/2` and the compensated direction `π+15Π`,
the correct row-left convention is `b=-15Π` in cohomology. Its exact
short representative is the displayed `15/4` cup expression; the difference
from the antisymmetrized representative is explicitly accounted for below.

## 3. Complete module defect

Represent left-module coordinates by rows, with semilinear maps
\[
\phi_{ij}(v)=F_{ij}(v)\star G_{ij},\qquad
F_{ij}(G_{jk})\star G_{ij}=A_{ijk}\star G_{ik}.
\]
Write `Gij=gij+h uij+h² vij` with `gjk gij=gik`. Order one is
\[
u_{jk}g_{ij}+g_{jk}u_{ij}-u_{ik}
=b_{ijk}g_{ik}-\mu_1(g_{jk},g_{ij}).
\tag{1}
\]
After (1) is solved, order two is
\[
v_{jk}g_{ij}+g_{jk}v_{ij}-v_{ik}=-R_{ijk},
\]
where the full defect is
\[
\begin{aligned}
R={}&u_{jk}u_{ij}+\mu_1(u_{jk},g_{ij})+\mu_1(g_{jk},u_{ij})
 +\mu_2(g_{jk},g_{ij})+T_{ij}(g_{jk})g_{ij}\\
 &-b_{ijk}u_{ik}-\tfrac12b_{ijk}^2g_{ik}-\mu_1(b_{ijk},g_{ik}).
\end{aligned}\tag{2}
\]
Normalize on the left: `C2_ijk=gik^-1 R_ijk`. For End-valued row cochains,
\[
(\delta x)_{ijk}=x_{ij}+g_{ij}^{-1}x_{jk}g_{ij}-x_{ik}.
\]
Thus the order-two problem is exactly `δ(g^-1v)=-C2`.
In particular the `T` and `μ1(b,g)` terms must not be discarded in the
unprojected equation, and the triple unit must not be commuted through a
matrix under the star product. The generator computes only the full-sign
part of (2), not all of (2).
