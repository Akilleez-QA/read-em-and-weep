# INS01 output-edge order API regression

## Fix verification

Accepted at immutable commit 9cd60c44f1cc3a732b58dcf1575be5c2539f8f17. The unchanged test_edge_order.py passes in both normal and optimized Python: the reversed edge now raises the intended ValueError. Three additional constructor-only synthetic controls in test_guard_scope.py pass in both modes. They confirm that equal physical labels with different increasing standard tags remain accepted, repeated common labels with different occurrences are rejected, and auxiliary-first ordering is used. No physical source or coefficient evaluation is involved.

With both test files copied to the repository root, reproduce against the fixed commit:

    PYTHONPATH=research/codex-swarm/inserted-coefficients python test_edge_order.py -v
    PYTHONPATH=research/codex-swarm/inserted-coefficients python -O test_edge_order.py -v
    PYTHONPATH=research/codex-swarm/inserted-coefficients python test_guard_scope.py -v
    PYTHONPATH=research/codex-swarm/inserted-coefficients python -O test_guard_scope.py -v

The subsequent commit 7d73d540981a3a152d807c39844ec63bc9913b89 changes overview/status/readback documentation only; its INS implementation is unchanged. The constructor still intentionally accepts only increasing nonrepeated common edges: callers must implement alternating extension of the complete result outside this raw API. Other physical-input, extension, support and admission obligations remain separate.

## Original finding

Reviewed repository: https://github.com/Akilleez-QA/read-em-and-weep
Initial immutable commit: bc34cfc960095326ba6eb87de215810136c2d954
Rechecked against immutable commit: 691c9b1d5b268186c490995c52a886cdc9eebf0b (same failure).
Affected file: research/codex-swarm/inserted-coefficients/inserted_program.py
Affected function: PrismProgram.__init__, lines 98–111 (edge validation at lines 99–100 on the rechecked commit).

Place test_edge_order.py in your repository root and run against either pinned commit:

    PYTHONPATH=research/codex-swarm/inserted-coefficients python test_edge_order.py -v

Expected current result: FAIL, because N(a,b)=-1 and N(b,a)=0 at exponent (0,0,0,0), although alternating extension requires N(b,a)=1. All data are artificial constants; no physical catalog, source program, polynomial evaluation or coefficients are imported or executed.

Output owners are (1,'a',1,0,8) and (1,'b',2,0,12), in the FullOwner field order (seed,occurrence,carrier,legal_mask,standard_tag). Ca=Cb=Z=Qhat=1 and B=0. The tag8 fiber is carrier3/mask0; the tag12 fiber is carrier4/mask0. The source is constant1 on sorted carrier triple(2,3,4), zero on all others, with the existing SourceSlice providing the permutation sign. For forward order the inserted owners are (1,('inserted','a','b','u'),3,0,8) and (1,('inserted','a','b','v'),4,0,12); reversed order exchanges fiber/tag assignments and uses ('inserted','b','a',role). The complete synthetic witness construction is in the test.

The mathematical precondition is in research/hm/null-source-integration/combined-pole/PROOF.md section3 at commit 02d0e727ffb95dfd9281906cc284c56e8bffd018: evaluate raw formula on an increasing source-first common output edge, then extend the complete result alternatingly. This test exercises acceptance of an out-of-domain edge; it is not a counterexample for valid increasing calls or a claim that this artificial source is a closed physical source.

Minimal safe fix: reject reversed/repeated common edges in PrismProgram.__init__ using the auxiliary-first carrier/mask/tag source key. Alternatively implement a complete-result alternating wrapper, consistently transporting B, witnesses, Ca/Cb and fibers. Sorting only the inserted source tuples does not fix output order. The test accepts an explicit ValueError for the reversed input as a correct API fix.

## Fixed-seed scope check

Read the inherited source-integration.json at PR85 commit 82a8785d0a23e8d4e44e9ca4f52c8bb24fdadbdc. All four seed12/30 output edges are increasing; this finding does not demonstrate an error in those valid calls:

- N_12_2_3: (12,2,2,11,13) -> (12,3,4,15,15)
- N_12_1_2: (12,1,1,9,9) -> (12,2,2,11,13)
- N_30_3_4: (30,3,3,7,14) -> (30,4,4,15,15)
- N_30_2_3: (30,2,2,3,12) -> (30,3,3,7,14)
