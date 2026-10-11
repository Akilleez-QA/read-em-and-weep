# Literature and comparison-theorem survey

Scope: published results that could give an all-order continuation, or a comparison or detection theorem, for the Horrocks–Mumford deformation of the triple \((X,E,\xi)\) pinned in `research/hsd/gate-ladder.md` at `d915eeab061f3dddebe1a1d3d7c80ca09609dcee` (branch `research/hsd-gate-ladder`, Section 4.1). The object of that gap is the full-sign star-algebroid residual \(O_{\mathrm{full}}=\mathrm{pr}_\chi O_2(a)\), \(\chi=\{1,2,3,4\}\), in the \(352\)-dimensional space \(\operatorname{Ext}^2(E,E)_\chi\).

Each hypothesis below is marked **holds**, **fails**, or **unverified**, with the reason taken from that pin or from a dimension the pin’s geometry determines. A reading is inapplicable when a hypothesis it requires is marked **fails**. An unverified comparison remains a candidate. No reading is the only surviving strategy. Vanishing of ordinary \(\sigma\) on the full-sign sector rules out injectivity of \(\sigma\) on that whole sector. It does not rule out injectivity of \(\sigma\) on \(\operatorname{im}(\operatorname{ev}_E)\).

This repair follows review 6110240962. Every arXiv citation is version-pinned to a file that was fetched. The official HTML of arXiv:2502.03415v2 does contain Lemma 8.3.4 and Remark 8.3.5. The same two statements are Lemma 8.2.4 and Remark 8.2.5 in arXiv:2502.03415v1. Bloch’s paper was not accessed. No value of \(O_2\) is computed, and no character multiplicity is recomputed.

The carrier route on \(\mathbf{P}^1\times\mathbf{P}^3\) is outside this survey.

## 0. The pinned setup used as the checklist

From Section 1 of the pin.

- \(C\) is the smooth projective model of \(y^2=x^3-x\), and \(X=C^4\).
- \(H\) is the normalized Horrocks–Mumford bundle on \(\mathbf{P}^4\), \(f:X\to\mathbf{P}^4\) is the composite of the degree-two maps \(C\to\mathbf{P}^1\) with the symmetric quotient \((\mathbf{P}^1)^4\to\mathbf{P}^4\), and \(N=\mathcal{O}_X(\Theta)\) is the exterior product of the four origin line bundles. \(E=f^*H\otimes N\) is rank two and determinant-trivial, with \(c_2(E)=15\theta^2\) and \(\operatorname{ch}(E)=\exp(i\sqrt{15}\,\theta)+\exp(-i\sqrt{15}\,\theta)\).
- \(V_i\) is dual to \(dx_i/y_i\), \(\pi=V_1\wedge V_2+V_3\wedge V_4\), \(\Pi=\iota_\pi(\theta^2)/2\), and \(\xi=\pi+15\Pi\in HH^2(X)\). Under HKR, \(\pi\) is the Poisson summand and \(15\Pi\) is the scalar gerbe summand. Both have deck characters \(\{1,2\}\) and \(\{3,4\}\) for \(G=(\mathbf{Z}/2)^4\), \(y_i\mapsto -y_i\).
- \(\operatorname{ev}_E(\xi)=0\), with triple-overlap unit \(b=-15\Pi\).
- A second-order ambient extension is a star-algebroid through order \(h^2\) in the direction \(\xi\) (D’Agnolo–Schapira, arXiv:math/0506064v2, Section 3, as cited by the pin). For a first-order module lift \(a\), the residual \(O_2(a)\) lies in \(\operatorname{Ext}^2(E,E)\), and \(O_{\mathrm{full}}\) is independent of that lift and of the second-order ambient acceleration. \(\dim\operatorname{Ext}^2(E,E)_\chi=352\).
- This is the star-algebroid module problem. The ordinary hull of \(E\) on fixed \(X\) is smooth of dimension \(87\), or \(83\) after determinant trivialization (Talpo–Vistoli, arXiv:1006.0497v2, Proposition 6.36). Every class in \(\operatorname{Ext}^1(E,E)\) has deck weight \(0\) or \(1\), so Yoneda squares miss \(\chi\).
- The ordinary Buchweitz–Flenner map
  \[
  \sigma:\operatorname{Ext}^2(E,E)\longrightarrow H^2(\mathcal{O}_X)\oplus H^3(\Omega_X^1)\oplus H^4(\Omega_X^2)
  \]
  vanishes on the whole \(352\)-dimensional sector. Its rank there is \(0\). The \(\chi\)-part of the target is \(4\)-dimensional and sits in \(H^3(\Omega^1)\). Ordinary \(\sigma(O_{\mathrm{full}})=0\) is automatic for every full-sign class. That vanishing excludes injectivity of \(\sigma\) on the whole sector. It does not exclude injectivity of \(\sigma\) on \(\operatorname{im}(\operatorname{ev}_E)\).
- \(15\Pi\) is an infinitesimal class in \(H^2(\mathcal{O}_X)\). The pin records no identification of it with a torsion Brauer class.
- The finite model at `add03476d9055aa00e1e00778eea6332cf8e01cc` (`research/hm/ext-model.md` on `research/hm-exact-ext`) gives \(\dim\operatorname{Ext}^j(E,E)=(1,87,7372,87,1)\) and, in weight \(4\), \(\dim\operatorname{Ext}^2=352\). That note states that no second-order obstruction claim follows from these dimensions alone.

Dimension used for surjectivity. \(T_X\) is trivial of rank \(4\), so
\[
\dim H^0(X,\wedge^2 T_X)=6,\qquad
\dim H^1(X,T_X)=4\cdot\dim H^1(\mathcal{O}_X)=16,\qquad
\dim H^2(X,\mathcal{O}_X)=6.
\]
The HKR source of \(\operatorname{ev}_E\) therefore has dimension \(28\). Since \(28<352\le 7372\), \(\operatorname{ev}_E:HH^2(X)\to\operatorname{Ext}^2(E,E)\) is not surjective, and its image cannot fill the full-sign sector. That dimension comparison does not by itself prove that the image meets the sector in zero.

### 0.1. Reviewer’s character statement, unverified here

Per review 6110240962, and not verified in this file: for deck-linearized \(E\), equivariant HKR on \(C^4\) gives \(HH^2\) only weight-\(0\) and weight-\(2\) characters, of multiplicity \(4\) each, and no full-sign character. The stated consequence is that \(\operatorname{im}(\operatorname{ev}_E)\) meets the full-sign sector in zero. Image-membership of \(O_{\mathrm{full}}\), together with injectivity of \(\sigma\) on that image and \(\sigma(O_{\mathrm{full}})=0\), would then force \(O_{\mathrm{full}}=0\). Failure of image-injectivity is not inferred by assuming the class is nonzero. This survey does not recompute the multiplicities.

## 1. Markman, arXiv:2502.03415

Fetched: the official HTML of [arXiv:2502.03415v2](https://arxiv.org/html/2502.03415v2) and of [arXiv:2502.03415v1](https://arxiv.org/html/2502.03415v1). The v2 comment on the abstract page says Section 8.1 is new. The two versions therefore number Section 8 differently. Both numberings are cited below. Neither numbering is asserted to be absent.

### 1.1. The two numberings

In arXiv:2502.03415v2, Section 8.3, the official HTML contains both statements.

- Lemma 8.3.4: if the kernels of \(ob_E\) and \(\rfloor ch(E)\) in \(HT^2(M)\) are equal and \(ob_E\) is surjective, then \(E\) is semiregular. The proof uses diagram (8.3.4), attributed there to Buchweitz–Flenner, arXiv:math/0606730v1, Proposition 6.2.1 and Corollary 6.3.2.
- Remark 8.3.5: dropping surjectivity in Lemma 8.3.4, and keeping the kernel equality, the semiregularity map still restricts to an injection on the image of the obstruction map.
- Remark 8.3.6 records invariance of the hypotheses of Lemma 8.3.4 under a derived equivalence when the image is again a coherent sheaf, and identifies the target summand with \(H\Omega_{-2}\).

In arXiv:2502.03415v1 the same two statements are Lemma 8.2.4 and Remark 8.2.5, and the derived-equivalence note is Remark 8.2.6. In that version the proof cites diagram (8.2.4). Displayed equation (8.3.4) is the Orlov transform \(E:=\Phi(\pi_1^*F_1\otimes\pi_2^*F_2)\), and displayed equation (8.3.5) is the subspace \([\pi_1^*HT^2(X)\otimes\pi_2^*HT^0(X)]\oplus[\pi_1^*HT^0(X)\otimes\pi_2^*HT^2(X)]\). Those v1 equation numbers are not Lemma 8.3.4 and Remark 8.3.5.

In v2 the Orlov transform with the same formula is displayed equation (8.4.4), and the corresponding subspace is displayed equation (8.4.5). Diagram (8.3.4) in v2 is the commutative diagram, not that transform. In v2, Example 8.2.4 and Lemma 8.2.5 are different statements from the v1 lemma and remark that carry those numbers.

In v2, Lemma 8.3.10 and Remark 8.3.11 do occur. Lemma 8.3.10 transports kernel-equals-annihilator across a derived equivalence of abelian varieties. Remark 8.3.11 extends that lemma to the Mukai vector on a more general projective variety. They are not the semiregularity criterion. arXiv:2509.23403v2 labels its Lemma 11.3 with the citations [M2, Lemma 8.3.10] and [M2, Remark 8.3.11]. Those labels, in arXiv:2502.03415v2, denote the transport statements just named, not Lemma 8.3.4 and Remark 8.3.5.

Primary citations below are the v2 numbers. Each v1 number is the same statement in v1.

### 1.2. Lemma 8.3.4, which is Lemma 8.2.4 in v1

Citation: arXiv:2502.03415v2, Lemma 8.3.4. The same statement is arXiv:2502.03415v1, Lemma 8.2.4.

Statement read: if \(\ker(ob_E)=\ker(\lfloor ch(E))\) inside \(HT^2(M)\) and \(ob_E\) is surjective, then \(E\) is semiregular. Semiregularity here is injectivity of \(\sigma\) on \(\operatorname{Ext}^2(E,E)\).

| Hypothesis | Mark | Reason |
|---|---|---|
| Input is a coherent sheaf on a smooth projective variety, with \(ob_E:HT^2\to\operatorname{Ext}^2\) | fails | The residual lives in the star-algebroid module category of the pin, Section 2. The ordinary sheaf \(E\) is a different deformation problem. |
| \(ob_E\) surjective | fails | Source dimension \(28\), target dimension \(7372\), and the full-sign sector already has dimension \(352\). |
| \(\ker(ob_E)=\ker(\lfloor ch(E))\) | unverified | No computation in this survey evaluates either kernel on \((X,E)\). |
| Injectivity of \(\sigma\) on all of \(\operatorname{Ext}^2(E,E)\), the lemma’s conclusion | fails | The pin records that ordinary \(\sigma\) vanishes on the nonzero \(352\)-dimensional full-sign sector, so \(\sigma\) is not injective on that whole sector, nor on all of \(\operatorname{Ext}^2(E,E)\). This mark is not a mark about \(\operatorname{im}(\operatorname{ev}_E)\). |

### 1.3. Remark 8.3.5, which is Remark 8.2.5 in v1

Citation: arXiv:2502.03415v2, Remark 8.3.5. The same statement is arXiv:2502.03415v1, Remark 8.2.5.

Statement read: dropping surjectivity, and keeping the kernel equality, the semiregularity map restricts to an injection on the image of the obstruction map.

| Hypothesis | Mark | Reason |
|---|---|---|
| The remark, as a statement about \(\operatorname{im}(ob_E)\) for a coherent sheaf | holds | It is the text of v2 Remark 8.3.5 and of v1 Remark 8.2.5, and \(E\) is a coherent sheaf on the smooth fourfold \(X\). |
| Kernel equality, which the remark retains | unverified | Not computed for the pinned \(E\). |
| \(O_{\mathrm{full}}\in\operatorname{im}(ob_E)=\operatorname{im}(\operatorname{ev}_E)\) | unverified | The dimension comparison shows that the image cannot fill the \(352\)-space. It does not show that the intersection is zero. The stronger intersection statement is the reviewer’s lemma in Section 0.1, unverified here. |
| Injectivity of \(\sigma\) on the whole full-sign sector | fails | Ordinary \(\sigma\) vanishes on that nonzero sector. |
| Injectivity of \(\sigma\) on \(\operatorname{im}(\operatorname{ev}_E)\) | unverified | Sector vanishing does not decide it. Image-membership, image-injectivity, and \(\sigma(O_{\mathrm{full}})=0\) would force \(O_{\mathrm{full}}=0\), by the same formal implication the review records. That is not a contradiction of the remark. |

Remark 8.3.6 in v2, Remark 8.2.6 in v1, records derived-equivalence invariance of the lemma’s hypotheses when the image is a coherent sheaf. The pin’s Section 2 records no identification of \(E\), or of \(O_{\mathrm{full}}\), with an object of \(D^b(X\times\widehat{X})\). That identification is unverified. The surjectivity hypothesis of the lemma already fails for \(E\), so the lemma is not restored by an equivalence. The remark that drops surjectivity is the separate comparison in the table above.

### 1.4. The secant kernel lemma and Section 9

Citation: arXiv:2502.03415v1, Lemma 8.3.1, for the secant box product and for its Orlov transform (8.3.4). The same statement in arXiv:2502.03415v2 is Lemma 8.4.1, for the transform (8.4.4).

Statement read: the kernel of the obstruction map equals the annihilator of the Chern character.

| Hypothesis | Mark | Reason |
|---|---|---|
| The sheaf is the secant box product of ideal sheaves of Abel–Jacobi curves, or the Orlov transform in v1 (8.3.4) or v2 (8.4.4) | fails | The pinned \(E\) is the Horrocks–Mumford pullback \(f^*H\otimes N\) on the abelian fourfold \(X=C^4\). |

Citation: arXiv:2502.03415v2, Lemma 9.3.11 and Theorem 1.5.1. Both numbers occur in the v2 HTML. The v2 proof of Lemma 9.3.11 cites Remark 8.3.5. The v1 proof of the corresponding lemma cites Remark 8.2.5.

Statement read: the \(\mu_{8d}\)-twisted reflexive sheaf \(\mathcal{B}\) on the quotient \(Y=(X\times\widehat{X})/\overline{G}\) is semiregular. Theorem 1.5.1 states that the Hodge–Weil classes of polarized abelian sixfolds of Weil type, with complex multiplication by \(\mathbf{Q}(\sqrt{-d})\) and discriminant \(-1\), are algebraic. The introduction of the same source says the semiregularity proof is special to genus \(3\).

| Hypothesis | Mark | Reason |
|---|---|---|
| Genus-\(3\) Jacobian, cyclic groups of order \(d+1\), general-position orbits, quotient sixfold, band \(\mu_{8d}\) | fails | The pinned variety is a product of four elliptic curves, the sheaf is \(f^*H\otimes N\), and \(15\Pi\) is an infinitesimal class in \(H^2(\mathcal{O}_X)\). |
| Theorem 1.5.1 as a continuation of \((X,E,\xi)\) | fails | The theorem concludes algebraicity of Weil classes on a sixfold of Weil type. It does not evaluate a star-algebroid residual on the fourfold. |

### 1.5. Section 7, for the torsion reading

Citation: arXiv:2502.03415v2, Definition 7.3.5, Definition 7.3.8, Conjecture 7.3.9, and Section 7.4. These numbers occur in the v2 HTML. Section 7 precedes the new Section 8.1, and the same definition and conjecture numbers are the ones used in Section 5.1 below.

Statement read: Definition 7.3.5 is the Atiyah class of a \(\mu_r\)-twisted sheaf. Definition 7.3.8 says the twisted sheaf is semiregular when \(\sigma\) is injective. Conjecture 7.3.9 is the twisted analogue of Buchweitz–Flenner, arXiv:math/9912245v1, Theorem 5.1: a semiregular \(\mu_r\)-twisted sheaf deforms over the locus where its Chern character stays of Hodge type. Section 7.4 proves the conjecture when the base is a family of abelian varieties and the Brauer class extends to a projective bundle. The text says the conjecture should follow from Pridham, arXiv:1208.3111v4, Remark 2.26, and that the author cannot reconcile the terminology. The band in the conjecture is \(\mu_r\).

| Hypothesis | Mark | Reason |
|---|---|---|
| The class is a Čech cocycle with values in \(\mu_r\) | fails | The pin records \(15\Pi\in H^2(\mathcal{O}_X)\) as infinitesimal, with no proved identification with a torsion Brauer class. |
| \(\sigma\) injective on all of the \(\operatorname{Ext}^2\) that contains the full-sign sector | fails | Ordinary \(\sigma\) vanishes on that sector, so it is not injective on the whole space. This is not a statement about \(\operatorname{im}(\operatorname{ev}_E)\). |

## 2. Markman, arXiv:2509.23403v2

Fetched: the official HTML of [arXiv:2509.23403v2](https://arxiv.org/html/2509.23403v2). Lemma 11.3, Question 11.4, Proposition 11.5, and Theorem 2.1 occur in that HTML.

### 2.1. Lemma 11.3

Citation: arXiv:2509.23403v2, Lemma 11.3.

Statement read: if \(\ker(\operatorname{ev}_E:HH^2(Y)\to\operatorname{Hom}(E,E[2]))\) equals the annihilator of \(ch(E)\) in \(HH^2(Y)\) and \(\operatorname{ev}_E\) is surjective, then \(E\) is semi-regular. The proof uses the HKR isomorphism and the diagram whose commutativity is attributed to arXiv:math/0606730v1, Proposition 6.2.1 and Corollary 6.3.2. The paragraph before the lemma calls this the criterion of [M2, Remark 8.3.11] and the lemma’s own bracket citation is [M2, Lemma 8.3.10]. Section 1.1 records what those two numbers are in arXiv:2502.03415v2. The statement of Lemma 11.3 matches v2 Lemma 8.3.4, not v2 Lemma 8.3.10.

| Hypothesis | Mark | Reason |
|---|---|---|
| \(\operatorname{ev}_E\) surjective onto \(\operatorname{Ext}^2(E,E)\) | fails | Source dimension \(28\), target dimension \(7372\). |
| Kernel equals the annihilator of \(ch(E)\) | unverified | Not computed for the pinned \(E\). |
| The sheaf is the secant sheaf of Proposition 11.1 | fails | Lemma 11.3 is stated generally, and the application in this section is the secant sheaf on a Jacobian, which is not \(f^*H\otimes N\). |
| Injectivity of \(\sigma\) on all of \(\operatorname{Ext}^2\), the conclusion under surjectivity | fails | Same whole-space vanishing as in Section 1.2. Not a mark about the image. |

### 2.2. Question 11.4

Citation: arXiv:2509.23403v2, Question 11.4.

Statement read, in full: “Is the surjectivity of \(ev_E\) needed in Lemma 11.3? Does the Semi-regularity Theorem 2.1 hold under the weaker assumption that \(\sigma_E\) restricts to the image of \(ev_E\) as an injective map (considering also twisted sheaves as we did in Section 2)?”

This is a question. It is not a theorem, so it supplies no continuation. The same section says the paper avoids the question by descending to a quotient on which surjectivity holds (Proposition 11.5). Section 12 says an affirmative answer would be relevant to dimension at least \(8\) and to CM fields with \([K:\mathbf{Q}]>2\), and that the secant examples of arXiv:2502.03415v2, Examples 8.2.3 and 8.2.4, are yet to be checked. Those two example numbers occur in the v2 HTML. Sector vanishing of \(\sigma\) is not an answer to the question: it rules out injectivity on the whole full-sign sector, and the question asks about injectivity on the image. That inference is withdrawn in Section 8.

| Hypothesis | Mark | Reason |
|---|---|---|
| A published affirmative answer in arXiv:2509.23403v2 | fails | The accessed text leaves the question open. |

### 2.3. Proposition 11.5 and Theorem 2.1

Citation: arXiv:2509.23403v2, Proposition 11.5 and Theorem 2.1.

Proposition 11.5 states that the descended sheaf \(\overline{\mathcal{E}}\) on the quotient abelian variety \(A=(X\times\widehat{X})/\overline{G}\) is semi-regular. The sketch uses Lemma 11.3 for ideal sheaves of curves and their box products. Theorem 2.1 is the semi-regularity theorem of that paper, applied in Section 11.5 to conclude algebraicity of Weil classes.

| Hypothesis | Mark | Reason |
|---|---|---|
| The object is \(\overline{\mathcal{E}}\) on that quotient | fails | The pinned object is the star-algebroid residual of \(f^*H\otimes N\). |

## 3. Pridham, arXiv:1208.3111v4

Fetched: the official HTML of [arXiv:1208.3111v4](https://arxiv.org/html/1208.3111v4) and page 12 of the v4 PDF. Remark 1.21 is on that page. Title: “Semiregularity as a consequence of Goodwillie’s theorem”.

### 3.1. The introduction theorem

The introduction states an unnumbered theorem. Statement read: for a local Artinian \(\mathbf{C}\)-algebra, a smooth morphism of Artin stacks, a square-zero ideal, and a perfect complex, the obstruction \(o(\mathscr{F})\) maps to \(0\) under the composite into the truncated de Rham complex if and only if the horizontal lift of \(\operatorname{ch}_p\) stays in \(F^p\).

| Hypothesis | Mark | Reason |
|---|---|---|
| The base extension is a square-zero extension of a commutative Artinian algebra, and the stack morphism is smooth | fails | The pinned deformation varies the product by the star-algebroid terms of order \(h\) and \(h^2\). Section 2 of the same paper declares that from that point all rings are commutative. |
| The obstruction is the ordinary module obstruction of \(E\) on a varying commutative base | fails | The pin places \(O_{\mathrm{full}}\) in the star-algebroid residual, and records that the ordinary hull is already smooth. |

### 3.2. Corollary 1.20 and Remark 1.21

Citation: arXiv:1208.3111v4, Corollary 1.20 and Remark 1.21 (PDF page 12).

Statement read. If \(\mathcal{N}\) is a geometric noncommutative scheme in Orlov’s sense, an admissible dg subcategory of \(\mathrm{per}_{dg}(\mathcal{O}_Y)\) for \(Y\) smooth and proper over a field of characteristic \(0\), then for a square-zero extension \(e:A\to B\) of commutative \(k\)-algebras with kernel \(I\), and a perfect \(\mathcal{N}\otimes_k B\)-complex \(\mathscr{F}\), the obstruction to lifting \(\mathscr{F}\) lies in the kernel of the Lefschetz map
\[
\mathcal{L}:\operatorname{Ext}^2(\mathscr{F},\mathscr{F}\otimes^{\mathbf{L}} I)\longrightarrow HH_{-2}(\mathcal{N})\otimes_k I.
\]
The proof reaches \(\mathsf{I}\mathcal{L}(o_e(\mathscr{F}))=0\) before the last step. The last step uses injectivity of \(\mathsf{I}\) on \(\mathrm{per}_{dg}(\mathcal{O}_Y)\), by the Lefschetz principle as in Remark 2.27, and only then concludes \(\mathcal{L}(o_e(\mathscr{F}))=0\).

Remark 1.21: until that final step, \(\mathcal{N}\) need only be a smooth proper dg subcategory of \(\mathrm{per}_{dg}(\mathcal{O}_Y)\) for \(Y\) quasi-compact and semi-separated, and then \(\mathsf{I}\mathcal{L}(o_e(\mathscr{F}))=0\). The remark does not conclude \(\mathcal{L}(o_e(\mathscr{F}))=0\). Passing from \(\mathsf{I}\circ\mathcal{L}=0\) to \(\mathcal{L}=0\) requires injectivity of \(\mathsf{I}\), which is the step the remark omits. The same remark allows \(\mathcal{O}_Y\) to be replaced by a presheaf \(\mathscr{A}\) of simplicial associative \(R\)-algebras on affine opens whose \(\pi_*\mathscr{A}\) admits a quasi-coherent \(\mathcal{O}_Y\)-algebra structure. The examples named are the structure hypersheaf of a derived scheme with underived truncation \(Y\), and any quasi-coherent simplicial associative algebra on that derived scheme.

| Hypothesis | Mark | Reason |
|---|---|---|
| Square-zero extension of commutative \(k\)-algebras, with the algebra held fixed, and \(O_{\mathrm{full}}\) equal to the module-lifting obstruction \(o_e(\mathscr{F})\) | unverified | Corollary 1.20 deforms the module and holds the algebra fixed. The pinned star product varies the product. The comparison that would present the truncation at order \(h^2\) as one such fixed algebra, and identify \(O_{\mathrm{full}}\) with \(o_e(\mathscr{F})\), is not in the pin. |
| \(\mathcal{N}\) admissible in \(\mathrm{per}_{dg}(\mathcal{O}_Y)\), or the weaker presheaf of Remark 1.21, and the cyclic-lifting hypotheses used for \(\mathsf{I}\circ\mathcal{L}=0\) | unverified | A star product on \(X\) is an associative deformation of \(\mathcal{O}_X\). Those hypotheses are not checked for \((X,E,\xi)\). |
| The conclusion \(\mathcal{L}(O_{\mathrm{full}})=0\) without injectivity of \(\mathsf{I}\) | fails | Remark 1.21 gives \(\mathsf{I}\circ\mathcal{L}=0\) under the hypotheses it states. It does not give \(\mathcal{L}=0\) unless \(\mathsf{I}\) is injective on that class. |

This reading is an unverified comparison. It is not singled out as the only surviving strategy. The commutative corollaries below are a different reading.

### 3.3. Corollaries 2.24 and 2.25, Remark 2.26

Citation: arXiv:1208.3111v4, Corollary 2.24, Corollary 2.25, Remark 2.26. These numbers occur in the v4 HTML.

Corollary 2.24: for a morphism of derived stacks over \(\mathbf{Q}\) and a nilpotent closed immersion, the Goodwillie–Jones Chern character induces an Abel–Jacobi map, and for a square-zero ideal the image of that map is given by the semiregularity component \(\sigma_{p-1}\). Corollary 2.25: for a local Artinian simplicial \(\mathbf{C}\)-algebra and a derived Artin stack whose truncation is locally of finite type, \(\operatorname{ch}_p\) stays in \(F^p\) if and only if the image of \(\mathcal{L}_{p-1}(o_e(\mathscr{F}))\) in the truncated derived de Rham cohomology vanishes. The paragraph before Corollary 2.25 says this establishes the conjectures of Buchweitz–Flenner and hence those of Bloch, for \(X\) a smooth proper scheme over a local Artinian \(\mathbf{C}\)-algebra. Remark 2.26 extends both corollaries to \(\mu_r\)-twisted perfect complexes by replacing \(X\) with the \(\mu_r\)-gerbe. The reason given is that \(\mu_r\) is étale and reductive over \(\mathbf{Q}\).

| Hypothesis | Mark | Reason |
|---|---|---|
| Commutative (derived) base, perfect complex of the structure sheaf or of a commutative derived scheme | fails | Section 2 restricts to commutative rings. The pinned product is the star product in the direction \(\xi\). |
| Band \(\mu_r\), Remark 2.26 | fails | \(15\Pi\) is infinitesimal in \(H^2(\mathcal{O}_X)\), not a class in \(H^2_{\mathrm{\acute{e}t}}(X,\mu_r)\). |
| Constant family, so the Hodge condition is automatic and the obstruction maps to \(0\) | fails | That conclusion is the ordinary annihilation. The pin records it for every full-sign class and records that it does not evaluate \(O_{\mathrm{full}}\). |

## 4. Buchweitz–Flenner, arXiv:math/9912245v1

Fetched: the official HTML of [arXiv:math/9912245v1](https://arxiv.org/html/math/9912245v1), the only arXiv version, dated 31 December 1999. Definition 4.1, Theorem 5.1, Theorem 7.2, Theorem 7.3, and Proposition 8.2 occur in that HTML.

### 4.1. Definition 4.1

Statement read: for a perfect complex on a morphism of complex spaces,
\[
\sigma=\operatorname{Tr}(*\cdot\exp(-\operatorname{At}(\mathscr{F}))):\operatorname{Ext}^2(\mathscr{F},\mathscr{F})\longrightarrow\prod_k H^{k+2}(X,\Lambda^k\mathbb{L}_{X/Y}).
\]

| Hypothesis | Mark | Reason |
|---|---|---|
| The map is defined for the coherent sheaf \(E\) on \(X\) | holds | \(E\) is a vector bundle on a smooth projective fourfold, so it is perfect. |
| Vanishing of this \(\sigma\) on the \(352\)-space detects or kills \(O_{\mathrm{full}}\) | fails | The pin records that this ordinary map is zero on the whole sector, and that the vanishing does not identify the relative cyclic map and does not evaluate the residual. |

### 4.2. Theorem 5.1

Statement read: if a horizontal section of \(\prod_{p\in I} R^p\pi_*\Omega^p_{X/S}\) is the corresponding Chern character component of an \(I\)-semiregular sheaf on the special fibre of a deformation of a compact algebraic manifold, then the section is algebraic nearby. \(I\)-semiregular means the corresponding part of \(\sigma\) is injective.

| Hypothesis | Mark | Reason |
|---|---|---|
| \(I\)-semiregularity, meaning injectivity of the corresponding part of \(\sigma\) on a space equal to the full-sign sector | fails | Ordinary \(\sigma\) vanishes on that whole sector. This does not mark injectivity on \(\operatorname{im}(\operatorname{ev}_E)\). |
| The deformation is a deformation of the manifold with the sheaf on the fibres | fails | The pinned deformation is a star-algebroid on a fixed fourfold. |

### 4.3. Theorems 7.2 and 7.3

Theorem 7.2, as read: \(X\) proper and smooth over \(\Sigma\), special fibre bimeromorphic to a Kähler manifold, \(\mathscr{F}_0\) a coherent module on the special fibre, \(S\) the base of a semiuniversal deformation of \(\mathscr{F}_0\). Then \(\dim S\ge\dim\operatorname{Ext}^1-\dim\ker\sigma\), and if \(\sigma\) is injective then \(S\) is smooth over a closed subspace of the formal base. Theorem 7.3, as read: on a fixed complex space, a coherent module of locally finite projective dimension with finite-dimensional \(\operatorname{Ext}^1\) satisfies the same dimension inequality, and if \(\sigma\) is injective then the semiuniversal base is smooth.

| Hypothesis | Mark | Reason |
|---|---|---|
| The functor is the ordinary deformation functor of the coherent sheaf | fails | The pin’s ordinary hull is already smooth of dimension \(87\). The residual \(O_{\mathrm{full}}\) is the star-algebroid residual. |
| Injectivity of \(\sigma\) on all of \(\operatorname{Ext}^2\), or on the whole full-sign sector | fails | The kernel contains that sector. Not a mark about the image of \(\operatorname{ev}_E\). |

The introduction attributes to Bloch the construction, for an lci subscheme \(Z\subset X\) of codimension \(q\), of
\[
\tau:H^1(Z,\mathcal{N}_{Z/X})\to H^{q+1}(X,\Omega_X^{q-1}),
\]
and the conclusion that injectivity of \(\tau\) makes \([Z]\) a smooth point of the Hilbert scheme. That attribution is Buchweitz–Flenner’s. Bloch’s paper itself is recorded in Section 6 as not accessed.

### 4.4. Section 8 and the Hochschild factorization, arXiv:math/0606730v1

Citation: arXiv:math/9912245v1, Section 8.1 and Proposition 8.2. For an lci \(Z\subset X\) of codimension \(q\), the text reconstructs a map \(\tau_B:H^k(Z,\mathcal{N}_{Z/X})\to H^{q+k}(X,\Omega^{q-1})\) and states that Bloch’s semiregularity map is the case \(k=1\). Proposition 8.2 states that \(\tau_B\) and the corresponding component of the Buchweitz–Flenner map coincide.

| Hypothesis | Mark | Reason |
|---|---|---|
| The object is an lci subscheme | fails | \(E\) is a rank-two vector bundle. |

Citation: arXiv:math/0606730v1, Proposition 6.2.1 and Corollary 6.3.2. This is the only arXiv version. Its HTML URL returned 404 on this repair, so the numbers are pinned as the numbers cited for diagram (8.3.4) in the fetched HTML of arXiv:2502.03415v2 and for the analogous diagram in arXiv:2509.23403v2, Lemma 11.3. Statement used there: for a perfect complex, the Hochschild form of \(\sigma\) makes the diagram with the ordinary semiregularity map and the HKR map commute, and the same linearity holds for the Chern–Hochschild character.

| Hypothesis | Mark | Reason |
|---|---|---|
| Perfect complex on a morphism of spaces | holds | \(E\) is a vector bundle on \(X\). |
| The proposition continues a first-order \(HH^2\) class to order \(h^2\) | fails | The cited statements identify the linear semiregularity map with a Hochschild-homology contraction. Neither statement evaluates a second-order residual. |

## 5. Later all-order and comparison results that were read

These are results cited by, or citing, the papers above on the passage from a first-order Hochschild or semiregularity class to an obstruction in every order. Each HTML below was fetched for the pinned version, and the printed numbers used here occur in that HTML unless a sentence says otherwise.

### 5.1. Perry, arXiv:2604.00511v2

Fetched: [arXiv:2604.00511v2](https://arxiv.org/html/2604.00511v2). The abstract says the paper generalizes Buchweitz–Flenner to noncommutative varieties with group actions, applies to twisted derived categories, and answers a question of Markman. The question named in the introduction is Conjecture 7.3.9 of arXiv:2502.03415v2, not Question 11.4 of arXiv:2509.23403v2.

Definition 2.4: \(E\) is semiregular when \(\sigma_E^2:\operatorname{Ext}^2(E,E)\to HH_{-2}(\mathcal{C})\) is injective. The same section defines \(G\)-semiregular (injective on the invariant subspace) and weakly \(G\)-semiregular (the image of a semiregular object of \(\mathcal{C}^G\)). Lemma 2.7: if \(|G|\) is invertible, \(G\)-semiregular implies weakly \(G\)-semiregular.

Theorem 1.1: smooth proper family of complex varieties, semiregular perfect complex with \(\operatorname{Ext}^{<0}=0\), and an algebraic class \(B_0\in H^2(X_0,\mathbf{Q}(1))\) such that \(\exp(B_0)\cdot\operatorname{ch}(E_0)\) stays Hodge. Then \(E_0\) deforms as a twisted perfect complex over an étale neighbourhood, and the class stays algebraic.

Theorem 1.2: the same conclusion for a family of abelian varieties, a finite group \(G\subset X_0\times X_0^\vee\) acting by translations and tensoring, and a weakly \(G\)-semiregular perfect complex.

Theorem 6.1: \(\mathcal{C}\) a smooth proper \(S\)-linear category of geometric origin, \(v\) a section of \(K^{\mathrm{top}}[0](\mathcal{C}/S)\), and \(E_0\) a gluable semiregular object of class \(v_0\). Then \(E_0\) deforms over an étale neighbourhood and \(v\) stays algebraic. The introduction defines geometric origin as a semiorthogonal component of a smooth proper \(S\)-scheme. Theorem 6.3 is the weakly \(G\)-semiregular extension, and it requires the invariant category to be of geometric origin as well.

| Hypothesis | Mark | Reason |
|---|---|---|
| Semiregularity in the sense of Definition 2.4, injectivity of \(\sigma\) on all of \(\operatorname{Ext}^2\) | fails | Ordinary \(\sigma\) vanishes on the \(352\)-dimensional sector, so it is not injective on all of \(\operatorname{Ext}^2\). This is not a mark about \(\operatorname{im}(\operatorname{ev}_E)\). |
| Geometric origin of the star-algebroid module category | fails | The definition requires a semiorthogonal component of a smooth proper scheme. The pinned category is modules over a star product. |
| Algebraic class \(B_0\in H^2(X,\mathbf{Q}(1))\) and a Brauer class on a family of varieties | fails | \(15\Pi\) is infinitesimal in \(H^2(\mathcal{O}_X)\). The deformation in Theorem 1.1 is a twisted perfect complex on a family of varieties. |

### 5.2. Bandiera–Lepri–Manetti, arXiv:2208.00694v2

Fetched: [arXiv:2208.00694v2](https://arxiv.org/html/2208.00694v2). Theorem 4.4 and Theorem 8.2 occur in that HTML.

Theorem 4.4: for a locally free module with a flat \(\mathcal{L}\)-connection on a smooth separated finite-type scheme over a field of characteristic \(0\), the Thom–Whitney totalization of \(\Omega^*(\mathcal{L},\mathcal{H}\mathrm{om}(E,E))\) controls the infinitesimal deformations. \(HH^1\) is the space of first-order deformations and \(HH^2\) is an obstruction space.

Theorem 8.2, in the section “Semiregularity maps and obstructions”: for a Lie pair \((\mathcal{L},\mathcal{A})\) and a locally free \(\mathcal{A}\)-module \((E,\nabla^{\mathcal{A}})\), each composite
\[
i_k\tau_k:HH^2(\mathcal{A};\operatorname{End}(E))\longrightarrow HH^{2+2k}\bigl(X,\Omega^*(\mathcal{L})/\mathcal{G}_{k+1}\bigr)
\]
annihilates every obstruction to deformations as an \(\mathcal{A}\)-module. If the Leray spectral sequence degenerates at \(E_1\), each semiregularity component annihilates obstructions.

| Hypothesis | Mark | Reason |
|---|---|---|
| The residual is the obstruction to deforming a locally free module with a flat connection along a Lie pair | fails | The pin describes the residual as the order-\(h^2\) associative descent residual of a star-algebroid. A Lie-algebroid module is a different category in that description. |
| Equality of that Lie-algebroid obstruction class with \(O_{\mathrm{full}}\) | unverified | The pin leaves this comparison open. The failed object hypothesis makes Theorem 8.2 inapplicable as stated. That inapplicability does not exclude the abstract curved DG-pair theorem of arXiv:2111.12985v3, recorded in Section 5.5. |

### 5.3. Lepri, arXiv:2104.12658v3

Fetched: [arXiv:2104.12658v3](https://arxiv.org/html/2104.12658v3). The printed numbers Corollary 3.16 and Corollary 4.12 do not occur in the HTML of v1, v2, or v3. The introduction’s two theorems in v3 are the following, and their statements match the two results previously cited under those absent numbers.

Theorem 0.1, which the text identifies with Corollary 2.16: a coherent sheaf with a finite locally free resolution on a smooth separated finite-type scheme over a field of characteristic \(0\) has every obstruction in the kernel of \(\tau_1:\operatorname{Ext}^2\to\mathbb{H}^2(X,\Omega^{\le 1}[2])\). If Hodge-to-de Rham degenerates at \(E_1\), every obstruction lies in the kernel of \(\sigma_1(a)=-\operatorname{Tr}(\operatorname{At}(\mathscr{F})\circ a)\), with target \(H^3(\Omega^1)\).

Theorem 0.2, which the text identifies with Corollary 3.12: for a principal bundle with a \(d_{\mathrm{Tot}}\)-closed cyclic form, every obstruction lies in the kernel of the corresponding map \(f_1\).

| Hypothesis | Mark | Reason |
|---|---|---|
| Coherent sheaf on a fixed smooth scheme, or a principal bundle | fails | The residual is a star-algebroid module residual. The kernel statement for the ordinary sheaf is the annihilation the pin already records on the full-sign sector. |

### 5.4. Lepri, arXiv:2102.05016v3

Fetched: [arXiv:2102.05016v3](https://arxiv.org/html/2102.05016v3). The introduction’s two theorems are Theorem 1.1, identified there with Corollary 4.1, and Theorem 1.2, identified there with Corollary 4.2.

Statement read: a connection of type \((1,0)\) on a finite locally free resolution lifts \(\tau_1:\operatorname{Ext}^*\to\mathbb{H}^*(X,\Omega^{\le 1}[2])\) to an \(L_\infty\) morphism, and every obstruction to deforming the coherent sheaf lies in \(\ker\tau_1\). Under Hodge-to-de Rham degeneration at \(E_1\), the obstruction lies in the kernel of \(\sigma_1(a)=-\operatorname{Tr}(\operatorname{At}(\mathscr{F})\circ a)\).

| Hypothesis | Mark | Reason |
|---|---|---|
| Coherent sheaf on a fixed complex manifold | fails | Same category mismatch as Theorem 0.1 of arXiv:2104.12658v3. The \(L_\infty\) lifting is a lifting of the ordinary first-order map. |

### 5.5. Bandiera–Lepri–Manetti, arXiv:2111.12985v3

Fetched: the official HTML of [arXiv:2111.12985v3](https://arxiv.org/html/2111.12985v3) and page 4 of the v3 PDF. Theorem 2.8 is on that page. The text also labels it Corollary 4.10.

Statement read: let \(I\) be a curved Lie ideal of a curved DG-algebra \((A,d,R)\), and let \(\pi:A\to A/I\). For every \(k\ge 0\) there is a canonical \(L_\infty\) morphism
\[
\sigma^k:\frac{A}{I}\rightsquigarrow\frac{A}{[A,A]+I^{(k+1)}A}[2k]
\]
whose linear component is the semiregularity component \(\sigma^k_1\), for every graded linear section of \(\pi\).

This is an abstract curved DG-pair theorem. It does not name \((X,E,\xi)\). It is not excluded by the separate Lie-algebroid application in arXiv:2208.00694v2, Theorem 8.2. That application has its own failed object hypothesis in Section 5.2. The abstract theorem stays an unverified comparison.

| Hypothesis | Mark | Reason |
|---|---|---|
| A curved DG-pair \((A,I)\) whose deformation functor, controlled by \(A/I\), has obstruction class \(O_{\mathrm{full}}\) | unverified | The theorem supplies the \(L_\infty\) morphism once such a pair and a linear section are given. No such pair is identified with the pinned star-algebroid. The Lie-module hypothesis of arXiv:2208.00694v2, Theorem 8.2, is a hypothesis of a different theorem and is not used to mark this one. |

### 5.6. Iacono–Manetti, arXiv:1112.0425v4

Fetched: [arXiv:1112.0425v4](https://arxiv.org/html/1112.0425v4). The unnumbered Main Theorem in the source: \(X\) smooth over an algebraically closed field of characteristic \(0\), \(Z\subset X\) closed of codimension \(p\), and the setup hypothesis that on a Zariski open \(U\) the subscheme \(Z\) is the zero locus of a section of a rank-\(p\) bundle. Then the composition of the semiregularity map with truncation,
\[
H^1(Z,N_{Z|X})\to H^{p+1}(X,\Omega_X^{p-1})\to\mathbb{H}^{2p}(X,\Omega_X^{<p}),
\]
annihilates every embedded obstruction. The main corollary says that if Hodge-to-de Rham degenerates at \(E_1\), the untruncated map does too.

| Hypothesis | Mark | Reason |
|---|---|---|
| Embedded lci deformation of a subscheme | fails | The pinned object is a rank-two bundle and a star-algebroid residual. |

### 5.7. Iacono, arXiv:0707.2454v2

Fetched: [arXiv:0707.2454v2](https://arxiv.org/html/0707.2454v2). Corollary 4.14 occurs in that HTML. Statement read: for a holomorphic map \(f:X\to Y\) of compact Kähler manifolds, with \(p=\dim Y-\dim X\), the obstruction space to deformations of \(f\) with \(Y\) fixed lies in the kernel of
\[
\sigma:H^2(C^\cdot_{f_*})\to H^{p+1}(Y,\Omega_Y^{p-1}).
\]
The introduction says that for an inclusion this map reduces to Bloch’s semiregularity map.

| Hypothesis | Mark | Reason |
|---|---|---|
| Deformation of a holomorphic map of compact Kähler manifolds | fails | The pinned deformation is a star-algebroid module on a fixed fourfold. |

### 5.8. Nishinou, arXiv:2009.01651v1

Fetched: [arXiv:2009.01651v1](https://arxiv.org/html/2009.01651v1), the only arXiv version. Theorems 1, 2, and 3 occur in that HTML.

Theorem 1, as read: an immersion of a compact reduced curve, or of a smooth divisor when the ambient dimension is greater than \(2\), into the special fibre of a deformation of a compact Kähler manifold of dimension at least \(2\), with local complete intersection image, and with the map semiregular. If the cycle class stays Hodge, the map deforms to other fibres. Theorem 2 relates classical semiregularity of a normal-crossings image to surjectivity onto the infinitesimal normal sheaf. Theorem 3 is the nodal Cayley–Bacharach form on a surface.

| Hypothesis | Mark | Reason |
|---|---|---|
| The object is a semiregular divisor map | fails | \(E\) is a rank-two bundle, and the obstruction in view is \(O_{\mathrm{full}}\). |

### 5.9. Chang, arXiv:0808.0988v2

Fetched: [arXiv:0808.0988v2](https://arxiv.org/html/0808.0988v2). The section “Semiregularity” contains no numbered theorem. The argument, as read: for a smooth compact Kähler manifold with an étale locally universal family, obstructions to deformations of the manifold lie in the kernel of contraction
\[
H^2(X,T_X)\to\bigoplus_i\operatorname{Hom}(H^{p,q},H^{p-1,q+2}).
\]
The text calls this Kodaira’s principle that ambient cohomology annihilates obstructions.

| Hypothesis | Mark | Reason |
|---|---|---|
| The obstruction space is \(H^2(X,T_X)\) for a deformation of the manifold | fails | \(O_{\mathrm{full}}\) lies in \(\operatorname{Ext}^2(E,E)_\chi\). The ordinary deformations of \(X\) are the \(H^1(T_X)\) summand of \(HH^2\), which is a different space. |

## 6. Bloch’s semiregularity map

not accessed

The article text of “Semi-regularity and deRham cohomology”, Inventiones Mathematicae 17 (1972), was not obtained. No arXiv version is cited. No theorem number from that paper is stated here.

What Buchweitz–Flenner, arXiv:math/9912245v1, Section 8.1 and the introduction, attribute to Bloch is recorded in Section 4.3 above and is their attribution. The attributed map takes values on \(H^1(Z,\mathcal{N}_{Z/X})\) for an lci subscheme. The pinned object is not an lci subscheme, so that attributed statement does not apply. This is a check of the secondary attribution only.

## 7. What was not given a continuation theorem

The pin cites D’Agnolo–Schapira, arXiv:math/0506064v2, Section 3, as the descent language of the star-algebroid, and the finite-model notes cite Lowen, arXiv:0707.2602v1, for the characteristic morphism that evaluates a Hochschild class on an object. Those roles are first-order or definitional. Numbered all-order continuation theorems from Yekutieli, arXiv:0905.0488v5, from BGNT, arXiv:0810.0030v2, and from Lowen, arXiv:0707.2602v1, were not extracted in this survey. No theorem number from those three papers is used as a continuation of \(O_{\mathrm{full}}\). For any claim that one of them continues \(O_{\mathrm{full}}\) to all orders, the status of that claim in this file is: not accessed.

## 8. Withdrawn inferences

Three inferences from the previous draft of this file are withdrawn.

1. The sentence that arXiv:2502.03415 has no Lemma 8.3.4 and no Remark 8.3.5 is withdrawn. Both occur in the official HTML of v2. The numbering Lemma 8.2.4 and Remark 8.2.5 is the numbering of v1, cited in Section 1.1.
2. The sentence that one strategy survives, and that it is the only one, is withdrawn. Ordinary \(\sigma=0\) on the full-sign sector excludes injectivity on that entire nonzero sector. It does not exclude injectivity on \(\operatorname{im}(\operatorname{ev}_E)\). The reviewer’s lemma in Section 0.1, unverified here, would make the full-sign intersection of that image zero, so an image-membership comparison would force a full-sign class in the image to vanish once image-injectivity and \(\sigma(O)=0\) are granted. It would not contradict image-injectivity.
3. The proposed test that projects the algebra-variation summands of the residual in `research/hm/second-order-algebroid.md` at `c8aec970fd65a105f39f4e8aeb8a17f0f0053f89` into the finite model at `add03476d9055aa00e1e00778eea6332cf8e01cc` is withdrawn as an exclusion test. Closure is recorded for the full second-order residual, including mixed first-order terms. A selected-summand subset has no presentation-independent class. A nonzero selected contribution does not exclude a valid lift over a fixed algebra. No such projection is computed in this file.

## 9. Remaining comparison hypotheses

For each source that this file still treats as an unverified comparison, the hypotheses below are exactly the ones that still have to be checked before the source applies to the pinned residual of \((X,E,\xi)\). Nothing in this section evaluates \(O_2\).

### 9.1. arXiv:2502.03415v2, Remark 8.3.5

The same statement is arXiv:2502.03415v1, Remark 8.2.5. Lemma 8.3.4 is not in this list: its surjectivity hypothesis fails by the dimension comparison in Section 0.

Still unverified for the pinned residual:

- Kernel equality \(\ker(ob_E)=\ker(\lfloor ch(E))\) in \(HT^2(X)\) for this \(E\). The remark keeps this hypothesis and drops surjectivity.
- The comparison of deformation problems that identifies \(O_{\mathrm{full}}\) with a class in the ordinary \(\operatorname{Ext}^2(E,E)\) to which \(ob_E\) applies. The pin’s residual is a star-algebroid class.
- Membership of that class in \(\operatorname{im}(\operatorname{ev}_E)\). The reviewer’s lemma in Section 0.1, unverified here, asserts that the full-sign intersection is zero. If that assertion is proved, membership forces the full-sign component to vanish, and with image-injectivity and \(\sigma(O)=0\) forces the class to vanish. That package is not checked here.

The conclusion, once those hold, is injectivity of \(\sigma\) on the image, not injectivity on the full-sign sector.

### 9.2. arXiv:1208.3111v4, Remark 1.21

Still unverified for the pinned residual:

- A presentation of the star product truncated at order \(h^2\), then held fixed, as a presheaf of simplicial associative algebras allowed by Remark 1.21, or as a smooth proper dg subcategory of \(\mathrm{per}_{dg}(\mathcal{O}_Y)\) for \(Y\) quasi-compact and semi-separated.
- The square-zero extension of commutative \(k\)-algebras over that fixed algebra, and the cyclic-lifting hypotheses the remark uses.
- The identification of \(O_{\mathrm{full}}\) with the module-lifting obstruction \(o_e(\mathscr{F})\) of that fixed algebra.

Under those hypotheses the remark gives \(\mathsf{I}\circ\mathcal{L}(o_e(\mathscr{F}))=0\). It does not give \(\mathcal{L}(o_e(\mathscr{F}))=0\) unless \(\mathsf{I}\) is injective on that class. Injectivity of \(\mathsf{I}\) is the final step of Corollary 1.20, not part of Remark 1.21, and is itself unverified for a star-product truncation.

### 9.3. arXiv:2111.12985v3, Theorem 2.8

Page 4 of the v3 PDF. Still unverified for the pinned residual:

- A curved DG-pair \((A,I)\) and a graded linear section of \(A\to A/I\) such that the DG-Lie algebra \(A/I\) controls the deformation problem whose obstruction class is \(O_{\mathrm{full}}\).
- The identification of that class with a Maurer–Cartan obstruction to which the \(L_\infty\) morphism \(\sigma^k\) applies, so that the linear component annihilates it.

Theorem 8.2 of arXiv:2208.00694v2 is not one of these hypotheses. Its Lie-algebroid module hypothesis fails for the pinned residual, and that failure leaves Theorem 2.8 untouched.

No other source in this file is left as an unverified comparison. Question 11.4 of arXiv:2509.23403v2 is a question. The remaining sources are inapplicable for a hypothesis marked **fails** above, or were not accessed.
