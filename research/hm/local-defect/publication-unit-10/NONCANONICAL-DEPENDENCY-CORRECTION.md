# Noncanonical length bounds and their exact dependencies

This note clarifies the dependencies of the preserved390/420 corollaries and their historical audits. It does not alter their source proof bytes or assert that an unevaluated source realizes a candidate.

## Minimal inputs suffice for the420 conclusion

The normalizer orbit classification gives the canonical30-point orbit. Outside it, the possible orbit sizes below600 are250,300,375 and500. Excluding simple defects on those noncanonical orbits makes their common nonzero stalk length at least2. Thus their contributions are at least500,600,750 and1000 respectively; all remaining noncanonical orbits contribute at least600 by positive stalk length alone. The uniform conclusion supplied by these inputs is500, not600.

Canonical local exclusions through13 give30·14=420. Hence the nonzero defect has total length at least min(420,500)=420, with the identical result for the saturation defect under the stated finite-duality identification.

From only this minimal chain, totals strictly below500 must be supported on the canonical orbit, giving the necessary possibilities420,450,480. The corresponding necessaryq values for total5q are84,90,96. A classification of all totals below600 is not licensed by the simple-defect inputs alone.

## Stronger input restores the preserved below600 classification

The separate250-point double-defect exclusion proves that a supported250-point orbit has stalk length at least3, rather than merely2. Its contribution is then at least750. With that additional theorem, the300-point simple-defect bound600 is the smallest noncanonical contribution, so the uniform600 bound and the preserved below600 classification follow.

The exact additional dependency is [250-point double-defect exclusion](../../normalizer-rank-five/normalizer-250-double-defect/PROOF.md), with its mathematical audit. This theorem must be present with its orbit/stabilizer and local-module hypotheses checked before using the stronger statements. It is not needed for the420-versus390 global contradiction.

## Other required proof packets

- [Minimal orbit](../../normalizer-rank-five/normalizer-minimal-point-orbit/PROOF.md) and [refined orbit gap](../../normalizer-rank-five/normalizer-refined-point-gap/PROOF.md).
- [250-point simple defect](../../normalizer-rank-five/normalizer-250-simple-defect/PROOF.md).
- [300-point orbits](../../normalizer-rank-five/normalizer-300-point-orbits/PROOF.md), [375-point orbit](../../normalizer-rank-five/normalizer-375-point-orbit/PROOF.md), [500-point orbits](../../normalizer-rank-five/normalizer-500-point-orbits/PROOF.md).
- [Local simple-defect character criterion](../minimal-local-defect-character/PROOF.md).

Exact publication pins are required for these scientific imports. Point-orbit sizes and defect lengths are distinct quantities. No new source evaluation or formal checker execution is claimed.
