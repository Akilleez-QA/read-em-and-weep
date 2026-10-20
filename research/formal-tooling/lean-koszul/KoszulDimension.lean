import Lean.Elab.Tactic.Omega

/-!
# Finite-dimensional page bookkeeping for the Koszul argument

This file proves the natural-number dimension argument, not construction of
cohomology, vector spaces, a Koszul complex, or a spectral sequence. The equations
in `PageStep` are explicit imported finite-dimensional rank-nullity and quotient
identities. Their interpretation is:

* `before = kernel + outgoing`: rank-nullity for the outgoing differential;
* `kernel = after + incoming`: the next page is kernel modulo incoming image.

In particular the second identity imports the fact that the incoming image lies
in the outgoing kernel. Actual geometry and identifications of differentials are
not axioms declared here: they must be supplied as parameters to the final theorem.
-/
namespace KoszulDimension

/-- Dimension-level data for one homology/page transition. -/
structure PageStep (before after : Nat) where
  kernel : Nat
  outgoing : Nat
  incoming : Nat
  rank_nullity : before = kernel + outgoing
  quotient_dimension : kernel = after + incoming

namespace PageStep

/-- The dimension removed in a page transition is the sum of both image ranks. -/
theorem balance {before after : Nat} (s : PageStep before after) :
    before = after + s.incoming + s.outgoing := by
  have h₁ := s.rank_nullity
  have h₂ := s.quotient_dimension
  omega

/-- Every next-page term has dimension at most the preceding term. -/
theorem nonincrease {before after : Nat} (s : PageStep before after) :
    after ≤ before := by
  have h := s.balance
  omega

/-- With no outgoing arrow, only the incoming image can remove dimensions. -/
theorem no_outgoing_balance {before after : Nat} (s : PageStep before after)
    (h : s.outgoing = 0) : before = after + s.incoming := by
  have hb := s.balance
  omega

/-- A source dimension bounds the dimension loss when there is no outgoing map. -/
theorem no_outgoing_bound {before after source : Nat}
    (s : PageStep before after) (h : s.outgoing = 0)
    (image_le_source : s.incoming ≤ source) : before ≤ after + source := by
  have hb := s.no_outgoing_balance h
  omega

end PageStep

/-- An arbitrary finite succession of kernel/image quotients. Unlike DropBudget,
this allows outgoing maps, as needed when bounding incoming source slots. -/
inductive PageEvolution : Nat → Nat → Prop where
  | same (dimension : Nat) : PageEvolution dimension dimension
  | next {first middle last : Nat}
      (page : PageStep first middle) (tail : PageEvolution middle last) :
      PageEvolution first last

/-- Every later source page is dimension-bounded by its first page. -/
theorem source_dimension_bound {first last : Nat}
    (evolution : PageEvolution first last) : last ≤ first := by
  induction evolution with
  | same dimension => omega
  | next page tail ih =>
      have h := page.nonincrease
      omega

/-- A finite sequence of page transitions with no outgoing arrows. The budget is
an upper bound on the sum of available incoming source dimensions. -/
inductive DropBudget : Nat → Nat → Nat → Prop where
  | done (dimension : Nat) : DropBudget dimension dimension 0
  | step {before after terminal rest source : Nat}
      (page : PageStep before after)
      (no_outgoing : page.outgoing = 0)
      (image_le_source : page.incoming ≤ source)
      (tail : DropBudget after terminal rest) :
      DropBudget before terminal (source + rest)

/-- Telescoping finite exhaustion: initial dimension is bounded by the terminal
survivors plus the entire incoming budget. This is independent of any geometry. -/
theorem drop_budget_bound {initial terminal budget : Nat}
    (chain : DropBudget initial terminal budget) :
    initial ≤ terminal + budget := by
  induction chain with
  | done dimension => omega
  | step page no_outgoing image_le_source tail ih =>
      have h := page.no_outgoing_bound no_outgoing image_le_source
      omega

/-- A zero terminal term requires enough incoming dimension to exhaust the start. -/
theorem zero_terminal_bound {initial budget : Nat}
    (chain : DropBudget initial 0 budget) : initial ≤ budget := by
  have h := drop_budget_bound chain
  omega

/-- The page-four slot retains at least 35 dimensions if page two starts at 90
and pages two and three have only incoming source budgets 50 and 5. -/
theorem ninety_leaves_thirty_five {page3 page4 : Nat}
    (s2 : PageStep 90 page3) (s3 : PageStep page3 page4)
    (no_out2 : s2.outgoing = 0) (no_out3 : s3.outgoing = 0)
    (bound2 : s2.incoming ≤ 50) (bound3 : s3.incoming ≤ 5) :
    35 ≤ page4 := by
  have h2 := s2.no_outgoing_bound no_out2 bound2
  have h3 := s3.no_outgoing_bound no_out3 bound3
  omega

/-- Imported data for the slot (-1,2). Every field is a premise, not a claim
that Lean has constructed the geometric spectral sequence. `mu32` can be an
actual linear map in a richer development; `zeroMap` must then be its zero map.

The d1 rank 10 is the imported consequence of surjectivity of mu21. The incoming
rank vanishing implication imports the alternating-Koszul-map identification.
The source bounds import subquotient monotonicity between E1 and the relevant
page. The zero page-four term imports absence of later arrows plus zero abutment.
-/
structure Inputs {Map : Type} (mu32 zeroMap : Map) where
  middleDim : Nat
  page2Dim : Nat
  page3Dim : Nat
  page4Dim : Nat
  d1 : PageStep middleDim page2Dim
  d2 : PageStep page2Dim page3Dim
  d3 : PageStep page3Dim page4Dim
  imported_middle_dimension : middleDim = 5 * 20
  imported_mu21_rank : d1.outgoing = 10
  imported_koszul_incoming_zero : mu32 = zeroMap → d1.incoming = 0
  imported_no_outgoing_d2 : d2.outgoing = 0
  imported_no_outgoing_d3 : d3.outgoing = 0
  source2Dim : Nat
  source3Dim : Nat
  imported_source2_subquotient : source2Dim ≤ 10 * 5
  imported_source3_subquotient : source3Dim ≤ 5 * 1
  incoming2_le_source : d2.incoming ≤ source2Dim
  incoming3_le_source : d3.incoming ≤ source3Dim
  imported_stabilization_and_zero_abutment : page4Dim = 0

/-- Under the zero-map supposition, rank-nullity and quotient dimensions force
exactly 90 dimensions on page two. No subtraction on Nat is assumed. -/
theorem page_two_dimension_if_zero {Map : Type} {mu32 zeroMap : Map}
    (h : Inputs mu32 zeroMap) (hz : mu32 = zeroMap) : h.page2Dim = 90 := by
  have hb := h.d1.balance
  have hm := h.imported_middle_dimension
  have ho := h.imported_mu21_rank
  have hi := h.imported_koszul_incoming_zero hz
  omega

/-- The dimension budget yields nonvanishing of mu32, relative to the separately
listed imported cohomological, Koszul, and spectral-sequence premises. -/
theorem mu32_ne_zero {Map : Type} {mu32 zeroMap : Map}
    (h : Inputs mu32 zeroMap) : mu32 ≠ zeroMap := by
  intro hz
  have hp := page_two_dimension_if_zero h hz
  have b2 : h.d2.incoming ≤ 50 := by
    have hs := h.imported_source2_subquotient
    have hi := h.incoming2_le_source
    omega
  have b3 : h.d3.incoming ≤ 5 := by
    have hs := h.imported_source3_subquotient
    have hi := h.incoming3_le_source
    omega
  have chain : DropBudget h.page2Dim h.page4Dim (50 + (5 + 0)) :=
    .step h.d2 h.imported_no_outgoing_d2 b2
      (.step h.d3 h.imported_no_outgoing_d3 b3 (.done h.page4Dim))
  have budget := drop_budget_bound chain
  have terminal := h.imported_stabilization_and_zero_abutment
  omega

end KoszulDimension
