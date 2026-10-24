# Reproduce the bounded checks

Using Python 3 and only its standard library, run:

    python verify.py
    python -O verify.py

Both runs must report PASS and the frozen proof SHA256 0a24ab99c6f3d6c2f60212532c7f4aed2bd7d5fba17823243dd479a83a7308dd with the same explicit check count.

The selected isolated replay contains exactly seven files:

* PROOF.md
* INPUTS.json
* REPRODUCE.md
* verify.py
* characters.py
* inputs/nine-jets.md
* inputs/twelve-orientation.md

Copy only these files, retaining paths, into a newly empty directory. Exclude all LOCAL* records, working or follow-on drafts, independent scratch audits, reviewer records, old outputs and caches. Check selected bytes remain unchanged after both runs.

The verifier authenticates the complete proof and both complete direct sources by exact byte lengths, SHA256 and Git blob SHA1. It checks only the three displayed universal common-kernel degree stages, fixed capacity polynomials at their four/four/three possible quotient-rank counts, small physical character identities and defect-length arithmetic. These are not source-instance splitting candidates. characters.py separately checks 81 fixed exact-rational McKay identities. No actual coefficient, parameter, point, jet, tensor, matrix, instance rank or normalization is evaluated, and no broad scan is performed.

Explicit require calls remain active under -O. Independent whole-proof review must separately verify the actual derivative projections, transversality-based normal splitting, coherent image arguments, invariant Hom restrictions and saturated common-kernel/full-span conclusions. The checker is not a substitute for those geometric arguments.
