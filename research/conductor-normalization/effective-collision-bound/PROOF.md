# Publication scope

This is a preserved theorem manuscript, with the exact hypotheses and held identifications listed in unit 05 INPUTS.md. Abstract geometry and formal conditional implications are distinct from identification with the actual HM module or retained source. Historical words such as “new,” “remaining,” or “previously verified” describe the source manuscript, not a claim about the current research frontier.

# An explicit sufficient collision order: k ≥ 13

## Result

Let F be the normalized Horrocks–Mumford bundle on Y=P⁴ over C, and B0=End₀(F). Then B0 is 11-regular in the Castelnuovo–Mumford sense. In particular

    H¹(Y,B0(t))=H²(Y,B0(t))=0 for every integer t≥10.

Thus one can take T=10 in ../sixth-ideal-pushforward/ALL-POWERS.md, giving k≥14 directly from its common-threshold formula. Keeping the separate H¹/H² thresholds and the stronger adjacent-syzygy degree bound improves the sufficient order: under that theorem's hypotheses, for every k≥13,

    H²(Y,(q_*(I_D^k EA))_sign)
      =H²(Y,B0(-4)K_(k-3))=0.

Consequently every closed sign representative with ordinary triple-diagonal ideal membership I_D^k, k≥13, has zero ambient first-ten class. This is a sufficient, deliberately conservative bound, not a minimum. No assertion is made that the physical source has this ideal order, and collision order is not deformation order.

## 1. Verified primary input and normalization

Ada Boralevi, *The Horrocks–Mumford bundle restricted to planes*, Collectanea Mathematica 58 (2007), 101–117, arXiv version 2 (6 June 2006), gives the monad in equation (1.1), PDF page 1:

    A=5O(-1) → M=2Ω²(2) → C=5O.

The middle cohomology is F. The notation paragraph on PDF page 3 expressly identifies this F as normalized, with c₁(F)=-1 and c₂(F)=4. Both pages were checked in the primary PDF:

https://arxiv.org/pdf/math/0602002

Monad means the first arrow is a subbundle injection, the second arrow is a bundle surjection, their composite is zero, and their middle cohomology is the locally free F. Therefore, with K=ker(M→C), there are exact bundle sequences

    0→K→M→C→0,       0→A→K→F→0.

The bundle ranks are 7,12,5 in the first sequence and 5,7,2 in the second. These are formal ranks of the displayed bundles, not evaluations of a selected matrix map.

The determinant is checked directly. Since Ω¹ has rank four and determinant O(-5), c₁(Λ²Ω¹)=3c₁(Ω¹)=-15H. Hence c₁(Ω²(2))=-3H, det M=O(-6), and det K=O(-6). It follows that det F=O(-6)⊗O(5)=O(-1), consistent with the source normalization. For rank two this gives F∨≅F(1).

## 2. Regularity conventions and permitted bounds

A bundle G is m-regular if Hⁱ(G(m-i))=0 for i=1,...,4. The following standard projective-space facts are used:

- m-regularity implies (m+s)-regularity for every s≥0.
- If E is a-regular and G is b-regular, and at least one is locally free, E⊗G is (a+b)-regular.
- In characteristic zero, ΛʳE is a direct summand of E^{⊗r}; thus a 0-regular bundle has 0-regular exterior powers.
- For an exact resolution ...→E₂→E₁→E₀→G→0, if Eⱼ is (m+j)-regular, then G is m-regular.

A verified reference for the first three is Robert Lazarsfeld, *Positivity in Algebraic Geometry I*, Theorem 1.8.3, Proposition 1.8.9 and Corollary 1.8.10. The resolution criterion is Example 1.8.7. The author-hosted chapter and the publisher reading sample include this section:

https://www.math.stonybrook.edu/~roblaz/Reprints/Laz.PAG.Chapt1.pdf

https://beckassets.blob.core.windows.net/product/readingsample/389723/9783540225331_excerpt_001.pdf

The resolution criterion also follows directly by splitting the resolution into kernel sequences: for i>0, the group Hⁱ(G(m-i)) maps successively to H^(i+1) of the first kernel, H^(i+2) of the second, and so on; the needed Eⱼ groups vanish because (m-i)=(m+j)-(i+j). The chain terminates above degree four. No H⁰-surjectivity premise is being silently imposed.

Important distinction: a bound for reg(ker(M→C)) cannot in general be inferred just from the regularities of M and C. We instead dualize and use the determinant identity in Section 4.

## 3. The dual middle term is 0-regular

The rank-four exterior duality identity gives

    (Ω²(2))∨≅Ω²(3),        M∨≅2Ω²(3).

The sheafified homogeneous-coordinate Koszul complex on P⁴ gives the exact linear resolution

    0→O(-2)→5O(-1)→10O→Ω²(3)→0.

Consequently Ω²(3), and hence M∨, is 0-regular by the resolution criterion and reg O(-j)=j. There is no use of the HM negative-twist Ext table.

For completeness, tensoring copies of this locally free linear resolution remains exact as a total complex and gives a linear resolution of each tensor power of M∨. Thus those tensor powers are 0-regular directly; the characteristic-zero antisymmetrizing idempotent then gives 0-regularity of every ΛʳM∨. This independently checks the particular use of the general tensor-regularity theorem in this step.

## 4. Dualize the kernel sequence before bounding regularity

Dualize the first monad sequence:

    0→C∨=5O→M∨→K∨→0.

This time K∨ is a cokernel, not a kernel. Directly, for i=1,...,4,

    Hⁱ(M∨(-i)) → Hⁱ(K∨(-i)) → H^(i+1)(5O(-i)).

The left group vanishes because M∨ is 0-regular. The right group is zero: for i=1,2 it is intermediate line-bundle cohomology; for i=3 it is H⁴(5O(-3))=0; for i=4 it is H⁵=0. Thus K∨ is 0-regular.

Tensor-regularity subadditivity now makes (K∨)^{⊗6} 0-regular. Because we are over C, Λ⁶K∨ is its antisymmetric direct summand and is likewise 0-regular. Rank K=7 and det K=O(-6) give

    Λ⁶K∨≅K⊗det K∨=K(6).

Hence K is 6-regular. This argument needs neither a genericity assertion nor a Buchsbaum–Rim theorem, and it avoids the invalid inference from the original kernel sequence's terms alone.

## 5. From K to F and tracefree endomorphisms

Twist 0→A→K→F→0 by 6-i. For i=1,...,4 the controlling part of its cohomology sequence is

    Hⁱ(K(6-i)) → Hⁱ(F(6-i)) → H^(i+1)(A(6-i)).

The left group is zero by Section 4. For i=1,2 the right group is intermediate cohomology of line bundles, hence zero; for i=3 it is H⁴(5O(2))=0; for i=4 it is H⁵=0. Therefore F is 6-regular.

Since F∨≅F(1), the dual is 5-regular. Tensor-regularity subadditivity on projective space now implies

    End(F)=F⊗F∨ is 11-regular.

The trace decomposition in characteristic zero is End(F)=O⊕B0, with the scalar summand split by one half of the trace. Hence B0 itself is 11-regular. Persistence of regularity gives the precise consequences

    H¹(B0(t))=0 for t≥10,
    H²(B0(t))=0 for t≥9.

A common sufficient threshold is T=10. These are independently obtained positive-twist vanishings, not conclusions inferred from negative H¹ data or a Riemann–Roch sign.

## 6. Apply the audited all-power theorem

For n=k-3≥1, that theorem provides an exact resolution

    0→⊕O(-eᵢ)→⊕O(-dᵢ)→K_n→0,

with every dᵢ≥n. In the audited ordering aᵢ>a_(i+1) and bᵢ<b_(i+1), the adjacent-syzygy degree satisfies

    eᵢ=2aᵢ+3b_(i+1)=dᵢ+3(b_(i+1)-bᵢ)≥n+3.

This uses only distinct integer exponents of adjacent minimal monomial generators. Tensor the resolution by B0(-4). Trace self-duality and Serre duality on P⁴ identify the two relevant outer groups as

    H²(B0(-4-dᵢ))∨=H²(B0(dᵢ-1)),
    H³(B0(-4-eᵢ))∨=H¹(B0(eᵢ-1)).

For k≥13 we have n≥10, so dᵢ-1≥9 and eᵢ-1≥n+2≥12. The first outer group vanishes by the H² threshold 9, and the second by the H¹ threshold 10. The long exact sequence therefore gives H²(B0(-4)K_n)=0. The sign-pushforward identification in ALL-POWERS.md then proves the stated result.

The bound does not decide the fourth-/fifth-power secondary Koszul map discussed in ../fourth-power-cohomology/PROOF.md, or any intermediate order. In particular it is compatible with h¹(B0(4))≥85. It evaluates neither that map nor any physical source.

## Scope

This proof uses formal bundle identities, exact complexes, regularity and duality. No selected polynomial instance, matrix rank, source representative, obstruction coordinate, or jet is evaluated.  Independent review is recorded in AUDIT.md.
