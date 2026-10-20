# Independent audit of full rectangular finiteness

## Verdict

The theorem in PROOF.md, Sections 1–4, is valid under its stated hypotheses. The entire closed rank-at-most-one (2,3) rectangular incidence has finite support and is a finite scheme over C. This is a stronger conclusion than finite middle image; no reducedness or absence of infinitesimal deformation follows.

The optional geometric ordered-lift statement in Section 5 is also valid with its explicit convention that one counts reduced closed ordered-lift images, not frames, parametrizations, or unrelated scroll embeddings.

## Closedness and constant-rank boundary

The boundary is the zero scheme of the determinant of the rank-five addition map X⊕Y→V. It is therefore closed in projective R before any use of completeness. The global pointwise argument excludes intersection dimension two, including at limiting points. Consequently its reduced irreducible components have addition rank exactly four everywhere. Reducedness is sufficient for the local constant-rank lemma: after inverting a rank-four minor, the residual matrix entries vanish on all closed points and hence vanish identically. No smoothness assumption is needed.

Projecting the kernel of addition into either summand identifies it with the common line h. This is an everywhere rank-one subbundle of the trivial V-bundle and defines a genuine morphism to P(V). Thus the polar-pair map is regular on the whole component, rather than only rational on a dense open. Its image lies in the closed polar determinantal locus D scheme-theoretically after reduction.

## Polar dependence and fixed hyperplane

At a boundary point, h and u are independent, and f(h,u,h) and f(h,u,u) are independent by the repeated-input identity. On H=X+Y, the first polar takes values in the line L=C f(h,u,h). Therefore its rank is exactly two, u is outside H, and H=P_hu^{-1}(L): the latter has dimension three plus one. This equality removes any hidden choice of a hyperplane after the polar pair is fixed.

The finite-polar theorem applies with exactly the same hypotheses. Its proof uses the canonical decomposition V=Ch⊕Cu⊕ker P_hu on each reduced projective component of D and constancy of projector entries. There is no dependence on the rectangular theorem, residual-rank classification, target-dimension bounds, or physical/source assumptions. An integral component mapping into finite D has constant pair, hence constant h, u, L, and H.

## Quotient projectors

With E=H/Ch fixed, X/Ch and Y/Ch are subbundles of E⊗O of ranks one and two. Their addition is an isomorphism on every fiber, hence globally. The associated projectors have regular scalar entries on an integral projective variety; all entries are constant. Each quotient subspace is consequently fixed, and taking its full inverse image in H fixes X and Y. Since these and u are all coordinates in the ambient product, the component is a point.

There is no application of projector rigidity to a nonproper open stratum. Complementary triples are treated by the separate complete-curve determinant-pole argument, whose Section 5.1 correctly allows degree d=0: its inequality forces both d=0 and determinant divisor degree zero, then both nonnegative Grassmannian degrees vanish. This excludes positive-dimensional components meeting the complementary open set.

A finite-type projective scheme with finite support is zero-dimensional and finite over C. This remains true with nilpotents and does not assert that the finite scheme is reduced.

## Optional ordered-lift geometry

For a type III triple, the scalar rectangular matrix is, up to nonzero scalar, [[0,0,1],[0,-1,0]]. The scalar is indeed nonzero because the rectangular image has rank exactly one everywhere on R. The matrix has rank two. Its (1,1) zero hypersurface in P¹×P² is the projectivization of the kernel of a surjection O³→O(1) over P¹. The kernel is O⊕O(-1), so this surface is F_1 and is irreducible.

More explicitly, if the first factor has coordinates [s:t], every second-factor solution has coordinates [a:bs:bt]. These are exactly the ordered type III parametrization coordinates. This establishes density, and in fact fiberwise coverage after the usual projective-bundle interpretation of the parameters. Thus its reduced closed image is uniquely determined by the triple and f. The stated restrictions on what is being counted are necessary and are correctly included.

## Scope
