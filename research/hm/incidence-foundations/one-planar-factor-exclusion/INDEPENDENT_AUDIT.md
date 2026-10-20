# Independent audit of the one-planar-factor exclusion

Audited `/research/hm/incidence-foundations/one-planar-factor-exclusion/PROOF.md`, sections 1–4, over C. Verdict: the theorem and its proof are valid as stated. No correction is needed. Section 5 contains integration assertions rather than ingredients of this theorem; those prior exclusions were not independently checked in this audit.

## Hypotheses actually used

E has dimension four, U is a three-dimensional subspace, K has dimension at most five in Sym²E, and an integral surface X in P(U)×P(E) dominates P(U). Its second image is nonplanar. Every product from X belongs to K. Neither compatibility nor square avoidance is used.

## Incidence and matrix-rank checks

The dense open where the transverse coordinate of b is nonzero still has dense image in the first plane: otherwise its image would lie in a proper closed subset, forcing the entire integral X into the inverse image of that subset. Thus the quotient image of K′ spans U, and dim K0≤2.

For nonzero quadrics in Sym²U, ordered linear factorizations are finite by unique factorization. Consequently the factor-pair incidence above P(K0) has dimension at most one, including the possibility that K0 is zero. Generic kernel dimension at least two would produce a nonzero vector in its intersection with U for general a, contradicting this incidence dimension bound. The full constraint matrix therefore has generic rank three, and its kernel map parametrizes the dense graph in X.

Three rows independent over the rational function field are automatically independent over C. Since the q≥4 constraint rows are independent over C, one can add a fourth C-independent row. The resulting square matrix retains generic rank three; its generic kernel equals that of the full matrix by containment and equal dimension.

## Adjugate factorization over the polynomial ring

The UFD argument is sound even when minors have common factors. Choose a nonzero column of adj(N), divide by its homogeneous gcd, and call the result c. Every other column is a rational multiple f of c. For each irreducible polynomial p, some entry of primitive c has p-valuation zero, so polynomiality of f c implies v_p(f)≥0. Hence f is polynomial. Divide the vector of these polynomial multipliers by its homogeneous gcd h to obtain primitive r. Homogeneity provides uniform nonzero-entry degrees and gives deg h+deg c+deg r=3.

The adjugate identities imply Nc=0 and rᵗN=0. Nonplanarity forces deg c≥2, since four linear forms in three variables have a constant dependence. Constant-row independence forces deg r≥1. Thus c has degree two, r degree one, and h is constant. There is no missing alternative involving base points or common divisors.

## Coordinate normalization and symmetric blocks

Constant row changes preserve both the space of constraints and the symmetric U×U restriction of each constraint. In the current strengthened version, write r=C a with C a rank-three constant 4×3 matrix. An invertible constant transformation sends C to [I3;0]; applying the inverse-transpose transformation to the rows of N then gives r=(x,y,z,0) in the original source coordinates. No source or target coordinate change is needed. The earlier simultaneous-U-basis normalization was also valid because symmetric matrices change by congruence, but this row-only argument removes the issue entirely.

In the span-two case, coprimality of x and y gives R1=y t and R2=−x t with constant nonzero t. Therefore t c=0 identically and the second image is planar, the required contradiction.

In the span-three case, let q_i(a)=aᵗ A_i a. The relation Σa_i A_i a=0 implies F=Σa_i q_i=0. Differentiation yields ∂_jF=q_j+2(Σa_i A_i a)_j=q_j, so all q_j vanish and all symmetric A_j vanish. The remaining transverse coefficient matrix is skew-symmetric of odd size three, hence singular; its constant row dependence is a constant dependence of the corresponding rows of N. This contradicts their independence.

## Integration boundary

The result excludes one planar and one nonplanar ordered surface image under the stated span bound. It does not address the both-nonplanar case. The broader frontier statement in section 5 is justified only together with the separately established earlier exclusions. This audit does not supply or assume those earlier proofs as part of the main theorem.

