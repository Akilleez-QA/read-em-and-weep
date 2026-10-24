# Reproduce the constant-span and defect checks

From this directory:

    python verify.py > RESULT.replay.json
    python -O verify.py > RESULT.optimized.replay.json
    cmp RESULT.json RESULT.replay.json
    cmp RESULT.replay.json RESULT.optimized.replay.json
    python review_verify.py > REVIEW-RESULT.replay.json
    python -O review_verify.py > REVIEW-RESULT.optimized.replay.json
    cmp REVIEW-RESULT.json REVIEW-RESULT.replay.json
    cmp REVIEW-RESULT.replay.json REVIEW-RESULT.optimized.replay.json

The author checker uses the physical McKay recurrence in characters.py. The independent checker uses closed conjugacy-class characters over Q(sqrt(5)), with a binomial symmetric-character formula and no author implementation import. Both check only fixed representations, all five abstract C5 stabilizer weights, the seven zero-defect and four positive-defect rank-two scalar degree partitions, and rank/degree inequalities. These partitions are forced first by rank, parity and total degree in the proof; neither checker generates a global bundle or source domain.

Author semantic controls alter the allowed constant quotient dimensions, determinant-defect bounds, a missing trivial representation and the tail-defect equality. They diagnose the particular necessity argument, not occurrence of modified data. No actual coefficients, parameter values, points, jets, tensors, matrices or instance ranks are evaluated.

INPUTS.json pins three complete original sources. REVIEW-AUTHENTICITY.json records independent fresh GitHub retrieval and full-byte, hash and Git-blob agreement for each. The independent checker binds the reviewed proof SHA256. REVIEW-INDEPENDENT.md audits the sheaf and connection arguments mathematically, including the genuine constant complement, universal Veronese derivative, original defect identification, and all stabilizer characters. None of this is proof-assistant certification of the imported actual geometry.

The exact conclusion applies only to the two decomposable top-four primal forms: minimal constant span twenty-one, original defect twelve, and two necessary rank-two small dual endpoint forms. Their two surviving stabilizer characters remain distinct even though their induced characters agree. No surviving primal or dual form is asserted realized or excluded, and the separate triplet-positive branch remains open.
