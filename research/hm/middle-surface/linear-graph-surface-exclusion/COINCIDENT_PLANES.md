# Coincident planar images and integration

Retain the global residual setting: E has dimension four, K has dimension five and full support, and v:K to E is densely compatible with an integral rank-two surface S and avoids every compatible square. Suppose both ordered factor images lie in the same plane P(U), with dim U=3.

Let K' be the span of S. It is contained in K intersect Sym²U, and has dimension at least three. Dimension five would give K'=K supported on U, contradicting full support. If its dimension is four, the abstract square-avoiding ternary-web theorem in /research/hm/normalizer-rank-five/rank-six-cubic-web/REDUCIBLE.md applies to v restricted to K', with target E unchanged, and excludes a compatible surface. No extension of v is made.

If its dimension is three, S is dense in P(K'), so K' is a ternary plane entirely of rank at most two. The bounded-rank plane classification makes it either Sym²Z for a two-plane Z, or hU. In the first case dense compatibility gives v(K') contained in Z. The binary cubic z wedge v(z²) has a projective zero, contradicting square avoidance. In the second case, taking the two rank-two paths h(h+t a) and h(h+t b), with h,a,b independent, gives v(h²) in span(h,a) intersect span(h,b)=Ch, again a contradiction.

Thus coincident planar factor images are excluded in the full-support compatible setting. Combined with PROOF.md, this excludes both distinct and coincident planar images. Combining further with ../nonlinear-curve-factor-exclusion/PROOF.md and ../quartic-middle-finiteness/PROOF.md, any remaining positive-dimensional middle family of full-support rank-five compatible surface fibers must have both factor projections of dimension two and at least one nonplanar surface in P(E).

This conclusion does not exclude one planar and one nonplanar image, two nonplanar images, ternary-support kernels, or moving middle components with only curve fibers.
