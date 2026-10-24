# Reproduce the bounded checks

Use Python 3 and only its standard library. From this directory run:

    python verify.py
    python -O verify.py

Both runs must report PASS with the same explicit check count and the frozen proof SHA256 a9b56b6f84c9a11dedb94639bf16ab5c1065e21a91d067c52f75435d4b014da2.

The exact isolated replay set has eight files:

* PROOF.md
* INPUTS.json
* REPRODUCE.md
* verify.py
* characters.py
* inputs/twenty-exclusion.md
* inputs/defect-capacity.md
* inputs/projected-ranktwo.md

Copy only these files, retaining relative paths, into a newly empty directory before the independent replay. Exclude LOCAL*, INDEPENDENT-ORIENTATION-PROOF.md, reviewer raw fetches, previous output records, caches, and all other exploration. Verify the selected bytes are unchanged after both runs.

The verifier checks the complete pinned proof and three source files by exact byte length, SHA256, and Git blob SHA1. Its mathematical checks are only fixed small physical character identities, the eleven-term coherent capacity sum, the displayed normal degrees, Serre-duality degree, and exact-sequence rank/degree arithmetic. characters.py additionally checks 81 fixed McKay identities over exact rational pairs. No actual coefficient, parameter, point, jet, tensor, matrix, instance rank, source normalization, or broad candidate scan is evaluated.

All main checks use explicit require calls and remain active with -O. Computation does not prove the actual-geometric steps: whole-proof review must separately check the backward-kernel coherence, absence of horizontal residue, actual normal orientation, torsion restriction, equivariant cohomology, and saturation of the common kernel.
