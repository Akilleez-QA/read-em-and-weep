# A three-term middle operator cancels full U but retains a source deficit

## Result and exact scope

There is an explicit universal three-term middle operator whose U column
can be canceled **as a full exterior tensor**, not merely after restriction
to the positive conic or passage to the principal source quotient. Its
forced c-column source balance is also explicit. The remaining high c
error has zero curve quotient but a nonzero balanced source deficit.
This supplies a concrete partial construction of the next division; it
neither supplies that division nor computes the fourth Bockstein.

All positive H coefficients, negative Hamiltonian coefficients, conformal
cubic channel scales, monad scales and physical equation scale remain
symbolic. The numerical constants below are coefficients of universal
operators, never assigned values of the actual source.

## 1. Marked operators

Use the full six-space, actual Cartan marking, determinant adjoints and
W-changing lift of `CLEAN-SOURCE-BALANCE-TENSOR-FOUNDATION.md` and
`universal_source_balance_helpers.py`. Let

\[
\mathcal L_P(R)(\eta)=i_x\bigl(F_P(R\wedge\eta)
                         -R\wedge F_P^\dagger\eta\bigr),
\]

where \(F_P\) acts on VVW by \(P\otimes D_a\), is zero on VVV and
VWW, and its full determinant adjoint is retained. There is no additional
factor one half in this displayed convention. Let \(T_4(K)\) denote the
full negative Euler lift, including its determinant-dual mixed action.

In balanced Cartan+Spin coordinates put
\(H_0=\widehat H|_{\rm Cartan}\), let
\(B_H=\operatorname{mixed5}(\operatorname{quartic}(H_0))\), and let
\(E_C,E_{10}\) be the marked Cartan and Spin-to-Cartan inclusions. Define

\[
T_0=\frac38\mathcal L_{aE_C(H_0)}(R_q)
    -\frac32\mathcal L_{aE_{10}(B_H)}(R_q)
    +\frac38\mathcal L_{a\Pi}(R_h).                         \tag{1}
\]

The physical Clifford convention is \(M(v)^2=\chi q_0 I\). In the
verifier \(q_0=(xy+z^2)/\theta\), so \(\chi=\theta\); this retains,
rather than normalizes away, the physical equation scale. The marked
positive trace-free tensor is

\[
H=\begin{pmatrix}h_a&h_b&h_c\\h_d&h_a&h_f\\2h_f&2h_c&-2h_a\end{pmatrix}.
\]

Set

\[
Z_H=\begin{pmatrix}h_f&h_d\\h_a&-h_f\\h_c&h_a\\h_b&-h_c\end{pmatrix},
\qquad K_s=\frac{3a^2}{4\chi}Z_H,
\qquad K=K_{\rm inc}K_s\,\mathrm{cliff}.                    \tag{2}
\]

Here \(Z_H=6P_{\rm std}B_H\), an exact marked Clebsch identity, so (2)
is an intrinsic Spin-to-Cartan coefficient in these fixed conventions.
Its negative coefficient degree is four. All lifts in (1)-(2) are the
established global determinant-skew polynomial lifts; no locally chosen
middle action is substituted for their mixed companions.

## Fixed Atiyah representative

The target is the pinned natural Cartan/Atiyah chain representative of
`UNIVERSAL-MONAD-CLIFFORD-HOMOTOPY-AND-HAMILTONIAN-DEFECT.md` and
`UNIVERSAL-CARTAN-KOSZUL-MULTIPLIER-HOMOTOPY.md`, Section1. In this source
frame its left arrow has Z_U=0 and Z_A=k_At c_m delta_D C, with the fixed
common scalar k_At retained. The action is the negative-coordinate
deformation **after natural K pullback**, namely
`delta_D(i_x Z)=i_x rho^3(D)Z`; it is not fixed-wedge differentiation.
The verifier implements exactly `i_x action(D,Ctilde)` with that same
unchanged c-source frame. Thus full-U cancellation below concerns this
pinned representative, not an arbitrary gauge-equivalent target.

## 2. Full U cancellation

The literal exterior identities are

\[
T_0 A=0,\qquad T_4(K)B=0,\qquad T_0B+T_4(K)A=0.             \tag{3}
\]

The verifier checks every form coefficient in (3). In particular

\[
(T_0B)_{VV}=-K_{\rm inc}K_sM(v),
\]

and the mixed coefficients cancel as well; no WW error is discarded.
For the actual nonzero monad scales
\(\alpha_U=a_mA+b_mB\), \(\alpha_A=c_mC\), the middle operator

\[
T=T_0+\frac{b_m}{a_m}T_4(K)                                \tag{4}
\]

therefore annihilates the entire U column. No reverse c-source or
additional Euler-kernel repair is required for this member. Equations (1)-(4) use the normalized representative with its common
Atiyah multiplier stripped off. The actual middle is k_At times (4),
and every actual source block below is also multiplied by k_At. Any
additional fixed common probe multiplier multiplies middle, source,
and target together.

## 3. The forced c source is not free

Keep the actual full c column \(C\), including its mixed coefficients
\(C_3,C_4\). The exact full source-balance theorem gives

\[
P_C=\frac1{12}\mathrm{cliff}
 \bigl[\operatorname{adj}_6(K_u)\,\mathrm{low}\,C_4
       -\operatorname{adj}_6(K_w)\,\mathrm{low}\,C_3\bigr],
\qquad T_4(K)C=B(P_C).                                    \tag{5}
\]

The checker verifies (5) again with the entire quadratic c-source free.
With differential convention \(dT=T\alpha-\alpha S\), the required
source block is \(S_{UA}=(c_m/a_m)P_C\). It cancels the complete lower
mixed/WW c companion of (4), and leaves the normalized high residual

\[
E_c=T_0C-a h\,\delta_{D_a}C-A(P_C).                         \tag{6}
\]

Thus the actual c error for target \(a h Z_a\) is
\(k_{\rm At}c_mE_c\). Any additional fixed common probe multiplier
multiplies this residual too. Both
\(a_m\) and \(b_m\) cancel from (6) only after the explicit source
balance, not by setting those channels equal to one.

## 4. Exact nonzero source deficit

The VV coefficient of (6) is entirely Cartan. Retain the actual uniform
C5-compatible conformal cubic marking

\[
f_{\rm std}=\begin{pmatrix}0&0&F_C&0\\F_A&0&0&0\\0&0&0&F_D\\0&F_B&0&0\end{pmatrix},
\quad F_A=-9F_BF_C/F_D,
\]

with all three independent scales nonzero and unassigned. Write
\(f=P_{\rm std}f_{\rm std}\), \(\ell=uT-wS\), and use the frozen sign
\(p_C=-f(\ell z)\). The entire c-source is
\(z=z_0S^2+z_1ST+z_2T^2\). The positive conic is parameterized by the
free spinor \(r=(r_0,r_1)\), with
\(v=(r_0^2,-r_1^2,-r_0r_1)\). Let

\[
\lambda_w=(u^3,u^2w,uw^2,w^3)f^{-1},\quad
F=\lambda_w\overline A(r^2)r,\quad
\sigma=\lambda_w(E_c)_{VV}.
\]

Exact symbolic factorization gives
\(\sigma|_{q_0=0}=F\,t\), with \(t\) of cover bidegree \((1,3)\).
It is not zero. With
\(D=(hS+lT)\partial_S+(kS-hT)\partial_T\) and
\(2a=ku^2-2huw-lw^2\), one exact coefficient is

\[
[z_0h_ck^2r_0u^3],t=-\frac{9F_BF_C}{4F_D\theta}\ne0.       \tag{7}
\]

Only nonzero channel/frame units were divided out. This is a universal
free-coefficient identity over the whole compatible stabilizer orbit,
not a selected source value. The monomial is parameter-harmonic: the
Hamiltonian trace operator \(\partial_h^2+4\partial_k\partial_l\)
does not affect its \(k^2\) coefficient. The actual probe and monad
factors multiply (7) by their retained nonzero scalars.

Equation (7) proves that this particular fully U-balanced member fails
the first physical sigma-divisibility test. It does **not** exclude the
remaining four-parameter principal family or other middle sectors.
The exact meaning of \(t\) as a unique residual \(M(v)z\) source with a
mandatory B companion is recorded in
`A-VANISHING-CURVE-QUOTIENT-LEAVES-A-UNIQUE-BALANCED-SOURCE-DEFICIT.md`.
The subsequent two-stage test is
`FULL-U-CANCELLATION-GIVES-A-CONSTRUCTIVE-TWO-STAGE-C-DIVISION.md`.

## Verification

Run `python verify_simple_middle_full_u_and_forced_c_deficit.py`.
The full-U and forced-source identities use literal polynomial equality,
not any curve-division algorithm. The final factorization and coefficient
(7) are checked directly. No curve-remainder algorithm is used by this
verifier, and its conclusion does not depend on a coefficient-extraction
normal-form certificate.
