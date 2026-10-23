# Fifteen-axis occurrence and simple ambient base scheme

PROOF.md proves that the universal nonic pencil contains the fifteen-axis orbit exactly on alpha+beta=0, and that its ambient local ideals there are maximal ideals. The complete conditional base scheme on that line has length 49.

Run `python verify.py` and `python -O verify.py`; both produce RESULT.json byte for byte. The checker uses SymPy and exact rational arithmetic with sqrt(5). INPUTS.json records immutable public source commits, paths, Git blob hashes and SHA-256 digests. model.py is copied unchanged from its pinned source.

Only PROOF.md, README.md, verify.py, model.py, INPUTS.json, RESULT.json, the three files under inputs/, and any final independent review receipt form the reproducibility packet. Exploratory scripts and outputs are not dependencies.
