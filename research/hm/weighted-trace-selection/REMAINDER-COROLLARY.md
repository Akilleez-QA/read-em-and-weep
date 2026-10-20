# The transported remainder and collision restriction

## Scope convention

The assertions below concern coefficient geometry, finite-group actions and the stated coherent cohomology. References to unevaluated coordinates mean that this argument does not evaluate them; they are not a claim about the latest status of every other argument. The raw-source regularity, coefficient/character identification and raw-to-canonical class comparison are separate hypotheses wherever a source application is discussed. No first-order lifting theorem, higher-order obstruction vanishing, formal integrability or algebraicity follows merely from these coefficient statements.

Work over C on Z=(P¹)^4, with A=O(1,1,1,1), a locally free geometric coefficient E, and D the reduced union of the four triple diagonals. Use the normalization σ₁−σ₂=3(x₁−x₄)(x₃−x₂), and its two relabelings, with σ₁+σ₂+σ₃=0. These weights are four times those in PROOF.md §2; the remainder scales by the same factor, without changing any ideal or vanishing criterion. On a common affine chart write a=x₁−x₄, b=x₂−x₄ and c=x₃−x₄. For genuine, fully transported regular cochains r_i on common intersections, set

    T=(1/9) Σ_(i<j) (σ_i−σ_j)(r_i−r_j).

The full weight-ideal proof and its independent closure review are already committed in [WEIGHT-GEOMETRY-INPUTS.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/aab61d34a84c9b8b5a908606a7beb7212d45fe7c/research/conductor-normalization/ideal-power-contractions/WEIGHT-GEOMETRY-INPUTS.md) and [WEIGHT-GEOMETRY-HISTORICAL-AUDIT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/aab61d34a84c9b8b5a908606a7beb7212d45fe7c/research/conductor-normalization/ideal-power-contractions/WEIGHT-GEOMETRY-HISTORICAL-AUDIT.md). In particular I_D is the image ideal of the two-dimensional weight space and lies in the square of the small-diagonal ideal. The full coset normalization and Leibniz formulas are in [the weighted remainder proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/4edb97ceeb159778fa20ffd33c0e540af1292e06/research/hm/null-retained-weighted-remainder/WEIGHTED-RESULT.md).

## Consequence and proof


Each summand defining T is a section of I_D tensor A tensor E, provided the r_i have first been transported to the same coefficient frame and intersection. Therefore T restricts to zero on D scheme-theoretically, not merely at generic reduced root configurations.

Near the quadruple-root diagonal, its ideal is J=(a,b,c). Both generators of I_D are quadratic in a,b,c, so I_D is contained in J squared. Consequently T lies in J squared tensor A tensor E. Near a generic triple-root diagonal, the weight ideal instead has first-order transverse generators, as the rank-two Jacobian shows.

The weight ideal alone does not give vanishing on the entire simple-root-collision divisor. For example, on the formal divisor x1=x2 with the other roots distinct, sigma_2=sigma_3 but sigma_1 is generally different; the weighted formula becomes

    T = (sigma_1/3) [r_1-(r_2+r_3)/2].

This is only an identity of restricted cochains. The actual source and its stabilizer/frame action can impose additional cancellations. No claim of actual nonvanishing on this divisor is made.

Vanishing upon restriction to D does not imply that a closed T is a boundary on Z. The Koszul sequence is a coefficient resolution, not a contracting homotopy for the source's Cech complex. In particular, rewriting T with two generators need not make their coefficient cochains individually closed or exact. Establishing a primitive still requires a cohomological argument or an explicit regular h with delta h=T, together with the source-to-canonical comparison boundary.


If T is closed for the O_Z-linear Čech differential, its ideal-valued lift is closed because I_DAE→AE is an injective sheaf map and hence gives an injective map in every Čech degree. This does not imply that an arbitrary preimage under U⊗E→I_DAE is closed. The cited historical audit proves this distinction in full.
