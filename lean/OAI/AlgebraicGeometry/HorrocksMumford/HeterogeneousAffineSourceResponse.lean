module

public import Mathlib.Algebra.Module.Submodule.Ker
public import Mathlib.Tactic.Abel

/-!
# Conditional heterogeneous affine source response

Credit: PR815, commit `0eaeca734b9e17142da2f1bdfd9a1721d0bb1d42`,
equations (13), (14), (16), and (20)–(24). The supplied proof note has SHA-256
`78a0f462ffd0710d248658aaf95926f926297b0bae43aade85eb4c7fc934d236`.

The trace modules model degree twelve / physical twist six, and the norm
modules model degree sixteen / physical twist fourteen; no graded spaces
are constructed here. The source module is supplied independently, and is
not identified with a differential's range. These are conditional overlap
identities, with no global gluing, exclusion, or main proof-repair claim.
-/

set_option autoImplicit false

@[expose] public section

namespace OAI.HorrocksMumford

universe uR uP uTi uTj uNi uNj

variable {R : Type uR} [Ring R]
variable {P : Type uP} [AddCommGroup P] [Module R P]
variable {Ti : Type uTi} [AddCommGroup Ti] [Module R Ti]
variable {Tj : Type uTj} [AddCommGroup Tj] [Module R Tj]
variable {Ni : Type uNi} [AddCommGroup Ni] [Module R Ni]
variable {Nj : Type uNj} [AddCommGroup Nj] [Module R Nj]

/-- A local norm response to a supplied source, with a distinct trace target. -/
def affineSourceNormResponse (μ : Ti →ₗ[R] Ni) (L : P →ₗ[R] Ti)
    (Q : Ni) (y : Ti) (s : P) : Ni :=
  Q + μ (y - L s)

variable (μi : Ti →ₗ[R] Ni) (μj : Tj →ₗ[R] Nj)
variable (g : Tj →ₗ[R] Ti) (h : Nj →ₗ[R] Ni)
variable (Li : P →ₗ[R] Ti) (Lj : P →ₗ[R] Tj)
variable (Qi : Ni) (Qj : Nj) (f yi : Ti) (yj : Tj) (s : P)

/-- The exact target-minus-transport norm defect, retaining the affine shift. -/
theorem affineSourceNormResponse_defect
    (htransport : μi.comp g = h.comp μj)
    (hshift : h Qj - Qi = μi f) :
    affineSourceNormResponse μi Li Qi yi s -
        h (affineSourceNormResponse μj Lj Qj yj s) =
      μi (yi - Li s - g (yj - Lj s) - f) := by
  have hcomm (x : Tj) : μi (g x) = h (μj x) :=
    LinearMap.congr_fun htransport x
  simp only [affineSourceNormResponse, map_add, map_sub, hcomm]
  calc
    _ =
        (μi yi - μi (Li s) - (h (μj yj) - h (μj (Lj s)))) -
          (h Qj - Qi) := by abel
    _ = _ := by rw [hshift]

/-- Norm overlap equality is precisely membership of the trace defect in the kernel. -/
theorem affineSourceNormResponse_eq_iff_mem_ker
    (htransport : μi.comp g = h.comp μj)
    (hshift : h Qj - Qi = μi f) :
    affineSourceNormResponse μi Li Qi yi s =
        h (affineSourceNormResponse μj Lj Qj yj s) ↔
      yi - Li s - g (yj - Lj s) - f ∈ LinearMap.ker μi := by
  rw [LinearMap.mem_ker, ← sub_eq_zero,
    affineSourceNormResponse_defect μi μj g h Li Lj Qi Qj f yi yj s
      htransport hshift]

/-- Injectivity upgrades the kernel criterion to the exact source-response overlap law. -/
theorem affineSourceNormResponse_eq_iff_of_injective
    (htransport : μi.comp g = h.comp μj)
    (hshift : h Qj - Qi = μi f)
    (hinjective : Function.Injective μi) :
    affineSourceNormResponse μi Li Qi yi s =
        h (affineSourceNormResponse μj Lj Qj yj s) ↔
      Li s - g (Lj s) = yi - g yj - f := by
  rw [affineSourceNormResponse_eq_iff_mem_ker μi μj g h Li Lj Qi Qj f yi yj s
    htransport hshift, LinearMap.mem_ker]
  have hzero : μi (yi - Li s - g (yj - Lj s) - f) = 0 ↔
      yi - Li s - g (yj - Lj s) - f = 0 := by
    constructor
    · intro heq
      apply hinjective
      simpa only [map_zero] using heq
    · intro heq
      rw [heq, map_zero]
  rw [hzero]
  have htrace : yi - Li s - g (yj - Lj s) - f =
      (yi - g yj - f) - (Li s - g (Lj s)) := by
    rw [map_sub]
    abel
  rw [htrace, sub_eq_zero, eq_comm]

end OAI.HorrocksMumford
