# The split low-positive label is excluded by exhaustion of its ten sources

## Statement and exact original source list

The original-zero-defect profile-(1,1) label

    G3.11.863639aa192e,
    A_q=O(-10)+O(4)+O(6), B_q=O(-8)+O(-6)+O(8),
    source_index=69,

is impossible under the pinned actual-bundle and Gauss-profile hypotheses: every source tuple in its complete original necessary list is excluded by the structural results below.

The original inputs are at commit db51525015bb7c5e825833d550d08dedf6f6ea96 of Akilleez-QA/read-em-and-weep:

- research/hm/order-four-quadratic-load/one-one-endpoint-necessary-pairs.json, Git blob fe0afa410d89340d3082dc814277f89fbb582c19;
- research/hm/order-four-quadratic-load/rank-three-quotient-frontier-144.json, Git blob 8b5971092f9ef762584912609fd5e9301c4e271d;
- research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md, Git blob b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3.

https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load

The stable-label record identifies source index69. Its exact necessary-pair record lists precisely the ten tuples with a=d=g=0, h=1 and b+c+e+f=2. The complete actual bundle decoding is

    E=(cV+(e+1)P+fD) O(-2)+bT O(-3)+cV O(-4)
      +eWp O(-5)+f O(-8)+O(-10).

The e term contributes an extra P to the top coefficient, in addition to Wp O(-5). Every listed source has rank17 and degree-54: its rank is 5+6(b+c+e+f), and its degree is -18-18(b+c+e+f).

Strict-top injects the nonzero top coefficient of every listed source into

    H0(A_q(2))=Sym6 W+Sym8 W=V+2P+D.

Thus its actual top image never has generic rank zero. Each subsequent rank-one/rank-two partition below is exhaustive.

## Proof dependencies

P814 is [the rank-two polar proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/1f94be65b3a470a1b594e61d56df7f6057c9d907/research/hm/profile11-low-positive/PROOF.md), commit 1f94be65b3a470a1b594e61d56df7f6057c9d907, SHA256 f0bd13d85ae8a890dbec84e5f15b7ec8605b04f474d5c7d80faeb3aa08f4defc. R814 is [the rank-one bb exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/1f94be65b3a470a1b594e61d56df7f6057c9d907/research/hm/profile11-low-positive/RANK-ONE-TOP-EXCLUSION.md), at the same commit, SHA256 2f480884b26a089bcd6f3633e75e790472cc493d9908dd83f0497c6b1fbe8d50.

P826 is [the split-ce constant-span exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/96734783c561c2baca8f91d69772318446898f06/research/hm/profile11-split-ce-constant-span-exclusion/SPLIT-CE-CONSTANT-SPAN-EXCLUSION.md), commit 96734783c561c2baca8f91d69772318446898f06, SHA256 e3c1cb16be8ed7714cb2c3d5f6a3ba9f7da85567aa5a53e100b2d3458fc977bd.

P828 is [the horizontal quotient exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/ae077cbe42d65cde27d65ce88923dc35851b6952/research/hm/profile11-horizontal-quotient-exclusion/HORIZONTAL-CONSTANT-QUOTIENT-EXCLUSION.md), commit ae077cbe42d65cde27d65ce88923dc35851b6952, SHA256 a637a5ba2c69b460bd2e058ea26100b4d2830e1b4f72fd823bae1dbba6e8701a.

P830 is [the split-bf rank-two nonzero-channel exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/620d5598ccc19e5e1c458a4cddb0d3a0709d83c3/research/hm/profile11-split-bf-rank-two-exclusion/SPLIT-BF-RANK-TWO-NONZERO-CHANNEL.md), commit 620d5598ccc19e5e1c458a4cddb0d3a0709d83c3, SHA256 d762e23c6b402bf8bfd62160e310ecacf601a910d47f6a3e278cd8a3806657f6.

P836 is [the onto-bb exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/c6b6ec427e5690055c18c181fad39efd6624cc83/research/hm/profile11-onto-bb-exclusion/ONTO-BB-SOURCE-EXCLUSION.md), commit c6b6ec427e5690055c18c181fad39efd6624cc83, SHA256 4fbecacfb401cad0b82f3e5990d56fc0da65af6b493596ea6a8cadce16d8ca98. Its complete top-image alternatives come from [PR821](https://github.com/Akilleez-QA/read-em-and-weep/blob/0d7e1e7312a114ded8a2c49ed1a7ca2f4d7e4c7f/research/hm/profile11-onto-rank-four-top/ONTO-RANK-FOUR-TOP-SUBSYSTEMS.md), commit 0d7e1e7312a114ded8a2c49ed1a7ca2f4d7e4c7f, SHA256 87244e453597105dffb298743c1725ac29b00c8b8dc1cafad37f55235c81ea34.

Psplit is PR844 at immutable commit c86ed140ecd1371d2881727094f56230bdd04b85, in [research/hm/profile11-split-backward-exclusion](https://github.com/Akilleez-QA/read-em-and-weep/tree/c86ed140ecd1371d2881727094f56230bdd04b85/research/hm/profile11-split-backward-exclusion), and consists of the following exact companion proofs.

- [SPLIT-BACKWARD-DESCENT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/c86ed140ecd1371d2881727094f56230bdd04b85/research/hm/profile11-split-backward-exclusion/SPLIT-BACKWARD-DESCENT.md), SHA256 ee1096f2368fee248792c35feeb3c689a134b8e1a84934c9699575fbe920ee1a;
- [SPLIT-BC-SOURCE-EXCLUSION.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/c86ed140ecd1371d2881727094f56230bdd04b85/research/hm/profile11-split-backward-exclusion/SPLIT-BC-SOURCE-EXCLUSION.md), SHA256 22910f2176448710de765823ee872bcb43ead8e300a9ebdf65e6a16b0307f40e;
- [SPLIT-BF-BACKWARD-INTERFACE.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/c86ed140ecd1371d2881727094f56230bdd04b85/research/hm/profile11-split-backward-exclusion/SPLIT-BF-BACKWARD-INTERFACE.md), SHA256 b5924ec48fe1dd7583b37d75d47b8ef1ec3f0b3a589744349ebf924c08de4a61;
- [SPLIT-BF-SOURCE-COROLLARY.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/c86ed140ecd1371d2881727094f56230bdd04b85/research/hm/profile11-split-backward-exclusion/SPLIT-BF-SOURCE-COROLLARY.md), SHA256 3f7aec33779fe0a1e85069cd734ecbe9bbe44ba956ffcde0c4a42852c51ead48.

## Exhaustive source accounting

This is exactly the original compatible_E_types order. The coordinates are (a,b,c,d,e,f,g,h).

1. ff = (0,0,0,0,0,2,0,1). Its top coefficient P+2D cannot inject into V+2P+D. This is the existing strict-top pruning recalled in P814, not a new removal counted here.
2. ef = (0,0,0,0,1,1,0,1). The two top P copies separately supply the O(4) and O(6) rows, forcing the top map onto. P814's rank-two polar obstruction excludes this entire source.
3. ee = (0,0,0,0,2,0,0,1). Its top coefficient 3P cannot inject into V+2P+D. This is existing strict-top pruning.
4. cf = (0,0,1,0,0,1,0,1). The top V and D supply separate basepoint-free O(4) and O(6) rows. P814 forces the actual constant P and projected standard linear subsystem; P828 excludes the source by the horizontal projected-lattice contradiction.
5. ce = (0,0,1,0,1,0,0,1). The two P copies force the top map onto. P814 supplies the actual constant D and standard projected subsystem. P826 excludes the source through the exact constant-span intersection and invariant determinant-degree22 contradiction.
6. cc = (0,0,2,0,0,0,0,1). Its top coefficient 2V+P cannot inject into V+2P+D. This is existing strict-top pruning.
7. bf = (0,1,0,0,0,1,0,1). In top rank two, the nine top sections force saturation; P814 excludes the zero internal channel and P830 every nonzero internal channel. In top rank one the image is the complete O(6), and Psplit's bf interface and source corollary exclude that branch by the universal split descent. Hence the whole source is excluded.
8. be = (0,1,0,0,1,0,0,1). The two top P copies force the top map onto. P814's rank-two polar obstruction excludes the entire source.
9. bc = (0,1,1,0,0,0,0,1). P814 excludes top rank two, which is automatically saturated by its seven independent top sections and the invariant-divisor bound. In rank one, an O(6) saturation is excluded by the missing V in Sym8, while lower degrees have too few sections; the image is the complete O(4). Psplit's bc proof excludes both alternatives for the lower T-to-O(6) channel and all subsequent top-channel/defect branches by the universal split descent.
10. bb = (0,2,0,0,0,0,0,1). R814 excludes top rank one. In top rank two the generated-image bound allows only defect zero or twelve. PR821's classification forces a defect-twelve image to be Wp O(-1); it cannot inject generically with rank two into O(4)+O(6), because its O(4) row is zero equivariantly. Thus the top map is onto. PR821 gives exactly two actual constant-span possibilities, the degree-eight system and the P-conic; P836 excludes both. Hence the whole source is excluded.

The three inherited strict-top removals ff,ee,cc are retained solely to exhibit the complete original source exhaustion, not counted again as new source pairs. Likewise ce is assigned once to P826; the alternative horizontal-lattice proof in P828 does not create an additional source removal.

## Exact descent interface and independence

For the remaining rank-one bf and bc branches, the separate initial arguments both establish the actual quotient

    K_1/K_2=O(2)+O(4),
    rank K_2=12, deg K_2=-60, maxdeg K_2<=-4,
    chi_G(K_2(4))=V-A,
    chi_G(K_2(5))=-W+Wp+2T.

The actual derivative target of K_2 is the subbundle (K_1/K_2)(-2)=O(0)+O(2) of (H O/K_2)(-2). Its induced map has exactly the actual derivative kernel and raw image. The kernels remain saturated in the same constant ambient bundle, and the profile-(1,1) backward rank bound is at most two. These are precisely the hypotheses of the source-free split theorem, not merely matching abstract splitting characters.

That theorem rederives every split quotient without substituting a balanced-target result. In particular it retains the new K_4=D O(-6)+O(-8)+Wp O(-11) branch and both possible terminal invariant degree-twelve defects. The actual defective quotient, rather than its saturation, supplies the next derivative target and yields the strict-top or horizontal-kernel contradiction. Thus neither application has a missing torsion branch.

The dependency graph is noncircular. Each initial bf or bc proof establishes the interface before invoking the universal split theorem. The latter assumes neither source exclusion and neither label exhaustion; its bounded support inputs are the public representation identities and actual-kernel lemmas. The other source exclusions were proved independently of the present complete-label conclusion.

## Conclusion and boundary

Every actual realization of this stable label would use one of the original ten splitting types. Each is contradicted, with all top ranks, internal channels, initial lower channels, and possible divisor defects accounted for. Therefore G3.11.863639aa192e is excluded.

This is one stable-label exclusion, not a realization count, not an exclusion of all profile-(1,1) labels, and not a proof of the global HM completion problem. No frontier arithmetic beyond this one label is asserted. The source-list and structural arguments use no selected actual HM/source coefficients, parameters, points, evaluated derivatives, matrices, instance ranks, selected models, experiments, scans, or unapproved large computation.
