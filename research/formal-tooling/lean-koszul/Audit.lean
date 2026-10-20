import KoszulDimension
import KoszulSlots

/- Synthetic consistency witness for the bookkeeping assumptions.
This is not an HM geometric instance or an evaluated multiplication map. -/
namespace KoszulAudit
open KoszulDimension

def consistentInputs : Inputs true false where
  middleDim := 100
  page2Dim := 50
  page3Dim := 0
  page4Dim := 0
  d1 := ⟨90, 10, 40, by decide, by decide⟩
  d2 := ⟨50, 0, 50, by decide, by decide⟩
  d3 := ⟨0, 0, 0, by decide, by decide⟩
  imported_middle_dimension := rfl
  imported_mu21_rank := rfl
  imported_koszul_incoming_zero := by intro h; cases h
  imported_no_outgoing_d2 := rfl
  imported_no_outgoing_d3 := rfl
  source2Dim := 50
  source3Dim := 5
  imported_source2_subquotient := by decide
  imported_source3_subquotient := by decide
  incoming2_le_source := by decide
  incoming3_le_source := by decide
  imported_stabilization_and_zero_abutment := rfl

/-- All premises can hold simultaneously; the theorem is not proved from a
universally uninhabitable record. -/
theorem premises_inhabited : Nonempty (Inputs true false) :=
  ⟨consistentInputs⟩

#print axioms KoszulDimension.source_dimension_bound
#print axioms KoszulDimension.PageStep.no_outgoing_balance
#print axioms KoszulSlots.no_outgoing_right
#print axioms KoszulSlots.no_outgoing_left
#print axioms KoszulSlots.no_late_incoming
#print axioms KoszulSlots.PageRankData.rank_zero_outside_source
#print axioms KoszulSlots.PageRankData.rank_zero_outside_target
#print axioms KoszulSlots.PageRankData.right_outgoing_zero
#print axioms KoszulSlots.PageRankData.left_outgoing_zero
#print axioms KoszulSlots.PageRankData.late_incoming_zero
#print axioms KoszulDimension.PageStep.balance
#print axioms KoszulDimension.PageStep.nonincrease
#print axioms KoszulDimension.PageStep.no_outgoing_bound
#print axioms KoszulDimension.drop_budget_bound
#print axioms KoszulDimension.zero_terminal_bound
#print axioms KoszulDimension.ninety_leaves_thirty_five
#print axioms KoszulDimension.page_two_dimension_if_zero
#print axioms KoszulDimension.mu32_ne_zero
#print axioms premises_inhabited
end KoszulAudit
