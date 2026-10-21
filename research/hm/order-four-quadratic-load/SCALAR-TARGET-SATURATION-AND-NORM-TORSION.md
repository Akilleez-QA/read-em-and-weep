# Scalar targets force residual rank two and determine the pure torsion divisor

## Hypotheses and conclusion

Work over C with G=SL2(F5), P=P(Sym^2 W), T=P(W*), and the ordered-root map nu:T x T -> P. Write D for its diagonal and Delta for the discriminant conic, so nu*Delta=2D. Use the established actual residual map

    m: E4=W tensor S6* -> K8=nu_*pr1*(F4(1)),

its actual pure subbundle S7* -> E4, its injective restriction j, and its nonzero divided pure cross section T2. Assume there is a scalar line summand L=O_T(a) of F4 such that T2 has values in L external-tensor O_T(6). Denote its nonzero scalar biform by f.

Then the following statements hold without choosing any actual coefficient:

1. The ENTIRE actual residual map factors through H=nu_*pr1*L(1)=S_(a+1), not just its pure restriction. Its generic rank is exactly two.
2. The saturated images of both m and j inside K8 are H.
3. If K_low is the sum of the other root-transformed target summands, then

       coker(j) = K_low direct-sum T_f,
       T_f = coker[S7* -> S_(a+1)].

   Its entire torsion subsheaf is T_f. This is a pure one-dimensional Cohen-Macaulay sheaf. Its determinant/Fitting divisor C_f has degree a+6, and

       nu*C_f = div(f) + div(tau*f),
       chi(T_f(t)) = (a+6)t + a+12.

4. Writing N=ker(m), c1(N)=-d, and I=im(m), the exact sequence

       0 -> S5*/N -> T_f -> H/I -> 0

   keeps all divisorial and punctual contributions. In particular the divisorial defect of I in H has degree

       t = a+10-d,

   while S5*/N has divisorial degree d-4. No local freeness of I or H/I is assumed.

For types IV and VII the hypothesis is automatic with a=18: all low-component coupling spaces vanish. Thus these two target types FORCE residual generic rank two, C_f has degree 24, and chi(T_f(t))=24t+30. This does not prove that either target type occurs. Nor does it prove that the first-order kernel persists under higher smoothing obstructions.

For type VI, write T2=(0,mu L0,H_scalar) as in TYPE-SIX-TWO-SCALAR-INJECTIVITY-GATE.md. The condition mu=0 implies the present hypothesis with a=14, so it is SUFFICIENT for residual rank two. In that case C_f has degree 20 and chi(T_f(t))=20t+26. No claim that lambda=0 alone suffices is made.

## 1. Why a scalar pure section controls the full actual map

Let pi_low:F4 -> F_low be projection away from L. The raw pure boundary is

    R(r,s)=delta_r(q0 ell_s^8)=D(r,s)^2 T2(r,s).

Under the hypothesis pi_low R=0. For each fixed r, pure eighth powers ell_s^8 span the Cartan Sym^8 W. Therefore the actual linear boundary pi_low delta_r annihilates q0 Sym^8 W. This is an assertion about the actual boundary, not a claim of genericity in its space of intertwiners.

The actual residual vectors are

    b(s)w=(ell_s^4) symmetric-product (ell_s^3 w).

Their second and fourth transvectants vanish, so they lie in that Cartan summand. The established cross-root and diagonal formulas for m therefore have zero low-target projections. Equivalently it suffices to check this on the distinct-root dense open; a morphism between locally free sheaves which is zero there is zero everywhere. Thus m factors through H globally, including the discriminant.

Its restriction j already has generic rank two. Since H has rank two, m and j have rank two and generic image H. The quotient K8/H=K_low is locally free, so the saturation of either image in K8 is exactly H.

## 2. Natural root frames and the norm divisor

For clarity the second complementary-root denominator is essential. Work affinely with P(z)=(z-r)(z-s), and represent a pure source by u(z) on the length-two root scheme. The full pure representative is b0(z)u(z), where b0(z)=ell_z^8. Keeping this representative rather than its root remainder is valid: their difference is P times an actual same-root square, whose boundary is zero.

Divide b0(z)u(z)=P(z)J(z)+L(z), where L interpolates its values at r and s. Evaluating the derivative identity at r gives

    J(r) = [(b0 u)'(r) - (b0(s)u(s)-b0(r)u(r))/(s-r)]/(r-s).

The boundary delta_r annihilates both b0(r) and b0'(r), since these are actual squares. The actual multiplication is -delta_r(q0 J(r)), so its natural root-value formula is

    j_r = -R(r,s)u(s)/(s-r)^2 = -f(r,s)u(s).

The same formula with the roots exchanged gives the other row. Consequently the determinant in these root frames is -f(r,s)f(s,r). This is the norm identity on the distinct-root open and hence globally as a line-bundle section. Indeed both sides are sections of nu*O_P(a+6)=O(a+6,a+6), using the natural determinant linearizations. This establishes the claimed divisor identity without treating two coincident roots as independent values.

In particular if f has exact diagonal order k, its swapped section has the same order. The pullback determinant has order 2k on D; because nu*Delta=2D, C_f has EXACT multiplicity k along Delta. All diagonal contributions are retained in the norm formula.

## 3. Purity, Hilbert polynomial, and actual-image accounting

Since j is injective between rank-two bundles, its cokernel T_f has locally a length-one locally free resolution. At any closed point in its support, the depth lemma gives depth at least one. Hence it has no zero-dimensional subsheaf or embedded point and is Cohen-Macaulay of pure dimension one. Its zeroth Fitting ideal is locally generated by det(j), so the norm divisor is also its exact Fitting divisor with generic lengths.

For n>=1, ch(S_n)=2+(n-1)H-(n-1)H^2/2. Also ch(S7*)=2-6H-3H^2. Thus

    ch(T_f)=(a+6)H+(3-a/2)H^2.

Riemann-Roch on P2 gives the stated Hilbert polynomial. The splitting of coker(j) follows from the direct-sum target and the vanishing low components, so T_f is the entire torsion, not merely one torsion subsheaf.

Now j(S7*) is contained in I. Quotienting the actual source sequence

    0 -> S7* -> E4 -> S5* -> 0

by N, and using N intersect S7*=0, yields I/j(S7*)=S5*/N. Quotienting H/j(S7*) gives the displayed exact sequence. The established Chern identity c1(I)=d-10 and c1(H)=a imply t=a+10-d. This is divisorial degree only; H/I can additionally have a zero-dimensional quotient.

## 4. Universal diagonal alternatives in the two scalar targets

The invariant filtration by powers of D has kth space

    H0(O(a-k,6-k))^G,    0<=k<=6.

Multiplication by the invariant determinant gives the successive inclusions. Clebsch-Gordan and the binary-icosahedral invariant degrees through 24, namely 0,12,20,24, give dimensions

    a=18: 3,2,2,1,1,1,1, followed by 0;
    a=14: 2,1,1,1,1,0,0, followed by 0.

It follows that the exact diagonal order k of a nonzero scalar f is

    a=18: k=0,2,or6;
    a=14: k=0 or4.

These are also the exact discriminant multiplicities in C_f. In the deepest cases the scalar has the rigid form

    a=18, k=6: f = c D^6 F12(r),
    a=14, k=4: f = c D^4 Polar_(10,2)(F12)(r,s),

where c is nonzero, F12 spans the degree-12 binary invariant line, and Polar denotes its unique indicated polarization. These formulas classify the relevant invariant lines only; no actual scalar is selected.

## 5. Constraint from the nondegenerate source form

The source has its canonical nondegenerate symmetric O(-5)-valued form q, and the established non-isotropic-kernel theorem says q_N is generically nondegenerate. Thus the scalar-factor cases above necessarily possess a nonzero kernel discriminant section

    det(q_N) in H0(O_P(2d-10))^G.

There is a useful exact divisorial identity retaining the actual-image defect. Use q inverse to form the symmetric target Gram morphism

    B = m q^(-1) m*: H* -> H(5).

It is generically nondegenerate. Its determinant is an invariant section of O_P(2a+10), and

    div(det B) = 2 D_(H/I) + div(det q_N).

Here D_(H/I) is the divisorial cycle of the actual target quotient, not of a silently saturated replacement. To prove this at a prime divisor, work over its DVR. The quotient E4/N=I is free there, so choose a splitting E4=N direct-sum L. The map m has blocks [0,A], and det(A) has valuation length(H/I). Jacobi's complementary-minor identity for the invertible form q gives

    det(B) = det(A)^2 det(q_N)/det(q)

up to frame units. Since q is nondegenerate, det(q) is a unit. The identity of valuations follows, and these determine the global divisor identity. It also proves generic nondegeneracy of B from that of q_N.

In particular the degree identity is

    2a+10 = 2(a+10-d)+(2d-10).

For a=18 this reads 46=2t+(2d-10), with even 6<=d<=28; for a=14 it reads 38=2t+(2d-10), with even 6<=d<=24. The existing finite second-Chern gates still apply. These are necessary constraints, not an exclusion of either scalar target.

## Reproducibility and limits

verify_scalar_target_saturation.py checks the low coupling vanishings, the scalar diagonal filtrations, and the exact Chern/Hilbert accounting by universal character and rational polynomial arithmetic. It uses no actual HM/source coefficients, selected matrices, evaluated ranks, or local-model experiment.

Dependencies: the actual pure-square injection and source quotient sequence; the actual cross-root/division formula; the seven F4 splittings; and NO-ISOTROPIC-RANK-TWO-RESIDUAL-KERNEL.md. No external write or publication is performed here. Nothing here settles which target type actually occurs or whether a first-order kernel survives later smoothing obstructions.
