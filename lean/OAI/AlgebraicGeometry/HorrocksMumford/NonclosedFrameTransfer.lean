/-
Supporting algebra draft. Source: null's PR816, pinned at
 eed6010347fcebc21aef30413b0e1da3be68a9b4.
Proof SHA-256: 5f2069fe845df87caa3a4bdb1c2bd7434ff6513bddda5bc21f54f042a04a4e84.
-/
module

public import Mathlib.Algebra.Module.LinearMap.Defs
public import Mathlib.Tactic.Abel

set_option autoImplicit false

@[expose] public section

namespace OAI.HorrocksMumford

variable {R : Type*} [Ring R]
variable {Cminus Czero Cplus Dminus Dzero Dplus HCa HCb HDa HDb : Type*}
variable [AddCommGroup Cminus] [Module R Cminus]
  [AddCommGroup Czero] [Module R Czero]
  [AddCommGroup Cplus] [Module R Cplus]
  [AddCommGroup Dminus] [Module R Dminus]
  [AddCommGroup Dzero] [Module R Dzero]
  [AddCommGroup Dplus] [Module R Dplus]
  [AddCommGroup HCa] [Module R HCa]
  [AddCommGroup HCb] [Module R HCb]
  [AddCommGroup HDa] [Module R HDa]
  [AddCommGroup HDb] [Module R HDb]

variable (dCm : Cminus →ₗ[R] Czero) (dC0 : Czero →ₗ[R] Cplus)
  (dDm : Dminus →ₗ[R] Dzero) (dD0 : Dzero →ₗ[R] Dplus)
  (hCb0 : Czero →ₗ[R] Cminus) (hCb1 : Cplus →ₗ[R] Czero)
  (hDa0 : Dzero →ₗ[R] Dminus) (hDa1 : Dplus →ₗ[R] Dzero)
  (iCa : HCa →ₗ[R] Czero) (iCb : HCb →ₗ[R] Czero)
  (pCb : Czero →ₗ[R] HCb) (iDa : HDa →ₗ[R] Dzero)
  (pDa : Dzero →ₗ[R] HDa) (pDb : Dzero →ₗ[R] HDb)
  (Em : Cminus →ₗ[R] Dminus) (E0 : Czero →ₗ[R] Dzero)
  (Ep : Cplus →ₗ[R] Dplus)

/-- PR816 equation (1), as a degree-zero component identity with four hypotheses.
Both defect terms are positive; no normalized contraction or closedness of E is assumed. -/
theorem nonclosedFrameTransfer
    (hC : dCm.comp hCb0 + hCb1.comp dC0 = LinearMap.id - iCb.comp pCb)
    (hD : dDm.comp hDa0 + hDa1.comp dD0 = LinearMap.id - iDa.comp pDa)
    (hCi : dC0.comp iCa = 0)
    (hDp : pDb.comp dDm = 0) :
    ((pDb.comp E0).comp iCb).comp (pCb.comp iCa)
      - (pDb.comp iDa).comp ((pDa.comp E0).comp iCa)
      = (pDb.comp
          (((dDm.comp Em - E0.comp dCm).comp hCb0)
            + hDa1.comp (dD0.comp E0 - Ep.comp dC0))).comp iCa := by
  apply LinearMap.ext
  intro x
  have hci : dC0 (iCa x) = 0 := by
    simpa only [LinearMap.comp_apply, LinearMap.zero_apply] using
      congrArg (fun f : HCa →ₗ[R] Cplus => f x) hCi
  have hdp (y : Dminus) : pDb (dDm y) = 0 := by
    simpa only [LinearMap.comp_apply, LinearMap.zero_apply] using
      congrArg (fun f : Dminus →ₗ[R] HDb => f y) hDp
  have hc := congrArg (fun f : Czero →ₗ[R] Czero => f (iCa x)) hC
  simp only [LinearMap.add_apply, LinearMap.comp_apply, LinearMap.sub_apply,
    LinearMap.id_apply, hci, map_zero, add_zero] at hc
  have hc' : iCb (pCb (iCa x)) = iCa x - dCm (hCb0 (iCa x)) := by
    apply eq_sub_iff_add_eq.mpr
    simpa only [add_comm] using eq_sub_iff_add_eq.mp hc
  have hd := congrArg (fun f : Dzero →ₗ[R] Dzero => pDb (f (E0 (iCa x)))) hD
  simp only [LinearMap.add_apply, LinearMap.comp_apply, LinearMap.sub_apply,
    LinearMap.id_apply, map_add, map_sub, hdp, zero_add] at hd
  have hd' : pDb (iDa (pDa (E0 (iCa x)))) =
      pDb (E0 (iCa x)) - pDb (hDa1 (dD0 (E0 (iCa x)))) := by
    apply eq_sub_iff_add_eq.mpr
    simpa only [add_comm] using eq_sub_iff_add_eq.mp hd
  simp only [LinearMap.sub_apply, LinearMap.comp_apply, LinearMap.add_apply,
    hc', hd', map_sub, map_add, hci, map_zero, sub_zero, hdp]
  abel

/-- The typed zero-defect limit; this does not assert global descent. -/
theorem nonclosedFrameTransfer_closed
    (hC : dCm.comp hCb0 + hCb1.comp dC0 = LinearMap.id - iCb.comp pCb)
    (hD : dDm.comp hDa0 + hDa1.comp dD0 = LinearMap.id - iDa.comp pDa)
    (hCi : dC0.comp iCa = 0)
    (hDp : pDb.comp dDm = 0)
    (hTm : dDm.comp Em - E0.comp dCm = 0)
    (hT0 : dD0.comp E0 - Ep.comp dC0 = 0) :
    ((pDb.comp E0).comp iCb).comp (pCb.comp iCa)
      = (pDb.comp iDa).comp ((pDa.comp E0).comp iCa) := by
  have h := nonclosedFrameTransfer dCm dC0 dDm dD0 hCb0 hCb1 hDa0 hDa1
    iCa iCb pCb iDa pDa pDb Em E0 Ep hC hD hCi hDp
  rw [hTm, hT0] at h
  apply sub_eq_zero.mp
  simpa using h

/-- Closed inclusion and projection kill exact degree-zero cochains. -/
theorem nonclosedFrameTransfer_exactProjection
    (K0 : Czero →ₗ[R] Dminus) (K1 : Cplus →ₗ[R] Dzero)
    (hCi : dC0.comp iCa = 0) (hDp : pDb.comp dDm = 0) :
    (pDb.comp (dDm.comp K0 + K1.comp dC0)).comp iCa = 0 := by
  apply LinearMap.ext
  intro x
  have hci : dC0 (iCa x) = 0 := by
    simpa only [LinearMap.comp_apply, LinearMap.zero_apply] using
      congrArg (fun f : HCa →ₗ[R] Cplus => f x) hCi
  have hdp : pDb (dDm (K0 (iCa x))) = 0 := by
    simpa only [LinearMap.comp_apply, LinearMap.zero_apply] using
      congrArg (fun f : Dminus →ₗ[R] HDb => f (K0 (iCa x))) hDp
  simp only [LinearMap.comp_apply, LinearMap.add_apply, LinearMap.zero_apply,
    map_add, hci, map_zero, hdp, add_zero]

end OAI.HorrocksMumford

#print axioms OAI.HorrocksMumford.nonclosedFrameTransfer
#print axioms OAI.HorrocksMumford.nonclosedFrameTransfer_closed
#print axioms OAI.HorrocksMumford.nonclosedFrameTransfer_exactProjection
