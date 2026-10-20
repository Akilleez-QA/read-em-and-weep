# Bounded executable two-term residue capsule

This is the narrower executable implementation complement to the mathematical arbitrary-list contract in [PR107](https://github.com/Akilleez-QA/read-em-and-weep/pull/107), predecessor commit `c06ac39dfa47b50b55a266c9df4571971b7d7760`. It does not implement that arbitrary-list contract. Related prior capsules: checked Lean core [PR103](https://github.com/Akilleez-QA/read-em-and-weep/pull/103), Vermilion selector [PR104](https://github.com/Akilleez-QA/read-em-and-weep/pull/104), and selector–Laurent bridge [PR106](https://github.com/Akilleez-QA/read-em-and-weep/pull/106).

## Exact result

Two explicitly unrolled five-exponent i64 selectors followed by one addition. Twelve inputs have signed64 premises; each coefficient additionally lies in ±(2^62−1). The Lean bridge invokes the actual generated overflow and postcondition theorems and identifies the clipped result with the formal residue coefficient of exactly two Laurent terms. Repeated exponents add normally. It does not compute an absolute budget.

Historical positive checking accepted nine obligations (eight VCs and one decision-evidence obligation), exit 0. The otherwise identical false postcondition with +1 was rejected in the Lean phase, exit 1. The independent audit, clean sequential replay, initial failures, proof printing and standard-axiom reports are retained. Generated placeholders and rejected negative proof twins are not successful proofs.

## Provenance and transformations

All 57 recovered authored files are retained. Every Lean and Rust file is byte-identical to the recovered reviewed original. Prose/log/JSON/IR private absolute prefixes are display-normalized to `${ARTIFACT_ROOT}`, `${HOME}` or `${TMPDIR}`; numerical results, VC hashes and exit statuses are unchanged. README gets a publication banner. Original scripts and original checksum lists are retained with `.historical.txt` suffixes because they describe the old workspace, not a runnable public layout. `publication-provenance.json` binds every original file and maps its final public path; `manifest.json` binds final public bytes. Historical checksum references remain historical and are not substituted for the public manifest.

Only packaging checks were run for publication: original-byte/hash recovery, unchanged mathematical sources, final manifest consistency, path/credential-pattern scan and shell syntax. No new Lean check, Rust/VC generation, dependency build or HM evaluation was performed.

## Reproduction using existing dependencies

Use Vermilion `1a56a4f38cbb126b7d73b04207e9c6fda9f179bf`, Lean 4.33.0 commit `d8b18978322de05a8f3dba51ef03cf5461676c17`, Rust 1.96.0, Z3 4.12.5, and Verus `48600836424a79420589c56d86e720236a029811`. The included Lean/Verus toolchain declarations and lake-manifest pin dependencies. No upstream source or build tree is vendored.

For proof-only replay, activate that already-built environment, set VERMILION_ROOT to the pinned checkout, and run `bash recheck-proofs.sh`. It rebuilds only the local accepted proof modules and audits their axioms; it does not regenerate Rust obligations or run the negative checker. This new portable script is syntax-checked but was not run during publication.

For the full official positive/negative replay, copy this capsule to the existing checkout's examples/bounded-residue directory, preserving bridge-deps and proof twins. From the checkout, with its existing compiler environment active, use:

    ./scripts/run_example.sh examples/bounded-residue bounded.rs --per-file --lib BoundedResidue --manual-proofs
    ./scripts/run_example.sh examples/bounded-residue bounded_wrong.rs --per-file

Require positive exit 0 and negative exit 1 with phase=lean in `.vermilion/bounded_wrong-run.json`, then run the proof-only replay. The original per-file example required no new Lake library registration. Full historical orchestration is in recheck.sh.historical.txt.

## Remaining obligations

No arrays, arbitrary-length executable loop, loop invariant, machine-safe runtime budget, arbitrary-precision implementation, verified Rust interpreter/compiler, analytic residue or full geometric/HM bridge. Rust-to-SST correspondence, call-spec substitution, VC generation and machine embedding remain the existing Vermilion trust boundary. No source-instance or global obstruction conclusion follows from this capsule.
