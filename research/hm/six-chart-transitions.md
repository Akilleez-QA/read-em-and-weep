# Six normalized transition matrices

Status: generated and checked by exact polynomial identities. The first-order null-homotopy and second-order obstruction projection remain separate unfinished calculations.

## Files and representation

Run verify-hm-transitions.js with Node.js. The dependency-free program reconstructs the monad, both local contraction types, all six normalized inclusions/projections, and all transition matrices.

The companion hm-transition-anchors.json records six factored rational matrices F_i=N_i/d_i in variables a=v₁/v₀,b=v₂/v₀,c=v₃/v₀,d=v₄/v₀. A polynomial is represented by exponent-vector/coefficient pairs. No numerical evaluation or interpolation is used.

For column coordinates define
G_ij=F_i⁻¹F_j=adj(N_i)N_j/(d_i d_j).
The equality uses the checked identity det N_i=d_i².
For the left-row convention in the second-order algebroid calculation use g_ij=G_ijᵗ. Form nonlinear residuals in that row convention, then transpose the resulting End(E)-valued cocycle before applying the column-coordinate contraction.

## Construction in one global four-term basis

For a cyclic chart j, substitute v_{j+k}/v_j into the primary local formulas, using cyclic index order. Permute the rows of K₀ within each of its three five-dimensional blocks by r↦r+j modulo5, and permute projection columns accordingly.

Homogenization supplies a common polynomial denominator without expanding rational substitutions repeatedly. Rescale the second inclusion column by v_j and the second projection row by v_j⁻¹. This is the determinant-trivial normalization established in the local-contractions document.

For the auxiliary chart, rescale the second inclusion column by −d/a² and the second projection row by −a²/d.

Let I_i,P_i be these normalized matrices in the common four-term basis. Set F_i=P₀I_i. The direct transition is P_iI_j.

The certificate checks:
1. P_iI_i=1 on all six charts.
2. δI_i=0 and P_iγ=0 on all six charts.
3. det F_i=1 on all six charts.
4. F_i⁻¹F_j=P_iI_j for all36 ordered pairs.
5. G_ijG_jk=G_ik for all216 ordered triples.

Every check clears the specified denominators and compares integer polynomials exactly. Safe-integer assertions guard the arithmetic. The full216-cocycle pass was executed; it was not replaced by sampling.

The anchor representation uses the rational function field of the v₀-chart. It may introduce removable poles outside that chart. Equality with the direct chart formula P_iI_j establishes the appropriate continuation wherever the original frames are defined.

## Line-bundle refinement

On each elliptic factor choose N frames1 and q=y/x on the legal two-open refinement in the algebroid document. On a product chart let ν be the product of the selected q factors.

Changing from the reference meromorphic N frame to this local frame changes a normalized E frame by diag(ν,ν⁻¹). Therefore the full transitions on the line-refined atlas are
G_(i,ε),(j,δ)=diag(ν_ε⁻¹,ν_ε) G_ij diag(ν_δ,ν_δ⁻¹).

The determinant and cocycle identities for these extra factors follow by direct diagonal cancellation. The executable's216-triple count refers to the six carrier charts; it does not claim an exhaustive expanded test of every line-refined triple.

## Next required checks

Before interpreting any second-order output, the implemented cochain comparison must pass:
- For N and N⁻¹, the first-order compensated residual projects to16Π=−4[q₁∪q₂+q₃∪q₄].
- For E, the first-order compensated residual projects to zero.

These checks bind the gerbe sign, row/column conversion, refinement and finite comparison. A failed check invalidates that implementation before any second-order inference.

The present certificate does not solve the first-order cochain equation, instantiate the complete refinement comparison, or compute the full-sign second-order obstruction.
