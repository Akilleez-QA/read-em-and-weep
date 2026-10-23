# Reproduce the frozen P-source target certificate

From this directory, with Python 3 standard library only:

    python3 -B verify.py > result-normal.json
    cmp RESULT.json result-normal.json
    python3 -B -O verify.py > result-optimized.json
    cmp RESULT.json result-optimized.json
    python3 -B independent/independent_check.py > independent-normal.json
    cmp independent/RESULT.json independent-normal.json
    python3 -B -O independent/independent_check.py > independent-optimized.json
    cmp independent/RESULT.json independent-optimized.json

The production result contains 559 explicit checks and 81 character-module controls. The independently implemented class-character checker contains 2509 checks. Production indices are zero-based. Independent records use one-based row numbers, except the explicitly named forced_nonzero_cubic_zero_based_indices field. Both use explicit exceptions, not optimization-disabled assertions. Production and independent results have distinct schemas and separate frozen RESULT files.

INPUTS.json authenticates seven immutable public originals, including characters.py. The independent AUTHENTICATION.json records eight independently read public originals; the eighth is the original actual-splitting theorem, linked at its immutable commit. The independent checker’s default input path was adjusted only for this portable directory layout; the hash-bound proof, production checker, inputs, and frozen results remain unchanged. REVIEW.md preserves the separate mathematical review and its scope.

The original 159 records are read, never regenerated. Counts are historical, not live. There are zero incremental exclusions beyond PR1140. Eight retained records force an actual Euler factorization under the P-source hypothesis, not an all-source exclusion or realization claim. The original proof repair remains open.
