module

public import Mathlib.Algebra.Module.LinearMap.Defs

/-!
# Universal frame transitions and defect cocycles

Section 2 of null's PR816 proof note, commit
`eed6010347fcebc21aef30413b0e1da3be68a9b4`, SHA-256
`5f2069fe845df87caa3a4bdb1c2bd7434ff6513bddda5bc21f54f042a04a4e84`.
These are typed linear algebra identities; no geometric contraction is constructed.
-/

set_option autoImplicit false

@[expose] public section

namespace OAI.HorrocksMumford

variable {R : Type*} [Ring R]
variable {Kminus Kzero Kplus Ha Hb Hc : Type*}
variable [AddCommGroup Kminus] [Module R Kminus]
variable [AddCommGroup Kzero] [Module R Kzero]
variable [AddCommGroup Kplus] [Module R Kplus]
variable [AddCommGroup Ha] [Module R Ha]
variable [AddCommGroup Hb] [Module R Hb]
variable [AddCommGroup Hc] [Module R Hc]

/-- The middle-frame retraction homotopy gives transition composition. -/
theorem frameTransition_comp
    (dm : Kminus →ₗ[R] Kzero) (d0 : Kzero →ₗ[R] Kplus)
    (h0 : Kzero →ₗ[R] Kminus) (h1 : Kplus →ₗ[R] Kzero)
    (ia : Ha →ₗ[R] Kzero) (ib : Hb →ₗ[R] Kzero)
    (pb : Kzero →ₗ[R] Hb) (pc : Kzero →ₗ[R] Hc)
    (homotopy : dm.comp h0 + h1.comp d0 = LinearMap.id - ib.comp pb)
    (closed_i : d0.comp ia = 0) (closed_p : pc.comp dm = 0) :
    (pc.comp ib).comp (pb.comp ia) = pc.comp ia := by
  apply LinearMap.ext
  intro x
  have hi : d0 (ia x) = 0 := DFunLike.congr_fun closed_i x
  have hp : pc (dm (h0 (ia x))) = 0 :=
    DFunLike.congr_fun closed_p (h0 (ia x))
  have h := congrArg (fun y => pc y) (DFunLike.congr_fun homotopy (ia x))
  have hz : 0 = pc (ia x) - pc (ib (pb (ia x))) := by
    simpa only [LinearMap.add_apply, LinearMap.sub_apply, LinearMap.comp_apply,
      LinearMap.id_apply, map_add, map_sub, hi, map_zero, hp, zero_add] using h
  exact (sub_eq_zero.mp hz.symm).symm

/-- Retractions and a homotopy in each frame give both inverse orders. -/
theorem frameTransition_inversePair
    (dm : Kminus →ₗ[R] Kzero) (d0 : Kzero →ₗ[R] Kplus)
    (ha0 hb0 : Kzero →ₗ[R] Kminus) (ha1 hb1 : Kplus →ₗ[R] Kzero)
    (ia : Ha →ₗ[R] Kzero) (ib : Hb →ₗ[R] Kzero)
    (pa : Kzero →ₗ[R] Ha) (pb : Kzero →ₗ[R] Hb)
    (homotopy_a : dm.comp ha0 + ha1.comp d0 = LinearMap.id - ia.comp pa)
    (homotopy_b : dm.comp hb0 + hb1.comp d0 = LinearMap.id - ib.comp pb)
    (closed_ia : d0.comp ia = 0) (closed_ib : d0.comp ib = 0)
    (closed_pa : pa.comp dm = 0) (closed_pb : pb.comp dm = 0)
    (retract_a : pa.comp ia = LinearMap.id)
    (retract_b : pb.comp ib = LinearMap.id) :
    (pa.comp ib).comp (pb.comp ia) = LinearMap.id ∧
      (pb.comp ia).comp (pa.comp ib) = LinearMap.id := by
  constructor
  · exact (frameTransition_comp dm d0 hb0 hb1 ia ib pb pa
      homotopy_b closed_ia closed_pa).trans retract_a
  · exact (frameTransition_comp dm d0 ha0 ha1 ib ia pa pb
      homotopy_a closed_ib closed_pb).trans retract_b

variable {Ca Cb Cc Da Db Dc : Type*}
variable [AddCommGroup Ca] [Module R Ca]
variable [AddCommGroup Cb] [Module R Cb]
variable [AddCommGroup Cc] [Module R Cc]
variable [AddCommGroup Da] [Module R Da]
variable [AddCommGroup Db] [Module R Db]
variable [AddCommGroup Dc] [Module R Dc]

/-- Arbitrary transfers have the typed defect triple-overlap law. -/
theorem frameTransfer_defectCocycle
    (gCba : Ca →ₗ[R] Cb) (gCcb : Cb →ₗ[R] Cc) (gCca : Ca →ₗ[R] Cc)
    (gDba : Da →ₗ[R] Db) (gDcb : Db →ₗ[R] Dc) (gDca : Da →ₗ[R] Dc)
    (Ma : Ca →ₗ[R] Da) (Mb : Cb →ₗ[R] Db) (Mc : Cc →ₗ[R] Dc)
    (cocycle_C : gCcb.comp gCba = gCca)
    (cocycle_D : gDcb.comp gDba = gDca) :
    Mc.comp gCca - gDca.comp Ma =
      (Mc.comp gCcb - gDcb.comp Mb).comp gCba +
        gDcb.comp (Mb.comp gCba - gDba.comp Ma) := by
  rw [LinearMap.sub_comp, LinearMap.comp_sub]
  rw [LinearMap.comp_assoc, cocycle_C]
  rw [← LinearMap.comp_assoc Ma gDba gDcb, cocycle_D]
  rw [LinearMap.comp_assoc gCba Mb gDcb]
  let A := Mc.comp gCca
  let B := gDcb.comp (Mb.comp gCba)
  let C := gDca.comp Ma
  change A - C = (A - B) + (B - C)
  calc
    A - C = A + (-B + B) - C := by rw [neg_add_cancel, add_zero]
    _ = (A - B) + (B - C) := by simp only [sub_eq_add_neg, add_assoc]

end OAI.HorrocksMumford
