> Publication note: Read [PUBLICATION.md](PUBLICATION.md) first. Original checks below are historical; original shell scripts now have `.historical.txt` suffixes. Use the public reproduction instructions, not private-path commands.

# Universal selector accumulation safety contract

Lean 4.33.0 mathematical proof extension, checked using the existing Mathlib/Vermilion environment with no installations. This directory is independent of prior verified sources; `ResidueBridge.lean` is an unchanged byte copy of the existing Laurent-list model.

## Result

For every finite list of terms `(e, c)` with five-integer exponent vectors and integer coefficients, if the sum of absolute values of **all input coefficients** is at most `2^63 - 1`, every prefix sum of coefficients selected by any chosen exponent lies in signed64 range `[-2^63, 2^63 - 1]`. The prefix quantifier includes the empty prefix and take lengths larger than the input list. Repeated exponents are allowed and add normally.

`absBudget_eq_sum` identifies the recursive budget with the ordinary mapped list sum. `selectSum_abs_le` proves the triangle-inequality bound. `take_budget_le` proves prefix monotonicity. `every_prefix_signed64` combines these facts into the signed64 contract.

`accumulate` is a mathematical integer left fold starting from an explicit accumulator. `accumulate_eq` proves this equals the initial value plus the existing model's selected sum. `accumulation_contract` specializes to initial zero and the all-minus-one exponent: every prefix accumulator lies in signed64 range, and the final accumulator is exactly `ResidueBridge.residue (ResidueBridge.interpret ts)`. The latter interprets finite Laurent lists by finitely supported functions, combining duplicate exponents.

## Checking and axioms

Run `./recheck.sh`. It checks model byte identity and freshly compiles both local Lean modules against the already installed environment. `compile.log` and `compile.exit` record the successful check. `source-sha256.txt` identifies sources and checking script. Public theorem axiom reports contain only `propext`, `Classical.choice`, and `Quot.sound`; no admitted theorem, `sorryAx`, or custom axiom is used.

## Exact limits

This proves a universal **sufficient mathematical safety contract**, not an executable i64 loop, Rust implementation, compiler, or newly generated VC. Linking a future loop requires proving its initialization, iteration/selection correspondence, and invariant preservation against its actual generated obligations. Exponent inputs are mathematical integers here; any machine representation bounds remain separate premises at the implementation boundary. This file does not import or reprove the accepted single-term generated selector bridge.

The budget is deliberately conservative: it can reject safe cancellation-heavy inputs and excludes a coefficient of `-2^63`, even though that coefficient alone is representable. The budget and absolute values are mathematical integers. Computing this precondition itself in i64 with ordinary `abs` or unchecked summation is **not justified**; in particular absolute value of minimum i64 overflows. No implementation of the precondition is provided. The contract is zero-initialized; a nonzero initial accumulator requires an additional bound.

No analytic residue theorem, full TW/HM bridge, arbitrary-precision executable, actual HM source/model matrix, product, rank, polynomial instance, point, jet, residual, or Massey evaluation is used or claimed. This is solely universal formal algebra and integer inequalities.

Independent audit was requested from the parent separately; this initial receipt does not claim that audit has completed.
