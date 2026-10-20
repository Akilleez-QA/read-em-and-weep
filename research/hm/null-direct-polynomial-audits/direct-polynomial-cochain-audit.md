# Audit: a direct polynomial representative for the actual pure obstruction

20 October 2026. Formal mathematical record; no obstruction coordinates were evaluated.

## Verdict and novelty

Accepted. The already audited eight-term formula yields a stronger, direct source-level bridge once the fixed first-order primitive and its global domains are supplied correctly:

For each pair p, there is one fixed affine base cover and a regular End-valued Čech two-cocycle

    C_p(A,B,C) ∈ Čech²(U,ρ*End H) ⊗ C[A,B,C]_2

whose class is the complete actual pure obstruction at every fiber where the stipulated root bundle exists. The class at other parameters is its polynomial extension. This proves homogeneous quadratic polynomiality without DVR extension or normality.

The new assertion is not the eight-term expansion, which [cusp-base-source-formula.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/871422b59c159d9e607735f2e0f33b953c4ea2b9/research/hm/null-cusp-base-source/cusp-base-source-formula.md) and [cusp-base-source-audit.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/871422b59c159d9e607735f2e0f33b953c4ea2b9/research/hm/null-cusp-base-source/cusp-base-source-audit.md) already establish. It is the existence of a single branch-independent regular base primitive, the elimination of all parameter-dependent refinements from the normalized source, and the consequent global polynomial cocycle. None of the six remaining obstruction values is computed or proved zero.

Inputs are the accepted actual first-order cancellation at F0, the actual root identity N²=p*L with L=O(1,1,1,1), the full PR16 ambient, and the eight-term identities. Pair-character Ext¹ vanishing is needed to identify the constructed boundary with the previously stipulated one, not to choose a primitive of a known exact first source.

## 1. Choose the base cover once

Let Y=(P¹)^4, M=ρ*End H, and J_p=O_Y(−2 in the two factors of p). Fix a finite affine cover U of Y refining the standard product coordinate cover and trivializing ρ*H and L. Further fixed affine refinements may be used to trivialize these bundles, but they are chosen over C and do not depend on F.

Y is separated, so finite intersections of these affine opens are affine. The same cover computes the coherent cohomology of M and M⊗J_p. Denote the fixed H and L transitions by h_e and l_e. They and their inverses are regular on their indicated overlaps. Their logarithmic derivatives are therefore regular differential coefficients on those overlaps.

An individual finite coordinate x_i is not asserted regular on every chart. On a product chart use w_i=x_i with η_i=y_i, or w_i=t_i=1/x_i with η_i=z_i=y_i/x_i². Then

    V_i|base=σ_iη_i∂w_i,
    V_i(η_i)=σ_iG_i'(w_i)/2,
    η_i²=G_i(w_i),

where σ_i=+1 on the finite chart and −1 on the infinite chart. Respectively

    G_i=Aw_i³+Bw_i²+Cw_i,
    G_i=Aw_i+Bw_i²+Cw_i³.

All G_i and G_i' have branch degree one. The odd-generator change η_infinity=x_i^(−2)η_finite is independent of A,B,C. Derivatives extend regularly to all localizations defining the fixed affine intersections. On any intersection, compute in the coordinates of one containing member and transform all odd generators and coefficients consistently.

This supplies the global-domain qualification missing from merely counting degrees in a common rational x-coordinate system.

## 2. Obtain one fixed regular first primitive

With actual compatible square-root frames, write g_e=τ_e h_e and τ_e²=l_e. The root frames can be obtained étale-locally by taking the square root of the invertible ratio between an initial root frame squared and the prescribed L frame. The resulting transitions are actual transitions, so τ_βγ τ_αβ=τ_αγ. They are not arbitrary independently chosen square roots of the edge transitions.

Differentiating before normalization gives

    V_i(g_e)=τ_e y_i[∂i+(∂i log l_e)/2]h_e

on a common finite coordinate domain, with the corresponding σ_i,η_i version on other charts. After normalization every scalar τ product cancels. The complete first source, including b_p, is therefore the pullback of a fixed regular M⊗J_p-valued Čech two-cochain c_p on U. Its coefficient expression is equation (1) of [cusp-base-source-formula.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/871422b59c159d9e607735f2e0f33b953c4ea2b9/research/hm/null-cusp-base-source/cusp-base-source-formula.md); it has no branch coefficients. The coefficients of q_i in the odd summand are also fixed. Coefficient extraction is not division by y_i at branch points.

Additional étale frame indices lying above the same base chart have h=l=1 and τ=±1. Their derivatives vanish. The normalized first source consequently depends only on the original base indices and descends to U. This is an explicit descent argument, stronger than observing that an arbitrary upstairs cochain is deck invariant.

The canonical finite-flat pair-character identification

    H²(X_F,End E)_p = H²(Y,M⊗J_p)

sends the actual first obstruction at F0 to [c_p]. The accepted cancellation there gives [c_p]=0. Acyclicity of the fixed cover therefore supplies a regular cochain X_p on that very cover with δX_p=−c_p, with the sign interpreted as in equation (1).

Choose this X_p once over C. No parameter division, parameter-dependent gauge, or solution over C(A,B,C) is needed. Existence of this regular cochain is a consequence of exactness in the fixed Čech complex; its physical coefficients have not been produced or evaluated. Put U_e=h_eX_{p,e}. These are fixed regular pair-twisted cochains, not untwisted global matrix functions.

For every actual root fiber define the normalized first lift by x_{p,e}=y_ry_sX_{p,e}, interpreted in the local odd generators, and u_{p,e}=g_ex_{p,e}. It solves the full first equation. Pair-character Ext¹ vanishing then identifies it up to reduction-preserving gauge with the stipulated original boundary. Full induced second-order gauge terms must be retained when making that comparison.

## 3. All eight terms are regular quadratic base expressions

The derivation identities in the audited source formula are exact. For example,

    V_i²(τ_e h_e)=τ_e[F_i∇_{i,e}²+(F_i'/2)∇_{i,e}]h_e,
    V_rV_s(τ_e h_e)=τ_e y_ry_s∇_{r,e}∇_{s,e}h_e.

The derivative of the connection coefficient is included in ∇². For the odd first lift, V_r(τ_e y_ry_sU_e)=τ_e y_s(F_r∇_r+F_r'/2)U_e, and similarly for s. These identities eliminate root factors only after their derivatives are accounted for.

The complete normalized residual is exactly H^−1(N1+…+N8) in [cusp-base-source-formula.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/871422b59c159d9e607735f2e0f33b953c4ea2b9/research/hm/null-cusp-base-source/cusp-base-source-formula.md). Its degree count is:

- N1, N6, N7: F_rF_s times fixed cochains.
- N2, N3: one external F times a degree-one D operator on fixed U.
- N4: two degree-one L operators, or F_rF_s times fixed mixed covariant derivatives.
- N5: a degree-one primitive a multiplied by one F and fixed Q and transition derivative.
- N8: one external F times the degree-one scalar operator d acting on the fixed gerbe coefficient β.

Thus every term has total branch degree two. ∇, h, l, U, Q, β and H^−1 are branch independent. The scalar primitives are a0=−Ax/2 and a∞=−Ct/2, both degree one. Neither T_p(g)g nor −μ_p(b_p,g) has been removed. The matrix order and Alexander–Whitney endpoints remain precisely those of the eight-term formula.

In chart coordinates w_i the same argument uses G_i,η_i,σ_i. Every coefficient is regular on its designated fixed base intersection and polynomial in A,B,C. Inverses of spatial transition units and fixed overlap coordinates are allowed on their domains; inverses of F, F', y, A, C, or the discriminant are not introduced.

## 4. Descent, coordinate compatibility, and closure

On any smooth parameter in S, use actual N∞ and compatible square frames to check the formula. Each original term has the common scalar τ_αγ after differentiation and multiplication. Its normalized coefficient therefore has no residual dependence on the étale root-frame choices. Extra ±1 transitions contribute no derivatives, and all cochains and ambient endpoints are pulled back from the fixed index map. Hence the resulting expression depends only on base indices and descends to a regular base two-cochain.

Different local coordinate and odd-generator descriptions agree there because they represent the same actual geometric residual. Both descriptions have already been shown to be polynomial, with regular coefficients on their fixed common intersection. Their difference vanishes for every parameter in the dense open S, so it is identically zero as a polynomial with coefficients in that fixed section space. This proves coordinate compatibility for all parameters without requiring an actual globally chosen root on the full parameter space.

Likewise, on every smooth parameter the complete algebroid identities and the solved first-order equation imply δC_p(F)=0. The Čech differential on M is branch independent, and δC_p is polynomial with coefficients in fixed section spaces. Dense-open vanishing therefore gives δC_p=0 identically. No individual N_j is asserted closed. This is a direct universal cocycle proof, not a limit argument or an application of singular HKR.

One may equivalently verify the identities in the universal finite-flat algebra with compatible local square frames wherever a root exists. The dense-open polynomial argument avoids introducing a global root gerbe or claiming a global root bundle at bad codimension-two parameters.

## 5. Actual-fiber interpretation and remaining scope

The universal polynomial cocycle has a class in H²(Y,M)⊗C[A,B,C]_2. On every smooth fiber it represents the complete actual pure obstruction for the specified boundary by §2. On an open parameter region with an actual root, the same root-frame identities identify its specialization with the actual residual, including at singular fibers. In particular N∞ exists over A≠0, so its specialization at (1,0,0) is the actual cusp class. This interpretation does not require guessing a root where none has been supplied.

The fixed primitive X need not have a chosen permutation-equivariant or D5-equivariant representative. Covariance and the compact target restriction are class-level statements supplied by the separately audited actual-family comparisons. The present proof establishes polynomiality and source identification, not literal equivariance of a selected cochain.

Combining it with those prior covariance results leaves the same six unknown coordinates, two in twist −1 and four in twist −2, with Q(F0)=v+Rv and v=Q(1,0,0). No coordinate, nonzero test, vanishing theorem, or second-order primitive is obtained by the degree argument. A physical implementation would still need actual h,l,X, all eight source terms, the certified comparison and line-calibration tests, and six cohomology evaluations modulo boundaries.

## Sources and provenance

Read [cusp-base-source-formula.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/871422b59c159d9e607735f2e0f33b953c4ea2b9/research/hm/null-cusp-base-source/cusp-base-source-formula.md) and [cusp-base-source-audit.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/871422b59c159d9e607735f2e0f33b953c4ea2b9/research/hm/null-cusp-base-source/cusp-base-source-audit.md) in full. The complete PR16 source was directly inspected during the preceding boundary task at commit c8aec970fd65a105f39f4e8aeb8a17f0f0053f89, blob a58834ab61e18a5dedd8a7bf20bec7121bfa9165. The fixed first-source and actual-family premises are established in [branch-boundary-extension.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/c9412e435d6349ea5c9395711aa794e3dd003641/research/hm/null-branch-polynomial-extension/branch-boundary-extension.md) and [branch-boundary-audit.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/c9412e435d6349ea5c9395711aa794e3dd003641/research/hm/null-branch-polynomial-extension/branch-boundary-audit.md).

This audit does not claim a fresh physical source calculation. Its additional bridge is the single fixed regular base primitive and the fixed-cover polynomial descent of the already known complete residual. Public posting remains pending and was not attempted.
