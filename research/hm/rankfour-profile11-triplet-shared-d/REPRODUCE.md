# Reproduce the shared-D exclusion checks

Run from this directory with ordinary Python 3:

    python verify.py
    python -O verify.py

The verifier uses only the standard library and the fixed physical-W character recurrence in characters.py. It checks the exact immutable input commit/path pins in INPUTS.json, the complete retained source texts, byte lengths, SHA256 and Git blob SHA1, and the frozen whole-proof-reviewed proof hash. It also verifies the displayed finite representation identities and rank/degree contradictions. Its explicit checks remain active under python -O. No raw connector response is needed for offline replay.

PROOF.md contains the actual geometric proof. In particular, the verifier is not a replacement for the actual annihilator extension, canonical Harder-Narasimhan identification, constant-span splitting, and principal-parts arguments. No actual parameter, coefficient, point, jet, tensor or matrix is selected or evaluated, and no bundle-candidate or height scan is performed.

The exact input commits and paths are in INPUTS.json. The independent review and compact fresh source-authentication results are recorded separately. Raw fetch responses remain local audit material and are intentionally omitted from the publication slice. INDEPENDENT-REVIEW-FIXED-CHECKS.json records the reviewer's separate arithmetic results; verify.py is the runnable checker for the selected publication files. The mathematical proof covers only PR1205's full-positive coherent-image branch and leaves all other endpoint-image alternatives unchanged.
