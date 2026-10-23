module

public import Mathlib.LinearAlgebra.TensorProduct.Map
public import Mathlib.Algebra.Module.Submodule.Ker

set_option autoImplicit false

@[expose] public section

namespace OAI.HorrocksMumford

open scoped TensorProduct

variable (R W M2 M3 M4 : Type*) [CommRing R]
variable [AddCommGroup W] [AddCommGroup M2] [AddCommGroup M3] [AddCommGroup M4]
variable [Module R W] [Module R M2] [Module R M3] [Module R M4]

/-- All three endomorphism channels, with no invertibility restriction. -/
abbrev D0 := (M2 →ₗ[R] M2) × (M3 →ₗ[R] M3) × (M4 →ₗ[R] M4)

/-- The two independent tensor-map target channels. -/
abbrev T0 := (W ⊗[R] M2 →ₗ[R] M3) × (W ⊗[R] M3 →ₗ[R] M4)

variable {R W M2 M3 M4}

/-- The intrinsic fixed-pencil defect for supplied tensor maps (PR808, §2, (4)). -/
def pencilDelta (α : W ⊗[R] M2 →ₗ[R] M3) (β : W ⊗[R] M3 →ₗ[R] M4) :
    D0 R M2 M3 M4 →ₗ[R] T0 R W M2 M3 M4 where
  toFun X :=
    (X.2.1.comp α - α.comp (TensorProduct.map (LinearMap.id : W →ₗ[R] W) X.1),
     X.2.2.comp β - β.comp (TensorProduct.map (LinearMap.id : W →ₗ[R] W) X.2.1))
  map_add' X Y := by
    apply Prod.ext
    · apply TensorProduct.ext'
      intro w v
      simp [TensorProduct.tmul_add, sub_add_sub_comm]
    · apply TensorProduct.ext'
      intro w v
      simp [TensorProduct.tmul_add, sub_add_sub_comm]
  map_smul' r X := by
    apply Prod.ext
    · apply TensorProduct.ext'
      intro w v
      simp [TensorProduct.tmul_smul, smul_sub]
    · apply TensorProduct.ext'
      intro w v
      simp [TensorProduct.tmul_smul, smul_sub]

/-- The full fixed-pencil commutant, as a linear submodule. -/
def pencilCommutant (α : W ⊗[R] M2 →ₗ[R] M3) (β : W ⊗[R] M3 →ₗ[R] M4) :
    Submodule R (D0 R M2 M3 M4) :=
  LinearMap.ker (pencilDelta α β)

variable (α : W ⊗[R] M2 →ₗ[R] M3) (β : W ⊗[R] M3 →ₗ[R] M4)

/-- Kernel membership is exactly the two tensor intertwining equations. -/
theorem mem_pencilCommutant_iff (X : D0 R M2 M3 M4) :
    X ∈ pencilCommutant α β ↔
      X.2.1.comp α = α.comp (TensorProduct.map (LinearMap.id : W →ₗ[R] W) X.1) ∧
      X.2.2.comp β = β.comp (TensorProduct.map (LinearMap.id : W →ₗ[R] W) X.2.1) := by
  change
    (X.2.1.comp α - α.comp (TensorProduct.map (LinearMap.id : W →ₗ[R] W) X.1),
     X.2.2.comp β - β.comp (TensorProduct.map (LinearMap.id : W →ₗ[R] W) X.2.1)) =
      (0, 0) ↔ _
  rw [Prod.mk.injEq, sub_eq_zero, sub_eq_zero]

/-- Testing every pure tensor is equivalent to the intrinsic kernel condition. -/
theorem mem_pencilCommutant_iff_tmul (X : D0 R M2 M3 M4) :
    X ∈ pencilCommutant α β ↔
      (∀ (w : W) (v : M2), X.2.1 (α (w ⊗ₜ[R] v)) = α (w ⊗ₜ[R] X.1 v)) ∧
      (∀ (w : W) (v : M3), X.2.2 (β (w ⊗ₜ[R] v)) = β (w ⊗ₜ[R] X.2.1 v)) := by
  rw [mem_pencilCommutant_iff]
  constructor
  · intro h
    constructor
    · intro w v
      simpa using LinearMap.congr_fun h.1 (w ⊗ₜ[R] v)
    · intro w v
      simpa using LinearMap.congr_fun h.2 (w ⊗ₜ[R] v)
  · intro h
    constructor
    · apply TensorProduct.ext'
      intro w v
      simpa using h.1 w v
    · apply TensorProduct.ext'
      intro w v
      simpa using h.2 w v

/-- The simultaneous identity endomorphism triple. -/
def pencilIdentity : D0 R M2 M3 M4 :=
  (LinearMap.id, LinearMap.id, LinearMap.id)

/-- Componentwise composition; the left triple acts after the right triple. -/
def pencilCompose (X Y : D0 R M2 M3 M4) : D0 R M2 M3 M4 :=
  (X.1.comp Y.1, X.2.1.comp Y.2.1, X.2.2.comp Y.2.2)

theorem pencilIdentity_mem :
    (pencilIdentity : D0 R M2 M3 M4) ∈ pencilCommutant α β := by
  rw [mem_pencilCommutant_iff_tmul]
  constructor <;> intro w v <;> rfl

theorem pencilCompose_mem (X Y : D0 R M2 M3 M4)
    (hX : X ∈ pencilCommutant α β) (hY : Y ∈ pencilCommutant α β) :
    pencilCompose X Y ∈ pencilCommutant α β := by
  rw [mem_pencilCommutant_iff_tmul] at hX hY ⊢
  constructor
  · intro w v
    change X.2.1 (Y.2.1 (α (w ⊗ₜ[R] v))) = α (w ⊗ₜ[R] X.1 (Y.1 v))
    rw [hY.1 w v, hX.1 w (Y.1 v)]
  · intro w v
    change X.2.2 (Y.2.2 (β (w ⊗ₜ[R] v))) = β (w ⊗ₜ[R] X.2.1 (Y.2.1 v))
    rw [hY.2 w v, hX.2 w (Y.2.1 v)]

end OAI.HorrocksMumford
