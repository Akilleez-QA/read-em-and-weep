# Independent review of incidence direct images

Reviewed PROOF.md SHA256: e4dfdaaae3e80ba43a4e8c567fffa6b074b7a9b35a7cbd9d22a62e2f57858077.

Verdict: the structure-sheaf and dualizing-sheaf direct-image claims pass mathematical review, conditional on the explicitly pinned geometric inputs from PR555 and PR556. This is not proof-assistant verification.

## Actual unit and spectral support

The Koszul complex has terminal term O_Z in degree zero, so O_Z[0] is genuinely a subcomplex. Its quotient Q has the same negative-degree terms and zero degree-zero term. The projective-space calculation leaves only R^4 p_*Q^(-j), for 5<=j<=10. Their total degrees 4-j are strictly negative. The bounded spectral sequence therefore gives H^n(Rp_*Q)=0 for n>=0. The convergence and finite-filtration assertion is exactly the form supplied by [Stacks, Lemma 13.21.3](https://stacks.math.columbia.edu/tag/015J).

The resulting triangle identifies the map from O_Y with the natural unit, because the inclusion of the terminal Koszul term followed by its augmentation is O_Z -> i_*O_I. Its cohomology sequence gives surjectivity in degree zero and vanishing in positive degrees. No differential is reconstructed from its numerical dimensions. The stated R^4 term has the correct lines-convention factor: dualizing H^0(O(j-5) tensor det(A*)) gives Sym^(j-5) A tensor det(A).

## Scheme-theoretic target

An incidence kernel vector with a unit coordinate expresses one matrix column in terms of the other four, over the actual local coordinate ring. Thus all maximal minors vanish scheme-theoretically. Dominance and integrality of B make O_B -> pi_*O_I injective: its generic-point map embeds the function field, and regular functions on a nonempty open of an integral scheme embed in that field. Surjectivity follows from the already established ambient unit surjection. Exact and faithful closed-immersion pushforward then detects the higher-direct-image vanishings. Derived full faithfulness is neither needed nor asserted.

## Proper duality and determinant line

Both schemes are proper, finite type over C, Cohen-Macaulay and pure of dimension eight. Thus their base-normalized absolute dualizing complexes are omega[8], as in [Stacks, Lemma 48.27.5](https://stacks.math.columbia.edu/tag/0FVZ). [Stacks, Lemma 48.20.9(6)](https://stacks.math.columbia.edu/tag/0AU5) applies to the proper morphism and the bounded coherent object O_I. It identifies the dual of the canonical unit with the trace from Rpi_*omega_I[8] to omega_B[8]. Hence the trace is an isomorphism after the first theorem, and cancelling equal shifts is valid. This use of duality does not require pi to be flat or I to be smooth.

The constant line det(A*) tensor det(S*) tensor det(M) is retained, so the formula has not replaced a canonical equivariant identification by an unspecified trivialization. Projection formula with O_B(5) verifies both the displayed expression for omega_B and the vanishing of R^n pi_*O_I(5,0) for n>0. None of these statements makes omega_B invertible. Nor do they establish normality, rational singularities, or a smooth resolution.

No selected source-instance evaluation or numerical rank calculation is used in this review.
