module

public import OAI.AlgebraicGeometry.HorrocksMumford.HeterogeneousAffineSourceResponse
public import Mathlib.Algebra.Module.Submodule.Range

/-!
# Conditional normalization comparison in one aligned ambient frame

Supporting algebra from PR866, commit 25b1d2927294fffbc393e6ac2285f5a58cfd6c60,
PROOF.md SHA256 a7f6afe41fe569cb9a061a047b1d0a140fd198950cda6fe3bace6978f3cf0b14.
Only supplied linear maps and certificates are used; physical authentication
and alignment are assumptions. No overlap/cocycle theorem is duplicated.
-/

set_option autoImplicit false

@[expose] public section

namespace OAI.HorrocksMumford

universe uR uC uG uL uV uT uN

variable {R : Type uR} [Ring R]
variable {C0 : Type uC} [AddCommGroup C0] [Module R C0]
variable {Dg : Type uG} [AddCommGroup Dg] [Module R Dg]
variable {Dloc : Type uL} [AddCommGroup Dloc] [Module R Dloc]
variable {V4 : Type uV} [AddCommGroup V4] [Module R V4]
variable {Tr : Type uT} [AddCommGroup Tr] [Module R Tr]
variable {Nm : Type uN} [AddCommGroup Nm] [Module R Nm]

/-- Full global rows descend to the comparison on every differential-image element. -/
theorem mixedNormalization_range_comparison
    (d : C0 →ₗ[R] Dg) (loc : Dg →ₗ[R] Dloc) (delta : Dloc →ₗ[R] Tr)
    (LA LB : LinearMap.range d →ₗ[R] Tr) (ellA ellB : C0 →ₗ[R] Tr)
    (hA : ∀ x, LA (d.rangeRestrict x) = ellA x)
    (hB : ∀ x, LB (d.rangeRestrict x) = ellB x)
    (hrows : ∀ x, ellB x - ellA x = delta (loc (d x))) :
    ∀ t : LinearMap.range d, LB t - LA t = delta (loc t.val) := by
  intro t
  obtain ⟨x, hx⟩ := LinearMap.mem_range.mp t.property
  have ht : d.rangeRestrict x = t := Subtype.ext hx
  rw [← ht, hB, hA]
  exact hrows x

/-- Supplied data in one aligned frame. `qW` is already the correct-twist product.
`LA` and `LB` accept only the differential image; `R4` accepts all local maps. -/
structure MixedNormalizationAdapter
    (d : C0 →ₗ[R] Dg) (loc : Dg →ₗ[R] Dloc)
    (R4 : Dloc →ₗ[R] V4) (coneTau : V4 →ₗ[R] Tr)
    (LA LB : LinearMap.range d →ₗ[R] Tr) (mu : Tr →ₗ[R] Nm) where
  S : Dg
  qW : Dg
  hT : S - qW ∈ LinearMap.range d
  yA : Tr
  yB : Tr
  Q : Nm
  comparison : ∀ t : LinearMap.range d,
    LB t - LA t = (coneTau.comp R4) (loc t.val)
  cone_qW : (coneTau.comp R4) (loc qW) = 0
  lower_jet : yB - yA = (coneTau.comp R4) (loc (S - qW))

namespace MixedNormalizationAdapter

variable {d : C0 →ₗ[R] Dg} {loc : Dg →ₗ[R] Dloc}
variable {R4 : Dloc →ₗ[R] V4} {coneTau : V4 →ₗ[R] Tr}
variable {LA LB : LinearMap.range d →ₗ[R] Tr} {mu : Tr →ₗ[R] Nm}
variable (A : MixedNormalizationAdapter d loc R4 coneTau LA LB mu)

/-- Cone restriction followed by trace extraction. -/
def delta : Dloc →ₗ[R] Tr := coneTau.comp R4

/-- The certified corrected source, with its image membership retained. -/
def t : LinearMap.range d := ⟨A.S - A.qW, A.hT⟩

/-- The normalization error in the independent trace module. -/
def eta : Tr := (coneTau.comp R4) (loc A.t.val)

/-- Paired response for A. -/
def rhoAA : Nm := affineSourceNormResponse mu LA A.Q A.yA A.t

/-- Mixed response: lower data from A, source row from B. -/
def rhoAB : Nm := affineSourceNormResponse mu LB A.Q A.yA A.t

/-- Paired response for B with the same supplied lower datum Q. -/
def rhoBB : Nm := affineSourceNormResponse mu LB A.Q A.yB A.t

/-- Cone evaluation on S is legal without assuming S lies in the differential image. -/
theorem eta_source : A.eta = (coneTau.comp R4) (loc A.S) := by
  change (coneTau.comp R4) (loc (A.S - A.qW)) = _
  rw [map_sub, map_sub, A.cone_qW, sub_zero]

/-- Simultaneous normalization changes cancel in the trace combination and response. -/
theorem paired_cancellation :
    A.yB - LB A.t = A.yA - LA A.t ∧ A.rhoBB = A.rhoAA := by
  have hc : LB A.t - LA A.t = A.eta := A.comparison A.t
  have hy : A.yB - A.yA = A.eta := A.lower_jet
  have hp : A.yB - LB A.t = A.yA - LA A.t := by
    calc
      _ = (A.yB - A.yA) - (LB A.t - LA A.t) + (A.yA - LA A.t) := by abel
      _ = _ := by rw [hy, hc]; abel
  exact ⟨hp, by simp only [rhoBB, rhoAA, affineSourceNormResponse, hp]⟩

/-- The exact mixed defect and its compensating counterterm. -/
theorem mixed_defect :
    A.rhoAB - A.rhoAA = -mu A.eta ∧
      A.rhoAB + mu A.eta = A.rhoAA := by
  have hc : LB A.t - LA A.t = A.eta := A.comparison A.t
  have hm : mu (LB A.t) - mu (LA A.t) = mu A.eta := by
    rw [← map_sub, hc]
  have hd : A.rhoAB - A.rhoAA = -mu A.eta := by
    simp only [rhoAB, rhoAA, affineSourceNormResponse, map_sub]
    calc
      _ = -(mu (LB A.t) - mu (LA A.t)) := by abel
      _ = _ := by rw [hm]
  refine ⟨hd, ?_⟩
  calc
    _ = (A.rhoAB - A.rhoAA) + mu A.eta + A.rhoAA := by abel
    _ = A.rhoAA := by rw [hd]; abel

/-- No injectivity is required for the kernel matching criterion. -/
theorem mixed_eq_iff_mem_ker : A.rhoAB = A.rhoAA ↔ A.eta ∈ LinearMap.ker mu := by
  rw [LinearMap.mem_ker, ← sub_eq_zero, A.mixed_defect.1, neg_eq_zero]

/-- Injectivity on regular sections is an explicit certificate, never division. -/
theorem mixed_eq_iff_of_injective (hinj : Function.Injective mu) :
    A.rhoAB = A.rhoAA ↔ A.eta = 0 := by
  rw [A.mixed_eq_iff_mem_ker, LinearMap.mem_ker]
  constructor
  · intro h
    apply hinj
    simpa only [map_zero] using h
  · intro h
    rw [h, map_zero]

end MixedNormalizationAdapter
end OAI.HorrocksMumford
