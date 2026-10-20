# Actual cubic application of exceptional net locus bound

The preceding universal arguments are not duplicated. The universal dimension/Chern arguments are proved in unit03, using units01–02. Unit09 verifies their hypotheses for actual cubic kernels. The following retained conclusions include the earlier frontier exclusions and their final sharpening.

## Imported stratum notation

Write G_k for the exact-kernel-dimension-k stratum in Gr(3,V), K_W=ker(T_W), and C for the closed locus where K_W contains a three-dimensional determinant-zero net. Unit03 proves dim C≤4 under the rank-one-free hypotheses verified in unit09.

## 6. Consequence for the independent-triple frontier

The kernel-three determinant-zero branch is contained in C, hence has dimension at most four. Its fixed-plane independent-frame fibers have dimension five, by the imported net theorem; its total contribution therefore has dimension at most nine.

The exact criterion previously obtained was that an additional ten-dimensional component with generically independent triples exists exactly when

    dim (G_4 union {W in G_3: det|K_W=0}) = 5.

The second locus now has dimension at most four. Thus that criterion reduces to dim G_4=5. No upper bound of four for G_4 itself, no existence of its points, and no claim about reducedness or equidimensionality is proved here.

## 7. Exclusion of the entire reducible-determinant branch

For a four-dimensional rank-one-free kernel, determinant is nonzero by the universal constant-rank P^3 obstruction. If this homogeneous cubic is reducible over C, one of its factors has degree one. The corresponding hyperplane is a three-dimensional determinant-zero subspace of the kernel. Conversely the presence of such a hyperplane supplies a linear factor. The singular-net theorem in unit03, Section 1, proves its uniqueness and the irreducibility of the remaining smooth quadratic factor. Thus

    C = {W in G_3: det|K_W=0}
        union {W in G_4: det|K_W is reducible}.

This equality is of underlying sets; no scheme-theoretic equality of these strata is asserted. In particular, both loci on the right have dimension at most four. The independent-frame fibers over every point of C have dimension five by the imported results, so the independent-triple locus over C has dimension at most nine.

Consequently an additional ten-dimensional component with generically independent triples exists if and only if

    dim {W in G_4: det|K_W is irreducible} = 5.

This follows from the prior exact criterion, the proper-degeneracy upper bound dim G_4<=5, and the exclusion of C above. The irreducible-determinant four-kernel locus is the sole remaining possible source of an independent ten-dimensional component. Its dimension and actual nonemptiness remain unresolved.

The independent universal normal-form proof in [the reducible four kernel theorem](../reducible-four-kernel/PROOF.md) yields the same pointwise characterization; the singular-net theorem in unit03, Section 1 supplies all pointwise facts required here without relying on any scheme-level rigidity claim.
