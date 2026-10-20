Historical mathematical review of the source manuscript. Its PASS verdict applies to that source proof under the stated hypotheses; it is not a new review of different proof bytes or a formal verification certificate.

# Independent source audit: fiber localization

Verdict: PASS, conditional on the stated identification F = N tensor f*HM and its natural deck/permutation action.

## Public mathematical sources

The localization statement is https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6260145920. Its geometric and equivariance premises are retained.

Primary paper: Ada Boralevi, The Horrocks–Mumford bundle restricted to planes, arXiv:math/0602002v2 (6 June 2006), https://arxiv.org/pdf/math/0602002. Corollary 2.2 (printed p.5) lists six resolution types, exactly two unstable. Theorem 3.1 (pp.6–7) identifies the full jumping locus with the smooth degree-25 surface S25, birational to Shioda's modular surface. The introduction (p.3) explicitly places the additional 25 planes in stable strata. Thus they are not additional unstable components. The paper is being used for these geometric classification facts only.

## Checks

1. Plane family: multiplication by a nonzero quadratic h embeds Sym²V in Sym⁴V even for a double root. The gcd recovers h, so phi:P²→Gr(3,5) is injective. Its pulled-back tautological rank-three bundle is O(−1) tensor Sym²V, hence Plücker pullback O(3). In characteristic zero its generic degree is one; therefore the irreducible image has degree 9. Containment in the irreducible surface S25 would force equality, contradicting degree 25. The degree-eight map from the two remaining elliptic factors onto the parameter P² is surjective, so the good locus in B is nonempty and dense. Nothing here proves the exceptional locus empty or zero-dimensional.

2. Exact finite pushforward: each elliptic double cover has O⊕O(−2). The symmetric quotient sigma has sigma_*O=O⊕O(−1); projection formula handles O(−2,−2). The universal divisor of bidegree (2,1) gives the exact kernel O(−1)^3→O for the mixed term, precisely Ω¹. Consequently p_*O=O⊕O(−1)⊕2Ω¹⊕O(−2)⊕O(−3), of rank eight. The splitting is an actual bundle splitting, not merely a K-theory identity.

3. Simplicity: stability annihilates Hom(E,E(−j)) for j>0, and Ω¹→O(−1)^3 annihilates the mixed terms. Only the scalar endomorphism remains. Finite pullback stability itself is not needed or asserted.

4. Relative cohomology: on the good locus G=End₀(F) has H⁰=H²=0 fiberwise, the latter by Serre duality on an abelian surface. Coherent cohomology and base change for the proper smooth projection with a vector bundle coefficient gives R⁰=R²=0 and R¹ locally free. (This is coherent base change, rather than the similarly named étale theorem.) Its rank is 120. Independently of line-twist normalization, integral c₂(End F_b)=8(4·4−(−1)²)=120 and the surface Todd class is one; thus chi(G_b)=−120. The stated c₁=0,c₂=30 gives the same answer.

5. Leray has only its q=1 row, giving H²(r⁻¹U,G)=H¹(U,R¹r_*G) for any open U in the good base. For affine U the latter vanishes. This establishes restriction vanishing, without requiring U to preserve the group action. H²(C⁴,O) has only characters with two odd deck factors, so the full four-fold deck-sign sector is tracefree.

6. Numerical symmetry check: chi(End E(t))=2t²+6t−11. Stability and Serre duality give h¹ at 0,−1,−2,−3 equal to 12,15,15,12. Euler gives chi(End E tensor Ω¹)=−34. Both H⁰ and H² vanish: for H² use T(−3)=Ω¹ and the same H⁰ argument. Thus its h¹ is 34. Subtracting the scalar contribution removes one dimension from each mixed deck sector (h¹ Ω¹=1) and none from the other two. The four ranks are therefore 27,33,33,27, summing to 120.

7. Swap check: the natural swap linearization on O(−2,−2), inherited from exchanging the two cover generators, is even on their product. Projection formula therefore labels O(−2) even and O(−3) odd, giving both-odd ranks 15 and 12. No Koszul sign belongs in this pushforward of functions. The ordinary permutation sign on the inner transposition selects the odd summand W. Leray is equivariant, so restriction of the retained sector lands in H¹(B°,W), with the remaining base symmetries and pair-exchange compatibility still imposed.

## Boundaries

The rank 12 is a vector-bundle rank, not dim H¹(B°,W), a count of surviving source values, or a 30→12 elimination. Neither affine-local vanishing nor generic simplicity proves good-locus global vanishing or removes exceptional-support classes. None proves module quantization or resolves scalar module obstructions. The comment states these limitations correctly. The audit verifies the abstract geometric implication under the standing identification; it does not independently establish that identification or determine any specified source value.
