import ResidueBridge
import residue.residue_term
import residue.missing_face_zero

/-! Bridge from the accepted generated selector VC to one formal Laurent term.
The Rust-to-SST/VC translation remains a trusted boundary. No list aggregation
or machine accumulation is claimed here. Imported proof twins are unchanged. -/
namespace SelectorLaurentBridge

 def exponent (e0 e1 e2 e3 e4 : Int) : ResidueBridge.Exponent :=
  fun i => if i = 0 then e0 else if i = 1 then e1 else if i = 2 then e2 else if i = 3 then e3 else e4

 abbrev guard (e0 e1 e2 e3 e4 : Int) : Prop :=
  ((((e0 = 0 - 1 ∧ e1 = 0 - 1) ∧ e2 = 0 - 1) ∧ e3 = 0 - 1) ∧ e4 = 0 - 1)

/-- The conjunction represented by the generated short-circuit SSA temporaries.
The comparisons retain the generated signed clipping operation. -/
 def machineGuard (e0 e1 e2 e3 e4 : Int) : Prop :=
  let m := Vermilion.sclip 64 (0 - 1)
  ((((e0 = m ∧ e1 = m) ∧ e2 = m) ∧ e3 = m) ∧ e4 = m)

/-- Returned Int expression of the lowered selector body, after substitution
of its short-circuit temporary propositions. This is not a Rust interpreter. -/
noncomputable def returned (e0 e1 e2 e3 e4 coefficient : Int) : Int :=
  Vermilion.iteP (machineGuard e0 e1 e2 e3 e4) coefficient 0

 theorem clipped_minus_one : Vermilion.sclip 64 (0 - 1) = -1 := by
  norm_num [Vermilion.sclip, Vermilion.iteP]

/-- Import and apply the actual accepted postcondition; all six bounded-input
premises are retained and every SSA assumption is discharged, not axiomatized. -/
theorem accepted_postcondition (e0 e1 e2 e3 e4 coefficient : Int)
    (h0 : Vermilion.inSignedRange 64 e0)
    (h1 : Vermilion.inSignedRange 64 e1)
    (h2 : Vermilion.inSignedRange 64 e2)
    (h3 : Vermilion.inSignedRange 64 e3)
    (h4 : Vermilion.inSignedRange 64 e4)
    (hc : Vermilion.inSignedRange 64 coefficient) :
    returned e0 e1 e2 e3 e4 coefficient =
      Vermilion.iteP (guard e0 e1 e2 e3 e4) coefficient 0 := by
  let m := Vermilion.sclip 64 (0 - 1)
  let p1 := e0 = m ∧ e1 = m
  let p2 := p1 ∧ e2 = m
  let p3 := p2 ∧ e3 = m
  let p4 := p3 ∧ e4 = m
  have accepted := residue.residue_term.ensures_5 e0 e1 e2 e3 e4 coefficient
    p1 p2 p3 p4 h0 h1 h2 h3 h4 hc
    (by norm_num [Vermilion.inSignedRange])
    (by intros; norm_num [Vermilion.inSignedRange])
    (by simp_all [p1, m]) (by simp_all [p1, m])
    (by intros; norm_num [Vermilion.inSignedRange])
    (by simp_all [p2, m, clipped_minus_one]) (by simp_all [p2, m, clipped_minus_one])
    (by intros; norm_num [Vermilion.inSignedRange])
    (by simp_all [p3, m, clipped_minus_one]) (by simp_all [p3, m, clipped_minus_one])
    (by intros; norm_num [Vermilion.inSignedRange])
    (by simp_all [p4, m, clipped_minus_one]) (by simp_all [p4, m, clipped_minus_one])
  simp only [returned, machineGuard, guard, p4, p3, p2, p1, m, Vermilion.iteP] at accepted ⊢
  convert accepted using 1 <;> congr 1

 theorem guard_iff_exponent (e0 e1 e2 e3 e4 : Int) :
    guard e0 e1 e2 e3 e4 ↔ exponent e0 e1 e2 e3 e4 = ResidueBridge.residueExponent := by
  rw [← ResidueBridge.residue_predicate]
  simp [guard, exponent, Fin.forall_fin_succ, and_assoc]

/-- The program's returned Int equals the all-minus-one coefficient of one term. -/
theorem returned_eq_single_coefficient (e0 e1 e2 e3 e4 coefficient : Int)
    (h0 : Vermilion.inSignedRange 64 e0)
    (h1 : Vermilion.inSignedRange 64 e1)
    (h2 : Vermilion.inSignedRange 64 e2)
    (h3 : Vermilion.inSignedRange 64 e3)
    (h4 : Vermilion.inSignedRange 64 e4)
    (hc : Vermilion.inSignedRange 64 coefficient) :
    returned e0 e1 e2 e3 e4 coefficient =
      (Finsupp.single (exponent e0 e1 e2 e3 e4) coefficient)
        ResidueBridge.residueExponent := by
  rw [accepted_postcondition e0 e1 e2 e3 e4 coefficient h0 h1 h2 h3 h4 hc]
  simp only [Vermilion.iteP, Finsupp.single_apply, guard_iff_exponent]

 theorem returned_eq_singleton_residue (e0 e1 e2 e3 e4 coefficient : Int)
    (h0 : Vermilion.inSignedRange 64 e0)
    (h1 : Vermilion.inSignedRange 64 e1)
    (h2 : Vermilion.inSignedRange 64 e2)
    (h3 : Vermilion.inSignedRange 64 e3)
    (h4 : Vermilion.inSignedRange 64 e4)
    (hc : Vermilion.inSignedRange 64 coefficient) :
    returned e0 e1 e2 e3 e4 coefficient =
      ResidueBridge.residue (ResidueBridge.interpret [(exponent e0 e1 e2 e3 e4, coefficient)]) := by
  simpa [ResidueBridge.residue, ResidueBridge.interpret] using
    returned_eq_single_coefficient e0 e1 e2 e3 e4 coefficient h0 h1 h2 h3 h4 hc

/-- Both the accepted first-coordinate face VC and the concrete Laurent model
vanish. The call-result range premise in that VC is proved from its branches. -/
theorem first_coordinate_face_zero (e0 e1 e2 e3 e4 coefficient : Int)
    (h0 : Vermilion.inSignedRange 64 e0)
    (h1 : Vermilion.inSignedRange 64 e1)
    (h2 : Vermilion.inSignedRange 64 e2)
    (h3 : Vermilion.inSignedRange 64 e3)
    (h4 : Vermilion.inSignedRange 64 e4)
    (hc : Vermilion.inSignedRange 64 coefficient)
    (hn : 0 ≤ e0) :
    returned e0 e1 e2 e3 e4 coefficient = 0 ∧
      ResidueBridge.residue (ResidueBridge.interpret
        [(exponent e0 e1 e2 e3 e4, coefficient)]) = 0 := by
  have hr : Vermilion.inSignedRange 64
      (Vermilion.iteP (guard e0 e1 e2 e3 e4) coefficient 0) := by
    unfold Vermilion.iteP
    split
    · exact hc
    · norm_num [Vermilion.inSignedRange]
  have hz := residue.missing_face_zero.ensures_1 e0 e1 e2 e3 e4 coefficient
    h0 h1 h2 h3 h4 hc hn (by simpa only [guard, Vermilion.iteP] using hr)
  constructor
  · rw [accepted_postcondition e0 e1 e2 e3 e4 coefficient h0 h1 h2 h3 h4 hc]
    simpa only [guard, Vermilion.iteP] using hz
  · apply ResidueBridge.residue_eq_zero_of_nonnegative_coordinate _ (0 : Fin 5)
    intro t ht
    simp only [List.mem_singleton] at ht
    subst t
    simpa [exponent] using hn

end SelectorLaurentBridge

#print axioms SelectorLaurentBridge.accepted_postcondition
#print axioms SelectorLaurentBridge.returned_eq_single_coefficient
#print axioms SelectorLaurentBridge.returned_eq_singleton_residue
#print SelectorLaurentBridge.accepted_postcondition

#print axioms SelectorLaurentBridge.first_coordinate_face_zero
