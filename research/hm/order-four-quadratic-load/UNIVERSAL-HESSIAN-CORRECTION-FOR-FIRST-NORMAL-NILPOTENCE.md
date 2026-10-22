# An explicit universal Hessian correction for first-normal nilpotence

## Result and limits

For ANY homogeneous binary cubic f and quintic g, there is an exact polynomial identity expressing the square of their Euler-decomposition determinant as a combination of f^2, fg, g^2. It yields an explicit square-zero trace-free lift modulo q^2 of the familiar cone nilpotent, where q=xz-y^2 is the universal A1 equation.

This is a universal symbolic identity, not an evaluated actual HM local model. No chosen HM coefficients, matrix ranks, local-model scan, or experimental scalar are used. It gives local correction formulas that may support an absolute secondary-operator calculation. It does NOT assert that these formulas glue through the actual nonsplit quintic-generator extension, identify them with the unique global midpoint lift, or evaluate the positive cubic Bockstein.

## 1. A universal identity for two symmetric two-by-two matrices

For symmetric matrices U,V and a column z, put

    mix(U,V)=U11 V22+U22 V11-2 U12 V12.

Direct polynomial expansion gives

    det(Uz,Vz)^2
      =(z^tUz)(z^tVz) mix(U,V)
       -(z^tUz)^2 det(V)-(z^tVz)^2 det(U).             (1)

The companion test verifies (1) with six independent matrix-entry variables and two independent vector-coordinate variables. These are universal indeterminates, not actual bundle matrices.

## 2. Euler converts (1) to an ideal-square identity

Let f,g have degrees p,q greater than one. Let H_f,H_g be their Hessian matrices, and J=f_a g_b-f_b g_a. Euler identities give

    H_f z=(p-1) grad(f),  z^t H_f z=p(p-1)f,
    H_g z=(q-1) grad(g),  z^t H_g z=q(q-1)g.

Applying (1) therefore yields

    J^2 = pq/((p-1)(q-1)) fg mix(H_f,H_g)
          -p^2/(q-1)^2 f^2 det(H_g)
          -q^2/(p-1)^2 g^2 det(H_f).                 (2)

Use the canonical Euler decompositions

    f=aF+bH,  F=f_a/p, H=f_b/p,
    g=aG+bK,  G=g_a/q, K=g_b/q.

Their determinant Delta=FK-HG equals J/(pq). For p=3,q=5, equation (2) becomes

    Delta^2 = fg mix(H_f,H_g)/120
              -f^2 det(H_g)/400-g^2 det(H_f)/36.       (3)

Thus Delta^2 belongs to (f,g)^2 by an explicit universal formula. No inference from support, length, or generic rank is needed.

## 3. An actual equation-level first-normal correction

Let R=C[x,y,z], q=xz-y^2, and Cmat=[[x,y],[y,z]]. Interpret the even polynomials F,H,G,K as arbitrary lifts from R/(q) to R. Set

    u=(F,H) Cmat (F,H)^t,
    v=(F,H) Cmat (G,K)^t,
    w=(G,K) Cmat (G,K)^t,
    Delta=FK-HG.

The two-by-two Gram determinant identity is EXACT over R:

    u w-v^2=q Delta^2.

Consequently the trace-free matrix

    N0=[[v,-u],[w,-v]]

satisfies N0^2=-q Delta^2 I. Modulo q it is the cone nilpotent built from f,g.

Write a correction T=[[t,s],[r,-t]]. Then

    (N0+qT)^2=q(-Delta^2+2vt-ur+ws) I  modulo q^2.

Choose even lifts of the Hessian expressions

    t=mix(H_f,H_g)/240,
    r=det(H_g)/400,
    s=-det(H_f)/36.

Equation (3) proves that the scalar in parentheses is zero modulo q. Therefore

    (N0+qT)^2=0 modulo q^2.                            (4)

The transverse degrees match: u,v,w have degrees6,8,10; q has degree4; and s,t,r have degrees2,4,6. Thus (4) respects the degree pattern of the actual homogeneous (3,5) vertex pair. Changes of even polynomial lifts only modify the correction by higher-q terms or by another first-normal correction; no unique lift is claimed locally.

## 4. The exact unresolved gluing and comparison

The actual cubic generator is a line subbundle and the actual quintic generator exists only modulo cubic multiples, in a proved nonsplit extension. Hessians of a changed generator contain derivative terms, so the displayed T must not be declared invariant under those changes without a calculation. In particular a universal formula on a chart is not a global splitting of that extension.

The midpoint theorem separately proves existence and uniqueness of a GLOBAL invariant square-zero adjoint lift. To use (4) for the positive cubic gate, one must compare its generator-change corrections with that global lift and then compute the first-normal obstruction to lifting the twisted differential operator with symbol h a D_a. Neither equation (3) nor nilpotence alone supplies this operator obstruction.

The useful new datum is the explicit Hessian correction in place of an existential local ideal-square membership. It preserves, rather than discards, the remaining frame and normal-extension comparison.
