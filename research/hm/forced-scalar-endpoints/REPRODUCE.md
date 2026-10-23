# Reproduce the scalar endpoint restriction

Use Python 3 standard library only, in this directory:

    python3 verify.py > /tmp/scalar-normal.json
    python3 -O verify.py > /tmp/scalar-optimized.json
    cmp RESULT.json /tmp/scalar-normal.json
    cmp RESULT.json /tmp/scalar-optimized.json

All inputs have exact public commit pins, full original bytes, SHA256, Git blob SHA1 and lengths in INPUTS.json. The verifier authenticates these before importing the retained character module. The normal and optimized runs use explicit failure checks rather than assertions. No actual-instance coefficient or evaluation is part of this reproduction. PROOF.md supplies the geometric argument; the checker is a supporting exact universal certificate, not proof-assistant formalization.
