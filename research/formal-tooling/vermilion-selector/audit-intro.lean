import Vermilion.Obligations

-- Original proof twin: examples/m1-pipeline/proofs/simple/increment.lean

set_option linter.unusedVariables false
set_option linter.style.nameCheck false
set_option linter.dupNamespace false

namespace simple.increment

-- vrml:begin simple.increment.assert_0 0921af6002162b46
/--
Generated VC `simple.increment.assert_0`.

- Rust source: `examples/m1-pipeline/simple.rs:10:13-10:18`
- Rust/SST construct: possible arithmetic underflow/overflow
- AssertId: `0`
- Statement hash: `0921af6002162b46`
-/
def assert_0_meta : Vermilion.ObligationMeta := {
  rustFile := "examples/m1-pipeline/simple.rs"
  startLine := 10
  startColumn := 13
  endLine := 10
  endColumn := 18
  assertId := "0"
  functionName := "simple.increment"
  kind := "assert"
  statementHash := "0921af6002162b46"
}
@[vrml_obligation] theorem assert_0
    (x : Int)
    (requires_0 : Vermilion.inUnsignedRange 32 x)
    (requires_1 : x < 100) :
    Vermilion.inUnsignedRange 32 (x + 1) := by
  vrml
-- vrml:end simple.increment.assert_0

-- vrml:begin simple.increment.assert_1 e456b18eee1fd113
/--
Generated VC `simple.increment.assert_1`.

- Rust source: `examples/m1-pipeline/simple.rs:11:12-11:17`
- Rust/SST construct: Rust source assertion
- AssertId: `1`
- Statement hash: `e456b18eee1fd113`
-/
def assert_1_meta : Vermilion.ObligationMeta := {
  rustFile := "examples/m1-pipeline/simple.rs"
  startLine := 11
  startColumn := 12
  endLine := 11
  endColumn := 17
  assertId := "1"
  functionName := "simple.increment"
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
-- vrml:end simple.increment.assert_1

-- vrml:begin simple.increment.ensures_2 2a190a9cf7e9f307
/--
Generated VC `simple.increment.ensures_2`.

- Rust source: `examples/m1-pipeline/simple.rs:8:13-8:23`
- Rust/SST construct: function postcondition (`ensures`)
- AssertId: `2`
- Statement hash: `2a190a9cf7e9f307`
-/
def ensures_2_meta : Vermilion.ObligationMeta := {
  rustFile := "examples/m1-pipeline/simple.rs"
  startLine := 8
  startColumn := 13
  endLine := 8
  endColumn := 23
  assertId := "2"
  functionName := "simple.increment"
  kind := "ensures"
  statementHash := "2a190a9cf7e9f307"
}
@[vrml_obligation] theorem ensures_2
    (x : Int)
    (requires_0 : Vermilion.inUnsignedRange 32 x)
    (requires_1 : x < 100)
    (assert_0 : Vermilion.inUnsignedRange 32 (x + 1))
    (assert_1 : ((x + 1) % 4294967296) > 0) :
    ((x + 1) % 4294967296) = (x + 1) := by
  vrml
-- vrml:end simple.increment.ensures_2

end simple.increment


#print axioms simple.increment.assert_0

#print axioms simple.increment.assert_1

#print axioms simple.increment.ensures_2
