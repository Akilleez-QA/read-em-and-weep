# Isolated shared-certificate arithmetic controls

## Result

42/42 invented-input controls pass, byte-identically in normal Python and `python -O`. Both `actual_id0` invocations refuse with exit code 2 before candidate reading or AST extraction. No patch was applied. No production module, program, physical source, model, owner, or jet was imported or executed. The only candidate file read was inert `field.py.txt`.

This is evidence about an extracted arithmetic closure, not production integration, physical-value computation, admission, or resource adequacy for ID0.

## Pins

Candidate text SHA-256: `0efb8eff9bacacc9cddad9f29a598479c2c6925cf6472e2733ce4d37e841cc1c`.

Extracted AST (ast.dump, include_attributes=False) SHA-256: `cfda96f5c5403152853f2ff0952371072e7cd12347fc0b8b20f7e35580ee21a3`.

Both pins are enforced before extracted code runs. Harness/artifact hashes are in SHA256SUMS.

## Static inspection and extraction changes

The original field candidate has only a module docstring, three imports from Python stdlib (dataclasses, fractions, types), ZERO tuple creation, an object seal, and function/class definitions at top level. Class creation evaluates dataclass decorators and field descriptors. No file, network, process, source/owner/model loaders or import-time physical computation appear there.

The extraction retains exact original AST function/method bodies for LimitExceeded, NotLaurentPolynomial, _integer, _exponent, _axis, Limits, _same, Poly, Rational, LaurentContext and LaurentCertificate. Execution keeps only its constructor, meter/properties and polynomial/rational constructors; unused methods element, scalar, x, y, curve are omitted. Element, UnsupportedInverse, original imports, and module docstring are omitted. ZERO and _LAURENT_SEAL assignments are retained.

Changes: class module identity is the harness; the namespace and classes are new objects, isolated from production; the seal is newly created in that namespace; Execution has fewer methods; the compiled filename is synthetic, while retained AST line/column positions remain those of the candidate. Stdlib dataclass, field, Fraction, and MappingProxyType are explicitly supplied instead of executing candidate import statements. The entire remaining global dependency closure is checked against an explicit allowlist. Builtins contain no import, open, eval, exec, filesystem, process, or network capability. The harness itself uses filesystem access only to read the pinned inert text; shell redirection writes evidence. This is a safety-scoped test, not a general sandbox against malicious Python or hostile test inputs.

For retained method bodies and supplied exact types, no arithmetic algorithm, class decorator, budget operation, identity check, seal check, or lifetime check was edited. Omitting unused field-facing methods does not change the exercised polynomial/rational call paths. This claim is limited to those paths; extraction does not establish full-module integration behavior.

## Invented controls

Use x on axis 0 and y on axis 1. All polynomial terms and coefficients are invented, with caps of 10,000 products, 20,000 storage events, 20,000 steps and 64-bit height (plus one specifically reduced step budget).

- r = ((3x²+5x+7)(x+1))/(x(x+1)). Certification retains exact rational/context/execution identities, divides the entire residual x+1, and stores quotient 3x²+5x+7 and shift (1,0,0,0).
- Laurent coefficients at x^-1, x^0, x^1, x^20 are 7,5,3,0.
- The 1:2:1 weighted terminal at those first three exponents is 7+2·5+3=20. The weighted request adds only three product-meter events (weight multiplies), rather than repeating division. Certification itself uses 15 products, 141 steps and 95 storage events on this toy.
- Equal-but-distinct rationals, same-label-but-distinct contexts, foreign execution contexts, unsealed construction, and mutable request lists are rejected. Frozen certificate/context writes are rejected. Frame labels remain caller declarations, not authentication.
- 1/(x+1) fails certification with nonzero remainder. A legacy read at unsupported exponent x^20 still fails, proving no support-based shortcut there.
- (x+y)/y under lex order yields quotient 1 and remainder x: division continues after an irreducible leading term is moved into remainder.
- Canonical zero certifies and returns coefficient zero.
- Exceeding products, storage, steps, or bit height permanently poisons the aggregate execution: old certificate reads, weighted reads, recertification, old polynomials, and new arithmetic fail.
- A naturally exhausted step budget during certification raises LimitExceeded and remains poisoned on recertification.

Tests use explicit runtime checks, not Python assert; optimized mode therefore exercises the same checks. Inputs are finite tuples; the only candidate unbounded-looking polynomial division loop is guarded on each iteration by the finite step meter. No adversarial custom coefficient or iterable objects are passed.

## Remaining gap

No evidence here establishes production importability, physical source validity, owner matching, source/model evaluation, jets, real terminal inputs, actual ID0 value, or physical admission. Those remain separate gates. The tested certificate retains exact in-process object identity and shared execution lifetime; it is not a durable certificate, cryptographic authentication, or an unforgeability boundary against arbitrary Python code with introspection access. Meter limits bound algorithmic hooks, not physical memory or wall-clock guarantees.

## Reproduction

python test_extracted_arithmetic.py invented-controls --candidate-path FIELD_CANDIDATE.txt

python -O test_extracted_arithmetic.py invented-controls --candidate-path FIELD_CANDIDATE.txt

python test_extracted_arithmetic.py actual_id0  # unconditional exit 2


This public copy uses the portability-only harness adaptation documented in PORTABILITY.md. REVIEW.md is the unchanged independent review of the frozen original; its old CLI commands describe that original, not this portable CLI.
