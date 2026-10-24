# Selected-only reproduction

Copy exactly the following seven files, preserving relative paths, to a newly empty directory:

1. PROOF.md
2. INPUTS.json
3. REPRODUCE.md
4. verify.py
5. characters.py
6. inputs/top-jet-complement.md
7. inputs/nonsplit-quotient.md

Run with the Python standard library:

    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH= python verify.py
    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH= python -O verify.py

Both outputs must be identical PASS objects. Guards use explicit exceptions and survive optimization. The imported character module performs 81 fixed exact-rational McKay checks. No unused helper initiates a search.

The direct originals are PR1224 at 317cf0c533b6ab8ce650d566e08c87610dd11ccd and PR1222 at f7abba83fedd46a9d91f5abbd9e40d3b02ae65f1. INPUTS.json fixes their full paths, UTF8 bytes, SHA256 and Git blobs. The frozen proof is 15,127 bytes, SHA256 205256f2772d21d81025e6c511a52de564bfd7e9e0d94cce79fc3f684b6d17ba.

Checks concern only exact input authentication, fixed universal representation multiplicities and degrees, elementary-order arithmetic, and three formal weight identities for the rank-three exterior functor. The local orders are hypotheses established by the proof's exact sheaf quotient; the checker does not compute any actual Smith form. No selected actual coefficients, points, jets, tensors, matrices, graph scalars, invariant normalizations or instance ranks are evaluated. There is no large computation, broad scan, package installation, network request or remote write.

An independent reviewer must read the entire frozen proof and both complete originals, freshly authenticate each by immutable repository path and Git blob, inspect the checker, and replay exactly these seven files in a fresh isolated directory. The whole-proof verdict must bind the exact proof hash and verify the Wronskian span argument, coherent derivative sum, actual B5/U5 quotient, exact torsion layers, exterior divisibility and determinant-line recovery. Arithmetic does not replace geometric review.

Author result JSONs and reviewer records are publication evidence, not replay inputs. Exclude raw local fetch records, scratch audits, caches and publication manifests.
