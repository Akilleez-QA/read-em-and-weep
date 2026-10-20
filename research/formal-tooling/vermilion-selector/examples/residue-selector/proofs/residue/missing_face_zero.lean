import Vermilion.Obligations
import residue.Evidence

set_option linter.unusedVariables false
set_option linter.style.nameCheck false
set_option linter.dupNamespace false

namespace residue.missing_face_zero

-- vrml:begin residue.missing_face_zero.ensures_1 882c66ea6eff9c14
/--
Generated VC `residue.missing_face_zero.ensures_1`.

- Rust source: `examples/residue-selector/residue.rs:19:13-19:19`
- Rust/SST construct: function postcondition (`ensures`)
- AssertId: `1`
- Statement hash: `882c66ea6eff9c14`
-/
def ensures_1_meta : Vermilion.ObligationMeta := {
  rustFile := "examples/residue-selector/residue.rs"
  startLine := 19
  startColumn := 13
  endLine := 19
  endColumn := 19
  assertId := "1"
  functionName := "residue.missing_face_zero"
  kind := "ensures"
  statementHash := "882c66ea6eff9c14"
}
@[vrml_obligation] theorem ensures_1
    (e0 : Int)
    (e1 : Int)
    (e2 : Int)
    (e3 : Int)
    (e4 : Int)
    (coefficient : Int)
    (requires_0 : Vermilion.inSignedRange 64 e0)
    (requires_1 : Vermilion.inSignedRange 64 e1)
    (requires_2 : Vermilion.inSignedRange 64 e2)
    (requires_3 : Vermilion.inSignedRange 64 e3)
    (requires_4 : Vermilion.inSignedRange 64 e4)
    (requires_5 : Vermilion.inSignedRange 64 coefficient)
    (requires_6 : e0 ≥ 0)
    (assume_7 : Vermilion.inSignedRange 64 (Vermilion.iteP (((((e0 = (0 - 1)) ∧ (e1 = (0 - 1))) ∧ (e2 = (0 - 1))) ∧ (e3 = (0 - 1))) ∧ (e4 = (0 - 1))) coefficient 0)) :
    (Vermilion.iteP (((((e0 = (0 - 1)) ∧ (e1 = (0 - 1))) ∧ (e2 = (0 - 1))) ∧ (e3 = (0 - 1))) ∧ (e4 = (0 - 1))) coefficient 0) = 0 := by
  vrml
-- vrml:end residue.missing_face_zero.ensures_1

end residue.missing_face_zero

