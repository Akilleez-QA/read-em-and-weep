# Frozen rank-four maximal (3,3) exclusion

## Scope and stack

This packet excludes only generic rank four with maximal ordered Gauss
plateau lengths `(k,l)=(3,3)`, conditional on the actual geometric premises
stated in `PROOF.md`. The physical parameter line and representation
marking are fixed throughout. No rank-three exclusion is transplanted.

The publication is stacked on the [necessary remaining-rank partition,
PR #1171](https://github.com/Akilleez-QA/read-em-and-weep/pull/1171), at
commit `8497b6e793f36c14448fecdf88d209971273e069`, branch
`null/remaining-rank-strata`. Its [frozen partition proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/8497b6e793f36c14448fecdf88d209971273e069/research/hm/remaining-rank-strata/PROOF.md)
has SHA256 `4e3444e45d39cab9f45d31b8c204fa8749b076e33a5ccc55a6fe2e06d20038ed`.
Relative to its 27 necessary bad coarse bins, this removes exactly one,
leaving 26. These are necessary containers, not realizable configurations
or a completion denominator. The nine bad rank values 4 through 12 are
unchanged. No rank-at-least-five, positive-square surjectivity,
full-adjoint invertibility, or original-repair conclusion follows.

The new exclusion itself does not require the global rank-four lower
bound: it is a contradiction under the particular rank-four (3,3)
hypothesis. That previously established bound and the partition are used
only to describe the remaining coarse overlist.

## Frozen artifacts and public inputs

The author's entire packet is retained byte-for-byte at this directory's
root. Its historical `COORDINATION.json` is a public-source checkpoint,
not a mathematical premise. The independent packet is retained
byte-for-byte in `independent/`, including its exact `reviewed/` copies.

- `PROOF.md`: SHA256 `7fac6f279bc25dcc0561743dfae189dd70f2cf98e81ad11371745f1c954d4e6a`.
- `verify.py`: SHA256 `debf8427b38d9fc7a0d1f71c11b0096edf4f730d6d0189af2eaea7aec7e275cd`.
- `independent/REVIEW.md`: SHA256 `833f49eda36b097bda48790b31c08dd557926d2a73333a1e09a98f72de891b4e`.
- `independent/check.py`: SHA256 `0c977043a983cd0d5d3f5ba6c343d6aee92287e7d051db5ec4fb374be927fd98`.

`INPUTS.json` supplies the original immutable public URLs, byte lengths,
SHA256 values and Git blob identities for the three author inputs.
The additional general changing-rank source retained for the independent
review is [RANK-TWO-GAUSS-PLATEAU-NECESSARY-BOUND.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/RANK-TWO-GAUSS-PLATEAU-NECESSARY-BOUND.md),
SHA256 `868b89283fc98d276b8c9833f16d3dd16fe2b6a98a326769ce43d3a7e46d8b3c`.
Only its general derivative/sheaf facts are used, not its rank-two conclusion.
`independent/INPUTS.json` authenticates ten retained input artifacts;
`independent/SHA256SUMS` binds that review packet. The top-level
`SHA256SUMS` binds every publication file except itself.

## Reproduction and verification boundary

No nonstandard Python dependencies are needed. From this directory:

    python3 verify.py > author-normal.json
    python3 -O verify.py > author-optimized.json
    cmp author-normal.json RESULT.json
    cmp author-optimized.json RESULT.json
    python3 independent/check.py > review-normal.json
    python3 -O independent/check.py > review-optimized.json
    cmp review-normal.json independent/RESULT.json
    cmp review-optimized.json independent/RESULT.json
    sha256sum -c SHA256SUMS
    (cd independent && sha256sum -c SHA256SUMS)

Both scripts also run by absolute path from any working directory.
Normal and optimized output were reproduced byte-for-byte both from the
publication directory and an unrelated directory, eight executions total.
The final author certificate records 768 controls. The independent checker
does not import the author program; it reconstructs exact class characters,
the endpoint identity, the source deficit, the complete forced quotient
window, and both negative-tail cohomology corrections.

The whole written proof has independent conditional mathematical PASS.
This is not proof-assistant verification. Hashes establish exact source
bytes, not the truth of all transitive geometric prerequisites. The scripts
check universal arithmetic; the written proof supplies actual geometry,
sheaf extension, saturation, and persistence. No actual HM coefficient,
parameter, jet, matrix, instance rank, or historical enumeration is evaluated.
