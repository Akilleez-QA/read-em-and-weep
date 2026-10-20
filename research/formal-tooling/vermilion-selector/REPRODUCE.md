# Existing Vermilion checkout replay

Use the exact Vermilion, Verus, Lean, Rust and Z3 versions in README.md and the included dependency locks. This capsule does not vendor or rebuild them. Copy the examples/residue-selector subtree into that existing checkout and apply the four-line proof-library registration in workspace-changes.patch (or use the official register_proof_lib.py command in commands.txt). Run the residue example with --lib ResidueSelector --manual-proofs. The accepted proof twins, not generated placeholders or rejected negative controls, are the proof evidence. Preserve the original initial missing-evidence failure, repaired successful run, and false-postcondition rejection.

Historical commands are in commands.txt. No new run was performed for publication. See logs/independent-axioms-residue.log and INDEPENDENT-AUDIT.md.
