# Exact nine-file selected replay

Copy exactly these nine files, preserving relative paths, into a newly empty directory:

1. PROOF.md
2. INPUTS.json
3. REPRODUCE.md
4. verify.py
5. characters.py
6. inputs/first-kernel-structure.md
7. inputs/third-kernel-top-rigidity.md
8. inputs/top-jet-complement.md
9. inputs/common-kernel-ladder.md

Run inside that new directory using only the Python standard library:

    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH= python verify.py
    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH= python -O verify.py

Both outputs must be identical PASS objects. All guards use explicit exceptions and survive optimization. The character helper performs 81 fixed exact-rational physical-W McKay consistency checks; its requested representations are exactly the finite universal identities used in the proof. There is no search over splitting types or actual instances.

The frozen entire proof is 16,808 UTF8 bytes, SHA256 074dba0e590290f7b811a848b5fb4910ab6eebe5597f855111b66d5cd5fe71d0.

The four complete direct originals are authenticated in INPUTS.json and independently hard-coded in verify.py by exact repository path, immutable commit, UTF8 length, SHA256, and Git blob identity. They are PR1228, PR1229, PR1224, and PR1217. Full fresh author read-only connector responses are retained in LOCAL-SOURCE-FETCHES.json, excluded from publication and replay. No truncated excerpt replaces an input.

Checks concern source authentication and bounded universal character, rank, degree, and Ext arithmetic only. They do not evaluate any selected actual coefficient, parameter, point, jet, tensor, matrix, normalization, graph scalar, or source-instance rank. There is no broad scan, large computation, package installation, network request, or remote write during replay. Arithmetic success is not a geometric review.

A new independent reviewer must read the entire frozen proof, all four complete immutable originals, and both Python files. It must independently fetch each original by immutable repository path and Git blob, authenticate exact bytes, and replay exactly these nine selected files in a newly empty isolated directory in both normal and optimized Python. Its entire-proof verdict must bind the exact frozen proof hash. The review must check:

- The common F type is separately supplied for K1 and K3, while F^- is re-proved from common actual data rather than imported from K1.
- Every step of the rank-four Q section argument at twists six, seven, and eight, including the nonzero Wprime Euler component and coherent P-row fullness.
- The actual B6/F6 -> B3/F isomorphism and its coherent lower projection on U4.
- O-linearity and nonvanishing of beta_B restricted to F^-, with no quotient connection.
- The exact intrinsic B^- kernel and actual inclusion of the coherent image in E before any degree comparison.
- Exclusion of unequal normal middle types by the required scalar quotient E -> O(10), not by falsely killing the P row.
- Identification of the balanced coefficient W from Sym11 W and the actual B^+ incidences.
- The conditional stopping boundary, with no further kernel chain, split-dual exclusion, realization, higher-jet extrapolation, or whole-profile exclusion.

Author result JSONs and later reviewer records are evidence, not replay inputs. Exclude drafts, raw fetches, caches, scratch files, and publication manifests from selected replay. This packet does not perform any merge or upstream submission.
