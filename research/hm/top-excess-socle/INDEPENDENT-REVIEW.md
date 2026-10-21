# Independent mathematical audit

Reviewed PROOF.md SHA256 `8b8427a89131f2004ef95c12ffc550f5d55fe9a71d728d93ebb650b1a565b43e`.

Verdict: the claimed graded P-module isomorphism Tor_4^P(A,B) = (P/P_+)(-7)^{45} is valid, conditional on the four exact published dependencies listed in the proof. This is independent mathematical review, not formal proof-assistant checking. No source-instance evaluation, coefficient or rank search, or large computation was used.

## Universal presentation

The symmetric-power presentation is correct: taking symmetric degree p in the symmetric algebra of the presented module gives the relations obtained by multiplying its defining linear forms in x,y by Sym^(p-1) W. There are no additional relations to assume.

I checked the decorated-fiber argument independently. Temporarily label repeated E-index occurrences. For fixed total exponent, if the buffer t is smaller than its target then the sum of the box coordinates is larger than its target sum, so a surplus box exists. Moving from it into the buffer stays within all bounds until t reaches its target. The reversed procedure applies when t is larger. At equal buffer values, a surplus box and a deficient box can exchange one unit through the buffer. When t<p, surplus-first is allowed; when t=p, deficit-first is allowed because p>=1. Each pair reduces the sum of absolute box discrepancies by two. Consequently the procedure terminates at the target. Forgetting labels preserves each allowed relation, including coincident E indices. Degree zero is immediate. Distinct fibers have distinct nonzero monomial images, so the argument proves an actual module isomorphism, not only a dimension bound or a set-theoretic assertion.

The exclusion of p=0 is essential and correctly stated. For p=0 the symmetric power is P, not B, and there is no buffer. The proof uses only p=8.

## Base change and grading

The exact purely quadratic presentation of H, supplied by PR499 together with the actual relation inclusion of PR490, identifies S tensor_P N with H. Symmetric powers commute with this base change, and tensoring distributes over the even/odd direct sum of S. No flatness is needed in either step.

For the odd summand, O_d=S_(2d+1), with negative original polynomial pieces zero. In particular O_d=0 for d<0. All M_p pieces also start in degree zero. Thus its regrading identifies the dth tensor component precisely with original degree 2d+1, with no negative-degree correction. The canonical identities omega_A=O(-3) and omega_B=M_8(-5) agree piece by piece, as well as with multiplication by P, using PR540's canonical formulas. Canonical determinant coefficient lines are explicitly omitted only for these non-equivariant assertions.

## Concentration, action, and shift

PR494 gives Sym_S^8 H only in original degrees 0,1,2, of dimensions 9,45,55. Its odd piece is therefore exactly its degree-one space T tensor Sym^8 W. Every positive-degree element of P raises original degree by at least two and hence kills this odd piece. Thus the canonical tensor is the residue-field module of dimension 45 in Veronese degree 8, not merely a module with 45 minimal generators.

Under the convention M(s)_d=M_(d+s), shifting this module by 15 places it in degree -7. Graded duality places Tor_4 in degree 7. Its annihilator is exactly P_+: positive-degree elements kill it, while any polynomial with nonzero constant acts by that nonzero scalar on a nonzero vector space. The length is exactly 45.

The secondary even-part consequence is also valid: A tensor_P omega_B has degrees 5 and 6 of dimensions 9 and 55. Its degree-one action is ordinary binary multiplication from (E tensor Sym^2 W) tensor Sym^8 W onto E tensor Sym^10 W, and P_+ squared annihilates it. This does not require an inference from dimensions alone.

The result determines the highest Tor over P and does not determine the separate S-linear parameter k, the other intermediate Tor modules, the original fixed-pair residual, higher-order lifting, or algebraicity.
