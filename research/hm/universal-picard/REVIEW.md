# Independent review: universal Picard gluing

Verdict: PASS, conditional on the exact geometric inputs pinned in PROOF.md. This is an independent mathematical review, not a formal proof-assistant check. No selected actual HM/source instance, coefficient matrix, or numerical rank was evaluated.

## Scope and dependencies

The review uses the actual conductor and residual-fibration dictionary of PR582, commit ec6e753518a59406b16e565b042621afad635cff, together with its pinned dependencies. In particular the two branch residues, five surface double points per base node, reduced sixty-point restriction factorization, and elliptic summand N=O_B(-5) are hypotheses imported from those proofs. It does not independently reestablish the source geometry.

## Checks

1. **The family is a line bundle on the surface.** At a surface double point, the ring is the fiber product of its two smooth branch rings over C. After extending scalars to A, the glued module consists of branch pairs whose residues satisfy f(0)=t_z g(0). Multiplication by the branch pair (t_z,1) identifies the ordinary fiber-product ring with this module; the inverse rescales the first branch by t_z^{-1}. Thus the unit gluing construction gives an invertible module. This concerns the surface, and is different from the conductor kernel after pushing to the nodal base.

2. **Universal kernel.** The residue matrix A^2 to A^5 is injective: subtracting two rows produces a nonzero difference of independent Laurent variables, which is a nonzerodivisor in A. This remains true after localization in the full parameter torus, including at a point where the difference specializes to zero. Hence the universal kernel is the sheaf of functions vanishing at all twelve branch preimages, h_*O_B(-D) external-product O_P. One must not replace localization by restriction to the uniform subtorus; the latter is a different, nonflat base change.

3. **Defect and Tor.** The displayed resolution 0 to A^2 to A^5 to K_q to 0 is exact. Tensoring with a parameter residue field gives Tor_1 equal to the kernel of the specialized matrix, of dimension one at a uniform block and zero otherwise. Higher Tor vanishes. Because the original cokernel is a module on q times P, all these Tor modules carry the residue action of the base local ring. There is no hidden branch action on the one-dimensional Tor term.

4. **Elliptic factor and derived base change.** Pullback of the fixed elliptic splitting along the flat product projection is valid. The relative Ext^1 group is H^1 of a sheaf supported on a scheme finite over affine P, so it vanishes. Thus the actual point-restriction factorization annihilates the elliptic component before the gluing weights and finite pushforward are applied. The resulting two-term complex and elliptic summand are parameter-flat. Their derived specialization is the actual fixed-fiber normalization complex with the specialized gluing weights. The argument establishes the base-change comparison, not just equality of dimensions.

5. **Ordinary specialization.** The conductor specialization embeds in the actual fiber kernel. Its quotient is one residue line at each uniform block and zero at each nonuniform block. Equivalently, the low-degree Tor exact sequence gives equation (9). At a uniform block its completed stalk is 0 to m_R to R_tau to k to 0. This sequence cannot split because R_tau is torsion-free under the nonzerodivisor s+t, whereas k is killed by that element. The total quotient length is 6-r, and the degree change from -6 to -r agrees with that length.

6. **Relative obstruction.** Were the relative complex a direct sum of its cohomology sheaves near a uniform parameter, degree-zero cohomology after derived specialization would be m_R direct-sum k at that node. Actual derived base change gives R_tau, isomorphic to R. The former has nonzero torsion under s+t and the latter does not. This invariant proves the contradiction without presupposing an Ext-group vanishing and survives faithful flat completion. The elliptic summand is parameter-flat and contributes no extra degree-zero Tor.

7. **Sharpness of the locus.** At an all-nonuniform parameter, select one unequal pair in each of the six blocks and invert their differences. The resulting unit two-by-two minors give explicit left inverses of all six residue matrices. Their images have complements, yielding the asserted parameter-local cohomology splitting. Each uniform-block subtorus is smooth of codimension four. Consequently the union of these subtori is exactly the obstruction locus for existence on a parameter neighborhood. No global complement on the entire complementary open is claimed or needed.

## Conclusion

The proof establishes a genuine family-level distinction: all individual fibers have the module splitting proved in PR582, while the universal family fails to split in every parameter neighborhood meeting a uniform block. Derived base change itself holds; the obstruction is the nonflat defect and its nontrivial residue-line extension. The result is about coherent module complexes and Picard gluing, not multiplicative formality or higher-order/algebraicity of the original HM construction.
