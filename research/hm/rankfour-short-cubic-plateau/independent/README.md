# Independent rank-four (1,3) review

Verdict: PASS for the precise conditional maximal-plateau exclusion, not all rank four or original proof repair.

- `REVIEW.md`: complete independent review and scope.
- `independent_check.py`, `RESULT.json`: independent exact character arithmetic and complete necessary-domain checks.
- `verify_review.py`, `CONTROLS.json`: normal/optimized/portable reproduction, all-candidate cross-comparison, and executed negative controls.
- `INPUTS.json`, `inputs/`: four complete immutable source documents.
- `reviewed_author/`: exact hash-bound reviewed proof, verifier, result, and retained inputs.
- `MANIFEST.json`: SHA256 inventory.

Run `python3 verify_review.py`. All programs require only the Python standard library. No actual map instance or historical classification is evaluated.
