# Independent accumulation safety audit

Date: 2026-10-18. Verdict: **PASS for the universal mathematical accumulation contract under its stated budget premise.** This is not verification of an executable Rust/i64 aggregation loop.

## Independent rebuild

After the producer froze the sources, `audit/rebuild.sh` copied both Lean sources to a fresh temporary directory and independently compiled `ResidueBridge` and `AccumulationBound`, in that order, using the existing Lean **4.33.0**, commit `d8b18978322de05a8f3dba51ef03cf5461676c17`. The fresh directory was first on `LEAN_PATH`. No producer-built module was reused for either source. Prebuilt Mathlib and standard dependencies remain part of the existing environment.

The rebuild and independent checks exited **0**. See `audit/independent-rebuild.log`, `audit/independent-rebuild.exit`, `audit/AuditChecks.lean`, and `audit/rebuild.sh`. The script also checks that the copied sources are still identical to the frozen originals after compilation. `ResidueBridge.lean` is byte-identical to the model in the prior selector-to-Laurent bridge directory.

## Premises and proof content

- The list and its length are arbitrary. Terms have exponent type `Fin 5 → ℤ` and coefficient type `ℤ`; there is no concrete mathematical instance or numerical HM evaluation.
- The only safety hypothesis is `absBudget ts ≤ 2^63 - 1`. The recursive budget sums the absolute values of **all** coefficients, not only selected coefficients. `absBudget_eq_sum` proves equality with the ordinary mapped-list sum. This is a sufficient, intentionally conservative condition, not a necessary criterion for safe accumulation.
- `selectSum_abs_le` proves the triangle-inequality estimate by induction, including both selected and unselected branches. `take_budget_le` proves that each prefix budget is no greater than the full budget. Consequently `every_prefix_signed64` covers every natural-number take length, including zero and lengths beyond the list. It applies to any target exponent.
- `signed64` is exactly `-(2^63) ≤ x ∧ x ≤ 2^63 - 1`. The absolute budget actually establishes the stronger symmetric lower bound `-(2^63 - 1)`. Thus the signed-range asymmetry is respected, while the valid value `-2^63` is conservatively excluded by this premise. Independent Lean boundary checks establish both that `-2^63` is representable and that its singleton budget fails the premise; the positive maximum passes.
- `accumulate` uses `List.foldl` and exact mathematical addition, with the explicit step `acc + (if exponent = target then coefficient else 0)`. The independent check verifies its cons-step recursion by reflexivity. `accumulate_eq` connects that left-to-right fold to the recursively defined selected sum using associativity, for any initial mathematical integer.
- `accumulation_contract` specializes the initial value to **zero**, proves representability of every prefix accumulator, and identifies the final accumulator with the model residue. A nonzero initial value has no safety theorem here without an additional bound.
- The meaning link is the existing `residue_interpret` theorem: finitely supported coefficient functions combine repeated exponents by addition, and the formal residue extracts the all-minus-one exponent. It is an additive Laurent-list model, not an analytic or geometric residue construction.

No theorem assumes the desired prefix safety or final coefficient identity. No list length, coefficient sign, or duplicate-exponent restriction is silently required.

## Axioms and trust boundary

The independently rebuilt four exported accumulation theorems and checked supporting bound lemmas report only `propext`, `Classical.choice`, and `Quot.sound`. The model's reports are subsets of the same standard axioms. Neither checked source contains a `sorry`, `admit`, or custom `axiom` declaration, and no reported dependency includes `sorryAx`. This is an axiom-relative Lean check, not an axiom-free claim.

The theorem proves that the mathematical values at every modeled iteration boundary fit in signed64 under the premise. It does **not** provide an actual executable loop, generate or discharge that loop's VCs, establish compiler/lowering correctness, prove a machine representation invariant, or connect an iteration implementation to the already accepted single-term generated selector VC. In particular the exponent vectors here have no machine-range hypotheses. These implementation links remain future obligations.

The budget itself is computed in mathematical integers. An i64 implementation of `absBudget` is not justified: `abs(-2^63)` and the budget's own unchecked sum can overflow. An actual implementation must separately establish the budget safely. This audit rejects any claim that the result already verifies an arbitrary-length executable Rust residue evaluator.

No actual HM source/model/evaluation was accessed. No installation, external write, or Rust generation was performed. Only local proof compilation and audit files were produced.

## Exact source fingerprints

- `AccumulationBound.lean`: `58089d8f62351afd200362e136710bb2dcd3cc785b1f7e7bf27df976166c5745`
- `ResidueBridge.lean`: `f90f3b54a4e9f97d9109bdb67decb4ef9c881704c80d7b6cec5cf8ed52923846`

`audit/source-binding.json` additionally binds the checking scripts, independent checks/logs, prior model, compiler binary, toolchain declaration, and dependency manifest. The verdict applies to these exact proof source contents.
