# The conormal Porteous class is eighteen on the conic plus six points

## Statement

For the actual quadratic-net conormal map

    theta:E=A O_R(-6) -> F=N*_(T/P6),

the rank-drop scheme is the reduced disjoint union C0 and Z6. Its virtual codimension-two Porteous class has degree 24. The localized contributions are exactly

    18 from the conic C0,     1 from each point of Z6.

This accounts for the class as 18+6, without replacing the actual positive-dimensional degeneracy by a hypothetical length-24 scheme.

## 1. The kernel degree on the conic

Retain Q(x,y)=M(x)y=N(y)x and the parametrization Phi(p)=[q0(p)p:g(p)]. Along C0 the matrix N(g(p)) has rank two and right kernel spanned by p, whereas the q0 M block vanishes.

The adjugate matrix of N(g(p)) has homogeneous entries of degree six. On a dense open its columns are proportional to the coordinate vector p. Since this vector is primitive in the polynomial ring, each proportionality factor is a polynomial. Thus there is a homogeneous degree-five vector a(p) such that

    adj N(g(p))=p a(p)^t.                            (1)

For example polynomiality follows from the identities p_i r_j=p_j r_i for each column r, using that the coordinate entries have greatest common divisor one. Formula (1) is an identity of universal polynomial tensors, not an evaluation of selected coefficients.

Rank two on C0 means that a(p) is never zero there. Its line is the left kernel of N(g(p)). The untwisted kernel line in A O_C0 is therefore O_C0(-5). Tensoring with the source twist O_C0(-6) gives

    K=ker(theta|C0)=O_C0(-11)=O_P1(-22).             (2)

Here O_C0(1)=O_P1(2). Self-dual identifications of A change only fixed invertible bases and do not change the degree.

## 2. The intrinsic excess line

Let C be the rank-two cokernel of theta|C0. Since E and F have the same first Chern class, the kernel-image-cokernel sequences on C0 give

    deg C=deg K=-22.

Consequently the rank-two bundle Hom(K,C) has degree

    -22-2(-22)=22.

The first derivative of theta normal to C0 gives the intrinsic map

    N_(C0/R) -> Hom(K,C).

It is a subbundle injection. Locally a rank-two matrix can be split into an identity block and a two-entry residual column; the reduced degeneracy ideal (q0) means those entries are q0 times functions with at least one a unit. The normal derivative is therefore nowhere zero.

The normal line of the smooth plane conic has degree four. Hence the excess quotient line

    L_ex = Hom(K,C)/N_(C0/R)

has degree 22-4=18.

## 3. Reduction to the ordinary zero-section excess formula

To justify that this line supplies the Porteous excess, pass to the bundle P(E) of source lines over R, with projection pi and tautological line O(-1). The map theta defines a section

    s of pi*F tensor O(1),

a rank-four bundle on the smooth fourfold P(E). Its zero scheme parametrizes lines in the kernel of theta.

The map has rank exactly two at every point of C0 and Z6. Along C0 this follows from rank N(g)=2. At Z6 the q0 M block has rank two and N(g)=0. Thus the section zero scheme is a copy of C0, embedded by its kernel line K, together with six points. Locally the two directions in E/K are cut transversely by the identity block, and the remaining equations are precisely the two-entry residual column. The equality of degeneracy schemes proved in REDUCED-CONORMAL-DEGENERACY-SCHEME.md therefore identifies the zero scheme scheme-theoretically with this reduced curve and the six reduced points.

The curve is a regular embedding of codimension three in P(E). After removing the two transverse vertical equations, its excess quotient is exactly L_ex from Section 2. The ordinary zero-section excess-intersection formula consequently assigns it

    c1(L_ex) cap [C0],

of degree 18. Each of the six isolated reduced zeros is transverse in the fourfold and contributes one. All hypotheses of this excess formula are supplied by the local identity-block description and the previously proved reduced scheme structure; no expected-codimension assertion is applied to the original degeneracy curve.

For comparison with the total class, write xi=c1(O_P(E)(1)). The projective-bundle formula for lines gives

    pi_*(xi^2)=1,
    pi_*(xi^3)=-c1(E),
    pi_*(xi^4)=c1(E)^2-c2(E).

Thus

    pi_* c4(pi*F tensor O(1))
      = c2(F)-c1(F)c1(E)+c1(E)^2-c2(E)
      = c2(F-E)=24H^2.

The localized degrees calculated above sum to this class: 18+6=24.

## Scope

This is an excess-intersection calculation for the actual quadratic-net conormal map, not an assertion of a finite rank-drop locus and not a computation of any outstanding adjoint multiplication rank. Its inputs are the exact bilinear scaffold, the smooth cubic surface, and the reduced degeneracy scheme. No selected HM/source coefficients, evaluated actual matrices or ranks, scans, or experiments are used.
