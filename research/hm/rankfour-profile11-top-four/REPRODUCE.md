# Reproduce the fixed top-four reduction checks

From this directory run:

    python verify.py > RESULT.replay.json
    python -O verify.py > RESULT.optimized.replay.json
    cmp RESULT.replay.json RESULT.optimized.replay.json
    cmp RESULT.json RESULT.replay.json
    python review_verify.py > REVIEW-RESULT.replay.json
    python -O review_verify.py > REVIEW-RESULT.optimized.replay.json
    cmp REVIEW-RESULT.replay.json REVIEW-RESULT.optimized.replay.json
    cmp REVIEW-RESULT.json REVIEW-RESULT.replay.json

The author verifier uses the physical nine-vertex McKay recurrence, authenticated against exact characters by characters.py. The independent verifier uses closed class characters over Q(sqrt(5)) and the class-size inner product. The thirteen scalar-top shapes and one triplet-top shape are fixed inputs already proved by symbolic rank partitions in PROOF.md; no quotient domain is generated or scanned. Each capacity has a square-completion upper certificate and one displayed attaining height witness. No height search is used. The two final kernel exclusions inspect only individual irreducible negative blocks whose genuine cubic H1 budget has dimension at most six; no kernel-bundle domain is generated.

verify.py executes twelve semantic mutation controls. The first eight are: adding the missing W to M3; adding a trivial constituent to M2; adding a second A_std to M2; adding a second V internal target in the source-V dimension argument; and adding a V constituent to each of the four quartic characters. The final four relax the two dual-sign thresholds and add a second V to each small-kernel derivative target. These verify the declared decisive obstruction, not occurrence of modified data. Source-Hom tests use only fixed small universal products, never actual coefficients or map instances.

INPUTS.json pins four complete immutable source originals. REVIEW-AUTHENTICITY.json records the reviewer's separate fresh GitHub fetch and full-byte, Git-blob and SHA256 comparisons. REVIEW-INDEPENDENT.md records the whole-proof review and exact reviewed proof hash. Byte authentication verifies provenance, not the imported actual geometric premises.

The exact conclusion is three necessary quotient forms, all forcing source D, for maximum ordinary degree four in actual maximal rank-four profile (1,1), for every determinant defect. No surviving form is asserted realized, no profile is closed, and no coarse-bin count changes.
