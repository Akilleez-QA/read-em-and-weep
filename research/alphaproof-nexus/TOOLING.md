# Offline validation entrypoint

This directory integrates a pinned **proof-results release**, not a theorem-search
agent or the AlphaProof training system. `validate.py` uses Python 3.10+ and its
standard library. It does not require Lean for its default operation.

## What was actually tested here

- The Python fixture/mock suite passes: `python -B -m unittest -v test_validate.py`.
- `python -B validate.py` verifies the actual `pins.json` against independently
  embedded release constants and prints a validation plan.
- **Local Lean compilation has not been run.** Lean and Lake were unavailable in
  the authoring environment. The compiler interaction is covered by mocks, not a
  real Lean execution; the first prepared-environment replay may expose additional
  compiler/import-path requirements and must be reported honestly.
- Upstream CI evidence belongs to the separate release inventory. This tool does
  not query CI, and an upstream CI pass is not a local compilation result.

Run these commands from this directory:

```sh
python -B validate.py
python -B -m unittest -v test_validate.py
```

The first command launches **no subprocesses**, accesses no network, and does not
inspect a checkout or dependency artifacts. It checks the six-key pin manifest,
including all ten lockfile revisions and the three exact file SHA-256 values.
It is not a proof check or an integrity check of the entire integration directory.
Even when `--checkout` and `--lean` are supplied, compilation is disabled unless
`--run` is explicitly present. A successful plan prints `local_compilation:
"not_run"`, `checkout_checked: false`, and `dependencies_checked: false`.

## Optional: one proof in a prepared, isolated environment

Only do this in a trusted, already-prepared standalone upstream checkout,
separate from the existing Lean 4.34.1 fork/project. The checker will neither
create this checkout nor prepare its dependencies. It does not provide an
implicit fallback if anything is missing.

The containment guard rejects a checkout that contains this integration directory,
equals it, or is inside it. It does **not** discover every surrounding project's
repository root. Keeping the prepared checkout outside the existing fork is a
manual prerequisite, including when an integration directory has been copied out
of that fork or another nested checkout exists elsewhere in the fork.

Prerequisites:

1. An upstream checkout at
   `0647711a71183c1ea492ad60860776617ce1ea88`, with a local `.git` directory,
   its exact tracked contents, and a clean index.
2. All ten existing dependency checkouts under `.lake/packages`, at the exact
   revisions in `pins.json` and the upstream lockfile. Each must have its own
   local `.git` directory and unchanged tracked contents. Linked Git worktrees,
   tracked symlinks/submodules, and symlinked dependency directories are rejected.
3. Trusted, previously built Lean 4.27.0 dependency artifacts. In particular,
   `.lake/packages/mathlib/.lake/build/lib/lean/Mathlib.olean` must exist and be
   nonempty. Additional required imports must already exist; a missing import
   makes compilation fail. Merely having source checkouts is insufficient.
4. An installed native Lean 4.27.0 compiler, with its `lib/lean/Init.olean`.
   Supply its absolute, canonical `bin/lean` path. An elan proxy such as
   `~/.elan/bin/lean`, shell wrapper, or symlink is rejected. Supported directory
   names are `leanprover--lean4---v4.27.0` or the official
   `lean-4.27.0-{linux,linux_aarch64,darwin,darwin_aarch64}` layouts. The tool
   separately checks `--version` and `--print-prefix` before compilation.
5. POSIX address-space resource limits and an already-installed native Git
   executable on the system search path.

For example, after those prerequisites have been prepared separately:

```sh
python -B validate.py --run \
  --checkout /absolute/path/to/prepared/alphaproof-nexus-results \
  --lean /absolute/path/to/lean-4.27.0-linux/bin/lean \
  --timeout 300 --memory-mib 4096
```

This is an example path, not an instruction to install or download anything.
`--timeout` is the proof compiler's wall limit in seconds (default 300; range
1–3600). `--memory-mib` limits each compiler process's POSIX address space
(default 4096; range 512–32768). Address space is not the same as resident memory;
some systems may require a larger limit. Git checks use a separate 30-second,
4096-MiB per-command limit; version/prefix queries use 10 seconds each. The
entire preflight does not have a single aggregate wall deadline.

The only compiled source is:

`APNOutputs/AICollaborator/AlgebraicGeometry/hilbert_functions_5.lean`

The original file stays unchanged. The checker copies its verified bytes into a
temporary directory and appends only `#print axioms P5`. It runs that temporary
file directly with Lean and a deliberately constructed `LEAN_PATH`. No other
Hilbert module or library-wide target is compiled; sibling Hilbert modules have
colliding top-level names and must not be combined casually. The
`formal_conjectures` source checkout is pinned but is not an import search root
for this Mathlib-only proof.

A passing run requires a successful compiler exit and the `P5` axiom report.
Only the usual baseline `propext`, `Classical.choice`, and `Quot.sound` is allowed;
`sorryAx` or another axiom fails the check. The output includes the raw Lean
report. Tracked source and index integrity is checked again afterward. A failed
preflight, missing compiler/artifact, resource limit, compiler error, or missing
axiom report returns exit code 1 and never claims local certification.

Save the successful JSON receipt if the run is used as verification evidence. It
records the release commit, exact source SHA-256 values, all dependency revisions,
expected toolchain, observed compiler version/prefix/path, compiler exit code,
checkout and import paths, applied proof resource limits, and raw axiom output.
These source pins still do not certify the provenance of prebuilt artifacts.

## Safeguards and the trust boundary

- The manifest cannot silently redefine the repository, commit, compiler,
  dependency revisions, or file hashes: they are also embedded in the reviewed
  Python source. Review both together for an intentional future release change.
- Git reads HEAD/tree/index only. Tracked files are hashed in Python as Git blobs,
  so worktree clean/smudge filters are never run by `git diff` or `git status`.
  Replacement objects and lazy fetching are disabled; protocol access is denied.
- The tool never calls `lake`, `elan`, a package manager, clone/fetch/update/cache
  commands, upstream shell/Python scripts, or the existing fork's configuration.
- Subprocesses receive argument lists with `shell=False`, a cleaned environment,
  and `LEAN_NUM_THREADS=1`. Inherited Lean paths, Git overrides, and dynamic-loader
  environment overrides are not forwarded. Child process groups are cleaned up
  after exit or timeout. Output/file-size and address-space limits are applied.
- Relative-path traversal, symlinked source/dependency paths, and symlinks under
  selected compiled import directories are rejected. Use canonical paths.

**This is not a security sandbox.** Lean metaprograms and compiler/native plugins
can execute code with the invoking user's permissions. A pinned source revision
does not establish that the source is harmless. The installed compiler and
prebuilt `.olean`/native artifacts remain trusted inputs: a matching checkout
does not prove that its prebuilt artifacts were produced from that checkout.
The native-binary and version checks also do not authenticate the compiler's
provenance. No artifact rebuild, binary signature verification, or isolation from
filesystem/network access is provided. Use an appropriately isolated environment
without secrets if those inputs are not already trusted. The validator itself
does not request network operations, but it cannot prevent compiled metaprograms
from doing so. Do not modify checkouts or artifacts concurrently with a run.

## Test coverage

The tests use local synthetic data and mocked subprocesses. They cover default
opt-in behavior, corrupt pins/source/toolchain/lock, all dependency pin handling,
wrong HEAD, dirty/staged proofs, source and artifact path escapes, wrong compiler
version/prefix, wrapper/elan rejection, missing prerequisites, axiom rejection,
sanitized environments, no-shell invocation, process-group timeout cleanup,
memory-limit configuration, and exactly one temporary source invocation. These
checks validate orchestration, not the Lean theorem or real-toolchain compatibility.
