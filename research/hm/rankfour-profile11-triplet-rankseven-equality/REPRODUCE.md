# Reproduce the bounded checks

Use Python 3 and only its standard library:

    python verify.py
    python -O verify.py

Both runs must report PASS and the frozen proof SHA256 a6e56f535af652d3ff437cc5041527636f601751ae24285ba1ec91670f4db7ae, with the same explicit check count.

The exact isolated replay set contains eight files:

* PROOF.md
* INPUTS.json
* REPRODUCE.md
* verify.py
* characters.py
* inputs/common-kernel-ladder.md
* inputs/nine-jets.md
* inputs/deep-images.md

Copy only these selected files with their relative paths into a newly empty directory. Exclude LOCAL* files, working and follow-on drafts, independent scratch audits, reviewer raw fetches, old outputs and caches. Verify selected bytes remain unchanged after both runs.

The verifier pins the complete proof and all three complete direct sources by byte length, SHA256 and Git blob SHA1. It checks fixed physical characters, exactly three displayed quotient-rank counts, the equality/slack degrees, auxiliary source/saturation degrees, corrected normal targets 12,14,16, the three zero-case capacity bounds and nonzero degree gains, and the residual rank-two quotient arithmetic. The character module separately checks 81 fixed exact-rational McKay identities. This is bounded universal arithmetic, not an actual coefficient, parameter, point, jet, tensor, matrix, instance-rank or normalization evaluation and not a broad candidate scan.

All main checks use explicit require calls and remain active under -O. Independent whole-proof review must separately audit the coherent equality flags, first ramified saturation, every actual normal projection, generic rank-one behavior of saturated auxiliary jet spans, persistence of Q, negative top, and the precise remaining claim boundary. Arithmetic checks do not substitute for that geometric proof.
