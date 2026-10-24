# Reproduce the bounded checks

Use Python 3 with only its standard library:

    python verify.py
    python -O verify.py

Both runs must report PASS and proof SHA256 3e1ce0d1589d694d578796a90398cbdaf8fdf6fb340158b5098ad3f79cdfa95b with the same explicit count.

The exact isolated replay set has eight files:

* PROOF.md
* INPUTS.json
* REPRODUCE.md
* verify.py
* characters.py
* inputs/rankseven-equality.md
* inputs/nine-jets.md
* inputs/defect-capacity.md

Copy only these files with their relative paths into a newly empty directory. Exclude LOCAL* files, independent scratch audits, other drafts, reviewer fetches, prior outputs and caches. Check that selected bytes remain unchanged after both runs.

The verifier authenticates the complete proof and three complete direct sources by exact lengths, SHA256 and Git blob SHA1. It checks fixed small physical character identities, the finite formal mixed-jet rectangle, bidegrees, parity, the universal leading-symbol Vandermonde identity in degree twelve, and the representation dimension gap. The thirteen formal basis checks for the symbol use no coefficients of f12 and no actual source coefficients; they do not evaluate a point, matrix, tensor or instance rank. No eigenvalue or eigenvector is calculated. characters.py also checks 81 fixed exact-rational McKay identities. No broad candidate scan or large computation occurs.

All main checks use explicit require calls, active under -O. The actual mixed-jet containment, intrinsic diagonal argument, transvectant identification, rational Wronskian proof, exact kernel and quotient factorization, and all claim boundaries must be checked by the independent entire-proof reviewer. The executable arithmetic is not a substitute for that proof.
