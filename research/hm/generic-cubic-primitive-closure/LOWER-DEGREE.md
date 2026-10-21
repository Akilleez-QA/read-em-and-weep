# Lower-degree single-multiplier coverage

Work over C, with B=End_0(F) and the same 25-line degeneracy curve C as in PR541. There is a nonempty Zariski-open set of quadratics q for which

q:H^1 B(3) -> H^1 B(5)

is surjective. Consequently Q5(q,v)=0 for every cubic v, including zero. Separately, a general linear form gives H^1 B(4) -> H^1 B(5) surjective. These are actual adjoint-module maps, not just primary maps.

## Residual calculation

Write P_j for the actual primary image in H^1 B(j) and N_j for its quotient. PR532's restriction-ambiguity argument identifies

N_j^* = D^* tensor (H^0 O_C(5-j) / res S_(5-j)), 1<=j<=6.

Thus for a degree-d multiplier f, the transpose of N_(5-d) -> N_5 sends a tuple of constants modulo diagonal constants to its componentwise product with f, modulo restrictions of S_d.

Let U_l be the image of H^0 O_l(d)^* in S_d^*. Its dimension is d+1. Let R_d be the dimension of the span of all U_l. The generic-hyperplane theorem and the primitive optimal-partition lemma proved in PR541 give the generic residual defect

R_d - 1 - min{R_d-1, 25d}.

Indeed the unique coarsest optimal partition is invariant under the primitive normalizer action on the lines, so it is either the singleton partition or the one-block partition. This argument does not assume that S_d restricts injectively to the entire curve. For d=1,2, R_d-1 <=4,14 respectively, whereas 25d=25,50. The residual defect is therefore zero on a nonempty open set in each parameter space.

## Primary coverage and the full maps

Use M_j=H^1 F(j). Primary sources for d=1,2 are U tensor M_2 and U tensor M_1; the primary target is U tensor M_3. Naturality suffices here: surjectivity before passing to the actual primary image implies surjectivity on that image.

For quadratics, PR449 identifies S_2=A^* tensor sl(W), M_1=A tensor W and M_3=W, with multiplication contraction followed by the trace-zero endomorphism, up to a nonzero scalar. Here dim A=5 and dim W=2. An invertible trace-zero endomorphism, tensored with any nonzero functional on A, gives a surjective abstract multiplication map. Thus the primary-good locus is nonempty open. This is an existence argument in representation space, not evaluation of a selected coefficient.

For linear forms, PR450 proves S_1 tensor M_3^* -> M_2^* is an isomorphism. Restricting to ell tensor M_3^* is injective for EVERY nonzero ell, proving ell:M_2 -> M_3 surjective.

Intersect the nonempty primary-good and residual-good opens in the irreducible projective parameter space. In the exact primary/residual rows, lift a desired target residual class using residual surjectivity, then subtract its lift and use primary surjectivity. This proves full adjoint surjectivity.

## Consequences and limits

The quadratic result kills the ordinary two-generator degree-five quotient for every cubic, because its quadratic image already fills the target. It does NOT assert the analogous squared-quadratic quotient vanishes for arbitrary cubic. PR541 supplies that stronger uniform conclusion on a different, cubic-good open.

The linear result here is generic, not a classification of all special hyperplanes. Hyperplanes containing a component line certainly fail the residual map: a constant tuple supported on that component lies in the transpose kernel and is nonzero modulo diagonal constants. Exhaustion of the failure set requires an additional geometric argument and is not asserted here.

This proves no membership statement for the original fixed quadratic or cubic. Q4, actual source membership, lifting and algebraicity remain separate. No selected-instance matrix, coefficient, rank or source evaluation is performed.

## Pinned dependencies

- PR541, 72f9575febc9eb232ca6f5e8436aecc9e5cbb533: generic-hyperplane formula, primitive partition closure, actual normalizer action.
- PR532, 5f08a072fa8d3bdf12007a6aab2f374c85c5e503: actual residual duality including restriction kernels.
- PR449, e4b6acdd27d8da8be4052c117ea2dca0f48f46ff: primary quadratic multiplication.
- PR450, 54d1eafe617e042edc452cb66edb8e4f7c78d2bf: primary linear contraction isomorphism.

All PRs are in https://github.com/Akilleez-QA/read-em-and-weep . The new content is single-multiplier coverage of H^1 B(5), with its uniform-in-the-other-generator consequence; previously established primary coverage alone does not imply this.
