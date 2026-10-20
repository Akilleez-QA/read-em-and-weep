# Corrected noncanonical contribution in the global contradiction

The global assembly needs every noncanonical supported orbit to contribute at least420 to the length of the same finite sheaf T=Ext²(B,O). A uniform noncanonical contribution of600 was asserted in an earlier publication-scope review, but is not supplied by a point-orbit gap of250 and exclusion of simple defects alone. This review statement is corrected here; the original assembly proof only used “no smaller contribution” than420.

## Exact inputs

Retain the established equivariant sheaf setup and the normalizer orbit classification: the canonical orbit has30 points; outside it the smallest possible orbit sizes below600 are250,300,375 and500. Suppose the separately proved local simple-defect exclusions apply to all supported orbits of those four sizes. Equivariance makes the stalk lengths constant on each orbit, and a nonzero finite-length stalk has a positive integer length. The exclusions therefore make that length at least2 on each of these four kinds of orbit. Orbits of size at least600 require only stalk length at least1.

These are orbit-size and local-module premises together, not an assertion that every noncanonical point orbit has at least500 or600 points. The proofs of the normalizer classification and simple-defect exclusions are required dependencies.

## Length calculation

The possible noncanonical contributions are bounded below by

    250·2=500, 300·2=600, 375·2=750, 500·2=1000,
    or600·1=600 for an orbit of size at least600.

Hence the warranted uniform noncanonical contribution is at least500. Improving the250 case to600 would require an additional stalk-length exclusion, such as length2, and is neither assumed nor claimed here.

The canonical local exclusions through length13 give contribution at least30·14=420 for a supported canonical orbit. Since T is nonzero and its support is a union of orbits, the corrected combined bound is

    length(T) ≥ min(420,500)=420.

The independent global upper bound length(T)≤390 therefore yields the same contradiction. The resulting generic-rank-ten and generic transverse length-five conclusions do not require the unsupported uniform600 claim. No actual source value or matrix is evaluated, and no higher-order or algebraicity assertion is added.

## Required proof packets

- [Canonical orbit](../../normalizer-rank-five/normalizer-minimal-point-orbit/PROOF.md) and [refined orbit gap](../../normalizer-rank-five/normalizer-refined-point-gap/PROOF.md).
- [250-point simple-defect exclusion](../../normalizer-rank-five/normalizer-250-simple-defect/PROOF.md).
- [300-point orbits](../../normalizer-rank-five/normalizer-300-point-orbits/PROOF.md), [375-point orbit](../../normalizer-rank-five/normalizer-375-point-orbit/PROOF.md), and [500-point orbits](../../normalizer-rank-five/normalizer-500-point-orbits/PROOF.md).
- [Local simple-defect character criterion](../minimal-local-defect-character/PROOF.md).

These are required scientific dependencies; their exact commit pins must accompany final publication.

## Optional stronger premise
The separate [250-point double-defect exclusion](../../normalizer-rank-five/normalizer-250-double-defect/PROOF.md), with its audit and stated hypotheses, upgrades that orbit to stalk length at least3 and contribution at least750. With this additional dependency, the other orbits give a uniform noncanonical bound600. The present global contradiction deliberately uses only the weaker500 chain and does not require this extra theorem.
