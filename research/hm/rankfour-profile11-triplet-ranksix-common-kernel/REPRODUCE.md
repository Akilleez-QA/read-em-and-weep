# Reproduce the bounded checks

Use Python 3 and only its standard library:

    python verify.py
    python -O verify.py

Both runs must report PASS and proof SHA256 06e1795f1390e8451dbf4e98e10a8011b3e97ce733ec6b1cbbd5af90b4694111, with identical explicit check counts.

The exact isolated replay set consists of seven files:

* PROOF.md
* INPUTS.json
* REPRODUCE.md
* verify.py
* characters.py
* inputs/rankseven-equality.md
* inputs/nine-jets.md

Copy only these files with their relative paths into a newly empty directory. Exclude LOCAL* files, independent scratch work, other drafts, reviewer fetches, prior outputs and caches. Check that every selected byte remains unchanged after both runs.

The verifier authenticates the entire proof and both complete sources by exact lengths, SHA256 and Git blob SHA1. Its mathematics is limited to fixed small physical character identities and the displayed exact-sequence rank/degree arithmetic. characters.py additionally checks 81 fixed exact-rational McKay identities. There is no actual coefficient, parameter, point, jet, tensor, matrix, instance-rank or normalization evaluation and no candidate scan.

Explicit require calls remain active with -O. The actual projection arguments, equivariant splitting uniqueness, coherent versus fiber ranks, exact kernel and forward span, and whole-bundle-only constant-span claim require the separate independent entire-proof review; the checker does not prove them.
