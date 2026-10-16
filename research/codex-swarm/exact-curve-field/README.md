# RF01 exact curve field

Executable generic Python standard-library arithmetic for
`Q(x_0,x_1,x_2,x_3)[y_0,y_1,y_2,y_3] / (y_i^2 - x_i^3 + x_i)`.
Indices are zero based. No physical program, coefficients, source JSON,
model, catalog route, or admission decision is provided or loaded.
All producer tests are artificial only.

`field.py` exposes `Execution`, immutable `Limits`, `Poly`, `Rational`, and
`Element`. Algebraic objects are frozen, contain tuples and immutable
`Fraction`s, and retain their execution meter by identity. There are no
external dependencies. Import by adding this directory to the caller's
module search path, then `from field import Execution, Limits`.

```python
from fractions import Fraction
from field import Execution, Limits

# Artificial demonstration only.
e = Execution(Limits(products=100000, storage_events=100000,
                     bit_height=256, steps=200000))
x, y = e.x(0), e.y(0)
f = (x + y) / x
jet = f.jet([0, 1, 0])
assert (y*y - x*x*x + x).is_zero()
coefficient = (x / x).laurent_coefficient((0, 0, 0, 0))
assert coefficient == Fraction(1)
counts = dict(e.counts)
```

## API and exactness

- `e.poly({(a,b,c,d): Fraction(...)})` creates a sparse polynomial with
  nonnegative exponents. Only `int` and `Fraction` coefficients are accepted;
  floats, booleans, strings, and implicit approximate conversions are refused.
- `e.rational(numerator, denominator=1)` accepts polynomials or exact scalars.
  Add, subtract, multiply, divide, `partial(i)`, `is_zero()`, and equality are
  exact. Equality cross-multiplies; numerator support determines exact zero.
  There is no general multivariate gcd simplification. Denominator growth can
  exhaust a cap; callers must propagate that failure.
- `e.element({mask: rational})` uses masks `0..15` for `y^mask`. `e.scalar`,
  `e.x(i)`, `e.y(i)` are constructors. Products reduce every overlapping bit
  by `x_i^3-x_i`. Arithmetic operators require operands of the same algebraic
  type and execution; use explicit constructors for constants.
- `V(i)` implements the invariant derivation on coefficients **and** the
  moving basis: `V_i(x_i)=y_i`, `V_i(y_i)=(3*x_i^2-1)/2`. `jet(axes)` applies
  each listed derivation successively. Distinct axes commute algebraically.
- `inverse()` on an element supports exactly one nonzero basis component,
  including any rational function coefficient. Zero raises `ZeroDivisionError`;
  multiple basis components raise `UnsupportedInverse`. No unsupported
  reciprocal is silently approximated. This can serve caller-supplied primitive
  H, legal x, or nu divisions only when they satisfy this structural contract;
  this package recognizes none of those source-specific objects.
- `rational_x()` refuses nonzero y components. `laurent_coefficient(e)` first
  extracts the denominator's coordinate monomial, runs exact single-divisor
  lexicographic multivariate polynomial long division against the remaining
  full denominator, and raises `NotLaurentPolynomial` on **any** remainder.
  Only after successful division does it look up the shifted exponent. Even
  out-of-support requested coefficients do not bypass the division.
- `Poly.divide(divisor)` returns `(quotient, remainder)`. No matrix API is
  implemented; no commutativity assumption is imposed on a caller's matrices.

## Shared fail-closed accounting

Create **one `Execution` for the entire caller execution** and use it for all
objects, jets, divisions, checks, and any matrices the caller builds. There is
no hidden per-object allowance or automatic meter reset. Cross-execution
arithmetic is refused. Independently creating another `Execution` deliberately
creates another budget and must not be used by a caller to evade its aggregate
limit.

`counts` is a read-only snapshot. `products` charges every rational-coefficient
multiply or divide, including polynomial multiplication, scaling, derivative
coefficient products, long-division leading-coefficient division, and rational
normalization. `basis_products` separately reports field basis pair products;
each is also charged a `steps` event and executes the instrumented polynomial
arithmetic. `storage_events` charges sparse insert/update attempts, retained
terms and object construction, plus moving-frame temporary entries. It is a
cumulative allocation-event hook, not live memory usage or a byte estimate.
`bit_height` records the maximum numerator/denominator bit length of exact
coefficients and polynomial exponents seen by constructors and arithmetic.
`steps` charges scalar operations, term processing, basis products, long-division
iterations, and jet applications. These hooks describe concrete generic work,
not a model support estimate or admission certificate.

Exceeding any configured cap raises `LimitExceeded` and permanently poisons the
execution. Subsequent operations, zero tests, equality, and construction using
its existing objects fail closed. No truncated result or inferred zero is
returned. Python itself does not provide a hard byte cap through these hooks;
the test runner adds OS limits. A source caller must separately enforce its
own process limits and physical-use gate **before** constructing or evaluating
source-specific field objects. Nothing in this module grants admission or
provides a model/catalog evaluation route.

## Artificial verification

Run `python -B research/codex-swarm/exact-curve-field/run_tests.py` from the
repository root. The runner confines its test child to 768 MiB address space,
59 CPU seconds, and 60 wall seconds, with core dumps and bytecode writes
disabled. The 13 producer tests use only artificial exact inputs. They do not
open source JSON or run any physical program. `proof.md` records identities,
algorithm reasoning, and verification scope. `producer-ready.json` records the
producer hashes; independent review files are reserved and absent.
