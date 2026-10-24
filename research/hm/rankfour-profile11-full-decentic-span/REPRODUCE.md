# Reproduce the full degree-ten coefficient-span checks

Run from this directory:

    python verify.py > RESULT.replay.json
    python -O verify.py > RESULT.optimized.replay.json
    cmp RESULT.json RESULT.replay.json
    cmp RESULT.replay.json RESULT.optimized.replay.json
    python review_verify.py > REVIEW-RESULT.replay.json
    python -O review_verify.py > REVIEW-RESULT.optimized.replay.json
    cmp REVIEW-RESULT.json REVIEW-RESULT.replay.json
    cmp REVIEW-RESULT.replay.json REVIEW-RESULT.optimized.replay.json

The author checker uses fixed McKay character products. The independent checker imports no author code and uses closed conjugacy-class character polynomials. Both bind the exact proof and mandatory complete immutable input, and their counted RuntimeError checks survive Python optimization. Only two fixed coefficient representations, multiplicity bounds, dimensions and rank-degree identities are checked. There is no bundle candidate scan or actual coefficient, parameter, point, jet, tensor, matrix or instance-rank evaluation.

REVIEW-AUTHENTICITY.json records fresh byte-exact retrieval of the complete PR1202 source. REVIEW-INDEPENDENT.md checks the full geometric argument, particularly the difference between a subbundle and a genuine direct summand, the actual constant direct sum in the excluded case, and saturation of its annihilators. Numerical checks do not replace this argument or certify imported geometry by a proof assistant.

All required files are selected in PUBLICATION-MANIFEST.json. The conclusion derives the full eleven-dimensional coefficient span of the surviving actual O(-10) line and the ten-dimensional constant kernel of its dual coefficient map. It does not retroactively assume completeness in earlier proofs or assert a horizontal splitting in the surviving case. No further primal exclusion or realization is claimed by this packet.
