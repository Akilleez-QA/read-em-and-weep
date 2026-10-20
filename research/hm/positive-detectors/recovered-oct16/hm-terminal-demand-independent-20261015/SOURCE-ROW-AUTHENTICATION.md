> Historical prerequisite proof from 15 October 2026; recorded checks are not new runs. See the common PUBLICATION-SCOPE.md.

# Fresh row authentication and counting correction

Read October 15, 2026 from commit 08b73637d4136f91606aad332c46cafd064417f8, research/hm/current-scalar-geometric-dependencies/data/model.json, blob fcd48a9a22d40d55ce7a08b8aefcb4eaa2fdf761.

The source gives gamma[0,:]=(0,0,v1,v4,0), gamma[1,:]=(0,0,0,v2,v0), gamma[5,:]=(0,-v3,0,0,-v2), gamma[6,:]=(-v3,0,-v4,0,0). The two ev rows are (v0,v1,v2,v3,v4,0,0,0,0,0) and (0,0,0,0,0,v0,v1,v2,v3,v4).

For a bottom-degree W:K3→K0, d_End W has F20=W ev and F31=gamma W. Substituting the displayed source rows proves the four detector expressions annihilate this incoming differential exactly. All 40 cases (four detectors times ten elementary W) were checked by sparse integer coefficient addition directly against freshly fetched model JSON; all zero. No geometric source polynomial product or residual evaluation was performed.

This freshly authenticates the twelve entries as chain-map rows, including their signs, independently of the lost receipts. It does not freshly prove completeness on the relevant sector or the historical assignment of names h,j,p,r; those remain separate statements.

Fresh PR1 comment 6141322825 §7 defines Pi by independent sums over alpha0,...,alphaq, with alpha=(carrier,mask), and §2.2 sums over staircase permutations. Consequently a degree-four terminal sum has 24 staircase permutations, each with five independently summed source-vertex labels. The standard e_i are fixed by each staircase. A phrase such as '24 times 5 common labels' must not be interpreted as 120 total summands. The naive upper enumeration is 24×96^5 before exact support and alternation exclusions. This is only combinatorial metadata, not a proposed computation.

Source links:
- https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-geometric-dependencies/data/model.json
- https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6141322825
