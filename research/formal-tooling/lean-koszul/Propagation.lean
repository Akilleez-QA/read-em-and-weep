import Mathlib.LinearAlgebra.Quotient.Basic
import Mathlib.LinearAlgebra.Dimension.DivisionRing
import Mathlib.LinearAlgebra.FiniteDimensional.Basic

/-!
# Conditional propagation of an equivariant cubic

This file formalizes only linear-algebra implications. The spaces, actions,
coordinate-spanning statements, scalar identities, and filtered transfer
statements are parameters. In particular it does not construct an actual
cohomology/Massey map, prove its nonvanishing, or evaluate any such map.
-/
namespace KoszulPropagation

variable {K : Type*} [Field K]
variable {U V W Z T : Type*}
variable [AddCommGroup U] [Module K U]
variable [AddCommGroup V] [Module K V]
variable [AddCommGroup W] [Module K W]
variable [AddCommGroup Z] [Module K Z]
variable [AddCommGroup T] [Module K T]

/-- Invariance under a family of linear operators. No choice of basis is used. -/
def Invariant {G : Type*} (ρ : G → V →ₗ[K] V) (S : Submodule K V) : Prop :=
  ∀ g v, v ∈ S → ρ g v ∈ S

/-- The irreducibility property actually needed: invariant subspaces are trivial.
It can be supplied by a genuine irreducibility theorem for a group action. -/
def IrreducibleOperators {G : Type*} (ρ : G → V →ₗ[K] V) : Prop :=
  ∀ S : Submodule K V, Invariant ρ S → S = ⊥ ∨ S = ⊤

/-- A nonzero equivariant linear map into an irreducible target is surjective. -/
theorem equivariant_nonzero_surjective {G : Type*}
    (ρU : G → U →ₗ[K] U) (ρV : G → V →ₗ[K] V)
    (hirr : IrreducibleOperators ρV) (f : U →ₗ[K] V)
    (heq : ∀ g u, f (ρU g u) = ρV g (f u)) (hnz : f ≠ 0) :
    Function.Surjective f := by
  have hinv : Invariant ρV (LinearMap.range f) := by
    intro g v hv
    obtain ⟨u, rfl⟩ := hv
    exact ⟨ρU g u, heq g u⟩
  rcases hirr (LinearMap.range f) hinv with hzero | hfull
  · exfalso
    apply hnz
    ext u
    have hu : f u ∈ LinearMap.range f := ⟨u, rfl⟩
    rw [hzero] at hu
    exact hu
  · intro v
    have hv : v ∈ LinearMap.range f := by rw [hfull]; trivial
    exact hv

/-- A surjective linear map takes any spanning generators of its source to
spanning generators of its target. This handles pure cubic generators of the
linearized cubic domain without assuming every vector is itself a pure cubic. -/
theorem surjective_map_spanning {X : Type*} (g : X → U) (f : U →ₗ[K] V)
    (hg : Submodule.span K (Set.range g) = ⊤)
    (hf : Function.Surjective f) :
    Submodule.span K (Set.range (fun x => f (g x))) = ⊤ := by
  let S : Submodule K V := Submodule.span K (Set.range (fun x => f (g x)))
  have hle : Submodule.span K (Set.range g) ≤ S.comap f := by
    apply Submodule.span_le.mpr
    rintro _ ⟨x, rfl⟩
    exact Submodule.subset_span ⟨x, rfl⟩
  rw [hg] at hle
  apply top_unique
  intro v _
  obtain ⟨u, rfl⟩ := hf v
  exact hle (Submodule.mem_top : u ∈ (⊤ : Submodule K U))

/-- Coordinate multiplication carries a spanning family to a spanning mixed
family, provided all coordinate images together span the next target.
The latter hypothesis is the linear-algebra content of coordinate multiplication
surjectivity, not an assertion that each individual coordinate is surjective. -/
theorem coordinate_spanning {A X : Type*}
    (c : X → V) (μ : A → V →ₗ[K] W) (m : A × X → W)
    (hc : Submodule.span K (Set.range c) = ⊤)
    (hμ : Submodule.span K (Set.range (fun p : A × V => μ p.1 p.2)) = ⊤)
    (hid : ∀ a x, m (a, x) = μ a (c x)) :
    Submodule.span K (Set.range m) = ⊤ := by
  let S : Submodule K W := Submodule.span K (Set.range m)
  have hcoordinate : ∀ a v, μ a v ∈ S := by
    intro a
    have hle : Submodule.span K (Set.range c) ≤ S.comap (μ a) := by
      apply Submodule.span_le.mpr
      rintro _ ⟨x, rfl⟩
      change μ a (c x) ∈ S
      rw [← hid a x]
      exact Submodule.subset_span ⟨(a, x), rfl⟩
    rw [hc] at hle
    intro v
    exact hle (Submodule.mem_top : v ∈ (⊤ : Submodule K V))
  have hle : Submodule.span K (Set.range (fun p : A × V => μ p.1 p.2)) ≤ S := by
    apply Submodule.span_le.mpr
    rintro _ ⟨p, rfl⟩
    exact hcoordinate p.1 p.2
  rw [hμ] at hle
  exact top_unique hle

/-- A surjective assembled coordinate map (for example from a direct sum or
tensor product) supplies the coordinate-spanning premise. Elementary inputs
must span its domain, and their images must be the stated coordinate products. -/
theorem coordinate_spanning_of_surjective_assembly {A X P : Type*}
    [AddCommGroup P] [Module K P]
    (c : X → V) (μ : A → V →ₗ[K] W) (m : A × X → W)
    (assemble : P →ₗ[K] W) (elementary : A × V → P)
    (hassemble : Function.Surjective assemble)
    (helementary : Submodule.span K (Set.range elementary) = ⊤)
    (hassembly : ∀ a v, assemble (elementary (a, v)) = μ a v)
    (hc : Submodule.span K (Set.range c) = ⊤)
    (hid : ∀ a x, m (a, x) = μ a (c x)) :
    Submodule.span K (Set.range m) = ⊤ := by
  have hcoord := surjective_map_spanning elementary assemble helementary hassemble
  have hfun : (fun p : A × V => assemble (elementary p)) =
      (fun p : A × V => μ p.1 p.2) := by
    funext p
    exact hassembly p.1 p.2
  rw [hfun] at hcoord
  exact coordinate_spanning c μ m hc hcoord hid

/-- Apply coordinate propagation twice, to the upper and then lower channel. -/
theorem two_mixed_channels_span {A B X : Type*}
    (c : X → V) (μ32 : A → V →ₗ[K] W) (μ21 : B → W →ₗ[K] Z)
    (upper : A × X → W) (lower : B × (A × X) → Z)
    (hc : Submodule.span K (Set.range c) = ⊤)
    (h32 : Submodule.span K (Set.range (fun p : A × V => μ32 p.1 p.2)) = ⊤)
    (h21 : Submodule.span K (Set.range (fun p : B × W => μ21 p.1 p.2)) = ⊤)
    (hu : ∀ a x, upper (a, x) = μ32 a (c x))
    (hl : ∀ b ax, lower (b, ax) = μ21 b (upper ax)) :
    Submodule.span K (Set.range upper) = ⊤ ∧
      Submodule.span K (Set.range lower) = ⊤ := by
  have hupper := coordinate_spanning c μ32 upper hc h32 hu
  exact ⟨hupper, coordinate_spanning upper μ21 lower hupper h21 hl⟩

/-- No splitting is assumed: containing a subspace and surjecting onto its
quotient forces the retained image to be the entire target. -/
theorem subspace_and_quotient (I L : Submodule K T)
    (hlower : L ≤ I)
    (hquot : Function.Surjective (fun i : I => L.mkQ (i : T))) : I = ⊤ := by
  apply top_unique
  intro t _
  obtain ⟨i, hi⟩ := hquot (L.mkQ t)
  change L.mkQ (i : T) = L.mkQ t at hi
  have hdiff : t - (i : T) ∈ L := by
    have hker : L.mkQ (t - (i : T)) = 0 := by
      rw [map_sub, hi, sub_self]
    have : t - (i : T) ∈ LinearMap.ker L.mkQ := hker
    simpa only [Submodule.ker_mkQ] using this
  have hsum : (t - (i : T)) + (i : T) ∈ I := I.add_mem (hlower hdiff) i.property
  simpa only [sub_add_cancel] using hsum

/-- The imported four- and eight-dimensional pieces give twelve, after the
actual subspace/quotient argument proves fullness. -/
theorem retained_twelve [FiniteDimensional K T] (I L : Submodule K T)
    (hlower : L ≤ I)
    (hquot : Function.Surjective (fun i : I => L.mkQ (i : T)))
    (h4 : Module.finrank K L = 4)
    (h8 : Module.finrank K (T ⧸ L) = 8) :
    I = ⊤ ∧ Module.finrank K T = 12 := by
  refine ⟨subspace_and_quotient I L hlower hquot, ?_⟩
  have hdim := L.finrank_quotient_add_finrank
  rw [h4, h8] at hdim
  exact hdim.symm

/-- Complete conditional chain. The two transfer hypotheses explicitly encode
what the upstairs/downstairs comparison must establish geometrically. They are
not proved here. In particular, nonvanishing of the actual cubic is not proved. -/
theorem conditional_full_retained_span {G A B X : Type*}
    (ρU : G → U →ₗ[K] U) (ρV : G → V →ₗ[K] V)
    (hirr : IrreducibleOperators ρV) (f : U →ₗ[K] V)
    (heq : ∀ g u, f (ρU g u) = ρV g (f u)) (hnz : f ≠ 0)
    (generators : X → U)
    (hgen : Submodule.span K (Set.range generators) = ⊤)
    (μ32 : A → V →ₗ[K] W) (μ21 : B → W →ₗ[K] Z)
    (upper : A × X → W) (lower : B × (A × X) → Z)
    (h32 : Submodule.span K (Set.range (fun p : A × V => μ32 p.1 p.2)) = ⊤)
    (h21 : Submodule.span K (Set.range (fun p : B × W => μ21 p.1 p.2)) = ⊤)
    (hu : ∀ a x, upper (a, x) = μ32 a (f (generators x)))
    (hl : ∀ b ax, lower (b, ax) = μ21 b (upper ax))
    (I L : Submodule K T)
    (transferLower : Submodule.span K (Set.range lower) = ⊤ → L ≤ I)
    (transferUpper : Submodule.span K (Set.range upper) = ⊤ →
      Function.Surjective (fun i : I => L.mkQ (i : T))) : I = ⊤ := by
  have hsurj := equivariant_nonzero_surjective ρU ρV hirr f heq hnz
  have hc := surjective_map_spanning generators f hgen hsurj
  obtain ⟨hupper, hlower⟩ := two_mixed_channels_span
    (fun x => f (generators x)) μ32 μ21 upper lower hc h32 h21 hu hl
  exact subspace_and_quotient I L (transferLower hlower) (transferUpper hupper)

end KoszulPropagation
