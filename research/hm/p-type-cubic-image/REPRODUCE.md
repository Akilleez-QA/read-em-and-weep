# Reproduction

Python 3 standard library only. From this directory run:

    python3 verify.py > RESULT.normal.json
    python3 -O verify.py > RESULT.optimized.json
    cmp RESULT.normal.json RESULT.optimized.json
    cmp RESULT.normal.json RESULT.json

The checker raises explicit errors rather than relying on assertions. It authenticates all five full public originals in INPUTS.json. characters.py independently constructs the nine physical irreducible characters from the exact Q(sqrt(5)) values and verifies tensoring by W; verify.py additionally verifies pairwise character orthogonality, the unique Euler representation, first occurrence in Sym7, the P-source quartic Euler characteristic, formal Euler chart exactness and sixteen virtual Euler twists.

No actual-instance coefficients, points, parameters, jets, matrices, or ranks are supplied to these scripts. Formal chart variables are not sampled. The checked algebra does not replace the saturation, graph-cancellation, and Gauss arguments in PROOF.md. No historical enumeration is run and no new live exclusions are counted.

characters.py is adapted from the public PR1140 universal checker, whose relevant mathematics and physical character source are pinned in INPUTS.json. The frozen original character-reference.py is retained as source evidence and is not executed by the checker.

## Independent reproduction

From this directory run:

    python3 independent/independent_check.py > independent.normal.json
    python3 -O independent/independent_check.py > independent.optimized.json
    cmp independent.normal.json independent.optimized.json
    cmp independent.normal.json independent/RESULT.json

The independent checker and review are retained unchanged. Its 682 explicit arithmetic controls supplement the written geometric review; they are not proof-assistant verification. AUTHENTICATION.json in independent/ records independent retrieval of the five complete originals retained in inputs/. The historical review reference to REVIEW-original-freeze.md identifies the superseded review, which is not included in this packet.
