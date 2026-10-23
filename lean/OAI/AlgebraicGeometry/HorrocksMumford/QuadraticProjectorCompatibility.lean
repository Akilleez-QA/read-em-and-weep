module

public import Mathlib.Algebra.Module.Submodule.Range

/-!
Supporting algebra for Lean 4.34.1 and mathlib
d13f23b723b8a846827a245b89c10fc7d3f11612.

The abstract projector criterion in PR818, §5. The map `q` is supplied;
no actual positive quadratic action or extension is constructed.
-/

set_option autoImplicit false

@[expose] public section

namespace OAI.HorrocksMumford

variable {K V W : Type*} [Semiring K]
  [AddCommGroup V] [Module K V] [AddCommGroup W] [Module K W]

/-- A specified map intertwines two idempotents exactly when both off-diagonal
blocks vanish. Here `LinearMap.id` is the identity endomorphism and `comp`
expresses multiplication of endomorphisms. -/
theorem quadraticProjectorCompatibility_iff_crossTerms
    (q : V →ₗ[K] W) (p : V →ₗ[K] V) (r : W →ₗ[K] W)
    (hp : p.comp p = p) (hr : r.comp r = r) :
    r.comp q = q.comp p ↔
      (r.comp q).comp (LinearMap.id - p) = 0 ∧
      ((LinearMap.id - r).comp q).comp p = 0 := by
  have hp' (x : V) : p (p x) = p x := LinearMap.congr_fun hp x
  have hr' (y : W) : r (r y) = r y := LinearMap.congr_fun hr y
  constructor
  · intro h
    have h' (x : V) : r (q x) = q (p x) := LinearMap.congr_fun h x
    constructor
    · ext x
      simp only [LinearMap.comp_apply, LinearMap.sub_apply, LinearMap.id_apply,
        map_sub, LinearMap.zero_apply]
      rw [h', h', hp', sub_self]
    · ext x
      simp only [LinearMap.comp_apply, LinearMap.sub_apply, LinearMap.id_apply,
        LinearMap.zero_apply]
      rw [← h' x, hr', sub_self]
  · rintro ⟨h₁, h₂⟩
    ext x
    have h₁' : r (q x) = r (q (p x)) := by
      have hx := LinearMap.congr_fun h₁ x
      simpa only [LinearMap.comp_apply, LinearMap.sub_apply, LinearMap.id_apply,
        map_sub, LinearMap.zero_apply, sub_eq_zero] using hx
    have h₂' : q (p x) = r (q (p x)) := by
      have hx := LinearMap.congr_fun h₂ x
      simpa only [LinearMap.comp_apply, LinearMap.sub_apply, LinearMap.id_apply,
        LinearMap.zero_apply, sub_eq_zero] using hx
    exact h₁'.trans h₂'.symm

/-- Intertwining idempotents is equivalent to preserving their image and
kernel summands. No dimension, basis, or field hypothesis is required. -/
theorem quadraticProjectorCompatibility_iff_range_ker
    (q : V →ₗ[K] W) (p : V →ₗ[K] V) (r : W →ₗ[K] W)
    (hp : p.comp p = p) (hr : r.comp r = r) :
    r.comp q = q.comp p ↔
      (∀ x, x ∈ LinearMap.range p → q x ∈ LinearMap.range r) ∧
      (∀ x, x ∈ LinearMap.ker p → q x ∈ LinearMap.ker r) := by
  have hp' (x : V) : p (p x) = p x := LinearMap.congr_fun hp x
  have hr' (y : W) : r (r y) = r y := LinearMap.congr_fun hr y
  constructor
  · intro h
    have h' (x : V) : r (q x) = q (p x) := LinearMap.congr_fun h x
    constructor
    · intro x hx
      obtain ⟨y, rfl⟩ := LinearMap.mem_range.mp hx
      exact LinearMap.mem_range.mpr ⟨q y, h' y⟩
    · intro x hx
      apply LinearMap.mem_ker.mpr
      rw [h', LinearMap.mem_ker.mp hx, map_zero]
  · rintro ⟨himage, hkernel⟩
    ext x
    have hfixed : r (q (p x)) = q (p x) := by
      obtain ⟨y, hy⟩ := LinearMap.mem_range.mp
        (himage (p x) (LinearMap.mem_range_self p x))
      rw [← hy, hr']
    have hzero : r (q (x - p x)) = 0 := by
      apply LinearMap.mem_ker.mp
      apply hkernel
      apply LinearMap.mem_ker.mpr
      rw [map_sub, hp', sub_self]
    have heq : r (q x) = r (q (p x)) := by
      simpa only [map_sub, sub_eq_zero] using hzero
    exact heq.trans hfixed

/-- The same exact test for every member of a supplied family of maps. -/
theorem quadraticProjectorCompatibility_family_iff_crossTerms
    {ι : Type*} (q : ι → V →ₗ[K] W)
    (p : V →ₗ[K] V) (r : W →ₗ[K] W)
    (hp : p.comp p = p) (hr : r.comp r = r) :
    (∀ i, r.comp (q i) = (q i).comp p) ↔
      ∀ i, (r.comp (q i)).comp (LinearMap.id - p) = 0 ∧
        ((LinearMap.id - r).comp (q i)).comp p = 0 := by
  constructor
  · intro h i
    exact (quadraticProjectorCompatibility_iff_crossTerms (q i) p r hp hr).mp (h i)
  · intro h i
    exact (quadraticProjectorCompatibility_iff_crossTerms (q i) p r hp hr).mpr (h i)

end OAI.HorrocksMumford
