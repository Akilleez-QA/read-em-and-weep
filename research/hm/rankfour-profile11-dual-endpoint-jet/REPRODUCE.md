# Reproduce the intrinsic first-jet endpoint checks

Run from this directory:

    python verify.py > RESULT.replay.json
    python -O verify.py > RESULT.optimized.replay.json
    cmp RESULT.json RESULT.replay.json
    cmp RESULT.replay.json RESULT.optimized.replay.json
    python review_verify.py > REVIEW-RESULT.replay.json
    python -O review_verify.py > REVIEW-RESULT.optimized.replay.json
    cmp REVIEW-RESULT.json REVIEW-RESULT.replay.json
    cmp REVIEW-RESULT.replay.json REVIEW-RESULT.optimized.replay.json

The author checker uses physical McKay recurrence in characters.py. The independent checker uses closed conjugacy-class characters and does not import the author's implementation. Both check only fixed low-degree representation/Hom identities and rank-degree identities appearing in the proof. No actual coefficients, points, jets, tensors, matrices, instance ranks, global bundle domain or source search is evaluated. The simple numerical semantic controls do not assert occurrence of altered data.

INPUTS.json pins two complete immutable original inputs, including the previously published constant-span/defect theorem. REVIEW-AUTHENTICITY.json records fresh independent full-byte authentication of both sources. The author and independent checkers bind the exact reviewed proof SHA256. REVIEW-INDEPENDENT.md reviews the entire geometric derivation, including the actual constant linear series rather than a complete one, the physical equivariant jet/Euler comparison, and saturation inside the coherent transpose source. These are mathematical reviews, not proof-assistant certification of imported geometry.

All files needed for these commands are selected in PUBLICATION-MANIFEST.json. No unshipped earlier-stage notes or files are needed. The conclusion excludes only the split small dual endpoint, forces the balanced endpoint and its exact actual derivative, and identifies the original next dual kernel. Both positive primal forms remain conditional necessities, original defect twelve remains unchanged, and the separate triplet-positive branch is outside scope.
