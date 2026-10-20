import AccumulationBound
open ResidueBridge SelectorAccumulationBound
#print axioms SelectorAccumulationBound.absBudget_nonneg
#print axioms SelectorAccumulationBound.selectSum_abs_le
#print axioms SelectorAccumulationBound.take_budget_le
#check SelectorAccumulationBound.accumulation_contract
-- Confirm exact asymmetric machine interval and deliberate conservative premise.
example : signed64 (-(2^63)) := by norm_num [signed64]
example : ¬ absBudget [(residueExponent, -(2^63))] ≤ i64Max := by
  norm_num [absBudget, i64Max]
example : absBudget [(residueExponent, 2^63 - 1)] ≤ i64Max := by
  norm_num [absBudget, i64Max]
-- Explicit left-fold recursion for the operation actually formalized.
example (target : Exponent) (a : ℤ) (t : Term ℤ) (ts : List (Term ℤ)) :
    accumulate target a (t :: ts) =
      accumulate target (a + if t.1 = target then t.2 else 0) ts := by
  rfl
-- Algebraic contract is independent of term-count and includes the empty prefix.
example (ts : List (Term ℤ)) : accumulate residueExponent 0 (ts.take 0) = 0 := by
  simp [accumulate]
