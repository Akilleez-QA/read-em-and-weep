# Source126 nilpotent generation restriction

The invariant-positive-compatible algebra acts faithfully on its first negative-pencil endpoint. For the Type III residual template, the pure X radical arrow has a forced nonzero P channel under the canonical invariant quadric, rank four. The X-target row is onto V+P, rank seven. Thus Type III's two-dimensional radical reduces to at most one compatible direction, necessarily with nonzero Y component.

These are new necessary compatibility restrictions, not scalarity, source exclusion or the complete repair. All four surviving source-dual pairings and three stable labels remain unchanged. The conclusion uses actual generation and the equality of aggregate-positive and invariant images, not only the abstract kernel/cokernel characters.

- PROOF.md: mathematical argument and scope.
- INPUTS.json and inputs/: original authenticated proof bytes.
- verify.py: 1326 checks, including 1008 finite parity-factorization regressions, exact fixed-character arithmetic and synthetic negative controls.
- RESULT.json: deterministic output.

Reproduce using Python3, with no third-party dependencies:

    python verify.py
    python -O verify.py

Both runs give identical results. No actual HM coefficients, points, parameters or selected-instance ranks are evaluated. The checks are not proof-assistant verification.
