# Independent mathematical review: reversal-fixed marked classes

## Reviewed artifact and verdict

The exact proof reviewed is `reversal-fixed-classes-proof.md`, SHA-256
`148dd88be35ab5bce6b95005ebef8a9425dbe92bfa8a457dc05f9ce635dfb34f`
(21,951 bytes). The review applies to that content, not to unreviewed later revisions.

**Verdict:** no blocking mathematical finding within the stated scope and retained literal-lifting hypotheses. The finite and formal parity images are exactly the fixed object-class loci of reversed opposite, and the first failed test has the stated origin-independent anti-fixed defect.

This was independent symbolic mathematical review, including direct derivation of the noncommutative transport identities. Only document reading and an integrity checksum were performed locally. No source instance, HM map, detector, jet, obstruction coefficient, or mathematical checker was executed. No public repository write was made in this review.

## Exact sources checked

- PR425 at `df433cdd359fa9c7750bf9c8b9765229eac534f6`, proof blob `938c9d9a809d6d6f0712b8335888b56cff898636`.
- PR436 at `502c978a17cd7037d740d4d08d373c1cb8bd5829`, proof blob `33797db390d2c3863f3ec5c74a8f63c7d595fc2e`.
- PR438 at `971c16a67b1e7d12fce0a8e2d2165ca4839911de`, proof blob `a583f09897ea9511df09c3080f57728add217332`.
- The public invariant literal small-extension argument in PR1, comment `6259748725`; the relevant PR425/436/438 announcements and current coordination review in comment `6290132737`; and the author’s public scoped reviews on those three PRs.

The three PR heads were independently re-read and matched the supplied pins. Their results are used with their retained hypotheses, not as source-instance calculations. The general abelian version retains the literal lifting premise; the public source argument's explicit application is the stipulated elliptic fourfold.

## 1. Exact involution and noncommutative orientation

For a source product `*` and reversed-opposite product `diamond`, the relation
`tau(a*b) = tau(b) diamond tau(a)` is exact. Consequently
`d_x(a)=tau(a^{-1})` is a group homomorphism between the corresponding unit groups, not an antihomomorphism. It obeys both naturality under algebra maps and
`tau Ad_*(a) tau = Ad_diamond(d_x(a))`.

This verifies the triple-unit inverse, the inner descent equation, and the pentagon with its original ordered factors and unchanged Cech indices. Independently, inverting the original pentagon gives exactly the opposite-product pentagon; applying parameter reversal completes the check.

The convention that the chart map `E` runs algebraically from the transported chart to the source chart is respected. The transformed edge unit is `d_x(B)`, and applying `d_x` to the ordered four-factor expression for the transported triple unit proves the transport identity without commuting any factors. Gauge composition is `(E L, E(K) B)`, and its image is the composition of the images.

The chart 2-unit image must be `d_x(C)`. Substitution in the actual endpoint-preserving formula shows that it keeps the same 2-morphism orientation. Vertical composition is preserved because `d_x` is a group homomorphism; horizontal composition has chart unit `C E(D)` and is also preserved by naturality. Applying the construction twice returns every object, gauge and chart 2-unit literally.

The fixed initial presentation remains literally fixed. Strict fixed objects, gauges, and chart 2-units are respectively parity presentations, even/unitary gauges, and unitary chart 2-units. The manuscript correctly does not identify the enlarged parity convention with extra ordinary 2-units with the strict fixed 2-data.

## 2. Top action and fixed directions

Relative to a literal parity upper origin, the exact action on top differences is
`(u,v,a) -> ((-1)^n u^op, (-1)^n v, (-1)^(n+1) a)`.
The inverse of a triple unit contributes the scalar minus sign. Varying the top product contributes nothing further to that inverse, because its only possible classical arguments are `(1,1)` and the binary cochain is normalized.

The induced signs on the three coherent-cohomology summands are therefore
`((-1)^(n+1), (-1)^n, (-1)^(n+1))` on bivectors, `H^1(T)`, and `H^2(O)`. The explicit decomposition into global bivector, derivation-valued Cech cocycle, and scalar Cech cocycle justifies the splitting without a hidden formality inference.

The fixed subspace is exactly the PR425 parity-image subspace: `H^1(T)` at even degrees and the bivector plus `H^2(O)` summands at odd degrees. Equality of dimensions is not substituted for equality of the realized image.

## 3. Genuine finite fibers and lower gauge ambiguity

The crucial map from literal unrestricted top classes over a parity lower representative to the true unrestricted class fiber is proved bijective, not presumed so. Surjectivity uses freely lifted coordinate data and lets transport determine the endpoint. Injectivity uses PR438's full lower-automorphism 2-triviality and lifts its ordinary chart unit to replace the upper gauge by one with literal identity reduction.

Because the selected lower representative is literally fixed, this bijection is involution-equivariant. The lower transport need not itself be parity. Formula (4.1) correctly conjugates a fixed-class witness after arbitrary transport; its lower automorphism is then removed by an endpoint-preserving chart-unit correction.

The stated canonical H-torsor structure also passes the audit. Common unrestricted lifted coordinate data work for both top products, since units with classical term 1 are invertible in either. At top order the classical chart and edge parts are id and 1, so transport is identity-linear on `(u,v,a)`. Changing a lift adds only a top gauge. Changing the lower identifying gauge adds a lower relative automorphism, whose full 2-trivialization removes its action on classes. Thus no unnoticed affine translation or residual lower-automorphism quotient alters the claimed fiber.

## 4. Induction, formal compatibility, and the defect

The finite fixed-class induction is valid: a fixed upper class has a parity-normalizable lower class; its genuine fiber is identified equivariantly with the literal top torsor; a parity upper origin makes the involution linear; and a fixed top difference lies exactly in the already realized parity subspace.

The formal step correctly invokes PR438's unrestricted inverse-limit injectivity and finite-detection theorem. It never assumes independently chosen finite gauges are compatible, nor promotes the one-step image theorem directly to a formal assertion. The imported results supply the actual alignment and compatibility arguments.

The new defect `q_n(u)=(u-Iu)/2` is well-defined in the anti-fixed summand when the lower class is parity-normalizable. Changing parity origin translates by a fixed vector and therefore does not change the defect. The canonical, identity-linear H-action just checked makes the defect independent of lower representative and identifying gauge as well. Its zero locus is precisely the parity image in that fiber. The claimed first failure exists by finite detection; no later defect is silently defined after the lower normalizability condition has failed.

## Scope retained

The conclusion concerns invariant marked ambient object classes with freely adjustable higher products. It does not classify coherent involutive actions or homotopy fixed-point data, full fixed 2-groupoids, unmarked or non-invariant quotients, moduli, periods, prescribed-product extensions, modules, convergence, algebraization, or algebraic cycles. The defect is a parity-normalization obstruction, not an obstruction to unrestricted continuation. Source-dependent obstructions and the six pure conditions remain unevaluated.
