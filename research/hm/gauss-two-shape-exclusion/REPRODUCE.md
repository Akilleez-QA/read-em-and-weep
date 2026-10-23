# Reproduce the bounded formal checks

Run from this directory with Python 3 and the standard library:

    python verify.py
    python -O verify.py

Each command authenticates seven complete pinned originals and reproduces RESULT.json exactly. The source files in inputs are read as documents/data only. No historical program is executed and no quotient enumeration is rerun.

The checker verifies the character identities, degree and rank arithmetic, both formal target splittings, the exact forced kernel coefficients and final multiplicity contradiction. It filters the already fixed historical 182-row list for the two proved shapes solely to record their original stable IDs, ordered quotient pairs and determinant defects. It does not infer that the list is geometrically necessary from its JSON labels. The actual-source geometric proof is in PROOF.md and requires independent mathematical review, not just a successful program run.

characters.py authenticates its tensor-W recurrence against exact character values on all nine conjugacy classes. The review independently computes the necessary representation multiplicities by class averages rather than using that recurrence. No actual HM coefficient, chosen parameter, point, jet, tensor, matrix, source-instance rank or scan is evaluated.

The core theorem assumes the exact D-type actual source and uses its original Gauss embedding. Its application to every source type additionally imports the primary four-type theorem at PR1123. The published visibility lemma is pinned at PR1129. This packet does not establish COV or repair the original theorem.
