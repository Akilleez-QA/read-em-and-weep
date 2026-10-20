# Historical review receipt

This review concerns its original manuscript version, not the normalized publication bytes. It is not a final publication-scope approval.

# Independent refinement audit

The auditor checked the original symmetry reductions and the final 5,192-index pruning.

- Upper r≤s preserves upper-symbol span. It does not assert equality of the full upper values.
- Lower l≤h gives exact equality after the retained projector, because scalar multiplication commutes and retained filtration zero is zero.
- J1 has weights (c,4c²+epsilon) with epsilon=1,4. The literal W beta weights are ±2 and the Galois-conjugate W′ weights are ±1.
- Reversal sends c to 1-c and preserves epsilon. The two fixed lines c=3 are negative, using the independently established trace -2.
- Upper offset delta-(l-3a)² and all upper and lower pruning predicates are correct.
- The upper count is 100→80→64.
- The lower fixed-c table for delta=1,2,3,4 and difference squares 0,1,4 is respectively (1,1,2), (2,4,1), (2,1,4), (1,2,1). Thus every c contributes 4+7+7+4=22; all five give110, and excluding c=3 leaves88.
- Translation of the original labels by t sends (a,l,h) to (a+2t,l+t,h+t), hence c to c-t, preserving delta and epsilon. This validates using c=0 to count every c.
- Intermediate exclusions are redundant because their failure implies epsilon=2(h+3(a+l))² in {0,2,3}.
- The total is64·66+88·11=4224+968=5192.

Survivors are not asserted nonzero. Upper omissions are valid modulo the lower retained subspace; lower omissions are exact after projection. The remaining lower values span that subspace and the remaining upper symbols span its quotient, so the final spanning argument is sound.

Only static proof reads and symbolic finite representation combinatorics were used. No actual matrix, rank, multiplication instance, polynomial instance, residue, or operation-value evaluation was performed.
