# Direct maximal-profile (2,2) cover

This focused package proves a conditional necessary three-pair quotient cover
for the actual maximal rank-three Gauss profile (2,2), using the immutable
four-source theorem and actual bundle/persistence inputs in SOURCE-PINS.json.
The proof and verifiers do not import the historical source-pair ledger, record
files, or enumeration scripts. Listed pairs are necessary possibilities, not
asserted realizations. Their exclusion is a separately pinned older terminal
theorem, not a fresh actual-rank calculation.

## Files and reproduction

- PROOF.md: complete intrinsic finite window, every necessary filter, positive
  determinant-defect handling, and terminal transfer.
- verify_direct22_cover.py: standalone exact Q(sqrt(5)) character verifier.
- independent_mckay_replay.py: independently written integer McKay recurrence
  and recursive rank-budget enumeration.
- test_compare_replays.py: complete-domain, full-stage-set, 279-product, ordered
  survivor, seven-counterfactual-control, and wider-window comparisons.
- RESULT.json and INDEPENDENT-RESULT.json: exact ordered survivor pairs.
- CROSSCHECK-RESULT.json: complete comparison results.
- PUBLIC-INDEPENDENT-REVIEW.md: portable independent mathematical review,
  arithmetic checks, unchanged reviewed artifact hashes, and public provenance.
- SOURCE-PINS.json: six immutable public source paths, Git blob IDs, and SHA-256
  hashes, each authenticated before publication.
- MANIFEST.json: hashes of all published package files except the manifest.

With Python 3 and no third-party dependencies, from this directory:

    python verify_direct22_cover.py
    python -O verify_direct22_cover.py
    python independent_mckay_replay.py
    python -O independent_mckay_replay.py
    python test_compare_replays.py
    python -O test_compare_replays.py

The author verifier passes 837 checks and seven counterfactual controls. The
independent enumeration contains 1,130 shapes and stage sizes
134 -> 25 -> 23 -> 10 -> 3 -> 3. All three programs have byte-identical ordinary
and optimized outputs. The author verifier writes only its local RESULT.json;
no source download is needed to reproduce the finite calculations. The written
geometric proof, rather than those finite outputs alone, establishes necessity.

## Boundary and relation to the rank bound

This is a shorter necessary cover under the newer four-source premise, replacing
the historical enumerator chain for this profile when applying the pinned
terminal three-pair theorem. It is not a new rank bound or a new branch cut.

This package does not itself establish a global SF bound, maximal rank,
positive-square surjectivity, full-adjoint invertibility, a Bockstein order,
or completion of the original proof repair. Its conclusion is the exact
conditional necessary cover stated in PROOF.md.
