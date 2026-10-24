# Exact eight-file selected-only reproduction

Copy exactly these eight files, preserving relative paths, into a newly empty directory:

1. PROOF.md
2. INPUTS.json
3. REPRODUCE.md
4. verify.py
5. characters.py
6. inputs/lifted-jets-and-kernel-two.md
7. inputs/five-kernels.md
8. inputs/quartic-normal-map.md

Run using only the Python standard library:

    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH= python verify.py
    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH= python -O verify.py

Both outputs must be identical PASS objects. All guards use explicit exceptions and survive optimization. The character module performs 81 fixed exact-rational McKay checks; it contains no source-instance data or broad search.

The frozen entire proof has 20,248 UTF8 bytes and SHA256 c501c094dfe7cff853f8b0a64552b4a59478581a2d11921ec5f8f70f34bb0542. The verifier hard-codes that hash and length, plus all three complete input paths, immutable commits, lengths, SHA256 hashes and Git blob identities. INPUTS.json records the same immutable source bindings. The sources are PR1226 at c565bd8b5b65829e99bdd96a7c5f076b01050465, PR1198 at 7d71f0e2a3963cff64a069198f4415c5cfd0fe9b, and PR1225 at 06385eec63b85efac6cc25441d4b58d4fa5a8adb.

Author fresh read-only connector responses are retained in LOCAL-SOURCE-FETCHES.json but are excluded from publication and replay. Author normal/optimized result JSONs and reviewer records are evidence, not selected replay inputs. Exclude raw local fetches, scratch audits, caches and the publication manifest itself.

The checks concern complete local input authentication and fixed universal physical representations, line-bundle degree arithmetic, exact virtual Euler characters, and formal differentiation of an order-three annihilation rectangle. The dimension-four budget is resolved through its three integer factorizations, not a scan of kernel tuples. No actual coefficient, parameter, point, jet, tensor, matrix, graph scalar, invariant normalization or source-instance rank is selected or evaluated. No package installation, network access or remote write occurs during replay.

A new independent reviewer must read the entire frozen proof, all three complete originals and both Python sources; independently fetch all three originals through immutable repository path and Git blob; authenticate their exact bytes; and replay only these eight files in a newly empty isolated directory in normal and optimized Python. The entire-proof verdict must bind the exact frozen hash. The geometric audit must inspect the strict-top negative-horizontal argument, the coherent W' row, the unique quartic-kernel placement of S4, every nonzero and saturated actual backward row of the octic ladder, constant projection without inverse differentiation, the full annihilation rectangle, the T6 comparison inside actual K through its quotient O, and the exact irreducible cohomology budget. Arithmetic does not replace these proof obligations.

The conclusion is only that original K3 forces top F<=-6 and F=(D+P)(-6)+O(-10) in the retained full-positive, local-delta-twelve, residual simultaneous k=2 geometry. It does not exclude or realize K3 or the branch, and makes no assertion about F^- or algebraicity.
