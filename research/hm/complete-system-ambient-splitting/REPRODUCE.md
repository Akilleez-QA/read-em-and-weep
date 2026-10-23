# Reproduce the universal graph identities

Python 3 with SymPy 1.14.0 was used. From this directory:

    python verify.py > replay.json
    diff -u RESULT.json replay.json

Expected: 78 formal cases and 17,709 passing assertions. All graph entries and residual-polynomial coefficients remain independent symbols. No actual source data or parameter values are substituted. These are exact algebraic identity tests, not a search or numerical sample. The proof establishes the saturation and second-fundamental-form consequences that the symbolic checker alone cannot establish.

The independent source-copy check compared inputs/pr1138.md from the existing reviewed packet with a fresh immutable GitHub fetch in inputs/pr1138-remote.md; the bytes match. inputs/pr1142.md is also the full immutable proof. Public coordination was read through comment 6375020455, where the actual height-seven application remains with its owner. INPUTS.json records these sources and the frozen theorem/checker/result hashes. The general theorem is proved directly and does not logically depend on the profile-exclusion proofs; those inputs only document the conditional application's scope.

No GitHub writes were performed by this task.
