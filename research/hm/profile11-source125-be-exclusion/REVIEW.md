# Independent review of the source125 be exclusion

## Reviewed version

Reviewed on 2026-10-23. This review is bound to the following exact file bytes:

- PROOF.md: SHA256 `c7b19a527cf4da3fd64a81aa714a99449c278997aed007bad1cd206e7f5413ad`
- verify.py: SHA256 `13b8730aca60e969acf3385ec2389729f70e4b70896039fd5b0efbf22a85467d`
- REPRODUCE.md: SHA256 `a45acbfdcd233ef0f837664954bd22bf4a97a97916ac3131d913e2ab00c36705`

The proof and verifier were read independently. The cf and bf proofs cited in the dependency section were also read to check the stated actual-bundle interfaces. The two-P kernel classification is used as the explicitly pinned dependency, not independently re-proved here.

## Finding

No mathematical gap was found in the stated single-original-source exclusion, conditional on its pinned universal and actual-bundle dependencies. In particular, the new argument does not assume that an arbitrary equivariant splitting is horizontal.

The following structural points were checked in detail:

1. The lower-row-zero branch has no internal channel. In the high-only single-P branch, a divisor-reduced degree-six P system has kernel V(-4) with no internal channel. Its possible saturation correction is incompatible with the rank-four quadratic gap and the invariant-divisor bound.

2. The high-P kernel list is complete at rank three. The rank-three, rank-two-plus-line, and three-line forms exhaust equivariant splittings of the required parity. The twist-two cohomology budget and twist-three character give the displayed candidates, and the forbidden O(-6)-to-P(-2) injection removes the last two unwanted cases.

3. The Ext splitting is exhaustive for all three listed high-P kernels. The five summand checks are the invariant parts of A V Sym2 and V W Sym1, the V multiplicities in Sym4 and Sym12, and the ordinary H1(O(1)) vanishing for Wp(-3). All vanish. Thus there is no unsplit positive-kernel case omitted from the internal-image analysis. The surviving internal channels have saturated images, including the graph into the complementary P and T blocks for the high-only first spans. Specifically in KW, W(-7) has no internal channel, while the O(-10) channel has a nonzero T(-5) component inherited from the full-top analysis. That component is the basepoint-free tautological degree-five line, so its graph with any P(-4) component is saturated. Its first-span degree is minus eight plus eighteen minus eight, namely two, excluding KW without any assumption about saturation of the isolated P component. The two remaining first-span characters and ranks/degrees agree with (3) and (4).

4. The crucial high-only projection in Section 4 is injective. On F-plus, a T(-1) summand can project only to the unique T(-1) summand of L; a zero projection would force rank six into the constant rank-three V. Thus that projection is a nonzero scalar and is injective. When the Wp(-1) summand is present, its projection cannot be zero because Hom_G(Wp(-1),V O) vanishes; a nonzero constant map to the Wp multiplicity space is injective. These inequivalent blocks have disjoint images. Consequently the projected F has rank four, excluding the high-only direction from ker b.

5. The constant-V capture is exact. The kernel of the full top projection is the canonical Euler Wp(-3) in ker b. It is saturated in V because the top is saturated in the ambient constant bundle. The larger intersection E with V cannot have rank three, since saturation would put the whole constant V inside E, contradicting H0(E)=0. The two saturated rank-two intersections are therefore equal. The nonzero lower derivative of the Euler block factors through (V/Wp(-3))(-2), so the map V/Wp(-3)=O(6) to the lower O(6) factor is nonzero and hence an isomorphism. The removed line is an actual saturated graph, not a chosen horizontal splitting.

6. The second constant projection is justified by the basepoint-free high Wp system and its saturated internal line. The resulting rank-four degree-zero span is genuinely constant, with coefficient P. Its exact intersection and the vanishing tail components of O(-16) yield the displayed locally free R0 and E-double-prime.

7. The final constants bound does not assume H0(R0)=0. Since R0 embeds in a constant bundle, all splitting degrees are nonpositive; rank nine and degree minus ten imply h0 at most eight. Removing the actual global constant subspace leaves a negative residual of rank at least four and degree minus thirty. Strict-top with only O(-10) available forces degree at most minus forty, giving the claimed contradiction.

## Reproduction

The frozen verifier was run independently with the two local audit inputs. It verified their exact pinned Git blob hashes and exited successfully with:

```text
PASS: 80 fixed Hom checks, high-P kernels, Ext/polar/Euler identities, original source125 be identity.
No source/model evaluation, support search, all-twist envelope, or current frontier count was performed.
```

The run involved only the fixed universal character calculations and the pinned catalog identity. No selected HM/source-instance coefficients, parameters, points, derivative evaluations, matrices, ranks, experiments, scans, or large computation were used in this review.

## Scope

This is a written mathematical audit, not formal certification. It supports only the exact original be tuple stated in PROOF.md; it supplies neither a whole-label exclusion nor a current frontier count. Arithmetic verification does not replace the saturation, constant-connection, exact-intersection, and branch-exhaustion reasoning audited above.
