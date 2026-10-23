# Reproduce the source-113 bf audit

PROOF.md is the written mathematical result. The verifier is a bounded arithmetic cross-check, not a substitute for the actual connection, saturation and exact-intersection arguments, and not Lean certification.

Run with Python 3 and its standard library:

    python verify.py
    python review_independent.py

characters.py implements the fixed binary-icosahedral character ring over Q(sqrt(5)). The independent review_independent.py instead uses the fixed McKay adjacency recurrence and does not import characters.py; it checks the same core character support, polar outcomes, changed Hom spaces and input identity by a separate implementation. The verifier checks the thirteen declared abstract kernel candidates, five exact kernels, their entire D/T/scalar internal Hom support, the two factor channels for rank-dropping D maps, six polar-character outcomes, all changed constant-span and lower-row Hom tests, the uniform full-span saturation budget and the original dual-endpoint contradiction.

The computation does not select or evaluate actual source coefficients, parameters, points, derivative values, matrices, ranks or models. It performs no scan, experiment or frontier enumeration.

The four original files belong in audit-inputs; verify.py checks their exact Git blob hashes. All are from commit db51525015bb7c5e825833d550d08dedf6f6ea96, under:

https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load

- ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md
- NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md
- one-one-endpoint-necessary-pairs.json
- rank-three-quotient-frontier-144.json

PROOF.md pins PR859, PR867, PR868 and PR877 and rechecks the changed D row and negative endpoints. The exact scope is the whole index-113 tuple (0,1,0,0,0,1,0,1), not an independently certified whole-label count.

Expected output starts:

    PASS: four original Git hashes; exact bf tuple; thirteen kernel candidates;
