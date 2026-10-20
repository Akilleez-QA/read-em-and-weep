import Mathlib.Data.Finsupp.Basic

/-!
A sparse Laurent-sum interpretation for arbitrary coefficients.
This is an additive coefficient bridge only: no multiplication, bounded-integer
arithmetic, particular mathematical model, or analytic residue is asserted.
-/
namespace ResidueBridge

abbrev Exponent := Fin 5 → ℤ
abbrev Term (R : Type*) := Exponent × R
abbrev LaurentSum (R : Type*) [Zero R] := Exponent →₀ R

def residueExponent : Exponent := fun _ => -1

section
variable {R : Type*} [AddCommMonoid R]

/-- Each sparse-list entry contributes a singleton finitely supported function.
Repeated exponents add, and zero coefficients vanish in the interpretation. -/
noncomputable def interpret : List (Term R) → LaurentSum R
  | [] => 0
  | (e, c) :: ts => Finsupp.single e c + interpret ts

/-- Exact, unbounded algebraic summation of all entries selected by exponent. -/
def selectSum (target : Exponent) : List (Term R) → R
  | [] => 0
  | (e, c) :: ts => (if e = target then c else 0) + selectSum target ts

/-- Sparse-list selection is precisely coefficient extraction. -/
theorem coefficient_interpret (ts : List (Term R)) (target : Exponent) :
    interpret ts target = selectSum target ts := by
  induction ts with
  | nil => simp [interpret, selectSum]
  | cons t ts ih =>
    rcases t with ⟨e, c⟩
    simp [interpret, selectSum, Finsupp.single_apply, ih]

/-- Formal five-variable Laurent residue: coefficient at (-1,-1,-1,-1,-1). -/
noncomputable def residue (p : LaurentSum R) : R := p residueExponent

theorem residue_interpret (ts : List (Term R)) :
    residue (interpret ts) = selectSum residueExponent ts :=
  coefficient_interpret ts residueExponent

/-- The selector's coordinatewise predicate is exactly equality to the residue exponent. -/
theorem residue_predicate (e : Exponent) :
    (∀ i : Fin 5, e i = -1) ↔ e = residueExponent := by
  constructor
  · intro h
    funext i
    exact h i
  · intro h
    subst e
    intro i
    rfl

/-- Selection vanishes if no entry has the target exponent. -/
theorem selectSum_eq_zero (ts : List (Term R)) (target : Exponent)
    (h : ∀ t ∈ ts, t.1 ≠ target) : selectSum target ts = 0 := by
  induction ts with
  | nil => rfl
  | cons t ts ih =>
    rcases t with ⟨e, c⟩
    have he : e ≠ target := h (e, c) (by simp)
    have ht : ∀ t ∈ ts, t.1 ≠ target := fun t hm => h t (by simp [hm])
    simp [selectSum, he, ih ht]

/-- A nonnegative exponent in one chosen coordinate excludes the residue monomial. -/
theorem residue_eq_zero_of_nonnegative_coordinate
    (ts : List (Term R)) (i : Fin 5)
    (h : ∀ t ∈ ts, 0 ≤ t.1 i) : residue (interpret ts) = 0 := by
  rw [residue_interpret]
  apply selectSum_eq_zero
  intro t ht he
  have hi := h t ht
  rw [he] at hi
  change (0 : ℤ) ≤ -1 at hi
  omega

end
end ResidueBridge

#print axioms ResidueBridge.coefficient_interpret
#print axioms ResidueBridge.residue_interpret
#print axioms ResidueBridge.residue_predicate
#print axioms ResidueBridge.selectSum_eq_zero
#print axioms ResidueBridge.residue_eq_zero_of_nonnegative_coordinate
