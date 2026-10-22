# The actual corrected fourth source has a forced nonzero parameter trace

## Actual statement and scope

Let C=coker(q0:M0->M2), and let J be the image of the original kernel K=(A+D5)xi in C. Since a xi=q0 zeta_a for a in A,

    J=D5 xi_Q.

No dimension of J is required below. Write Cbar=C/J. The actual corrected class needed for the fourth division is canonically

    x(a,h)=[v_h(a)-b(a,h)zeta_a] in Cbar,
    q0 v_h=a h zeta_a,
    [a v_h]=beta2_a(b(a,h)).                        (1)

The fixed-probe raw cubic theorem proves that b is the nonzero canonical linear correction. The family v_h can be chosen trace-free in its quadratic parameter a, but x CANNOT be trace-free. Its invariant parameter trace is a NONZERO injective D5-valued family. This supplies a forced part of the actual next source, not a fourth Bockstein value.

## 1. Independence and symmetric multiplication

Changing v_h changes it by K. Its image in Cbar therefore does not change. The correction b is uniquely fixed by the sheaf injection beta2. Thus x is independent of the ambient right inverse used to produce v_h.

For a,c in A, commutative multiplication and the cyclic relation give

    q0(a zeta_c-c zeta_a)=ac xi-ca xi=0.

The difference belongs to K and is zero in Cbar. Hence there is a well-defined symmetric linear map

    T:Sym^2 A -> Cbar,   T(a symmetric c)=[a zeta_c]. (2)

Its quadratic diagonal is t(a)=[a zeta_a]. The invariant trace component is zero ALREADY in the ambient M2. Indeed POSITIVE-FIRST-BOCKSTEIN-VANISHES-BY-CYCLIC-RAO.md gives M0=1+A+V+D5 and ker(q0 on M0)=C xi. Thus (q0 M0)^G=0. The exact cokernel C has no invariant, so M2^G=0; this also follows directly from the pinned character M2=A+2V+3P4+4D5. The parameter trace of the equivariant quadratic family a zeta_a belongs to M2^G and is therefore zero. Consequently T factors through Sym^2_0 A=D5, without using any lower normal-operator comparison.

This T is NONZERO. Indeed multiplication by b in A kills J by first-Bockstein vanishing, so descends to Cbar; applied to t(a), it gives [b a zeta_a]=beta2_a(b), up to the fixed pencil sign. If T were zero, the actual second symbol would be zero, contradicting its proved nonzero scalar. As D5 is irreducible, T on Sym^2_0 A is injective.

## 2. The uncorrected source has zero trace

The ambient identity from Section1 gives Tr_A(a h zeta_a)=h Tr_A(a zeta_a)=0. Taking the parameter trace of q0 v_h=a h zeta_a therefore puts Tr_A(v_h) in K, whose restriction is zero in Cbar. Equivalently a fixed equivariant right inverse chooses a trace-free v_h before restriction, while every other choice changes its trace by K. Consequently

    Tr_A([v_h])=0 in Cbar.                         (3)

Here Tr_A denotes contraction of a quadratic parameter tensor with the inverse invariant metric on A. If a metric-orthonormal basis is used only to express that universal contraction, Tr_A Q is the sum of Q(e_i). This is representation algebra, not a choice of actual HM source coefficients.

## 3. The forced correction creates a nonzero trace

The actual raw-cubic theorem identifies

    b(a,h)=gamma S_h(a),    gamma nonzero,

where h -> S_h is a fixed G-isomorphism from D5 onto the trace-free self-adjoint endomorphisms of A. Using (2), contraction yields

    Tr_A([b(a,h)zeta_a])=gamma T(S_h).              (4)

For example, the basis expression is the sum of [(S_h e_i)zeta_(e_i)], exactly the symmetric tensor contraction defining T(S_h). The alternating part is already zero in Cbar by Section1. There is no assumption that individual ambient products a zeta_c are symmetric before taking this quotient.

Combining (3) and(4),

    Tr_A x(-,h)=-gamma T(S_h).                     (5)

Both gamma and the irreducible map T are nonzero. Thus (5) is an injective D5 family and in particular is NOT zero. The next source requires this trace, even though the preceding canonical v_h family admits a trace-free choice.

## 4. Limit of the deduction

The actual next operation is q0 w_h=a(v_h-b zeta_a), followed by [a w_h] modulo beta2. Equation(5) does not determine this operation and does not exclude cancellation among its four equivariant channels. It is not licensed to impose the old trace-free normal form on x or to discard b zeta_a.

The normalization gamma changes with the chosen invariant metric and representation identification. Only its nonzero status and the invariant contraction identity are asserted. No selected actual coefficient, actual matrix/rank evaluation, or model experiment is used.

## Reproduction

Run verify_fourth_corrected_source_trace.py. It verifies the universal three-dimensional symmetric-tensor contraction. The actual nonzero factors are supplied by the cited raw-cubic and second-symbol theorems, not by an instance calculation.
