# Negative Euler repairs have a canonical full source balance

## Result and scope

Keep the actual nonzero monad scales a_m,b_m,c_m and the fixed coefficient/determinant markings. Let K(w) be any negative-quartic six-space endomorphism annihilating the Cartan summand. Thus

    K = R · cliff,                 R : Spin → V6,

with all sixty quartic coefficients allowed. Write T_K for the literal degree-four negative Euler lift. There are canonical source maps P_U and P_C such that the **entire columns**, not only their principal VV components, satisfy

    T_K B = B P_U,                 T_K C = B P_C.                 (1)

Here P_U has negative degree four, while P_C has positive/negative degrees (1,3). The second equality retains both its mixed and WW terms. Its exact formula below extends the Spin-to-Cartan calculation to both Spin-to-Cartan and Spin-to-Spin blocks.

Consequently the source U-row

    S_UU=P_U,                     S_UA=(c_m/b_m)P_C               (2)

cancels all these B companions, but necessarily leaves the c-column term

    −(a_m c_m/b_m) A(P_C).                                        (3)

Thus a free principal source choice cannot simply be reused as the full source: the lower mixed/WW equation fixes it through (2), subject to any other explicitly retained contributions in that degree. This is an exact comparison for the stated repair sector, not a computation of the actual fourth Bockstein.

## 1. Conventions and formula

Use `CLEAN-SOURCE-BALANCE-TENSOR-FOUNDATION.md` and its standalone
`universal_source_balance_helpers.py` definitions.
In particular

    cliff · spin=I,   Pi=I−spin·cliff,
    J6=G⊗J,          adj6(K)=J6^(-1) K^t J6,
    up=G⊗I,          low=up^(-1).

Cartan and Spin are orthogonal for J6. The algebraic Clifford coefficient matrix is M(v), and the positive one-form L_z with coefficient vector up·spin·z satisfies

    i_v L_z=M(v)z/3,              B(z)=3 i_x(L_z ∧ omega_W).       (4)

These are coefficient-frame formulas. A pairing-defined Clifford map M/nu cannot replace M without transporting the compensating physical nu factors. No determinant, equation, or monad scale is normalized away here.

Put j=i_w omega_W=−w du+u dw. Write C_3,C_4 for the positive-one-form coefficient vectors of the actual c column, in the du,dw components. They are linear in v and independent of u,w. Define

    P_ss=cliff · R,               P_U=−P_ss^dagger,

    P_C = (1/12) cliff [ adj6(K_u) low C_4
                        − adj6(K_w) low C_3 ].                   (5)

The dagger on P_ss uses the fixed two-dimensional alternating pairing. Formula (5) includes the full source variable of C. It is not an evaluation at one c input.

## 2. Full c-column proof

Because K kills Cartan, T_K C has zero VV component. Since adj6(K) has image in Spin, put

    F_i=−up adj6(K) low C_i = up·spin·R_i,   i=3,4.

All F_i have negative degree four. The Euler formula

    T_K C = (1/4) sum_i i_x(e_i ∧ E_(K_i) C)

gives its mixed coefficients exactly as

    (T_K C)_i = (5/4)F_i − (1/4) partial_i(uF_3+wF_4).           (6)

In particular u(T_K C)_3+w(T_K C)_4=0. The regular two-variable Koszul identity gives

    (T_K C)_mixed=L_beta ∧ j,
    beta=(partial_u R_4−partial_w R_3)/4=−3P_C.                 (7)

There is no division by u,w or a component of the actual cubic. The whole Euler output is i_x-closed. The unique WW component completing (7) to an i_x-closed form is

    −(M(v)beta/3) omega_W.

Uniqueness follows because an i_x-closed form supported only in WW is zero over the polynomial ring: multiplication by both u,w is injective. Therefore

    T_K C=−i_x(L_beta∧omega_W)=B(−beta/3)=B(P_C),                (8)

which proves the second identity in (1). In particular this companion does not vanish merely because its VV component vanishes.

The first identity in (1) is the full Spin-to-Spin balance from the cited theorem, plus the full vanishing of the Spin-to-Cartan B action. Both are also checked jointly with all sixty coefficients in the verifier below.

## 3. Forced source balance and the principal correction

Write the two monad source blocks as

    alpha_U=a_m A+b_m B,          alpha_A=c_m C.

Take the U-row (2), and initially set the A-row of S to zero. With the fixed first-column convention T_K alpha−alpha S, (1) gives

    (T_K alpha−alpha S)_U = a_m(T_K A−A P_U),
    (T_K alpha−alpha S)_A = −(a_m c_m/b_m) A(P_C).               (9)

A further reverse source S_AU contributes the explicit term −c_m C S_AU to the first formula; an A-end source must likewise be retained if added. Thus (9) does not discard either allowed source block.

The B map is polynomially injective: its WW coefficient is M(v)z, and M(v)^2=chi q0 I with chi nonzero. Hence, if no other term supplies this lower mixed/WW c degree, cancelling it forces S_UA=(c_m/b_m)P_C uniquely. With other contributions present, their known lower component must instead be included in this affine equation. No universal exclusion of those other sectors is claimed.

The c source A(P_C) has degrees (2,3), exactly the principal c degree. It is an A-source image in the full principal quotient, but it is not zero as a full prescribed-source expression. This explains why the earlier quotient tests remain valid while their arbitrary source representatives do not automatically give a complete primitive.

For the kernel-Euler symbol K=f(ell Q)·cliff, the mixed-U theorem determines Q uniquely whenever its two exact recovery tests hold. Formula (5) then determines the associated c source as well. It is not an additional free parameter available to repair the c column without rechecking U.

## 4. Reproducibility and boundary

Run `python verify_negative_euler_full_source_balance.py`. It retains all sixty coefficients of R, all sixteen coefficients of the cubic marking, and the full quadratic c-source variable. It verifies the whole exterior identities (1), (6)–(8), the beta recovery, closure, and source cancellation. These are universal free-symbol identities, not selected actual coefficients, actual-instance matrices/ranks, or numerical scans.

The actual residual has not been shown to satisfy the mixed-U tests or the coupled c equation. No fourth value, complete higher division, or original repair is asserted.
