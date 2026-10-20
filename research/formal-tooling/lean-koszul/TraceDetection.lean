import Mathlib.LinearAlgebra.Trace
import Mathlib.LinearAlgebra.Dual.Lemmas

/-!
Universal trace detection, independent of any geometric presentation.
The final theorem is conditional: the geometric pairing identity and nonzero
antecedent are explicit inputs, not conclusions of this file.
-/
namespace TraceDetection

open TensorProduct

variable {k A C W : Type*} [Field k]
  [AddCommGroup A] [Module k A]
  [AddCommGroup C] [Module k C]
  [AddCommGroup W] [Module k W]

/-- An injective coefficient map preserves nonzero linear maps into its source. -/
theorem injective_comp_ne_zero (γ : A →ₗ[k] C) (φ : W →ₗ[k] A)
    (hγ : Function.Injective γ) (hφ : φ ≠ 0) : γ.comp φ ≠ 0 := by
  intro h
  apply hφ
  ext w
  apply hγ
  have hw := LinearMap.congr_fun h w
  simpa using hw

/-- The trace of the universal rank-one endomorphism is evaluation.
This is deduced from Mathlib's trace/contraction identity. -/
theorem trace_rankOne [FiniteDimensional k W] (f : Module.Dual k W) (w : W) :
    LinearMap.trace k W (f.smulRight w) = f w := by
  change LinearMap.trace k W (dualTensorHom k W W (f ⊗ₜ[k] w)) = f w
  rw [LinearMap.trace_eq_contract_apply, contractLeft_apply]

/-- The rectangular trace pairing detects every nonzero linear map.
Only W needs to be finite-dimensional; C may be arbitrary. -/
theorem exists_trace_comp_ne_zero [FiniteDimensional k W]
    (T : W →ₗ[k] C) (hT : T ≠ 0) :
    ∃ B : C →ₗ[k] W, LinearMap.trace k W (B.comp T) ≠ 0 := by
  classical
  have hw : ∃ w : W, T w ≠ 0 := by
    by_contra h
    apply hT
    ext w
    by_contra hw
    exact h ⟨w, hw⟩
  obtain ⟨w, hw⟩ := hw
  have hf : ∃ f : Module.Dual k C, f (T w) ≠ 0 := by
    by_contra h
    apply hw
    apply (Module.forall_dual_apply_eq_zero_iff k (T w)).mp
    intro f
    by_contra hf
    exact h ⟨f, hf⟩
  obtain ⟨f, hf⟩ := hf
  refine ⟨f.smulRight w, ?_⟩
  have heq : (f.smulRight w).comp T = (f.comp T).smulRight w := by
    ext x
    rfl
  rw [heq, trace_rankOne]
  exact hf

/-- Injectivity followed by trace duality supplies an abstract detecting map. -/
theorem exists_trace_injective_comp_ne_zero [FiniteDimensional k W]
    (γ : A →ₗ[k] C) (φ : W →ₗ[k] A)
    (hγ : Function.Injective γ) (hφ : φ ≠ 0) :
    ∃ B : C →ₗ[k] W, LinearMap.trace k W (B.comp (γ.comp φ)) ≠ 0 :=
  exists_trace_comp_ne_zero (γ.comp φ) (injective_comp_ne_zero γ φ hγ hφ)

/-- Conditional cohomology detection. H is any pointed class space. A geometric
application must supply both the trace identity and vanishing of pairing at zero.
Neither cohomology, geometric injectivity, nor the antecedent is constructed here. -/
theorem class_ne_zero_of_trace_pairing [FiniteDimensional k W]
    {H : Type*} [Zero H] (r : H)
    (pairing : H → (C →ₗ[k] W) → k)
    (pairing_zero : ∀ B, pairing 0 B = 0)
    (γ : A →ₗ[k] C) (φ : W →ₗ[k] A)
    (hγ : Function.Injective γ) (hφ : φ ≠ 0)
    (pairing_trace : ∀ B, pairing r B = LinearMap.trace k W (B.comp (γ.comp φ))) :
    r ≠ 0 := by
  obtain ⟨B, hB⟩ := exists_trace_injective_comp_ne_zero γ φ hγ hφ
  intro hr
  apply hB
  rw [← pairing_trace B, hr, pairing_zero B]

end TraceDetection
