# Necessary endpoint ranks for one compatible radical element

**Craig Ward · 23 October 2026 · Update through PR988**

[PR988](https://github.com/Akilleez-QA/read-em-and-weep/blob/7ceeaa0bb1942ed628f7a25fa2f5fd3c3a1fe49d/research/hm/source126-compatible-line-ranks/PROOF.md) applies to a single nonzero source126 radical element j commuting with Q. It does not assume compatibility of the full two-dimensional radical, nor does it identify sums of images with the image of one element. The necessary catalogue frontier remains **four pairs and three labels**.

## 1. Exhaustive necessary rank lists

The pairs below are (rank j2, rank j4) on the actual 41- and 37-dimensional endpoints:

| Source type | Necessary pairs |
|---|---|
| Type I | (4,4), (9,9), (5,4), (9,4) |
| Type II | (4,4), (9,9), (5,4), (10,9), (9,4), (14,9) |
| Type III | (9,9), (10,9), (14,9) |

These are necessary footprints, not actual realizations or new catalogue pairs. In every type the fourth-endpoint P row is nonzero. The Type III extension uses the abstract unique Y-to-D covariant and saturation, not an unproved identification of the actual Y inclusion with a first polar. Compatibility further forces its fourth D row to be nonzero: otherwise the bundle image would lie in P O(-2), whose coefficient span cannot contain the actual nonzero A coefficient.

## 2. Exact image and kernel interfaces

Write im j2=uP+vD and im j4=P+δD. Let k be the multiplicity of im j2_D intersected with the actual D kernel of Q. Compatibility and surjectivity of Q on its entire D target give v=δ+k. Here u,k,δ are zero or one, while v≤1 in Type I and δ=1 in Type III.

For U=ker j2 and Z=ker j4, the actual restricted map has the full original kernel A+D and cokernel uP+kD. The possibility u=k=0 would make this preserved negative subpencil Q-surjective, forcing the same actual second A obstruction to vanish, contrary to its established nonvanishing. Thus (u,k) is one of (1,0), (0,1), (1,1), yielding exactly the table.

The induced quotient Q has kernel kD and cokernel (1-u)P. These identify actual subspaces and quotients; no preferred irreducible copies or full-radical collective-image equality is substituted.

## 3. Two rows force nonsurjectivity

A j-commuting surjection must induce a surjection from N2/im j2 to N4/im j4. Its necessary dimension inequality is rank j2−rank j4≤4. Exactly **(9,4) and (14,9)** violate it, by one dimension. Every commuting map then has rank at most36, including every Q+tT_a and after scalar-field extension.

The retained original Q rank33 and generic second rank3 give the matching lower bound. In either row, the generic original pencil therefore has rank exactly36, kernel dimension five and cokernel dimension one. After removing 33 unit pivots and three order-two pivots, the remaining 1×5 formal block is zero. Thus every later original generic Bockstein vanishes. Exceptional directions with enlarged earlier kernels are not computed.

This is not a contradiction excluding these rows: a generic cokernel line is not ruled out by a maximal-rank theorem established here. It also does not establish actual compatible-line existence.

## 4. Where endpoint-module data stop deciding the problem

For square-zero operators, a module of dimension n and operator rank r is a sum of r free dual-number blocks and n−2r simple blocks. A surjection to dimensions (m,s) exists exactly when r≥s and n−r≥m−s. The four other rows satisfy both inequalities. Explicit abstract surjections demonstrate that the rank-only obstruction cannot exclude surjectivity in them.

These maps need not be G-equivariant, multiplication maps or actual HM realizations. Their role is to establish the sharp boundary of this abstract obstruction, not produce a solution. Additional actual geometry must select or exclude the possible rows or supply a stronger obstruction.

## 5. Evidence and remaining scope

The full final proof and independent review were read. The review reports **105 exact checks** in ordinary and optimized Python, authenticating eight inputs and checking synthetic diagrams, image ranks, restricted/quotient cohomology and the four abstract surjections. Its final Type III refinement was reviewed and rerun on the final bytes. No actual parameter or instance rank was evaluated.

No separate interface-transfer theorem is incorporated here. The original repair, source realization and catalogue frontier remain unchanged. The accompanying chapter 49 independently records the collaborator's selected ninth-neighborhood gate; it is not a rank computation of these endpoint modules.
