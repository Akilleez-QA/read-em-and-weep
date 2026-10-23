# Reproduction and limits

Run from this directory with Python 3 (standard library only):

    python3 verify.py > normal.json
    python3 -O verify.py > optimized.json
    cmp normal.json optimized.json
    cmp normal.json RESULT.json

The verifier uses explicit exceptions, so optimization does not disable checks. It authenticates all four retained public inputs by length, SHA256 and Git blob ID. All polynomial checks are exact integer/rational coefficient identities, with the coordinate remaining formal. It does not choose or evaluate actual HM coefficients, parameters, points, jets, matrices, or ranks.

PROOF.md gives the all-degree geometric proof and the exact kernel/jet identity. The finite tests are regression checks, not proof-assistant verification or an experimental substitute for the proof. The D-source consequence is S_8=0 and therefore last nonzero index at most7. No remaining frontier record is declared excluded by this packet.
