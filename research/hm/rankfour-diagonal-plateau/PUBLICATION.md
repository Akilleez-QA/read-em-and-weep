# Portable publication: ordered maximal rank-four (2,2)

This packet proves one conditional geometric exclusion: the actual ordered maximal rank-four plateau (2,2) is impossible under the five retained actual-geometric inputs pinned in `INPUTS.json`. It makes no claim of generic SF rank at least five, square surjectivity, full-adjoint invertibility, or a repair of the original theorem.

The proof retains length-twelve torsion and all five center-even stabilizer characters. Nine degree cases give 359 cohomology tuples; torsion-safe horizontal-subbundle tests leave 172, including 40 positive-defect cases. Every remaining case forces a rank-five, degree-minus-22 endpoint of generic derivative rank one. Its complete invariant flag requires 18 to equal zero or at least 48, a contradiction. No additional four-source theorem or actual-instance matrix evaluation is used.

In the accumulated conditional coarse ledger, this removes one bin: 23 to 22 overall, five to four at rank four, and 92 to 88 with four source labels. The remaining rank-four ordered bins are (3,1), (2,1), (1,2), and (1,1). The preceding partial cubic-image bound does not close (3,1).

## Reproduce

Run `python3 check_publication.py` from any working directory. The wrapper authenticates every manifest-listed file, checks the fourteen-file accepted-author snapshot, replays author normal/optimized checks and 28 mutation controls, and invokes the independent normal/optimized replay and 22 mutation controls. The independent replay compares the complete 359-tuple and 172-tuple sets, not just their counts. Python standard library only; checks do not depend on assertions.

The frozen author verifier reports 26,178 checks. The portable independent verifier reports 11,331 checks. `independent-review/REVIEW.md` records the mathematical review and its retained-premise boundary. All five pinned public source documents are included unchanged; the rank-one flag theorem is included directly. The top-level author proof, verifier, result files and controls are byte-identical to the accepted snapshot.

`MANIFEST.json` authenticates all other publication files, including the wrapper and independent inventory. `independent-review/MANIFEST.json` authenticates the independent packet. The wrapper verifies these inventories both before and after replay. Neither the tests nor this packet constitute a proof-assistant certificate.
