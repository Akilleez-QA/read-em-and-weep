# Current independent mathematical review

Independent mathematical review, 20 October 2026. This is a check of the written derivation and the stated immediate prerequisites, not a formal verification certificate. Earlier audits are treated as historical evidence, not as a substitute for this review.

Reviewed PROOF.md SHA256: 17b5489f297f3919200072d12c35bc2c909331fb880e8dad893758389d14c905

Reviewed Git blob SHA1: 1e88c38641c9b8e0e6b7209c3125bba31abafa28

## Verdict and scope

PASS. The six-point classification is unconditional in the specified complex Heisenberg representation. The incidence refinements retain the K,T and derivative-duality premises of PR146. There is no proof here of linear independence of the six products or of their avoidance by P(T) or its Veronese conic.

## Checks

- The weight matrices have fifth power one and vanishing traces of powers 1 through 4, so their eigenvalues are the five distinct fifth roots. The infinitesimal action on a degree-five eigenbasis monomial is the sum of its five eigenvalues with multiplicity, not their product. The cyclotomic polynomial forces the only zero-weight exponent vector to be (1,1,1,1,1).
- Heisenberg conjugation permutes these eigenlines by a translation of F5, hence evenly. The determinant-one condition makes their product an invariant vector. The four nonzero weights on one F5-line span the full trace-zero diagonal Cartan and kill that product.
- The imported proper-Lie-support argument is valid: two independent supported weights generate all 24 nonzero weights under nonorthogonal addition. Therefore a nonzero stabilizer forces exactly one of the six products and its entire four-dimensional Cartan. Distinct Cartans force distinct products.
- The infinitesimal orbit image has only nontrivial Heisenberg characters, while q and T are invariant. Thus vector and projective Lie stabilizers coincide, and restriction of the derivative image to K loses no rank. The exceptional/nonexceptional ranks are exactly 20/24.
- With dim K=123, the projective incidence fibers have dimensions 102/98. A finite exceptional parameter set and two-dimensional P(T) give codimension at least 20, improved to 22 if no exception lies in P(T). The conic version improves to 23 when that conic avoids the exceptions. Any exceptional fiber is itself a 102-dimensional linear subspace of the image, giving exact codimension 20 whenever the relevant parameter space meets an exception.

The full vector and projective stabilizer groups are not identified with one another: determinant-one monomial matrices stabilize the projective product, while the vector stabilizer retains the even-permutation subgroup. Their common identity component is the diagonal determinant-one torus.
