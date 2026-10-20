# Historical mathematical audit receipt

This is a preserved review of the source mathematical manuscript, not a fresh review of the publication bytes. Hashes quoted below identify the historical source versions. See [hm-quintic-restriction-PUBLICATION-CHECK.md](../hm-quintic-restriction-PUBLICATION-CHECK.md) for the final-publication review.

# Independent audit of the nonzero-scalar corollary

## Verdict and dependency boundary

**Pass.** The new corollary correctly applies the separately established c≠0 theorem. Its pointwise and relative conclusions now hold for the actual HM bundle without a remaining scalar-case condition, subject to the explicitly imported geometric inputs.

Audited [NONZERO-COROLLARY.md](NONZERO-COROLLARY.md) SHA-256:

`038c429400ac00da021177fc123150e3e4ae6dc6056daa7475b2dd6162c35a2a`.

I read the final [scalar-propagation audit](../quintic-scalar-propagation/AUDIT.md) and verified that its recorded proof hash equals the current on-disk [scalar-propagation proof](../quintic-scalar-propagation/PROOF.md) hash:

`35a93234687c5d79533f8fc55a7589b3cae6546e683dd3e4c192adbbc3d89c4c`.

This is an application audit. It accepts the independently audited nonvanishing theorem as a dependency and does not re-prove scalar closure. Earlier [PROOF.md](PROOF.md) and [RELATIVE.md](RELATIVE.md), and their independent audits, are unchanged. Their zero-scalar implications remain valid conditional statements, although their zero branch is now excluded for the actual bundle.

## Checked consequences

1. Since Φ=cΨ with c≠0, its pointwise rank equals that of Ψ. Substitution into the previously audited restriction theorem gives the precise Ext row (1,26−r,26−r,1). Simplicity, nonemptiness of all three smooth-quintic strata, their linear/quadric descriptions, and the general value 24 all transfer without additional hypotheses or calculations.

2. Nonvanishing activates the injective-sheaf-map branch of the relative theorem. Hence R¹π_*𝔅 is canonically the constant rank-24 bundle H¹B⊗O on all Ω. Its base-change map is injective with canonical cokernel Tor₁(𝒞,k(x)), of dimension 2−rank Ψ(p). Therefore the claimed dimensions 0,1,2 at ranks 2,1,0 are correct. The individual H¹ spaces at a jump point are not the ordinary fibers of that rank-24 bundle. No claim of a universal tangent bundle with those fibers is made.

3. The canonical degree-two sequence retains the necessary O(−1) twist on its quotient. The cokernel 𝒞 is that of the actual universal map induced by Φ. Nonzero scaling of the abstract presentation does not change its image or cokernel, so using the Ψ determinant quadric to describe its support is legitimate. The previously audited rank-one maximal Cohen–Macaulay property and local freeness away from the vertex apply. Degree-two base change is an isomorphism at every point as asserted; this does not require R² to be locally free and is consistent with its torsion along the quadric.

4. The determinant equation is an actual locus where middle Ext dimensions rise above the general value. Its scaling ambiguity is harmless because det(cΨ)=c²det Ψ. It remains different from the discriminant of singular quintic hypersurfaces: its intersection with the smooth-quintic locus is nonempty, as already proved.

The corollary does not silently assert a numerical normalization of c, a value of an obstruction map, unobstructedness, a local moduli-space dimension, or a cofactor rank. None of those conclusions follows merely from c≠0. Its stated limits are correct.

## Scope

Only static proof/audit reads, hashes, and this local audit-file write were used. No selected polynomial, actual HM map, scalar value, or matrix rank was evaluated. No previously audited conditional file or external application was changed.
