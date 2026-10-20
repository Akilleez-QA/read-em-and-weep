# Scope and later implications

The universal lemmas below remain valid. Intermediate unresolved-case descriptions are historical: the universal K7 and K8 bounds are supplied by diagonal-hartogs-fiber-bound/PROOF.md and UNSQUARED_PENCIL.md. For any actual canonical operation satisfying a later global rank-at-least-five theorem, residual-rank-one through four loci are empty; these are not simultaneous live canonical alternatives. Conditional global dimension implications retain their separately stated hypotheses.

# Residual rank three and the next rank-two reduction

## 1. Global consequence under the established middle-support hypothesis

The universal pointwise K7 theorem applies to every seven-dimensional kernel with square-avoiding correction, not only generic nets. In the established trilinear setup, residual rank three means dim K_u=7. The exact outer reconstruction identifies its separately projectivized independent-zero fiber with the compatible ordered locus, with no extra lift parameter. Thus every such fiber has dimension at most two.

Under the previously established hypothesis (H) that the projective residual rank-drop middle locus has dimension at most two, every component generically of residual rank three has affine dimension at most 2+2+3=7. The last three dimensions are the three independent nonzero input scales. Together with the earlier rank-four and rank-five bounds, and the rank-at-least-six dimension-six theorem, any component of affine dimension at least eight must have generic residual rank at most two. No dimension-seven exclusion is asserted.

See ../full-support-rank-five-dimension-bound/PROOF.md for reconstruction and precise provenance of (H); ../rank-four-compatible-fiber-bound/PROOF.md for rank four.

## 2. Eight-dimensional kernels with coprime annihilator quadrics

Let K have dimension eight and W=K-perp be its pencil of two independent quadrics. If they have no common factor, their common square locus has dimension at most one. The diagonal–Hartogs extension lemma applies verbatim and bounds compatible fibers by two. Under (H) the corresponding generic residual-rank-two components also have affine dimension at most seven.

## 3. A common-factor pencil containing its factor square

If the pencil has a common factor, write W=zL for a two-dimensional space of linear forms L. A common quadratic factor would make the pencil dependent. Suppose z∈L; choose W=span(z²,zx), with z,x independent. Put A=ker z and R=ker z∩ker x, of vector dimensions three and two. The product equations give exactly

    (P(A)×P(A)) ∪ (P(R)×P(E)) ∪ (P(E)×P(R)).

On the first component all products lie in Sym²A⊂K, so the direct hyperplane lemma of PROOF.md excludes a compatible threefold. On the other components a factor image lies in the line P(R). The universal finite-compatible-partner-plane lemma in ../rank-three-compatible-fiber-structure/PROOF.md bounds any such compatible locus by two: outside finitely many first factors its fiber has dimension at most one; at those finitely many points it has dimension at most two. The reversed component is symmetric.

Consequently this common-factor pencil also has compatible fiber dimension at most two.

## Remaining rank-two case

A hypothetical compatible threefold for an eight-dimensional kernel must therefore have annihilator pencil zL with z∉L. This is a necessary normal form, not an existence assertion. The case is not resolved here. Neither are kernels of dimension nine or ten, or the global dimension-seven exclusion.
