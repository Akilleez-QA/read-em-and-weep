# Independent rank-four (3,2) review

Conditional PASS for the ordered maximal generic-rank-four plateau (3,2) exclusion only.

- `REVIEW.md`: independent whole-proof geometric and arithmetic review.
- `verify.py`: exact conjugacy-class and ordinary-deficit implementation, with no author-code imports.
- `RESULT.json`: all fourteen necessary Euler survivors and both rejecting-character columns.
- `ENDPOINTS.json`: complete independently enumerated endpoint domains.
- `test_controls.py`, `CONTROLS.json`: normal/optimized replay and nine executed negative controls.
- `INPUTS.json`, `inputs/`: four complete immutable originals.
- `author/`: final reviewed proof, checker, output, input manifest, and originals.
- `MANIFEST.json`: publication-file authentication inventory.

Run `python3 verify.py`, `python3 -O verify.py`, and `python3 test_controls.py`.
The first two outputs match `RESULT.json`; the last matches `CONTROLS.json`.
All programs resolve their inputs relative to their files, not the current directory.
The public review omits only references to a superseded packaging inventory;
its mathematical review, final proof/checker/output hashes, and replay verdict are unchanged.
