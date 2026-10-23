module

public import Mathlib.RingTheory.SimpleModule.Basic

set_option autoImplicit false

@[expose] public section

namespace OAI.HorrocksMumford

variable {R : Type*} [Ring R]
variable {M : Fin 3 → Type*}
variable [∀ i, AddCommGroup (M i)] [∀ i, Module R (M i)]
variable [∀ i, IsSimpleModule R (M i)]

/-- Schur's lemma turns inequivalence into vanishing of off-diagonal maps. -/
theorem multiplicityFree_hom_eq_zero
    (hsep : Pairwise (fun i j => IsEmpty (M i ≃ₗ[R] M j)))
    {i j : Fin 3} (hij : i ≠ j) (f : M i →ₗ[R] M j) : f = 0 := by
  rcases f.bijective_or_eq_zero with hf | hf
  · exact False.elim ((hsep hij).false (LinearEquiv.ofBijective f hf))
  · exact hf

/-- Every endomorphism of this multiplicity-free product acts coordinatewise. -/
theorem multiplicityFree_endomorphism_coordinate
    (hsep : Pairwise (fun i j => IsEmpty (M i ≃ₗ[R] M j)))
    (f : (∀ i, M i) →ₗ[R] (∀ i, M i)) (x : ∀ i, M i) (i : Fin 3) :
    (f x) i = (f (LinearMap.single R M i (x i))) i := by
  classical
  have hx := congrArg (fun y : ∀ i, M i => (f y) i)
    (LinearMap.sum_single_apply M x)
  rw [map_sum, Finset.sum_apply] at hx
  apply hx.symm.trans
  apply Finset.sum_eq_single i
  · intro j _ hji
    have hz := multiplicityFree_hom_eq_zero hsep hji
      ((LinearMap.proj i).comp (f.comp (LinearMap.single R M j)))
    have he := LinearMap.congr_fun hz (x j)
    change (f (Pi.single j (x j))) i = 0 at he
    exact he
  · simp

/-- Exact cyclic support for three pairwise inequivalent simple modules.
The coordinate-preservation step is derived from a complementary projection. -/
theorem mem_cyclicSpan_iff_coordinate_support
    (hsep : Pairwise (fun i j => IsEmpty (M i ≃ₗ[R] M j)))
    (v x : ∀ i, M i) :
    x ∈ Submodule.span R ({v} : Set (∀ i, M i)) ↔
      ∀ i, v i = 0 → x i = 0 := by
  classical
  let S : Submodule R (∀ i, M i) := Submodule.span R {v}
  have hv : v ∈ S := Submodule.mem_span_singleton_self v
  constructor
  · intro hx i hi
    have hle : S ≤ LinearMap.ker (LinearMap.proj i) := by
      apply Submodule.span_le.mpr
      intro y hy
      rcases Set.mem_singleton_iff.mp hy with rfl
      exact hi
    exact hle hx
  · intro hx
    obtain ⟨T, hT⟩ := exists_isCompl S
    let p : (∀ i, M i) →ₗ[R] (∀ i, M i) := S.projection T hT
    have hpv : p v = v := S.projection_apply_of_mem_left hT hv
    have hfix : ∀ i, v i ≠ 0 →
        (LinearMap.proj i).comp (p.comp (LinearMap.single R M i)) = LinearMap.id := by
      intro i hi
      let d : M i →ₗ[R] M i :=
        (LinearMap.proj i).comp (p.comp (LinearMap.single R M i))
      have hdv : d (v i) = v i := by
        change (p (LinearMap.single R M i (v i))) i = v i
        rw [← multiplicityFree_endomorphism_coordinate hsep p v i, hpv]
      have hz : (d - LinearMap.id : M i →ₗ[R] M i) (v i) = 0 := by
        simpa using sub_eq_zero.mpr hdv
      rcases (d - LinearMap.id : M i →ₗ[R] M i).injective_or_eq_zero with hinj | hzero
      · exact False.elim (hi (hinj (hz.trans (map_zero _).symm)))
      · exact sub_eq_zero.mp hzero
    have hpx : p x = x := by
      funext i
      rw [multiplicityFree_endomorphism_coordinate hsep p x i]
      by_cases hi : v i = 0
      · simp [hx i hi]
      · have he := LinearMap.congr_fun (hfix i hi) (x i)
        exact he
    rw [← hpx]
    exact S.projection_apply_mem hT x

/-- A cyclic vector generates the whole product precisely when no coordinate vanishes. -/
theorem cyclicSpan_eq_top_iff
    (hsep : Pairwise (fun i j => IsEmpty (M i ≃ₗ[R] M j)))
    (v : ∀ i, M i) :
    Submodule.span R ({v} : Set (∀ i, M i)) = ⊤ ↔ ∀ i, v i ≠ 0 := by
  classical
  constructor
  · intro htop i hi
    have : Nontrivial (M i) := IsSimpleModule.nontrivial R (M i)
    obtain ⟨y, hy⟩ := exists_ne (0 : M i)
    have hm : LinearMap.single R M i y ∈ Submodule.span R ({v} : Set (∀ i, M i)) := by
      rw [htop]
      exact Submodule.mem_top
    have hz := (mem_cyclicSpan_iff_coordinate_support hsep v _).mp hm i hi
    apply hy
    simpa using hz
  · intro hv
    apply top_unique
    intro x _
    exact (mem_cyclicSpan_iff_coordinate_support hsep v x).mpr
      (fun i hi => False.elim (hv i hi))

end OAI.HorrocksMumford
