# Independent review of the quartic jump classification

## Verdict and scope

**PASS, conditional on the exact earlier inputs identified in the proof.** This is an independent mathematical review, not a proof-assistant verification. The reviewed file is `PROOF.md`, SHA256 `b1bd2697849b4ead14e9b5d8dc7812a3ea5822263c9c44272f038bfb39b12fc0`.

The required inputs are the actual family and multiplication map of [PR519 at cf328c6b0d05551a52911a3a4ba420c68f6fcc6f](https://github.com/Akilleez-QA/read-em-and-weep/blob/cf328c6b0d05551a52911a3a4ba420c68f6fcc6f/research/hm/gorenstein-flat-family/PROOF.md), the bound a(w)<=15 of [PR516 at 89b66cbede7513c4f196fdbda0ee3bb77c53d2e0](https://github.com/Akilleez-QA/read-em-and-weep/blob/89b66cbede7513c4f196fdbda0ee3bb77c53d2e0/research/hm/gorenstein-resolution/PROOF.md), and the established normalizer-equivariance of the original module. This review checks the new deduction from those inputs, rather than claiming a fresh proof of the complete dependency chain.

## Independent checks

1. **Heisenberg multiplicity and bundle splittings.** Degree four has nontrivial central character. The Heisenberg irreducible classification therefore puts both source and target in one five-dimensional isotypic class. Since the group acts trivially on the parameter line, taking its multiplicity bundle commutes with fibers, by the characteristic-zero averaging projector. The source becomes 10O(-3). Averaging a splitting of the target extension preserves its O and O(-1) summands as Heisenberg-equivariant bundles, giving 3O plus 2O(-1) after taking multiplicities. No normalizer-equivariant splitting follows or is required. Consequently a=5(5-rank(phi)), with generic rank between two and five.

2. **Intrinsic divisor.** The generic-rank minor ideal is nonzero and is locally principal on the smooth parameter curve. At a point, Smith normal form gives its order as the sum of the nonzero diagonal-factor valuations. Its support is precisely rank drop, and its multiplicity is at least the fiber rank deficiency. This also proves that a simple divisor point has rank deficiency exactly one, not a larger jump hidden by set-theoretic reasoning.

3. **Mixed-degree bound.** An r-minor using k lower target rows has degree 3r-k. There are only three upper rows, so k>=max(0,r-3). Any nonzero minor bounds the common divisor by its own zero divisor. The resulting upper bounds 6,9,11,13 are valid even though not all components have the same degree. In particular, the rank-four bound is strictly below twelve.

4. **Invariance independent of choices.** The original multiplication map has generic rank 5r and is intrinsically normalizer-equivariant. Its maximal-minor divisor is invariant. Tensoring the reduced map with the five-dimensional irreducible repeats each local Smith exponent five times, so this original divisor equals 5D. Dividing divisor coefficients by five proves invariance of D without any linear action on chosen multiplicity bases.

5. **Faithful projective action and orbits.** The binary two-dimensional irreducible representation has scalar central involution and nontrivial projectivization. Thus its projective action factors through A5 and is faithful by simplicity. The [Horrocks--Mumford appendix](https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf) lists the two dimension-two irreducible characters with central-involution character -2. A finite point stabilizer in PGL2(C) is cyclic, so possible A5 orbit lengths are 60,30,20,12. The six order-five subgroups each fix two points; distinct such subgroups cannot share a fixed point. Their twelve fixed points form a single orbit, since each point has stabilizer exactly of order five. Hence the length-twelve orbit is unique.

6. **Exhaustiveness and sheaf consequences.** An invariant effective divisor of degree at most eleven is empty. At degree at most thirteen it is either empty or the reduced twelve-point orbit. This establishes all claimed constant cases and the sole possible nonconstant pattern, namely generic a=0 and a=5 on that orbit. In that case the reduced-map cokernel is a torsion sheaf of length twelve with one-dimensional exceptional fibers; the original cokernel has length sixty and five-dimensional fibers. Constant-rank cokernels are locally free. These are sheaf claims, not just claims about supports.

## Clarification of the action input

The final proof includes the requested short faithfulness argument and appendix reference for the established projective A5 action. This clarification was checked independently in item 5 above. It makes explicit the input needed for the orbit bound and does not change the classification or add a selected-instance calculation.

## Limits

The proof does not decide the generic rank or whether the twelve-point pattern occurs. It does not show that all listed patterns are realized. No actual HM/source-instance matrix, selected parameter, coefficient search, numerical rank experiment, or large computation was evaluated. The result concerns quartic minimal generators; no conclusion about the original first-order residual, higher-order lifting, or algebraicity is asserted.
