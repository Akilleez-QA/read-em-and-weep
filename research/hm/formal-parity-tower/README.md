# Marked formal reversal-compatible continuation classes

This advances the one-step relative result of PR425 to the full coefficientwise formal tower, conditional on PR416's retained invariant literal lifting input.

Fix a literal reversal-compatible presentation modulo h^M, M >= 3, on the stated inversion-invariant abelian cover. Allow higher local products, maps, and units to vary. Use invariant even chart gauges and reversal-unitary edge units, identity modulo h^M.

The complete proof establishes:

- Finite restriction fibers are the actual torsors from PR425: H^1(T) at even degree and H^0(Lambda^2 T) plus H^2(O) at odd degree.
- Lower relative automorphisms are 2-trivial, so no extra lower-automorphism quotient is hidden in those fibers.
- Formal classes equal the inverse limit of finite class sets. Compatible representatives and compatible equivalences are constructed explicitly.
- Choosing an origin in every finite fiber yields a noncanonical product parameterization as a filtered set. On an abelian fourfold the successive factor dimensions are 16 at even degrees and 12 at odd degrees.
- Formal pi_1 is zero. Unitary chart 2-units give scalar pi_2 with only odd logarithmic coefficients; ordinary chart 2-units give all positive coefficients starting at M. Object classes are unchanged.

See [PROOF.md](PROOF.md) for all hypotheses, derivations, and exact public source pins. The key new ingredients are liftability of admissible gauge and chart-unit data, induction on full lower automorphisms, and inverse-limit strictification. This is not an inference from one-step torsors alone.

## Nonduplication and scope

PR409 (`59fc9cdc40cf9a21fbb38549767829ff7471294f`) proves parity-separated lifting. PR416 (`c71356722bc7bd1a426d26ea0ca6d050f4c3ed81`) selects a formal continuation. PR425 (`df433cdd359fa9c7750bf9c8b9765229eac534f6`) classifies one-step relative lifts and explicitly stops short of a formal classification. The present result supplies that next marked, parity-compatible classification, with the coherence proof that was not provided by those statements.

The repository coordination discussion and searches for reversal, formal continuations, tower, and lim1 were checked on 20 October 2026. No duplicate of this marked parity-tower result was found. PR232's formal tower statement concerns effective equivariant descent of locally free modules over supplied algebra towers, not classification of ambient continuation choices. This is a bounded repository comparison, not an exhaustive literature-novelty claim.

No canonical affine product, moduli scheme, unrestricted normal-form theorem, fixed-product all-orders theorem, module lift, period map, actual-source evaluation, convergence, algebraization, or algebraic-cycle construction is claimed. The fixed fifth-product obstruction and the pure diagonal six-condition problem remain unchanged.

