# Reproduce the W-positive structural exclusion

Run from this directory:

    python verify.py > RESULT.replay.json
    python -O verify.py > RESULT.optimized.replay.json
    cmp RESULT.json RESULT.replay.json
    cmp RESULT.replay.json RESULT.optimized.replay.json
    python review_verify.py > REVIEW-RESULT.replay.json
    python -O review_verify.py > REVIEW-RESULT.optimized.replay.json
    cmp REVIEW-RESULT.json REVIEW-RESULT.replay.json
    cmp REVIEW-RESULT.replay.json REVIEW-RESULT.optimized.replay.json

The author uses fixed physical McKay products; the independent checker imports no author implementation. Both bind the exact proof and mandatory complete immutable inputs with checks active under Python optimization. The only rank bounds checked are symbolic bounds from the one already proved source K and fixed target representation. No matrix of an actual map is constructed or evaluated. The seven capacity integers are the unique rank-one sequence forced in the proof, not a search over possible flags.

REVIEW-AUTHENTICITY.json independently authenticates the three original inputs. The actual full coefficient system is imported from its proved immutable theorem, not assumed in earlier arguments. REVIEW-INDEPENDENT.md audits the entire proof: exact cubic image and the missing rank-seven alternative, actual saturation of G0 and its projected dual annihilator, constancy of the ten-space, the universal derivative kernel, the exact saturated O(2) image and the elementary seven-step kernel capacity. Numerical checks support but do not replace those arguments or machine-certify imported geometry.

All dependencies required by these commands are included among the selected publication files. No actual HM/source coefficients, parameters, points, jets, tensors, matrices, instance ranks, broad candidate domain or historical enumeration are used. The result excludes only the W-positive decomposable top-degree-four primal form. Together with the preceding scalar-positive exclusion it removes both decomposable branches, but it does not exclude the separate triplet-positive form or close the top-four locus or full profile.
