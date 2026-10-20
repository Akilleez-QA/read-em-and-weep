# Independent audit: nonplanar factor images reduce to a common quadric

Status: PASS, including the strengthened common-quadric conclusion. The initial proof draft stated the weaker common quadric-or-cubic result; the gradient-syzygy argument below removes the cubic case.

## Hypotheses checked

Work over C, with E of dimension four and K of dimension five and full support. The ordered-factor surface is integral, generically rank two, and both factor images are nonplanar surfaces. No correction, compatibility, or square-avoidance assumption is used. The previously proved nonlinear-curve factor exclusion and one-planar factor exclusion are legitimate dependencies with exactly the required hypotheses.

## Kernel-ruling reduction

A nonlinear curve along which the kernel has vector dimension at least two supplies an integral ruled ordered-factor surface by a rational rank-two subbundle. Its product image has dimension two because factorization is finite. Its closure is indeed a component over its product image: the whole ordered-factor inverse image is finite over that image and therefore has dimension two. Thus the nonlinear-curve exclusion applies even though the chosen ruled family need not be a component of the entire incidence over P(K).

This proves generic kernel dimension one on each factor surface, hence birational factor projections, and excludes ambient matrix rank at most two.

## Ambient rank-three cases

If the rational kernel map has surface image, symmetry puts its one-dimensional generic inverse fibers in projective kernels, contradicting the preceding nonlinear-curve observation.

If its image is a line P(L), generic kernel dimension is three. Two distinct parameters give three-dimensional product spaces whose intersection must be their cross product, since their sum lies in K of dimension five. Varying parameters yields Sym²L contained in K contained in LE. The two-dimensional quotient pencil in L tensor (E/L) has rank-one members with varying first factors, hence has a fixed second factor. K is then supported in a three-dimensional subspace, a contradiction.

For constant image e, K=eE+Cq. In the quotient E/Ce, all nonzero products are multiples of the fixed nonzero q-bar. Its factors are finite in number, so both original factors range only over fixed projective lines through e, unless one factor is e. This cannot contain the hypothesized two-surface-image component.

For dominant image, symmetry makes the kernel map a birational involution. The one-planar theorem forces general planes to map to planes. The induced rational map on dual P³ is generically injective, hence dominant. The strict inverse transform of a general plane is therefore a plane. A primitive degree-d polynomial presentation has no fixed divisor; a general target plane contains the images of none of the finitely many exceptional divisors. Its pullback is thus precisely the strict-transform plane with multiplicity one, so d=1. An invertible linear map has symmetric product span at least six by its eigenvalue sums, contrary to dimension K=5.

Consequently ambient rank is four.

## Stronger maximal-minor argument

The signed maximal minors form a nonzero homogeneous degree-four left-kernel vector. Divide by their homogeneous gcd g. Its primitive part cannot have degree zero, because this would be a constant dependence of the five independent symmetric forms. It cannot have degree one either:

For independent quadratic polynomials Q_i, suppose homogeneous linear l_i satisfy sum l_i grad(Q_i)=0. Dot with the coordinate vector to obtain 2 sum l_i Q_i=0. Differentiate this zero cubic and subtract the assumed syzygy. This gives sum Q_i grad(l_i)=0. Independence of the Q_i makes each constant grad(l_i) zero, hence every l_i zero. The normalization between polar rows and gradients is a common nonzero factor and changes nothing.

The primitive minor vector therefore has degree at least two, and degree(g) is at most two. The irreducible equation of either nonplanar factor surface divides every maximal minor and hence g. Both equations have degree at least two. They must consequently coincide up to scalar and have degree exactly two.

## Scope

This is a reduction to a common integral quadric, not an exclusion or classification of correspondences on that quadric. It does not show that the birational correspondence is induced by an ambient projective linear map.
