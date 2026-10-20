# Punctual modification and the Leray differential

Under the additional hypothesis that the exceptional sheaf T has finite support, the full proof constructs the canonical sequence

    0 → D → D∨∨ → Q_exc → 0

and identifies T with ℰxt²(Q_exc,ω). Naturality of Serre duality identifies the Leray map d₂:H⁰(T)→H²(E), up to the single conventional sign, with the dual of H⁰(D∨∨)→H⁰(Q_exc). Thus its kernel is the dual of the evaluation cokernel.

## Dependencies and non-overlap

The exact predecessor is [PR247, commit 01c96a7e1b24685eacd5d1dc52ed0ea026490146](https://github.com/Akilleez-QA/read-em-and-weep/pull/247), specifically [PROOF.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/01c96a7e1b24685eacd5d1dc52ed0ea026490146/research/hm/relative-models/relative-chern-constraints/PROOF.md) Section1 and its relative-duality identity. That proof leaves the Leray transgression abstract. The present proof adds torsion-freeness under finite support, the canonical punctual quotient, and the identification of the structural map, not merely a dimension identity.

Only Section4 additionally uses [RIGIDITY_COROLLARY.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/01c96a7e1b24685eacd5d1dc52ed0ea026490146/research/hm/relative-models/relative-chern-constraints/RIGIDITY_COROLLARY.md), h⁰(D)=44, and the imported h²(K)=62. It obtains r=h⁰(D∨∨)−44 and h¹(E)=62−ℓ+r but evaluates neither r nor ℓ.

The exceptional-fiber dimension theorem in PR116 and the supplementary alternative proof are contextual, not an extra mathematical prerequisite. In particular there is no dependency cycle through that supplement.

## Conditional boundary

Finite support and nonemptiness are not proved. Exceptional curves invalidate the punctual argument and require the divisorial formulas in PR247. The residue-fiber dimension does not determine the quotient, length or evaluation map. All cohomology here concerns the full fixed-projection recipient, not the retained thirty-dimensional summand: block exchange interchanges projections.

HISTORICAL-AUDIT.md preserves the source proof's independent mathematical checks and labels their historical scope. SOURCE-BINDINGS.json records source and clarified public-text hashes. The theorem is structural, not an evaluation of an actual obstruction.

CURRENT-INDEPENDENT-REVIEW.md reviews this normalized edition; CURRENT-REVIEW-BINDING.json binds its exact files. Historical review scopes remain unchanged.
