# Selected-only reproduction

The proof is the mathematical argument. The verifier checks only the exact immutable inputs, fixed universal character identities, degree arithmetic and the formal mixed-norm/Serre-duality directions. It evaluates no actual source coefficient, parameter, point, jet, tensor, matrix, instance rank, invariant normalization or graph scalar.

Copy exactly these seven files, preserving relative paths, into a newly empty directory:

1. PROOF.md
2. INPUTS.json
3. REPRODUCE.md
4. verify.py
5. characters.py
6. inputs/ranksix-common-kernel.md
7. inputs/mixed-jet-pairing.md

Run with Python's standard library only:

    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH= python verify.py
    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH= python -O verify.py

The result objects must be identical and report PASS. Runtime conditions use explicit exceptions and remain active under -O. The imported fixed character module separately performs 81 exact-rational McKay checks. No network, package installation, large computation, historical enumeration, candidate search or remote write occurs during replay.

The complete immutable originals are PR1219 at 95137a91303d46fd945f5a2d0fed330f0e32df8c and PR1221 at 84b418e22f03b5718409bdeb23ae353ecc4eb681. INPUTS.json fixes their exact paths, full bytes, SHA256 and Git blob SHA1. The proof SHA256 is d4ff280dc943c2a112ea68ff4d9c4750fe5f93b3892d8a104fa9c08aa5960568.

An independent reviewer must read the entire proof and both complete originals, freshly authenticate them against immutable repository path and Git blob responses, inspect the checker, and replay only the seven files above in a fresh isolated directory. The whole-proof verdict must bind this exact proof hash. Reviewer records and result JSONs are publication evidence but are not replay inputs. Local fetch records, scratch audits, caches and publication manifests are excluded from publication.
