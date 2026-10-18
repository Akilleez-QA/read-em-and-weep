# AC01 cost and admission review

Reviewed baseline: [PR 89 at d37436ee72fcb8bc93ce9b1ef7ff4febeed0c789](https://github.com/Akilleez-QA/read-em-and-weep/tree/d37436ee72fcb8bc93ce9b1ef7ff4febeed0c789/research/codex-swarm/detector-admission).
Height-repair follow-up: e844d047045847f1406003883cc943ce48768d8a.

## Result

**Keep `BLOCKED_ROUTE`.** The frozen literal raw-source/request30 route has a defensible, deliberately enormous *conditional symbolic* operation/height/logical-storage majorant. It is not a native bit-work, live-byte, shared-ledger, or execution-admission certificate. I found no additional mathematical counterexample to that common symbolic majorant in this cost review.

Two replay/API defects require distinct treatment:

1. The baseline primitive `observed_bit_height_upper` omits exponent observations. **The e844d047 repair addresses this defect**, including its Rational composition. This does not turn the symbolic upper into physical admission.
2. **Open transitive-binding defect:** the standalone `whole_envelope.build()` authenticates SR producer files but does not validate the actual bytes named by SR's `local_dependencies`. Imported source can change without changing the emitted envelope. AC's direct pins close this for the compiler when using `actual_route_certificate()`, but omit `inserted-coefficients/interfaces.py`, leaving that dependency uncovered in the integrated path as well.

This review does not independently re-prove the geometric source/cover/comparison premises or the complete literal source denotation. Those are separate acceptance obligations. No physical source polynomial, jet, fiber assignment, or obstruction coefficient was evaluated.

## Finding 1: exponent observations, repaired in e844d047

[Baseline rf_bounds.py, lines 77–88](https://github.com/Akilleez-QA/read-em-and-weep/blob/d37436ee72fcb8bc93ce9b1ef7ff4febeed0c789/research/codex-swarm/detector-admission/rf_bounds.py#L77-L88) returns the coefficient-height bound as `observed_bit_height_upper`. [RF Poly construction](https://github.com/Akilleez-QA/read-em-and-weep/blob/d37436ee72fcb8bc93ce9b1ef7ff4febeed0c789/research/codex-swarm/exact-curve-field/field.py#L170-L187) also observes exponent integers.

For the invented one-term polynomial x0^1024 with coefficient 1, adding or multiplying by 1 produces a reported upper of 3 while RF observes 11; negation reports 2 while RF observes 11. The coefficient-height claims themselves are not contradicted. Nor does this refute the common whole-route B, which bounds degree separately and is much larger than its exponent bit lengths.

The repaired return value takes the maximum of 1, the output coefficient bound, both input coefficient bounds, and the bit lengths of both input degrees and the output degree. For nonnegative polynomial exponents this covers constructor exponent observations; the existing derivative height formula covers the exponent multiplier as well. `rf_rational_bound` propagates the corrected maxima through its primitive operations.

Additional controls: 120 tiny invented Poly cases, including zero outputs, high exponents and larger coefficients, plus six Rational-composition cases, pass normally and under `-O`. The repair is accepted for this narrowly identified defect.

## Finding 2: transitive imported source is not authenticated

[whole_envelope.py, lines 9–22](https://github.com/Akilleez-QA/read-em-and-weep/blob/d37436ee72fcb8bc93ce9b1ef7ff4febeed0c789/research/codex-swarm/detector-admission/whole_envelope.py#L9-L22) authenticates the SR marker and the files in its `files` dictionary. That includes the *text* of SR's source-pins.json, but the builder never hashes the actual dependencies named by that text. AST-node counting cannot substitute for their content hashes.

Two metadata-only mutations in isolated copies are both accepted with an unchanged JSON envelope:

- Change `interfaces.sorted_source` parity from `(-1)**sum(...)` to `(+1)**sum(...)`.
- Change the imported compiler's staircase iterator from `permutations(range(4))` to `permutations(range(1000000))`.

Neither changed source is imported or executed. The same AST-node counts cause the unchanged envelope to pass. The second mutation directly invalidates the claimed source-control premises; the first changes source denotation. The frozen reviewed files themselves match their expected hashes, so this is an authentication/replay defect, not evidence that either mutation exists in the reviewed commit.

[certifier.authenticate_inputs](https://github.com/Akilleez-QA/read-em-and-weep/blob/d37436ee72fcb8bc93ce9b1ef7ff4febeed0c789/research/codex-swarm/detector-admission/certifier.py#L57-L61) hashes the compiler directly, but AC's [direct source pins](https://github.com/Akilleez-QA/read-em-and-weep/blob/d37436ee72fcb8bc93ce9b1ef7ff4febeed0c789/research/codex-swarm/detector-admission/source-pins.json) omit the interfaces dependency. The authenticated SR pins already provide that expected digest.

Suggested correction: before AST counting or envelope generation, validate all local dependencies from the already-authenticated SR source-pins.json, including RF, compiler, lift schema and interfaces. Keep the immutable model/source/partition binding explicit as well. Add both mutation controls, requiring fail-closed rejection. The supplied standalone `check_transitive_binding.py` exits 1 while either mutation is accepted and 0 once both are rejected. It leaves original files unchanged.

## Mathematical cost audit

### Actual input and outer constants

I independently reconstructed all 1,973 catalog leaf rows using integer constants/exponent metadata only. Every row matches actual-input-bounds.json. The maximum coordinate degree, coefficient bit envelope and support-box cardinality are 6, 16 and 2,401 respectively.

The reasoning is valid: elementary e_k in four variables has coefficient L1 norm binom(4,k), and each coordinate degree is at most the stored exponent sum. Thus the L1 bound is a sum of absolute stored coefficients times products of those norms. An enclosing support box is an upper bound, not occupied support. Explicit zero leaves remain zero.

The first-hit multinomial constant bound and chained-binomial work bound are conservative. The outer construction's maximum total and slot count yield the stated 8,014-bit constant envelope; intermediate integer recurrence products are also covered. This is an input-constant envelope, not a claim that generated partition polynomials have those same small dimensions.

### RF primitive arithmetic

For canonical sparse inputs with m and n terms, a fixed output monomial has at most min(m,n) coefficient pairs. Summing products of rational coefficients therefore has the stated conservative numerator/denominator-height upper. Poly products visit all mn pairs; addition and derivative recurrences charge their constructors and coefficient work. Rational bounds include denominator-leading-coefficient normalization, rather than treating constant normalization as free.

An independent fixed-seed collection of 100 pairs of tiny invented rationals produced 2,700 comparisons of output term/degree/coefficient-height bounds and RF products/steps/storage-event bounds across addition, multiplication and differentiation. All comparisons passed in both execution modes. This is corroboration, not a proof by testing.

The 16-component field product's 256 basis pairs and each pair's at-most-four curve reductions fit well inside the deliberately generous compound-operation allowance. Moving-y derivative contributions are present. A general multi-component inverse remains unsupported; actual-route inverse admissibility is a separate source/function-field premise. No unit-cost general inverse is silently supplied by this envelope.

### Whole caller graph and universal majorant

The reviewed literal route calls the canonical raw source, complete SC Source/Lift, matrix helpers and fixed outer construction. Its recursion families are bounded: the small fixed composition recursion, the binary-power wrapper and lift stages 2 to 1 to 0. The other source/model/matrix paths are acyclic. Source matrix loops and constant-catalog loops are bounded independently of generated RF supports. Dynamic polynomial-term loops remain inside RF and are charged by RF recurrences.

The published call-depth and active-loop majorants are safely loose for this frozen graph. The AST total is 12,804, below the declared caller-position majorant. The activation-tree expression M overcounts all source-side positions and RF entry calls without enumerating owner assignments or relying on cache hits.

For B at least 2^20, the primitive recurrence values and counters fit below (B+2)^16. Iterating that majorant across the generous per-Element compound-operation bound is dominated by the published F. Iterating F for M positions supplies a finite preterminal degree, term-count and Fraction-height upper. The endpoint B then also dominates prior values and intermediate constructor work, permitting the stated cumulative RF-counter majorant.

This is a mathematical statement about the frozen literal program and its named input/domain premises. The mutation finding above means the current builder does not itself ensure that every imported program remains that frozen program.

### Exact terminal division

The weighted-degree argument correctly avoids assuming that intermediate coordinate degrees stay within the input coordinate box. For divisor coordinate degree D, weights ((D+1)^3,(D+1)^2,D+1,1) strictly order divisor monomials by lexicographic order. A division replacement cannot increase weighted degree, and leading monomials strictly decrease. Consequently work, quotient and remainder supports lie in a finite box and the proposed iteration upper is valid.

The recurrence h_next <= 2h + 2h_den + 5 conservatively covers leading-coefficient division, multiplication by a divisor coefficient and subtraction. Quotient/remainder updates are covered too. The instantiated K, T and H are finite symbolic expressions; none needs to be numerically materialized. Artificial degree-growth and lex-order controls corroborate this argument.

Exact remainder checking must precede coefficient lookup. A nonzero remainder is failure of the required Laurent/divisibility premise or implementation, never evidence that the requested coefficient is zero. The source's Laurent property and nonzero denominators remain imported mathematical premises.

### Logical storage and lifetimes

Retaining every route object until after terminal output existence is a valid conservative lifetime discipline: no output allocation can be hidden by an earlier input free. It covers evolving accumulators, per-assignment source/lift caches, previous values and terminal division buffers, while actual cache clearing can only reduce the retained set.

The stated S is a logical payload/reference-cell majorant. It is not measured or certified Python occupancy. Converting it to bytes requires an authenticated representation/workspace factor that covers Python/native objects, integer limbs, arithmetic scratch, headers, aliasing and the applicable storage metric. That factor is explicitly absent. The fictional packed-integer layout used by the synthetic certifier cannot supply it for RF's Fraction/dict/tuple implementation.

## Admission boundary

The package appropriately preserves these distinctions:

- RF `products` counts Fraction multiplication **and division**; it is not automatically a nonconstant polynomial-product count.
- RF `steps` is a logical hook, not a complete CPU-time or native bit-operation bound.
- `storage_events` is construction/update activity, not live bytes.
- A finite formula or huge upper bound is not measured work, required work, a minimum resource requirement, or an algorithm-independent no-fit result.
- A sparse/streamed/otherwise different algorithm needs its own source-bound execution and cost certificate. This envelope does not establish optimality of request30 or cover a reset budget for each detector in the complete fallback family.

Before physical admission, the route still needs an independently accepted complete source/control binding, a resource-unit mapping, a valid representation/native-workspace byte proof, and an authoritative current shared state including spent work, all reservations, live allocations and aliases, retained outputs, and the joint event/lifetime schedule. Explicit release authority remains separate. Unknown quantities must remain unknown, never zero. Historical statements or caller-supplied fictional replays cannot authenticate current all-worker state.

The evidence artifact limits its absence claim to the searched publication scope. I did not convert that scope into a universal or current-state absence claim, nor infer authority from the existence of a producer marker.

## Reproduction artifacts

- `test_cost_review.py`: nine independent baseline controls; source text/metadata and tiny artificial RF arithmetic only. Nine pass normally and under `-O`. Known-defect controls pass by demonstrating the baseline defects.
- `check_transitive_binding.py`: minimal portable fail-closed regression control. Both mutations are accepted at the baseline; its expected defect-detection exit is 1.
- `test_height_repair.py`: two test methods containing 120 Poly cases and six Rational-composition cases; both pass normally and under `-O` against e844d047.
- Corresponding logs contain only control outcomes and generic mathematical data.

No external post, physical arithmetic, aggregate-state change or execution release is part of this review.
