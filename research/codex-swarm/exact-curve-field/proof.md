# RF01 producer reasoning and artificial verification

This is generic executable arithmetic, not a proof-status schema, physical
admission, detector realization, or independent review. No physical objects,
source coefficients/jets/fibers/polynomials, physical program, or source JSON
were read or evaluated. Only newly created files in this directory were written.
Applicable instructions were read from `/home/akilleez/AGENTS.md`; no repository
or ancestor instruction file was present below that file on this task's path.
No Git commands were used.

## Algebraic invariants

A `Poly` stores a sorted tuple of distinct four-tuples with nonzero exact
Fraction coefficients; construction merges duplicate terms and deletes exact
zeros. Polynomial addition and convolution preserve this representation.
A `Rational` has a nonzero polynomial denominator. Constant denominators are
absorbed and zero has denominator one; no gcd simplification is assumed.
Cross-products decide rational equality exactly in Q[x].

An `Element` stores distinct masks in the free 16-element basis over Q(x).
For masks a,b, their product has mask a XOR b and coefficient multiplied by
`product_i (x_i^3-x_i)` over bits in a AND b. The square classes are independent:
for any nonempty subset, valuation at the prime x_i for a selected i is odd,
so its product is not a square in Q(x_0,x_1,x_2,x_3). Thus the multiquadratic
extension has the asserted basis and componentwise zero testing is sound.

For c*y^m, the coefficient derivative contributes
`partial_i(c)*y_i*y^m`; if bit i is set, the moving-basis derivative also
contributes `c*(3*x_i^2-1)/2*y^(m XOR bit_i)`. The quotient rule computes
partial_i(c). The relation is stable because
`V_i(y_i^2-x_i^3+x_i) = 2*y_i*(3*x_i^2-1)/2 - (3*x_i^2-1)*y_i = 0`.
Different axes act on disjoint generators, giving commuting derivations.

For one component c*y^m, the reciprocal is
`y^m / (c*product_{i in m}(x_i^3-x_i))`.
Multiplication therefore gives one exactly. General sums of y components are
explicitly refused by the reciprocal API.

For rational-x N/D, write D=x^d*D0 using coordinatewise minima of D's support.
Lexicographic single-divisor polynomial long division computes N=Q*D0+R,
where no remainder monomial is divisible by the leading monomial of D0.
At each iteration the leading monomial decreases in a well-order, so the
algorithm terminates (or a configured cap aborts). R=0 certifies the Laurent
polynomial x^(-d)*Q. Conversely, D0 is divisible by no coordinate x_i;
if N/D is Laurent, clearing its coordinate powers and unique factorization
force D0 to divide N in Q[x]. Thus a nonzero R warrants refusal, including
when the requested exponent appears absent. No series coefficient convention
or support-based zero inference is used.

## Producer checks

`test_field.py` contains 13 artificial tests covering all 256 basis products,
all 16 basis reciprocals, non-vacuous differentiation of both sides of the
curve relation on all four axes, Leibniz with moving-frame terms, distinct-axis
commutation, quotient derivatives, artificial nu reciprocal, ordered mixed
jets, exact multivariate denominator cancellation with negative Laurent
powers, and non-divisible quotients at in-support and far-away requests.
Negative tests cover zero division, unsupported y sums, non-rational-x
coefficient extraction, approximate inputs, invalid axes/exponents,
immutability, cross-execution refusal, shared product exhaustion across
separate objects, and tiny storage/step/coefficient/exponent bit-height caps.
Poisoned executions reject subsequent operations on preexisting objects.

The bounded runner passed all 13 tests. This is producer evidence only;
`test_independent.py` and `review-independent.md` are reserved and were not
created or edited. Matrices are not implemented, so no noncommuting matrix
claim is made. No actual source model is required or tested. Physical use
remains gated by the integrating source caller, outside this package.
