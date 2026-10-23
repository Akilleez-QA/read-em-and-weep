# Reproduce the source-113 bc audit

The written proof is PROOF.md. It is the mathematical deliverable; the verifier is only a bounded arithmetic and catalog cross-check, not a proof of the geometry or Lean certification.

Run with Python 3 and the standard library:

    python verify.py

characters.py supplies exact Q(sqrt(5)) character arithmetic for the nine irreducible binary-icosahedral representations. verify.py checks only a fixed set of universal characters, four declared kernels and their internal Hom spaces, degree arithmetic, dual cohomology, and the exact original catalog entry. It does not evaluate an actual HM/source coefficient, parameter, point, derivative, matrix or rank, and does not scan models or enumerate a frontier.

The two catalog JSON files in audit-inputs are checked against their Git blob hashes from immutable commit db51525015bb7c5e825833d550d08dedf6f6ea96. If preparing a lean publication without vendoring copies, retrieve exactly:

- https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/one-one-endpoint-necessary-pairs.json
- https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/rank-three-quotient-frontier-144.json

The theorem inputs, independently retrieved and hash-checked in this review, are:

- ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md, blob b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3.
- NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md, blob d7506dae49b4be43230450c4132bd5db91f137ef.

All four originals are under the same immutable commit and directory. The proof pins its additional exact dependencies PR861 and PR868 directly and restates every argument used.

Expected output begins:

    PASS: pinned catalog hashes; all ten original tuples; exact bc source;

Scope is one whole source-edge exclusion for (0,1,1,0,0,0,0,1) at index 113. No label or frontier decrement is asserted here.
