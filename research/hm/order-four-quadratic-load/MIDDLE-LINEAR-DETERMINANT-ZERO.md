# Checked HM hyperplane multiplication obstruction

Checked 2026-10-21. No selected HM coefficients, matrices, rank evaluations, or numerical examples were constructed or evaluated.

## Exact primary theorem

Constantin Bănică and Nicolae Manolache, *Remarks on rank 2 stable vector bundles on P³ with Chern classes c1=-1,c2=4*, INCREST preprint 104/1981, November 1981, §1, Lemma 1, printed pp.3–4 (PDF pp.7–8): every stable rank-two vector bundle G on P³ with these Chern classes satisfies H⁰(G(2))≠0.

Primary scan: https://imar.ro/~increst/1981/104_1981.pdf

The statement and complete proof were visually checked against the scan. Its prerequisites and argument are: the only possible spectra are (-2,-1,0,1) and (-1,-1,0,0), both giving H²(G(k))=0 for k≥0. Stability gives H³(G)=0. If H⁰(G(2)) vanished, χ(G(2))=0 would imply H¹(G(2))=0. Consequently G is 3-regular and G(3) globally generated. A general section gives a smooth degree-10 genus-6 curve Y with ωY=OY(1), and exact sequence 0→O→G(3)→IY(5)→0. The authors invoke Gruson–Peskine to place Y on a quartic. Twisting the sequence down gives H⁰(G(2))=H⁰(IY(4))≠0, contradiction.

The cited curve theorem is reference [5]: L. Gruson and C. Peskine, *Genre des courbes de l’espace projectif*, Algebraic Geometry, Tromsø 1977, Lecture Notes in Mathematics 687 (1978), pp.31–59. Publisher-verified chapter DOI: https://doi.org/10.1007/BFb0062927. The preprint supplies no internal page or theorem number for [5], and the publisher exposes only subscription metadata/preview; no exact internal locator has been verified. That underlying paper has not been independently checked here; the Bănică–Manolache proof and its citation were checked.

## Application to the specific normalized HM bundle

Let E denote the HM bundle with c1(E)=5, c2(E)=10, and F=E(-3), so c1(F)=-1 and c2(F)=4. Write G=F|H for a hyperplane H⊂P⁴.

Ada Boralevi, *The Horrocks–Mumford bundle restricted to planes*, arXiv:math/0602002v2 (6 June 2006), notation on printed p.3 and §3 opening on printed p.6, explicitly uses this normalized F and states that its restriction to EVERY hyperplane P³⊂P⁴ is stable, citing [4], [7], [13].

Source: https://arxiv.org/pdf/math/0602002

Therefore the hypotheses of Bănică–Manolache Lemma 1 hold for each G=F|H, and H⁰(F|H(2))≠0 for every hyperplane H.

## Formal deduction for universal multiplication

For each nonzero linear form ℓ defining H, tensor the hyperplane sequence by F(2):

0 → F(1) --ℓ→ F(2) → F|H(2) → 0.

The established HM vanishings H⁰(F(1))=H⁰(F(2))=0 identify H⁰(F|H(2)) with the kernel of

μℓ : H¹(F(1)) → H¹(F(2)).

Both spaces have dimension 10. Hence every μℓ is singular, with corank at least one. Over the dual projective space P(H⁰(OP⁴(1))), the universal map is

H¹(F(1))⊗O(-1) → H¹(F(2))⊗O.

Its determinant is a section of O(10) (up to a fixed one-dimensional determinant factor). It vanishes at every complex point, hence is identically zero. There is no nonempty locus where this particular multiplication map is an isomorphism.

## Limits

The theorem gives corank ≥1, not an exact generic corank. Spectrum identities control the relevant negative H¹ and higher H² groups, but do not alone determine H¹(G(2)) or H⁰(G(2)); χ(G(2))=0 only equates their dimensions. No stronger generic lower bound is claimed here. The conclusion closes the proposed invertible-linear-primary route, but does not establish or refute generic quadratic multiplication on the Rao module of the 25-line curve, and does not settle residual quadratic coverage or Q4.
