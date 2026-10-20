# Independent audit of the twisted-endomorphism exclusion

## Conclusion and scope

The mathematical audit checked the rank-one argument, the spectral construction, and every determinant-rank branch. The proof establishes

    H⁰(P⁴, End₀(F)(1)) = 0

for the normalized Horrocks–Mumford bundle over C. No gap remains in these structural exclusions. The argument needs only the stated Chern classes and the section vanishing verified below, together with standard divisor, depth, and cohomology facts explained in the proof.

Only the H⁰ vanishing is included here. The separate endpoint vanishing and associated h¹ consequence are outside this publication. This is a written mathematical audit, not a machine-checked proof or a novelty assessment.

## 1. The HM section-vanishing input

The source check inspected printed pages 14–16 of Wolfram Decker, *Monads and cohomology modules of rank 2 vector bundles*, Compositio Mathematica 76 (1990), 7–17. The primary source is available at [Numdam](https://www.numdam.org/article/CM_1990__76_1-2_7_0.pdf).

Page 14 defines the free resolution of the section module; page 15 relates its terms to the first-cohomology resolution; page 16 gives the explicit shifts and directly displays the section-module presentation. They agree with

    0 → 2S(−8) → 20S(−6) → 35S(−5)
      → 15S(−4) ⊕ 4S(−3) → H⁰F(*) → 0.

In particular, the rightmost free module has no component in degrees below 3. Its graded surjection proves H⁰(F(u))=0 for every u<3. This conclusion uses the graded section-module presentation, so it involves no unjustified assumption that a sheaf surjection is surjective on global sections. The input and its normalization are consistent with the main proof.

## 2. Correction of the initial RR false lead

The initial proposed calculation used t²+2t−2. That constant is incorrect. For a rank-two bundle E on P² with c₁(E)=−H and c₂(E)=4H²,

    ch(E)=2−H−(7/2)H²,
    td(P²)=1+(3/2)H+H²,
    χ(E(t))=t²+2t−3.

Consequently, on a smooth quadric surface S=P¹×P¹, comparison with

    χ(O_S(a+t,b+t))=(t+a+1)(t+b+1)

gives a+b=0 and ab=−4. It permits precisely (a,b)=(2,−2) and (−2,2). It does not itself exclude determinant rank at least three. The final proof has correctly removed that false contradiction and supplies separate arguments for rank three and ranks four/five.

## 3. Generic-rank-one homomorphisms and square determinants

The claim that a saturated rank-one subsheaf K of a vector bundle is a line bundle here is justified and is not circular. Its quotient is torsion-free. At every local ring of dimension at least two, the depth lemma gives depth(K) at least two. Together with torsion-freeness this is the reflexivity criterion on a smooth variety. Rank-one reflexive sheaves on P⁴ are line bundles.

For a generic-rank-one map ψ:F→F(1), its kernel is saturated because its quotient is the image inside a vector bundle. The saturation of that image is also a line bundle. Writing these as O(a) and O(b), respectively, the verified section vanishing implies a≤−3 and b≤−2.

The quotient F/O(a) is rank-one torsion-free with double dual O(−1−a), so it is I_Z(−1−a) for a subscheme of codimension at least two. The induced nonzero map to O(b) would belong to H⁰O(a+b+1), which is zero. The identity Hom(I_Z,O)=O is valid on the smooth normal ambient variety: a homomorphism is multiplication by a rational function, regular away from Z, and extension across codimension at least two applies.

Cayley–Hamilton gives φ(1)φ=q·id for trace-free φ. If q=0 and φ is nonzero, φ has generic rank one. If q=ℓ² is nonzero, φ−ℓ·id is nonzero with determinant zero and generic rank one. Its nonzeroness also follows immediately from trace(φ−ℓ·id)=−2ℓ in characteristic zero. Thus determinant ranks zero and one are rigorously excluded.

## 4. Spectral-module construction and the MCM assertion

The most direct construction is the one now recorded in Section 2: first restrict (F,φ) to the selected base Pⁿ, then regard F|Pⁿ as a module for O⊕O(−1), with multiplication specified by φ and z²=q. The corresponding spectral sheaf M satisfies π_*M=F|Pⁿ by construction. This avoids needing a separate theorem about restriction preserving maximal Cohen–Macaulayness.

For determinant rank at least two, the restricted quadratic is nonsquare in the rational function field, and its spectral cover is integral. The rank-two module downstairs is rank one over the quadratic function-field extension upstairs.

The depth argument is valid. At a closed base point, a regular system of n parameters is a regular sequence on the free stalk of F|Pⁿ. Localizing the finite algebra and its module at any point above that base point preserves the regular sequence. Finiteness makes the parameter ideal primary to the upstairs maximal ideal. Thus M has depth n at each closed point. The Cohen–Macaulay property localizes. On the normal covers used here, M is therefore rank-one reflexive, and on their smooth loci it is a line bundle. No cyclicity assumption at a singular point is needed.

## 5. Determinant ranks four and five

A general base P³ makes the restricted quadratic have rank four. The double cover is consequently a smooth quadric threefold Q³. Its rank-one MCM spectral sheaf is locally free.

The elementary Picard-group argument in the main proof is correct. For uv+x²+y²+z²=0, the chart u≠0 is A³, while u=0 is an irreducible hyperplane section. Divisor-class localization shows that the hyperplane class generates; its positive intersection degree shows infinite order. Smoothness identifies the class and Picard groups.

Therefore M=O_Q³(k), and π_*M=O(k)⊕O(k−1). The first Chern class forces k=0, while the second then vanishes, contradicting c₂=4. Both determinant ranks are excluded.

## 6. Determinant rank two

The spectral surface is the normal cone Q={xz−y²=0}⊂P³. For its ruling line L={x=y=0}, the complement is exactly the chart x≠0, hence A². Class-group localization therefore makes Cl(Q) generated by [L]. The main proof's degree argument correctly shows infinite order. An equivalent check is that if nL were principal for n>0, its defining rational function would have no poles on the normal projective integral surface, hence would be constant.

The hyperplane x=0 has Weil divisor 2L. Thus all rank-one reflexive sheaves are O_Q(k) or I_L(k). The ideal I_L is reflexive: away from the vertex L is Cartier, and at the vertex the depth lemma applied to its ideal sequence gives depth two. It represents the class −[L].

The two Euler polynomials are (t+k+1)² and (t+k)(t+k+1). The first has the required linear coefficient only for k=0, when its constant is 1 rather than −3. The second has odd linear coefficient 2k+1, so cannot match 2. This branch is fully excluded without treating every rank-one MCM sheaf as a line bundle.

## 7. Determinant rank three

On a suitable base P³ the cover X is the projective cone over S=P¹×P¹, with one vertex v. A base plane avoiding the kernel point gives a smooth hyperplane S away from v. The corrected RR calculation forces M|S to be O(2,−2) or its transpose.

The geometry and Picard argument are correct: X minus its vertex is the total space of O_S(1,1), with S the zero section. Compactifying to a P¹-bundle and removing its infinity section eliminates a divisor of relative degree one, so pullback identifies Pic(S) with Pic(X minus its vertex). Restriction to the zero section is the inverse. Hence M on the vertex complement is the pullback of M|S.

Choose the complementary affine vertex chart U, the affine cone over S. Its punctured version is the punctured tautological line bundle. The associated affine G_m projection gives

    H¹(U\{v},M)=⊕_{n∈Z}H¹(S,O(a+n,b+n)).

Changing the tautological sign merely reverses the integer index. Cohomology commutes with this direct sum on the projective, hence quasi-compact and separated, surface. For (a,b)=(2,−2), the n=0 summand has dimension 3 by Künneth, and the transposed case gives the same nonvanishing.

Affineness of U identifies this group with H²_{v}(U,M). But depth_v(M)=3 forces that local cohomology group to vanish. This is a genuine contradiction and closes the only branch left open by the corrected surface RR calculation.

## Final assessment

Every possible rank 0 through 5 of the quadratic determinant is now excluded for a nonzero trace-free twisted endomorphism. The conclusion H⁰End₀(F)(1)=0 is valid. The proof uses no evaluation of a particular HM matrix or multiplication-map rank. Its statements about higher twists, socles, secondary maps, and collision bounds remain appropriately limited.
