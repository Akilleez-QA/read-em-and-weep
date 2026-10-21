# Independent review: universal Picard defect and Postnikov annihilator

Verdict: PASS. Independently mathematically reviewed; not formally checked. No selected actual HM/source-instance evaluation, numerical experiment, or large computation was performed.

## Reviewed artifact and dependency

This review covers `PROOF.md` with SHA-256 `ab1914607dc58121c5416e4c9aead3a2a30cdf01f011983ecb2c94a82b1c9abc`.

The geometric input remains conditional on PR583, commit `ce046d10a03a609aee3d0125b3264dd36bb9d598`, `research/hm/universal-picard/PROOF.md`, and its pinned dependencies. The reviewer checked its displayed residue matrix, relative complex, and nonflat-cohomology specialization statements against the local argument here. This review does not independently reprove the underlying geometry.

## Independent algebra checks

1. Subtracting the first output coordinate gives the block matrix with a unit entry and the column minus delta. The source change alpha'=alpha−t1 beta is invertible. Each successive equation tj=t1 leaves a Laurent polynomial domain. Thus the four entries form a regular sequence and I is prime of codimension four. The presentation is injective on its left, has generic rank three, and gives Fitt_3(K)=I, Fitt_4(K)=A, and Fitt_2(K)=0. At a prime containing I, reduction modulo the maximal ideal gives four minimal generators, excluding freeness of this rank-three module. Projective dimension is consequently one there and zero elsewhere.

2. Dualizing the length-one free resolution gives Ext^1_A(K,A)=A/I and vanishing in degrees at least two. The Koszul resolution displayed for K* has the correct exterior-power ranks 1, 4, and 6. Grade four gives Hom_A(A/I,A)=Ext^1_A(A/I,A)=Ext^2_A(A/I,A)=0, so I*=A and Ext^1_A(I,A)=0. Dualizing the kernel presentation therefore recovers precisely the original column presentation of K. The compatible evaluation diagram identifies the resulting isomorphism with K→K**. Reflexivity follows. As a separate local-depth check, at any prime containing I the regular local ring A_p has dimension at least four and the module has depth dim(A_p)−1 by Auslander–Buchsbaum. Thus no depth-two defect is hidden on the nonfree locus. The double-dual argument already supplies torsion-freeness.

3. The ring convention is explicit: T=R tensor_C A for the fixed completed node R, rather than an unstated parameter-adic completion. The residue sequence remains exact under this flat scalar extension. After the target operation, the first component B→A is surjective with kernel E. The subcomplex [E→A^4] has quotient [A→A] with identity differential, so its inclusion is a quasi-isomorphism inducing the inherited maps on both cohomology modules. The remaining differential is minus delta times the second-branch residue. Its two-extension is therefore the actual Postnikov class of the supplied relative residue complex, not merely another class in the same Ext group.

4. Multiplication of the first branch by t1 identifies T with E as a T-module. It does not identify the inherited conductor inclusion with the unscaled standard inclusion. The proof explicitly retains that distinction. A stronger coordinate check uses the normalization residue boundary: E is the pullback of B→A^2 along beta↦(t1 beta,beta), hence its extension class in the boundary basis is exactly (t1,1). This validates the twist without any choice of an unspecified primitive generator.

5. Independently applying Hom to the nodal resolution with d1=(s,t), d2=diag(t,s), d3=diag(s,t) yields Ext^1_R(C,R/(t))=C: its degree-one kernel is the first branch module and its boundaries are its s-multiples. The other branch gives another C. Since m is the direct sum of the two branch modules, Ext^1_R(C,m)=C^2. The absence of residue-field submodules of the normalization makes the residue boundary C^2→Ext^1_R(C,m) injective, hence bijective. Finite rank in each degree of the resolution and flatness over C justify Ext^1_T(A,m_A)=A^2, including the boundary basis after base extension.

6. The long exact Ext sequence is applicable to the short exact presentation even though its terms are not T-projective. Additivity identifies the preceding map as multiplication by the four entries of minus delta, with image I E1. Exactness consequently gives an injection E1/I E1→Ext^2_T(K,m_A), not just a quotient or a spectral-sequence candidate. The connecting homomorphism is the Yoneda splice already obtained in item 3. Its representative (t1 mod I,1) has annihilator precisely I. Therefore A kappa is isomorphic to A/I and remains nonzero at every parameter localization containing I. No assertion about the rest of Ext^2 is needed.

7. The annihilator of the direct sum of the six nodewise classes is the intersection of their annihilators. An intersection of these prime ideals is radical, so the asserted reduced union is justified. The statement deliberately concerns the nodewise direct sum and does not assume an unproved global Ext decomposition.

## Scope and specialization

The exact annihilator is an A-module statement about the universal Postnikov class. It is not a claim that the ordinary closed-fiber Postnikov class is nonzero. On the uniform locus K is not A-flat, and its Tor^1 changes degree-zero cohomology upon derived specialization. Thus the fiber splitting results and the universal obstruction coexist without contradiction. The proof states this caveat explicitly, including the warning against identifying restriction of the universal kernel with the fiber kernel.

No full HM repair, adjoint delta20 conclusion, higher-order lifting claim, new algebraicity claim, or multiplicative formality claim follows from this result. Within the stated module-theoretic and relative-derived scope, no correction is required.
