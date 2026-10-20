import bounded
import SelectorLaurentBridge
namespace BoundedBridge
open SelectorLaurentBridge
noncomputable def selected (e0 e1 e2 e3 e4 c : Int) : Int :=
  Vermilion.iteP (guard e0 e1 e2 e3 e4) c 0
noncomputable def returnedTwo (a0 a1 a2 a3 a4 ca b0 b1 b2 b3 b4 cb : Int) : Int :=
  Vermilion.sclip 64 (selected a0 a1 a2 a3 a4 ca + selected b0 b1 b2 b3 b4 cb)
theorem selected_range (e0 e1 e2 e3 e4 c : Int)
    (hc : Vermilion.inSignedRange 64 c) :
    Vermilion.inSignedRange 64 (selected e0 e1 e2 e3 e4 c) := by
  unfold selected Vermilion.iteP
  split
  · exact hc
  · norm_num [Vermilion.inSignedRange]
theorem two_term_residue (a0 a1 a2 a3 a4 ca b0 b1 b2 b3 b4 cb : Int)
    (ha0 : Vermilion.inSignedRange 64 a0)
    (ha1 : Vermilion.inSignedRange 64 a1)
    (ha2 : Vermilion.inSignedRange 64 a2)
    (ha3 : Vermilion.inSignedRange 64 a3)
    (ha4 : Vermilion.inSignedRange 64 a4)
    (hca : Vermilion.inSignedRange 64 ca)
    (hb0 : Vermilion.inSignedRange 64 b0)
    (hb1 : Vermilion.inSignedRange 64 b1)
    (hb2 : Vermilion.inSignedRange 64 b2)
    (hb3 : Vermilion.inSignedRange 64 b3)
    (hb4 : Vermilion.inSignedRange 64 b4)
    (hcb : Vermilion.inSignedRange 64 cb)
    (hcaBound : -4611686018427387903 ≤ ca ∧ ca ≤ 4611686018427387903)
    (hcbBound : -4611686018427387903 ≤ cb ∧ cb ≤ 4611686018427387903) :
    returnedTwo a0 a1 a2 a3 a4 ca b0 b1 b2 b3 b4 cb = ResidueBridge.residue (ResidueBridge.interpret
      [(exponent a0 a1 a2 a3 a4, ca), (exponent b0 b1 b2 b3 b4, cb)]) := by
  have ra := selected_range a0 a1 a2 a3 a4 ca hca
  have rb := selected_range b0 b1 b2 b3 b4 cb hcb
  have safe := bounded.residue_two.assert_2 a0 a1 a2 a3 a4 ca b0 b1 b2 b3 b4 cb
    ha0 ha1 ha2 ha3 ha4 hca hb0 hb1 hb2 hb3 hb4 hcb hcaBound hcbBound ra rb
  have post := bounded.residue_two.ensures_3 a0 a1 a2 a3 a4 ca b0 b1 b2 b3 b4 cb
    ha0 ha1 ha2 ha3 ha4 hca hb0 hb1 hb2 hb3 hb4 hcb hcaBound hcbBound ra rb safe
  change returnedTwo a0 a1 a2 a3 a4 ca b0 b1 b2 b3 b4 cb = selected a0 a1 a2 a3 a4 ca + selected b0 b1 b2 b3 b4 cb at post
  rw [post]
  simp only [selected, Vermilion.iteP, guard_iff_exponent]
  simp [ResidueBridge.residue, ResidueBridge.interpret, Finsupp.single_apply]
end BoundedBridge
#print axioms BoundedBridge.two_term_residue
#print BoundedBridge.two_term_residue
