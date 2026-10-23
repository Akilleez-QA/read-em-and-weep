# Reproduction

Run `python verify.py` and `python -O verify.py` in this directory. The checker authenticates all nine immutable originals, checks the exact original10/13 row identities, and verifies the fixed character/degree witnesses in PROOF.md. It imports only the new bounded character helper characters.py and standard Python. It does not execute any historical enumeration or actual-instance computation.

The deterministic RESULT.json was generated with `python verify.py --write`. Its bookkeeping confirms the implications of the written proof; it is not a substitute for geometric necessity or a realization theorem. This slice does not import any later profile21 exclusion: its eight residual rows are intentionally kept until a separate proof closes them.
