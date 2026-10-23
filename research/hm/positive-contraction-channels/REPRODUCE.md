# Reproduction

Run `python verify.py` and `python -O verify.py` with Python and SymPy. Each runs 76 bounded checks: six authenticate the three immutable input proofs, and seventy check the universal representation tensors, traces, channel supports and sharpness example. No selected actual-source computation occurs. No assertion statement is used for a check, so optimization does not remove tests.

PROOF.md is the structural mathematical argument. The checker is a finite symbolic certificate, not formal proof-assistant verification. REVIEW.md records independent mathematical and code review. INPUTS.json identifies the exact source blobs and content hashes.
