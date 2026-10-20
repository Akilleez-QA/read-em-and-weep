import ResidueBridge
import Mathlib.Tactic

/-! Universal unbounded-integer accumulation contract. No executable loop is asserted. -/
namespace SelectorAccumulationBound
open ResidueBridge

/-- Absolute input budget, computed in mathematical integers, not i64. -/
def absBudget : List (Term ℤ) → ℤ
  | [] => 0
  | t :: ts => |t.2| + absBudget ts

theorem absBudget_eq_sum (ts : List (Term ℤ)) :
    absBudget ts = (ts.map (fun t => |t.2|)).sum := by
  induction ts with
  | nil => rfl
  | cons t ts ih => simp [absBudget, ih]

def i64Max : ℤ := 2^63 - 1

def signed64 (x : ℤ) : Prop := -(2^63) ≤ x ∧ x ≤ 2^63 - 1

theorem absBudget_nonneg (ts : List (Term ℤ)) : 0 ≤ absBudget ts := by
  induction ts with
  | nil => simp [absBudget]
  | cons t ts ih => exact add_nonneg (abs_nonneg _) ih

theorem selectSum_abs_le (target : Exponent) (ts : List (Term ℤ)) :
    |selectSum target ts| ≤ absBudget ts := by
  induction ts with
  | nil => simp [selectSum, absBudget]
  | cons t ts ih =>
    rcases t with ⟨e,c⟩
    simp only [selectSum, absBudget]
    by_cases h : e = target
    · simp only [if_pos h]
      exact (abs_add_le _ _).trans (add_le_add (le_refl |c|) ih)
    · simp only [if_neg h, zero_add]
      exact ih.trans (le_add_of_nonneg_left (abs_nonneg c))

theorem take_budget_le (ts : List (Term ℤ)) (n : ℕ) :
    absBudget (ts.take n) ≤ absBudget ts := by
  induction ts generalizing n with
  | nil => simp [absBudget]
  | cons t ts ih =>
    cases n with
    | zero => simpa [absBudget] using absBudget_nonneg (t :: ts)
    | succ n => simpa [absBudget] using add_le_add_left (ih n) |t.2|

/-- Every list prefix is safe, including empty and overlong takes. -/
theorem every_prefix_signed64 (target : Exponent) (ts : List (Term ℤ))
    (h : absBudget ts ≤ i64Max) (n : ℕ) :
    signed64 (selectSum target (ts.take n)) := by
  have hb := (selectSum_abs_le target (ts.take n)).trans ((take_budget_le ts n).trans h)
  have bounds := abs_le.mp hb
  dsimp [signed64, i64Max] at *
  constructor <;> omega

/-- Final selected sum agrees with Laurent residue and obeys the same bound. -/
theorem residue_contract (ts : List (Term ℤ)) (h : absBudget ts ≤ i64Max) :
    selectSum residueExponent ts = residue (interpret ts) ∧
    signed64 (residue (interpret ts)) := by
  constructor
  · exact (residue_interpret ts).symm
  · rw [residue_interpret]
    simpa using every_prefix_signed64 residueExponent ts h ts.length

/-- Left-to-right mathematical accumulator, matching a future loop invariant. -/
def accumulate (target : Exponent) (initial : ℤ) (ts : List (Term ℤ)) : ℤ :=
  ts.foldl (fun acc t => acc + if t.1 = target then t.2 else 0) initial

theorem accumulate_eq (target : Exponent) (ts : List (Term ℤ)) (initial : ℤ) :
    accumulate target initial ts = initial + selectSum target ts := by
  induction ts generalizing initial with
  | nil => simp [accumulate, selectSum]
  | cons t ts ih =>
    rcases t with ⟨e,c⟩
    simpa [accumulate, selectSum, add_assoc] using
      ih (initial + if e = target then c else 0)

/-- Universal safety-and-meaning contract for zero-initialized left folds. -/
theorem accumulation_contract (ts : List (Term ℤ)) (h : absBudget ts ≤ i64Max) :
    (∀ n : ℕ, signed64 (accumulate residueExponent 0 (ts.take n))) ∧
    accumulate residueExponent 0 ts = residue (interpret ts) := by
  simp only [accumulate_eq, zero_add]
  exact ⟨every_prefix_signed64 residueExponent ts h, (residue_interpret ts).symm⟩
end SelectorAccumulationBound

#print axioms SelectorAccumulationBound.every_prefix_signed64
#print axioms SelectorAccumulationBound.residue_contract
#print axioms SelectorAccumulationBound.accumulate_eq
#print axioms SelectorAccumulationBound.accumulation_contract
