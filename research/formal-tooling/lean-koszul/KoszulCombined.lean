import KoszulDimension
import KoszulSlots

/-!
# Combined conditional numerical Koszul theorem

This integrates the support/rank interface with finite kernel/image quotients.
It does not construct geometry, a spectral sequence, or linear maps. All such
realizations remain parameters. In particular `mu21` is represented only by its
differential rank; rank equal to target dimension is the numerical surjectivity
criterion, not a theorem about a constructed linear map.
-/
namespace KoszulCombined
open KoszulSlots KoszulDimension

/-- Rank-nullity plus the kernel/image quotient dimension identity, restricted
to the two slots needed. This is an explicit imported page identity, not a
conclusion about exhaustion or a bound on the total incoming dimension. -/
def QuotientIdentities (D : PageRankData) : Prop :=
  ∀ (r : Nat) (p : Int), 1 ≤ r → (p = -1 ∨ p = 0) →
    D.dim r p 2 = D.dim (r + 1) p 2 + D.incoming r p 2 + D.rank r p 2

/-- Recover both explicit PageStep identities from their combined balance. -/
def pageStep (D : PageRankData) (Q : QuotientIdentities D)
    (r : Nat) (p : Int) (hr : 1 ≤ r) (hp : p = -1 ∨ p = 0) :
    PageStep (D.dim r p 2) (D.dim (r + 1) p 2) where
  kernel := D.dim (r + 1) p 2 + D.incoming r p 2
  outgoing := D.rank r p 2
  incoming := D.incoming r p 2
  rank_nullity := Q r p hr hp
  quotient_dimension := rfl

/-- Absence of all higher right-slot arrows forces page-two stabilization. -/
theorem right_stable (D : PageRankData) (Q : QuotientIdentities D)
    (h23 : D.dim 1 (-2) 3 = 0) (h34 : D.dim 1 (-3) 4 = 0)
    (n : Nat) (hn : 2 ≤ n) : D.dim n 0 2 = D.dim 2 0 2 := by
  induction n with
  | zero => omega
  | succ n ih =>
      by_cases h : n = 1
      · subst n; rfl
      · have hn2 : 2 ≤ n := by omega
        have hb := Q n 0 (by omega) (Or.inr rfl)
        have hi := D.right_incoming_zero h23 h34 n hn2
        have ho := D.right_outgoing_zero n (by omega)
        have prev := ih hn2
        omega

/-- Support alone forces page-four stabilization of the left slot. -/
theorem left_stable (D : PageRankData) (Q : QuotientIdentities D)
    (n : Nat) (hn : 4 ≤ n) : D.dim n (-1) 2 = D.dim 4 (-1) 2 := by
  induction n with
  | zero => omega
  | succ n ih =>
      by_cases h : n = 3
      · subst n; rfl
      · have hn4 : 4 ≤ n := by omega
        have hb := Q n (-1) (by omega) (Or.inl rfl)
        have hi := D.late_incoming_zero (-1) n hn4
        have ho := D.left_outgoing_zero n (by omega)
        have prev := ih hn4
        omega

/-- Right-slot cokernel vanishes: the rank of d1, hence of the identified mu21,
is 10. The rank is derived, not assumed. -/
theorem mu21_rank_ten (D : PageRankData) (Q : QuotientIdentities D)
    (h23 : D.dim 1 (-2) 3 = 0) (h34 : D.dim 1 (-3) 4 = 0)
    (rightDim : D.dim 1 0 2 = 10)
    (N : Nat) (hN : 4 ≤ N) (rightZero : D.dim N 0 2 = 0) :
    D.rank 1 (-1) 2 = 10 := by
  have stable := right_stable D Q h23 h34 N (by omega)
  have hb := Q 1 0 (by omega) (Or.inr rfl)
  change D.dim 1 0 2 = D.dim 2 0 2 + D.incoming 1 0 2 + D.rank 1 0 2 at hb
  have ho := D.right_outgoing_zero 1 (by omega)
  have hin : D.incoming 1 0 2 = D.rank 1 (-1) 2 := by
    simp [PageRankData.incoming]
  omega

/-- Construct every premise of the standalone dimension theorem from the
support/rank data, page identities, first-page dimensions, and eventual zero
abutment. The only map identification needed is that mu32=0 kills the incoming
d1 rank at (-1,2). -/
def dimensionInputs {Map : Type} {mu32 zeroMap : Map}
    (D : PageRankData) (Q : QuotientIdentities D)
    (h23 : D.dim 1 (-2) 3 = 0) (h34 : D.dim 1 (-3) 4 = 0)
    (rightDim : D.dim 1 0 2 = 10) (middleDim : D.dim 1 (-1) 2 = 100)
    (source2 : D.dim 1 (-3) 3 ≤ 50) (source3 : D.dim 1 (-4) 4 ≤ 5)
    (koszulZero : mu32 = zeroMap → D.incoming 1 (-1) 2 = 0)
    (N : Nat) (hN : 4 ≤ N)
    (rightZero : D.dim N 0 2 = 0) (leftZero : D.dim N (-1) 2 = 0) :
    KoszulDimension.Inputs mu32 zeroMap where
  middleDim := D.dim 1 (-1) 2
  page2Dim := D.dim 2 (-1) 2
  page3Dim := D.dim 3 (-1) 2
  page4Dim := D.dim 4 (-1) 2
  d1 := pageStep D Q 1 (-1) (by omega) (Or.inl rfl)
  d2 := pageStep D Q 2 (-1) (by omega) (Or.inl rfl)
  d3 := pageStep D Q 3 (-1) (by omega) (Or.inl rfl)
  imported_middle_dimension := middleDim
  imported_mu21_rank := mu21_rank_ten D Q h23 h34 rightDim N hN rightZero
  imported_koszul_incoming_zero := koszulZero
  imported_no_outgoing_d2 := D.left_outgoing_zero 2 (by omega)
  imported_no_outgoing_d3 := D.left_outgoing_zero 3 (by omega)
  source2Dim := D.dim 1 (-3) 3
  source3Dim := D.dim 1 (-4) 4
  imported_source2_subquotient := source2
  imported_source3_subquotient := source3
  incoming2_le_source := by
    have hs := D.rank_le_source 2 (-3) 3
    have hb := D.first_bound 2 (-3) 3 (by omega)
    change D.incoming 2 (-1) 2 ≤ D.dim 1 (-3) 3
    simpa [PageRankData.incoming] using Nat.le_trans hs hb
  incoming3_le_source := by
    have hs := D.rank_le_source 3 (-4) 4
    have hb := D.first_bound 3 (-4) 4 (by omega)
    change D.incoming 3 (-1) 2 ≤ D.dim 1 (-4) 4
    simpa [PageRankData.incoming] using Nat.le_trans hs hb
  imported_stabilization_and_zero_abutment := by
    have h := left_stable D Q N hN
    omega

/-- Conditional integrated conclusion: numerical surjectivity rank 10 for mu21
and nonvanishing of mu32, with the 90-versus-55 contradiction supplied by the
proved dimension theorem. No actual geometric realization is asserted. -/
theorem rank_ten_and_mu32_ne_zero {Map : Type} {mu32 zeroMap : Map}
    (D : PageRankData) (Q : QuotientIdentities D)
    (h23 : D.dim 1 (-2) 3 = 0) (h34 : D.dim 1 (-3) 4 = 0)
    (rightDim : D.dim 1 0 2 = 10) (middleDim : D.dim 1 (-1) 2 = 100)
    (source2 : D.dim 1 (-3) 3 ≤ 50) (source3 : D.dim 1 (-4) 4 ≤ 5)
    (koszulZero : mu32 = zeroMap → D.incoming 1 (-1) 2 = 0)
    (N : Nat) (hN : 4 ≤ N)
    (rightZero : D.dim N 0 2 = 0) (leftZero : D.dim N (-1) 2 = 0) :
    D.rank 1 (-1) 2 = 10 ∧ mu32 ≠ zeroMap := by
  exact ⟨mu21_rank_ten D Q h23 h34 rightDim N hN rightZero,
    KoszulDimension.mu32_ne_zero (dimensionInputs D Q h23 h34 rightDim
      middleDim source2 source3 koszulZero N hN rightZero leftZero)⟩

end KoszulCombined

#print axioms KoszulCombined.right_stable
#print axioms KoszulCombined.left_stable
#print axioms KoszulCombined.mu21_rank_ten
#print axioms KoszulCombined.rank_ten_and_mu32_ne_zero
