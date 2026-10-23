# Four-pair composition certificate

The new source126 quotient restriction assigns residual Types I and II to the same dual bundle and Type III to a second dual bundle. Conditional on that reviewed theorem and the pinned six-pair predecessor, its two removed pairs are (E10,Q231) and (E10,Q249). The two retained source126 pairs are (E10,Q129) and (E10,Q157). This is a new quotient restriction, not the earlier overdue source2 ledger correction.

The exact new partition is 6=2+4. Its four survivors are distributed 2+1+1 over the same three stable labels. Source127 and source2 rows are preserved exactly. Numeric identifiers are recovered from coefficient tuples and bundle multisets, with multiplicities retained; they are not assumed intrinsic. The tests transport the entire calculation through a nontrivial E and Q catalogue reindexing and block reordering.

## Reproduction

    python verify.py
    python test_verify.py
    python -O verify.py
    python -O test_verify.py

The predecessor remains immutable at inputs/six.json. Input hashes are in pins.json. The generator writes only the new frontier.json when explicitly run with --write. The test suite rejects wrong scopes, ambiguous semantic matches, duplicate/missing cuts, wrong dual orientation, double application, and unjustified label decrements.

## Prerequisites and scope

The six-pair checkpoint is published in PR940 at commit7e3a97c554da608360f6bd96ac4606e970741378. Its exact SHA256 is9042fa6453037f77b0bff5765e04a92b4f596c85575f4f7d63866db5aa6d8677.

The source126 theorem is published in PR941 at commit c14af3d39881197edd781aa06cb1e918ef8fd42a, research/hm/source126-dual-specialization/PROOF.md, with independent PASS in REVIEW.md. Exact final proof, review and RESULT.json hashes are recorded in publication.json. All 19 integration tests pass normally and under optimization; the prerequisite checker independently passes 288 checks in both modes.

The checker establishes exact composition and semantic catalogue matching. It does not prove the geometric theorem merely by running Python, evaluate an actual HM instance, exclude any full stable label, or claim a complete proof repair. A count of four necessary pairs is not a completion percentage or a count of all remaining proofs.
