import KoszulCombined
namespace KoszulAudit
open KoszulSlots KoszulCombined
private def dim (r : Nat) (p q : Int) : Nat :=
  if r = 1 ∧ q = 2 then
    if p = -2 then 90 else if p = -1 then 100 else if p = 0 then 10 else 0
  else 0
private def rank (r : Nat) (p q : Int) : Nat :=
  if r = 1 ∧ q = 2 then
    if p = -2 then 90 else if p = -1 then 10 else 0
  else 0

def consistentPages : PageRankData where
  dim := dim
  rank := rank
  outside := by
    intros r p q h
    simp only [dim]
    simp only [Supported] at h
    repeat' first | split | omega
    all_goals simp_all <;> omega
  first_bound := by
    intros r p q h
    simp only [dim]
    repeat' first | split | omega
    all_goals simp_all <;> omega
  rank_le_source := by
    intros r p q
    simp only [dim, rank]
    repeat' first | split | omega
    all_goals simp_all <;> omega
  rank_le_target := by
    intros r p q
    simp only [dim, rank]
    repeat' first | split | omega
    all_goals simp_all <;> omega

theorem consistentQuotients : QuotientIdentities consistentPages := by
  intro r p hr hp
  simp only [consistentPages, dim, rank, PageRankData.incoming]
  repeat' first | split | omega
  all_goals simp_all <;> omega

/-- Simultaneous consistency of all inputs to the combined theorem. This is
synthetic page bookkeeping, not a concrete HM spectral sequence. -/
theorem combinedPremisesInhabited :
    ∃ D : PageRankData, QuotientIdentities D ∧
      D.dim 1 (-2) 3 = 0 ∧ D.dim 1 (-3) 4 = 0 ∧
      D.dim 1 0 2 = 10 ∧ D.dim 1 (-1) 2 = 100 ∧
      D.dim 1 (-3) 3 ≤ 50 ∧ D.dim 1 (-4) 4 ≤ 5 ∧
      (true = false → D.incoming 1 (-1) 2 = 0) ∧
      D.dim 4 0 2 = 0 ∧ D.dim 4 (-1) 2 = 0 := by
  refine ⟨consistentPages, consistentQuotients, ?_⟩
  decide
#print axioms combinedPremisesInhabited
end KoszulAudit
