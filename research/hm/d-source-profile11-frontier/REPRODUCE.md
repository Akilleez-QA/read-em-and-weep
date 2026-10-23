# Reproduce the fixed-list D-source frontier

Python3 standard library only, no network and no actual-instance inputs:

    python3 verify.py > replay.json
    cmp RESULT.json replay.json
    python3 -O verify.py > optimized.json
    cmp RESULT.json optimized.json

The checked result reports 1204 explicit require controls and 81 character-module controls. INPUTS.json authenticates nine immutable public inputs. The frozen 159-record list is read but never regenerated. Temporary replay files need not be committed.

Read PROOF.md for the geometric necessity, endpoint hypothesis, imported shape exclusions and limits. The output establishes only the stated D-source-conditioned necessary frontier.
