# Actual cubic application of isotropic four kernel exclusion

The preceding universal arguments are not duplicated. Sections1–4 are proved in unit02, using the net theorem and P³ obstruction of unit01. The actual rank-one-free kernel and spectral incidence are supplied by unit09. The existence corollary uses the preserved constant-rank-net application§7 in this packet.

## 5. Consequence for the three-plane kernel problem

The kernel K_W in [the general three plane kernel theorem](../../../global-kernel-incidence/general-three-plane-kernel/PROOF.md) contains no nonzero rank-one element. Hence if dim K_W=4, its trace-square restriction cannot vanish identically. This removes the totally isotropic branch in that dimension.

This lemma alone does not exclude restricted quadratic ranks one or two, and does not by itself establish an independent zero frame for every four-dimensional kernel. Those cases require the remaining factor-pattern exclusions from the exact polynomial criterion. No claim about any actual kernel, its dimension, or its quadratic rank is made beyond the conditional universal statement above.

## 6. Combined corollary: all four-dimensional kernels have independent zeros

Import the independently reviewed universal classification and Section 7 of [the constant rank kernel nets theorem](../constant-rank-kernel-nets/PROOF.md). That result proves that a four-dimensional rank-one-free subspace K⊂sl(U) with q|K nonzero has nonempty spectral incidence

    X_K={ [A]∈P(K): det A=0, tr(A²)≠0 }.

The isotropic-exclusion theorem in unit02, Section 4 removes its remaining q≡0 alternative. Thus X_K is nonempty for every such K. Moreover h|K is nonzero by the constant-rank P³ obstruction in [the full cubic locus dimension theorem](../../../global-kernel-incidence/full-cubic-locus-dimension/PROOF.md). Its projective zero scheme is a cubic hypersurface in P³, all of whose irreducible components have dimension two. The nonempty open subscheme X_K is therefore pure of dimension two (in the sense that every irreducible component has dimension two). No reducedness or smoothness assertion is made.

For an actual structural kernel K_W of dimension four, the imported finite étale oriented cover and principal (G_m)³-bundle construction identify the independent-frame fiber over W. It is nonempty and pure of dimension five. Finite étale covers and Zariski locally trivial torus bundles preserve the relevant component-dimension calculation; this does not assert that the fiber is smooth or irreducible.

## 7. Exact criterion for an additional ten-dimensional independent component

Retain all structural hypotheses and notation of [the full cubic locus dimension theorem](../../../global-kernel-incidence/full-cubic-locus-dimension/PROOF.md), in particular dim V=5, dim Z=10, and the proper degeneracy-locus bound dim G_k≤5 for k≥2. Let

    B = G_4 ∪ { W∈G_3 : det|K_W is identically zero }.

This is a constructible locus in Gr(3,V). The second part is closed within the constant-kernel-rank stratum G_3: vanishing of all coefficients of the restricted determinant is the zero locus of a section of a twisted third symmetric-power kernel bundle. Dimension of B refers to dimension of its underlying constructible set (equivalently its closure). Empty B is allowed.

The span morphism from independent zero triples has a nonempty fiber of pure dimension five over every W∈B. For G_4 this is Section 6. For the G_3 part it follows from the constant-rank-net theorem: the fixed-plane frame fiber is in fact smooth and irreducible of dimension five. We make no corresponding smoothness or irreducibility claim in the G_4 case.

Give B a finite locally closed stratification and restrict the span morphism to each stratum, with reduced structures when computing dimensions. The dimension theorem for finite-type morphisms with all geometric fibers of dimension five gives

    dim (Z^(3)|B) = dim B + 5

when B is nonempty. One way to see the equality is to stratify further so that the dimensions of fibers of each irreducible component over its image are constant. On each such piece the dimension of the total space is the dimension of its image plus its fiber dimension. The upper bound is dim B+5. Over an irreducible top-dimensional stratum of B, the finitely many component images cover the stratum, so some are dominant; the generic full fiber still has dimension five, and at least one dominant component attains this fiber dimension. That component gives the reverse inequality. This argument requires neither flatness nor a proper span morphism.

Outside B, the independent-triple part has dimension at most nine: the k≤2 cases have this bound in the full-cubic-dimension theorem, and for k=3 with h nonzero the spectral incidence has dimension at most one, giving frame fiber dimension at most four over a base of dimension at most five. No k>4 occurs.

It follows that the following are equivalent:

1. The full cubic zero locus Z has a ten-dimensional irreducible component whose generic triple is independent.
2. dim B=5.

Indeed, if dim B=5, then Z^(3)|B has dimension ten, so its closure contains a ten-dimensional irreducible component of Z meeting the independent open. Conversely a ten-dimensional component meeting that open has a ten-dimensional independent part. The complement of B contributes at most nine, so its part over B has dimension ten, forcing dim B=5 by the displayed dimension equality and dim B≤5.

This is an exact conditional criterion, not an existence statement: the nonemptiness and dimensions of the actual loci comprising B are still undetermined. In particular no generic kernel dimension, additional component count, global smoothness, or equidimensionality of Z is asserted.
