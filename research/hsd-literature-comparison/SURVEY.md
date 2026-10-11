# Literature and comparison-theorem survey

Scope: published results that could give an all-order continuation, or a comparison or detection theorem, for the Horrocks–Mumford deformation of the triple \((X,E,\xi)\) pinned in `research/hsd/gate-ladder.md` at `d915eeab061f3dddebe1a1d3d7c80ca09609dcee` (branch `research/hsd-gate-ladder`, Section 4.1). The object of that gap is the full-sign star-algebroid residual \(O_{\mathrm{full}}=\mathrm{pr}_\chi O_2(a)\), \(\chi=\{1,2,3,4\}\), in the \(352\)-dimensional space \(\operatorname{Ext}^2(E,E)_\chi\).

Each hypothesis below is marked **holds**, **fails**, or **unverified**, with the reason taken from that pin or from a dimension the pin’s geometry determines. A strategy survives only when no hypothesis required for this residual is marked **fails**. An unverified comparison still survives as a candidate.

Sources were the arXiv TeX and, where a printed number is cited, the ar5iv rendering of the same source. A theorem number that does not appear in the source that was read is not used. Bloch’s own paper was not accessed.

The carrier route on \(\mathbf{P}^1\times\mathbf{P}^3\) is outside this survey. No value of \(O_2\) is computed here.

## 0. The pinned setup used as the checklist

From Section 1 of the pin.

- \(C\) is the smooth projective model of \(y^2=x^3-x\), and \(X=C^4\).
- \(H\) is the normalized Horrocks–Mumford bundle on \(\mathbf{P}^4\), \(f:X\to\mathbf{P}^4\) is the composite of the degree-two maps \(C\to\mathbf{P}^1\) with the symmetric quotient \((\mathbf{P}^1)^4\to\mathbf{P}^4\), and \(N=\mathcal{O}_X(\Theta)\) is the exterior product of the four origin line bundles. \(E=f^*H\otimes N\) is rank two and determinant-trivial, with \(c_2(E)=15\theta^2\) and \(\operatorname{ch}(E)=\exp(i\sqrt{15}\,\theta)+\exp(-i\sqrt{15}\,\theta)\).
- \(V_i\) is dual to \(dx_i/y_i\), \(\pi=V_1\wedge V_2+V_3\wedge V_4\), \(\Pi=\iota_\pi(\theta^2)/2\), and \(\xi=\pi+15\Pi\in HH^2(X)\). Under HKR, \(\pi\) is the Poisson summand and \(15\Pi\) is the scalar gerbe summand. Both have deck characters \(\{1,2\}\) and \(\{3,4\}\) for \(G=(\mathbf{Z}/2)^4\), \(y_i\mapsto -y_i\).
- \(\operatorname{ev}_E(\xi)=0\), with triple-overlap unit \(b=-15\Pi\).
- A second-order ambient extension is a star-algebroid through order \(h^2\) in the direction \(\xi\) (D’Agnolo–Schapira, Section 3, as cited by the pin). For a first-order module lift \(a\), the residual \(O_2(a)\) lies in \(\operatorname{Ext}^2(E,E)\), and \(O_{\mathrm{full}}\) is independent of that lift and of the second-order ambient acceleration. \(\dim\operatorname{Ext}^2(E,E)_\chi=352\).
- This is the star-algebroid module problem. The ordinary hull of \(E\) on fixed \(X\) is smooth of dimension \(87\), or \(83\) after determinant trivialization (Talpo–Vistoli, Proposition 6.36). Every class in \(\operatorname{Ext}^1(E,E)\) has deck weight \(0\) or \(1\), so Yoneda squares miss \(\chi\).
- The ordinary Buchweitz–Flenner map
  \[
  \sigma:\operatorname{Ext}^2(E,E)\longrightarrow H^2(\mathcal{O}_X)\oplus H^3(\Omega_X^1)\oplus H^4(\Omega_X^2)
  \]
  vanishes on the whole \(352\)-dimensional sector. Its rank there is \(0\). The \(\chi\)-part of the target is \(4\)-dimensional and sits in \(H^3(\Omega^1)\). Ordinary \(\sigma(O_{\mathrm{full}})=0\) is automatic for every full-sign class.
- \(15\Pi\) is an infinitesimal class in \(H^2(\mathcal{O}_X)\). The pin records no identification of it with a torsion Brauer class.
- The finite model at `add03476d9055aa00e1e00778eea6332cf8e01cc` (`research/hm/ext-model.md` on `research/hm-exact-ext`) gives \(\dim\operatorname{Ext}^j(E,E)=(1,87,7372,87,1)\) and, in weight \(4\), \(\dim\operatorname{Ext}^2=352\). That note states that no second-order obstruction claim follows from these dimensions alone.

Dimension used for surjectivity. \(T_X\) is trivial of rank \(4\), so
\[
\dim H^0(X,\wedge^2 T_X)=6,\qquad
\dim H^1(X,T_X)=4\cdot\dim H^1(\mathcal{O}_X)=16,\qquad
\dim H^2(X,\mathcal{O}_X)=6.
\]
The HKR source of \(\operatorname{ev}_E\) therefore has dimension \(28\). Since \(28<352\le 7372\), \(\operatorname{ev}_E:HH^2(X)\to\operatorname{Ext}^2(E,E)\) is not surjective, and its image cannot fill the full-sign sector.

## 1. Markman, arXiv:2502.03415

Source read: `250531.tex`, with printed numbers from the ar5iv rendering of the same text. Section 9, Section 8.3, and the two labels the gap statement asks for are treated first.

### 1.1. There is no Lemma 8.3.4 and no Remark 8.3.5

In the source that was read, the statements about kernels, surjectivity, and injectivity on the image sit in Section 8.2. Section 8.3 uses the numbers (8.3.4) and (8.3.5) as displayed equations.

- Equation (8.3.4) defines \(E:=\Phi(\pi_1^*F_1\otimes\pi_2^*F_2)\), the Orlov transform of a box product of secant sheaves.
- Equation (8.3.5) is the subspace \([\pi_1^*HT^2(X)\otimes\pi_2^*HT^0(X)]\oplus[\pi_1^*HT^0(X)\otimes\pi_2^*HT^2(X)]\).

arXiv:2509.23403 cites these criteria as [M2, Lemma 8.3.10] and [M2, Remark 8.3.11]. Those labels do not occur in the `250531.tex` / ar5iv text of 2502.03415. The statements that text does contain are Lemma 8.2.4 and Remark 8.2.5.

### 1.2. Lemma 8.2.4

Citation: arXiv:2502.03415, Lemma 8.2.4 (`lemma-criterion-for-semiregularity`).

Statement read: if \(\ker(ob_E)=\ker(\lfloor ch(E))\) inside \(HT^2(M)\) and \(ob_E\) is surjective, then \(E\) is semiregular. The proof identifies \(\sigma\) with the unique injective factor of \(\lfloor ch(E)\) through \(ob_E\), using commutativity of diagram (8.2.4), which the text attributes to Buchweitz–Flenner, arXiv:math/0606730, Proposition 6.2.1 and Corollary 6.3.2.

| Hypothesis | Mark | Reason |
|---|---|---|
| Input is a coherent sheaf on a smooth projective variety, with \(ob_E:HT^2\to\operatorname{Ext}^2\) | fails | The residual lives in the star-algebroid module category of the pin, Section 2. The ordinary sheaf \(E\) is a different deformation problem. |
| \(ob_E\) surjective | fails | Source dimension \(28\), target dimension \(7372\), and the full-sign sector already has dimension \(352\). |
| \(\ker(ob_E)=\ker(\lfloor ch(E))\) | unverified | No computation in this survey evaluates either kernel on \((X,E)\). |
| Conclusion used as a detection theorem for \(O_{\mathrm{full}}\) | fails | Semiregularity means injectivity of \(\sigma\). The pin records that ordinary \(\sigma\) is zero on the \(352\)-dimensional sector that contains \(O_{\mathrm{full}}\). |

### 1.3. Remark 8.2.5

Citation: arXiv:2502.03415, Remark 8.2.5 (`remark-semiregularity-map-restricts-as-an-injective-map-to-the-image-of-ob`).

Statement read: dropping surjectivity in Lemma 8.2.4, the semiregularity map still restricts to an injection on the image of \(ob_E\).

| Hypothesis | Mark | Reason |
|---|---|---|
| The remark, as a statement about \(\operatorname{im}(ob_E)\) for a coherent sheaf | holds | It is proved in the source from the same commutative diagram, and \(E\) is a coherent sheaf on the smooth fourfold \(X\). |
| \(O_{\mathrm{full}}\in\operatorname{im}(ob_E)=\operatorname{im}(\operatorname{ev}_E)\) | unverified | Dimension shows the image cannot fill the \(352\)-space. It does not show that the image misses \(\chi\). The translation-invariant HKR basis is spanned by wedges and tensors of the \(V_i\) and the classes of \(dx_i/y_i\), each of character \(\{i\}\). A product of two such characters has weight \(0\) or \(2\). That count is not executed in this repository, so \(HH^2(X)_\chi=0\) stays unverified. |
| Injectivity on a subspace that contains \(O_{\mathrm{full}}\) | fails | \(O_{\mathrm{full}}\) lies in the sector on which the pin records \(\sigma=0\). A nonzero class in that sector is not detected by injectivity of \(\sigma\). |

Remark 8.2.6 records that the hypotheses of Lemma 8.2.4 are invariant under a derived equivalence when the image is again a coherent sheaf, and that the target summand is \(H\Omega_{-2}\). The pin’s Section 2 records no identification of \(E\), or of \(O_{\mathrm{full}}\), with an object of \(D^b(X\times\widehat{X})\). That identification is unverified, and the surjectivity hypothesis of the lemma already fails for \(E\).

### 1.4. Lemma 8.3.1 and Section 9

Citation: arXiv:2502.03415, Lemma 8.3.1 (`lemma-kernel-of-ob-E-is-annihilator-of-ch_E`).

Statement read: for the secant box product, and for its Orlov transform (8.3.4), the kernel of the obstruction map equals the annihilator of the Chern character.

| Hypothesis | Mark | Reason |
|---|---|---|
| The sheaf is the secant box product of ideal sheaves of Abel–Jacobi curves, or the sheaf \(E\) of (8.3.4) | fails | The pinned \(E\) is the Horrocks–Mumford pullback \(f^*H\otimes N\) on the abelian fourfold \(X=C^4\). |

Citation: arXiv:2502.03415, Lemma 9.3.11 (`lemma-semiregularity-of-twisted-sheaf-B`), and Theorem 1.5.1 (`thm-algebraicity`).

Statement read: the \(\mu_{8d}\)-twisted reflexive sheaf \(\mathcal{B}\) on the quotient \(Y=(X\times\widehat{X})/\overline{G}\) is semiregular. The proof uses Remark 8.2.5, Lemma 8.3.1(2), and the equality of the image of \(ob_{\mathcal{E}}\) with the invariant summand \(\operatorname{Ext}^2(\mathcal{E},\mathcal{E})^{G^\vee}\). Theorem 1.5.1 states that the Hodge–Weil classes of polarized abelian sixfolds of Weil type, with complex multiplication by \(\mathbf{Q}(\sqrt{-d})\) and discriminant \(-1\), are algebraic. The introduction of the same source says the semiregularity proof is special to genus \(3\).

| Hypothesis | Mark | Reason |
|---|---|---|
| Genus-\(3\) Jacobian, cyclic groups of order \(d+1\), general-position orbits, quotient sixfold, band \(\mu_{8d}\) | fails | The pinned variety is a product of four elliptic curves, the sheaf is \(f^*H\otimes N\), and \(15\Pi\) is an infinitesimal class in \(H^2(\mathcal{O}_X)\). |
| Theorem 1.5.1 as a continuation of \((X,E,\xi)\) | fails | The theorem concludes algebraicity of Weil classes on a sixfold of Weil type. It does not evaluate a star-algebroid residual on the fourfold. |

### 1.5. Section 7, for the torsion reading

Citation: arXiv:2502.03415, Definition 7.3.5, Definition 7.3.8, Conjecture 7.3.9, and Section 7.4.

Statement read: Definition 7.3.5 is the Atiyah class of a \(\mu_r\)-twisted sheaf. Definition 7.3.8 says the twisted sheaf is semiregular when \(\sigma\) is injective. Conjecture 7.3.9 is the twisted analogue of Buchweitz–Flenner, Theorem 5.1: a semiregular \(\mu_r\)-twisted sheaf deforms over the locus where its Chern character stays of Hodge type. Section 7.4 proves the conjecture when the base is a family of abelian varieties and the Brauer class extends to a projective bundle. The text says the conjecture should follow from Pridham, Remark 2.26, and that the author cannot reconcile the terminology. The band in the conjecture is \(\mu_r\).

| Hypothesis | Mark | Reason |
|---|---|---|
| The class is a Čech cocycle with values in \(\mu_r\) | fails | The pin records \(15\Pi\in H^2(\mathcal{O}_X)\) as infinitesimal, with no proved identification with a torsion Brauer class. |
| \(\sigma\) injective on the obstruction space that contains the residual | fails | Ordinary \(\sigma\) vanishes on the \(352\)-dimensional sector. |

## 2. Markman, arXiv:2509.23403, Question 11.4

Source read: `251020.tex`, printed numbers from the ar5iv rendering. The user asked for version 2; the accessed source is the arXiv file carrying those section numbers.

### 2.1. Lemma 11.3

Citation: arXiv:2509.23403, Lemma 11.3.

Statement read: if \(\ker(\operatorname{ev}_E:HH^2(Y)\to\operatorname{Hom}(E,E[2]))\) equals the annihilator of \(ch(E)\) in \(HH^2(Y)\) and \(\operatorname{ev}_E\) is surjective, then \(E\) is semi-regular. The proof uses the HKR isomorphism and the diagram whose commutativity is attributed to arXiv:math/0606730, Proposition 6.2.1 and Corollary 6.3.2. The text introduces the lemma as the criterion of [M2, Remark 8.3.11] and labels the citation [M2, Lemma 8.3.10]. Those labels are the mismatch recorded in Section 1.1.

| Hypothesis | Mark | Reason |
|---|---|---|
| \(\operatorname{ev}_E\) surjective onto \(\operatorname{Ext}^2(E,E)\) | fails | Source dimension \(28\), target dimension \(7372\). |
| Kernel equals the annihilator of \(ch(E)\) | unverified | Not computed for the pinned \(E\). |
| The sheaf is the secant sheaf of Proposition 11.1 | fails | Lemma 11.3 is stated generally, and the application in this section is the secant sheaf on a Jacobian, which is not \(f^*H\otimes N\). |

### 2.2. Question 11.4

Citation: arXiv:2509.23403, Question 11.4.

Statement read, in full: “Is the surjectivity of \(ev_E\) needed in Lemma 11.3? Does the Semi-regularity Theorem 2.1 hold under the weaker assumption that \(\sigma_E\) restricts to the image of \(ev_E\) as an injective map (considering also twisted sheaves as we did in Section 2)?”

This is a question. It is not a theorem, so it supplies no continuation. The same section says the paper avoids the question by descending to a quotient on which surjectivity holds (Proposition 11.5). Section 12 says an affirmative answer would be relevant to dimension at least \(8\) and to CM fields with \([K:\mathbf{Q}]>2\), and that the secant examples of arXiv:2502.03415, Examples 8.2.3 and 8.2.4, are yet to be checked.

| Hypothesis | Mark | Reason |
|---|---|---|
| A published affirmative answer | fails | The accessed text leaves the question open. |
| The weaker package, if it were a theorem, applied to \(O_{\mathrm{full}}\) | fails | Detection still requires the class to lie in \(\operatorname{im}(\operatorname{ev}_E)\) and to be seen by an injective \(\sigma\). The class lies in the sector where the pin records \(\sigma=0\). Membership in the image is unverified, and either outcome blocks detection: inside the image, injectivity fails; outside the image, the package does not see the class. |

### 2.3. Proposition 11.5 and Theorem 2.1

Citation: arXiv:2509.23403, Proposition 11.5 and Theorem 2.1.

Proposition 11.5 states that the descended sheaf \(\overline{\mathcal{E}}\) on the quotient abelian variety \(A=(X\times\widehat{X})/\overline{G}\) is semi-regular. The sketch uses Lemma 11.3 for ideal sheaves of curves and their box products. Theorem 2.1 is the semi-regularity theorem of that paper, applied in Section 11.5 to conclude algebraicity of Weil classes.

| Hypothesis | Mark | Reason |
|---|---|---|
| The object is \(\overline{\mathcal{E}}\) on that quotient | fails | The pinned object is the star-algebroid residual of \(f^*H\otimes N\). |

## 3. Pridham, arXiv:1208.3111

Source read: `semireg2.tex`, printed numbers from the ar5iv rendering. Title in the source: “Semiregularity as a consequence of Goodwillie’s theorem”.

### 3.1. The introduction theorem

The introduction states an unnumbered theorem (`theorem*` in the source). Statement read: for a local Artinian \(\mathbf{C}\)-algebra, a smooth morphism of Artin stacks, a square-zero ideal, and a perfect complex, the obstruction \(o(\mathscr{F})\) maps to \(0\) under the composite into the truncated de Rham complex if and only if the horizontal lift of \(\operatorname{ch}_p\) stays in \(F^p\).

| Hypothesis | Mark | Reason |
|---|---|---|
| The base extension is a square-zero extension of a commutative Artinian algebra, and the stack morphism is smooth | fails | The pinned deformation varies the product by the star-algebroid terms of order \(h\) and \(h^2\). Section 2 of the same paper declares that from that point all rings are commutative. |
| The obstruction is the ordinary module obstruction of \(E\) on a varying commutative base | fails | The pin places \(O_{\mathrm{full}}\) in the star-algebroid residual, and records that the ordinary hull is already smooth. |

### 3.2. Corollary 1.20 and Remark 1.21

Citation: arXiv:1208.3111, Corollary 1.20 and Remark 1.21.

Statement read. If \(\mathcal{N}\) is a geometric noncommutative scheme in Orlov’s sense (an admissible dg subcategory of \(\mathrm{per}_{dg}(\mathcal{O}_Y)\) for \(Y\) smooth and proper over a field of characteristic \(0\)), then for a square-zero extension \(e:A\to B\) of commutative \(k\)-algebras with kernel \(I\), and a perfect \(\mathcal{N}\otimes_k B\)-complex \(\mathscr{F}\), the obstruction to lifting \(\mathscr{F}\) to a perfect \(\mathcal{N}\otimes_k A\)-complex lies in the kernel of the Lefschetz map
\[
\mathcal{L}:\operatorname{Ext}^2(\mathscr{F},\mathscr{F}\otimes^{\mathbf{L}} I)\longrightarrow HH_{-2}(\mathcal{N})\otimes_k I.
\]
Remark 1.21: until the last step, \(\mathcal{N}\) need only be a smooth proper dg subcategory of \(\mathrm{per}_{dg}(\mathcal{O}_Y)\) for \(Y\) quasi-compact and semi-separated, and then \(\mathsf{I}\mathcal{L}(o_e(\mathscr{F}))=0\). The same remark allows \(\mathcal{O}_Y\) to be replaced by a presheaf \(\mathscr{A}\) of simplicial associative \(R\)-algebras on affine opens whose \(\pi_*\mathscr{A}\) admits a quasi-coherent \(\mathcal{O}_Y\)-algebra structure. The examples named are the structure hypersheaf of a derived scheme with underived truncation \(Y\), and any quasi-coherent simplicial associative algebra on that derived scheme.

| Hypothesis | Mark | Reason |
|---|---|---|
| Square-zero extension of commutative \(k\)-algebras, with \(\mathcal{N}\) held fixed | unverified | Corollary 1.20 deforms the module and holds the algebra fixed. The pinned star product varies the product. Remark 1.21 would apply if the product truncated at order \(h^2\) can be presented as one such fixed presheaf and \(O_{\mathrm{full}}\) is the module-lifting obstruction over that fixed algebra. Neither presentation nor identification is in the pin. |
| \(\mathcal{N}\) admissible in \(\mathrm{per}_{dg}(\mathcal{O}_Y)\), or the weaker presheaf of Remark 1.21 | unverified | A star product on \(X\) is an associative deformation of \(\mathcal{O}_X\). The remark’s simplicial and quasi-coherent hypotheses for that truncation are not checked. |
| The Lefschetz map on this class is a new constraint | unverified | The pin states that vanishing of ordinary \(\sigma\) on the full-sign sector does not identify the relative cyclic map of Corollary 1.20, and does not evaluate that map on the obstruction. If the two maps agree on \(O_{\mathrm{full}}\), the corollary’s conclusion is the automatic vanishing \(\sigma(O_{\mathrm{full}})=0\). |

This is the only reading in the present survey with no hypothesis marked **fails**. It survives as an unverified comparison. The commutative corollaries below do not.

### 3.3. Corollaries 2.24 and 2.25, Remark 2.26

Citation: arXiv:1208.3111, Corollary 2.24, Corollary 2.25, Remark 2.26.

Corollary 2.24: for a morphism of derived stacks over \(\mathbf{Q}\) and a nilpotent closed immersion, the Goodwillie–Jones Chern character induces an Abel–Jacobi map, and for a square-zero ideal the image of that map is given by the semiregularity component \(\sigma_{p-1}\). Corollary 2.25: for a local Artinian simplicial \(\mathbf{C}\)-algebra and a derived Artin stack whose truncation is locally of finite type, \(\operatorname{ch}_p\) stays in \(F^p\) if and only if the image of \(\mathcal{L}_{p-1}(o_e(\mathscr{F}))\) in the truncated derived de Rham cohomology vanishes. The paragraph before Corollary 2.25 says this establishes the conjectures of Buchweitz–Flenner and hence those of Bloch, for \(X\) a smooth proper scheme over a local Artinian \(\mathbf{C}\)-algebra. Remark 2.26 extends both corollaries to \(\mu_r\)-twisted perfect complexes by replacing \(X\) with the \(\mu_r\)-gerbe. The reason given is that \(\mu_r\) is étale and reductive over \(\mathbf{Q}\).

| Hypothesis | Mark | Reason |
|---|---|---|
| Commutative (derived) base, perfect complex of the structure sheaf or of a commutative derived scheme | fails | Section 2 restricts to commutative rings. The pinned product is the star product in the direction \(\xi\). |
| Band \(\mu_r\), Remark 2.26 | fails | \(15\Pi\) is infinitesimal in \(H^2(\mathcal{O}_X)\), not a class in \(H^2_{\mathrm{\acute{e}t}}(X,\mu_r)\). |
| Constant family, so the Hodge condition is automatic and the obstruction maps to \(0\) | fails | That conclusion is the ordinary annihilation. The pin records it for every full-sign class and records that it does not evaluate \(O_{\mathrm{full}}\). |

## 4. Buchweitz–Flenner, arXiv:math/9912245

Source read: the December 31, 1999 arXiv TeX, printed numbers from the ar5iv rendering.

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
| \(I\)-semiregularity on a space containing \(O_{\mathrm{full}}\) | fails | Ordinary \(\sigma\) has kernel equal to the whole \(352\)-dimensional sector. |
| The deformation is a deformation of the manifold with the sheaf on the fibres | fails | The pinned deformation is a star-algebroid on a fixed fourfold. |

### 4.3. Theorems 7.2 and 7.3

Theorem 7.2, as read: \(X\) proper and smooth over \(\Sigma\), special fibre bimeromorphic to a Kähler manifold, \(\mathscr{F}_0\) a coherent module on the special fibre, \(S\) the base of a semiuniversal deformation of \(\mathscr{F}_0\). Then \(\dim S\ge\dim\operatorname{Ext}^1-\dim\ker\sigma\), and if \(\sigma\) is injective then \(S\) is smooth over a closed subspace of the formal base. Theorem 7.3, as read: on a fixed complex space, a coherent module of locally finite projective dimension with finite-dimensional \(\operatorname{Ext}^1\) satisfies the same dimension inequality, and if \(\sigma\) is injective then the semiuniversal base is smooth.

| Hypothesis | Mark | Reason |
|---|---|---|
| The functor is the ordinary deformation functor of the coherent sheaf | fails | The pin’s ordinary hull is already smooth of dimension \(87\). The residual \(O_{\mathrm{full}}\) is the star-algebroid residual. |
| Injectivity of \(\sigma\) on the \(352\)-space | fails | The kernel is the whole sector. |

The introduction attributes to Bloch the construction, for an lci subscheme \(Z\subset X\) of codimension \(q\), of
\[
\tau:H^1(Z,\mathcal{N}_{Z/X})\to H^{q+1}(X,\Omega_X^{q-1}),
\]
and the conclusion that injectivity of \(\tau\) makes \([Z]\) a smooth point of the Hilbert scheme. That attribution is Buchweitz–Flenner’s. Bloch’s paper itself is recorded in Section 6 as not accessed.

### 4.4. Section 8 and the Hochschild factorization, arXiv:math/0606730

Citation: arXiv:math/9912245, Section 8.1 and Proposition 8.2. For an lci \(Z\subset X\) of codimension \(q\), the text reconstructs a map \(\tau_B:H^k(Z,\mathcal{N}_{Z/X})\to H^{q+k}(X,\Omega^{q-1})\) and states that Bloch’s semiregularity map is the case \(k=1\). Proposition 8.2 states that \(\tau_B\) and the corresponding component of the Buchweitz–Flenner map coincide.

| Hypothesis | Mark | Reason |
|---|---|---|
| The object is an lci subscheme | fails | \(E\) is a rank-two vector bundle. |

Citation: arXiv:math/0606730, Proposition 6.2.1, in the subsection “The semiregularity map on Hochschild cohomology”. Statement read: for a perfect complex, the map \(\sigma^H(f)=\operatorname{Tr}((f\otimes\mathrm{id})\circ AH_{\mathscr{F}})\) into Hochschild homology makes the diagram with the ordinary semiregularity map and the HKR map commute. Corollary 6.3.2 (`AHcom`) states that \(\sigma^H\) also commutes with the action of Hochschild cohomology through the Chern–Hochschild character \(\operatorname{ch}^H=\sigma^H(\mathrm{id})\). Markman’s Lemma 8.2.4 and Lemma 11.3 of arXiv:2509.23403 attribute their first-order diagrams to Proposition 6.2.1 and Corollary 6.3.2 of this paper.

| Hypothesis | Mark | Reason |
|---|---|---|
| Perfect complex on a morphism of spaces | holds | \(E\) is a vector bundle on \(X\). |
| The proposition continues a first-order \(HH^2\) class to order \(h^2\) | fails | Proposition 6.2.1 identifies the linear semiregularity map with a Hochschild-homology contraction. Corollary 6.3.2 is the same linearity for the Chern–Hochschild character. Neither statement evaluates a second-order residual. |

## 5. Later all-order and comparison results that were read

These are results cited by, or citing, the papers above on the passage from a first-order Hochschild or semiregularity class to an obstruction in every order.

### 5.1. Perry, arXiv:2604.00511

Source read: `semiregularity.tex`. Printed numbers below are the shared `amsthm` counter in that source. The abstract says the paper generalizes Buchweitz–Flenner to noncommutative varieties with group actions, applies to twisted derived categories, and answers a question of Markman. The question named in the introduction is Conjecture 7.3.9 of arXiv:2502.03415, not Question 11.4 of arXiv:2509.23403.

Definition 2.4: \(E\) is semiregular when \(\sigma_E^2:\operatorname{Ext}^2(E,E)\to HH_{-2}(\mathcal{C})\) is injective. The same section defines \(G\)-semiregular (injective on the invariant subspace) and weakly \(G\)-semiregular (the image of a semiregular object of \(\mathcal{C}^G\)). Lemma 2.7: if \(|G|\) is invertible, \(G\)-semiregular implies weakly \(G\)-semiregular.

Theorem 1.1 (`theorem-semiregularity-intro`): smooth proper family of complex varieties, semiregular perfect complex with \(\operatorname{Ext}^{<0}=0\), and an algebraic class \(B_0\in H^2(X_0,\mathbf{Q}(1))\) such that \(\exp(B_0)\cdot\operatorname{ch}(E_0)\) stays Hodge. Then \(E_0\) deforms as a twisted perfect complex over an étale neighbourhood, and the class stays algebraic.

Theorem 1.2: the same conclusion for a family of abelian varieties, a finite group \(G\subset X_0\times X_0^\vee\) acting by translations and tensoring, and a weakly \(G\)-semiregular perfect complex.

Theorem 6.1: \(\mathcal{C}\) a smooth proper \(S\)-linear category of geometric origin, \(v\) a section of \(K^{\mathrm{top}}[0](\mathcal{C}/S)\), and \(E_0\) a gluable semiregular object of class \(v_0\). Then \(E_0\) deforms over an étale neighbourhood and \(v\) stays algebraic. The introduction defines geometric origin as a semiorthogonal component of a smooth proper \(S\)-scheme. Theorem 6.3 is the weakly \(G\)-semiregular extension, and it requires the invariant category to be of geometric origin as well.

| Hypothesis | Mark | Reason |
|---|---|---|
| Semiregularity, or weak \(G\)-semiregularity, of the object whose \(\operatorname{Ext}^2\) contains \(O_{\mathrm{full}}\) | fails | Ordinary \(\sigma\) vanishes on the \(352\)-dimensional sector. The deck group in the pin is \((\mathbf{Z}/2)^4\) acting on \(X\), and the full-sign sector is the sign character, not a subspace on which \(\sigma\) is injective. |
| Geometric origin of the star-algebroid module category | fails | The definition requires a semiorthogonal component of a smooth proper scheme. The pinned category is modules over a star product. |
| Algebraic class \(B_0\in H^2(X,\mathbf{Q}(1))\) and a Brauer class on a family of varieties | fails | \(15\Pi\) is infinitesimal in \(H^2(\mathcal{O}_X)\). The deformation in Theorem 1.1 is a twisted perfect complex on a family of varieties. |

### 5.2. Bandiera–Lepri–Manetti, arXiv:2208.00694

Source read: the arXiv TeX. The shared counter gives the printed numbers below.

Theorem 4.4 (`thm.Deformazioni`): for a locally free module with a flat \(\mathcal{L}\)-connection on a smooth separated finite-type scheme over a field of characteristic \(0\), the Thom–Whitney totalization of \(\Omega^*(\mathcal{L},\mathcal{H}\mathrm{om}(E,E))\) controls the infinitesimal deformations. \(HH^1\) is the space of first-order deformations and \(HH^2\) is an obstruction space.

Theorem 8.2, in the section “Semiregularity maps and obstructions”: for a Lie pair \((\mathcal{L},\mathcal{A})\) and a locally free \(\mathcal{A}\)-module \((E,\nabla^{\mathcal{A}})\), each composite
\[
i_k\tau_k:HH^2(\mathcal{A};\operatorname{End}(E))\longrightarrow HH^{2+2k}\bigl(X,\Omega^*(\mathcal{L})/\mathcal{G}_{k+1}\bigr)
\]
annihilates every obstruction to deformations as an \(\mathcal{A}\)-module. If the Leray spectral sequence degenerates at \(E_1\), each semiregularity component annihilates obstructions.

| Hypothesis | Mark | Reason |
|---|---|---|
| The residual is the obstruction to deforming a locally free module with a flat connection along a Lie pair | fails | The pin describes the residual as the order-\(h^2\) associative descent residual of a star-algebroid, with terms from the star product. A Lie-algebroid module is a different category in that description. |
| Equality of that Lie-algebroid obstruction class with \(O_{\mathrm{full}}\) | unverified | The pin leaves this comparison open. The failed object hypothesis already removes the theorem from the surviving list. The unverified equality would be a new identification, which this theorem does not supply. |

### 5.3. Lepri, arXiv:2104.12658

Source read: the arXiv TeX. Title: “Cyclic forms on DG-Lie algebroids and semiregularity”.

The introduction’s first theorem is Corollary 3.16 (`cor.fasci2`): a coherent sheaf with a finite locally free resolution on a smooth separated finite-type scheme over a field of characteristic \(0\) has every obstruction in the kernel of \(\tau_1:\operatorname{Ext}^2\to\mathbb{H}^2(X,\Omega^{\le 1}[2])\). If Hodge-to-de Rham degenerates at \(E_1\), every obstruction lies in the kernel of \(\sigma_1(a)=-\operatorname{Tr}(\operatorname{At}(\mathscr{F})\circ a)\), with target \(H^3(\Omega^1)\).

The introduction’s second theorem is Corollary 4.12 (`cor.principali`): for a principal bundle with a \(d_{\mathrm{Tot}}\)-closed cyclic form, every obstruction lies in the kernel of \(f_1:H^2(X,\mathfrak{ad})\to\mathbb{H}^2(X,\Omega^{\le 1}[2])\).

| Hypothesis | Mark | Reason |
|---|---|---|
| Coherent sheaf on a fixed smooth scheme, or a principal bundle | fails | The residual is a star-algebroid module residual. The kernel statement for the ordinary sheaf is the annihilation the pin already records on the full-sign sector. |

### 5.4. Lepri, arXiv:2102.05016

Source read: the arXiv TeX. Title: “Connections and \(L_\infty\) liftings of semiregularity maps”.

The introduction’s two theorems are identified there with Corollary `cor.thm.main2` and Corollary `cor.main2`. Statement read: a connection of type \((1,0)\) on a finite locally free resolution lifts \(\tau_1:\operatorname{Ext}^*\to\mathbb{H}^*(X,\Omega^{\le 1}[2])\) to an \(L_\infty\) morphism, and every obstruction to deforming the coherent sheaf lies in \(\ker\tau_1\). Under Hodge-to-de Rham degeneration at \(E_1\), the obstruction lies in the kernel of \(\sigma_1(a)=-\operatorname{Tr}(\operatorname{At}(\mathscr{F})\circ a)\).

| Hypothesis | Mark | Reason |
|---|---|---|
| Coherent sheaf on a fixed complex manifold | fails | Same category mismatch as Corollary 3.16 of arXiv:2104.12658. The \(L_\infty\) lifting is a lifting of the ordinary first-order map. |

### 5.5. Bandiera–Lepri–Manetti, arXiv:2111.12985

Source read: the arXiv TeX. Theorem 2.8 (`thm.main1`, also labeled as Corollary `cor.semireg`): for a curved Lie ideal of a curved DG-algebra, each linear semiregularity component \(\sigma_1^k\) is the linear part of an \(L_\infty\) morphism into the quotient by the commutators plus the next power of the ideal.

| Hypothesis | Mark | Reason |
|---|---|---|
| An algebraic curved DG-pair whose obstruction class is \(O_{\mathrm{full}}\) | unverified | The theorem is the algebraic machine used by arXiv:2208.00694. It does not name \((X,E,\xi)\). |
| The curved ideal is the star-product ideal of the pinned algebroid | fails | No such identification is stated, and the geometric theorem that applies the machine, Theorem 8.2 of arXiv:2208.00694, has the Lie-module hypothesis marked fails above. |

### 5.6. Iacono–Manetti, arXiv:1112.0425

Source read: the arXiv TeX. The unnumbered Main Theorem (`theorems` in the source): \(X\) smooth over an algebraically closed field of characteristic \(0\), \(Z\subset X\) closed of codimension \(p\), and the setup hypothesis that on a Zariski open \(U\) the subscheme \(Z\) is the zero locus of a section of a rank-\(p\) bundle. Then the composition of the semiregularity map with truncation,
\[
H^1(Z,N_{Z|X})\to H^{p+1}(X,\Omega_X^{p-1})\to\mathbb{H}^{2p}(X,\Omega_X^{<p}),
\]
annihilates every embedded obstruction. The main corollary says that if Hodge-to-de Rham degenerates at \(E_1\), the untruncated map does too.

| Hypothesis | Mark | Reason |
|---|---|---|
| Embedded lci deformation of a subscheme | fails | The pinned object is a rank-two bundle and a star-algebroid residual. |

### 5.7. Iacono, arXiv:0707.2454

Source read: the arXiv TeX. Title: “A semiregularity map annihilating obstructions to deforming holomorphic maps”. The unnumbered introduction theorem is Corollary 4.14 (`coroll semiregolari-ostruzion`). Statement read: for a holomorphic map \(f:X\to Y\) of compact Kähler manifolds, with \(p=\dim Y-\dim X\), the obstruction space to deformations of \(f\) with \(Y\) fixed lies in the kernel of
\[
\sigma:H^2(C^\cdot_{f_*})\to H^{p+1}(Y,\Omega_Y^{p-1}).
\]
The introduction says that for an inclusion this map reduces to Bloch’s semiregularity map.

| Hypothesis | Mark | Reason |
|---|---|---|
| Deformation of a holomorphic map of compact Kähler manifolds | fails | The pinned deformation is a star-algebroid module on a fixed fourfold. |

### 5.8. Nishinou, arXiv:2009.01651

Source read: the arXiv TeX. The counter is shared and global. The first three theorems are Theorem 1 (`thm:1`), Theorem 2 (`thm:2`), and Theorem 3 (`thm:CB`).

Theorem 1, as read: \(\varphi_0:C_0\to X_0\) is an immersion of a compact reduced curve, or of a smooth divisor when \(\dim X_0>2\), into the special fibre of a deformation of a compact Kähler manifold of dimension at least \(2\), the image is a local complete intersection, and \(\varphi_0\) is semiregular. If the cycle class stays Hodge, the map deforms to other fibres. Theorem 2 relates classical semiregularity of a normal-crossings image to surjectivity onto the infinitesimal normal sheaf. Theorem 3 is the nodal Cayley–Bacharach form on a surface.

| Hypothesis | Mark | Reason |
|---|---|---|
| The object is a semiregular divisor map | fails | \(E\) is a rank-two bundle, and the obstruction in view is \(O_{\mathrm{full}}\). |

### 5.9. Chang, arXiv:0808.0988

Source read: the arXiv TeX. Title in the source: “Derived Kodaira Spencer map and derived Cosection lemma”. The section “Semiregularity” contains no numbered theorem. The argument, as read: for a smooth compact Kähler manifold with an étale locally universal family, obstructions to deformations of the manifold lie in the kernel of contraction
\[
H^2(X,T_X)\to\bigoplus_i\operatorname{Hom}(H^{p,q},H^{p-1,q+2}).
\]
The text calls this Kodaira’s principle that ambient cohomology annihilates obstructions.

| Hypothesis | Mark | Reason |
|---|---|---|
| The obstruction space is \(H^2(X,T_X)\) for a deformation of the manifold | fails | \(O_{\mathrm{full}}\) lies in \(\operatorname{Ext}^2(E,E)_\chi\). The ordinary deformations of \(X\) are the \(H^1(T_X)\) summand of \(HH^2\), which is a different space. |

## 6. Bloch’s semiregularity map

not accessed

The article text of S. Bloch, “Semi-regularity and deRham cohomology”, Inventiones Mathematicae 17 (1972), was not obtained. The publisher response and the EuDML landing page do not contain the article. No theorem number from that paper is stated here.

What Buchweitz–Flenner, arXiv:math/9912245, Section 8.1 and the introduction, attribute to Bloch is recorded in Section 4.3 above and is their attribution. The attributed map takes values on \(H^1(Z,\mathcal{N}_{Z/X})\) for an lci subscheme. The pinned object is not an lci subscheme, so that attributed statement does not apply. This is a check of the secondary attribution only.

## 7. What was not given a continuation theorem

The pin cites D’Agnolo–Schapira, math/0506064, Section 3, as the descent language of the star-algebroid, and the finite-model notes cite Lowen, arXiv:0707.2602, for the characteristic morphism that evaluates a Hochschild class on an object. Those roles are first-order or definitional. Numbered all-order continuation theorems from Yekutieli, arXiv:0905.0488, from BGNT, arXiv:0810.0030, and from Lowen, arXiv:0707.2602, were not extracted in this survey. No theorem number from those three papers is used. Their HTML texts were not given a line-by-line theorem check here; for any claim that one of them continues \(O_{\mathrm{full}}\) to all orders, the status of that claim in this file is: not accessed.

## 8. Ranked strategies that survive

One strategy survives. Every injectivity theorem above fails on the \(352\)-dimensional sector, because the pin records that ordinary \(\sigma\) vanishes there and \(O_{\mathrm{full}}\) is a class in that sector. Every theorem whose object is an ordinary sheaf, an lci subscheme, a \(\mu_r\)-twisted sheaf, a Lie-algebroid module, or a semiorthogonal component of a scheme fails the category hypothesis in Section 2 of the pin. Question 11.4 is not a theorem.

### Rank 1. Pridham, Remark 1.21, with the kernel conclusion of Corollary 1.20

The reading that survives: truncate the star product at order \(h^2\), hold that associative algebra fixed, present it as a presheaf allowed by Remark 1.21, and ask whether \(O_{\mathrm{full}}\) is the module-lifting obstruction \(o_e(\mathscr{F})\) of Corollary 1.20. The Lefschetz map of that corollary is then a constraint only if it is not already the ordinary \(\sigma\) of the pin. Both the presentation and the identification are unverified. No hypothesis of this reading was marked fails.

Smallest computation in this repository. Use the authored residual in `research/hm/second-order-algebroid.md` at `c8aec970fd65a105f39f4e8aeb8a17f0f0053f89` (branch `research/hm-algebroid-equations`), Section 5, and the finite RHom model certified by `research/hm/ext-character-certificate.js` together with `research/hm/ext-model.md` at `add03476d9055aa00e1e00778eea6332cf8e01cc`. Project only the algebra-variation summands of that residual — the summands that contain \(\mu_2\), the algebroid correction \(T_{ij}\), or the square of the triple unit \(b_{ijk}\) — into that finite model, and test whether their class in \(\operatorname{Ext}^2(E,E)_\chi\) is zero for the differential of the product held fixed at order \(h\). A nonzero class means the residual changes the algebra at order \(h^2\), so it is not the module obstruction of a fixed algebra and Remark 1.21 does not apply. A zero class leaves the fixed-algebra reading open and does not evaluate the full residual. This projection is not a numerical evaluation of \(O_2\). The algebroid note already records that the projected second-order residual has not been instantiated.

No second strategy survives the hypothesis check. The comparison that would have to be reopened before Bandiera–Lepri–Manetti, Theorem 8.2, could be reconsidered is the equality of \(O_{\mathrm{full}}\) with a Lie-algebroid obstruction class. The pin’s description of the residual marks the Lie-module hypothesis fails, so that equality is not a surviving strategy. The character count that would decide whether \(HH^2(X)_\chi=0\), using the deck action already present in `research/hm/ext-character-certificate.js`, decides only which failure mode applies to Remark 8.2.5. It does not restore that remark: a class in the image meets a vanishing \(\sigma\), and a class outside the image is invisible to the remark.
