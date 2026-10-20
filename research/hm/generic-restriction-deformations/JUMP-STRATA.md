# The orbit family at the tangent-jump strata

This is a bounded complement to PROOF.md, using the same audited restriction sequence. It does not assert unobstructedness on the determinant quadric.

For EVERY smooth quintic Xₚ the orbit family g↦(g*F)|Xₚ has injective 24-dimensional Kodaira–Spencer map, because its ambient map is an isomorphism and H¹B→H¹(B|Xₚ) is always injective. Write

    r = 2 − rank Φ(p) ∈ {0,1,2}.

Let R be a minimal deformation hull for the restriction on the fixed Xₚ. Its tangent dimension is 24+r, so there is a presentation

    R = C[[t₁,…,t₂₄,z₁,…,z_r]] / I,   I⊂m².

The formal orbit family supplies a continuous local homomorphism

    ρ:R→C[[u₁,…,u₂₄]].

The dual tangent map is surjective. Choose 24 source elements whose images have independent linear parts in u. By the formal inverse-function theorem their images give coordinates on the target power-series ring. The composite from the source power-series ring is therefore surjective. After changing formal coordinates in that source, its map to the target is

    t_i↦u_i,   z_j↦0.

Explicitly, after making the images of t_i the target coordinates, replace each remaining generator z_j by z_j−f_j(t), where f_j is its target image expressed in those coordinates. The linear part of this source substitution is invertible, so it is a formal coordinate change.

Because the composite factors through R, its kernel contains I. In these coordinates the kernel is (z₁,…,z_r), proving

    I ⊂ (z₁,…,z_r) ∩ m².

Thus the miniversal formal base contains a closed embedded smooth 24-dimensional formal subgerm induced by the algebraic group family. Its local Krull dimension is at least 24; its embedding dimension is 24+r. When r=0 the ideal is zero, recovering the generic theorem. When r=1 or2 the equations vanish on z=0 but can still contain mixed terms t_i z_j. Neither a formal product decomposition nor equations depending only on z follow. The transverse direction count r is a tangent-space count, not a bound on orders or number of obstruction equations, nor a proof that the whole base is singular.

This argument uses the compatible classifying map into a hull and the formal inverse-function theorem exactly as in PROOF.md. It does not require a universal global coarse moduli space, or uniqueness of the classifying map. No matrix/rank/polynomial-instance evaluation was performed.
