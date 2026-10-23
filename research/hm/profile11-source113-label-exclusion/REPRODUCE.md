# Reproduce the original ten-source coverage audit

Run with Python 3 and the standard library:

    python verify.py

The verifier reads coverage.json and the two original catalog files in audit-inputs, checks their immutable Git blob hashes, selects original source_index 113, verifies the stable-label identity and exact quotient endpoints, and compares all ten original tuples with the ten coverage rows. It also checks the two direct strict-top multiplicity contradictions using fixed binary-icosahedral character arithmetic in characters.py.

The original files are:

- https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/one-one-endpoint-necessary-pairs.json
- https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/rank-three-quotient-frontier-144.json

Place their exact bytes under audit-inputs with the displayed filenames. The verified Git blob hashes are respectively fe0afa410d89340d3082dc814277f89fbb582c19 and 8b5971092f9ef762584912609fd5e9301c4e271d.

PROOF.md gives the immutable URLs and commits for every source-cut theorem and the original splitting/strict-top inputs. coverage.json contains the same exact pins in machine-readable form. source-proof-pins.json records the independently fetched Git blob and SHA256 hashes for the six distinct whole-source theorem files and the additional PR861 dependency. The verifier checks that these seven immutable records cover exactly the referenced theorem URLs and contain complete hash fields; the written review separately authenticates those hashes against the retrieved GitHub bytes. The full theorem audit copies are not required by the verifier or republished. The independent written review checks source-theorem scope and the PR861 dependency of PR868; the script does not purport to re-prove those geometric source theorems.

An independent audit is also provided as review_independent.py. It does not import characters.py: it uses the even A5 character table and Clebsch-Gordan recurrence, independently checks every original decoder rank/degree, and authenticates all seven source-theorem blobs. To run it, first add these audit inputs:

- ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md and NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md from the same original commit and directory as the two catalogs above.
- Each exact theorem file at the seven immutable URLs in source-proof-pins.json, saved under audit-inputs with that manifest's corresponding key as its filename, for example PR881-BF.md.

Then run:

    python review_independent.py

The theorem copies are audit inputs, not republished artifacts. The independent script verifies their Git blob and SHA256 hashes before checking the dependency mapping. Its geometric scope conclusions still rely on the written review rather than string matching.

Expected output begins:

    PASS: original stable label and endpoints; exact ordered ten-tuple set

This is a fixed ten-row coverage audit, not a search, model enumeration, source-instance evaluation or current global frontier recount. The mathematical conclusion is exclusion of the one original stable label G3.11.ad509d55173f under the pinned frontier hypotheses. No global pair count is produced.
