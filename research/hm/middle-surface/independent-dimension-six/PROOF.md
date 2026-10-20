# No low-rank middle surfaces; independent-zero dimension at most six

## Hypotheses

Work over C with the full source, normalizer, bundle and repeated-injectivity hypotheses in /research/hm/rank-four/quintic-surface-classification/RANK_AT_MOST_THREE_COROLLARY.md. In particular dim V=5, dim J=20, the fixed operation is outer symmetric and cyclic zero, all repeated maps are injective, the residual map Q has generic rank ten, its rank-drop support has dimension at most two (H), and the rank-six quotient has total codimension-two defect degree at most70. Retain the standard full Heisenberg normalizer action and the previously proved invariant-curve-cycle exclusions. These hypotheses are not deduced from the three tensor identities alone.

Put Z_s={rank Q<=s}, as reduced supports when discussing dimensions.

## 1. Rank at most five has no surface component

The independently audited /research/hm/middle-surface/decic-middle-surface-constraints/PROOF.md proves: if Z_5 has a surface component, its reduced surface union is a single integral invariant degree-ten surface, with integral general hyperplane section of arithmetic genus in {6,11,16}. This reduction includes arbitrary singular and nonnormal surfaces.

Each genus is excluded by a separately proved and independently audited result:

- Genus6: /research/hm/middle-surface/decic-genus-six-exclusion/PROOF.md, audit AUDIT.md. Resolution and adjunction, ruledness, and group-action obstructions exclude every possible minimal model.
- Genus16: /research/hm/middle-surface/decic-genus-sixteen-exclusion/PROOF.md, audit INDEPENDENT_AUDIT.md. Hilbert-function equality forces a unique quadric; linear-normal lifting and its nontrivial Heisenberg central character contradict invariance.
- Genus11: /research/hm/middle-surface/decic-hyperplane-deficiency/PROOF.md, audit /research/hm/middle-surface/decic-deficiency-audit/AUDIT.md. The only possible curve deficiency has dimension at most one; the restriction sequence identifies its dimension with H^2(I_Y(1)), whose nontrivial central character forces divisibility by five. Thus the deficiency vanishes and Y is ACM. But /research/hm/middle-surface/acm-decic-exclusion/PROOF.md and /research/hm/middle-surface/acm-decic-audit/AUDIT.md exclude ACM invariant decics via their four linear syzygies and a one-dimensional invariant tensor space.

There is consequently no surface component of Z_5. Since Z_5 is closed inside the rank-drop locus of dimension at most two by H, we conclude

    dim Z_5 <= 1.                                            (1)

This deduction uses all three exclusions, not the genus-eleven argument alone. It does not exclude curves or isolated points of Z_5.

## 2. Rank at most two is finite

Apply Section7 of /research/hm/middle-surface/rank-one-middle-curve-exclusion/PROOF.md using (1). The genuinely linear matrix b:O(-1)^15 -> O^20 has rank4+rank Q. Its degree-ten minors cut Z_5. Three general linear combinations form a complete-intersection curve of degree1000. At a generic point of a Z_2 curve these minors lie in the fourth power of the maximal ideal, because rank b<=6. The local length is at least64 by the regular-local parameter-ideal multiplicity argument.

Thus the reduced union of all curve components of Z_2 has degree at most floor(1000/64)=15. This is an actual normalizer-invariant effective curve cycle, excluded by /research/hm/rank-four/normalizer-small-curve-exclusion/PROOF.md. Therefore

    dim Z_2 <= 0.                                            (2)

The empty case is allowed. Finite support does not mean reduced scheme or empty scheme. The proof and multiplicity argument have the independent audit in rank-one-middle-curve-exclusion/INDEPENDENT_AUDIT.md. The earlier degree-eight argument there separately proves Z_1 finite from the already established dim Z_3<=1, without relying on (1).

## 3. Global dimension bound

For independent zero triples, use the established exact outer reconstruction and projective fiber bounds: residual rank1 has fiber dimension<=3; residual ranks2,3,4,5 have fiber dimension<=2. Their proofs are respectively rank-one-residual-fiber-model/PROOF.md; diagonal-hartogs-fiber-bound/UNSQUARED_PENCIL.md; diagonal-hartogs-fiber-bound/PROOF.md; rank-four-compatible-fiber-bound/PROOF.md; and full-support-rank-five-dimension-bound/PROOF.md (all relative to the manuscript collection). Residual rank0 is impossible by repeated injectivity and the eigenline Chern obstruction. The integrated rank-at-least-six bound is rank-six-surface-reduction/COROLLARY.md.

Restoring the three nonzero input scalings gives:

    rank1: finite middle + fiber<=3 +3 scales => affine dimension<=6;
    rank2: finite middle + fiber<=2 +3 scales => affine dimension<=5;
    ranks3,4,5: middle dimension<=1 + fiber<=2 +3 scales => affine dimension<=6;
    ranks>=6: affine dimension<=6 by the imported theorem.

The fiber-dimension theorem on each locally closed rank stratum proves

    every affine independent-zero component has dimension at most SIX.

No existence of a dimension-six independent component is asserted, and tangent dimensions or nilpotent structures are not bounded by this result.

## 4. The unique top-dimensional all-nonzero component

The dependent zero triples with all three inputs nonzero are precisely triples whose three nonzero vectors span the same one-dimensional subspace of V (the same point of P(V)), by the repeated-pencil argument in full-support-rank-five-dimension-bound/PROOF.md, Section1. This diagonal scaling family is irreducible of dimension4+3=7 and is closed within the locus of triples with no zero input. Cyclic zero ensures it consists of zeros.

The independent part has dimension at most6. Its closure within the all-nonzero zero locus cannot contain the seven-dimensional diagonal. Thus the diagonal scaling family is the UNIQUE seven-dimensional irreducible component there; every other component has dimension at most6.

Zero-input coordinate pieces are excluded from this assertion. In the unrestricted affine zero locus those pieces have dimension10. This theorem does not assert that every zero is dependent, nor settle the broader higher-order/algebraicity research goal.

## Verification and sources

Independent mathematical audits are listed above. Public mathematical sources appear in the component proofs.
