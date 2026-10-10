# A local full-sign second-order residual

This experiment instantiates the second-order matrix residual on a fixed finite line chart. It computes exact rational mixed jets and verifies the resulting Čech cocycle equation at a specified point. It does not compute the residual's global Ext² class.

Let π=V1∧V2+V3∧V4, with Vi=yi∂xi on functions rational in x. On the fixed line chart, g is rational in x, and the first-order correction decomposes as u=y1y2 u12+y3y4 u34. The full-sign coefficient of the second-order residual is obtained after dividing by y1y2y3y4. Its product terms are
u12_jk u34_ij+u34_jk u12_ij.
Its first-order bidifferential terms are the four expressions obtained by applying μ1,12 to u34 and by applying μ1,34 to u12, in both matrix positions.
Its second-order Moyal term is
(1/4)[(∂13 g_jk)(∂24 g_ij)−(∂14 g_jk)(∂23 g_ij)−(∂23 g_jk)(∂14 g_ij)+(∂24 g_jk)(∂13 g_ij)].
The factor 1/4 includes both orders of the two disjoint bivector summands.

No derivative of y enters these cross terms: every derivative of u12 in this expression is in variables 3 or 4, and conversely. This simplification is specific to the fixed line frame. Mixed line transitions carry extra y parity and require their logarithmic derivatives before normalizing the residual.

## Executed checks

The companion script uses exact BigInt rational arithmetic and squarefree jets of total degree at most two. The variables are x1,…,x4; the elementary-symmetric map is differentiated inside the jet algebra. It constructs the actual normalized splitting and transition matrices on carrier charts 0,1,2,5 at x=(2,3,4,5).

The splitting inverse identities are checked in the second-jet algebra. The residual is evaluated on all 64 ordered triples. All 256 ordered quadruples satisfy
R_ikl+g_kl R_ijk−R_ijl−R_jkl g_ij=0.
The script prints a raw residual matrix as an additional reproducibility datum. Its nonzero entries have no implication for nonvanishing in cohomology.

A separate execution also checked 384 first-order values and cross derivatives from the same second-jet implementation, all zero.

## Remaining global operation

The class is represented by C2=g_ik^{-1}R in row-End coordinates. It must be transposed before applying the column End(E)→End(K) inclusion. The local inclusion, the finite cover-refinement comparison, and the Laurent homological transfer must be composed and verified before reading an Ext² coordinate.

The local calculation does not replace this global operation. A proposed single-chart formal-residue shortcut has not been justified: partial formal patches and their lower Čech/internal correction terms still matter.
