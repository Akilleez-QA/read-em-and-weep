import Vermilion.Obligations

set_option linter.unusedVariables false
set_option linter.style.nameCheck false
set_option linter.dupNamespace false

-- vrml:begin residue.residue_term.evidence_decidable_prop 233918b60f8d2ffa
/--
Generated typeclass evidence obligation `residue.residue_term.evidence_decidable_prop`.

- Rust source: `examples/residue-selector/residue.rs:8:13-10:18`
- Evidence origin: Rust `bool` represented as Lean `Prop` requires explicit decision evidence
- Target: `Decidable p`
- Consumers: residue.residue_term.ensures_5
- Statement hash: `233918b60f8d2ffa`
-/
def residue_residue_term_evidence_decidable_prop_meta : Vermilion.ObligationMeta := {
  rustFile := "examples/residue-selector/residue.rs"
  startLine := 8
  startColumn := 13
  endLine := 10
  endColumn := 18
  assertId := "typeclass-evidence"
  functionName := "residue.residue_term"
  kind := "typeclass_evidence"
  statementHash := "233918b60f8d2ffa"
}
@[vrml_evidence] noncomputable instance residue_residue_term_evidence_decidable_prop
    (p : Prop) :
    Decidable p := by
  exact Classical.propDecidable p
-- vrml:end residue.residue_term.evidence_decidable_prop

