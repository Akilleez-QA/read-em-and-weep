# Canonical Euler--Koszul splitting of the next transport channels

## Scope

The source-dependent transport class of
ACTUAL-SECOND-NORMAL-OPERATOR-TRANSPORT-HAS-A-SOURCE-PARAMETRIZED-CLASS.md
has target P4 tensor A and cubic dependence on the negative direction a,
linear dependence on h in D5. This note describes its universal coefficient
space and exactly which directions its proposed final contraction cannot see.
It does NOT identify that transport class with the actual next division or
compute any of its coefficients.

Fix the invariant quadratic pairing and compatible volume on the three-space
A. They identify covectors and vectors and define cross product and curl.
All derivatives below are in a, with h held fixed. Put

    F3 = Hom_G(D5, P4 tensor A tensor Sym^3 A*),
    F4 = Hom_G(D5, P4 tensor Sym^4 A*).

Their dimensions are ten and five. The contraction is

    c(T)(a,h) = <a,T(a,h)>.

The canonical right inverse is s(Q)=grad_a(Q)/4, since Q has degree four.
No evaluation of an actual direction or source enters this definition.

## 1. An explicit five-plus-five decomposition

For every cubic vector-valued polynomial T, componentwise in P4,

    a cross curl T = grad(<a,T>) - 4T.

Consequently the exact decomposition is

    T = (1/4)grad(c(T)) + a cross R,
    R = -(1/4)curl T,       div R=0.                  (1)

R has degree two in a. Conversely, for quadratic R,

    curl(a cross R)=a div R-4R.

Thus divergence-free R is the UNIQUE such preimage of a contraction-zero T.
All operations in (1) commute with G and retain the full h parameter.
In particular

    F3 = s(F4) direct_sum K,
    K = {a cross R : R quadratic and div R=0}.         (2)

This is a canonical decomposition after the fixed pairing/volume marking;
its two summands have dimensions five and five.

Equivalently, the polynomial Koszul sequence identifies K with quadratic
vector families R modulo radial families R=a ell, where ell is linear.
The former space has dimension six and the latter dimension one. Indeed

    Sym^2 A tensor A = 2A+V+P4+D5,
    dim Hom_G(D5,P4 tensor A tensor Sym^2 A)=6,
    dim Hom_G(D5,P4 tensor A)=1.

The identity div(a ell)=4ell gives the unique divergence-free representative.
The curl proof supplies an explicit polynomial inverse, so neither pointwise
rank arguments nor a noncanonical dimension-only splitting is being used.

## 2. The sixth direction invisible in the final quotient

Let beta2_a:A->P4 be the ACTUAL fixed second-symbol map. Its family is
quadratic in a and sheaf-injective on A O(-2). The unique quadratic source
family in Hom_G(D5,A tensor Sym^2 A*) is nonzero; using the fixed D5-to-
trace-free-symmetric-tensor marking it is

    ell2(a,h)=a cross S_h(a),
    B(a,h)=beta2_a(ell2(a,h)).                         (3)

Any nonzero scale of the marked ell2 spans the same line. B is nonzero:
otherwise sheaf-injectivity of beta2 would force ell2=0. This is a proof of
composite nonvanishing using injectivity, not an inference from nonzero legs.
The published fourth-family theorem identifies C B as the entire factoring
line in F4. Retain its actual beta2 normalization; it is not assigned a value
by this note.

The final universal contraction map is therefore F3 -> F4/(C B). Its kernel
has the CANONICAL decomposition

    ker(c mod C B) = K direct_sum C s(B),
    dim = 5+1=6.                                     (4)

Thus a cubic vector transport change is invisible in that final quotient
exactly when it has the form

    a cross R + lambda grad(B)/4,    div R=0.

The five Koszul directions have zero raw contraction. The sixth has nonzero
raw contraction B but becomes zero only after the actual second-symbol
quotient. These are different mechanisms. No canonical complement to C B
inside F4 is asserted, and no actual omitted term is assumed to lie in (4).

## Reproduction and sources

Run python verify_transport_channel_euler_koszul_splitting.py. It verifies
all differential identities with every cubic/quadratic coefficient free,
and all representation multiplicities in the existing exact character ring.
The actual factoring-line and sheaf-injectivity inputs are the pinned
FOURTH-BOCKSTEIN-AFTER-ACTUAL-THIRD-VANISHING.md and the actual second-symbol
rank theorem; the ten-channel target is the transport-class note above.
There are no selected actual source coefficients, actual-instance matrices,
rank evaluations, or fourth-obstruction values.
