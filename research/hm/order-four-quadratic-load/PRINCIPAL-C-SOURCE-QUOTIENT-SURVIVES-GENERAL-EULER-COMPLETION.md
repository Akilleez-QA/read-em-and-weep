# The principal c-source quotient survives general Euler completion

## Purpose and fixed scope

For a raw W-action middle family, the complete high c-source quotient is
still a necessary condition after allowing arbitrary Cartan-input
negative-quartic Euler corrections. The U kernel-spinor screen from a
Spin-input-only repair is not retained. This statement justifies the
C-only restart; it does not assert that a surviving family solves U or c.

Use the public foundation PR697 (715bb7c683988da6cf220f26629b92d3575a0287)
and the general reconstruction theorem PR714
(6ebdea2d92a2e15d67132f5fba58e56546805412). Keep the actual source marking,
nonzero physical theta and all nonzero monad/Atiyah scales. A common
nonzero scalar may be divided from an entire equation, not from only
one column. The target cochain is fixed throughout.

## 1. Why the high c quotient is unchanged

The marked c column has coefficient bidegrees

    C_VV:(0,1),       C_VW:(1,0).

For every negative-quartic six-space coefficient K, the full Euler
formula gives the exact identity

    (T4(K)C)_VV=K C_VV.                                  (1)

A mixed input cannot produce a VV output in this formula. The right
side of (1) has degree(0,5). The other Euler outputs have degrees(1,4)
and(2,3) in the VW and WW slots.

The raw W-action c-VV error, including its prescribed target, has degree
(2,3). Hence a general Euler correction has **zero direct contribution**
to this high VV component, even when K has Cartan input. The source
which cancels (1) has AA degree(0,4) and therefore also changes only the
low c-VV component. Its existence and the remaining low Cartan companion
are separate mandatory tests, as in PR714.

The source terms that can change high c-VV degree(2,3) are precisely

    A(u),   u of degree(1,3),
    C(v),   v of degree(2,2),
    q0 times a divided cochain of VV degree(0,3).          (2)

All other homogeneous source components have different VV degrees.
The forced source u=P_C produced during Euler completion is included
in (2); it is not treated as zero. Consequently the class of the raw
high error in the quotient by all three terms in (2) is invariant under
the completion. Necessity of this quotient does not assume that every
source term in (2) can be realized compatibly with the other columns.

## 2. The full positive-conic source test

On the universal positive conic, write

    v=(r0 squared,-r1 squared,-r0 r1),
    M(v)=r lambda_r,  r=(r0,r1)^t, lambda_r=(-r1,r0).

This is a polynomial parametrization, not a selected actual point.
The high c-VV spin coefficient s is binary degree four. Since C is
Cartan and q0 restricts to zero, a necessary condition for (2) is

    lambda_r s=0.

If it holds, regular-sequence cancellation gives s=r beta, with beta
binary degree three. There is a canonical regular quadratic source

    beta=(partial_r0 s0+partial_r1 s1)/5,
    u=(-partial_r1 beta,partial_r0 beta)^t/3,
    M(v)u=s.                                            (3)

No value of r is assigned, and no coordinate is inverted. Formula (3)
is a choice of source representative, not an additional equation on the
raw family. Every other quadratic source solving the same spin equation
has the form u+r ell1, with ell1 binary linear.

Let lambda_w be the fixed quotient of the cubic marking by
f(ell Sym²W), and put

    F=lambda_w Abar(v,r).

After subtracting A(u), the remaining Cartan scalar class is defined
modulo F: replacing u by u+r ell1 changes it by -F ell1. The entire
C(v) term in (2) is killed by lambda_w. Thus vanishing of this scalar
class modulo F is a necessary condition independent of the canonical
choice (3). All three quadratic c-source inputs must be retained.
The statement does not assert that principal vanishing solves the
later full U, low c, or mixed high c equations.

## 3. Filter inventory for the bounded C-only restart

Start with all raw coefficient coordinates free, without an initial
ramification seed. The permitted principal tests are exactly:

1. The complete positive-conic spin test for each of the three c inputs.
2. The complete scalar quotient modulo F for each input, with (3) used
   solely as a representative and its ambiguity retained modulo F.

Thus this proof needs no prior ramification-row calculation. Such rows
can only be used as an optimization after separately proving that they
annihilate the entire source images (2); they are not a substitute for
the complete tests above.

No U row, U kernel-spinor condition, M-right-divisibility assumption,
SC/SS-only source normalization, or preselected principal Euler factor
may be inherited. Full U reconstruction must instead be run afresh using
PR714. Low c-VV preservation and the full low Cartan companion must then
be tested, before interpreting the high scalar deficit.

For the scalar quotient computation use an explicit polynomial domain
and fixed lex order r0>r1>u>w. The divisor is independent of the H and D
coefficient parameters. Quotient-remainder reconstruction must be checked
for every input component; coefficient extraction commutes with this
fixed linear normal form. Recursive multivariate division is not a
substitute. No statement here relies on an old recursive remainder.

## Reproduction

Run `python verify_principal_c_euler_quotient_invariance.py`.
It verifies (1) with all six-space coefficients free and the complete
Cartan three-form marking, verifies (3) with all cubic coefficients free,
and checks the complete quadratic-source ambiguity and its exact
multiple-of-F effect. The bidegree separation and filter necessity are
proved above. The verifier imports only the public foundation helper.
No selected actual source coefficient, instance matrix/rank, numerical
fiber test, curve reduction, actual fourth value, or full-family exclusion
is performed or claimed.
