module

public import Mathlib.LinearAlgebra.Isomorphisms

set_option autoImplicit false

@[expose] public section

namespace OAI.HorrocksMumford

variable {R C0 C1 T : Type*}
variable [Ring R] [AddCommGroup C0] [AddCommGroup C1] [AddCommGroup T]
variable [Module R C0] [Module R C1] [Module R T]

/-- The conditional source response, defined only on the differential's range. -/
noncomputable def sourceTraceResponse (d : C0 →ₗ[R] C1) (ell : C0 →ₗ[R] T)
    (h : LinearMap.ker d ≤ LinearMap.ker ell) : LinearMap.range d →ₗ[R] T :=
  ((LinearMap.ker d).liftQ ell h).comp d.quotKerEquivRange.symm.toLinearMap

/-- Evaluation of the quotient construction on an actual source. -/
theorem sourceTraceResponse_apply (d : C0 →ₗ[R] C1) (ell : C0 →ₗ[R] T)
    (h : LinearMap.ker d ≤ LinearMap.ker ell) (X : C0) :
    sourceTraceResponse d ell h (d.rangeRestrict X) = ell X := by
  change (LinearMap.ker d).liftQ ell h
    (d.quotKerEquivRange.symm ⟨d X, _⟩) = ell X
  rw [LinearMap.quotKerEquivRange_symm_apply_image]
  exact Submodule.liftQ_apply _ _ _

/-- The universal source-response property. Uniqueness is on `range d`, not `C1`. -/
theorem sourceTraceFactorization_iff (d : C0 →ₗ[R] C1) (ell : C0 →ₗ[R] T) :
    LinearMap.ker d ≤ LinearMap.ker ell ↔
      ∃! Lambda : LinearMap.range d →ₗ[R] T,
        ∀ X : C0, Lambda (d.rangeRestrict X) = ell X := by
  constructor
  · intro h
    refine ⟨sourceTraceResponse d ell h, sourceTraceResponse_apply d ell h, ?_⟩
    intro Lambda hLambda
    apply LinearMap.ext
    intro z
    rcases z.property with ⟨X, hX⟩
    have hz : d.rangeRestrict X = z := Subtype.ext hX
    rw [← hz, hLambda X, sourceTraceResponse_apply]
  · rintro ⟨Lambda, hLambda, _⟩ X hX
    change ell X = 0
    have hdX : d X = 0 := hX
    have hz : d.rangeRestrict X = d.rangeRestrict 0 :=
      Subtype.ext (by simpa using hdX)
    calc
      ell X = Lambda (d.rangeRestrict X) := (hLambda X).symm
      _ = Lambda (d.rangeRestrict 0) := congrArg Lambda hz
      _ = ell 0 := hLambda 0
      _ = 0 := map_zero ell

/-- Exactness at `C0` and vanishing on the preceding image give descent.
Both hypotheses are explicit algebraic obligations, not geometric assertions. -/
theorem sourceTrace_ker_le_of_exact {Cminus : Type*}
    [AddCommGroup Cminus] [Module R Cminus]
    (delta : Cminus →ₗ[R] C0) (d : C0 →ₗ[R] C1) (ell : C0 →ₗ[R] T)
    (hexact : LinearMap.range delta = LinearMap.ker d)
    (hzero : ell.comp delta = 0) : LinearMap.ker d ≤ LinearMap.ker ell := by
  intro X hX
  have hmem : X ∈ LinearMap.range delta := by
    rw [hexact]
    exact hX
  rcases hmem with ⟨Y, rfl⟩
  change (ell.comp delta) Y = 0
  exact congrArg (fun f : Cminus →ₗ[R] T => f Y) hzero

/-- The unique range factorization under explicit preceding-map exactness. -/
theorem sourceTraceFactorization_of_exact {Cminus : Type*}
    [AddCommGroup Cminus] [Module R Cminus]
    (delta : Cminus →ₗ[R] C0) (d : C0 →ₗ[R] C1) (ell : C0 →ₗ[R] T)
    (hexact : LinearMap.range delta = LinearMap.ker d)
    (hzero : ell.comp delta = 0) :
    ∃! Lambda : LinearMap.range d →ₗ[R] T,
      ∀ X : C0, Lambda (d.rangeRestrict X) = ell X := by
  exact (sourceTraceFactorization_iff d ell).mp
    (sourceTrace_ker_le_of_exact delta d ell hexact hzero)

/-- Closed changes of primitive do not change the response. -/
theorem sourceTrace_same_source (d : C0 →ₗ[R] C1) (ell : C0 →ₗ[R] T)
    (h : LinearMap.ker d ≤ LinearMap.ker ell) {X Y : C0}
    (hXY : d X = d Y) : ell X = ell Y := by
  have hz : d.rangeRestrict X = d.rangeRestrict Y := Subtype.ext hXY
  calc
    ell X = sourceTraceResponse d ell h (d.rangeRestrict X) :=
      (sourceTraceResponse_apply d ell h X).symm
    _ = sourceTraceResponse d ell h (d.rangeRestrict Y) :=
      congrArg (sourceTraceResponse d ell h) hz
    _ = ell Y := sourceTraceResponse_apply d ell h Y

/-- Abstract corrected response formula, with all lower terms held fixed.
No geometric interpretation of `Q`, `A`, or `y` is asserted here. -/
theorem correctedResponse_factorization {S : Type*} [SMul S T]
    (d : C0 →ₗ[R] C1) (ell : C0 →ₗ[R] T)
    (h : LinearMap.ker d ≤ LinearMap.ker ell) (Q y : T) (A : S) (X : C0) :
    Q + A • y - A • ell X =
      Q + A • y - A • sourceTraceResponse d ell h (d.rangeRestrict X) := by
  rw [sourceTraceResponse_apply]

/-- Formula independence for two primitives of the same corrected full source. -/
theorem correctedResponse_same_source {S : Type*} [SMul S T]
    (d : C0 →ₗ[R] C1) (ell : C0 →ₗ[R] T)
    (h : LinearMap.ker d ≤ LinearMap.ker ell) (Q y : T) (A : S)
    {X Y : C0} (hXY : d X = d Y) :
    Q + A • y - A • ell X = Q + A • y - A • ell Y := by
  rw [sourceTrace_same_source d ell h hXY]

end OAI.HorrocksMumford
