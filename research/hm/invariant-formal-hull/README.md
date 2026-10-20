# The 79-variable ordinary deck-equivariant formal hull

This packet supplies the higher-order formal conclusion, not merely the tangent-space dimension: the completed full coefficient family is miniversal for marked ordinary deformations of the specified deck-linearized bundle on fixed X. Its Noetherian hull is k[[t1,...,t79]]. The group action and linearization are fixed, and the group acts trivially on the Artinian bases.

The full historical proof and its independent mathematical audit are retained. The audit includes a separate direct small-extension proof, not merely an approval label. This is the October 18, 2026 ordinary formal-smoothness result. The older 24-direction target-family proof is not republished or counted as a separate result here.

## Exact current prerequisites

- [PR179 coefficient family](https://github.com/Akilleez-QA/read-em-and-weep/blob/2b03992b32d2f5cf0509b6f4840adf08369f54b7/research/hm/cubic-loci/foundation-p01/COEFFICIENT-FAMILY.md): the actual smooth 79-dimensional family and injective Kodaira–Spencer map. This supplies geometric premise P, conditional on the explicitly specified literal presentation.
- [PR179 invariant cohomology](https://github.com/Akilleez-QA/read-em-and-weep/blob/2b03992b32d2f5cf0509b6f4840adf08369f54b7/research/hm/cubic-loci/foundation-p01/INVARIANT-COHOMOLOGY.md): independently proves the deck-invariant row (1,79,352,0,0), including D=79. It uses finite pushforward, classical HM cohomology and base change, not the historical rank calculation. Thus the historical proof's warning that D was imported is preserved as provenance; the present dependency chain supplies a structural proof of D.
- [PR125 presentation](https://github.com/Akilleez-QA/read-em-and-weep/blob/8281ea90d8a1ffd14eaa10af76174b4c25a32742/research/hm/hm-presentation-independent/PROOF.md) identifies the stipulated literal presentation with the classical HM bundle.
- [PR125 primary cohomology verification](https://github.com/Akilleez-QA/read-em-and-weep/blob/8281ea90d8a1ffd14eaa10af76174b4c25a32742/research/hm/hm_primary_source_verification.md) records the verified Decker–Schreyer proposition used in PR179. The structural argument and the cohomology theorem remain distinct inputs.

The source proof's characteristic-zero conclusion remains conditional on P and D for the specified data. PR179's base-change argument supplies these numerical dimensions for the stipulated characteristic-zero base changes, not arbitrary forms or positive characteristic.

## What is and is not proved

The family is formally smooth and tangent-bijective as a map to the marked equivariant deformation groupoid. Classifying maps and compatible isomorphisms exist; uniqueness, a fine moduli scheme, and algebraization of arbitrary formal maps are not asserted. No fixed-determinant variant is included. Scalar infinitesimal automorphisms are retained.

Ordinary all-order lifting is not star all-order lifting. The subsequent first-star-order theorem requires its own raw transgression and regular-cover inputs and is not proved in this packet. The unrestricted ordinary deformation space is not claimed smooth.

The historical statement that smoothness alone does not prove individual ordered products vanish remains logically correct. PR179 separately proves their vanishing for invariant inputs; that stronger multiplication result is not inferred from formal smoothness here.

## General theory

The proof uses [Stacks Project 06IL](https://stacks.math.columbia.edu/tag/06IL) for minimal versal formal objects and [0DVP](https://stacks.math.columbia.edu/tag/0DVP) for finite-projective patching. The independent audit additionally proves the lifting conclusion directly by the torsor of fixed-reduction lifts.
