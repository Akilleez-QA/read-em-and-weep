# A q-multiplied lower middle has an exact higher-weight normal form

## Scope

This is a universal identity for a completed symmetric pair, retaining both
arrows of its middle-cochain differential. It does not prove that its remaining
C residual is q-divisible, solve a source system, or evaluate the fourth
Bockstein. It does not identify arbitrary higher completions with this chosen
completion. No instance of the actual monad is evaluated.

Let the determinant-valued alternating form be denoted by brackets. All its
physical line factors are retained; in a local frame the common inverse
determinant factor may be an arbitrary unit. Put

    S(x,y)(v) = x [y,v] + y [x,v].

Thus S is symmetric in x,y and is a symplectic, trace-free middle operator.
Work in the physical frame, with nonzero channel scales a_m,b_m and
kappa=b_m/a_m. Let g be a constant mixed coefficient and h a positive-linear
mixed coefficient. Their homogeneous balanced partners are Z_q for qg and
Z_h for h. Write

    L_q = qg - kappa Z_q,       L_h = h - kappa Z_h.

The hypothesis on these partners is the full U-arrow annihilation, not just
annihilation of its lowest homogeneous component. In terms of the unscaled
negative U pairing r=[g,B_U], s=[h,B_U], it is

    [g,alpha_U]=b_m r,          [h,alpha_U]=b_m s,
    [Z_q,alpha_U]=a_m q r,      [Z_h,alpha_U]=a_m s.

These identities hold componentwise for both U sources. For the homogeneous
completion construction they follow from Euler's identity, with the degree-two
factor 1/2 retained in Z_q. They are explicit hypotheses of the present lemma.

## Exact middle identity and twists

Define

    T = S(L_q,L_h),     B = S(g,L_h),
    T_high = -kappa S(Z_q,L_h).

Then, before restriction to the quadric or any quotient,

    T = q B + T_high.                                      (1)

The physical twists are those of a twist-four middle T and a twist-two middle
B; multiplication by the equation q of twist two gives precisely qB. All
coefficients are regular when the original pair and homogeneous partners are
regular. In particular (1) requires no inversion of f, g, or the vertex ideal.
The weight-zero part of T has been removed. Its retained C-arrow terms are

    (T_high C)_3 = -kappa (Z_q [h,C] + h [Z_q,C]),
    (T_high C)_5 = kappa^2 (Z_q [Z_h,C] + Z_h [Z_q,C]).       (2)

Formula (2) retains every mixed and WW contribution. It is not permission to
feed its first line into an interface requiring a no-WW input.

## The nonzero U quotient cannot be discarded

Although T alpha_U=0, its higher normal form need not annihilate U:

    B alpha_U = b_m L_h r,
    T_high alpha_U = -q b_m L_h r.                          (3)

A common determinant-frame unit multiplies both right sides. Thus the U
component is q-divisible but is generally nonzero. Dropping it is not a
cochain-equivalent replacement. In particular one must not subtract only the
C component of B alpha and assume that the subtraction is closed.

## Full differential and divided cohomology class

For the monad arrows alpha and beta, use the convention

    d(B) = (B alpha, -beta B).

This is the complete degree-one boundary of the degree-zero cochain whose
only nonzero block is B. Both source endpoint blocks of that degree-zero
cochain are zero. The two components satisfy

    beta(B alpha) + (-beta B)alpha = 0

identically. Therefore

    d(T_high) = d(T) - q d(B).                              (4)

If a previously specified full source cochain P and a fixed target F satisfy

    d(T,P) - F = q V,

then the SAME P and F satisfy

    d(T_high,P) - F = q (V-d(B)).                           (5)

No source end block, fixed target normalization, or physical channel scale
has been suppressed in this comparison. When the division exists, V and
V-d(B) define the same hypercohomology class. This follows from an actual
regular degree-zero boundary, not merely equality of a homogeneous C residue.
If division has not been proved, (4) is still an exact identity, but no divided
class is asserted. Global use of (5) requires global B, as supplied by a global
polynomial tensor construction; a purely local B proves only the local version.

## Reproducible certificate

`verify_q_lower_middle_higher_weight_normal_form.py` checks (1)--(4) over free
symbolic vectors, with an arbitrary inverse-determinant factor. It separately
checks all two U and three C columns, the full two-arrow boundary, and
symplecticity. Its abstract symplectic vector space is a certificate of the
universal bilinear identity, not a selected actual monad matrix or rank test.
