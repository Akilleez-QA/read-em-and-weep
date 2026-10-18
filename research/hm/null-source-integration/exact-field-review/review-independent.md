# RF01 independent review

Reviewed immutable commit: `42559cd29f71656893aa0b3c6b87fb1de203f9be` (PR89).

Reviewed `field.py` SHA256: `753e5acdb8d3df830ff08e6a0aaa7eb423979ebca13f7e3f311e0d244e89bd7f`.

## Verdict

The sparse algebra, sixteen-component square-root basis, moving invariant derivations, restricted reciprocals and certified Laurent extraction are accepted at the generic artificial-input scope reviewed. The advertised execution-ownership/fail-closed constructor contract is **not accepted yet**: `Execution.rational` has the concrete ownership defect below. No physical source data, polynomial, coefficient, source jet, catalog, owner fiber or model program was executed. Tests use only explicit artificial data.

## Required fix: rational factory can silently change executions

[Execution.rational, lines129–136](https://github.com/Akilleez-QA/read-em-and-weep/blob/42559cd29f71656893aa0b3c6b87fb1de203f9be/research/codex-swarm/exact-curve-field/field.py#L129-L136) converts non-Poly inputs through its receiver, but does not check the receiver or existing Poly inputs. If both supplied polynomials belong to a different common execution, `Rational(numerator,denominator)` accepts them and charges that other execution.

Consequently `requested.rational(foreign.constant(2),foreign.constant(3))` returns a rational owned by `foreign`, while the requested meter receives no work. After `requested` is poisoned by cap exhaustion, the same factory call still succeeds. This is an ordinary public constructor path, not mutation of private counters or model-specific behavior.

Required repair: call `self.check()` before inspecting or constructing inputs, and reject any supplied Poly whose `ex is not self`. Continue preserving the normal same-execution validation in `Rational`. The receiver must remain authoritative even when both arguments already have polynomial type.

`test_factory_regression.py` is a minimal standalone reproduction. Both contract tests fail at the reviewed commit, in normal Python and Python -O, with exit status1. The full independent suite includes the same two failures. These failures should become passing regression tests after repair; they are intentionally not marked as expected failures.

## Algebraic audit

- Sparse polynomial constructors merge equal exponent tuples over exact Fractions and remove exact zeros. Arithmetic respects nonnegative polynomial exponents. Lexicographic leading terms form a compatible well-order for single-divisor long division.
- The basis product uses XOR for remaining square roots and multiplies by each overlapping `x_i^3-x_i` once. The proof's square-class independence argument is valid: valuation at a selected prime `x_i` is odd in any nonempty product of the four curve factors. Componentwise equality/zero testing is therefore valid over the stated multiquadratic field.
- `V_i` differentiates rational coefficients by the quotient rule and adds the moving-basis term `(3*x_i^2-1)/2` when bit i is present. The additional term is essential and present. Both the curve relation and distinct-axis commutation are consistent with this derivation.
- The single-basis reciprocal `y^m/(c*product_(i in m)(x_i^3-x_i))` is correct. General sums are explicitly unsupported, not treated as zero or approximated. This is a partial reciprocal API for the field, rather than a complete field-inversion implementation.
- Laurent extraction factors the coordinate monomial `x^d` from the denominator and divides the numerator by the entire residual denominator. A nonzero remainder is rejected before coefficient lookup, even for far-away exponents. Since the residual has no coordinate factor, unique factorization justifies the converse Laurent criterion. The returned coefficient index is correctly shifted by `+d`.

## Accounting scope

Ordinary arithmetic shares object-identity execution meters; mixed-execution binary arithmetic is rejected. Checked product, storage-event, step and bit-height limits throw rather than returning a truncated object. Existing same-execution objects reject further checked operations after poisoning. The rational-factory defect is the identified exception to this claim and must be repaired.

Counters are algorithmic hooks, not hard byte or wall-time bounds. Sparse intermediates, rational denominator growth, long-division work and equality cross-products still require an independently admitted execution plan and external process limits. A caller must not create replacement meters to reset its aggregate allowance. This package contains no physical-use gate or source binding, as its README explicitly states.

## Independent verification

Producer tests: thirteen pass normally and thirteen pass under Python -O.

Independent suite: eight tests run in each mode; six pass and two fail solely on the factory-ownership defect. Passing controls cover:

1. All256 basis products against an independently expanded dictionary of overlap factors, with rational scale -2/5.
2. All256 choices of basis mask, axis and polynomial degree0..3 for `V_i²(x_i^k*y^mask)`, checked against independently expanded closed coefficients. This detects omitted moving-frame terms.
3. Single-component rational reciprocals, differentiated inverse identities, zero/unsupported reciprocals and refusal of y-bearing Laurent extraction.
4. Four-axis denominator cancellation, exact negative Laurent shifts, polynomial division reconstruction, nonzero remainder and out-of-support rejection.
5. Cross-execution polynomial, rational and field binary-arithmetic refusal.
6. Cap poisoning propagated to preexisting objects, constructors, equality, zero tests and empty jets on the same execution.

Tests and logs are self-contained beside the reviewed `field.py`. Producer replays and the optimized independent replay used 768 MiB address-space,45 CPU-second and45 wall-second limits; all completed in under a second. The minimal regression and initial independent run also completed in under a second. No test uses physical source inputs.

## Remaining integration obligations

- Close the receiver-ownership defect and rerun the two regression cases in both modes.
- Bind any actual scalar, curve frame, primitive or source circuit to this generic representation with a separate source-faithfulness argument.
- Preserve matrix multiplication order in any matrix wrapper; this kernel implements scalar arithmetic only and proves no matrix-level source identity.
- Ensure every required reciprocal satisfies the supported single-basis contract, or separately implement and review general inversion.
- Propagate Laurent-certification failure and resource exhaustion; neither means a missing coefficient is zero.
- Keep physical execution gated outside the kernel and supply an aggregate arithmetic/height/storage/process schedule before constructing source-specific objects.

[Implementation](https://github.com/Akilleez-QA/read-em-and-weep/blob/42559cd29f71656893aa0b3c6b87fb1de203f9be/research/codex-swarm/exact-curve-field/field.py) · [Producer proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/42559cd29f71656893aa0b3c6b87fb1de203f9be/research/codex-swarm/exact-curve-field/proof.md)

## Fix acceptance: 3ca9d546

The factory-ownership finding above is resolved at `3ca9d546b480491d14b8bb063ad13cc8fbf44f32`. Reviewed fixed `field.py` SHA256: `4dade295de59741ceb54eb4574c58ffc82c8a1a17063fd1c081656a8b2069b01`.

`Execution.rational` now calls `self.check()` first and rejects either supplied Poly whose execution is not the receiver, before any coercion. This closes both the live foreign-input path and the poisoned-receiver path without changing the mathematical kernel.

The unchanged [public minimal regression](https://github.com/Akilleez-QA/read-em-and-weep/blob/23bffa822566ff98b0e7ff4c6c63b266827b7aaa/research/hm/null-source-integration/exact-field-review/test_factory_regression.py), SHA256 `74c729f8eff58ecfcbb93221acc27e391c85fe62320c07d7470b94fa64a1f4c7`, now passes both tests normally and under Python -O. The expanded independent suite passes all nine tests in both modes. Added variants check foreign/own, own/foreign, foreign/scalar, scalar/foreign, foreign/default-denominator and foreign/foreign combinations are rejected without charging the receiving meter; valid same-execution/scalar combinations retain the receiver; zero denominators still fail; and a poisoned receiver rejects all tested combinations before argument conversion, including an approximate input.

The generic algebra and reviewed shared-execution ownership/fail-closed contract are therefore accepted at this fixed snapshot. The old finding and failing-snapshot results remain above as historical evidence. Physical execution authorization, source-faithful binding, ordered matrix integration, reciprocal coverage and aggregate process-resource planning remain separate. No physical source work was performed during fix verification.

[Verified fixed implementation](https://github.com/Akilleez-QA/read-em-and-weep/blob/3ca9d546b480491d14b8bb063ad13cc8fbf44f32/research/codex-swarm/exact-curve-field/field.py#L129-L139)
