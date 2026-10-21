# Independent mathematical review

Reviewed exact PROOF.md SHA256 d80793962f4dc6257158da932c309485c6f89e2b8d4d7feb99214660ae97adb0, conditional on its pinned PR523, PR525 and PR526 inputs.

## Constant rank five

Checked kernel, image and cokernel degrees separately. The odd target has degree twelve. Writing K=O(-d), the image has degree d and its line cokernel has degree 12-d. The coefficient exponent in the quotient is therefore 10-d, after subtracting the target twist two. The lower bound d>=3, upper bound d<=10, and odd parity are valid. The source excludes d=3, while the quotient excludes d=5 and d=9 using the stated distinct irreducibles.

For d=7, the quotient on Qspin is uniquely the cubic evaluation, up to a nonzero scalar. Its kernel is U' O(1) after the twist by O(2). The W0 target summand is killed by the quotient and hence splits directly into the image. Since Hom_G(R6,U' tensor W')=0, the actual beta cannot surject this image. This verifies the rank-five exclusion without using numerical matrix ranks or claiming multiplicity-one maps nonzero.

## Constant rank four

Verified the full list (3,3),(3,4),(3,5),(4,4). Averaging splittings of the G-stable degree filtration is legitimate in characteristic zero, and equal-degree blocks have genuine coefficient representations after the standard line twist. A degree-three line would require R6 in Sym3(W'), which is absent. In the equal-degree-three case the coefficient representation must be even; a two-dimensional even representation is a sum of trivial representations because the nontrivial two-dimensional irreducibles are odd. This also gives forbidden lines.

The surviving ordinary kernel 2O(-4) makes the image rank four and degree eight. Each of its splitting degrees is at most two because it embeds in 6O(2), so the image is 4O(2). Twisting its inclusion down by two gives an actual invariant four-dimensional subspace of W0+Qspin, necessarily Qspin. Thus gamma vanishes. The converse uses the pinned uniform bound u<=10 correctly: gamma=0 gives rank at most four, while that bound gives rank at least four on every fiber.

## Final dichotomy

A fiberwise invertible beta would have a nowhere-vanishing O(12) determinant, so constant zero is impossible. The previous exhaustive pattern classification, the new rank-five exclusion and the rank-four characterization prove the stated dichotomy. The gamma coefficient space is one-dimensional, but its actual scalar is not proved nonzero. The proof explicitly preserves this unresolved dependency and does not conflate it with the different quartic invariant.

Approved as an independently reviewed structural proof conditional on the pinned inputs. Not formally checked by a proof assistant. No selected HM/source-instance evaluation, numerical multiplication-rank computation, coefficient search or large computation was performed. Original fixed-pair residual, higher-order lifting and algebraicity remain open.
