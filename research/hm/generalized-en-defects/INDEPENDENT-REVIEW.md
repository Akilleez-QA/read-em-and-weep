# Independent review: generalized Eagon–Northcott reciprocal defects

Verdict: conditional PASS, subject to the mathematical inputs pinned in PROOF.md. This is a mathematical audit, not formal proof-assistant verification.

Reviewed proof SHA256: 1227efce7a4ddde19a39515f19a780c32474912c9e1588f7500df2040904fbc8.

## Independent checks

1. The normalization has length nine. For i<=a, the terms are Lambda^i F tensor Sym^(a-i)G; for i>=a+1 they are Lambda^(i+1)F tensor D_(i-a-1)(G*) tensor det(G*). Exterior complement identifies the dual of term 9-j with term j of the complementary complex indexed by 8-a, tensored by det(F)* tensor det(G). Both inequalities and the boundary indices agree.

2. The correspondence respects differentials: contraction and multiplication are transposes under divided-power/symmetric duality. The exterior-complement pairing sends the joining contraction by Lambda^2(phi) to the complementary joining contraction, up to removable homological signs. This is stronger than a matching of term ranks.

3. Localization outside the maximal ideal makes phi a split surjection. The resulting generalized complexes are split exact. One can see this by decomposing F=ker(phi) direct sum G: the symmetric Koszul strands and dual divided-power strands are exact except at their joining summands, and the maximal-minor joining map identifies those summands. Thus every homology module has finite length; generic grade-nine exactness is not being assumed.

4. For a homological free complex, the relevant hyper-Ext total degree is p+q. Since finite-length Ext occurs only at p=5, the dual cohomology at n=5+i is Ext^5(H_i,S). Combining n=5+i with reversed length nine gives complementary homology degree 4-i. This independently checks the homological shift and the vanishing above degree four.

5. The graded orientation calculation is consistent: det(F)* tensor det(G)=S(20) tensor det(U)* tensor det(W), whereas Ext^5(M,S)=M^vee(5) tensor det(T)*. Dualizing their equality yields shift -15 and exactly det(U) tensor det(W)* tensor det(T)*. No middle-pairing symmetry or equivariant trivialization is inferred.

6. At a=8 the last map is the maximal-minor splice. Its transpose has cokernel Q tensor det(F)* tensor det(G), not S tensor that line. Consequently the complementary zeroth-homology endpoint is Q rather than Sym^0(H). For a<=7 the last dual map is instead the symmetric-power presentation of Sym^(8-a)(H).

7. The pinned identities Sym^2(H)=R^vee(-5) and H^vee=H(5) give top defects R(-10) and H(-10) at a=6 and a=7. The ranks, generator degrees, annihilators, Hilbert functions, and socle degrees stated for these two defects agree with the pinned resolutions. For a=8, reversing Q's Hilbert function gives (3,35,35,15,5,1) in degrees 10 through 15. Duality of socles and generators gives three degree-10 generators and twenty degree-11 generators, with one-dimensional degree-15 socle.

## Clarification and boundaries

The only requested edit was dependency attribution: PR491 supplies the compatible total-degree-five pairing used for H's self-duality, while PR499 supplies its pure resolution. No substantive mathematical correction was required.

The reciprocity and endpoint identifications do not determine the remaining degree-six connecting-map parameter, individual middle-defect Hilbert functions, or the symmetry type of a self-pairing. They concern auxiliary graded modules, not fixed-source vanishing, higher-order lifting, or algebraicity. No selected HM/source coefficients, numerical matrix ranks, or large computation were used.

Primary construction checked against Andrew R. Kustin, “Canonical complexes associated to a matrix,” Section 3, especially Definition 3.1: https://arxiv.org/abs/1509.04367 . The proof explicitly converts the exterior-complement conventions and records its own normalization.
