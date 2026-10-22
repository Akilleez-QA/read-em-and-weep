# The actual next division requires complementary middle transport

## Precise strengthening

Retain the actual monad, the nonzero direction a and source h, and the
Cartan coefficient projection pi onto P inside the positive two-form sector.
Let T be a proposed degree-zero middle operator of twist four. Suppose one
and the same symbol S gives all three projected arrow actions

    pi(T A)=S Abar,   pi(T B)=0,   pi(T C)=S p_C.       (1)

Then no choice of the FOUR source blocks on U plus A can make T part of an
actual primitive satisfying

    dC_h=a h Z_a-q V_h.

The nonzero scalar k relating Z_a to the natural Atiyah cochain can be
absorbed uniformly into T and the source blocks; it does not affect the
contradiction. No independent channel scalar is normalized away.

This excludes more than the earlier A-annihilating principal family: S in
(1) need not annihilate Abar, and every source block is allowed. It excludes
all canonical Cartan-only lifts, including sums with arbitrary polynomial
coefficient degrees, because they satisfy (1).

It does NOT show that every successful middle operator must mix different
exterior-form sectors. The spin summand already present inside the VV sector
is another possible source of the missing Cartan output. The forced conclusion
is exactly that at least one equality in (1) must fail for the full actual
middle operator. Spin-VV-to-Cartan-VV and mixed-form-to-Cartan-VV blocks are
both possible mechanisms, and their contributions may coexist.

## Proof retaining all source blocks

Use the actual twelve-point ramification argument and tangent planes from
ACTUAL-RAMIFICATION-FORCES-A-NONTRIVIAL-PRINCIPAL-U-SOURCE-CORRECTION.md.
For each nonzero a,h, it supplies at least six ramification pairs with
 a(w)h(v) nonzero. At any variable pair of that locus, let lambda be the
quotient functional P/Hminus, so

    lambda Abar=0,   lambda p_C=0,
    im Abar=Lplus subset Hminus=im p_C,
    Lplus is not Lminus.

Write the four source blocks as P_UU, P_AU (U to A), P_UA (A to U), P_AA.
The two left-arrow principal balances on q=0, using (1), are

    a_m S Abar = a_m Abar P_UU + c_m p_C P_AU,
    c_m S p_C = a_m Abar P_UA + c_m p_C P_AA
                     +c_m a h (delta_(D_a)C)_(VV).    (2)

The b_m terms have zero Cartan VV projection. This is a projection of the
FULL monad equation, not a declaration that its other coefficients vanish.
The natural negative Atiyah deformation has zero U-source column, which
is why the first line has no target term.

Applying lambda to the first line of (2) gives lambda S Abar=0, since a_m is
nonzero. Pick an abstract input z with p_C(w,z) in Lplus but not Lminus;
such inputs exist by the ramification geometry. Then lambda S p_C(w,z)=0.
Applying lambda to the second line gives instead

    lambda S p_C(w,z)=2a(w)^2 h(v) z(w),              (3)

which is nonzero. This contradiction proves the result with ALL source
blocks retained. The exact factor two and coefficient convention are those
of the pinned Clebsch/Hamiltonian identity; any common nonzero normalization
would give the same contradiction.

## The exact necessary interface value

Do not rescale the actual primitive in this paragraph: Z_a=k e_a with the
fixed nonzero k. For any chosen comparison symbol S define

    E_A=pi(T A)-S Abar,
    E_B=pi(T B),
    E_C=pi(T C)-S p_C.

At the same ramification pair, take source inputs with p_C(w,z)=Abar(v,u),
using the actual marked channel maps. Applying lambda to the full U balance
and then subtracting it from the c balance gives the exact identity

    lambda(E_C(z)-E_A(u)-(b_m/a_m)E_B(u))
            =2k a(w)^2 h(v) z(w).                    (4)

The two terms involving S cancel because their inputs are literally equal.
All four source-block images are annihilated by lambda as before. Equation
(4) is independent of the arbitrary comparison symbol S and retains both
the monad ratio and the fixed Atiyah normalization. Its right side is nonzero
on the chosen open part of the twelve-point ramification orbit. It specifies
a necessary value of the full complementary combination; it does not compute
its individual blocks or any fourth Bockstein value.

## Why the omitted interface is genuinely available

The coefficient A is not confined to its Cartan projection Abar: its spin
projection is the nonzero Clifford tensor, with the fixed sign/scale of the
Cartan-spin splitting. A full middle operator may send that spin component
back into P. Thus the first equality in (1) is a real restriction, not a
formal identity for every operator on the middle bundle. Likewise the full
B and C arrows have mixed coefficients which a general middle operator may
send into Cartan VV. The positive off-diagonal tensor of
ACTUAL-POSITIVE-ATIYAH-DERIVATIVE-HAS-A-SURJECTIVE-P4-TENSOR.md is an actual
nonzero interface and must not be erased by replacing a full operator with
its Cartan compression.

The conclusion directs the ongoing construction toward the full middle
operator and coupled source equations. It neither supplies that operator
nor evaluates the divided class or fourth Bockstein.

## Reproduction

The companion verifier checks the exact two-column projected balance with
all four free source blocks, the common-image contradiction, and the fact
that a spin-to-Cartan correction can invalidate the first assumption in (1).
The actual ramification existence and nonvanishing inputs are the geometric
proof in the pinned predecessor, not conclusions of a numerical test.
