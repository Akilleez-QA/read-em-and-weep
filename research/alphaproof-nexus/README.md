# AlphaProof Nexus: pinned proof-output integration

This package gives the fork a reproducible entry point to the public
[AlphaProof Nexus results release](https://github.com/google-deepmind/alphaproof-nexus-results/tree/0647711a71183c1ea492ad60860776617ce1ea88),
plus one small attributed Lean proof example. It imports no model, controller,
or proof-search service. The release publishes proof outputs and supporting
materials; it does not supply the AlphaProof Nexus agent engine.

## What is included

- `inventory.json`: all 92 released file paths, byte sizes and Git blob SHA-1
  identifiers at commit `0647711a71183c1ea492ad60860776617ce1ea88`, including
  **71 Lean files**. This is a complete pinned source inventory, not a claim that
  the complete corpus is vendored or has been validated locally.
- `pins.json`: the exact release commit, Lean 4.27.0, all ten locked dependency
  revisions, and SHA-256 pins for the selected proof and project lock inputs.
- `examples/LogConcaveCore.lean`: a 13-line proof body copied verbatim from
  `hilbert_functions_5.lean`, lines 504–516, with its Google copyright and Apache
  notice retained. Only an import, explanatory comment and local namespace were
  added around the excerpt. `example-origin.json` records the provenance.
- `inspect_sources.py`: offline byte, excerpt, import and target-statement text
  checks. Its placeholder scan ignores ordinary comments and strings.
- `validate.py`: an opt-in, resource-bounded, single-file Lean validation entry
  point for a separately prepared checkout. Default operation only checks pins
  and displays the plan. See [TOOLING.md](TOOLING.md) for exact prerequisites and
  trust limits.

Nothing here changes the fork's existing Lean project. That project currently
pins Lean 4.34.1 and a different mathlib revision; these upstream proofs are kept
outside its module tree and must use their own isolated 4.27.0 environment.

## Quick checks, no downloads or Lean execution

From this directory, with Python 3.10 or later:

```sh
python3 inspect_sources.py
python3 validate.py
python3 -m unittest discover -p 'test_*.py' -v
```

To inspect an already downloaded copy of the full pinned P5 source as text:

```sh
python3 inspect_sources.py --upstream-proof /absolute/path/to/hilbert_functions_5.lean
```

The reported `lean_kernel_validation_performed: false` is intentional. Static
checks establish byte identity and the literal target, not successful proof
elaboration, semantic equivalence, absence of all possible trust escapes, or a
kernel/axiom audit of transitive imports.

## Access the full pinned corpus

The [immutable source tree](https://github.com/google-deepmind/alphaproof-nexus-results/tree/0647711a71183c1ea492ad60860776617ce1ea88)
provides every inventory entry. For an isolated local source checkout, review
upstream's license notices first, then run these commands in a fresh location:

```sh
git clone --no-checkout https://github.com/google-deepmind/alphaproof-nexus-results.git alphaproof-nexus-isolated
git -C alphaproof-nexus-isolated checkout --detach 0647711a71183c1ea492ad60860776617ce1ea88
```

These manual commands retrieve the full proof corpus. The scripts in this
package never clone, fetch, install a compiler, download cache files, invoke
Lake, or execute an upstream helper script. Dependency preparation is a
separate, explicit operation in that isolated checkout: follow the pinned
[upstream README](https://github.com/google-deepmind/alphaproof-nexus-results/blob/0647711a71183c1ea492ad60860776617ce1ea88/README.md)
and inspect its configuration before running build/cache commands. Use the
pinned toolchain and lockfile, rather than the fork's existing toolchain.
Review any applicable software-execution permissions before preparation.

Once the official native Lean compiler and all ten pinned dependency checkouts
and their prebuilt artifacts are available, `validate.py` can verify the
tracked source trees and compile just P5 with an appended `#print axioms P5`.
See TOOLING.md for the exact opt-in command. This checks one selected theorem;
it does not build all 71 files. Other Hilbert files reuse global names and
should be validated separately rather than imported together.

## Mathematical scope

The selected upstream declaration is:

```lean
def ProblemP5 : Prop :=
  ∀ (P : PureOrderIdeal 3),
    typePO P = 2 →
    IsLogConcaveUpTo (socleDegree P) (pureOSequence P.ideal)

theorem P5 : ProblemP5 := by
  -- complete proof remains in the pinned upstream source
```

This states log-concavity for **pure O-sequences in codimension 3 and type 2**,
or the corresponding monomial level algebras. The
[paper's corrected version 2](https://arxiv.org/html/2605.22763v2) distinguishes
this from the general level-algebra Hilbert-function question for (3,2), which
remains open. The tiny vendored lemma is an elementary integer-inequality
proof pattern used by the larger proof. Neither it nor this integration
settles the Horrocks–Mumford obstruction calculation in this fork.

The pinned release has 9 Erdős, 38 OEIS, 7 Hilbert and 11 Stacks Project Lean
files, plus 6 other AI-collaborator files. These are source-file counts, not
counts of independent results. The paper reports 44 solved OEIS conjectures
out of 492 considered; the release contains 38 OEIS proof files. This package
does not infer a one-to-one correspondence or resolve that difference.

## Validation status

The checked-in `static-check.json` records byte-identical excerpt verification,
the exact P5 target text, the sole `Mathlib` import, and no `sorry`, `admit`,
`axiom` or `native_decide` tokens outside ordinary comments/strings in that
selected source. The term `admit` in an upstream prose comment is ignored.
The 48 Python tests exercise source guards and the opt-in runner using fixtures;
ordinary and optimized Python modes both passed. `test-results.json` records
that scope.

No Lean compiler was available in the packaging environment. **No fresh Lean
build was run for either the example or P5.** Upstream has a
[successful CI run at the pinned commit](https://github.com/google-deepmind/alphaproof-nexus-results/actions/runs/29846710371);
that is separate evidence, not a local validation result. A future bounded
run should retain its compiler version, exact input pins, exit status and
printed axiom dependencies. Stronger independent kernel replay and comparison
of the elaborated target against an independently specified target would be
additional validation steps; they are not supplied by the current static scan.

## Attribution and licenses

See [NOTICE.md](NOTICE.md) and [licenses/Apache-2.0.txt](licenses/Apache-2.0.txt).
The vendored example is Apache-2.0 software. We do not relicense the entire
release: its other materials and third-party contributions have separate
notices. In particular, the OEIS portion has CC-BY-SA considerations. The
inventory links to those materials without copying their prose or datasets.
