# Comparison hypotheses for the pinned residual

Scope: the hypotheses still listed in `research/hsd-literature-comparison/SURVEY.md` §9 at `069aea3d6d013b6f1caaa2d94c1517fca7025964`, for the fixed model pinned in `research/hsd/gate-ladder.md` at `d915eeab061f3dddebe1a1d3d7c80ca09609dcee` and the character table in `research/hm/ext-model.md` at `add03476d9055aa00e1e00778eea6332cf8e01cc`. Each mark is **holds**, **fails**, or **still unverified**. No value of \(O_2\) is computed.

The arithmetic is `research/hsd-literature-comparison/character_count.py`. It uses `fractions.Fraction` and decides ranks by Gaussian elimination over \(\mathbf{Q}\). On the pinned input it reports `pinned_holds=1`. Two controls are required to fail the same checker; both fail (`controls_fired=2`).

## 1. Statements read

arXiv:2502.03415v2, PDF page 59. Diagram (8.3.4) is the triangle \(HT^2(M)\xrightarrow{ob_E}\operatorname{Ext}^2(E,E)\) and \(HT^2(M)\xrightarrow{\lfloor ch(E)}\bigoplus_q H^{q+2}(M,\Omega^q)\), with \(\sigma\) down the right side. The page says the diagram commutes by [BF2, Prop. 6.2.1 and Cor. 6.3.2].

Lemma 8.3.4, same page: “If the kernels of \(ob_E\) and \(\lfloor ch(E)\) in \(HT^2(M)\) are equal and \(ob_E\) is surjective, then \(E\) is semiregular.”

Remark 8.3.5, same page: “If we drop the assumption that \(ob_E\) is surjective in Lemma 8.3.4 we still conclude that the semiregularity map restricts to the image of the obstruction map as an injective map.”

The same two statements are Lemma 8.2.4 and Remark 8.2.5 in arXiv:2502.03415v1, as already recorded in the survey. This file uses the v2 text and the v2 page.

Lemma 8.3.3, PDF page 58, is a different sheaf. For the ideal sheaf \(F\) of that section it says the contraction \(H^2(\mathcal{O})\oplus H^1(T)\oplus H^0(\wedge^2 T)\to H^2(\mathcal{O})\oplus H^3(\Omega^1)\) “restricts to the first summand as an isomorphism onto the first summand of the co-domain, as \(ch_0(F)=1\)”. The pinned Chern character is \(\operatorname{ch}(E)=\exp(i\sqrt{15}\,\theta)+\exp(-i\sqrt{15}\,\theta)\), whose degree-zero term is \(2\). Lemma 8.3.3 is not applied to \(E\).

arXiv:1208.3111v4, PDF page 12. Corollary 1.20: if \(\mathcal{N}\) is a geometric noncommutative scheme in the sense of [Orl, Definition 4.3] over a characteristic \(0\) field \(k\), then for a square-zero extension \(e:A\to B\) of commutative \(k\)-algebras with kernel \(I\), and a perfect \(\mathcal{N}\otimes_k B\)-complex \(\mathscr{F}\), the obstruction \(o_e(\mathscr{F})\) lies in the kernel of
\[
\mathcal{L}:\operatorname{Ext}^2_{\mathcal{N}\otimes_k B}(\mathscr{F},\mathscr{F}\otimes^{\mathbf{L}}_B I)\longrightarrow HH^k_{-2}(\mathcal{N})\otimes_k I.
\]
The proof ends: a \(k\)-linear splitting gives \(\mathsf{I}\mathcal{L}(o_e(\mathscr{F}))=0\); then “as in Remark 2.27 the Lefschetz principle makes \(\mathsf{I}\) injective for \(\mathrm{per}_{dg}(\mathcal{O}_Y)\)”, and \(\mathsf{I}\) remains injective on a direct summand, so \(\mathcal{L}(o_e(\mathscr{F}))=0\).

Remark 1.21, same page: “Until the final step, the proof of Corollary 1.20 only requires that \(\mathcal{N}\) be a smooth proper dg subcategory of \(\mathrm{per}_{dg}(\mathcal{O}_Y)\), for \(Y\) quasi-compact and semi-separated. In such cases, we can still say that \(\mathsf{I}\mathcal{L}(o_e(\mathscr{F}))=0\).” The same remark allows \(\mathcal{O}_Y\) to be replaced by a presheaf \(\mathscr{A}\) of simplicial associative \(R\)-algebras on affine opens whose \(\pi_*\mathscr{A}\) admits a quasi-coherent \(\mathcal{O}_Y\)-algebra structure, including the structure hypersheaf of a derived scheme with underived truncation \(Y\).

PDF page 13 opens Section 2 with “From now on, all rings will be commutative.” That sentence is after Remark 1.21.

arXiv:2111.12985v3, PDF page 4. Theorem 2.8 (=Corollary 4.10): let \(I\) be a curved Lie ideal of a curved DG-algebra \((A,d,R)\) and let \(\pi:A\to A/I\). For every \(k\ge 0\) there is a canonical \(L_\infty\) morphism
\[
\sigma^k:A/I\rightsquigarrow A/([A,A]+I^{(k+1)}A)[2k]
\]
whose linear component is \(\sigma^k_1\), for every graded linear section \(s\) of \(\pi\). The theorem does not name \((X,E,\xi)\). The paragraph after Corollary 2.10 on the same page says that if a deformation problem is controlled by \(A/I\), then the induced map on \(H^2(A/I)\) annihilates the obstructions, because the target deformation functor is unobstructed. That control hypothesis is not part of the displayed statement of Theorem 2.8.

## 2. The character count

Pinned input, from gate-ladder §1 at `d915eeab`.

- \(G=(\mathbf{Z}/2)^4\) acts by \(y_i\mapsto -y_i\). Characters are subsets of \(\{1,2,3,4\}\).
- \(V_i\) is dual to \(dx_i/y_i\). The substitution \(y_i\mapsto -y_i\) sends \(dx_i/y_i\) to \(dx_i/(-y_i)=-dx_i/y_i\). The coefficient is \(-1\in\mathbf{Q}\), so \(V_i\) has character \(\{i\}\).
- \(H^1(X,T_X)^G\) is spanned by the four diagonal product-elliptic directions. With \(T_X\) trivial on the product, the Künneth basis of \(H^1(T_X)\) is \(\eta_i\otimes V_a\), where \(\eta_i\in H^1(\mathcal{O}_X)\) is pulled back from the \(i\)-th factor. The diagonal classes are \(\eta_i\otimes V_i\). Invariance of each diagonal, together with the character of \(V_i\), forces \(\eta_i\) to have character \(\{i\}\).
- The HKR decomposition used for the dimension \(28\) in the survey is the basis: six bivectors \(V_i\wedge V_j\) (\(i<j\)), sixteen tensors \(\eta_i\otimes V_a\), and six products \(\eta_i\cup\eta_j\) (\(i<j\)).

Characters of that basis, as representations:

| Summand | Vectors | Character |
|---|---:|---|
| \(H^0(\wedge^2 T)\) | \(V_i\wedge V_j\), \(i<j\) | \(\{i,j\}\), one vector each |
| \(H^1(T)\), diagonal | \(\eta_i\otimes V_i\) | trivial, four vectors |
| \(H^1(T)\), off diagonal | \(\eta_i\otimes V_a\), \(i\neq a\) | \(\{i,a\}\), two vectors on each pair |
| \(H^2(\mathcal{O})\) | \(\eta_i\cup\eta_j\), \(i<j\) | \(\{i,j\}\), one vector each |

The trivial character therefore has multiplicity \(4\). Each of the six weight-\(2\) characters has multiplicity \(1+2+1=4\). Weights \(1\), \(3\), and \(4\) have multiplicity \(0\). In particular the full-sign character \(\chi=\{1,2,3,4\}\) has multiplicity \(0\). The two bivectors in \(\pi=V_1\wedge V_2+V_3\wedge V_4\) have characters \(\{1,2\}\) and \(\{3,4\}\), which is the character the pin assigns to both summands of \(\xi\).

The script does not take these multiplicities from the labels. For each of the \(16\) characters it builds the group-average projector
\[
P=\frac1{16}\sum_{g\in G}\chi(g)\,\rho(g)\in\operatorname{Mat}_{28}(\mathbf{Q})
\]
and computes its rank by elimination. The ranks are \(4\) on the trivial character, \(4\) on each weight-\(2\) character, and \(0\) on every other character, including \(\chi\). The ranks sum to \(28\).

The \(\chi\)-isotypic component of \(HT^2(X)\) is the zero space. The pin grades \(HH^2\) by these deck characters and grades \(\operatorname{Ext}^2(E,E)\) by the same group: ext-model.md at `add03476` indexes characters by subsets \(S\subset\{1,2,3,4\}\), and the unique weight-\(4\) character is \(\chi\), of dimension \(352\). A linear map of these representations sends the \(\chi\)-component of the source to the \(\chi\)-component of the target. The source component is zero, so
\[
\operatorname{im}(\operatorname{ev}_E)\cap\operatorname{Ext}^2(E,E)_\chi=\{0\}
\]
for the deck-equivariant evaluation. The unique linear map \(\mathbf{Q}^0\to\operatorname{Ext}^2(E,E)_\chi\) has kernel dimension \(0\). That is injectivity of the full-sign component of \(\operatorname{ev}_E\). It is not injectivity of Pridham’s \(\mathsf{I}:HH\to HC\).

Section 0.1 of the survey stated this character decomposition as unverified, and stated the intersection consequence. The decomposition holds, and the intersection consequence holds for the deck-equivariant evaluation. \(O_{\mathrm{full}}\) is not evaluated, so the intersection does not decide membership of \(O_{\mathrm{full}}\) in the image. Membership of a full-sign class in the image is equivalent to vanishing of that class.

### Controls that must fail

1. Tangent sign flipped. The coefficient of \(dx_i/(-y_i)\) is read as \(+1\), so every \(V_i\) is given the trivial character, while each \(\eta_i\) keeps character \(\{i\}\). The same checker reports \(18\) failures. Among them: \(V_1\wedge V_2\) is not the character \(\{1,2\}\); \(V_3\wedge V_4\) is not \(\{3,4\}\); the four diagonals are not invariant; the trivial multiplicity is \(6\), not \(4\); each weight-\(2\) multiplicity is \(1\), not \(4\); and the four weight-\(1\) characters have multiplicity \(4\). The script exits unless this control fails. It failed.
2. One extra basis vector of character \(\chi\), appended to the pinned basis. The full-sign projector is then \(29\times 29\) of rank \(1\). The zero map on that one-dimensional source has kernel dimension \(1\), so the injectivity assertion fails. The checker reports the multiplicity, the projector rank, and the kernel dimension. The script exits unless this control fails. It failed.

## 3. Marks for SURVEY §9

### 3.1. arXiv:2502.03415v2, Remark 8.3.5

Surjectivity in Lemma 8.3.4 is already marked **fails** in the survey, by \(28<7372\). It is not reopened. The remark keeps kernel equality and drops surjectivity. Its conclusion, once the hypotheses hold, is injectivity of \(\sigma\) on the image of \(ob_E\), not injectivity on the \(352\)-dimensional sector.

| Hypothesis | Mark | Reason |
|---|---|---|
| \(\ker(ob_E)=\ker(\lfloor ch(E))\) in \(HT^2(X)\) | still unverified | Diagram (8.3.4) gives \(\lfloor ch(E)=\sigma\circ ob_E\), hence \(\ker(ob_E)\subseteq\ker(\lfloor ch(E))\). The pin gives \(\operatorname{ev}_E(\xi)=0\), so \(\xi\) lies in the kernel of the evaluation. It does not give \(\lfloor ch(E)(\xi)\). Lemma 8.3.3’s isomorphism on \(H^2(\mathcal{O})\), quoted in §1, uses \(ch_0=1\) for a different sheaf. The pinned degree-zero term is \(2\), and the pin does not prove \(\Pi\neq 0\). Equality is the hypothesis Remark 8.3.5 keeps, and no pinned artifact decides it. |
| Identification of \(O_{\mathrm{full}}\) with a class in ordinary \(\operatorname{Ext}^2(E,E)\) to which \(ob_E\) applies | still unverified | Gate-ladder §2 says the ordinary hull is smooth and Yoneda squares miss \(\chi\), and that the star-algebroid residual is the class in the \(352\)-space. A class that has not been evaluated can be zero in both problems. The comparison of the two classes is not in the pin. |
| Membership of that class in \(\operatorname{im}(\operatorname{ev}_E)\) | still unverified | §2 gives \(\operatorname{im}(\operatorname{ev}_E)\cap\operatorname{Ext}^2_\chi=\{0\}\). For the full-sign class itself, membership is equivalent to \(O_{\mathrm{full}}=0\). \(O_2\) is not evaluated, so membership is not decided. Image-injectivity of ordinary \(\sigma\) on the whole image is a separate statement and is not computed here. Vanishing of \(\sigma\) on the \(352\)-space remains the survey’s mark that \(\sigma\) is not injective on that sector. |

The character statement in survey §0.1 **holds**: weight \(0\) and the six weight-\(2\) characters, multiplicity \(4\) each, and no full-sign character. The intersection consequence **holds** for the deck-equivariant evaluation.

### 3.2. arXiv:1208.3111v4, Remark 1.21

| Hypothesis | Mark | Reason |
|---|---|---|
| The star product truncated at order \(h^2\), then held fixed, presented as a Remark 1.21 presheaf or as a smooth proper dg subcategory of \(\mathrm{per}_{dg}(\mathcal{O}_Y)\) | still unverified | The pin describes a star-algebroid through order \(h^2\) in the direction \(\xi\). It does not exhibit that truncation as such a presheaf or subcategory. |
| A square-zero extension of commutative \(k\)-algebras over that fixed algebra, and the cyclic-lifting hypotheses used for \(\mathsf{I}\circ\mathcal{L}=0\) | still unverified | No such extension, and no such lifting, is pinned for the truncated product. |
| Identification of \(O_{\mathrm{full}}\) with \(o_e(\mathscr{F})\) | still unverified | No pinned artifact names \(O_{\mathrm{full}}\) as that obstruction. |

Under the hypotheses the remark states, the printed conclusion is \(\mathsf{I}\mathcal{L}(o_e(\mathscr{F}))=0\). The step from that identity to \(\mathcal{L}(o_e(\mathscr{F}))=0\) is the last step of the proof of Corollary 1.20, which Remark 1.21 excludes. Injectivity of \(\mathsf{I}:HH^k_*(\mathcal{N})\to HC^k_*(\mathcal{N})\) on a star-product truncation is **still unverified**. No matrix of \(\mathsf{I}\) on \(\operatorname{im}(\operatorname{ev}_E)\) is pinned. The injective map computed in §2 is the full-sign component of deck-equivariant evaluation, whose source is zero. It is a different map.

### 3.3. arXiv:2111.12985v3, Theorem 2.8

| Hypothesis | Mark | Reason |
|---|---|---|
| A curved DG-pair \((A,I)\) and a graded linear section of \(A\to A/I\) such that \(A/I\) controls the deformation problem whose obstruction is \(O_{\mathrm{full}}\) | still unverified | Theorem 2.8 produces \(\sigma^k\) for any curved Lie ideal and any graded linear section. The pin does not supply a pair whose quotient controls the star-algebroid residual. |
| Identification of that class with a Maurer–Cartan obstruction to which \(\sigma^k\) applies, so that the linear component annihilates it | still unverified | The annihilation sentence on PDF page 4 requires the deformation problem to be controlled by \(A/I\). That is the previous row. |

Theorem 8.2 of arXiv:2208.00694v2 is not one of these hypotheses. The survey already records that its Lie-algebroid module hypothesis fails for the pinned residual, and that this failure leaves Theorem 2.8 untouched.

## 4. What this file does not decide

Kernel equality, the ordinary-obstruction comparison, membership of \(O_{\mathrm{full}}\) in \(\operatorname{im}(\operatorname{ev}_E)\), the three Remark 1.21 comparison hypotheses, injectivity of Pridham’s \(\mathsf{I}\) on a star truncation, and both Theorem 2.8 comparison hypotheses stay unverified. The character decomposition and the full-sign intersection hold. No theorem text has been added beyond the sentences quoted from the three PDFs.
