# Closing the positive-middle-cohomology endpoint by an abelian zero surface

## Result

For the normalized Horrocks–Mumford bundle F on complex projective four-space and B=End₀(F),

    H²(B(t))=0 for every t≥1.

In particular the formerly unresolved H²(B(1)) is zero. Trace self-duality gives also H²(B(t))=0 for every t≤−6. This resolves one live dependency without evaluating an HM matrix, multiplication rank, section instance, or physical source. It does not settle the degree −1 socle or H⁰(B(1)),…,H⁰(B(4)).

## 1. Direct primary input and normalization

G. Horrocks and D. Mumford, *A rank 2 vector bundle on P⁴ with 15,000 symmetries*, Topology 12 (1973), 63–81. Author-hosted primary PDF:

https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

Theorem 5.1, printed p.75 (zero-based PDF page 12), proves that a general section of their bundle has a smooth degree-ten abelian surface as its zero scheme. Printed p.70 (PDF page 7) computes its Chern classes c₁=5 and c₂=10. Their bundle is F(3) in our normalization c₁(F)=−1, c₂(F)=4. The paper's cohomology table on p.74 also has H² concentrated at twist −5 for their bundle, corresponding to twist −2 for F. The theorem and normalization were read directly in the primary PDF text, rather than inferred from a search excerpt.

An independent primary source for the only bundle-cohomology input needed is W. Decker, *Monads and cohomology modules of rank 2 vector bundles*, Compositio Math. 76 (1990), 7–17, printed p.13:

https://www.numdam.org/article/CM_1990__76_1-2_7_0.pdf

It identifies H²F(*) as a two-dimensional space in degree −2. Thus

    H²F(u)=0 whenever u≠−2.

The full H¹ table and section resolution verified in historical-source:sharper-hm-regularity/PROOF.md are NOT required for the vanishing proof below.

## 2. A general normal-bundle lemma

Let A⊂P⁴ be a smooth complex abelian surface, L=O_A(1), and N=N_(A/P⁴). Then

    H¹(A,N⊗L^t)=0 for every integer t≥1.

Indeed L is ample, K_A is trivial, and Kodaira vanishing gives H^i(A,L^u)=0 for i>0,u>0. Restrict and twist the Euler sequence:

    0→L^t→(L^(t+1))^⊕5→T_P⁴|A⊗L^t→0.

Its cohomology segment H¹(5L^(t+1))→H¹(T_P⁴|A(t))→H²(L^t) has zero ends, so the middle group is zero. The tangent bundle of an abelian surface is trivial. The twisted tangent-normal sequence is therefore

    0→(L^t)^⊕2→T_P⁴|A⊗L^t→N⊗L^t→0.

The segment H¹(T_P⁴|A(t))→H¹(N(t))→H²(2L^t) again has zero ends. This proves the lemma. All exact sequences are of locally free sheaves; smoothness is essential here.

## 3. Two exact-sequence chases prove the endpoint

Choose a general section s of F(3) with smooth abelian zero scheme A. This is an existence choice; no section coordinates are chosen or evaluated. Since its zero scheme has the expected codimension two, the section is regular. Its Koszul/Serre sequence is

    0→O(−3)→F→I_A(2)→0.

For a rank-two bundle with determinant O(−1), F∨=F(1). Tensoring this exact sequence by the locally free F∨(t) gives

    0→F(t−2)→End(F)(t)→I_A⊗F(t+3)→0.          (1)

The regular-section conormal isomorphism identifies N=F(3)|A. Hence the restriction sequence is

    0→I_A⊗F(t+3)→F(t+3)→N(t)→0.              (2)

For t≥1, the normal-bundle lemma and the primary H²-support theorem give

    H¹N(t)=0, H²F(t+3)=0, H²F(t−2)=0.

Sequence (2) contains

    H¹N(t)→H²(I_A⊗F(t+3))→H²F(t+3),

so H²(I_A⊗F(t+3))=0. Sequence (1) contains

    H²F(t−2)→H²End(F)(t)→H²(I_A⊗F(t+3)),

so H²End(F)(t)=0. The trace splitting End(F)=O⊕B yields the asserted vanishing for B. This argument needs no incoming-map surjectivity, no H⁰ calculation and no H¹F calculation.

With the additionally verified H¹ table, one can instead write H²End(F)(t)≅H¹N(t) for t≥1: the outer groups H²F(t−2), H³F(t−2), H¹F(t+3), H²F(t+3) vanish. The simpler proof above deliberately avoids these extra inputs.

Finally B∨=B and Serre duality on P⁴ give H²B(t)∨=H²B(−5−t). The positive result therefore also proves vanishing at every t≤−6.

