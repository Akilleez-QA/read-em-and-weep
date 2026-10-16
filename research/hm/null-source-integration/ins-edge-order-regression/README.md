# INS01 output-edge order API regression

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
