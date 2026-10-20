# Finite étale covers cannot split the actual thickening

Retain the smooth connected rank-ten open U, its actual square-zero thickening U⊂T, nilbundle N, and nonzero algebra-extension class kappa in H1(U,T_U⊗N) from PROOF.md. Let p:U'→U be any nonempty finite étale cover.

There is a finite étale lift T'→T with reduction U'→U, unique up to unique isomorphism over T compatible with that reduction. This follows from invariance of the étale category under nilpotent thickenings; finiteness is preserved in this correspondence. The nilradical of T' is p*N, by flatness. This is the étale lift of the actual thickening, not a fiber product T×_U U': there is no given global morphism T→U.

Primary background checked: Stacks Project, Section59.45, https://stacks.math.columbia.edu/tag/04DY , on invariance under nilpotent closed immersions, and Section58.5, https://stacks.math.columbia.edu/tag/0BL6 , for finite étale covers. The remaining trace and obstruction arguments are given below.

Because p is étale, Omega_U'=p*Omega_U and T_U'=p*T_U. The extension class of T' is p*kappa in H1(U',p*(T_U⊗N)). To verify this without assuming a global retraction, choose the established local algebra splittings on U. On each such open, base-change its split thickening by the restricted finite étale cover. These are the unique étale lifts there. On intersections, their differences are precisely the pulled-back derivations defining kappa. Uniqueness of étale lifting makes these local descriptions identify with T'.

The map

    H1(U,T_U⊗N) → H1(U',p*(T_U⊗N))

is injective. Indeed p has positive constant degree n since U is connected. For any vector bundle F on U, the unit O_U→p_*O_U splits by the normalized trace tr/n. Therefore F is a direct summand of F⊗p_*O_U. The projection formula identifies the latter with p_*p*F. Since p is finite, it is affine and has no higher direct images on quasi-coherent sheaves, so its degree-one cohomology is H1(U',p*F). The induced splitting proves injectivity. This argument applies to disconnected finite covers as well.

As kappa is nonzero, p*kappa is nonzero. Thus T' has no global regular retraction onto U' and is not globally isomorphic to a split square-zero thickening, even allowing a change of coordinates on the reduction. If an isomorphism induces a reduction automorphism, compose with its inverse to get a retraction, which is impossible.

Consequently adjoining finite étale covers, including finite étale roots of the torus coordinates, cannot repair the global nonsplitting. This does not conflict with the existing Zariski-local splittings: a collection of open immersions is not a single finite étale cover. No statement is made for ramified covers, arbitrary alterations or infinite covers. In particular, normalized trace alone does not justify such an extension, since étaleness was also used to identify tangent bundles and the pulled-back obstruction space.

This is a structural persistence theorem for the actual nilpotent thickening. It does not evaluate any source operation, matrix, input, jet, residue or detector, and has no implication that the separate higher mixed module obstruction vanishes or is nonzero.
