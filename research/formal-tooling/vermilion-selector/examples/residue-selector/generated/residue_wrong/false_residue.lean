import Vermilion.Obligations

set_option linter.unusedVariables false
set_option linter.style.nameCheck false
set_option linter.dupNamespace false

namespace residue_wrong.false_residue

-- vrml:begin residue_wrong.false_residue.ensures_0 062f94c1f3f3fe66
/--
Generated VC `residue_wrong.false_residue.ensures_0`.

- Rust source: `examples/residue-selector/residue_wrong.rs:5:13-5:19`
- Rust/SST construct: function postcondition (`ensures`)
- AssertId: `0`
- Statement hash: `062f94c1f3f3fe66`
-/
def ensures_0_meta : Vermilion.ObligationMeta := {
  rustFile := "examples/residue-selector/residue_wrong.rs"
  startLine := 5
  startColumn := 13
  endLine := 5
  endColumn := 19
  assertId := "0"
  functionName := "residue_wrong.false_residue"
  kind := "ensures"
  statementHash := "062f94c1f3f3fe66"
}
@[vrml_obligation] theorem ensures_0
    (coefficient : Int)
    (requires_0 : Vermilion.inSignedRange 64 coefficient) :
    coefficient = 0 := by
  vrml
-- vrml:end residue_wrong.false_residue.ensures_0

end residue_wrong.false_residue

