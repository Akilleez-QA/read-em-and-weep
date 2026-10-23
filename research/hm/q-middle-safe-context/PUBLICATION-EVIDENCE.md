# Publication evidence and portable smoke harness

The four producer files remain unchanged. `INDEPENDENT-REVIEW.md` is an
exact copy of the completed independent review, SHA-256
`dff00b61da5cb1a10d81bdf7078d4e33bdbd6062ecf10f2495fe7a5410fdb501`.
Its execution statements refer to the original executed harness identified
below, not to a second execution of this portable copy.

## Sanitized execution evidence

`namespace-smoke.receipt.json` preserves every original code/input/executable
hash, version, limit, status, resource measurement, and cleanup result. Private
machine paths and process identifiers were removed or replaced with explicit
labels. The original command hash is named `original_command_sha256`: it
hashes the original private argv, not the normalized displayed command.
The original receipt hash remains recorded, so the sanitized document is
not represented as byte-identical to the original.

| Evidence | SHA-256 |
|---|---|
| Original execution receipt | 9c478acfbd213a4ac3647a4a13880c01c1dc08dfa8eac4aeb67b470ca4aac8e1 |
| Sanitized namespace-smoke.receipt.json | 5aaa8c60fd3e30a9f3380d6892e41eae23f84bd2810d8d003564d3ad477c3dec |
| namespace-smoke.stdout.txt, exact terminal output | 0020a0c89d8e3d96bb20b2fda600b2f0e602a75fde0103455ba58f166b57c6e7 |
| namespace-smoke.stderr.txt, empty | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |

The passing run used one factory invocation, Python 3.12.14 and SymPy 1.14.0.
It checked 144 exports and 116 closure bindings, with 0.575766 CPU seconds,
0.7577938329995959 seconds of supervised runtime, and 66,813,952 bytes of
sampled aggregate peak RSS. CPU60/wall75/sampledRSS1.5GiB limits were in place.
The receipt explicitly denies hard address-space enforcement and a finite
guaranteed RSS overshoot bound. No source feasibility solve or family loop ran.

## Portable harness and static relocation review

| Harness | SHA-256 | Execution status |
|---|---|---|
| Original reviewed and executed harness | 2b592af1564ad927fb0b1716129e23e684b08745efa949826656fd4965b15c4c | PASS, the receipt above |
| Published portable smoke.py | cefc93fcd512672369a07137541df181c93638876a858bf1a5086e4c4b676292 | Static relocation review PASS; factory not rerun |

The only relocation changes are an argparse import and replacement of the
workspace-specific package locator with `--package`, defaulting to the smoke
file's own directory. The new path is resolved and must contain safe_context.py
and provenance.json. Every AST node from the original `sys.path.insert` through
the end of the script is exactly unchanged, including the historical-import
tripwire, sole factory call, 144-export test, shared closure checks, identities,
quartic check, tiny exterior fixtures and terminal output.

Thus the same directory supplied through `--package` selects the same ordinary
module through the same import mechanism; no loader, namespace, mathematical
statement, or import-resolution precedence was substituted. `--help` was
checked successfully and exits before symbolic imports or construction. The
passed symbolic run was not repeated merely to relocate its harness.

From a checkout with the package and its frozen sibling input directory:

```sh
python -B research/hm/q-middle-safe-context/smoke.py --package research/hm/q-middle-safe-context
```

Use that command only inside the approved bounded process-group supervisor,
with assertions enabled and the recorded dependency versions. If smoke.py is
colocated with safe_context.py, `--package` may be omitted. The independent
review does not authorize downstream graded construction or source solving.

The staging check verified exact review/stdout/stderr copying, absence of
private user-directory paths and process-id fields, unchanged limits and
resource/status values, and exact executable smoke suffix AST equality.
