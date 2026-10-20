# Public proof capsule

These are existing 2026-10-18 results and proof receipts, staged for focused review on 2026-10-20. No new proof compilation, dependency build, or selected HM evaluation was performed during publication.

Lean proof sources are byte-identical to the reviewed originals. Private absolute workspace, home and temporary prefixes in prose/receipts are normalized to `${ARTIFACT_ROOT}`, `${HOME}`, and `${TMPDIR}`. Historical shell scripts are retained as `.sh.historical.txt`, not advertised as portable runnable scripts. `recheck-public.sh` is the new portable proof-only entry point, syntax-checked but not executed during publication. Supply an existing pinned dependency checkout; it does not install or build dependencies.

`publication-provenance.json` binds original source bytes and normalized public receipt bytes. `manifest.json` binds the final public capsule. Prior audits apply to the unchanged Lean source, not to newly authored packaging. Recorded successful runs are historical evidence, not a claim of a fresh clean-room run. No compiler binaries, `.olean` objects, cache directories or upstream checkout are published.

Read the included original README and audit for precise hypotheses, remaining geometric/implementation bridges, and negative controls. The full HM proof and an executable residue accumulator remain unverified by these capsules.
