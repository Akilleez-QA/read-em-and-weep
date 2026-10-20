> Publication note: Read [PUBLICATION.md](PUBLICATION.md) first. Original checks below are historical; original shell scripts now have `.historical.txt` suffixes. Use the public reproduction instructions, not private-path commands.

# Checked abstract core of the Koszul argument

These sources were compiled with Lean 4.19.0 and Mathlib v4.19.0. The independent audit and direct compiler receipts are included.

## What is checked

- `KoszulSlots.lean`: exact integer bidegree/support classifications and their conditional rank consequences.
- `KoszulDimension.lean`: quotient-dimension bookkeeping, finite loss budgets, and the 90 versus 55 contradiction.
- `KoszulCombined.lean`: derives stabilization and rank ten from the stated page interfaces, then invokes the contradiction. It does not assume the nonzero conclusion.
- `Propagation.lean`: genuine Mathlib linear maps and submodules; equivariant nonzero-map surjectivity, transport of spanning families, and fullness from a subspace plus its quotient.
- `Audit*.lean`: axiom probes and synthetic witnesses showing the numerical assumption interfaces are consistent.

## Exact boundary

This is not a formalization of the complete HM geometric proof. Construction of the sheaf Koszul spectral sequence, its geometric realization, cohomology values, representation identification, actual cubic nonvanishing, and filtered transfer remain explicit imported hypotheses. The numerical layer does not construct spectral-sequence vector spaces. No actual HM source values were computed.

The checked proofs contain no `sorry`, custom axioms, or proof-oracle shortcuts. Their dependency reports list only standard Lean axioms. See `AUDIT.md` for precise theorem-by-theorem coverage.

## Rechecking

The archive intentionally excludes compiler binaries, cached Mathlib libraries, and generated `.olean` files. `ENVIRONMENT.md` records the official dependency sources and pinned commits. Restore the official Lean 4.19.0 release under `toolchain/lean-4.19.0-linux` and the Mathlib v4.19.0 checkout under `mathlib`, with its pinned dependencies and required cache available. Then run `./recheck.sh`. This rebuilds the proof artifacts and reruns the audit probes. The script was executed successfully in the original cloud workspace; its output is `ROOT-RECHECK.txt`.

The accompanying `lean-toolchain` records the compiler version. The mathematical source proof and its prose audit are included under `source-proof/` for the correspondence audit. The input assumptions are visible in the Lean theorem statements, not hidden in a generated success label.
