# No thirty-point orbit in any nonzero pure-V nonic member

**Craig Ward · 23 October 2026 · PR1042**

[Immutable full proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/848e947ae1575434e93a82a4ec8ba235606e3224/research/hm/source2-pure-v-thirty-orbit/PROOF.md).

The previously necessary thirty-point support alternative is excluded for **every nonzero coefficient pair**, not only the general member. On each of the fifteen involution mirrors, every basepoint is one of the known order-five, order-three or order-two axes. None has stabilizer exactly cyclic of order two, as a thirty-orbit would require.

## Full mirror and full coefficient pencil

Pinned finite-group generators identify q=0 as an actual involution mirror. Both p and t remain homogeneous variables; this is not an evaluated direction. Equivariance transports its calculation to all fifteen mirrors.

After removing the fixed degree-six axis divisor U²V, the restricted row has two residual binary cubics f,g, retaining independent α,β. Their homogeneous resultant is a nonzero constant times

    (α−β/2)²(α+β/2)²(α+β)².

At the three exceptional coefficient lines the complete homogeneous gcds are U, V and p²−t², respectively. Their zeros are precisely the existing order-five, order-three and Klein-four-stabilized order-two axes. Every other coefficient ratio has no residual common root. Direction endpoints and coefficient infinity are explicitly checked, so no leading-coefficient degeneration hides a projective case.

All thirty-point orbits would meet every mirror in two points with exactly C₂ stabilizer. The full mirror classification therefore rules out every such orbit. This argument is a uniform polynomial identity and resultant calculation, not a global numerical search.

This closes one support alternative without selecting an actual coefficient or source. The ambient reducedness of E₁₅ and E₁₂ comes from separate local-ideal theorems, not this exclusion. Together these results yield the [complete nonic classification](82-pure-v-complete-nonic-classification.md).
