# The balanced low-positive label is excluded by exhaustion of its ten sources

## Statement and exact original source list

The original-zero-defect profile-(1,1) label

    G3.11.73682b4c817f,
    A_q=O(-10)+W O(5), B_q=W O(-7)+O(8),
    source_index=72,

is impossible: every source tuple in its complete original necessary list is excluded by the pinned structural results below.

The original inputs are at commit db51525015bb7c5e825833d550d08dedf6f6ea96 of Akilleez-QA/read-em-and-weep:

- research/hm/order-four-quadratic-load/one-one-endpoint-necessary-pairs.json, Git blob fe0afa410d89340d3082dc814277f89fbb582c19;
- research/hm/order-four-quadratic-load/rank-three-quotient-frontier-144.json, Git blob 8b5971092f9ef762584912609fd5e9301c4e271d;
- research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md, Git blob b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3.

https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load

The stable-label record identifies source index72. Its exact necessary-pair record lists precisely the ten tuples with a=d=g=0, h=1 and b+c+e+f=2. The actual bundle decoding is

    E=(cV+(e+1)P+fD) O(-2)+bT O(-3)+cV O(-4)
      +eWp O(-5)+f O(-8)+O(-10).

In particular the e term contributes an extra P to the top coefficient. Every listed source has rank17 and degree-54, since its rank is 5+6(b+c+e+f) and degree is -18-18(b+c+e+f).

## Immutable proof dependencies

P814 is [the rank-two polar proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/1f94be65b3a470a1b594e61d56df7f6057c9d907/research/hm/profile11-low-positive/PROOF.md), commit 1f94be65b3a470a1b594e61d56df7f6057c9d907, SHA256 f0bd13d85ae8a890dbec84e5f15b7ec8605b04f474d5c7d80faeb3aa08f4defc. R814 is [the rank-one bb exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/1f94be65b3a470a1b594e61d56df7f6057c9d907/research/hm/profile11-low-positive/RANK-ONE-TOP-EXCLUSION.md), at the same commit, SHA256 2f480884b26a089bcd6f3633e75e790472cc493d9908dd83f0497c6b1fbe8d50.

P823 is the two-part [third-backward quotient](https://github.com/Akilleez-QA/read-em-and-weep/blob/399abe93debe71232f0b7808fc8f1a5582118708/research/hm/profile11-balanced-bf-backward-exclusion/BF-THIRD-BACKWARD-QUOTIENT.md) and [finite backward descent](https://github.com/Akilleez-QA/read-em-and-weep/blob/399abe93debe71232f0b7808fc8f1a5582118708/research/hm/profile11-balanced-bf-backward-exclusion/BF-FINITE-BACKWARD-DESCENT.md), commit 399abe93debe71232f0b7808fc8f1a5582118708. Their SHA256 hashes are 16475cd7d6012fff2efd8d3ec04bce884231ffbfe664914e948584c24afa69d0 and 9558490385822a4d559d555c4f3372fd594e7ef0f504454da0707d962cf9fd49. The pinned quartic input is PR819 at 03fee9278072f9ac00a5fcee5deb04b7fce61ae5.

P828 is [the horizontal quotient exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/ae077cbe42d65cde27d65ce88923dc35851b6952/research/hm/profile11-horizontal-quotient-exclusion/HORIZONTAL-CONSTANT-QUOTIENT-EXCLUSION.md), commit ae077cbe42d65cde27d65ce88923dc35851b6952, SHA256 a637a5ba2c69b460bd2e058ea26100b4d2830e1b4f72fd823bae1dbba6e8701a.

P836 is [the onto-bb exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/c6b6ec427e5690055c18c181fad39efd6624cc83/research/hm/profile11-onto-bb-exclusion/ONTO-BB-SOURCE-EXCLUSION.md), commit c6b6ec427e5690055c18c181fad39efd6624cc83, SHA256 4fbecacfb401cad0b82f3e5990d56fc0da65af6b493596ea6a8cadce16d8ca98. Its exhaustive top-image inputs are [PR821](https://github.com/Akilleez-QA/read-em-and-weep/blob/0d7e1e7312a114ded8a2c49ed1a7ca2f4d7e4c7f/research/hm/profile11-onto-rank-four-top/ONTO-RANK-FOUR-TOP-SUBSYSTEMS.md) and [the PR819 cubic torsion proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/03fee9278072f9ac00a5fcee5deb04b7fce61ae5/research/hm/profile11-balanced-low-positive-subsystems/BALANCED-TORSION-CUBIC-SUBSYSTEM.md).

P838 is [the balanced bb torsion exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/8b9e7affe6906ead2927fb251e6b64b886020030/research/hm/profile11-balanced-bb-torsion-exclusion/BALANCED-BB-TORSION-DESCENT-EXCLUSION.md), commit 8b9e7affe6906ead2927fb251e6b64b886020030, SHA256 db935dd621f64b9336727919f4af4710ceeac03f432d567c9530db9ba5eb10e8.

Pbc is [the balanced bc exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/5951b547d07afe052bc6f823a3ac2b5f29963114/research/hm/profile11-balanced-bc-exclusion/BALANCED-BC-BACKWARD-EXCLUSION.md), PR839 at commit 5951b547d07afe052bc6f823a3ac2b5f29963114, SHA256 64e55ab01aa6811d9a87ea73282512633c807aeb8a29f9be2f3636f652303288.

## Exhaustive source accounting

The order below is the original compatible_E_types order, with tuples written in the original (a,b,c,d,e,f,g,h) coordinates.

1. ff = (0,0,0,0,0,2,0,1). Its top coefficient P+2D cannot inject into V+2P+D. This is the existing strict-top pruning recalled in P814, not a new removal counted here.
2. ef = (0,0,0,0,1,1,0,1). P814 excludes the entire source by its rank-two quadratic polar obstruction.
3. ee = (0,0,0,0,2,0,0,1). Its top coefficient 3P cannot inject into V+2P+D. This is existing strict-top pruning.
4. cf = (0,0,1,0,0,1,0,1). P828 excludes the entire source by the actual horizontal projected-lattice contradiction.
5. ce = (0,0,1,0,1,0,0,1). P814 excludes the balanced source because its forced O(8) subline cannot inject into W O(7).
6. cc = (0,0,2,0,0,0,0,1). Its top coefficient 2V+P cannot inject into V+2P+D. This is existing strict-top pruning.
7. bf = (0,1,0,0,0,1,0,1). Its nine-dimensional top coefficient forces rank two and saturation, as proved in P814. P814 excludes zero internal derivative, and P823 excludes the remaining nonzero internal channel. Thus the whole source is exhausted.
8. be = (0,1,0,0,1,0,0,1). P814 excludes the entire source by the rank-two polar obstruction.
9. bc = (0,1,1,0,0,0,0,1). P814 excludes top rank two; Pbc excludes the remaining top rank-one O(4) branch, including both possibilities for the lower T quotient channel.
10. bb = (0,2,0,0,0,0,0,1). R814 excludes top rank one. In top rank two the only possibilities are onto or a determinant-defect-twelve image Wp O(-1), by the generated-image bound and the invariant-divisor minimum, as detailed in PR821/PR819. P836 excludes onto, and P838 excludes the defect-twelve branch. Thus the whole source is exhausted.

The strict-top injection used in items1,3,6 is

    H0(E(2)) -> H0(W O(7))=V+2P+D.

These three previously discarded tuples are retained in the list solely to make the original ten-source exhaustion complete. They are not counted again as newly removed source pairs. Likewise the alternative ce argument in P828 is not counted separately from its P814 exclusion.

## Conclusion and boundary

Every actual realization of the stated stable label would have one of these ten actual equivariant splitting types by the original complete necessary list. Each has now been contradicted, with all top-image and internal-channel subcases accounted for. Hence G3.11.73682b4c817f is excluded.

This conclusion is one stable-label exclusion. It is not a realization count, not a claim about all profile-(1,1) labels, and not a proof of the global HM completion problem. No frontier arithmetic beyond removal of this one label is asserted here. The source list and proof deductions use no selected actual HM/source parameters, coefficients, points, evaluated derivatives, matrices, instance ranks, selected models, scans, or unapproved large computation.
