module

public import Mathlib.Algebra.Module.Prod
public import Mathlib.Algebra.Module.Submodule.Ker
public import Mathlib.Tactic.Ring.Basic

set_option autoImplicit false

@[expose] public section

namespace OAI.HorrocksMumford

variable (K : Type*) [Field K]

/-- Coordinates are `(a0, a8, aC)`, represented as `a0, (a8, aC)`.
The output coordinates are `(tau2, tau3, tau4)` in the same convention. -/
def uncoupledTraceMap : (K × (K × K)) →ₗ[K] (K × (K × K)) where
  toFun a := (9 * a.1 + 15 * a.2.1 + 17 * a.2.2,
    (18 * a.1 + 18 * a.2.1 + 18 * a.2.2,
     16 * a.1 + 12 * a.2.1 + 9 * a.2.2))
  map_add' a b := by ext <;> dsimp <;> ring1
  map_smul' c a := by
    ext <;> dsimp <;> ring1

/-- The coupled coordinates are `(a0, aR)`. -/
def coupledTraceMap : (K × K) →ₗ[K] (K × (K × K)) where
  toFun a := (9 * a.1 + 32 * a.2,
    (18 * a.1 + 36 * a.2, 16 * a.1 + 21 * a.2))
  map_add' a b := by ext <;> dsimp <;> ring1
  map_smul' c a := by
    ext <;> dsimp <;> ring1

variable {K}

theorem uncoupled_reconstruct_a0 (a : K × (K × K)) :
    180 * a.1 = -54 * (uncoupledTraceMap K a).1 +
      69 * (uncoupledTraceMap K a).2.1 - 36 * (uncoupledTraceMap K a).2.2 := by
  change 180 * a.1 = -54 * (9 * a.1 + 15 * a.2.1 + 17 * a.2.2) +
    69 * (18 * a.1 + 18 * a.2.1 + 18 * a.2.2) -
    36 * (16 * a.1 + 12 * a.2.1 + 9 * a.2.2)
  ring1

theorem uncoupled_reconstruct_a8 (a : K × (K × K)) :
    180 * a.2.1 = 126 * (uncoupledTraceMap K a).1 -
      191 * (uncoupledTraceMap K a).2.1 + 144 * (uncoupledTraceMap K a).2.2 := by
  change 180 * a.2.1 = 126 * (9 * a.1 + 15 * a.2.1 + 17 * a.2.2) -
    191 * (18 * a.1 + 18 * a.2.1 + 18 * a.2.2) +
    144 * (16 * a.1 + 12 * a.2.1 + 9 * a.2.2)
  ring1

theorem uncoupled_reconstruct_aC (a : K × (K × K)) :
    180 * a.2.2 = -72 * (uncoupledTraceMap K a).1 +
      132 * (uncoupledTraceMap K a).2.1 - 108 * (uncoupledTraceMap K a).2.2 := by
  change 180 * a.2.2 = -72 * (9 * a.1 + 15 * a.2.1 + 17 * a.2.2) +
    132 * (18 * a.1 + 18 * a.2.1 + 18 * a.2.2) -
    108 * (16 * a.1 + 12 * a.2.1 + 9 * a.2.2)
  ring1

theorem coupled_reconstruct_a0 (a : K × K) :
    (-252) * a.1 = 36 * (coupledTraceMap K a).1 -
      32 * (coupledTraceMap K a).2.1 := by
  change (-252) * a.1 = 36 * (9 * a.1 + 32 * a.2) -
    32 * (18 * a.1 + 36 * a.2)
  ring1

theorem coupled_reconstruct_aR (a : K × K) :
    (-252) * a.2 = -18 * (coupledTraceMap K a).1 +
      9 * (coupledTraceMap K a).2.1 := by
  change (-252) * a.2 = -18 * (9 * a.1 + 32 * a.2) +
    9 * (18 * a.1 + 36 * a.2)
  ring1

variable [CharZero K]

theorem uncoupledTraceMap_injective : Function.Injective (uncoupledTraceMap K) := by
  intro a b h
  have h0 : (180 : K) * a.1 = 180 * b.1 := by
    rw [uncoupled_reconstruct_a0 a, uncoupled_reconstruct_a0 b, h]
  have h8 : (180 : K) * a.2.1 = 180 * b.2.1 := by
    rw [uncoupled_reconstruct_a8 a, uncoupled_reconstruct_a8 b, h]
  have hC : (180 : K) * a.2.2 = 180 * b.2.2 := by
    rw [uncoupled_reconstruct_aC a, uncoupled_reconstruct_aC b, h]
  have hn : (180 : K) ≠ 0 := Nat.cast_ne_zero.mpr (by decide)
  exact Prod.ext (mul_left_cancel₀ hn h0)
    (Prod.ext (mul_left_cancel₀ hn h8) (mul_left_cancel₀ hn hC))

theorem coupledTraceMap_injective : Function.Injective (coupledTraceMap K) := by
  intro a b h
  have h0 : (-252 : K) * a.1 = (-252) * b.1 := by
    rw [coupled_reconstruct_a0 a, coupled_reconstruct_a0 b, h]
  have hR : (-252 : K) * a.2 = (-252) * b.2 := by
    rw [coupled_reconstruct_aR a, coupled_reconstruct_aR b, h]
  have hn : (-252 : K) ≠ 0 := neg_ne_zero.mpr (Nat.cast_ne_zero.mpr (by decide))
  exact Prod.ext (mul_left_cancel₀ hn h0) (mul_left_cancel₀ hn hR)

omit [CharZero K] in
/-- Pure linear algebra: an injective postcomposition preserves the kernel. -/
theorem ker_comp_of_injective
    {V W U : Type*} [AddCommGroup V] [Module K V]
    [AddCommGroup W] [Module K W] [AddCommGroup U] [Module K U]
    (traceMap : W →ₗ[K] U) (hi : Function.Injective traceMap) (diag : V →ₗ[K] W) :
    LinearMap.ker (traceMap.comp diag) = LinearMap.ker diag := by
  ext x
  change traceMap (diag x) = 0 ↔ diag x = 0
  constructor
  · intro h
    apply hi
    simpa only [map_zero] using h
  · intro h
    rw [h, map_zero]

theorem uncoupled_ker_comp_diag
    {V : Type*} [AddCommGroup V] [Module K V] (diag : V →ₗ[K] (K × (K × K))) :
    LinearMap.ker ((uncoupledTraceMap K).comp diag) = LinearMap.ker diag :=
  ker_comp_of_injective (uncoupledTraceMap K) uncoupledTraceMap_injective diag

theorem coupled_ker_comp_diag
    {V : Type*} [AddCommGroup V] [Module K V] (diag : V →ₗ[K] (K × K)) :
    LinearMap.ker ((coupledTraceMap K).comp diag) = LinearMap.ker diag :=
  ker_comp_of_injective (coupledTraceMap K) coupledTraceMap_injective diag

end OAI.HorrocksMumford
