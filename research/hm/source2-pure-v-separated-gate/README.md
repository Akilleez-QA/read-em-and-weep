# Separated terminal graph and its two gate lines

PROOF.md identifies the two genuine separated-terminal cubic channels with
R1-4R2 and 3R1+2R2 through the actual PR1094 Spencer identity. Their
independence means the graph description alone imposes no linear gate
constraint, unlike the residual-large one-channel mechanism. The actual
graph and both functional components remain unselected.

Run `python verify.py` and `python -O verify.py` to reproduce RESULT.json.
INPUTS.json authenticates six immutable originals. The checker executes
only the small pinned universal model; historical verifiers are retained
as normalization evidence, not replayed. No actual HM instance is tested.
