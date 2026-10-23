# Reproduction

Use Python 3 with SymPy. From this directory run:

    python verify.py
    python -O verify.py

Both outputs must match RESULT.json byte-for-byte. The checker uses explicit failures, not assertions disabled by optimization. It authenticates all four complete public sources in INPUTS.json and checks the exact support/ambient classification, evaluation characters, Hilbert functions, formal apolar identities and universal derivative kernel/minors. It never evaluates actual HM source coefficients or a parameter value. The mathematical proofs of saturation, exact coefficient span and the abstract realization models are in PROOF.md; finite tests do not replace them.

The retained character source is copied unchanged as characters.py for self-contained reproduction. The optional --write flag regenerates the result only after every preceding control has passed.
