import Vermilion.Obligations

set_option linter.unusedVariables false
set_option linter.style.nameCheck false
set_option linter.dupNamespace false

section

-- vrml:begin bounded.residue_term.evidence_decidable_prop 5bc1a8a63f76e1da
/--
Generated typeclass evidence obligation `bounded.residue_term.evidence_decidable_prop`.

- Rust source: `examples/bounded-residue/bounded.rs:8:13-10:18`
- Evidence origin: Rust `bool` represented as Lean `Prop` requires explicit decision evidence
- Target: `Decidable p`
- Consumers: bounded.residue_term.ensures_5
- Statement hash: `5bc1a8a63f76e1da`
-/
def bounded_residue_term_evidence_decidable_prop_meta : Vermilion.ObligationMeta := {
  rustFile := "examples/bounded-residue/bounded.rs"
  startLine := 8
  startColumn := 13
  endLine := 10
  endColumn := 18
  assertId := "typeclass-evidence"
  functionName := "bounded.residue_term"
  kind := "typeclass_evidence"
  statementHash := "5bc1a8a63f76e1da"
}
@[vrml_evidence] noncomputable local instance bounded_residue_term_evidence_decidable_prop
    (p : Prop) :
    Decidable p := by
  -- TODO(vermilion): provide this class dictionary interactively.
  exact Classical.propDecidable p
-- vrml:end bounded.residue_term.evidence_decidable_prop

namespace bounded.residue_term

-- vrml:begin bounded.residue_term.assert_0 bc5476103be8309e
/--
Generated VC `bounded.residue_term.assert_0`.

- Rust source: `examples/bounded-residue/bounded.rs:12:14-12:16`
- Rust/SST construct: possible arithmetic underflow/overflow
- AssertId: `0`
- Statement hash: `bc5476103be8309e`
-/
def assert_0_meta : Vermilion.ObligationMeta := {
  rustFile := "examples/bounded-residue/bounded.rs"
  startLine := 12
  startColumn := 14
  endLine := 12
  endColumn := 16
  assertId := "0"
  functionName := "bounded.residue_term"
  kind := "assert"
  statementHash := "bc5476103be8309e"
}
@[vrml_obligation] theorem assert_0
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
    (requires_5 : Vermilion.inSignedRange 64 coefficient) :
    Vermilion.inSignedRange 64 (0 - 1) := by
  vrml
-- vrml:end bounded.residue_term.assert_0

-- vrml:begin bounded.residue_term.assert_1 5cb0b36cd429a8a5
/--
Generated VC `bounded.residue_term.assert_1`.

- Rust source: `examples/bounded-residue/bounded.rs:12:26-12:28`
- Rust/SST construct: possible arithmetic underflow/overflow
- AssertId: `1`
- Statement hash: `5cb0b36cd429a8a5`
-/
def assert_1_meta : Vermilion.ObligationMeta := {
  rustFile := "examples/bounded-residue/bounded.rs"
  startLine := 12
  startColumn := 26
  endLine := 12
  endColumn := 28
  assertId := "1"
  functionName := "bounded.residue_term"
  kind := "assert"
  statementHash := "5cb0b36cd429a8a5"
}
@[vrml_obligation] theorem assert_1
    (e0 : Int)
    (e1 : Int)
    (e2 : Int)
    (e3 : Int)
    (e4 : Int)
    (coefficient : Int)
    (tmp_ : Prop)
    (requires_0 : Vermilion.inSignedRange 64 e0)
    (requires_1 : Vermilion.inSignedRange 64 e1)
    (requires_2 : Vermilion.inSignedRange 64 e2)
    (requires_3 : Vermilion.inSignedRange 64 e3)
    (requires_4 : Vermilion.inSignedRange 64 e4)
    (requires_5 : Vermilion.inSignedRange 64 coefficient)
    (assert_0 : Vermilion.inSignedRange 64 (0 - 1))
    (branch_0 : e0 = Vermilion.sclip 64 (0 - 1)) :
    Vermilion.inSignedRange 64 (0 - 1) := by
  vrml
-- vrml:end bounded.residue_term.assert_1

-- vrml:begin bounded.residue_term.assert_2 02971fc7374e13ea
/--
Generated VC `bounded.residue_term.assert_2`.

- Rust source: `examples/bounded-residue/bounded.rs:12:38-12:40`
- Rust/SST construct: possible arithmetic underflow/overflow
- AssertId: `2`
- Statement hash: `02971fc7374e13ea`
-/
def assert_2_meta : Vermilion.ObligationMeta := {
  rustFile := "examples/bounded-residue/bounded.rs"
  startLine := 12
  startColumn := 38
  endLine := 12
  endColumn := 40
  assertId := "2"
  functionName := "bounded.residue_term"
  kind := "assert"
  statementHash := "02971fc7374e13ea"
}
@[vrml_obligation] theorem assert_2
    (e0 : Int)
    (e1 : Int)
    (e2 : Int)
    (e3 : Int)
    (e4 : Int)
    (coefficient : Int)
    (tmp_ : Prop)
    (tmp__2 : Prop)
    (requires_0 : Vermilion.inSignedRange 64 e0)
    (requires_1 : Vermilion.inSignedRange 64 e1)
    (requires_2 : Vermilion.inSignedRange 64 e2)
    (requires_3 : Vermilion.inSignedRange 64 e3)
    (requires_4 : Vermilion.inSignedRange 64 e4)
    (requires_5 : Vermilion.inSignedRange 64 coefficient)
    (assert_0 : Vermilion.inSignedRange 64 (0 - 1))
    (then_0_assert_1 : (e0 = Vermilion.sclip 64 (0 - 1)) → Vermilion.inSignedRange 64 (0 - 1))
    (then_0_assume_9 : (e0 = Vermilion.sclip 64 (0 - 1)) → (tmp_ ↔ (e1 = Vermilion.sclip 64 (0 - 1))))
    (else_0_assume_8 : (¬ (e0 = Vermilion.sclip 64 (0 - 1))) → (tmp_ ↔ False))
    (branch_1 : tmp_) :
    Vermilion.inSignedRange 64 (0 - 1) := by
  vrml
-- vrml:end bounded.residue_term.assert_2

-- vrml:begin bounded.residue_term.assert_3 72a282a6983d3537
/--
Generated VC `bounded.residue_term.assert_3`.

- Rust source: `examples/bounded-residue/bounded.rs:12:50-12:52`
- Rust/SST construct: possible arithmetic underflow/overflow
- AssertId: `3`
- Statement hash: `72a282a6983d3537`
-/
def assert_3_meta : Vermilion.ObligationMeta := {
  rustFile := "examples/bounded-residue/bounded.rs"
  startLine := 12
  startColumn := 50
  endLine := 12
  endColumn := 52
  assertId := "3"
  functionName := "bounded.residue_term"
  kind := "assert"
  statementHash := "72a282a6983d3537"
}
@[vrml_obligation] theorem assert_3
    (e0 : Int)
    (e1 : Int)
    (e2 : Int)
    (e3 : Int)
    (e4 : Int)
    (coefficient : Int)
    (tmp_ : Prop)
    (tmp__2 : Prop)
    (tmp__3 : Prop)
    (requires_0 : Vermilion.inSignedRange 64 e0)
    (requires_1 : Vermilion.inSignedRange 64 e1)
    (requires_2 : Vermilion.inSignedRange 64 e2)
    (requires_3 : Vermilion.inSignedRange 64 e3)
    (requires_4 : Vermilion.inSignedRange 64 e4)
    (requires_5 : Vermilion.inSignedRange 64 coefficient)
    (assert_0 : Vermilion.inSignedRange 64 (0 - 1))
    (then_0_assert_1 : (e0 = Vermilion.sclip 64 (0 - 1)) → Vermilion.inSignedRange 64 (0 - 1))
    (then_0_assume_9 : (e0 = Vermilion.sclip 64 (0 - 1)) → (tmp_ ↔ (e1 = Vermilion.sclip 64 (0 - 1))))
    (else_0_assume_8 : (¬ (e0 = Vermilion.sclip 64 (0 - 1))) → (tmp_ ↔ False))
    (then_1_assert_2 : tmp_ → Vermilion.inSignedRange 64 (0 - 1))
    (then_1_assume_12 : tmp_ → (tmp__2 ↔ (e2 = Vermilion.sclip 64 (0 - 1))))
    (else_1_assume_11 : (¬ tmp_) → (tmp__2 ↔ False))
    (branch_2 : tmp__2) :
    Vermilion.inSignedRange 64 (0 - 1) := by
  vrml
-- vrml:end bounded.residue_term.assert_3

-- vrml:begin bounded.residue_term.assert_4 93f7c0909badecc9
/--
Generated VC `bounded.residue_term.assert_4`.

- Rust source: `examples/bounded-residue/bounded.rs:12:62-12:64`
- Rust/SST construct: possible arithmetic underflow/overflow
- AssertId: `4`
- Statement hash: `93f7c0909badecc9`
-/
def assert_4_meta : Vermilion.ObligationMeta := {
  rustFile := "examples/bounded-residue/bounded.rs"
  startLine := 12
  startColumn := 62
  endLine := 12
  endColumn := 64
  assertId := "4"
  functionName := "bounded.residue_term"
  kind := "assert"
  statementHash := "93f7c0909badecc9"
}
@[vrml_obligation] theorem assert_4
    (e0 : Int)
    (e1 : Int)
    (e2 : Int)
    (e3 : Int)
    (e4 : Int)
    (coefficient : Int)
    (tmp_ : Prop)
    (tmp__2 : Prop)
    (tmp__3 : Prop)
    (tmp__4 : Prop)
    (requires_0 : Vermilion.inSignedRange 64 e0)
    (requires_1 : Vermilion.inSignedRange 64 e1)
    (requires_2 : Vermilion.inSignedRange 64 e2)
    (requires_3 : Vermilion.inSignedRange 64 e3)
    (requires_4 : Vermilion.inSignedRange 64 e4)
    (requires_5 : Vermilion.inSignedRange 64 coefficient)
    (assert_0 : Vermilion.inSignedRange 64 (0 - 1))
    (then_0_assert_1 : (e0 = Vermilion.sclip 64 (0 - 1)) → Vermilion.inSignedRange 64 (0 - 1))
    (then_0_assume_9 : (e0 = Vermilion.sclip 64 (0 - 1)) → (tmp_ ↔ (e1 = Vermilion.sclip 64 (0 - 1))))
    (else_0_assume_8 : (¬ (e0 = Vermilion.sclip 64 (0 - 1))) → (tmp_ ↔ False))
    (then_1_assert_2 : tmp_ → Vermilion.inSignedRange 64 (0 - 1))
    (then_1_assume_12 : tmp_ → (tmp__2 ↔ (e2 = Vermilion.sclip 64 (0 - 1))))
    (else_1_assume_11 : (¬ tmp_) → (tmp__2 ↔ False))
    (then_2_assert_3 : tmp__2 → Vermilion.inSignedRange 64 (0 - 1))
    (then_2_assume_15 : tmp__2 → (tmp__3 ↔ (e3 = Vermilion.sclip 64 (0 - 1))))
    (else_2_assume_14 : (¬ tmp__2) → (tmp__3 ↔ False))
    (branch_3 : tmp__3) :
    Vermilion.inSignedRange 64 (0 - 1) := by
  vrml
-- vrml:end bounded.residue_term.assert_4

-- vrml:begin bounded.residue_term.ensures_5 40bc1be52a94f9a9
/--
Generated VC `bounded.residue_term.ensures_5`.

- Rust source: `examples/bounded-residue/bounded.rs:8:13-10:18`
- Rust/SST construct: function postcondition (`ensures`)
- AssertId: `5`
- Statement hash: `40bc1be52a94f9a9`
-/
def ensures_5_meta : Vermilion.ObligationMeta := {
  rustFile := "examples/bounded-residue/bounded.rs"
  startLine := 8
  startColumn := 13
  endLine := 10
  endColumn := 18
  assertId := "5"
  functionName := "bounded.residue_term"
  kind := "ensures"
  statementHash := "40bc1be52a94f9a9"
}
@[vrml_obligation] theorem ensures_5
    (e0 : Int)
    (e1 : Int)
    (e2 : Int)
    (e3 : Int)
    (e4 : Int)
    (coefficient : Int)
    (tmp_ : Prop)
    (tmp__2 : Prop)
    (tmp__3 : Prop)
    (tmp__4 : Prop)
    (requires_0 : Vermilion.inSignedRange 64 e0)
    (requires_1 : Vermilion.inSignedRange 64 e1)
    (requires_2 : Vermilion.inSignedRange 64 e2)
    (requires_3 : Vermilion.inSignedRange 64 e3)
    (requires_4 : Vermilion.inSignedRange 64 e4)
    (requires_5 : Vermilion.inSignedRange 64 coefficient)
    (assert_0 : Vermilion.inSignedRange 64 (0 - 1))
    (then_0_assert_1 : (e0 = Vermilion.sclip 64 (0 - 1)) → Vermilion.inSignedRange 64 (0 - 1))
    (then_0_assume_9 : (e0 = Vermilion.sclip 64 (0 - 1)) → (tmp_ ↔ (e1 = Vermilion.sclip 64 (0 - 1))))
    (else_0_assume_8 : (¬ (e0 = Vermilion.sclip 64 (0 - 1))) → (tmp_ ↔ False))
    (then_1_assert_2 : tmp_ → Vermilion.inSignedRange 64 (0 - 1))
    (then_1_assume_12 : tmp_ → (tmp__2 ↔ (e2 = Vermilion.sclip 64 (0 - 1))))
    (else_1_assume_11 : (¬ tmp_) → (tmp__2 ↔ False))
    (then_2_assert_3 : tmp__2 → Vermilion.inSignedRange 64 (0 - 1))
    (then_2_assume_15 : tmp__2 → (tmp__3 ↔ (e3 = Vermilion.sclip 64 (0 - 1))))
    (else_2_assume_14 : (¬ tmp__2) → (tmp__3 ↔ False))
    (then_3_assert_4 : tmp__3 → Vermilion.inSignedRange 64 (0 - 1))
    (then_3_assume_18 : tmp__3 → (tmp__4 ↔ (e4 = Vermilion.sclip 64 (0 - 1))))
    (else_3_assume_17 : (¬ tmp__3) → (tmp__4 ↔ False)) :
    (Vermilion.iteP tmp__4 coefficient 0) = (Vermilion.iteP (((((e0 = (0 - 1)) ∧ (e1 = (0 - 1))) ∧ (e2 = (0 - 1))) ∧ (e3 = (0 - 1))) ∧ (e4 = (0 - 1))) coefficient 0) := by
  vrml
-- vrml:end bounded.residue_term.ensures_5

end bounded.residue_term

namespace bounded.residue_two

-- vrml:begin bounded.residue_two.assert_2 919ee63e1b70623e
/--
Generated VC `bounded.residue_two.assert_2`.

- Rust source: `examples/bounded-residue/bounded.rs:26:5-26:10`
- Rust/SST construct: possible arithmetic underflow/overflow
- AssertId: `2`
- Statement hash: `919ee63e1b70623e`
-/
def assert_2_meta : Vermilion.ObligationMeta := {
  rustFile := "examples/bounded-residue/bounded.rs"
  startLine := 26
  startColumn := 5
  endLine := 26
  endColumn := 10
  assertId := "2"
  functionName := "bounded.residue_two"
  kind := "assert"
  statementHash := "919ee63e1b70623e"
}
@[vrml_obligation] theorem assert_2
    (a0 : Int)
    (a1 : Int)
    (a2 : Int)
    (a3 : Int)
    (a4 : Int)
    (ca : Int)
    (b0 : Int)
    (b1 : Int)
    (b2 : Int)
    (b3 : Int)
    (b4 : Int)
    (cb : Int)
    (requires_0 : Vermilion.inSignedRange 64 a0)
    (requires_1 : Vermilion.inSignedRange 64 a1)
    (requires_2 : Vermilion.inSignedRange 64 a2)
    (requires_3 : Vermilion.inSignedRange 64 a3)
    (requires_4 : Vermilion.inSignedRange 64 a4)
    (requires_5 : Vermilion.inSignedRange 64 ca)
    (requires_6 : Vermilion.inSignedRange 64 b0)
    (requires_7 : Vermilion.inSignedRange 64 b1)
    (requires_8 : Vermilion.inSignedRange 64 b2)
    (requires_9 : Vermilion.inSignedRange 64 b3)
    (requires_10 : Vermilion.inSignedRange 64 b4)
    (requires_11 : Vermilion.inSignedRange 64 cb)
    (requires_12 : ((0 - 4611686018427387903) ≤ ca) ∧ (ca ≤ 4611686018427387903))
    (requires_13 : ((0 - 4611686018427387903) ≤ cb) ∧ (cb ≤ 4611686018427387903))
    (assume_14 : Vermilion.inSignedRange 64 (Vermilion.iteP (((((a0 = (0 - 1)) ∧ (a1 = (0 - 1))) ∧ (a2 = (0 - 1))) ∧ (a3 = (0 - 1))) ∧ (a4 = (0 - 1))) ca 0))
    (assume_15 : Vermilion.inSignedRange 64 (Vermilion.iteP (((((b0 = (0 - 1)) ∧ (b1 = (0 - 1))) ∧ (b2 = (0 - 1))) ∧ (b3 = (0 - 1))) ∧ (b4 = (0 - 1))) cb 0)) :
    Vermilion.inSignedRange 64 ((Vermilion.iteP (((((a0 = (0 - 1)) ∧ (a1 = (0 - 1))) ∧ (a2 = (0 - 1))) ∧ (a3 = (0 - 1))) ∧ (a4 = (0 - 1))) ca 0) + (Vermilion.iteP (((((b0 = (0 - 1)) ∧ (b1 = (0 - 1))) ∧ (b2 = (0 - 1))) ∧ (b3 = (0 - 1))) ∧ (b4 = (0 - 1))) cb 0)) := by
  vrml
-- vrml:end bounded.residue_two.assert_2

-- vrml:begin bounded.residue_two.ensures_3 0b1bf9253df95dc5
/--
Generated VC `bounded.residue_two.ensures_3`.

- Rust source: `examples/bounded-residue/bounded.rs:21:13-22:97`
- Rust/SST construct: function postcondition (`ensures`)
- AssertId: `3`
- Statement hash: `0b1bf9253df95dc5`
-/
def ensures_3_meta : Vermilion.ObligationMeta := {
  rustFile := "examples/bounded-residue/bounded.rs"
  startLine := 21
  startColumn := 13
  endLine := 22
  endColumn := 97
  assertId := "3"
  functionName := "bounded.residue_two"
  kind := "ensures"
  statementHash := "0b1bf9253df95dc5"
}
@[vrml_obligation] theorem ensures_3
    (a0 : Int)
    (a1 : Int)
    (a2 : Int)
    (a3 : Int)
    (a4 : Int)
    (ca : Int)
    (b0 : Int)
    (b1 : Int)
    (b2 : Int)
    (b3 : Int)
    (b4 : Int)
    (cb : Int)
    (requires_0 : Vermilion.inSignedRange 64 a0)
    (requires_1 : Vermilion.inSignedRange 64 a1)
    (requires_2 : Vermilion.inSignedRange 64 a2)
    (requires_3 : Vermilion.inSignedRange 64 a3)
    (requires_4 : Vermilion.inSignedRange 64 a4)
    (requires_5 : Vermilion.inSignedRange 64 ca)
    (requires_6 : Vermilion.inSignedRange 64 b0)
    (requires_7 : Vermilion.inSignedRange 64 b1)
    (requires_8 : Vermilion.inSignedRange 64 b2)
    (requires_9 : Vermilion.inSignedRange 64 b3)
    (requires_10 : Vermilion.inSignedRange 64 b4)
    (requires_11 : Vermilion.inSignedRange 64 cb)
    (requires_12 : ((0 - 4611686018427387903) ≤ ca) ∧ (ca ≤ 4611686018427387903))
    (requires_13 : ((0 - 4611686018427387903) ≤ cb) ∧ (cb ≤ 4611686018427387903))
    (assume_14 : Vermilion.inSignedRange 64 (Vermilion.iteP (((((a0 = (0 - 1)) ∧ (a1 = (0 - 1))) ∧ (a2 = (0 - 1))) ∧ (a3 = (0 - 1))) ∧ (a4 = (0 - 1))) ca 0))
    (assume_15 : Vermilion.inSignedRange 64 (Vermilion.iteP (((((b0 = (0 - 1)) ∧ (b1 = (0 - 1))) ∧ (b2 = (0 - 1))) ∧ (b3 = (0 - 1))) ∧ (b4 = (0 - 1))) cb 0))
    (assert_2 : Vermilion.inSignedRange 64 ((Vermilion.iteP (((((a0 = (0 - 1)) ∧ (a1 = (0 - 1))) ∧ (a2 = (0 - 1))) ∧ (a3 = (0 - 1))) ∧ (a4 = (0 - 1))) ca 0) + (Vermilion.iteP (((((b0 = (0 - 1)) ∧ (b1 = (0 - 1))) ∧ (b2 = (0 - 1))) ∧ (b3 = (0 - 1))) ∧ (b4 = (0 - 1))) cb 0))) :
    Vermilion.sclip 64 ((Vermilion.iteP (((((a0 = (0 - 1)) ∧ (a1 = (0 - 1))) ∧ (a2 = (0 - 1))) ∧ (a3 = (0 - 1))) ∧ (a4 = (0 - 1))) ca 0) + (Vermilion.iteP (((((b0 = (0 - 1)) ∧ (b1 = (0 - 1))) ∧ (b2 = (0 - 1))) ∧ (b3 = (0 - 1))) ∧ (b4 = (0 - 1))) cb 0)) = ((Vermilion.iteP (((((a0 = (0 - 1)) ∧ (a1 = (0 - 1))) ∧ (a2 = (0 - 1))) ∧ (a3 = (0 - 1))) ∧ (a4 = (0 - 1))) ca 0) + (Vermilion.iteP (((((b0 = (0 - 1)) ∧ (b1 = (0 - 1))) ∧ (b2 = (0 - 1))) ∧ (b3 = (0 - 1))) ∧ (b4 = (0 - 1))) cb 0)) := by
  vrml
-- vrml:end bounded.residue_two.ensures_3

end bounded.residue_two

end
