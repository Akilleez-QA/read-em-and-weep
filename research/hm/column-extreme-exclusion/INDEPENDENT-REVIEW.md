# Independent mathematical review

Reviewed proof SHA256: db502a20ae94147d83b21e6225c7ae39b42b89da6aa32a33bccb0f2e7cf53947.

The proposed exclusion is valid conditional on the preceding column-kernel-vanishing proof and the pinned actual normalizer representation identities. This is an independent mathematical review of the new exclusion, not a new certification of all preceding dependencies or formal proof-assistant verification. The preceding kernel lemma must receive its exact publication pin before this slice is published.

## Checks

1. If u=15 occurs, the preceding classification makes it constant. The map then has constant rank six. Its kernel K has rank three, and its image J is a subbundle of 10O(2), rather than just a torsion-free image with a possibly nontrivial saturation quotient. The exact bundle sequence gives deg(J)=-deg(K). The preceding H0(K(2)) vanishing makes every splitting degree of K at most minus three, while deg(J)<=12. These conditions give exactly the seven listed nondecreasing triples: 333, 334, 335, 336, 344, 345, 444.

2. The equivariant splitting argument is sound. The ordinary splitting-degree filtration on P1 is intrinsic, hence preserved by the finite group action. Its sequences split as ordinary bundles by the splitting theorem and the description of this filtration. Averaging a splitting over the finite group preserves its right-inverse property and makes it equivariant. Each resulting equal-degree block, after twisting by the standard O(d), is equivariantly trivial with coefficient representation its global sections. Thus no unsupported equivariant refinement of an arbitrary ordinary splitting is assumed.

3. A rank-one coefficient representation is trivial because SL(2,F5) is perfect. A degree-three or degree-four line summand would map by an invariant of (U+R6) tensor Sym^d(W'). The irreducibility and dimensions of Sym3(W') and Sym4(W') make this invariant space zero. Therefore such a line summand cannot occur in the injected kernel. This removes 334, 344, 345. It also implies that a three-dimensional coefficient representation in 333 or 444 cannot be reducible: every decomposition of a three-dimensional representation into smaller irreducibles has a trivial line. The remaining three-dimensional irreducibles are even. Likewise the degree-three rank-two coefficient block in 335 and 336 must be one of the odd two-dimensional irreducibles, not two trivial lines.

4. The central involution fixes P(W*) pointwise but acts by (-1)^d on the standard O(-d). Thus the parity of the total block is the parity of its coefficient representation multiplied by (-1)^d. A fiberwise equivariant map preserves this parity. Since the constant source is U even plus R6 odd, the parity conclusions in all four remaining cases are correct. This explicitly accounts for the base action and does not confuse coefficient parity with total bundle parity.

5. In case 333, K lies in the R6 summand. Consequently J splits as UO plus (R6O/K). Since J is locally free, the latter quotient is locally free; it has rank three and degree nine. Its injection into 10O(2) is impossible. Every splitting line of a vector bundle injecting into 10O(2) must have degree at most two, so a rank-three subbundle has degree at most six.

6. In case 444, K lies in UO, with equal rank three. Local freeness of the quotient forces the rank-zero quotient UO/K to vanish, hence gives an isomorphism contrary to their different degrees. The same argument applies in 336: both blocks have even total parity and land in UO, while deg(K)=-12.

7. In case 335, the rank-two degree-three block is even and lies in UO, while the degree-five line is odd and lies in R6O. The quotient J is the direct sum of their quotients. Each quotient is locally free because J is locally free. The U quotient is a line of degree six, so its injection into 10O(2) would require a nonzero map O(6) to O(2), which does not exist.

All possibilities are excluded. Thus constant u=15 is impossible. Combining with the preceding classification yields only constant values 0, 5, 10 or generic zero with value five on the twelve-point orbit. This does not assert that any particular surviving case occurs. The reasoning uses no selected actual HM/source-instance evaluation, numerical multiplication-rank experiment, coefficient search or large computation, and it does not resolve the original fixed-pair residual, higher-order lifting or algebraicity questions.

Publication receipt: the sole subsequent proof edit replaced the dependency placeholder with PR523 at d02ae6cb6d324bad2b858c6969ed4ce8d43b5e42. Final proof SHA256 79a268b5009f172f303c41fe47dacdd1cb59fa8d1df12068b527e23ffc3a7d73. Root verified this link-only edit; mathematical content is unchanged from the independently reviewed version.
