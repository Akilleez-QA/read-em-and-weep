# Independent checks

From the packet root:

    python3 verify.py > author-normal.json
    python3 -O verify.py > author-optimized.json
    cmp author-normal.json author-optimized.json
    cmp author-normal.json RESULT.json
    python3 review/independent_check.py > review-normal.json
    python3 -O review/independent_check.py > review-optimized.json
    cmp review-normal.json review-optimized.json
    cmp review-normal.json review/independent-result.json

The independent checker uses only the standard library and relative paths. Its path locator was adapted for this nested publication layout; the mathematical controls and reviewed author artifacts are unchanged. fresh-sources.json contains the complete independently fetched public source text, checked against the author's retained source bytes. The independent expected result is separate from the author's RESULT.json. REVIEW.md binds the reviewed author's proof, verifier, manifest, result and reproduction document by SHA256.
