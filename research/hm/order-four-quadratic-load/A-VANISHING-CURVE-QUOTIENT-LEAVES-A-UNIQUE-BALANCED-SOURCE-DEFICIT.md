# A vanishing curve quotient leaves a unique balanced-source deficit

## Scope

Use the full-U cancellation and retained sectors of
FULL-U-CANCELLATION-GIVES-A-CONSTRUCTIVE-TWO-STAGE-C-DIVISION.md.
The entire c-input tensor is retained. Let E be its Cartan VV residual,
and let sigma be the binary evaluation of f_cub^(-1) E. This statement
refines the first of that theorem's two tests. It does not assert that
the actual test passes or evaluate a fourth Bockstein.

Write v(r)=(r0^2,-r1^2,-r0 r1), r=(r0,r1)^t, and

    M(v(r)) = r l,          l=(-r1,r0).

Let lambda_w be the frozen negative cubic evaluation row and let Abar
be the Cartan part of A. The actual bicubic is

    F(r,w)=lambda_w Abar(v(r)) r.

Assume the principal c-source quotient vanishes on the whole bicubic.
Since sigma has bidegree (4,6) and F has bidegree (3,3), this says exactly

    sigma|conic = F t,       t of bidegree (1,3).              (1)

The quotient is a polynomial, not a localized quotient at ramification.
Its uniqueness follows because F is nonzero in the polynomial domain.

## The unique source kernel term

Set

    z=(-partial_r1 t, partial_r0 t)^t.                       (2)

It is independent of r and is a negative cubic. Since t is linear in r,
l z=t. Conversely the map z -> l z is an isomorphism from constant
spinors to positive binary linear forms, so (2) is unique. Put

    u(v,w)=M(v) z(w).

Then u|conic=r t. Therefore

    lambda_w [E-Abar(v)u]|conic = sigma|conic-F t = 0.        (3)

The full A-source subtraction has a spin component too. It is retained:

    cliff(A(u))=M(v)^2 z=chi q0 z.                          (4)

Thus it is divisible by the physical equation, not literally zero.
No normalizing replacement of chi q0 by an unmarked equation is made.

The first scalar test q0 | sigma is equivalent to t=0. Indeed the
positive Veronese parameterization has kernel (q0), and multiplication
by the nonzero F is injective. Hence the vanishing bicubic quotient alone
does not settle that scalar test: t records its precise remaining part.

## Why it is not a disposable source choice

If the residual is defined as dC-target and alpha_U=a_m A+b_m B,
changing the c-to-U source block by u/a_m subtracts A(u) but also
subtracts the entire companion

    (b_m/a_m) B(M(v)z).                                    (5)

That companion must be balanced by the actual middle/source equation.
It cannot be erased merely because the principal curve quotient vanishes.
The source block has physical degree four, since M has degree one and
z has negative degree three. Every expression is linear in the entire
c-input tensor and retains its parameter dependence.

The result identifies the unique kernel-spinor source needed to remove
this first quotient multiple; it neither constructs the compensating
middle correction nor changes the two-stage division criterion.

Run python verify_balanced_source_deficit.py.
