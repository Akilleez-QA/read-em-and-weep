# Degree-273 cancellation and the independent factor 48

## 1. The all-mask numerator is a regular section

Use the exact expression and legal-line partition from the preceding notes:

\[
f=\sum_{m_2,m_3,m_4}\rho_{2,m_2}\rho_{3,m_3}\rho_{4,m_4}
 c_{0,1,2m_2,3m_3,4m_4}.
\]

The first primary anchor is line-independent, so its weight sum is one. No
nonzero term in the remaining three-mask sum is dropped. The numerator
package's integer feature-moment identities give exactly this all-mask sum,
not a single-mask specialization.

Each selected weight clears that vertex's legal-line poles and adds one
factor of its primary denominator. The completed scalar primary allocation
is 13, so

\[
D=h_1^{13}h_2^{14}h_3^{14}h_4^{14}
\]

is sufficient. The only remaining first-open pole is the simple `v0` pole.
The frame calculation identifies `f` as a rational `F=O(-4)^external4` section
in every product chart. Therefore `v0 D f` is regular globally: this conclusion
uses the individually cleared summands and the completed pole certificate,
not homogeneous weight alone.

The multidegree of `v0` is `(1,1,1,1)` and that of each `h_j` is `(5,5,5,5)`.
Since `13+14+14+14=55`, the resulting line bundle is

\[
F\otimes O(1+5\cdot55,1+5\cdot55,1+5\cdot55,1+5\cdot55)
=O(272,272,272,272).
\]

On `Y_i=1`, `v0=1` and the section restricts to `A=Df`, precisely the pinned
scalar numerator. Its degree in every `x_i` is at most 272. Thus
`[x_i^273]A=0` as a polynomial identity over Q. No source expansion, zero
sample, modular lift, or scalar residue value is used in this deduction.

The leading-two-jet algorithm deliberately retains the conservative syntactic
bound 273 after additions cancel. Its outputs are therefore degrees 273 and
272, even though the first is mathematically zero. This regular-section
argument is the reason the first output may be discarded. It does not prove
that an arbitrary input with the same syntactic degree is regular.

Closedness and attribution to a particular deformation problem are needed
when identifying the residue with a geometric obstruction class. They are
not needed to deduce this polynomial degree bound for the exact expression
whose frame, pole, prefactor, and moment identities have been established.

## 2. What factor 48 means

Fix an eliminated axis `i`. Let `B_i=[x_i^272]A`, the degree-272 polynomial
emitted by the exact leading transformation. In the pinned concrete-tag
normalization, its output factor list explicitly contains

\[
B_i=\left(\prod_{j\ne i}x_j^{48}\right)R_i.
\]

Here `R_i` is a polynomial circuit over Q. The factor is the product of the
three remaining **coordinate** variables, not `(e1 e2 e3)^48`. The number 48
is obtained from this exact output factorization. It is not the primary pole
order, a topological normalization, or a guessed multiplicity. No claim is
made that it is the largest possible common factor.

The support proof is elementary induction. A coordinate leaf has its unit
exponent vector. For a product of polynomial symbols, coordinate lower and
upper bounds and total-degree bounds add, multiplied by the nonnegative
integer powers. For a sum, lower bounds take minima and upper bounds take
maxima. Cancellation can only shrink the actual support. Exact nonzero
rational scalar factors do not alter monomial support.

The checker verifies topological order, polynomial factors, positive integer
exponents, and reduced nonzero rational coefficients before applying the
induction. In particular, a symbolic denominator cannot hide behind an
apparently positive coordinate factor at the output. It verifies that each
of the three coordinate factors is explicitly present with power 48.

For all four pinned normalized axes this gives, in the surviving coordinates,

- coordinate lower bound 48 and upper bound 212;
- total-degree lower bound 353 and upper bound 449;
- after removing the three factors, coordinate upper bound `212-48=164` and
  total upper bound `449-3*48=305`.

These are conservative enclosures; they do not assert endpoint occurrence.
The exact-Q leading transformation and normalization are supplied by the
pinned jet package. This package independently checks their normalized
polynomial output structure and support, not the complete transformation
from the numerator on each invocation.

## 3. Downstream consequence and limits

The exposed coordinate factor must be removed before the secondary reverse
jet uses bound 164. Six retained reverse layers are then interpreted relative
to that bound; the removed factors must be restored in any original-degree
bookkeeping. A total homogeneous projection is a separate later operation.
No remaining variable may be set to one merely to obtain these bounds.

The historical `m2220` metadata in some compact pairs is not a universal
projector for the other scalar queries. Every subsequent evaluator must use
the actual query to select its reverse layer, role permutation, remaining
homogeneous degree, and coefficient window.

The factor-48 proof does not establish degree-273 cancellation. Conversely,
the regular-section proof does not establish factor 48. Neither evaluates a
quotient or proves a scalar coordinate zero. Those are separate computational
certificates with separate source and arithmetic checks.
