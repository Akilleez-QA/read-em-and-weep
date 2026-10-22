# Actual ramification detects a nonzero mixed-form middle value

## Result

The complementary-middle conclusion can be sharpened on a distinguished
shared source input. For every nonzero a,h, any ACTUAL next-division primitive
must have a nonzero mixed-form-to-Cartan-VV contribution on at least six of
the twelve ramification pairs of the actual bicubic. Spin-VV-to-Cartan-VV
transport alone cannot supply this value.

This is a necessary local value of the full actual middle operator, not a
fourth Bockstein value and not a construction of the primitive. The earlier
common-symbol proof did not assert this stronger conclusion. The additional
input here is the Clifford kernel line at the null positive covector.

## 1. The marked kernel line removes the remaining VV spin input

At an arbitrary null positive covector v=r^2, the fixed Clifford operator
M(v) is a nonzero multiple of r tensor r-flat. Thus

    ker M(v)=C r.

The Cartan/spin decomposition of the actual a-channel is the fixed Clebsch
splitting V tensor U=Sym^3 U plus U. On v tensor r its spin part vanishes,
and its Cartan part is a nonzero multiple of r^3. Consequently, for a suitable
nonzero u in ker M(v), the FULL VV coefficient A(v,u) is the positive cubic
point. There is no omitted spin component. All common nonzero Clifford,
Cartan and volume factors are retained by using the actual A(v,u), rather
than resetting the cube coefficient to one.

This follows from the universal Clebsch projections, not from an actual
source specialization. The Clifford and Cartan identifications are the
ones in CARTAN-PRINCIPAL-SYMBOLS-REQUIRE-THE-FULL-SPIN-INTERFACE.md.

## 2. A source difference with zero full VV coefficient

Use the actual ramification pairs and functional lambda from
ACTUAL-RAMIFICATION-FORCES-A-NONTRIVIAL-PRINCIPAL-U-SOURCE-CORRECTION.md.
At ramification over the negative line,

    Lplus subset Hminus,   lambda Abar=lambda p_C=0.

The positive cubic point r^3 does NOT belong to Lminus. Indeed if it did,
the negative derivative of the bicubic pairing would vanish as well as the
positive derivative, contradicting smoothness. Therefore there is a unique
input z in the c-source with

    p_C(w,z)=A(v,u)_(VV),        z(w) != 0.           (1)

The c-channel VV coefficient is already Cartan, and the b-channel has no VV
coefficient. Hence the actual middle-bundle vector

    Y=C(z)-A(u)-(b_m/a_m)B(u)                        (2)

has ZERO FULL VV coefficient. Its remaining coefficients lie in the mixed
VW and WW sectors. This equality retains the physical source markings and
monad ratio. No homogeneous truncation is being identified with a full
normal lift.

## 3. The forced actual mixed-form value

Let T be the actual middle component of any global primitive C_h with

    dC_h=a h Z_a-q V_h,       Z_a=k e_a,

in the fixed differential convention, and retain all four source blocks.
At a ramification pair on q=0, apply lambda to the Cartan VV projection of
the full left-arrow equation. Every source-end term disappears: the
projected A and C images lie in ker lambda, and B has no VV component.
The U-column gives

    lambda pi(T A(u)+(b_m/a_m)T B(u))=0.

The c-column gives, with the natural coefficient derivative and its fixed
Hamiltonian normalization,

    lambda pi(T C(z))=2k a(w)^2 h(v) z(w).

Subtracting yields the exact necessary identity

    lambda pi(T Y)=2k a(w)^2 h(v) z(w).              (3)

There is no comparison symbol S in (3). By (2), its left side measures only
the mixed-form-input-to-Cartan-VV part of the FULL middle operator. A block
acting solely on VV inputs, including arbitrary spin/Cartan mixing there,
annihilates Y's VV input and cannot supply (3).

The actual ramification divisor is a reduced twelve-point orbit with both
projections injective on its support. The nonzero negative quadratic a
vanishes at at most two projected points, and the nonzero positive trace-free
h restricts to a degree-four form on the positive null conic, vanishing at
at most four. Thus the right side of (3) is nonzero at at least six pairs.
These are uniform orbit and degree statements; no actual point, coefficient,
matrix or rank is selected or evaluated.

In particular Y is nonzero at those pairs. This also follows directly from
the actual subbundle property of the monad's left arrow: a_m A+b_m B and c_m C
have no nontrivial source relation. Nothing requires dividing by a matrix
entry or by a function vanishing at the vertex.

## Scope for the continuing construction

Equation (3) is an exact target for the currently missing full middle
interface. A nonzero positive off-diagonal leg alone does not verify it.
The full fixed-duality operator, neighboring bidegrees and source corrections
must still be assembled and checked globally. The actual divided class and
fourth obstruction remain unresolved.

## Reproduction

The verifier checks the complete free-spinor Clifford kernel identity, the
Clebsch pure-cube product, and the exact two-column subtraction with the
monad ratio and k retained. The actual bicubic smoothness and orbit geometry
are pinned mathematical inputs, not consequences of a numerical test.
