module

public import Mathlib.RingTheory.MvPolynomial.Homogeneous
public import Mathlib.LinearAlgebra.QuadraticForm.Basic

set_option autoImplicit false

@[expose] public section

namespace OAI.HorrocksMumford

variable (k : Type*) [Field k]

/-- Binary forms as actual homogeneous polynomials, including the zero form. -/
abbrev BinaryForm (n : ℕ) := MvPolynomial.homogeneousSubmodule (Fin 2) k n

/-- The varying-multiplier observation in S10, quadratic in the quartic input. -/
noncomputable def sourceFamilyObservation (L : BinaryForm k 4 →ₗ[k] BinaryForm k 12) :
    QuadraticMap k (BinaryForm k 4) (MvPolynomial (Fin 2) k) :=
  QuadraticMap.linMulLin
    (MvPolynomial.homogeneousSubmodule (Fin 2) k 4).subtype
    ((MvPolynomial.homogeneousSubmodule (Fin 2) k 12).subtype.comp L)

variable {k}

@[simp]
theorem sourceFamilyObservation_apply (L : BinaryForm k 4 →ₗ[k] BinaryForm k 12) (h : BinaryForm k 4) :
    sourceFamilyObservation k L h = (h : MvPolynomial (Fin 2) k) * (L h : MvPolynomial (Fin 2) k) :=
  rfl

/-- S10 has degree-sixteen output; no identification with a symmetric square is used. -/
theorem sourceFamilyObservation_mem_homogeneous16
    (L : BinaryForm k 4 →ₗ[k] BinaryForm k 12) (h : BinaryForm k 4) :
    sourceFamilyObservation k L h ∈ MvPolynomial.homogeneousSubmodule (Fin 2) k 16 := by
  change ((h : MvPolynomial (Fin 2) k) * (L h : MvPolynomial (Fin 2) k)).IsHomogeneous 16
  exact MvPolynomial.IsHomogeneous.mul h.property (L h).property

/-- Universal varying-multiplier cancellation in the actual polynomial domain. -/
theorem sourceFamilyObservation_injective : Function.Injective (sourceFamilyObservation k) := by
  intro L₁ L₂ heq
  apply LinearMap.ext
  intro h
  by_cases hh : h = 0
  · subst h
    simp only [map_zero]
  · apply Subtype.ext
    have hp : (h : MvPolynomial (Fin 2) k) ≠ 0 := by
      intro hz
      apply hh
      exact Subtype.ext hz
    have he := congrArg (fun Q : QuadraticMap k (BinaryForm k 4)
      (MvPolynomial (Fin 2) k) => Q h) heq
    exact mul_left_cancel₀ hp he

/-- The nonzero scalar weight in S9 preserves the S10 injectivity statement. -/
theorem weighted_sourceFamilyObservation_injective (c : k) (hc : c ≠ 0) :
    Function.Injective (fun L : BinaryForm k 4 →ₗ[k] BinaryForm k 12 =>
      (-(c ^ 3)) • sourceFamilyObservation k L) := by
  intro L₁ L₂ heq
  apply sourceFamilyObservation_injective
  have hw : -(c ^ 3) ≠ 0 := neg_ne_zero.mpr (pow_ne_zero 3 hc)
  have he := congrArg (fun Q : QuadraticMap k (BinaryForm k 4)
    (MvPolynomial (Fin 2) k) => (-(c ^ 3))⁻¹ • Q) heq
  simpa only [smul_smul, inv_mul_cancel₀ hw, one_smul] using he

end OAI.HorrocksMumford
