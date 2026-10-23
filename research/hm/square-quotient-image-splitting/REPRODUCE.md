# Reproduction and verification boundary

The two `audit-inputs/` copies mentioned in the proof are local verification inputs, not vendored publication files. Reconstruct them before running the verifier. From a checkout of Akilleez-QA/read-em-and-weep with the two pinned commits available, run the following from this package directory:

```sh
mkdir -p audit-inputs
git show db51525015bb7c5e825833d550d08dedf6f6ea96:research/hm/order-four-quadratic-load/HYPERPLANE-SQUARE-SURVIVORS.md > audit-inputs/SQUARE.md
git show 2f3eb11a6f55582e17f56c8bc9b310db9a37424d:research/hm/ninth-neighborhood-rank/PROOF.md > audit-inputs/RANK.md
python verify.py
python -O verify.py
```

Python with SymPy is required. Alternatively retrieve the original raw bytes at the exact commit/path pairs in INPUTS.json and save them to those same two filenames. Do not copy rendered HTML or normalize line endings. The verifier checks SHA256 and Git blob identities before reporting success.

The verifier checks formal transvectants of generic binary forms l³u and l³v with independent symbolic coefficients; the three highest-weight images at degree one; exact abstract SL2 and binary-icosahedral representation identities; rank/degree bookkeeping; the vanishing ambiguity spaces for equivariant complements; and immutable input hashes. These are universal identities, not selected actual HM/source forms or evaluated geometric instances.

The written proof supplies the vector-bundle splitting argument and its transfer to the actual image through the separately authenticated duality theorem. The verifier does not replace either argument with a finite sample and does not certify a complete geometric proof in a proof assistant.

Actual map coefficients, kernel splitting, opposite-bundle splitting, source realization and source/frontier exclusion remain outside the result.
