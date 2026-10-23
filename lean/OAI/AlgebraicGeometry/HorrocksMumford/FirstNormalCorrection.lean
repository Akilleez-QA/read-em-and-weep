module

public import Mathlib.LinearAlgebra.Matrix.Notation
public import Mathlib.LinearAlgebra.Matrix.Trace
public import Mathlib.Tactic.FieldSimp
public import Mathlib.Tactic.Ring.Basic

/-!
Supporting algebra for Lean 4.34.1 and mathlib
 d13f23b723b8a846827a245b89c10fc7d3f11612.
Supporting universal matrix identities for equations (10) and (15) of the
pinned affine-square-source-response proof. No geometric gluing is asserted.
-/

set_option autoImplicit false

@[expose] public section

namespace OAI.HorrocksMumford

/-- Lower triangular reference frame; `alpha` and `delta` are frame scalars. -/
def referenceFrame {K : Type*} [Field K] (alpha c delta : K) : Matrix (Fin 2) (Fin 2) K :=
  !![alpha, 0; c, delta]

/-- Explicit inverse, used only with both diagonal frame scalars nonzero. -/
def referenceFrameInv {K : Type*} [Field K] (alpha c delta : K) :
    Matrix (Fin 2) (Fin 2) K :=
  !![1 / alpha, 0; -c / (alpha * delta), 1 / delta]

/-- First normal transition generator. -/
def normalGenerator {K : Type*} [Field K] (t ell : K) : Matrix (Fin 2) (Fin 2) K :=
  !![t, 0; ell, -t]

/-- An arbitrary matrix in the displayed trace-zero form; no entry is suppressed. -/
def tracelessInput {K : Type*} [Field K] (x y z : K) : Matrix (Fin 2) (Fin 2) K :=
  !![x, y; z, -x]

 theorem referenceFrame_mul_inv {K : Type*} [Field K] (alpha c delta : K)
    (ha : alpha ≠ 0) (hd : delta ≠ 0) :
    referenceFrame alpha c delta * referenceFrameInv alpha c delta = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [referenceFrame, referenceFrameInv, Matrix.mul_apply, Fin.sum_univ_succ] <;>
    field_simp [ha, hd] <;> ring1

 theorem referenceFrame_inv_mul {K : Type*} [Field K] (alpha c delta : K)
    (ha : alpha ≠ 0) (hd : delta ≠ 0) :
    referenceFrameInv alpha c delta * referenceFrame alpha c delta = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [referenceFrame, referenceFrameInv, Matrix.mul_apply, Fin.sum_univ_succ] <;>
    field_simp [ha, hd] <;> ring1

/-- Equation (10), including all four entries. No characteristic assumption is needed.
The two nonzero assumptions concern frame units, not the geometric source `a`. -/
 theorem conjugated_commutator {K : Type*} [Field K]
    (alpha c delta t ell x y z : K) (ha : alpha ≠ 0) (hd : delta ≠ 0) :
    referenceFrame alpha c delta *
        (normalGenerator t ell * tracelessInput x y z -
          tracelessInput x y z * normalGenerator t ell) *
        referenceFrameInv alpha c delta =
      !![-(ell + 2 * c * t / delta) * y, 2 * alpha * t * y / delta;
         2 * delta * ell * x / alpha - 2 * delta * t * z / alpha -
           2 * c * ell * y / alpha - 2 * c ^ 2 * t * y / (alpha * delta),
         (ell + 2 * c * t / delta) * y] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [referenceFrame, referenceFrameInv, normalGenerator, tracelessInput,
      Matrix.mul_apply, Fin.sum_univ_succ] <;>
    field_simp [ha, hd] <;> ring1

/-- Equation (15) without its scalar `q` factor: valid for arbitrary matrices over
any commutative ring, without trace-zero or invertibility hypotheses. -/
 theorem trace_mul_commutator {R : Type*} [CommRing R]
    (L Z : Matrix (Fin 2) (Fin 2) R) :
    Matrix.trace (L * (Z * L - L * Z)) = 0 := by
  rw [mul_sub, Matrix.trace_sub]
  exact sub_eq_zero.mpr (Matrix.trace_mul_cycle' L Z L)

end OAI.HorrocksMumford
