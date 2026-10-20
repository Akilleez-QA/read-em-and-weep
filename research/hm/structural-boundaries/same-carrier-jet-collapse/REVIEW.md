# Independent structural audit

Verdict: **PASS for the same-carrier structural lemma, all displayed new algebraic-jet vanishings, and the direct literal-source reduction**, with the dependency and scope qualifications below. No sign correction is required.

## Artifact binding

- Reviewed file: `PROOF.md`
- SHA-256: `2e1d0c5e43302f66bedb114a0676d3fa928e73882498d21c54f9a7feab710901`
- Review date: 2026-10-18 UTC

## Independently checked

The accepted identity `P_c I_c=Id` yields the diagonal cocharacter transition on a full same-carrier owner intersection, rather than merely at a point. Product-factor derivations give `L_d=lambda_d h`, `U_d=eta_d h`, and zero distinct-axis derivatives of these currents. Consequently the normalized cross-axis second derivatives are central, while the literal `k` and all derivatives of `gk` vanish identically.

Direct comparison with the inert compiler's `Source.k`, `Source.mu2`, `Source.E` and `Source.residual` confirms the displayed mixed coefficient

    (eta_0 lambda_1-eta_1 lambda_0)
    (eta_2 lambda_3-eta_3 lambda_2)/4,

the scalar normalized baseline, both zero `Fk` branches, every sign in the surviving `E` terms, and the stated fluxes. Differentiating those fluxes gives exactly the residual: the additional product-rule terms vanish by transverse independence of the currents, not by any assertion about scalar-solver derivatives. The displayed literal current-curl vanishes because its `k` factors vanish. The coefficient-functional formula follows directly from its stated commutator definition.

The new jet claims were also checked directly against `dependencies/null-covariant-jet-transgression.md`, equations (5)-(8) and section 5. Every summand of `S2` and `M2` contains a distinct-axis `H` or `J`, so both vanish. Every component of `Phi` contains such an `H`. The nested-bracket `C4`, both midpoint curvatures, and all terms of `Q4=R22+R31` vanish because the currents commute. In particular, the scalar quantities `Delta_p` need not vanish: their factors `M_p` do. Thus `R_alg=0` follows from the displayed decomposition, and the new covariant-adjoint kernel term vanishes because its argument `Phi` is identically zero. This does not dispose of the older scalar-current flux or its kernel derivatives.

The rational-section argument is adequate: prove the formulas on a dense common unit locus and extend identities between regular source sections on the genuine owner intersection. Zero exponent differences are interpreted as identically zero without requiring an inverse of `r_d` at its zeros. This avoids a global logarithm and does not alter the physical frame or reset a connection.

## Dependencies and limitations

The zero substitutions in the explicit PR79 formulas were independently checked as described above. This review does not re-prove the general transgression identity, the generic identification `R_alg=Q4+S2`, or the complete normal-form defect-family accounting. Those remain cited dependencies with their original premises; the direct literal-source baseline reduction provides a separate check of the same-carrier conclusion.

Same-axis normalized jets are not asserted to vanish. All eight complementary scalar derivatives, the old scalar-current flux, kernel/weight/test/HPL/selector derivatives, and current-F cup terms remain. A local divergence is not thereby a Cech coboundary. Mixed-carrier inserted owners cannot be discarded. No global flux-domain claim, detector-count reduction, complete-target vanishing, obstruction value follows.

## Method

Only inert file reads, mathematical manipulation, file hashes, and writing this review were used. Relevant accepted background was read from `same-pair-ordinary-twist-exclusion-20261018/PROOF.md`; the literal compiler was read from `complementary-scalar-derivative-20261018/inputs/compiler.py.txt`; the new algebraic-jet formulas were read from the local dependency named above. No source/model/matrix/polynomial/point/jet evaluator, source program, numerical specialization, or executable mathematical checker was run. The hash binds the reviewed text; it is not an independent authentication of the externally cited sources.
