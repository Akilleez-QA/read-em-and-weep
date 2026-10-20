import Std.Tactic

/-!
# Finite Koszul spectral-sequence slot arithmetic

Source: ../koszul-cohomology-multiplication/PROOF.md, Sections 2–4,
SHA256 f81d33eec195fa3251acf95d47750a9371188b232974faf9eb125c40de48b107
(6501 bytes), as bound by that directory's AUDIT.md on 2026-10-18.

This file proves integer bidegree/support arithmetic and consequences of an
explicit numerical interface. It does not construct a sheaf Koszul complex,
a spectral sequence, cohomology, convergence, or actual multiplication maps.
Every geometric/page/rank input is a field or a theorem hypothesis below.
No actual source/model matrices or Massey values are evaluated.
-/

namespace KoszulSlots

/-- The finite first-page rectangle, inherited by all subsequent pages. -/
def Supported (p q : Int) : Prop := -5 ≤ p ∧ p ≤ 0 ∧ 0 ≤ q ∧ q ≤ 4

/-- Cohomological differential bidegree `(r, 1-r)`. -/
def Arrow (r : Nat) (p q p' q' : Int) : Prop :=
  p' = p + (r : Int) ∧ q' = q - (r : Int) + 1

/-- Exact list of supported higher incoming sources for `(0,2)`. -/
theorem incoming_right_iff (r : Nat) (hr : 2 ≤ r) (p q : Int) :
    (Supported p q ∧ Arrow r p q 0 2) ↔
      (r = 2 ∧ p = -2 ∧ q = 3) ∨ (r = 3 ∧ p = -3 ∧ q = 4) := by
  unfold Supported Arrow
  omega

/-- Exact list of supported higher incoming sources for `(-1,2)`. -/
theorem incoming_left_iff (r : Nat) (hr : 2 ≤ r) (p q : Int) :
    (Supported p q ∧ Arrow r p q (-1) 2) ↔
      (r = 2 ∧ p = -3 ∧ q = 3) ∨ (r = 3 ∧ p = -4 ∧ q = 4) := by
  unfold Supported Arrow
  omega

/-- At the right edge there is no outgoing differential on any positive page. -/
theorem no_outgoing_right (r : Nat) (hr : 1 ≤ r) :
    ¬ Supported (0 + (r : Int)) (2 - (r : Int) + 1) := by
  unfold Supported
  omega

/-- At the adjacent slot there is no outgoing differential from page two onward. -/
theorem no_outgoing_left (r : Nat) (hr : 2 ≤ r) :
    ¬ Supported (-1 + (r : Int)) (2 - (r : Int) + 1) := by
  unfold Supported
  omega

/-- From page four onward every incoming source lies above row four. -/
theorem no_late_incoming (p : Int) (r : Nat) (hr : 4 ≤ r) :
    ¬ Supported (p - (r : Int)) (2 + (r : Int) - 1) := by
  unfold Supported
  omega

/-- Explicit abstract numerical data; these are assumptions, not a constructed
spectral sequence. `rank r p q` means the rank of the arrow *out of* `(p,q)`.
The first-page bound is assumed only for positive page numbers. -/
structure PageRankData where
  dim : Nat → Int → Int → Nat
  rank : Nat → Int → Int → Nat
  outside : ∀ (r : Nat) (p q : Int), ¬ Supported p q → dim r p q = 0
  first_bound : ∀ (r : Nat) (p q : Int), 1 ≤ r → dim r p q ≤ dim 1 p q
  rank_le_source : ∀ (r : Nat) (p q : Int), rank r p q ≤ dim r p q
  rank_le_target : ∀ (r : Nat) (p q : Int),
    rank r p q ≤ dim r (p + (r : Int)) (q - (r : Int) + 1)

namespace PageRankData

/-- Rank of the arrow entering the selected slot. -/
def incoming (D : PageRankData) (r : Nat) (p q : Int) : Nat :=
  D.rank r (p - (r : Int)) (q + (r : Int) - 1)

theorem rank_zero_outside_source (D : PageRankData) (r : Nat) (p q : Int)
    (h : ¬ Supported p q) : D.rank r p q = 0 := by
  have hs := D.rank_le_source r p q
  have hz := D.outside r p q h
  omega

theorem rank_zero_outside_target (D : PageRankData) (r : Nat) (p q : Int)
    (h : ¬ Supported (p + (r : Int)) (q - (r : Int) + 1)) :
    D.rank r p q = 0 := by
  have ht := D.rank_le_target r p q
  have hz := D.outside r (p + (r : Int)) (q - (r : Int) + 1) h
  omega

theorem right_outgoing_zero (D : PageRankData) (r : Nat) (hr : 1 ≤ r) :
    D.rank r 0 2 = 0 :=
  D.rank_zero_outside_target r 0 2 (no_outgoing_right r hr)

theorem left_outgoing_zero (D : PageRankData) (r : Nat) (hr : 2 ≤ r) :
    D.rank r (-1) 2 = 0 :=
  D.rank_zero_outside_target r (-1) 2 (no_outgoing_left r hr)

theorem late_incoming_zero (D : PageRankData) (p : Int) (r : Nat) (hr : 4 ≤ r) :
    D.incoming r p 2 = 0 :=
  D.rank_zero_outside_source r (p - (r : Int)) (2 + (r : Int) - 1)
    (no_late_incoming p r hr)

/-- The two imported first-page vanishings exclude all higher incoming ranks. -/
theorem right_incoming_zero (D : PageRankData)
    (h23 : D.dim 1 (-2) 3 = 0) (h34 : D.dim 1 (-3) 4 = 0)
    (r : Nat) (hr : 2 ≤ r) : D.incoming r 0 2 = 0 := by
  by_cases h2 : r = 2
  · subst r
    have hs := D.rank_le_source 2 (-2) 3
    have hb := D.first_bound 2 (-2) 3 (by omega)
    have hz : D.rank 2 (-2) 3 = 0 := by omega
    simpa [incoming] using hz
  · by_cases h3 : r = 3
    · subst r
      have hs := D.rank_le_source 3 (-3) 4
      have hb := D.first_bound 3 (-3) 4 (by omega)
      have hz : D.rank 3 (-3) 4 = 0 := by omega
      simpa [incoming] using hz
    · exact D.late_incoming_zero 0 r (by omega)

/-- Explicit first-page dimension hypotheses yield the two rank bounds. -/
theorem left_incoming_two_le (D : PageRankData)
    (h : D.dim 1 (-3) 3 ≤ 50) : D.incoming 2 (-1) 2 ≤ 50 := by
  have hs := D.rank_le_source 2 (-3) 3
  have hb := D.first_bound 2 (-3) 3 (by omega)
  have hh : D.rank 2 (-3) 3 ≤ 50 := by omega
  simpa [incoming] using hh

theorem left_incoming_three_le (D : PageRankData)
    (h : D.dim 1 (-4) 4 ≤ 5) : D.incoming 3 (-1) 2 ≤ 5 := by
  have hs := D.rank_le_source 3 (-4) 4
  have hb := D.first_bound 3 (-4) 4 (by omega)
  have hh : D.rank 3 (-4) 4 ≤ 5 := by omega
  simpa [incoming] using hh

end PageRankData
end KoszulSlots

#print axioms KoszulSlots.incoming_right_iff
#print axioms KoszulSlots.incoming_left_iff
#print axioms KoszulSlots.PageRankData.right_incoming_zero
#print axioms KoszulSlots.PageRankData.left_incoming_two_le
#print axioms KoszulSlots.PageRankData.left_incoming_three_le
