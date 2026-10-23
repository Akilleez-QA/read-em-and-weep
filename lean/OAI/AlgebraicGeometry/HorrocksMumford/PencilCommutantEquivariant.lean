module

public import OAI.AlgebraicGeometry.HorrocksMumford.PencilCommutant

set_option autoImplicit false

@[expose] public section

namespace OAI.HorrocksMumford

open scoped TensorProduct

variable {R G W U V M2 M3 M4 : Type*} [CommRing R] [Monoid G]
variable [AddCommGroup W] [AddCommGroup U] [AddCommGroup V]
variable [AddCommGroup M2] [AddCommGroup M3] [AddCommGroup M4]
variable [Module R W] [Module R U] [Module R V]
variable [Module R M2] [Module R M3] [Module R M4]

/-- The bundled diagonal action on the ordered tensor product. -/
def tensorAction (rhoU : G →* Module.End R U) (rhoV : G →* Module.End R V) :
    G →* Module.End R (U ⊗[R] V) where
  toFun g := TensorProduct.map (rhoU g) (rhoV g)
  map_one' := by simp
  map_mul' g h := by
    rw [rhoU.map_mul, rhoV.map_mul, TensorProduct.map_mul]

@[simp] theorem tensorAction_apply (rhoU : G →* Module.End R U)
    (rhoV : G →* Module.End R V) (g : G) :
    tensorAction rhoU rhoV g = TensorProduct.map (rhoU g) (rhoV g) := rfl

/-- Linear maps intertwining the two supplied actions. -/
def equivariantHom (rhoU : G →* Module.End R U) (rhoV : G →* Module.End R V) :
    Submodule R (U →ₗ[R] V) where
  carrier := {f | ∀ g : G, f.comp (rhoU g) = (rhoV g).comp f}
  zero_mem' := by intro g; ext u; simp
  add_mem' := by
    intro f h hf hh g
    apply LinearMap.ext
    intro u
    have hf' := LinearMap.congr_fun (hf g) u
    have hh' := LinearMap.congr_fun (hh g) u
    simpa only [LinearMap.comp_apply, LinearMap.add_apply, map_add] using
      congrArg₂ (fun a b : V => a + b) hf' hh'
  smul_mem' := by
    intro r f hf g
    apply LinearMap.ext
    intro u
    have hf' := LinearMap.congr_fun (hf g) u
    simpa only [LinearMap.comp_apply, LinearMap.smul_apply, map_smul] using
      congrArg (fun v : V => r • v) hf'

theorem mem_equivariantHom_iff (rhoU : G →* Module.End R U)
    (rhoV : G →* Module.End R V) (f : U →ₗ[R] V) :
    f ∈ equivariantHom rhoU rhoV ↔
      ∀ g : G, f.comp (rhoU g) = (rhoV g).comp f := Iff.rfl

theorem mem_equivariantHom_iff_apply (rhoU : G →* Module.End R U)
    (rhoV : G →* Module.End R V) (f : U →ₗ[R] V) :
    f ∈ equivariantHom rhoU rhoV ↔
      ∀ (g : G) (u : U), f (rhoU g u) = rhoV g (f u) := by
  constructor
  · intro h g u
    exact LinearMap.congr_fun (h g) u
  · intro h g
    exact LinearMap.ext (h g)

/-- The three equivariant endomorphism channels; no units are required. -/
def pencilEquivariantDomain (rho2 : G →* Module.End R M2)
    (rho3 : G →* Module.End R M3) (rho4 : G →* Module.End R M4) :
    Submodule R (D0 R M2 M3 M4) where
  carrier := {X | X.1 ∈ equivariantHom rho2 rho2 ∧
    X.2.1 ∈ equivariantHom rho3 rho3 ∧ X.2.2 ∈ equivariantHom rho4 rho4}
  zero_mem' := ⟨(equivariantHom rho2 rho2).zero_mem,
    (equivariantHom rho3 rho3).zero_mem, (equivariantHom rho4 rho4).zero_mem⟩
  add_mem' := fun hX hY => ⟨(equivariantHom rho2 rho2).add_mem hX.1 hY.1,
    (equivariantHom rho3 rho3).add_mem hX.2.1 hY.2.1,
    (equivariantHom rho4 rho4).add_mem hX.2.2 hY.2.2⟩
  smul_mem' := fun r X hX => ⟨(equivariantHom rho2 rho2).smul_mem r hX.1,
    (equivariantHom rho3 rho3).smul_mem r hX.2.1,
    (equivariantHom rho4 rho4).smul_mem r hX.2.2⟩

/-- Both tensor Hom channels with the full diagonal action on their sources. -/
def pencilEquivariantTarget (rhoW : G →* Module.End R W)
    (rho2 : G →* Module.End R M2) (rho3 : G →* Module.End R M3)
    (rho4 : G →* Module.End R M4) : Submodule R (T0 R W M2 M3 M4) where
  carrier := {F | F.1 ∈ equivariantHom (tensorAction rhoW rho2) rho3 ∧
    F.2 ∈ equivariantHom (tensorAction rhoW rho3) rho4}
  zero_mem' := ⟨(equivariantHom (tensorAction rhoW rho2) rho3).zero_mem,
    (equivariantHom (tensorAction rhoW rho3) rho4).zero_mem⟩
  add_mem' := fun hF hH =>
    ⟨(equivariantHom (tensorAction rhoW rho2) rho3).add_mem hF.1 hH.1,
     (equivariantHom (tensorAction rhoW rho3) rho4).add_mem hF.2 hH.2⟩
  smul_mem' := fun r F hF =>
    ⟨(equivariantHom (tensorAction rhoW rho2) rho3).smul_mem r hF.1,
     (equivariantHom (tensorAction rhoW rho3) rho4).smul_mem r hF.2⟩

variable (rhoW : G →* Module.End R W)
variable (rho2 : G →* Module.End R M2) (rho3 : G →* Module.End R M3)
variable (rho4 : G →* Module.End R M4)

theorem mem_pencilEquivariantDomain_iff (X : D0 R M2 M3 M4) :
    X ∈ pencilEquivariantDomain rho2 rho3 rho4 ↔
      X.1 ∈ equivariantHom rho2 rho2 ∧
      X.2.1 ∈ equivariantHom rho3 rho3 ∧
      X.2.2 ∈ equivariantHom rho4 rho4 := Iff.rfl

theorem mem_pencilEquivariantTarget_iff (F : T0 R W M2 M3 M4) :
    F ∈ pencilEquivariantTarget rhoW rho2 rho3 rho4 ↔
      F.1 ∈ equivariantHom (tensorAction rhoW rho2) rho3 ∧
      F.2 ∈ equivariantHom (tensorAction rhoW rho3) rho4 := Iff.rfl

/-- A single defect channel intertwines the diagonal action. -/
theorem tensorDefect_mem_equivariantHom
    (rhoU : G →* Module.End R U) (rhoV : G →* Module.End R V)
    (a : W ⊗[R] U →ₗ[R] V) (x : Module.End R U) (y : Module.End R V)
    (ha : a ∈ equivariantHom (tensorAction rhoW rhoU) rhoV)
    (hx : x ∈ equivariantHom rhoU rhoU)
    (hy : y ∈ equivariantHom rhoV rhoV) :
    y.comp a - a.comp (TensorProduct.map (LinearMap.id : W →ₗ[R] W) x) ∈
      equivariantHom (tensorAction rhoW rhoU) rhoV := by
  have ha' := (mem_equivariantHom_iff_apply _ _ a).mp ha
  have hx' := (mem_equivariantHom_iff_apply _ _ x).mp hx
  have hy' := (mem_equivariantHom_iff_apply _ _ y).mp hy
  have hat (g : G) (w : W) (u : U) :
      a (rhoW g w ⊗ₜ[R] rhoU g u) = rhoV g (a (w ⊗ₜ[R] u)) := by
    simpa using ha' g (w ⊗ₜ[R] u)
  intro g
  apply TensorProduct.ext'
  intro w u
  simp only [LinearMap.comp_apply, LinearMap.sub_apply, tensorAction_apply,
    TensorProduct.map_tmul, LinearMap.id_apply]
  rw [hat, hx' g u, hat, hy' g, map_sub]

variable (alpha : W ⊗[R] M2 →ₗ[R] M3) (beta : W ⊗[R] M3 →ₗ[R] M4)
variable (hAlpha : alpha ∈ equivariantHom (tensorAction rhoW rho2) rho3)
variable (hBeta : beta ∈ equivariantHom (tensorAction rhoW rho3) rho4)

include hAlpha hBeta in
/-- The ambient defect lands in the equivariant target on the equivariant domain. -/
theorem pencilDelta_mem_equivariantTarget (X : D0 R M2 M3 M4)
    (hX : X ∈ pencilEquivariantDomain rho2 rho3 rho4) :
    pencilDelta alpha beta X ∈ pencilEquivariantTarget rhoW rho2 rho3 rho4 := by
  exact ⟨tensorDefect_mem_equivariantHom rhoW rho2 rho3 alpha X.1 X.2.1
      hAlpha hX.1 hX.2.1,
    tensorDefect_mem_equivariantHom rhoW rho3 rho4 beta X.2.1 X.2.2
      hBeta hX.2.1 hX.2.2⟩

/-- Equation (4) as a genuine linear map between equivariant submodule types. -/
def pencilDeltaEquivariant :
    pencilEquivariantDomain rho2 rho3 rho4 →ₗ[R]
      pencilEquivariantTarget rhoW rho2 rho3 rho4 :=
  (pencilDelta alpha beta).restrict
    (pencilDelta_mem_equivariantTarget rhoW rho2 rho3 rho4 alpha beta hAlpha hBeta)

@[simp] theorem pencilDeltaEquivariant_apply
    (X : pencilEquivariantDomain rho2 rho3 rho4) :
    (pencilDeltaEquivariant rhoW rho2 rho3 rho4 alpha beta hAlpha hBeta X :
      T0 R W M2 M3 M4) = pencilDelta alpha beta (X : D0 R M2 M3 M4) := rfl

/-- The restricted kernel is the pullback of the generic commutant. -/
theorem ker_pencilDeltaEquivariant :
    LinearMap.ker (pencilDeltaEquivariant rhoW rho2 rho3 rho4 alpha beta hAlpha hBeta) =
      (pencilCommutant alpha beta).comap
        (pencilEquivariantDomain rho2 rho3 rho4).subtype := by
  unfold pencilDeltaEquivariant pencilCommutant
  exact LinearMap.ker_restrict _

theorem mem_ker_pencilDeltaEquivariant_iff
    (X : pencilEquivariantDomain rho2 rho3 rho4) :
    X ∈ LinearMap.ker
      (pencilDeltaEquivariant rhoW rho2 rho3 rho4 alpha beta hAlpha hBeta) ↔
    (X : D0 R M2 M3 M4) ∈ pencilCommutant alpha beta := by
  rw [ker_pencilDeltaEquivariant]
  rfl

/-- An ambient triple is in the kernel image exactly when it is both commuting
and equivariant. The latter condition concerns all three endomorphisms. -/
theorem mem_map_ker_pencilDeltaEquivariant_iff (X : D0 R M2 M3 M4) :
    X ∈ (LinearMap.ker
      (pencilDeltaEquivariant rhoW rho2 rho3 rho4 alpha beta hAlpha hBeta)).map
        (pencilEquivariantDomain rho2 rho3 rho4).subtype ↔
    X ∈ pencilCommutant alpha beta ∧
      X ∈ pencilEquivariantDomain rho2 rho3 rho4 := by
  rw [ker_pencilDeltaEquivariant, Submodule.map_comap_subtype, Submodule.mem_inf]
  exact and_comm

/-- Both pencil equations hold for every W input, together with all three
pointwise equivariance conditions for every monoid element and module input. -/
theorem mem_map_ker_pencilDeltaEquivariant_iff_tmul (X : D0 R M2 M3 M4) :
    X ∈ (LinearMap.ker
      (pencilDeltaEquivariant rhoW rho2 rho3 rho4 alpha beta hAlpha hBeta)).map
        (pencilEquivariantDomain rho2 rho3 rho4).subtype ↔
    ((∀ (w : W) (v : M2),
        X.2.1 (alpha (w ⊗ₜ[R] v)) = alpha (w ⊗ₜ[R] X.1 v)) ∧
      (∀ (w : W) (v : M3),
        X.2.2 (beta (w ⊗ₜ[R] v)) = beta (w ⊗ₜ[R] X.2.1 v))) ∧
    ((∀ (g : G) (v : M2), X.1 (rho2 g v) = rho2 g (X.1 v)) ∧
      (∀ (g : G) (v : M3), X.2.1 (rho3 g v) = rho3 g (X.2.1 v)) ∧
      (∀ (g : G) (v : M4), X.2.2 (rho4 g v) = rho4 g (X.2.2 v))) := by
  rw [mem_map_ker_pencilDeltaEquivariant_iff,
    mem_pencilCommutant_iff_tmul, mem_pencilEquivariantDomain_iff,
    mem_equivariantHom_iff_apply, mem_equivariantHom_iff_apply,
    mem_equivariantHom_iff_apply]

end OAI.HorrocksMumford
