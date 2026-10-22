# A Jacobian identity excludes vanishing of the local trace-obstruction map

## Assumptions and result

Retain the hypotheses of [PR717, commit 7362df9da60a3b87b3200078a0145a376cc3056b](https://github.com/Akilleez-QA/read-em-and-weep/blob/7362df9da60a3b87b3200078a0145a376cc3056b/research/hm/nilpotent-trace-lift-invariance/PROOF.md) and the target reduction and harmonic normalization of [PR718, commit 2411fcd92acd738d0d8af7bebc79ee9191b276ef](https://github.com/Akilleez-QA/read-em-and-weep/blob/2411fcd92acd738d0d8af7bebc79ee9191b276ef/research/hm/trace-obstruction-target-reduction/PROOF.md). In particular k=C(L), S=k[X,Y], and f,g are a regular homogeneous pair. Write A=S/(f,g), with degrees deg f=3 and deg g=5, and retain the nonzero leading unit u. The preceding target reduction defines

    Obar_n: S1 -> A5,
    ell |-> [Psi(ell A0)/f],

where A0=[[f/2,0],[g,-f/2]]; this A0 is a matrix, distinct from the quotient ring A. For any fixed binary coordinates X,Y compatible with the harmonic normalization, put J=f_X g_Y-f_Y g_X. Then

    Y Obar_n(X)-X Obar_n(Y) = (u/15)[J] in A6.        (1)

Moreover [J] is nonzero and spans the one-dimensional socle A6. In particular Obar_n is nonzero. Thus the local obstruction map of PR716 has rank at least one and at most two. The lower bound is a structural theorem, not an evaluation of an actual matrix or a selected coefficient instance. It does not prove rank two, determine the kernel when the rank is one, or identify which local directions are actual global completion changes.

## 1. Derivation of the exact polynomial identity

For any ell, the ordinary contribution to Psi(ell A0) is ell(fx+gy). Thus it cancels identically in

    Y Psi(X A0)-X Psi(Y A0).

Only b_ell remains, with the exact formula from PR718, section 1, equation (4)

    b_ell=u(tau2(fg,ell f)/462-tau2(f²,ell g)/550).     (2)

Dehomogenize polynomial identities at X=1, put t=Y/X, and write F,G,L for f,g,ell. No actual source, coefficient or point is selected or evaluated. For L linear, the product rule and the general formula for tau2 give an expression for b_ell affine in the formal jets L,L', with L''=0. The coefficient of L' is

    u[(70 F F' G-42 F² G')/462
         -(60 F² G'-100 F F' G)/550]
      =u F(F'G/3-FG'/5).                             (3)

For ell=X one has L=1 and L'=0, while for ell=Y one has L=t and L'=1. Therefore t b_X-b_Y is the negative of (3). Euler's homogeneous identities give

    J(1,t)=3FG'-5F'G.

It follows, by rehomogenization of degree-nine polynomial identities, that

    Y Psi(X A0)-X Psi(Y A0) = (u/15) f J             (4)

in S itself. The preceding proof that f divides both Psi representatives allows division by f. Passing to A6 proves (1). In particular no choice of T survives in (4).

## 2. Elementary nonvanishing of the Jacobian class

Here is a self-contained commutative-algebra verification of the needed socle fact. Let m=(X,Y) and use Euler's identities to write

    [f,g]^t = M [X,Y]^t,
    M=[[f_X/3,f_Y/3],[g_X/5,g_Y/5]].

Then det M=J/15. Both f,g and X,Y are regular sequences in S. Their two-term Koszul resolutions give a comparison map lifting the quotient map A -> k=S/m: the map in degree one is the matrix expressing f,g in terms of X,Y (with the transpose appropriate to column conventions), and the map in degree two is multiplication by det M. This follows directly by checking the two Koszul differentials; equivalently it is the exterior square of the degree-one map.

For every finite-length S-module C supported at m, Ext^i_S(C,S)=0 for i=0,1. Indeed the Koszul resolution of k gives these vanishings for k, and a finite composition series with factors k gives the general statement by the long exact Ext sequence. The quotient A is finite-length because f,g are a homogeneous regular pair in two variables. Apply Ext to

    0 -> m A -> A -> k -> 0.

Since Ext^1_S(m A,S)=0, the induced map

    Ext^2_S(k,S) -> Ext^2_S(A,S)

is injective. The Koszul resolutions identify these modules, ignoring their harmless grading shifts, with k and A; the comparison above identifies the image of 1 with [det M]=[J/15]. Hence [J] is nonzero in A. The adjugate identity adj(M) M=det(M)Id also gives X det M,Y det M in (f,g), so this is a socle element. Its degree is six. Finally the complete-intersection Hilbert series

    Hilb_A(t)=(1-t³)(1-t⁵)/(1-t)²

has coefficient one at degree six and is zero in higher degrees. Thus [J] spans A6. To verify that this is the entire socle without importing the Gorenstein theorem, let [h] be a homogeneous socle class of degree r<6. Write

    Xh=af+bg,    Yh=cf+dg.

The regular-pair syzygy gives Ya-Xc=e g and Yb-Xd=-e f, with deg e=r-6<0; thus e=0. Coprimality of X,Y implies a=Xv,c=Yv and b=Xw,d=Yw. Cancelling X yields h=vf+wg, so [h]=0. Since the socle is graded and A has no components above degree six, Soc(A)=A6=k[J]. Nonvanishing and the socle argument used no reducedness assumption on the zero scheme or square-freeness of f or g.

## 3. Consequence and exact limitation

If Obar_n were zero, the left side of (1) would vanish, contrary to u nonzero, characteristic zero and [J] nonzero. Since its source and target both have dimension two, its rank lies in {1,2}. A nonzero alternating part of the multiplication pairing does not force the underlying 2-by-2 linear map to have rank two, so that stronger inference is not made.

Combining this with PR716, the full affine two-dimensional space of local second-normal solutions cannot have constant leading fourth-square class: some local tangent D has a nonzero class change a O_N(D), since a is a unit. This does not contradict invariance under actual global completion changes, which the cited PR685 already places in higher order and which do not move R4. Nor does it decide the value at the distinguished actual R. It rigorously excludes eliminating the local R dependence by asserting that the trace-obstruction map universally vanishes.

All calculations are universal identities in unspecified forms or formal jets. No actual HM/source coefficients, points, derivatives, selected model, or matrix-rank calculation are used.
