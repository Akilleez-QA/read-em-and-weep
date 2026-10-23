# Reproduce the independent review

From this directory, run:

    python3 independent_check.py > /tmp/scalar-independent-normal.json
    python3 -O independent_check.py > /tmp/scalar-independent-optimized.json
    cmp RESULT.json /tmp/scalar-independent-normal.json
    cmp RESULT.json /tmp/scalar-independent-optimized.json

The checker, review, manifest and result preserve their reviewed bytes. Complete immutable public inputs are retained locally for portable reproduction. AUTHOR_FETCHED.json mentioned in the historical review is a retrieval record, not a required input; the public pins and authenticated blob hashes are in INPUTS.json.
