# Independent review: primary conductor and cohomology

Verdict: PASS, independently mathematically reviewed; not formally checked.

Reviewed proof SHA-256: `10168b7272d7efa17694c1600f6c007d47a2f1f45289ef601f7d23d2e2a40951`.

## Dependencies and source checks

The review uses global scheme equality D=S from PR573 at commit 6c2dbd48edea0577acf063a60e1edbbbe92ced5c, and the exact normalization dictionary from PR570 at commit e5e55594ef2b99cefb81c4c02b22cb45e1ff0025. It does not replace those dependencies by equality of supports.

Independently checked BHM Section4.3, printed page58: the source explicitly states e(X)=60, χ(O_X)=5, K_X=3F, p_g(X)=4 and q(X)=0. Section4.5 Proposition9, printed pages63–64, identifies H=I+2F, H²=15 and the sixty points paired to thirty image points. Proposition10 explicitly states that the two smooth branches at each image point are transverse, and displays complementary tangent planes. These are source statements, not newly evaluated source-instance data.

Public source: https://mathweb.tifr.res.in/Documents/Publications/Studies/Vector-Bundles-On-Algebraic-Varieties.pdf

## Local algebra audit

For A=B1×_C B2, the difference of residues B1⊕B2→C is surjective with kernel A. Hence the normalization quotient has length one at each double point. Multiplication on this quotient factors through the common residue A→C; its annihilator is exactly the maximal ideal. Extension of this conductor to the normalization is the direct sum of the two branch maximal ideals. Completion is faithfully flat, and the finite normalization of the complex algebraic surface is compatible with this calculation. Thus the global conductor is reduced at the thirty points, and its upstairs ideal is the reduced ideal of sixty points, not a divisor or an invertible ideal.

## Global numerical and negative-twist audit

The constant-function map H⁰(O_S)→H⁰(O_X) is an isomorphism. The exact normalization sequence therefore gives h¹(O_S)=30 and h²(O_S)=4, so χ(O_S)=−25 and arithmetic genus −26. Twisting preserves quotient length thirty. Smooth-surface Riemann–Roch with H²=H.K_X=15 gives χ(O_S(n))=15n(n−1)/2−25 for every integer n.

The revised proof correctly uses the pulled-back hyperplane subsystem rather than assuming it is the complete linear system. A general member avoids the thirty singular points and is smooth by Bertini. Connectedness follows from H¹(O_X(−H))=0 and the divisor sequence. Adjunction on smooth X then gives sectional genus16; the Hilbert-polynomial difference independently gives 15n−15.

The extra negative-twist result is valid. H is ample because ν is finite. For n<0, ampleness gives H⁰(O_X(nH))=0; smooth Serre duality and Kodaira vanishing give H¹(O_X(nH))=0. The normalization sequence then identifies H¹(O_S(n)) with the thirty-dimensional quotient-section space. Combining with n=0 gives h¹(O_S(n))=30 for all n≤0. The same argument and Riemann–Roch give the stated h² for n<0. Vanishing of both H¹ and H² of O_P4(n) gives h²(I_S(n))=30 for all n≤0. This is an actual persistent deficiency, not merely a computation at n=0.

The additional n=1 calculation also passes. BHM page63 explicitly identifies the complete space H⁰(X,H) with V*, of dimension five. All five coordinate sections descend to S, so their map to T(1) is zero. The fiber F is nef and (K_X−H).F=−5, excluding a section of K_X−H. Smooth duality and Riemann–Roch therefore give H²(X,H)=H¹(X,H)=0, and the normalization exact sequence yields (h⁰,h¹,h²)(O_S(1))=(5,30,0). This does not extrapolate the negative-twist calculation to unproved higher positive twists.

## Dualizing-object audit

The normalization pushforward is locally the direct sum of two smooth codimension-two branch modules at a double point, and a smooth codimension-two module elsewhere. Its ambient sheaf Ext is concentrated in degree2. Finite duality identifies that Ext with ν_*ω_X. The thirty-point quotient has ambient sheaf Ext concentrated in degree4. The long exact Ext sequence consequently gives Ext²(O_S,ω_P4)=ν_*ω_X and Ext³(O_S,ω_P4)=Ext⁴(T,ω_P4), with all other degrees zero. In particular the shift in the proof is correct: the ambient dualizing complex shifted by [4] has cohomology in degrees −2 and −1, not −2 and 0.

At a double point the canonical module has two independent generators modulo the maximal ideal, so it is not invertible. Its cohomology dimensions (4,0,1) follow from finite pushforward and smooth-X Serre duality. The additional length-thirty dualizing-complex term is essential; canonical-sheaf duality alone cannot recover h¹(O_S)=30. No splitting of the dualizing complex, Cartier canonical divisor, or Cohen–Macaulay property of S is asserted or needed.

## Boundary

No unresolved mathematical defect was found in the reviewed revision. This is a structural proof using exact sequences, source invariants, smooth-surface vanishing and local regular-branch Koszul resolutions. No selected actual HM/source coefficients, matrices, ranks or parameter instances were evaluated. No formal proof-assistant verification is claimed. The result neither decides the separate actual connecting map δ nor supplies a higher-order lift or algebraicity certificate.
