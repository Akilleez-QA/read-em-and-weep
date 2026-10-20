import Vermilion.Obligations

set_option linter.unusedVariables false
set_option linter.style.nameCheck false
set_option linter.dupNamespace false

namespace intro_wrong.increment

-- vrml:begin intro_wrong.increment.assert_0 0921af6002162b46
/--
Generated VC `intro_wrong.increment.assert_0`.

- Rust source: `examples/residue-selector/intro_wrong.rs:10:13-10:18`
- Rust/SST construct: possible arithmetic underflow/overflow
- AssertId: `0`
- Statement hash: `0921af6002162b46`
-/
def assert_0_meta : Vermilion.ObligationMeta := {
  rustFile := "examples/residue-selector/intro_wrong.rs"
  startLine := 10
  startColumn := 13
  endLine := 10
  endColumn := 18
  assertId := "0"
  functionName := "intro_wrong.increment"
  kind := "assert"
  statementHash := "0921af6002162b46"
}
@[vrml_obligation] theorem assert_0
    (x : Int)
    (requires_0 : Vermilion.inUnsignedRange 32 x)
    (requires_1 : x < 100) :
    Vermilion.inUnsignedRange 32 (x + 1) := by
  vrml
-- vrml:end intro_wrong.increment.assert_0

-- vrml:begin intro_wrong.increment.assert_1 e456b18eee1fd113
/--
Generated VC `intro_wrong.increment.assert_1`.

- Rust source: `examples/residue-selector/intro_wrong.rs:11:12-11:17`
- Rust/SST construct: Rust source assertion
- AssertId: `1`
- Statement hash: `e456b18eee1fd113`
-/
def assert_1_meta : Vermilion.ObligationMeta := {
  rustFile := "examples/residue-selector/intro_wrong.rs"
  startLine := 11
  startColumn := 12
  endLine := 11
  endColumn := 17
  assertId := "1"
  functionName := "intro_wrong.increment"
  kind := "assert"
  statementHash := "e456b18eee1fd113"
}
@[vrml_obligation] theorem assert_1
    (x : Int)
    (requires_0 : Vermilion.inUnsignedRange 32 x)
    (requires_1 : x < 100)
    (assert_0 : Vermilion.inUnsignedRange 32 (x + 1)) :
    ((x + 1) % 4294967296) > 0 := by
  vrml
-- vrml:end intro_wrong.increment.assert_1

-- vrml:begin intro_wrong.increment.ensures_2 2a236a9cf7f2eaac
/--
Generated VC `intro_wrong.increment.ensures_2`.

- Rust source: `examples/residue-selector/intro_wrong.rs:8:13-8:23`
- Rust/SST construct: function postcondition (`ensures`)
- AssertId: `2`
- Statement hash: `2a236a9cf7f2eaac`
-/
def ensures_2_meta : Vermilion.ObligationMeta := {
  rustFile := "examples/residue-selector/intro_wrong.rs"
  startLine := 8
  startColumn := 13
  endLine := 8
  endColumn := 23
  assertId := "2"
  functionName := "intro_wrong.increment"
  kind := "ensures"
  statementHash := "2a236a9cf7f2eaac"
}
@[vrml_obligation] theorem ensures_2
    (x : Int)
    (requires_0 : Vermilion.inUnsignedRange 32 x)
    (requires_1 : x < 100)
    (assert_0 : Vermilion.inUnsignedRange 32 (x + 1))
    (assert_1 : ((x + 1) % 4294967296) > 0) :
    ((x + 1) % 4294967296) = (x + 2) := by
  vrml
-- vrml:end intro_wrong.increment.ensures_2

end intro_wrong.increment

