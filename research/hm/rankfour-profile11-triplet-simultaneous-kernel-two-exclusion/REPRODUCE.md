# Selected-only reproduction

Copy exactly these nine files, preserving relative paths, to a newly empty directory:

1. PROOF.md
2. INPUTS.json
3. REPRODUCE.md
4. verify.py
5. characters.py
6. inputs/quartic-normal-map.md
7. inputs/common-kernel-ladder.md
8. inputs/eighteen-jets.md
9. inputs/five-kernels.md

Run with the Python standard library:

    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH= python verify.py
    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH= python -O verify.py

Both outputs must be identical PASS objects. Guards use explicit exceptions and survive optimization. The character module performs 81 fixed exact-rational McKay checks; it contains no search or unused enumerator.

The frozen proof is 13,703 bytes, SHA256 0165fa9a854879e5b2c67885f3b0bede6c3f48b34e1c761c0ca846645a3247fa. INPUTS.json fixes all four complete immutable original paths, commits, UTF8 lengths, SHA256 values and Git blobs.

Checks concern only complete input authentication and fixed universal representation, degree, rank and exact-sequence arithmetic. They do not evaluate selected actual source coefficients, parameters, points, jets, tensors, matrices, graph scalars or instance ranks. There is no large computation, broad scan, package installation, network request or remote write.

An independent reviewer must read the entire frozen proof and all four complete originals; freshly authenticate each original by immutable repository path and Git blob; inspect both Python files; and replay exactly the nine selected files in a newly isolated directory in normal and optimized Python. The entire-proof verdict must bind the exact frozen hash. Required geometric review includes the actual upper kernels and shared coherent lower row, the conditional derivative factorization in the jet induction, lifted complete coefficient span, the actual direct-sum preimages and O-linear H(-2) normal row, the equivariant Ext obstruction, and equality with the actual sixth jets in the original constant ambient. Arithmetic does not replace whole-proof review.

The conclusion excludes only original K2 within the retained simultaneous rank-seven k=2 case. Other kernel types and other coherent-image branches remain open here. Author JSON results and reviewer records are publication evidence, not replay inputs. Exclude raw local fetches, scratch audits, caches and the publication manifest itself.
