# Stability of every smooth quintic HM restriction

## Statement

For every smooth quintic X⊂P⁴_C, the restriction E=F|X of the normalized Horrocks–Mumford rank-two bundle is slope-stable for H=O_X(1). No genericity, orbit transversality, or vertex-surjectivity hypothesis is needed for this assertion.

## Inputs and primary provenance

1. c1(F)=−H, hence c1(E)=−H.
2. H⁰(P⁴,F(s))=0 for s<3, and H¹(P⁴,F(s))=0 for s<0. These are imported from historical-source:sharper-hm-regularity/SHARPEST-BOUND.md, Section 1, and its primary Decker section-module/H¹-module resolution. The source is Wolfram Decker, *Monads and cohomology modules of rank 2 vector bundles*, Compositio Math. 76 (1990), pp. 7–17, especially pp. 14–16: https://www.numdam.org/article/CM_1990__76_1-2_7_0.pdf. No new matrix computation is required.
3. Pic(X)=Z·O_X(1), by SGA 2, Exposé XII, Corollary 3.7: the Picard group of a projective complete intersection of dimension at least three is generated freely by the hyperplane line bundle. Primary text: https://grothendiecksga.com/read/sga2/en/XII-3.html (Corollary 3.7); original/revised volume: https://arxiv.org/abs/math/0511279.

## Proof

For any integer a≥0, the restriction sequence is

0→F(−a−5)→F(−a)→i_*E(−a)→0.

The two outside groups in H⁰(F(−a))→H⁰(E(−a))→H¹(F(−a−5)) vanish by input 2. Thus H⁰(X,E(−a))=0 for every a≥0.

Suppose G⊂E is a rank-one torsion-free coherent subsheaf with slope at least that of E. Since X is smooth, hence normal and locally factorial, the rank-one reflexive hull G** is a line bundle. Input 3 writes it as O_X(a). The first Chern class and slope of G are those of G**, because G**/G is supported in codimension at least two. As H³=5,

μ_H(G)=5a, while μ_H(E)=−5/2.

The destabilizing inequality forces a≥0. On the complement of a codimension-at-least-two subset, G is equal to its double dual, and the inclusion gives a nonzero map O_X(a)→E there. Since Hom(O_X(a),E)=E(−a) is locally free and hence reflexive on normal X, its sections extend uniquely across codimension-at-least-two subsets. Therefore the map extends to a nonzero global map O_X(a)→E. This contradicts H⁰(E(−a))=0.

Every proper positive-rank subsheaf relevant to stability has rank one because E has rank two. The contradiction proves slope stability. Saturation is optional: the reflexive-hull argument checks arbitrary rank-one torsion-free subsheaves directly and does not incorrectly assume that every rank-one torsion-free sheaf itself is a line bundle.

## Scope

This supplies stability for all smooth restrictions from already verified cohomology and Lefschetz. It is logically independent of the étale-chart proof in PROOF.md, which only needs simplicity and an explicit determinant isomorphism. We do not use this lemma to assert a global coarse moduli identification, universal bundle, or a stronger decorated orbit equivalence.
