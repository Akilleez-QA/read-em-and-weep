# Static ID0 certificate

This bundle proves the seed-relabeling and single-quotient extraction claims for frozen retained detector ID0: outputs8,40,72 with weights1,2,1. It contains mathematical exposition, a standard-library static checker, immutable public-source pins, and exact copies of the mathematical premises. It does not contain or enable a physical-source adapter.

## Reproduce

Requirements: Python3.10 or later; an already available checkout of Akilleez-QA/read-em-and-weep at commit `e93cf712f9da4926a8450cc870ed45a7bfc379ab`. No network, additional packages, production imports, or physical execution is used by the checker.

From this bundle directory:

    python check_certificate.py --source-root /path/to/read-em-and-weep
    python -O check_certificate.py --source-root /path/to/read-em-and-weep

Alternatively pass the checkout's `research/codex-swarm` directory as --source-root. A directory containing just the23 source files in source-pins.json, with their relative subdirectories preserved, also suffices. The checker verifies every file's immutable SHA256 and Git blob identity before parsing any source AST. It never imports or evaluates repository code. No output files are written by the checker; its report goes to stdout.

Expected result: both runs produce identical JSON with status `static and invented algebra controls passed`, source_files_verified23, invented_polynomial_products195, and all physical-execution fields false. The included reports record these successful runs. The original proof must still be read: passing hashes and toy tests do not establish the imported geometric theorems.

## Immutable inputs

All23 repository source records are in source-pins.json, with direct commit-pinned public URLs:

https://github.com/Akilleez-QA/read-em-and-weep/tree/e93cf712f9da4926a8450cc870ed45a7bfc379ab/research/codex-swarm

The core source locations are:

- detector-realization/program.py: complete preterminal source sum and old terminal
- detector-realization/raw_engine.py: full raw source/model
- scalar-compiler/compiler.py: residual and HPL recursion
- inserted-coefficients/interfaces.py: full owner identity and source ordering
- exact-curve-field/field.py: exact denominator division
- full-lift-domain/lift.py: homogeneous degrees, whole-domain obligations and J3

The bundle also pins these mathematical premises by byte identity:

- premises/PROOF.md: corrected full-alternation proof, SHA256 e43de2abc2838f2d5e31c3fd45fc9517c963e3ad9c8a605f00ec62b50263bab9
- premises/COMMON_FRAME_CORRECTION.md: exact common-ambient normalization, SHA256 a88442758260f080d7c5c6d871b27522a60263cec6a8669e3956d63d7ff71bc7
- premises/REVIEW.md: corresponding corrected independent review, SHA256 e155fa2d432bfa4e4c673fc31cd4c66dc80d2af02e1ce0683a07a80e60978f39
- premises/weighted-requests-30.json: retained request metadata, SHA256707663b97c3a8289d6531172a1c509e54ceccb3185a6e07f4f28153fbc119375

These included mathematical texts contain their own source links. They are inputs to this certificate, not results proved by this checker. The corrected comparison is A^E=-L^t; the superseded extra scalar-shift comparison is not a premise.

The retained ID0 object is checked against its literal expected fields, indices, exponents and weights. Its original published full-family metadata is [weighted-requests.json at the immutable source pin](https://github.com/Akilleez-QA/read-em-and-weep/blob/e93cf712f9da4926a8450cc870ed45a7bfc379ab/research/codex-swarm/detector-selection/weighted-requests.json), SHA256 f256746fbfd0897fd4a5241e13715198004d277fec700b7ba5c4b3ace9bfe5e0. The checker does not fetch that file or recompute its rank theorem.

## Exact scope

The shared-quotient theorem is mathematical: factor B=x^d C, certify A=CQ once, then read the three coefficients of Q at shifted exponents. Every lookup must refer to the same complete rational and frame. A future implementation still needs guarded lifetime/context checks, exact weighted metering, complete transitive authentication and its own admission. This package neither evaluates D0 nor changes any existing guard.
