# Reproduce the bounded checks

Use Python 3 with its standard library. From this directory run:

    python verify.py
    python -O verify.py

Both commands must report PASS and the frozen proof SHA256 44ee429fa26b65b68b2668ce69dff219e4a4daf0a6bdaa9fac0e94aa8a631b3a, with the same explicit check count.

The exact isolated replay set has eight files:

* PROOF.md
* INPUTS.json
* REPRODUCE.md
* verify.py
* characters.py
* inputs/twelve-orientation.md
* inputs/projected-ranktwo.md
* inputs/deep-images.md

Copy only these files with their relative paths into a newly empty directory. Do not copy LOCAL* files or directories, independent scratch audits, previous output records, reviewer files or caches. Check all selected bytes remain unchanged after both runs.

The verifier authenticates the complete frozen proof and all three complete direct sources by pinned byte lengths, SHA256 and Git blob SHA1. The mathematical checks consist only of a coefficient-level polynomial identity, six explicitly displayed universal rank/degree stages, the endpoint equality arithmetic, and the fixed Sym4=D identity. The character module separately verifies 81 fixed McKay identities over exact rational pairs. No actual scalar-line coefficients, parameters, points, jet values, tensors, matrices, instance ranks or normalizations are evaluated, and no candidate splitting scan is performed.

All main checks use explicit require calls, so optimization does not disable them. The checker is not the geometric proof: independent whole-proof review must verify the actual negative backward flags, coherent quotient injections, annihilator transposition, generic next jet rank, saturated regular factorization, equal-degree global isomorphisms, and conditional endpoint interpretation.
