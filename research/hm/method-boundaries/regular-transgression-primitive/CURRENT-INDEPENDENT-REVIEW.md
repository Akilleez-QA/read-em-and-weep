# Current independent mathematical review

Date: 20 October 2026. Verdict: scoped PASS for the exact edition bound in CURRENT-REVIEW-BINDING.json.

## Exact symbolic identity

In a common column frame, the pinned curvature source gives delta kappa=-theta-qE. Transposing the pinned E operator gives one half of du_jk wedge theta_ij minus du_ij wedge theta_jk, with no transpose-reversal sign because the differentiated factors are scalar. Transitive transport and scalar restriction compatibility suffice; no differentiated matrix-transport commutation is assumed.

Writing f=du and F=delta u gives f_ik=f_ij+f_jk-dF. Expanding delta of B_ij=f_ij wedge(kappa_i+kappa_j)/2 produces the two connection differences and positive dF wedge(kappa_i+kappa_k)/2. Substitution proves E^t=-delta B+D with exactly the signs in the proof. The defect is essential for arbitrary nonclosed edge scalars.

For the full contraction K, the quarter normalization yields the eighth coefficients in D_K. The pinned Lambda retains both the projection trace and the eta-weighted gerbe term. The full two-term K expression and all its I,P,h,D and scalar derivatives are retained. The compact S scalar agrees term by term with source equation (21), including -15 q_c q_d/8. Applying the identity either to K/4 or to all of t-prime is valid; the latter uses delta t-prime=F rather than replacing it with Lambda/4. These are alternative equalities, not two simultaneous boundary removals.

## Endpoint-linear exclusion

For the full constant-coefficient alpha,beta ansatz, direct expansion gives formula (K). In the closed-scalar and qE=0 restriction, independent cross terms force alpha=beta=-1/2. These degrees of freedom are genuinely available under the descent equation: the vertex kappa differences and scalar edge differentials can be selected independently on a triple subject to their stated additive relations. With theta=qE=0 and all kappas equal to a nonzero formal one-form c, a nonclosed scalar with only du_ik wedge c nonzero makes E=0 but delta P=du_ik wedge c. Thus the universal identity fails. No actual source value or matrix instance enters this free-symbol argument.

The conclusion excludes only the quantified endpoint-linear ansatz. It cannot establish source nonvanishing, forbid source-specific cancellation with Q2, or exclude another regular primitive. The source K and qE have extra dependencies not imposed in that universal algebra. Conditional regularity is stated correctly, and a symmetry projection may be used only when defined on the actual cochains and commuting with delta.

## Source, overlap and later-result review

All five sources cited in PROOF.md were read at the precise commits and matched the stated Git blobs. The corrected common-frame convention is -L^t, without the spurious scalar derivative of untransported arrays. The complete normal form at 4659e4425c6b5ab6b1899e6af93656ac03ff0862 has a single combined boundary. Any comparison must carry the whole present equality through its maps, not subtract the old boundary again.

PR334 already contains the endpoint-average identity, the contraction/Q2 residual, and the whole-scalar reduction. Under theta_row=-kappa^t and chi=qE^t its notation yields the same formulas. The additional bounded two-parameter endpoint-linear exclusion here is distinct from PR334's particular contraction-only combined-Q2 countercontrol. Novelty is not claimed for the reused identity or beyond the inspected public antecedents.

The historical uncertainty language is explicitly limited by SCOPE.md. PR145's conditional canonical mixed-class vanishing is compatible with the present universal ansatz failure; it neither proves the displayed source-specific residual identically zero nor provides evaluated primitive coefficients. No source-instance evaluation, executable control rerun, or formal proof-assistant certification was performed.
