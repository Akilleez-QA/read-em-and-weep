# Reproduce the direct profile-(1,1) closure certificates

Run from this directory:

    python3 verify.py > result.normal.json
    python3 -O verify.py > result.optimized.json
    cmp RESULT.json result.normal.json
    cmp result.normal.json result.optimized.json

The production checker authenticates all14 immutable originals, reads the fixed original159 necessary records, and supplies a full certificate for each ordered record. It does not execute inputs/original-verifier.py or regenerate the historical candidate universe. The copied compatible_E_types field is not read. The only numerical work consists of fixed universal character arithmetic and eight primal plus six dual integer capacity evaluations per original record.

The independently authored review and verifier under independent/ are separate from production. Follow their own reproduction instructions. The two review documents audit the full mathematics and its exact dependency/coverage boundary, not only counts. Their verdicts apply to the proof hashes they record.

The intended theorem is exclusion of actual maximal profile (1,1), conditional on the pinned actual inputs and the original written profile-specific necessity theorem. Global maximal-profile exhaustion is not supplied here. No actual HM/source coefficients, points, parameters, jets, tensors, matrices, instance ranks, scans, selected local model, historical enumeration rerun, or large computation are used.
