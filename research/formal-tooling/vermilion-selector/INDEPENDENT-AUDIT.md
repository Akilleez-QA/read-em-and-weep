# Independent Vermilion execution audit

Audit date: 2026-10-18. Verdict: **PASS for installed/built tooling and the two explicitly bounded demonstrations**, subject to the trust boundary below.

## Source and installation

- Repository: https://github.com/ilyasergey/vermilion.git
- Checked HEAD: `1a56a4f38cbb126b7d73b04207e9c6fda9f179bf`.
- Executed version checks: Lean 4.33.0, commit `d8b18978322de05a8f3dba51ef03cf5461676c17`; Rust 1.96.0 (`ac68faa20`).
- Checked Verus checkout: `48600836424a79420589c56d86e720236a029811`.
- At audit, tracked source change was only a four-line ResidueSelector library registration in lakefile.lean. New residue-selector sources and proof artifacts are custom demonstrations, not upstream source.
- Official build log ends `Build completed successfully (3382 jobs)` and `Vermilion build complete.`; build.exit is 0. This means 3382 Lake jobs completed, not 3382 new mathematical results.
- Rust unit-test log contains 2 backend and 10 source-guard passing tests, 0 failures; rust-unit-tests.exit is 0.
- Build receipts were inspected; the expensive build was not independently repeated.

## Successful checks

1. Upstream intro increment: 3 generated obligations; intro-positive.exit = 0.
2. Custom residue selector and missing-face-zero: 7 VCs plus one explicit decision-evidence obligation, 3 twin units; residue-positive.exit = 0. Exact successful runner command: `./scripts/run_example.sh examples/residue-selector residue.rs --lib ResidueSelector --manual-proofs`.
3. Independently reran Lean on `.vermilion/audit-intro.lean` and `.vermilion/audit-residue.lean`, with local env.sh and LEAN_PATH from .vermilion/lean-path. Each returned 0. Receipts: `logs/independent-axioms-intro.log/.exit` and `logs/independent-axioms-residue.log/.exit`.
4. Independently compared every marked declaration block in the audit inputs against actual successful proof twins: 3/3 and 8/8 are byte-identical. Counts match generated JSON obligation manifests.
5. All eleven declarations report exactly `[propext, Classical.choice, Quot.sound]` as transitive axioms. No sorryAx or additional axiom occurs. Successful twins contain no sorry/admit placeholders. This is an axiom-relative kernel-check, not an axiom-free claim.

## Negative controls and evidence repair

- Intro false specification returns x+1 but requires x+2: exit 1, Lean rejects ensures_2.
- False residue specification returns arbitrary coefficient but requires zero: exit 1, Lean rejects ensures_0.
- Initial residue check failed closed on unresolved Decidable Prop evidence, exit 1, despite other VCs being provable. That receipt remains in `logs/residue-initial-unresolved-evidence.*`.
- Repair filled only the explicit evidence twin with `exact Classical.propDecidable p`; subsequent manual-proof kernel checking succeeded.
- Failed-control proof twins deliberately retain unresolved holes. They are not among successful artifacts. Generated Evidence.lean can retain a placeholder because the successful manual-proof route checks the complete, current user-owned proof twin as sole arbiter. Do not claim the entire checkout is sorry-free.

## Actual mathematical scope

The selector takes five signed 64-bit exponents and one signed 64-bit coefficient and returns that coefficient precisely when every exponent equals -1, otherwise zero. The second function proves zero contribution under the first-coordinate hypothesis e0 >= 0. The verification is universal over these bounded input types. It does not instantiate HM data, calculate a polynomial residue, prove arbitrary-precision algebra, verify all coordinate faces, or establish a geometric interpretation.

No actual HM source values, models, ranks, polynomial instances, points, jets, residual computations, or Massey computations were used or checked.

## Trust boundary

Per upstream `docs/trust.md` and `docs/vcgen.md`, the Verus front/middle end, Rust lowering, Lean VC generator, embedding conventions, and checking/reporting path remain trusted. Lean checks the generated statements under their axioms; it does not certify source-to-obligation translation or completeness of those obligations. This audit checked manifest counts and source/twin provenance for these small examples, not the soundness of the full translator.

The `1972 verified, 0 errors` line belongs to Verus/vstd setup, not the Vermilion Lean verdict for these examples. Neither that line nor this audit supports a fully foundational compiler/verification claim.

## Source fingerprints

- intro source: `714c834b015509643e705047d5372866803a2567a895cb07ecc7afc299eedcf6`
- custom selector source: `0a148a451fb3445684561e90cf481d894bccf7480aa42b7455d04544c3fcf46c`
- intro false control: `c998bbf7b5c639d813ebf18d7205525a9564dd0e01a42ba5dfa9461e89078add`
- residue false control: `7b111645ec7e6fb98debc6d30d62619fbf2acf0a1bf79154e6e6818cd4baad05`
