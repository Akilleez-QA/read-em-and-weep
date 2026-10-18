## Mathematical expression checked

For block index l=0,1,2,3 set

- ranks n=(5,15,10,2), weights k=(-1,1,3,5), signs e=(-1,1,-1,1);
- Ai=B_i,a, Bi=B_i,b, Aj=B_j,a, Bj=B_j,b;
- theta_a=qa/2 and theta_b=qb/2.

Then the expression is

s = sum_l e_l/4 [tr(Ai Bj)-tr(Bi Aj)]
  + sum_l e_l k_l/8 [qa tr(Bi)+qa tr(Bj)-qb tr(Ai)-qb tr(Aj)]
  - 15 qa qb/8.

The source `first-order-source.md` at `08b73637...`, §§2 and 4, gives
T_ij = -str(B_i wedge B_j + k theta_ij wedge (B_i+B_j))
and s = -(1/4) iOrd_pi T - (15/8) r.
Thus the plus 1/4 in the implementation is the product of these two minus signs, not a change of transgression convention. Both endpoint traces are necessary. This uses the pinned source's ordinary coefficient contraction and unsymmetrized endpoint formula, not a cyclic trace assertion on Cech cochains. In particular the rank-weight check is
sum_l e_l n_l k_l^2 = -5+15-90+50 = -30.
The -15/8 edge correction is the source's conversion to the ordered gerbe representative; it is not the 15/4 triangle gerbe coefficient.

The pinned JavaScript excerpt at `10810ee.../research/hm/null-operator-compiler/hm-pinned-source-formulas.js`, `globalBuild2.first`, states precisely this same expression, with `Ai.k` and `Ai.sign` populated by the displayed four-block list. Its SHA-256 matches raw-engine's declared source pin `c4f65ff831092d0e56b3e33a0357f44182169fda45943ea780c8c551b4023f94`. The BI denotation JSON supplies an independently readable identical expression; equality is established by the expanded formula, not inferred solely from hashes.
