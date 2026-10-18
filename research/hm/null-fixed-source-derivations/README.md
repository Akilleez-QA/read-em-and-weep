# Fixed-source incidence and derivation constraint

Read RESULT.md for the standalone result, THEOREM.md for the full proof and extension caveats, and REVIEW.md for the independent audit and verification limits.

Run these portable checks without executing any production source:

    python verify.py
    python -O verify.py
    python check_derivations.py
    python -O check_derivations.py

Optional provenance check against separately supplied complete inert source files:

    python verify.py --source-dir /path/to/inert/inputs

The packet includes only 20 bounded verbatim function excerpts. Full source hashes and reviewed mathematical-input hashes identify the inherited inputs; they are not remote-repository authentication. The complete fixed-field proof is included. No independent H24 coefficient, total cancellation, physical nonvanishing or impossibility of source deformations is asserted.
