module

public import Mathlib.LinearAlgebra.TensorProduct.Map
public import OAI.AlgebraicGeometry.HorrocksMumford.QuadraticProjectorCompatibility

/-!
Supporting tensor adapter for Lean 4.34.1 and mathlib
d13f23b723b8a846827a245b89c10fc7d3f11612.
The quadratic compatibility dependency is the exact PR865 source at
80f241711bcd3a053268de6a83c8aee68403ebbf, SHA-256
1bc07ce1ca444f822abc5a6c344d099475c9b6e45cc024ae2985878bb5b7ba32.
This supplies abstract tensor inputs for the criterion motivated by PR818,
f4a73af666900ad2cb34a756d24b88e19dd6feaa, §5 of
research/hm/negative-truncation-extension/PROOF.md. The map q is supplied;
no actual quadratic action or geometric lift is constructed.
-/

set_option autoImplicit false

@[expose] public section

namespace OAI.HorrocksMumford

variable {R W V N : Type*} [CommRing R]
  [AddCommGroup W] [Module R W] [AddCommGroup V] [Module R V]
  [AddCommGroup N] [Module R N]

/-- The genuine tensor endomorphism `id ⊗ p`. -/
def tensorProjector (p : V →ₗ[R] V) :
    TensorProduct R W V →ₗ[R] TensorProduct R W V :=
  TensorProduct.map (LinearMap.id : W →ₗ[R] W) p

/-- The slice `v ↦ q (w ⊗ v)` of a supplied bundled map. -/
def tensorProjectorSlice (q : TensorProduct R W V →ₗ[R] N) (w : W) : V →ₗ[R] N :=
  q.comp (TensorProduct.mk R W V w)

/-- Idempotence of the second factor induces idempotence on the tensor product. -/
theorem tensorProjector_idempotent (p : V →ₗ[R] V) (hp : p.comp p = p) :
    (tensorProjector (W := W) p).comp (tensorProjector (W := W) p) =
      tensorProjector (W := W) p := by
  apply TensorProduct.ext'
  intro w v
  simp only [tensorProjector, LinearMap.comp_apply, TensorProduct.map_tmul,
    LinearMap.id_apply]
  have hpv : p (p v) = p v := LinearMap.congr_fun hp v
  rw [hpv]

/-- Bundled intertwining is exactly intertwining on every pure-tensor slice. -/
theorem tensorProjectorCompatibility_iff_slices
    (q : TensorProduct R W V →ₗ[R] N) (p : V →ₗ[R] V) (r : N →ₗ[R] N) :
    r.comp q = q.comp (tensorProjector (W := W) p) ↔
      ∀ w : W, r.comp (tensorProjectorSlice q w) =
        (tensorProjectorSlice q w).comp p := by
  constructor
  · intro h w
    apply LinearMap.ext
    intro v
    simpa only [tensorProjectorSlice, tensorProjector, LinearMap.comp_apply,
      TensorProduct.mk_apply, TensorProduct.map_tmul, LinearMap.id_apply]
      using LinearMap.congr_fun h (TensorProduct.tmul R w v)
  · intro h
    apply TensorProduct.ext'
    intro w v
    simpa only [tensorProjectorSlice, tensorProjector, LinearMap.comp_apply,
      TensorProduct.mk_apply, TensorProduct.map_tmul, LinearMap.id_apply]
      using LinearMap.congr_fun (h w) v

/-- The exact bundled criterion retains both cross terms and both explicit
factor idempotence hypotheses. -/
theorem tensorProjectorCompatibility_iff_crossTerms
    (q : TensorProduct R W V →ₗ[R] N) (p : V →ₗ[R] V) (r : N →ₗ[R] N)
    (hp : p.comp p = p) (hr : r.comp r = r) :
    r.comp q = q.comp (tensorProjector (W := W) p) ↔
      (r.comp q).comp (LinearMap.id - tensorProjector (W := W) p) = 0 ∧
      ((LinearMap.id - r).comp q).comp (tensorProjector (W := W) p) = 0 := by
  exact quadraticProjectorCompatibility_iff_crossTerms q
    (tensorProjector (W := W) p) r (tensorProjector_idempotent p hp) hr

end OAI.HorrocksMumford
