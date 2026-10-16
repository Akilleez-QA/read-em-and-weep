Codex-PUB01 — read-only publication audit.

Source: PR80 `b5224465774932b25b03d74af5dbe087ba291ac2`; PR79 `ea2d1a1d2b5774984d0ad48bc15df5fa4d2e0f18`; PR81 `f166db3a5eef50d0421ec2f214ba46f9735f403d`; PR82 `aa422b2a82e424082f3e1174f5d3233f1afbd3bf`. Scope: swarm STATUS/README, relevant proof/reproduction dependencies, three PR79 publication packages, focused-PR contents, and cached coordination comments through [6210564082](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6210564082). Availability conclusions concern these fetched commits; live GitHub heads were not rechecked.

1. **Current documentation falsely describes published inputs as unavailable.**  
   `research/codex-swarm/README.md:38` says generator/numbering, mask-gap certificates and symmetry derivation await publication. Line 42 still holds E12 scanning pending seed identification. STATUS line 12 says executable lowering needs publication; line 43 names only the older support release.

   Suggested replacement:
   > PR79 at `ea2d1a1d2b5774984d0ad48bc15df5fa4d2e0f18` publishes support certificates, finite-domain foundations and the general v5 source-binding/formal-normal-order compiler. Seed4 is identified; its complete E12 directional coverage is published under fresh-consistent ordering. Historical-source comparison, source-specific regularization and complete physical coefficient lowering remain open. Seed4 coverage should not be rescanned.

   Historical worker reports may retain their original statements when clearly marked historical.

2. **Published artifacts exist, but PR80 lacks a complete current reproduction index.**  
   All listed hashes matched Git blobs: support package **65 entries**, compiler **34 SHA256SUMS entries**, foundations **53 entries**. This verifies artifact availability and byte integrity, not mathematics or recorded test outcomes. `arithmetic/README.md` correctly stages the older immutable support dependency, but omits the newer compiler/foundations.

   Add:
   > Source inventory: PR79 at `ea2d1a1…`, directories `null-support-certificates/`, `null-proof-foundations/`, and `null-operator-compiler/`. Each package has its own replay instructions and limits. Compiler/foundations use Python 3.12 and their published requirements. Swarm metadata scripts also require the pinned Git objects; a source ZIP alone is insufficient.

   Preserve older valid pins rather than replacing them indiscriminately.

3. **Focused review packages contain unresolved evidence pointers.**  
   PR81/82 report banners refer to `STATUS.md`, which neither focused branch contains. `reports/Codex-V01-endpoint-support.md:5` names absent `Codex-V01-endpoint-support.py` and `.json`; the shipped equivalents are `check_endpoint_support.py` and `certificates/endpoint-support.json`.

   Correction:
   > Reviewed metadata record; current acceptance scope is recorded in PR80 at `b522446…/research/codex-swarm/STATUS.md`. Reproduce using `check_endpoint_support.py`; saved classification: `certificates/endpoint-support.json`.

   All nine non-README extracted files in each focused PR match PR80 byte-for-byte. They are review subsets, not independent implementations.

4. **Additional pertinent work remains local in the inspected snapshot.**  
   `research/codex-swarm/arithmetic/compiler_v5/` and `research/codex-swarm/detector-selection/` are untracked, including binding snapshots, reviews, selection and a run receipt. They are absent from the inspected publication commits.

   Registry wording:
   > Additional compiler-binding and detector-selection drafts are local staging only; no accepted result relies on them pending publication with immutable provenance and review scope.

5. **No hard-coded private staging-path dependency found in the inspected published packages.**  
   No `/home/` or `/tmp/` references appeared in tracked swarm files or the published compiler/foundations. The configurable temporary directory in arithmetic reproduction instructions is portable staging, not evidence.

The published claims remain conditional: minimal completeness of twenty constant scalar maps, fixed-partition selector exclusions, and seed4 E12 directional coverage. Returned worker reports and recorded PASS logs do not independently establish those claims. None supplies corrected-source values or decides the complete obstruction.

No files changed, posts, commits, test-suite execution or physical-source arithmetic.

Publication note: this report records its inspection snapshot; subsequent corrections and review dispositions are recorded in STATUS.md and the relevant package README.
