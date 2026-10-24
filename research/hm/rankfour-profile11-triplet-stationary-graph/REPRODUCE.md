# Selected-only reproduction

The geometric proof is PROOF.md. The checker verifies one complete immutable input, a fixed invariant multiplicity, degree bookkeeping, formal Leibniz/symmetry coefficients and the double-divisor obstruction. No actual coefficient, graph scalar, point, jet, tensor, matrix, rank, invariant normalization or source instance is evaluated.

Copy exactly these six files, preserving relative paths, to a newly empty directory:

1. PROOF.md
2. INPUTS.json
3. REPRODUCE.md
4. verify.py
5. characters.py
6. inputs/nonsplit-quotient.md

Run using only the Python standard library:

    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH= python verify.py
    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH= python -O verify.py

Both result objects must be identical and report PASS. Runtime conditions use explicit exceptions, so optimization does not disable them. The imported character module separately performs 81 fixed exact-rational McKay identities. Its unused helper functions do not perform a search.

The complete direct original is PR1222 at f7abba83fedd46a9d91f5abbd9e40d3b02ae65f1, with exact path, UTF8 length, SHA256 and Git blob in INPUTS.json. The frozen proof has 12,872 bytes and SHA256 96c3a9dea9260bcc34435220e00ad78a721bb18423d38b3a9aae3b7124eab7b7.

An independent reviewer must read the entire proof and complete input, freshly authenticate the original by immutable repository path and Git blob, inspect all checker code, and replay exactly the selected six files in a fresh isolated directory. The whole-proof verdict must bind that exact proof hash and check frame independence, all generators, the coherent/fiberwise distinction and the scope of the converse. Arithmetic replay is not a substitute for that review.

Reviewer records and author result JSONs are publication evidence, not replay inputs. Exclude raw local fetch records, scratch audits, caches and publication manifests. No installation, network call, remote write, actual-instance evaluation, broad scan, or large computation is part of replay.
