> Publication note: Read [PUBLICATION.md](PUBLICATION.md) first. Original checks below are historical; original shell scripts now have `.historical.txt` suffixes. Use the public reproduction instructions, not private-path commands.

# Vermilion cloud build and verification receipt

Completed 2026-10-18. This is a new isolated cloud workspace; the existing Lean 4.19 project was not changed.

## Revisions and versions

- Vermilion: `1a56a4f38cbb126b7d73b04207e9c6fda9f179bf` (official `ilyasergey/vermilion` checkout).
- Lean: 4.33.0, commit `d8b18978322de05a8f3dba51ef03cf5461676c17`.
- Rust/cargo: 1.96.0; Z3: 4.12.5.
- Verus fork: `48600836424a79420589c56d86e720236a029811`.
- Exact Lean dependency pins are included in `lake-manifest.json`.

## Results

1. Official `scripts/build.sh` completed with exit 0. Lean build: 3,382 jobs. Rust unit tests: 12 passed, 0 failed. Pinned Verus and direct SST adapter built. Verus's own vstd build reported 1,972 verified, 0 errors; this is a separate Verus result, not a Lean verification claim.
2. Official introductory increment example: 3/3 obligations newly checked by Lean, exit 0, no proof holes.
3. Mutated intro postcondition (`y == x + 2`, unchanged increment body): rejected by Lean at the Rust postcondition, exit 1. The failure is not a parse or front-end error.
4. New abstract five-exponent residue-term selector and first-coordinate-face zero lemma: 8/8 obligations accepted, including 7 VCs and 1 explicit `Decidable Prop` dictionary. Successful proof twins contain no `sorry` or `admit`.
5. The initial selector run correctly failed closed on missing class evidence. Its receipt is retained. The sole manual repair was `exact Classical.propDecidable p` in the editable evidence twin. A fresh `--manual-proofs` run checked all proof twins and returned exit 0.
6. False residue control (`return coefficient` with universal postcondition `r == 0`): rejected by Lean, exit 1.
7. Transitive `#print axioms` audits of all 3 intro declarations and all 8 selector declarations returned exit 0 and listed only `propext`, `Classical.choice`, and `Quot.sound`. No `sorryAx`, additional project axiom, or SMT oracle axiom occurs in these proof terms.

## Exact scope

The executable selector takes five arbitrary `i64` exponents and an arbitrary `i64` coefficient. It returns the coefficient iff all five exponents equal -1, otherwise zero. Its second function proves that a nonnegative first exponent forces zero. These are universal specifications over bounded machine inputs, not tests of selected coefficient values. No HM source/model, polynomial instance, rank, point, jet, residual, or Massey value was executed.

This is one monomial coefficient-selection component. It does not implement arbitrary-precision arithmetic, sparse-polynomial summation, a full certificate checker, or the geometric-to-algebraic bridge. It does not assert that all five projective faces have been verified by the named first-coordinate lemma. No homogeneity inference is needed or claimed.

## Trust and failure artifacts

Lean checks the emitted statements. Verus front/middle-end correspondence, Rust lowering, the Lean VC generator, embedding conventions, and the checking/reporting path remain trusted as documented by official `docs/trust.md`. The translator is not foundationally verified. Classical choice is explicit and disclosed.

The generated machine evidence module deliberately retains its placeholder by the tool's design; the accepted proof twin replaces it. Only the complete, repaired twin is the final arbiter. Negative-control twins intentionally contain `sorry` after rejected goals and are not claimed as proofs. Inspect the positive subtrees and axiom audits rather than treating every file in the experiment as a successful proof.

## Reproduction

See `logs/commands.txt` for exact commands and `*.exit`/`*-run.json` for exit/phase receipts. Sources, generated manifests, proof twins, self-contained axiom-audit inputs and logs are included in the accompanying archive. The only tracked upstream modification is the four-line Lake proof-library registration; all custom work lives under `examples/residue-selector`.

### Recreate on a clean Linux workspace

Install official Lean 4.33.0 (lean and lake on PATH), Rust via rustup, and the native C++ prerequisites listed by upstream. Clone the public Vermilion repository and check out commit 1a56a4f38cbb126b7d73b04207e9c6fda9f179bf, then run ./scripts/build.sh. Its script obtains the pinned fork and dependencies. Copy this archive's examples/residue-selector subtree into the checkout; keep the upstream intro unchanged. Register with python3 scripts/register_proof_lib.py register ResidueSelector examples/residue-selector/proofs. Run the intro and the final --manual-proofs selector commands in commands.txt. Run the two negative commands expecting exit 1, not exit 0. They are intentionally false and must remain unverified.

For transitive axiom checks, copy audit-intro.lean and audit-residue.lean into the checkout and run each with lake env lean (or the cached LEAN_PATH method in commands.txt). These files contain the same accepted declaration blocks and print all their transitive axioms. INDEPENDENT-AUDIT.md records an independent byte-level match and rerun. Local install/build paths in logs have been replaced by <workspace>; download progress lines are omitted. Exit receipts preserve actual command outcomes.
