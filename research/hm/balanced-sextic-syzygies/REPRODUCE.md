# Reproduction

Requires Python 3 standard library only.

Run from this directory:

    python verify.py
    python -O verify.py

Both outputs must agree exactly with RESULT.json. The checker authenticates all three pinned public source files against INPUTS.json and checks universal characters and degree identities. It does not evaluate actual HM data or rerun the historical profile enumeration.

PROOF.md contains the mathematical argument; finite checks do not substitute for it. The imported characters.py is a byte-identical pinned public helper. The complete original reference and full PR1145 proof are retained in inputs/.

Independent review and controls are in independent/. Run:

    python independent/independent_check.py
    python -O independent/independent_check.py

Both outputs must match independent/RESULT.json. The independent checker is self-contained.
