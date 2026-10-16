# RF-R independent arithmetic review

Disposition: narrow algebraic core accepted with one open context-isolation defect (RF-R-1). The advertised constructor/shared-execution contract is **not fully accepted**. No producer change was made. This review supplies generic-kernel evidence only; the physical caller gate remains closed separately.

Read all six producer files, including `producer-ready.json`, all executable code, tests, runner, README, and proof. The marker is `producer-ready-artificial-only`, with five hashed payload files and six producer files total. No SR/AC draft was needed. Wrote only `test_independent.py` and this report. No Git, posts, physical HM source, model input, source calls, source coefficients, physical jets, or fiber runs were used. The artificial variable named nu below has no physical binding.

## Open defect RF-R-1: constructor ignores receiving execution

`field.py:129-136`, `Execution.rational`, never checks the receiver or verifies polynomial arguments belong to it. If both arguments are polynomials from another single execution, `Rational` checks only those arguments against each other and succeeds using their execution. This differs from mixed-execution arithmetic and the other tested constructors, which reject foreign objects.

Minimal synthetic reproduction (also encoded as the independent expected-failure test):

```python
owner = Execution()
receiver = Execution(Limits(products=0))
p, q = owner.constant(2), owner.constant(3)
r = receiver.rational(p, q)  # succeeds; expected ValueError
# r.ex is owner; normalization products are charged to owner, not receiver.
```

Impact: a caller using its designated execution's factory can silently construct and operate under a foreign meter. The receiving zero-product cap is not applied. Inspection also shows a poisoned receiving execution is not consulted on this path when the polynomial owner is live. This does not merge different owners into an algebraic operation, corrupt Fraction results, or defeat a correctly shared single execution; it breaks the factory's context boundary and weakens integration assurance. Producer should check receiver health and argument ownership before constructing; reviewer did not implement a fix. The independent test expects rejection and is marked `expectedFailure` solely to preserve the known defect visibly. An unexpected success after a fix makes unittest fail and prompts review of that marker. A green runner exit with this expected failure is not unconditional approval.

## Accepted arithmetic and independent evidence

Static review confirms sparse four-variable polynomial construction merges exact duplicate terms and removes zero coefficients. Fraction-only constructor conversion rejects approximate scalar input; constant rational denominators are absorbed, nonconstant denominator leads normalized, and zero normalized to denominator one. Equality cross-multiplies rather than depending on unreduced structural forms. No multivariate gcd cancellation is claimed or implemented.

Lex division uses the largest sorted exponent tuple, componentwise leading-monomial divisibility, and continues after transferring an irreducible leading term to the remainder. Hand-derived tests check both `x^2+z = (x-z)(x+z)+(z^2+z)` and an initial remainder followed by a later divisible term. Laurent extraction removes the coordinatewise denominator monomial, divides by the entire residual denominator, and rejects any remainder before inspecting the requested coefficient, including distant positive and negative requests. The proof's UFD argument is valid: a denominator without a coordinate factor that divides a coordinate multiple of the numerator must divide the numerator.

The detector-like weighted fixture forms `2*A-3*B=D*Q` over all four variables with a coordinate monomial times a nonmonomial D as denominator. Each individual quotient rejects even an out-of-support request. One final division on the combined numerator yields three independently specified Laurent coefficients and a certified absent coefficient. Adding one to that numerator rejects in-support and distant requests. This specifically checks cancellation before extraction; it is not a source detector implementation.

Basis multiplication reduces overlapping y powers using each `x_i^3-x_i`. The proof's independent square classes follow from odd valuation at a selected coordinate prime, so the 16-component zero criterion is justified. An independent oracle starts from unreduced integer y exponents, then applies Euclidean division by two at evaluation; it checks 256 products at a nonsingular exact specialization. This is one independent test method, not 256 newly counted tests or a recount of the producer's basis checks.

The invariant derivation differentiates both rational coefficients and the moving y frame. Its generator values preserve the curve relation; distinct axes commute on generators and hence on the field. A separate eight-variable Laurent-monomial differentiator (allowing negative x and y powers) applies the chain rule before basis reduction. It checks mixed derivatives of an artificial reciprocal nu with two moving y factors and repeated third derivatives of `x_0^2*y_0`, at two exact specializations. These comparisons do not call kernel derivatives, products, curve construction, or equality to calculate expected values. Evaluation converts rational coefficients by independent Fraction arithmetic. Such finite-specialization tests are regression evidence, not symbolic identity proofs; the source/proof review supplies the algebraic reasoning. Additional tests check Leibniz, commuting mixed applications, and the closed quotient-rule formula for a nonmonomial rational denominator.

Single-basis inverses accept rational coefficients with nonconstant numerators and denominators, including masks 0, 1, 5, 10, 15; multiplication by the inverse returns one. Zero, a two-component sum including scalar plus y, and non-rational-x extraction reject. These are denominator structural types only, with no claims about any actual H, x, nu, or other physical binding. General sums may be invertible mathematically; the deliberately partial reciprocal API correctly refuses them.

Frozen polynomial/rational/element/limit fields, immutable tuples/Fractions, and read-only snapshot counters are checked. Within the same execution, repeated work on preexisting objects accumulates product charges; exhaustion poisons polynomial, rational, and element zero/equality, empty jets, construction, and inverse operations. Additional arithmetic tests exceed coefficient-denominator bit height, exponent bit height, and derivative product caps after valid construction. Tiny step/storage caps are checked. Public mutable Execution internals or deliberate manual meter tampering are outside this cooperative caller contract.

## Bounded verification and residual scope

Reproduce from repository root:

```sh
python -B research/codex-swarm/exact-curve-field/test_independent.py
```

The owned runner launches four children: producer normal, independent normal, producer `-O`, independent `-O`. Each child has 805306368-byte (768 MiB) RLIMIT_AS, 59-second RLIMIT_CPU, 60-second subprocess wall timeout, zero core-dump limit, and bytecode disabled. Final observed results:

| Suite | Normal | `-O` |
| --- | --- | --- |
| Producer (existing evidence, not independent new cases) | 13 passed | 13 passed |
| Independent (13 new methods) | 12 passed, 1 expected failure RF-R-1 | 12 passed, 1 expected failure RF-R-1 |

All four final children completed in about 0.10–0.13 seconds each, with runner exit 0. No `assert` statement supplies test validation, so optimization does not remove it. Earlier development used a deeper artificial reciprocal derivative fixture that correctly exhausted the step cap; the final fixture uses two mixed derivatives and a separate polynomial repeated-derivative case. No producer arithmetic defect was inferred from that conservative exhaustion.

Products, storage events, bit height, steps, and basis products are concrete arithmetic hooks. Storage events are cumulative allocation/update counts, not live RAM, bytes, or physical admission; process address-space limits are enforced separately. Lack of gcd reduction can cause rapid denominator growth and conservative cap exhaustion. This review does not establish performance on larger inputs, matrix semantics, unrestricted inverses, source support/cost bounds, a complete detector, or physical source readiness. Caller aggregate-budget discipline and a separate physical admission gate remain necessary. RF-R-1 remains open.

## Before/after SHA-256

The following hashes were measured before testing and after the final test edit/runs and are identical. All five payload hashes match the marker. The marker itself is also unchanged.

| Producer file | Before = after SHA-256 |
| --- | --- |
| README.md | `27e377280daffc39656bba3a3c6aaf2b2667e2d325947a813f9237b7ca4f6fd4` |
| field.py | `753e5acdb8d3df830ff08e6a0aaa7eb423979ebca13f7e3f311e0d244e89bd7f` |
| producer-ready.json | `0211b2efc38f1ac913e2288db980f21047eb740cb3475642969eb21b041a9e3a` |
| proof.md | `9aaf3ae3db640cd82959ff800ed8023f124ce93c276043959f470866c5fa23f0` |
| run_tests.py | `1954cef036157f5ae35378b2f4499784aa6527bd9d7357e0676e0696b7d06906` |
| test_field.py | `18b8d46be3ec614a9e70276f317eb58b54f4b08a14c67084e01ffb83d1e97537` |

Payload bundle before = after: `446dde1fcecbeb70b1a6f62fb31ef45c35a00bdf462886b396b09d843302aa37`, using the marker's sorted `<sha256>  <relative-name>\n` definition, excluding the marker itself.

Final independent test SHA-256: `585eca56246cc784c53bfff8b2ce08d14bc3d758e53fd8835784dffb3bbf94e3`. The report is not self-hashed.
