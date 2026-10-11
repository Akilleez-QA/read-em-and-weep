# Theorem-and-map audit and gate ladder

Status: an audit of published theorems against two deformation problems. No value of the ambient second-order class is computed here. Nothing in this note promotes either route.

For the fixed chosen carrier, the central defect has independently certified length \(\operatorname{length}_B(Q)=12\). The certificates are PR #1, comment [6104798062](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6104798062), and comment [6104803214](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6104803214). The second is an independent SymPy Groebner-basis reproduction of the same five-relation module. As of the earlier checkpoint, before 6104798062, that length was uncomputed. This note records those certificates and does not recompute the length.

The certificate marks the global vector-bundle extension gate (G2) **EXCLUDED** for this carrier only. The formal continuation (G1) of this same carrier stays passed and retained. Other formal-lift and carrier choices stay **OPEN**. The original theorem, the central conditions for other carriers, and the Horrocks–Mumford second-order obstruction computation are not settled by this result.

Semiregularity, a torsion twist, and an eightfold transform are sufficient strategies, not gates every continuation must pass. The carrier weight, frame covariance, homogeneous homotopies, and confinement argument are supplied, pending artifact review. On the torsion-free central fibre, \(Q=0\) is what establishes central reflexivity; depth at least \(3\) is then Stacks Project, Lemma 0BUW, and freeness is the isolated self-dual stalk lemma. The comparison that remains open is model-specific: this varying star-algebroid and its actual second-order obstruction.

The two routes stay distinct. The Horrocks–Mumford route is a module over a star-algebroid on an abelian fourfold. The carrier-continuation route is a rank-four construction on \(\mathbf{P}^1\times\mathbf{P}^3\).

## 1. The ambient object

Let \(C\) be the smooth projective model of \(y^2=x^3-x\), and let \(X=C^4\). Let \(H\) be the normalized Horrocks–Mumford bundle on \(\mathbf{P}^4\), let \(f:X\to\mathbf{P}^4\) be the composite of the product of the degree-two maps \(C\to\mathbf{P}^1\) with the symmetric quotient \((\mathbf{P}^1)^4\to\mathbf{P}^4\), and let \(N=\mathcal{O}_X(\Theta)\) be the exterior product of the four origin line bundles. The carrier sheaf is
\[
E=f^*H\otimes N.
\]
It is rank two, determinant-trivial, with \(c_2(E)=15\theta^2\) and
\[
\operatorname{ch}(E)=\exp(i\sqrt{15}\,\theta)+\exp(-i\sqrt{15}\,\theta).
\]
This Chern character sees the field \(\mathbf{Q}(\sqrt{-15})\) only.

Let \(V_i\) be the translation-invariant vector field on the \(i\)-th factor dual to \(dx_i/y_i\), and set
\[
\pi=V_1\wedge V_2+V_3\wedge V_4,\qquad
\Pi=\iota_\pi(\theta^2)/2,\qquad
\xi=\pi+15\Pi\in HH^2(X).
\]
Under the Hochschild–Kostant–Rosenberg decomposition,
\[
HH^2(X)=H^0(X,\wedge^2 T_X)\oplus H^1(X,T_X)\oplus H^2(X,\mathcal{O}_X),
\]
the class \(\pi\) is Poisson and \(15\Pi\) is a scalar gerbe class. Both summands have deck characters \(\{1,2\}\) and \(\{3,4\}\) for the action of \(G=(\mathbf{Z}/2)^4\) by \(y_i\mapsto -y_i\).

The first-order module identity is \(\operatorname{ev}_E(\xi)=0\): the trace-free contraction of the Atiyah class of \(E\) against \(\pi\) equals \(-15\Pi\cdot\operatorname{id}_E\), and the gerbe summand cancels it. In the star-algebroid presentation this is the choice \(b=-15\Pi\) of the triple-overlap unit.

A second-order ambient extension is a star-algebroid on \(X\) through order \(h^2\) in the direction \(\xi\): an associative star product whose first bidifferential is \(\tfrac12\pi\), together with algebra isomorphisms and triple units satisfying the descent equations of D'Agnolo–Schapira, Section 3. For a first-order module lift \(a\) of \(E\), the resulting residual is a class
\[
O_2(a)\in\operatorname{Ext}^2(E,E).
\]
Its full-sign projection
\[
O_{\mathrm{full}}=\operatorname{pr}_\chi O_2(a),\qquad \chi=\{1,2,3,4\},
\]
is independent of the choice of first-order module lift and of the choice of second-order ambient acceleration. The character table gives
\[
\dim\operatorname{Ext}^2(E,E)_\chi=352.
\]
That \(352\)-dimensional space is the ambient second-order problem. It is not the ordinary deformation problem of \(E\) as an \(\mathcal{O}_X\)-module on the fixed fourfold.

### What the ambient problem is not

The ordinary coherent-sheaf deformation category of \(E\) on fixed \(X\) has a smooth hull of dimension \(87\), or dimension \(83\) after a determinant trivialization. The input is an actual smooth family with injective Kodaira–Spencer map, and the hull criterion is Talpo–Vistoli, Proposition 6.36. Every class in \(\operatorname{Ext}^1(E,E)\) has deck weight \(0\) or \(1\), so every Yoneda square has full-sign component zero. Ordinary semiregularity is not needed for that conclusion, and a vanishing in the ordinary category does not evaluate \(O_{\mathrm{full}}\).

The deck character of the canonical volume is \(\chi\). Serre duality therefore identifies the transpose of the first component of the ordinary semiregularity map, on the \(\chi\)-sector, with contraction against \(H^1(X,T_X)^G\). That invariant space is spanned by the four diagonal product-elliptic directions. Each of those directions extends \(E\), once it is realized by a local versal pointed elliptic family rather than by the coarse \(j\)-line. Consequently the ordinary Buchweitz–Flenner map
\[
\sigma:\operatorname{Ext}^2(E,E)\longrightarrow H^2(X,\mathcal{O}_X)\oplus H^3(X,\Omega_X^1)\oplus H^4(X,\Omega_X^2)
\]
vanishes on the whole \(352\)-dimensional sector. Its rank there is \(0\) and its kernel there is the whole sector. The \(\chi\)-part of the target is \(4\)-dimensional and sits in \(H^3(\Omega^1)\); the other two summands have no full-sign classes. Ordinary \(\sigma(O_{\mathrm{full}})=0\) is automatic for every full-sign class. It is a convention check, not an injectivity gate, and it does not determine \(O_{\mathrm{full}}\).

## 2. Deformation category

Four categories are in view. Only one of them contains \(O_{\mathrm{full}}\).

| Category | Object | Obstruction space | Does it contain \(O_{\mathrm{full}}\)? |
|---|---|---|---|
| Ordinary sheaf | \(E\) on fixed \(X\) | \(\operatorname{Ext}^2(E,E)\), ordinary Yoneda | No. The hull is smooth, and Yoneda squares miss \(\chi\). |
| \(\mu_r\)-twisted / finite gerbe | a sheaf twisted by a Čech class in \(H^2(X,\mu_r)\) | the same Ext group of the twisted sheaf | No identification is proved. The class \(15\Pi\) is an infinitesimal class in \(H^2(\mathcal{O}_X)\), not a torsion Brauer class. |
| Star-algebroid module | a module over a star-algebroid extending \(\xi\) | the residual \(C_2\) of the module descent equation, pushed to \(\operatorname{Ext}^2(E,E)\) | Yes. This is the ambient problem. |
| Eightfold transform | an object of \(D^b(X\times\widehat{X})\) obtained by an Orlov equivalence from secant data on \(X\) | the obstruction theory of that object | No identification with \(E\), or with \(O_{\mathrm{full}}\), is proved. Dimension \(8\) is the dimension of \(X\times\widehat{X}\). |

The carrier-continuation route is a fifth category, on a different variety: a structured rank-four complex on \(\mathbf{P}^1\times\mathbf{P}^3\), with
\[
D=\mathbf{P}^1\times\mathbf{P}^2,\quad
P=\mathcal{O}(3,-3),\quad
L=\mathcal{O}(4,-2),\quad
T=\mathcal{O}(1,1),
\]
and a lift retaining maps \(\alpha:P\to E\), \(v:\mathcal{O}\to E\), \(\beta:E\to T\) with \(\beta(v)=+t_0 h\). It is not a deformation of the Horrocks–Mumford pullback.

## 3. Map audit

Semiregularity, a torsion twist, and an eightfold transform are sufficient strategies. A continuation proof may use one of them. A direct construction of the pinned object need not. Failure of a strategy, or a category or sign error inside a write-up of that strategy, withdraws or corrects that argument. It does not exclude the geometric setup. The only exclusion is a certified obstruction under the pinned hypotheses of the setup.

For a strategy that does use a semiregularity-type map, the missing step is a model-specific comparison for this star-algebroid, not the ordinary vanishing recorded in Section 1.

### 3.1. Buchweitz–Flenner, arXiv:math/9912245

Numbering below is the arXiv text.

- Definition 4.1 defines
  \[
  \sigma:\operatorname{Ext}^2(\mathcal{F},\mathcal{F})\longrightarrow\prod_{q\ge 0}H^{q+2}(X,\Omega_X^q)
  \]
  by cup-product with powers of the Atiyah class and the trace. This is the ordinary map. On the full-sign sector it is the zero map, by the duality argument in Section 1.
- Proposition 4.4 identifies the contraction of the Atiyah class against a square-zero extension of the base with the obstruction to extending the module across that extension. The extensions it treats are extensions of the structure sheaf of a complex space, not star products.
- Corollary 4.3 is the commutative square relating \(\sigma\) to contraction against the Chern character, for a coherent sheaf on a complex manifold.
- Theorem 5.1 is the variational Hodge statement: if a horizontal class is a Chern character component of an \(I\)-semiregular sheaf on the special fibre of a deformation of a compact algebraic manifold, then the class stays algebraic nearby. Semiregularity means injectivity of the corresponding part of \(\sigma\). Injectivity fails on the \(352\)-space.
- Theorem 7.2, for a coherent sheaf on a proper smooth family whose special fibre is bimeromorphic to a Kähler manifold, gives \(\dim S\ge\dim\operatorname{Ext}^1-\dim\ker\sigma\), and smoothness of the semiuniversal base when \(\sigma\) is injective. Theorem 7.3 is the fixed-base case, for a coherent sheaf of locally finite projective dimension. Both theorems put obstructions in \(\ker\sigma\). On the full-sign sector that kernel is the whole sector, so the theorems do not force \(O_{\mathrm{full}}=0\) and do not propagate a vanishing to higher order.

Markman, arXiv:2509.23403, Theorem 2.1, attributes the extension form of this package to Buchweitz–Flenner, Theorem 1.5, and the commutativity of the square to Corollary 4.3. Markman, arXiv:2502.03415, cites Theorem 5.1 for the same variational consequence. Those citations were not renumbered against the published Compositio pagination in this audit. The statements actually read are the arXiv items above. None of them is the comparison statement.

### 3.2. Pridham, arXiv:1208.3111

- Corollaries 2.24 and 2.25 realize \(\sigma\) as the tangent of a map from the derived moduli stack of perfect complexes to a cyclic-homology analogue of Deligne cohomology. Obstructions to deforming a perfect complex map to the obstruction of its Chern character remaining of Hodge type. If the base is constant, the image is zero.
- Remark 2.26 records the same conclusion for \(\mu\)-twisted sheaves, by applying the theorem to a gerbe banded by \(\mu\). The band is torsion. It is not the infinitesimal class \(15\Pi\in H^2(X,\mathcal{O}_X)\), and the base deformation is a deformation of a commutative (or derived-commutative) scheme.
- Corollary 1.20 extends a cyclic-homology constraint to perfect complexes over an admissible dg subcategory of the perfect complexes on a smooth proper scheme. The remark following it allows a quasi-coherent presheaf of simplicial associative algebras. That constraint is a relative cyclic map. Vanishing of the ordinary Buchweitz–Flenner map \(\sigma\) on the full-sign sector does not identify this relative cyclic map, and it does not evaluate the map on the obstruction of a varying star-algebroid.

Status of this source for the ambient problem: no model-specific comparison, and no detection or injectivity theorem, has been verified for this varying star-algebroid and its actual obstruction.

### 3.3. Markman, arXiv:2502.03415 and arXiv:2509.23403

- arXiv:2502.03415, Section 7.1, recalls the ordinary semiregularity map. That is the map which vanishes on the \(352\)-space.
- Definition 7.3.5 and the surrounding discussion extend the Atiyah class to a sheaf twisted by a \(\mu_r\)-cocycle. Conjecture 7.3.9 asks for the Buchweitz–Flenner extension theorem in that twisted setting. Section 7.4 proves the conjecture when the base is a family of abelian varieties and the Brauer class extends to a projective bundle on the total space. The sheaves to which the proof applies are not \(E\). The construction that Markman proves semiregular, in Section 9, is an equivariant reflexive sheaf built from ideal sheaves of translates of an Abel–Jacobi curve on a Jacobian, descended to a quotient and twisted by \(\mu_{8d}\).
- The global consequence used for Weil classes is Theorem 1.5.1 of that paper: algebraicity for abelian sixfolds of Weil type of discriminant \(-1\), for every imaginary quadratic field, and then for every abelian fourfold of Weil type by Schoen's degeneration. The input sheaf is the secant sheaf just described.
- arXiv:2509.23403, Theorem 1.2, quotes that result. Its Sections 2–10 set up secant sheaves and Orlov's equivalence \(D^b(X\times X)\to D^b(X\times\widehat{X})\) for a general CM field. The algebraicity conclusion is conditional on semiregularity of the resulting object, and the paper states that this semiregularity is not established beyond the imaginary-quadratic range already treated. Section 12 asks for a stronger semiregularity theorem in dimension at least \(8\) and does not prove one.
- arXiv:2502.03415, Section 8.3, is a first-order Hochschild calculation. The evaluation \(\operatorname{ev}_E:HH^2\to\operatorname{Ext}^2\) is the obstruction map of a coherent sheaf. Lemma 8.3.4: if the kernel of that map equals the kernel of contraction against the Chern character, and the map is surjective, then the sheaf is semiregular. Remark 8.3.5: without surjectivity, the semiregularity map still restricts to an injection on the image of the obstruction map. The input of these statements is a coherent sheaf. A sheaf such as \(E\) is an admissible input once the hypotheses are checked. The statements compare the first-order obstruction map. They do not evaluate the second-order class \(O_{\mathrm{full}}\), and they do not give an all-order continuation.

First-order \(HH^2\) results do take coherent sheaves such as \(E\) as input. The missing checked result is a theorem, with hypotheses verified for this varying star-algebroid, that evaluates this second-order class or gives an all-order continuation. arXiv:2509.23403v2, Question 11.4, asks whether surjectivity of \(\operatorname{ev}_E\) can be dropped in its Lemma 11.3, and whether the Buchweitz–Flenner extension theorem holds when \(\sigma\) is merely injective on the image of \(\operatorname{ev}_E\), including for twisted sheaves. That weaker package is posed as a question. It is not a checked theorem, and it is not an evaluation of \(O_{\mathrm{full}}\). The eightfold secant sheaf in these papers is not identified with this \(E\). That identification remains a sufficient strategy, Section 4.2.

### 3.4. Lie-algebroid and formality statements

Bandiera–Lepri–Manetti, arXiv:2208.00694:

- Theorem 4.4: for a locally free module over a Lie algebroid \(\mathcal{A}\), the Thom–Whitney totalization of \(\Omega^*(\mathcal{A},\mathcal{E}nd(E))\) controls deformations as an \(\mathcal{A}\)-module. The obstruction space is Lie-algebroid hypercohomology \(\mathbb{H}^2(\mathcal{A};\mathcal{E}nd(E))\).
- Theorem 8.2: for a Lie pair \(\mathcal{A}\subset\mathcal{L}\) and a locally free \(\mathcal{A}\)-module, the composite of the semiregularity map with the map into the truncated quotient of \(\Omega^*(\mathcal{L})\) annihilates those obstructions. If the Leray spectral sequence of the pair degenerates at \(E_1\), each semiregularity component itself annihilates obstructions.

The ambient residual is the failure of an associative module equation over a star product, after the D'Agnolo–Schapira descent. A Lie-algebroid module structure sees a flat connection along an anchor, not the order-\(h^2\) associative terms \(\mu_2\), \(T(g)\), and \(b^2\). Using Theorem 8.2 as the mechanism for \(C_2\) is a sufficient strategy. It requires a comparison of the two obstruction classes. That comparison has not been verified. Ordinary vanishing of \(\sigma\) does not supply it.

Bandiera–Manetti–Meazzini, *Deformations of polystable sheaves on surfaces: quadraticity implies formality*, Moscow Mathematical Journal 22 (2022), no. 2, 239–263: for a polystable coherent sheaf on a smooth complex projective surface, the differential graded Lie algebra of derived endomorphisms is formal if and only if the Kuranishi family is quadratic. The base here is a fourfold, the category is the star-algebroid category rather than the ordinary sheaf category, and the ordinary hull is already a power-series ring. The surface theorem does not apply.

### 3.5. Sources that define the category and do not kill the obstruction

These are the sources that match the category actually in use. None of them asserts vanishing of \(O_{\mathrm{full}}\).

- D'Agnolo–Schapira, arXiv:math/0506064, Section 3: algebra-isomorphism and triple-unit descent for a quantized algebroid, and the module equation. Their existence theorem is for Lagrangian submanifolds, not for this rank-two bundle.
- Yekutieli, arXiv:0905.0488: twisted deformation quantization and crossed-groupoid descent on algebraic varieties. It does not force the module obstruction to vanish.
- Bressler–Gorokhovsky–Nest–Tsygan, arXiv:0810.0030: the Deligne groupoid of an algebroid stack. It identifies the deformation problem; it does not solve this instance.
- Lowen, arXiv:0707.2602: the characteristic morphism from Hochschild cohomology to the obstruction of deforming an object. This is the evaluation \(\operatorname{ev}_E\) used to compare two ambient lifts. It computes neither lift.

### 3.6. Detector rank and the evaluated obstruction

The exact rank \(333\) and the kernel dimension \(19\) are the rank and the kernel of one joint family: all \(30\) scalar maps, together with the map \(\ell\). They are not a rank of \(O_2\), and they do not locate \(O_2\).

Only two of those scalar maps have been evaluated on \(O_2\). The value \(\ell(O_2)\) is pending. The other \(28\) maps have not been evaluated on \(O_2\). A result \(\ell(O_2)=0\), taken alone, does not place \(O_2\) in the \(19\)-dimensional joint kernel.

The exact-\(Q\) elimination already verifies the zero residual tail of that elimination. A named JSON field would record the same report. It is a reporting nicety, not an additional mathematical certificate.

This note does not recompute the rank, the kernel, \(\ell(O_2)\), or the unevaluated maps.

## 4. Hypotheses, strategies, and supplied arguments

Three kinds of item are kept apart, before the retire and promote rule.

- A sufficient-strategy gate is required only when that proof strategy is the one in use. Semiregularity, a torsion twist, and an eightfold transform are of this kind. A direct construction need not pass them. Failure withdraws or corrects that argument and does not exclude the setup.
- A supplied argument is text already given for the carrier construction. Its status in this note is supplied-pending-artifact-review: the immutable proof or check artifact has not been reviewed here. The item blocks promotion until that review, and it does not retire the route.
- An open construction or comparison question is still unanswered. It blocks promotion of any continuation that needs it, and it does not retire the setup.

Exclusion of a geometric setup requires a certified obstruction under the pinned hypotheses. A category or sign error in a write-up is corrected, or that argument is withdrawn.

### 4.1. Horrocks–Mumford: the open comparison

- **Comparison.** No model-specific comparison, and no detection or injectivity theorem, has been verified for this varying star-algebroid and its actual obstruction. Vanishing of the ordinary Buchweitz–Flenner map \(\sigma\) on the full-sign sector does not identify the relative cyclic map of Pridham, Corollary 1.20, and does not evaluate that map on the obstruction. This comparison blocks promotion of a continuation that uses a semiregularity-type map. It is not necessary for a direct construction of the pinned object.

### 4.2. Sufficient-strategy gates

These gates are conditional on the chosen proof strategy. They are not necessary for every continuation.

- **Semiregularity.** A strategy may try to kill the residual by a semiregularity map: Buchweitz–Flenner, Theorems 7.2 and 7.3, Pridham, Corollaries 2.24 and 2.25, or Bandiera–Lepri–Manetti, Theorem 8.2. Ordinary \(\sigma\) is the zero map on the \(352\)-dimensional sector, so those ordinary theorems do not force \(O_{\mathrm{full}}=0\). Using any of them on the star-algebroid residual requires the comparison in Section 4.1. That comparison is not verified. Declining this strategy does not exclude the setup.
- **Torsion twist.** Replacing the infinitesimal class \(15\Pi\in H^2(X,\mathcal{O}_X)\) by a \(\mu_r\)-cocycle, so that Markman, Section 7.4, or Pridham, Remark 2.26, applies, is a sufficient strategy. Those statements use a torsion band. Declining the replacement does not exclude the setup.
- **Eightfold transform.** Identifying an Orlov transform of \(E\), or of a deformation of \(E\), with a semiregular secant sheaf of Markman, arXiv:2502.03415, Section 9, or with an object satisfying the semiregularity hypothesis left open in arXiv:2509.23403, is a sufficient strategy. The constructions differ. Declining the identification does not exclude the setup.

An all-order vanishing theorem of semiregularity type is this same strategy. It is not a gate every continuation must pass.

### 4.3. Carrier continuation: supplied arguments

The proposed all-order mechanism has three layers: a weight vanishing for the normal jet, algebraization by effective Lefschetz, and an isolated-defect criterion for the reflexive hull. The weight-slot arithmetic is not recomputed in this note. The arguments in C1 and C3, and the weight part of the construction in C2, are the ones supplied in PR #1 comments 6104475229 and 6104506387. Status: supplied-pending-artifact-review.

- **C1. Weight, frame covariance, and homogeneous homotopies.** Set \(z=t_0/t_1\), with \(\operatorname{wt}(t_0)=2\), \(\operatorname{wt}(t_1)=0\), and \(\operatorname{wt}(h)=-1\). The two local coefficients of the prescribed section of \(T=\mathcal{O}(1,1)\) are \(hz\) and \(h\), of weights \(1\) and \(-1\). These are the two raw \(T\)-frame characters, so \(\beta(v)=+t_0 h\) is homogeneous. The coordinate \(t_0\) is not assigned weight zero.

  For the five presentation coordinates \((P,E_0,E_1,E_2,\tau)\), the finite raw characters are \((3,0,2,2,1)\) and the infinity characters are \((-3,0,-6,-4,-1)\). Their difference is twice the base-degree vector \((3,0,4,3,1)\). Plane degrees are \((-3,0,-4,-4,1)\). On the \(U\)-chart, subtract the plane degree times \(\operatorname{wt}(U)\) from the raw character, and use \(\operatorname{wt}(h/U)=-1-\operatorname{wt}(U)\). The transitions, including completion columns, satisfy \(M(g_\lambda x)\,D_{\mathrm{source}}=D_{\mathrm{target}}\,M(x)\). Each \(k\)-th correction restores the same covariance after multiplication by \(h^k\). The relation line has raw characters \(0,-6\). The bundles \(P\), \(L\), and \(T\) have characters \((3,-3)\), \((4,-4)\), and \((1,-1)\).

  The chosen homotopies are homogeneous. The ordered Laurent Čech contraction retains or discards monomials and changes only the Čech index and the sign. The base splitting is made in each weight by the actual triangular transition. Frozen coefficients are not averaged. Algebraic \(\mathbf{G}_m\)-representations remain \(\mathbf{Z}\)-graded in every characteristic: distinct Laurent monomials remain distinct characters (Milne, Theorem 14.12 and Remark 14.13). Weights alias if one tests only the finite group \(\mathbf{F}_p^\times\), or only the differentiated Lie action. A replay retains integer exponent weights.

  The weight is this supplied argument. Review of the immutable artifact is still open.

- **C2. Lefschetz input.** Corollaire 3.4 takes as input an actual formal locally free sheaf on the completion along \(D\). The weights of C1 enter the construction of that sheaf. They are not a separate hypothesis of the Lefschetz theorem. Vanishing of the graded pieces \(H^2(\operatorname{Sym}^2 B\otimes L^{-1}I^k)\) for \(k\ge 7\) is a step in that construction. It is not, by itself, the formal sheaf. The open construction question is whether that formal locally free sheaf has been exhibited as a reviewed artifact. It is not an unchecked-weight hypothesis, and it is not a gap inside Corollaire 3.4.

- **C3. Confinement of the hull.** The sheaf \(R\) is reflexive on the regular fourfold and flat over \(\mathbf{P}^1\). At a point of a potentially bad fibre, \(\operatorname{depth}(R)\ge 2\) and the base uniformizer is regular on \(R\), so \(\operatorname{depth}(R_t)\ge 1\). The only possible torsion in the fibre is of finite length, hence zero. For \(t\ne 0\), the reflexive hull has split restriction to a plane and therefore splits on \(\mathbf{P}^3\) by Abe–Yoshinaga, Theorem 0.2. The Hilbert polynomial is constant and equals the generic split polynomial, so the finite-length quotient \(R_t^{**}/R_t\) has length zero. This removes noncentral singularities without a flatness hypothesis on the family of hulls.

  For the support, a full algebraic group-scheme linearization is not required. For each \(\lambda\), homogeneity gives a formal isomorphism with \(g_\lambda^*R\). Relative full faithfulness lifts it on the intersection of the two bundle neighborhoods, and reflexive uniqueness extends it over \(X\). The closed singular support is therefore invariant. Its projection is finite and disjoint from \(h=0\), so the support is the unique off-plane fixed point \(o=[0:0:0:1]\). Together with the fibre argument, the only remaining point is \((t_0=0,\,o)\). The defect of \(\beta\) is carried by the same structured isomorphisms and by \(\beta(v)=t_0 h\).

  Abe–Yoshinaga, Theorem 0.2, remains a splitting criterion on \(\mathbf{P}^n\). Stacks Project, Lemma 0EBJ, remains the extension lemma across depth at least \(2\). The confinement statement is this supplied argument. Those two results are steps inside it, not confinement theorems by themselves. Review of the immutable artifact is still open.

### 4.4. The central fibre, the depth step, and the stalk lemma

Reflexivity of the total sheaf \(R\) gives \(\operatorname{depth}(R)\ge 2\) at points whose local rings have dimension at least \(2\) (Abe–Yoshinaga, Proposition 1.2). In this criterion \(R\) is the canonical reflexive extension, so \(R=R^{**}\). That is a property of the total sheaf. It is not reflexivity of the central fibre \(R_0=R/zR\).

The central fibre is torsion-free before any length is computed. Away from the finite exceptional set it is a vector bundle. At each remaining point, reflexivity of \(R\) and regularity of \(z\) give depth at least \(1\) on the fibre, so the fibre has no finite-length torsion submodule.

If a module \(M\) does have a torsion submodule \(T\), set \(N=M/T\). Under the identification of a torsion-free module with its image in the double dual, there is an exact sequence
\[
0\to T\to M\to M^{**}\to N^{**}/N\to 0.
\]
The defect is the cokernel \(N^{**}/N\). The length of \(T\) is not added to that defect. If a computation uses the Hilbert-function difference \(h^0(M^{**}(n))-h^0(M(n))\), the torsion term has a different role. Finite-length support does not determine the twist at which that difference stabilizes. On \(\mathbf{P}^3\), take \(M=\mathcal{I}_p(-d)\). Then \(M^{**}=\mathcal{O}(-d)\) and the quotient is a skyscraper \(\mathcal{O}_p\) of length \(1\), for every \(d\). The difference \(h^0(M^{**}(n))-h^0(M(n))\) is \(0\) for \(n<d\) and \(1\) for \(n\ge d\). Support and length fix the stable value, not the threshold, and the threshold is arbitrarily large as \(d\) grows. The difference equals the length of \(\mathcal{O}_p\) once \(H^1(M(n))=0\) and the sections of \(M^{**}\) and of \(M\) agree off \(\mathcal{O}_p\). A justified threshold is a proved vanishing \(H^1(M(n))=0\), for instance the Castelnuovo–Mumford regularity of \(M\).

On the torsion-free central fibre one has \(T=0\). At the candidate point \(x=([0:1],[0:0:0:1])\), set \(A=\mathcal{O}_{X,x}\), \(M=R_x\), \(B=A/(z)\), and \(N=M/zM\). The module \(M\) is the total reflexive stalk, and \(B\) is the central three-dimensional ring. The central fibre stalk \(N\) is torsion-free, so \(N\to N^{**}\) is injective, with the double dual taken over \(B\). Define \(Q=N^{**}/N\). As of the earlier checkpoint, before 6104798062, the length of \(Q\) was uncomputed. For the fixed chosen carrier the certified value is \(\operatorname{length}_B(Q)=12\), by PR #1 comments 6104798062 and 6104803214. The preferred computation uses no twist window: the length of \(Q\) at \(x\).

Globally, \(R_0\) is the torsion-free central sheaf and its stalk is \(N\) over \(B\). The exact sequence of sheaves is \(0\to R_0\to R_0^{**}\to Q\to 0\). When \(Q\) is zero-dimensional, a proved bound \(H^1(R_0(n))=0\) gives \(h^0(R_0^{**}(n))-h^0(R_0(n))\) equal to the length of \(Q\). Vanishing or regularity of the total sheaf is not that certificate. Without any vanishing, \(h^0(R_0^{**}(n))-h^0(R_0(n))\) is at most the length of \(Q\), so a nonzero difference at a single \(n\) certifies \(Q\ne 0\). Only a zero, or an exact length, needs the bound \(H^1(R_0(n))=0\).

Central reflexivity is not a prerequisite for testing \(Q\). For this fibre, \(Q=0\) is what establishes central reflexivity. The conditional chain, with each step using only what the previous step has, is the following.

1. **Baseline hypotheses.** These can be checked before the test. The central fibre is torsion-free. The non-free locus meets the carrier in at most the one point \(([0:1],[0:0:0:1])\). The element \(z\) is a nonzerodivisor on \(M\). The stalk ring \(A\) is regular local of dimension \(4\). Self-duality of this stalk is not one of these hypotheses. The global isomorphism \(R\cong R^*\otimes L\) localizes there, and trivializing the invertible sheaf \(L\) at that stalk gives \(M\cong M^*\). That is provenance for the lemma. It is not an independent hypothesis and not a gate.
2. **Test \(Q\).** The outcome \(Q\ne 0\) stays available. It is not removed by assuming reflexivity of the fibre.
3. **\(Q=0\) gives central reflexivity.** On the torsion-free fibre the map \(N\to N^{**}\) is injective, so \(Q=0\) means \(N\cong N^{**}\).
4. **Depth.** Reflexivity of \(N\) gives \(\operatorname{depth}(N)\ge 2\). With \(z\) regular on \(M\), Stacks Project, Lemma [0BUW](https://stacks.math.columbia.edu/tag/0BUW), in its local form Lemma [090R](https://stacks.math.columbia.edu/tag/090R), gives \(\operatorname{depth}(M)=\operatorname{depth}(N)+1\ge 3\).
5. **Freeness and the bundle extension.** These are the lemma below.

**Isolated self-dual stalk lemma.** Under the baseline hypotheses, together with the stalk isomorphism \(M\cong M^*\) just recorded, \(Q=0\) if and only if \(M\) is free. Thus \(Q=0\) proves that the total stalk is free, and that freeness is the resulting vector-bundle extension of the carrier at the stalk. The dimension \(4\) is part of the statement. Depth at least \(3\) and Stacks Project, Proposition [00O7](https://stacks.math.columbia.edu/tag/00O7), give a free resolution of length at most \(1\). If \(M\) is not free, a minimal resolution \(0\to F_1\to F_0\to M\to 0\) has \(F_1\ne 0\), and \(E=\operatorname{Ext}^1(M,A)\) is nonzero of finite length by isolation. Dualizing yields \(0\to M^*\to F_0^*\to K\to 0\) and \(0\to K\to F_1^*\to E\to 0\). Stacks Project, Lemma [00LX](https://stacks.math.columbia.edu/tag/00LX), with \(\operatorname{depth}(E)=0\) and \(\operatorname{depth}(F_1^*)=4\), gives \(\operatorname{depth}(K)=1\), hence \(\operatorname{depth}(M^*)=2\). Self-duality would require \(\operatorname{depth}(M^*)=\operatorname{depth}(M)\ge 3\). In the other direction a free \(M\) has free \(N\), so \(Q=0\).

A nonzero value of \(Q\) obstructs this bundle extension. It does not obstruct the formal continuation along \(D\). As of the earlier checkpoint, before 6104798062, the length of \(Q\) at \(([0:1],[0:0:0:1])\) was uncomputed. For the fixed chosen carrier that length is the certified value \(\operatorname{length}_B(Q)=12\) (PR #1, comments 6104798062 and 6104803214, the latter an independent SymPy Groebner-basis reproduction). That value marks G2 **EXCLUDED** for this carrier only. G1, the formal continuation along \(D\), stays passed and retained. The central map conditions are not passed by the length certificate, and the central conditions for other carriers are not settled by this result. A zero of \(h^0(R_0^{**}(n))-h^0(R_0(n))\) on a finite twist window does not certify the length and does not certify the central map conditions.

C1 and C3, and the weight part of C2, do not depend on this length. No further depth-upgrade theorem is required once step 4 applies. Proposition 00O7 still says that a second syzygy of a nonzero finite-length module over a \(4\)-dimensional regular local ring has depth \(2\). That comparison is the one used inside the lemma. It is not a demand for another theorem, and it is not a prerequisite for testing \(Q\).

### 4.5. Fixed-carrier status: G1 retained, G2 excluded

Two gates of the fixed chosen carrier are kept separate.

- **G1. Formal continuation.** The all-order formal continuation along \(D\). Status: passed, and retained. The central-defect certificate leaves it in place. L4.C2 remains the separate artifact review of the written formal sheaf.
- **G2. Global vector-bundle extension.** Extending the resulting algebraic reflexive sheaf as a global vector bundle. Under the baseline hypotheses, the stalk lemma makes this equivalent to \(Q=0\). Status: **EXCLUDED** for this fixed carrier only.

The exclusion is the certified value \(\operatorname{length}_B(Q)=12\) at \(([0:1],[0:0:0:1])\). PR #1, comment 6104798062, records that length from a Gröbner basis of the reduced cokernel of the specialized relation matrix, with standard monomials numbering \(8+4\). PR #1, comment 6104803214, is an independent SymPy Groebner-basis reproduction of the same five relations and the same leading module monomials, confirming length \(12\). As of the earlier checkpoint, before 6104798062, that length was uncomputed.

Other formal-lift and carrier choices stay **OPEN**. No family-wide exclusion is claimed. The original theorem, the central conditions for other carriers, and the Horrocks–Mumford second-order obstruction computation are not settled by this result.

## 5. The Lefschetz input that does exist

SGA 2, Exposé XII, Corollaire 3.4, as printed on page 127 of arXiv:math/0511279, is the relative statement. It is not the absolute ample statement. The absolute statement is Corollaire 3.5 on the following page. In the recomposed HTML edition the same pair is Corollaire 42.4 and Corollaire 42.5.

Corollaire 3.4 assumes a projective flat morphism \(f:X\to S\) to a locally Noetherian base, an invertible sheaf \(\mathcal{O}_X(1)\) ample relative to \(S\), and a section \(t\) whose restriction to every fibre is regular. Let \(X_0\) be the zero scheme of \(t\). Assume that every fibre of \(X_0\) has depth at least \(2\) at its closed points and every fibre of \(X\) has depth at least \(2\) at its closed points. Then the pair \((X,X_0)\) satisfies effective Lefschetz:

1. For every open neighborhood \(U\) of \(X_0\), completion is fully faithful on locally free coherent sheaves.
2. Every locally free coherent sheaf on the formal completion along \(X_0\) is the completion of a locally free coherent sheaf on some open neighborhood of \(X_0\).

For \(X=\mathbf{P}^1\times\mathbf{P}^3\), \(S=\mathbf{P}^1\), and \(\mathcal{O}_X(1)=\mathcal{O}(0,1)\), relative ampleness holds, and \(D=\mathbf{P}^1\times\mathbf{P}^2\) is the zero scheme of a relative hyperplane section. The depth bounds hold because the fibres are \(\mathbf{P}^3\) and \(\mathbf{P}^2\). The base \(\mathbf{P}^1\) is Noetherian and carries an ample line bundle, which is the gluing hypothesis used in the proof of the corollary. So Corollaire 3.4 applies to the pair \((X,D)\) inside its stated category: locally free sheaves on the formal completion.

The input of the corollary is that formal sheaf. The weights of Section 4.3 enter the construction of the sheaf. They are not a separate hypothesis of the corollary. The corollary does not test \(Q\) and does not replace the stalk lemma of Section 4.4. Corollaire 3.5, the absolute ample statement, does not apply to \(\mathcal{O}(0,1)\).

Abe–Yoshinaga, RIMS preprint 1496, Theorem 0.2: a reflexive sheaf on \(\mathbf{P}^n\), \(n\ge 3\), splits as a sum of line bundles if and only if its restriction to some hyperplane does. Inside the supplied confinement argument of C3, this criterion is applied to the plane restriction of the hull for \(t\ne 0\). The theorem is that splitting step. It is not, by itself, the confinement statement.

## 6. Retire / promote rule

This rule is applied after the separation in Section 4.

A route is promoted only when its pinned construction gates have passed and every sufficient-strategy gate that the chosen proof actually uses has passed. A pass of L2 is never, by itself, promotion of the original target theorem. Neither route is promoted by \(O_{\mathrm{full}}=0\) or by \(\sigma(O_{\mathrm{full}})=0\). Under the verified isolation and regular-parameter hypotheses of Section 4.4, with stalk self-duality the localization of \(R\cong R^*\otimes L\), \(Q=0\) is the total-stalk freeness statement and the resulting bundle extension. It is not a pass of the original target theorem, and it is not a pass of later carrier conditions such as map-rank or comparison.

Semiregularity, a torsion twist, and an eightfold transform are sufficient-strategy gates. They are not necessary for every continuation. A direct construction may bypass them. Failure of a strategy that is not in use neither blocks promotion nor retires the route.

A category or sign error in a write-up is corrected, or that argument is withdrawn. The error does not exclude the geometric setup.

A geometric setup is excluded only by a certified obstruction under its pinned hypotheses. For the Horrocks–Mumford side, a certified nonzero full-sign obstruction excludes second-order extension of the pinned triple \((X,E,\xi)\), once geometric source identification, closedness, and choice/sign-independence have been proved. That exclusion is stronger than retiring one vanishing claim. It is narrower than an exclusion of every Horrocks–Mumford route: other carriers, other ambient directions, and repair routes stay. An open construction or comparison question blocks promotion and does not retire. A supplied argument whose artifact has not been reviewed blocks promotion and does not retire. A gate lists only hypotheses that can be checked before the test runs. The conclusion of a test is not one of its prerequisites. Retirement by a certified obstruction is not reversed by a later vanishing of a different class.

For the fixed chosen carrier, Section 4.5 records a certified obstruction of that narrower kind: G2 is **EXCLUDED** for this carrier only. G1 stays passed and retained. The exclusion does not settle the original theorem, the central conditions for other carriers, or the Horrocks–Mumford second-order obstruction computation. As of the earlier checkpoint, before 6104798062, the length of \(Q\) was uncomputed.

## 7. Gate ladder

### L0 — Category

| Route | Pass observable | Retire observable | Promotion |
|---|---|---|---|
| Horrocks–Mumford | The object is the star-algebroid module residual \(O_{\mathrm{full}}\in\operatorname{Ext}^2(E,E)_\chi\). | A certified obstruction under the pinned hypotheses, showing that this residual is not the object of the setup. A write-up that treats \(O_{\mathrm{full}}\) as an ordinary Yoneda class, a \(\mu_r\)-twisted class, or the obstruction of a Markman secant sheaf, without the comparison of Section 4.1, is corrected or withdrawn. That write-up does not exclude the setup. | None at L0. |
| Carrier continuation | The object is the structured rank-four data on \(\mathbf{P}^1\times\mathbf{P}^3\), kept distinct from \(E\). | A certified obstruction under the pinned hypotheses of this carrier. A write-up that identifies the construction with the Horrocks–Mumford pullback, or with the eightfold secant sheaf, is corrected or withdrawn. That write-up does not exclude the setup. | None at L0. |

L0 passes for both routes on the descriptions fixed above.

### L1 — First-order necessity

| Route | Pass observable | Retire observable | Promotion |
|---|---|---|---|
| Horrocks–Mumford | \(\operatorname{ev}_E(\xi)=0\), with gerbe sign \(b=-15\Pi\). | A certified nonzero value of \(\operatorname{ev}_E(\xi)\). | None. |
| Carrier continuation | The sixth normal jet satisfies the cocycle, symplectic, and section equations, in a pinned certificate. | A certified counterexample to one of those three equations, under the pinned hypotheses. | None. |

The Horrocks–Mumford pass is the first-order cancellation already recorded. This note does not recompute it. The carrier pass is not claimed here; that gate stays open, which blocks promotion and does not retire.

### L2 — Kill test

| Route | Pass observable | Retire observable | Promotion |
|---|---|---|---|
| Horrocks–Mumford | \(O_{\mathrm{full}}=0\) in the \(352\)-dimensional space. | A certified nonzero full-sign obstruction excludes second-order extension of the pinned triple \((X,E,\xi)\), once geometric source identification, closedness, and choice/sign-independence are proved. This is stronger than retiring one vanishing claim, and narrower than excluding every Horrocks–Mumford route. A residue modulo \(3\) counts only after integral specialization at \(3\) is verified: good reduction of \(X\) and of \(E\), and the functional \(\ell\) over \(\mathbf{Z}_{(3)}\). Until that specialization is checked, a mod-\(3\) value is uncertified. The vanishing \(\ell(O_2)=0\), alone, is not a pass and does not place \(O_2\) in the joint kernel. See Section 3.6. | Forbidden. A zero is one necessary test. |
| Carrier continuation | \(Q=0\) on the torsion-free central fibre, under the baseline hypotheses of Section 4.4. Central reflexivity is the conclusion of this vanishing, not a prerequisite. The chain is then depth at least \(3\) by Lemma 0BUW, then freeness and the bundle extension by the stalk lemma. | A certified \(Q\ne 0\) under those baseline hypotheses obstructs the global vector-bundle extension (G2) and does not obstruct the formal continuation (G1) along \(D\). For the fixed chosen carrier, \(\operatorname{length}_B(Q)=12\) is that certificate (PR #1, comments 6104798062 and 6104803214), so G2 is **EXCLUDED** for this carrier only. G1 stays passed and retained. Other formal-lift and carrier choices stay open. As of the earlier checkpoint, before 6104798062, the length was uncomputed. | The local-freeness implication holds when \(Q=0\). Promotion of the original target theorem, or of later carrier conditions, is forbidden. |

The Horrocks–Mumford class \(O_{\mathrm{full}}\) is not evaluated in this note, and that L2 gate stays open. The length certificate does not settle the Horrocks–Mumford second-order obstruction computation, the original theorem, or the central conditions for other carriers. For the fixed chosen carrier, G2 is **EXCLUDED** and G1 stays passed and retained, as in Section 4.5. As of the earlier checkpoint, before 6104798062, the length of \(Q\) was uncomputed.

### L3 — Hypothesis sheet

L3 passes for a chosen continuation only when every construction gate that continuation uses is verified, every supplied argument it uses has passed artifact review, and every sufficient-strategy gate it actually uses has passed. L3 does not retire a route because a sufficient strategy was not chosen. L3 retires a route only when a pinned hypothesis that the route uses is a certified obstruction.

| Item | Mark | Effect on L3 |
|---|---|---|
| Comparison, Section 4.1 | Open | Blocks a semiregularity-type continuation. Does not block a direct construction. Does not retire. |
| Semiregularity, torsion twist, eightfold transform | Sufficient strategies | Required only if chosen. Failure withdraws that argument. |
| C1 weight, frame covariance, homogeneous homotopies | Supplied, pending artifact review | Blocks promotion until review. Does not retire. |
| C2, the formal locally free sheaf as a reviewed artifact | Open construction | Blocks promotion. Not a separate weight hypothesis, and not a gap in Corollaire 3.4. |
| C3 confinement | Supplied, pending artifact review | Blocks promotion until review. Does not retire. |
| C4 chain: baseline hypotheses, then \(Q\), then central reflexivity, then depth, then freeness | \(z\)-regularity and isolation at \(([0:1],[0:0:0:1])\) are baseline. Stalk self-duality is the localization of \(R\cong R^*\otimes L\), not a gate. Central reflexivity is not baseline | \(Q=0\) on the torsion-free fibre gives central reflexivity, then Lemma 0BUW gives depth at least \(3\), then the stalk lemma gives freeness. A nonzero \(Q\) is not excluded by assumption for a formal-lift or carrier choice other than the fixed chosen carrier. As of the earlier checkpoint, before 6104798062, the length of \(Q\) was uncomputed. For the fixed chosen carrier the certified value is \(\operatorname{length}_B(Q)=12\), so G2 is **EXCLUDED** for this carrier only and G1 stays passed and retained. Other formal-lift and carrier choices stay open. The original theorem, the central conditions for other carriers, and the Horrocks–Mumford second-order obstruction are not settled. The central map conditions are not passed by the length certificate. |
| SGA 2, XII, Corollaire 3.4, for an actual formal locally free sheaf on \((\mathbf{P}^1\times\mathbf{P}^3,D)\) | Proved external input | Not a substitute for exhibiting that sheaf. |

### L4 — What sits above L3

A sufficient-strategy gate passes only when that strategy is chosen and a cited theorem applies to its object. A construction gate passes by verification or by artifact review, as marked.

| Gate | Obligation | Status |
|---|---|---|
| L4 comparison | A model-specific comparison, or a detection or injectivity theorem, for this varying star-algebroid and its actual obstruction. | No such theorem has been verified. Sufficient for a semiregularity strategy. Not necessary for every continuation. Ordinary \(\sigma\) does not identify the relative cyclic map. |
| L4 strategies | Semiregularity, torsion twist, or eightfold transform, when one of them is the chosen proof. | Conditional on that choice. Ordinary \(\sigma=0\) on the \(352\)-space does not fill the comparison. |
| L4.C1 | Artifact review of the supplied weight \(\operatorname{wt}(t_0)=2\), the frame covariance, and the homogeneous homotopies. | Supplied-pending-artifact-review. |
| L4.C2 | Exhibit the formal locally free sheaf as a reviewed artifact, then apply Corollaire 3.4 to that sheaf. | Open construction. The corollary is the theorem for that input. Weights enter the construction. |
| L4.C3 | Artifact review of the supplied confinement argument. | Supplied-pending-artifact-review. |
| L4.C4 | Run the chain of Section 4.4. The baseline hypotheses are checked before \(Q\) is tested. Stalk self-duality is provenance, not a gate. | \(Q=0\) gives central reflexivity of the torsion-free fibre, Lemma 0BUW gives depth at least \(3\), and the stalk lemma gives freeness and the bundle extension. As of the earlier checkpoint, before 6104798062, the length of \(Q\) at the one candidate stalk was uncomputed. For the fixed chosen carrier that length is the certified value \(\operatorname{length}_B(Q)=12\) (PR #1, comments 6104798062 and 6104803214), so G2 is **EXCLUDED** for this carrier only and G1 stays passed and retained. Other formal-lift and carrier choices stay open. The central map conditions are not passed by the length certificate. The original theorem, the central conditions for other carriers, and the Horrocks–Mumford second-order obstruction computation are not settled. A twist-window zero is not that length. |

The comparison is the item above L3 that still has no verified theorem, and it is a sufficient-strategy gate. The carrier items above L3 are an artifact review, an open construction, and the chain of Section 4.4. The stalk lemma is the freeness step of that chain. It is not a missing theorem.

## 8. Fault tree

Top event: a route is reported as promoted, or as all-order unobstructed, without a pass of the gates its chosen continuation uses; or a write-up error is reported as exclusion of the setup.

Horrocks–Mumford branch.

- \(O_{\mathrm{full}}=0\) is read as promotion. Blocked by the rule in Section 6 and by L2.
- Or ordinary \(\sigma\) is read as the relative cyclic map, or as an all-order mechanism. Ordinary vanishing does not identify that map. The comparison in Section 4.1 is unverified. This blocks a semiregularity strategy. It does not exclude a direct construction.
- Or a \(\mu_r\) theorem is applied to \(15\Pi\). The cocycle orders differ. That argument is corrected or withdrawn. It is a sufficient strategy, Section 4.2, and it does not exclude the setup.
- Or the Orlov transform of \(E\) is treated as Markman's semiregular secant sheaf. Same disposition: correct or withdraw the argument. The setup stays.
- Or a Lie-algebroid semiregularity theorem is applied to the associative residual. Theorem 8.2 of arXiv:2208.00694 controls a different differential graded Lie algebra. Using it is a sufficient strategy and needs the comparison. Ordinary vanishing of \(\sigma\) does not supply that comparison.
- Or the rank \(333\), or the kernel dimension \(19\), is read as an evaluation of \(O_2\). Those numbers are the joint family of the \(30\) scalar maps plus \(\ell\). Only two maps have been evaluated on \(O_2\), and \(\ell(O_2)\) is pending. Blocked by Section 3.6.
- Or a certified nonzero full-sign class is read as retiring only a vanishing claim, or as excluding every Horrocks–Mumford route. Once geometric source identification, closedness, and choice/sign-independence are proved, the exclusion is second-order extension of the pinned triple \((X,E,\xi)\). A residue modulo \(3\) counts only after good reduction of \(X\) and of \(E\) and the functional \(\ell\) over \(\mathbf{Z}_{(3)}\) are verified.
- Or a first-order \(HH^2\) theorem is read as an evaluation of \(O_{\mathrm{full}}\) or as an all-order continuation. Lemma 8.3.4 and Remark 8.3.5 take a coherent sheaf as input and compare the first-order obstruction map. Question 11.4 of arXiv:2509.23403v2 is a question under weaker hypotheses.

Carrier branch.

- \(Q=0\) is read as the original target theorem, or as a later carrier condition such as map-rank or comparison. Under the verified baseline hypotheses, \(Q=0\) does prove total-stalk freeness and the bundle extension, by the stalk lemma. That implication stands. The warning is against the claims that go beyond it.
- Or the certified \(\operatorname{length}_B(Q)=12\) for the fixed chosen carrier is read as excluding G1, as excluding other formal-lift or carrier choices, or as settling the original theorem, the central conditions for other carriers, or the Horrocks–Mumford second-order obstruction computation. G2 is **EXCLUDED** for this carrier only (PR #1, comments 6104798062 and 6104803214, the latter an independent SymPy Groebner-basis reproduction). G1 stays passed and retained. The other choices stay open. As of the earlier checkpoint, before 6104798062, that length was uncomputed.
- Or central reflexivity is required before \(Q\) is tested. On the torsion-free central fibre, \(Q=0\) is what establishes central reflexivity. Requiring it first excludes the nonzero branch by assumption. The chain in Section 4.4 tests \(Q\) under the baseline hypotheses only.
- Or a finite normal jet is fed to Corollaire 3.4 in place of the formal locally free sheaf. The input of the corollary is that sheaf. Weights enter its construction and are not a separate Lefschetz hypothesis. The open item is the reviewed artifact, L4.C2.
- Or the weight of \(t_0\) is reported as unset. The supplied argument fixes \(\operatorname{wt}(t_0)=2\), with frame covariance and homogeneous homotopies, pending artifact review.
- Or depth at least \(3\) is inferred from reflexivity of \(R\) alone, or is demanded as a further theorem. Reflexivity of \(R\) gives depth at least \(2\). Reflexivity of the fibre is the conclusion of \(Q=0\). With \(z\) regular, Lemma 0BUW then gives depth at least \(3\), and the stalk lemma gives freeness.
- Or the length of \(T\) is added to the defect \(N^{**}/N\). The sequence \(0\to T\to M\to M^{**}\to N^{**}/N\to 0\) keeps those lengths separate.
- Or stabilization is inferred from support. A zero of \(h^0(R_0^{**}(n))-h^0(R_0(n))\) on a finite twist window is read as \(Q=0\). The torsion-free central sheaf is \(R_0\), with stalk \(N\) over \(B\), and the exact sequence is \(0\to R_0\to R_0^{**}\to Q\to 0\). Finite-length support does not fix that threshold. A proved bound \(H^1(R_0(n))=0\) gives \(h^0(R_0^{**}(n))-h^0(R_0(n))\) equal to the length of \(Q\) when \(Q\) is zero-dimensional. Vanishing or regularity of the total sheaf is not that certificate. Without any vanishing the difference is at most the length of \(Q\), so a nonzero difference at a single \(n\) certifies \(Q\ne 0\). Only a zero, or an exact length, needs that bound. The local length of \(Q\) at \(([0:1],[0:0:0:1])\) is the direct computation. As of the earlier checkpoint, before 6104798062, that length was uncomputed. For the fixed chosen carrier the direct computation is the certified value \(\operatorname{length}_B(Q)=12\), which excludes G2 for this carrier only and leaves G1 passed and retained.
- Or stalk self-duality is opened as a separate gate. At that point, \(M\cong M^*\) is the localization of \(R\cong R^*\otimes L\) after trivializing \(L\).
- Or confinement is treated as an absent theorem. The hull argument is supplied, pending artifact review.

The ordinary smooth hull, the automatic vanishing of ordinary \(\sigma\) on the full-sign sector, Corollaire 3.4 for an already locally free formal sheaf, and the depth relation of Lemma 0BUW once its two hypotheses hold, are not branches of this tree. They are settled statements.

## 9. FMEA

Severity is an integer from \(1\) to \(5\). Severity \(5\) is a false promotion, or a genuine obstruction reported as an open computation. Severity \(3\) is a kill test reported as progress. Detection names the gate that sees the failure. Occurrence is not scored: several of these modes are documents that do not yet exist.

| Failure mode | Effect | Cause | Detection | Severity |
|---|---|---|---|---|
| \(O_{\mathrm{full}}=0\) reported as all-order unobstructedness | Horrocks–Mumford route promoted with no mechanism | L2 pass read as promotion | Section 6; L2 forbids promotion | 5 |
| Ordinary \(\sigma\) declared to be the relative cyclic map, or declared injective on the \(352\)-space | A strategy is treated as already compared, or a vacuous kernel is treated as a smoothness theorem | Ordinary \(\sigma\) vanishes on the sector and does not identify the relative cyclic map | Sections 3.2 and 4.1; rank of ordinary \(\sigma\) on the sector is \(0\) | 5 |
| A category or sign error in a write-up treated as exclusion of the setup | A sufficient strategy is confused with a necessary gate, and the setup is retired | Semiregularity, a torsion twist, or a transform used without the comparison | Section 6. Correct or withdraw the argument. Exclusion requires a certified obstruction under the pinned hypotheses | 4 |
| Markman Theorem 1.5.1 cited as a theorem about this \(E\) | The eightfold secant sheaf is confused with the fourfold pullback | Transform strategy assumed | Section 4.2. Withdraw that argument. The setup stays | 3 |
| Bandiera–Lepri–Manetti Theorem 8.2 cited as killing the associative residual | Lie-algebroid hypercohomology substituted for the star-algebroid residual | Comparison of the two obstruction classes not verified | Section 3.4. Sufficient strategy only | 3 |
| Rank \(333\) or kernel dimension \(19\) read as the position of \(O_2\) | Joint-family linear algebra reported as an evaluation of the obstruction | The rank is for \(30\) scalar maps plus \(\ell\). Only two maps are evaluated on \(O_2\); \(\ell(O_2)\) is pending; \(28\) maps are unevaluated. \(\ell(O_2)=0\) alone is not membership in the \(19\)-dimensional joint kernel | Section 3.6 | 4 |
| A named JSON field treated as a new certificate for the exact-\(Q\) tail | A reporting field promoted to a mathematical hypothesis | The exact-\(Q\) elimination already verifies the zero residual tail | Section 3.6 | 2 |
| Coarse \(j\)-line used for the four invariant directions | The extension of \(E\) is not a deformation at the CM point | The coarse moduli space is not fine, and it is ramified at \(j=0\) and \(j=1728\) | L1, versal pointed families | 3 |
| Sign \(b=+15\Pi\) instead of \(b=-15\Pi\) | A nonzero first-order residual, or a cancelled residual reported as nonzero | Gerbe sign opposite the Atiyah contraction | L1 retire observable; first-order calibration | 4 |
| \(Q=0\) reported as the original target theorem, or as a later carrier condition | Total-stalk freeness is over-read as the target theorem, or the central map conditions are treated as passed | Under the verified isolation and regular-parameter hypotheses, with stalk self-duality the localization of \(R\cong R^*\otimes L\), \(Q=0\) proves freeness and the bundle extension, and nothing beyond that. As of the earlier checkpoint, before 6104798062, the length of \(Q\) was uncomputed. For the fixed chosen carrier the certified value is \(\operatorname{length}_B(Q)=12\), so G2 is **EXCLUDED** for this carrier only. That exclusion is not a pass of the original theorem or of the central conditions for other carriers. The central map conditions are not passed by the length certificate | Section 4.5. The warning stops at the original target and later conditions | 5 |
| The checkpoint before 6104798062 reported as the current length of \(Q\), or \(\operatorname{length}_B(Q)=12\) read as settling G1, other carriers, the original theorem, or the Horrocks–Mumford obstruction | A fixed-carrier exclusion is erased, or is over-read | G2 for one frozen carrier confused with an open length, with G1, with other lifts, or with \(O_{\mathrm{full}}\) | Section 4.5. G2 is **EXCLUDED** for this carrier only, by PR #1 comments 6104798062 and 6104803214, the latter an independent SymPy Groebner-basis reproduction. G1 stays passed and retained. Other formal-lift and carrier choices stay open. As of the earlier checkpoint, before 6104798062, the length was uncomputed. The original theorem, the central conditions for other carriers, and the Horrocks–Mumford second-order obstruction computation are not settled | 5 |
| Weight of \(t_0\) reported as unset | A supplied weight reported as missing | The C1 argument not recorded. The supplied value is \(\operatorname{wt}(t_0)=2\), with frame covariance and homogeneous homotopies | L4.C1, status supplied-pending-artifact-review | 3 |
| Corollaire 3.4 applied to a jet, or weights treated as a separate Lefschetz hypothesis | Algebraization claimed for an object that is not the formal sheaf, or a construction step filed as a gap in the theorem | The input is the actual formal locally free sheaf. Weights enter that construction | L4.C2. Corollaire 3.5 does not apply to \(\mathcal{O}(0,1)\) | 4 |
| Hull confinement treated as an absent theorem, or reviewed before its artifact | A supplied argument reported as missing, or used as a pass | C3 is supplied-pending-artifact-review | L4.C3 | 3 |
| Central reflexivity required before testing \(Q\) | The nonzero-\(Q\) branch is excluded by assumption | A conclusion of the test is listed as its prerequisite | Section 4.4. On the torsion-free central fibre, \(Q=0\) establishes central reflexivity. Baseline hypotheses only are checked first | 4 |
| Depth at least \(3\) inferred from reflexivity of \(R\), or demanded as a further theorem | A depth-\(2\) stalk treated as depth \(3\), or Lemma 0BUW replaced by a phantom theorem | \(R\) not distinguished from the central fibre | L4.C4. Reflexivity of \(R\) gives depth at least \(2\). Reflexivity of the fibre follows from \(Q=0\). Then \(\operatorname{depth}(M)=\operatorname{depth}(N)+1\ge 3\) by Lemma 0BUW, and freeness by the stalk lemma | 4 |
| A nonzero full-sign class read as retiring only a vanishing claim, or as excluding every Horrocks–Mumford route | The pinned second-order extension is confused with a single sentence, or with every carrier and every repair | The exclusion is second-order extension of \((X,E,\xi)\), after geometric source identification, closedness, and choice/sign-independence | L2 | 4 |
| A residue modulo \(3\) counted before integral specialization | An uncertified reduction is used as an exclusion | Good reduction of \(X\) and of \(E\), and the functional \(\ell\) over \(\mathbf{Z}_{(3)}\), not yet verified | L2. Until then the mod-\(3\) value is uncertified | 4 |
| Length of \(T\) added to the defect \(N^{**}/N\) | The torsion submodule is counted twice | The sequence \(0\to T\to M\to M^{**}\to N^{**}/N\to 0\) not used | Section 4.4. The defect is \(N^{**}/N\). Do not read the length off an arbitrary twist window | 3 |
| Target written on total stalk instead of central fiber | The written length vanishes for every reflexive total stalk, so a nonfree central fibre is missed | The length is assigned to the total stalk \(M=R_x\) rather than to \(Q=N^{**}/N\) with \(N=M/zM\) | The quantity must be able to be nonzero for some nonfree \(M\) | 4 |
| Stabilization inferred from support | A twist-window zero is read as certifying \(Q=0\) | Finite-length support is treated as a bound on when \(h^0(R_0^{**}(n))-h^0(R_0(n))\) stabilizes. The sheaf \(\mathcal{I}_p(-d)\) on \(\mathbf{P}^3\) has quotient length \(1\) for every \(d\), while the difference is \(0\) for \(n<d\) and \(1\) for \(n\ge d\) | The sequence \(0\to R_0\to R_0^{**}\to Q\to 0\), with \(R_0\) the torsion-free central sheaf and stalk \(N\) over \(B\). A proved bound \(H^1(R_0(n))=0\) gives equality with the length of \(Q\) when \(Q\) is zero-dimensional. Vanishing or regularity of the total sheaf is not that certificate. Or the direct local length of \(Q\) at \(([0:1],[0:0:0:1])\). A twist-window zero alone is not evidence | 4 |
| Zero Hilbert-function difference read as \(Q=0\) without the \(H^1(R_0(n))\) certificate | False pass | A zero of \(h^0(R_0^{**}(n))-h^0(R_0(n))\) is read as \(Q=0\). Without a vanishing, that difference is only at most the length of \(Q\) | A vanishing proof must accompany any claimed zero | 4 |
| \(\sigma(O_{\mathrm{full}})=0\) used as a numerical gate | Computation spent on an identity | The identity holds for every full-sign class | L0; convention check only | 2 |

## 10. Prediction

The prediction under test was that at least two gates above L3 have no available theorem, and that no public source settles the needed comparison.

The comparison is still unsettled, and the count of four necessary gates without theorems does not survive this amendment.

- No model-specific comparison, and no detection or injectivity theorem, has been verified for this varying star-algebroid and its actual obstruction. Ordinary \(\sigma\) does not identify the relative cyclic map. Buchweitz–Flenner, Pridham, both Markman papers, Bandiera–Lepri–Manetti, and Bandiera–Manetti–Meazzini were read against that comparison. Each either addresses a different category or, in the ordinary case, produces a map that vanishes on the \(352\)-dimensional sector. This comparison is a sufficient-strategy gate. It is not necessary for every continuation.
- Semiregularity, the torsion twist, and the eightfold transform are the same kind of strategy gate.
- The weight \(\operatorname{wt}(t_0)=2\), the frame covariance, the homogeneous homotopies, and the confinement argument are supplied, pending artifact review.
- On the torsion-free central fibre the chain is baseline hypotheses, then \(Q\), then central reflexivity, then depth at least \(3\) by Lemma 0BUW, then freeness by the isolated self-dual stalk lemma. Central reflexivity is not a prerequisite for testing \(Q\). Stalk self-duality is the localization of \(R\cong R^*\otimes L\), not a separate gate. As of the earlier checkpoint, before 6104798062, the length of \(Q\) at \(([0:1],[0:0:0:1])\) was uncomputed. For the fixed chosen carrier that length is the certified value \(\operatorname{length}_B(Q)=12\), so G2 is **EXCLUDED** for this carrier only and G1 stays passed and retained. Other formal-lift and carrier choices stay open. The central map conditions are not passed by the length certificate. The original theorem, the central conditions for other carriers, and the Horrocks–Mumford second-order obstruction computation are not settled by this result. Finite-length support does not bound the twist at which the section difference stabilizes. A further depth-upgrade theorem is not required.
- Corollaire 3.4 is relative effective Lefschetz, and the pair \((\mathbf{P}^1\times\mathbf{P}^3,\mathcal{O}(0,1))\) meets its geometric hypotheses for an actual formal locally free sheaf. The open carrier construction question is the reviewed artifact of that sheaf. Weights enter the construction. They are not a separate Lefschetz hypothesis. The absolute statement, Corollaire 3.5, does not apply to \(\mathcal{O}(0,1)\).

## 11. Sources read

- Buchweitz–Flenner, arXiv:math/9912245, Definition 4.1, Proposition 4.4, Corollary 4.3, Theorem 5.1, Theorem 7.2, Theorem 7.3.
- Pridham, arXiv:1208.3111, Corollary 1.20, Corollaries 2.24 and 2.25, Remark 2.26.
- Markman, arXiv:2502.03415, Section 7.1, Definition 7.3.5, Conjecture 7.3.9, Section 7.4, Theorem 1.5.1, Section 8.3, Lemma 8.3.4, Remark 8.3.5.
- Markman, arXiv:2509.23403v2, Theorem 1.2, Theorem 2.1, Lemma 11.3, Question 11.4, Section 12.
- Bandiera–Lepri–Manetti, arXiv:2208.00694, Theorem 4.4, Theorem 8.2.
- Bandiera–Manetti–Meazzini, Moscow Mathematical Journal 22 (2022), no. 2, 239–263, main theorem as stated in the abstract: formality for a polystable sheaf on a smooth projective surface is equivalent to quadraticity of the Kuranishi family.
- D'Agnolo–Schapira, arXiv:math/0506064, Section 3.
- Yekutieli, arXiv:0905.0488.
- Bressler–Gorokhovsky–Nest–Tsygan, arXiv:0810.0030.
- Lowen, arXiv:0707.2602.
- Grothendieck, SGA 2, Exposé XII, Corollaire 3.4 and Corollaire 3.5, arXiv:math/0511279, pages 127–128.
- Abe–Yoshinaga, RIMS preprint 1496, Theorem 0.2, Proposition 1.2, Corollary 1.3.
- Stacks Project, Proposition [00O7](https://stacks.math.columbia.edu/tag/00O7), Lemma [00LX](https://stacks.math.columbia.edu/tag/00LX), Lemma [090R](https://stacks.math.columbia.edu/tag/090R), Lemma [0EBJ](https://stacks.math.columbia.edu/tag/0EBJ), and Lemma [0BUW](https://stacks.math.columbia.edu/tag/0BUW) (Lemma 47.11.3).
- Milne, *Algebraic Groups*, Theorem 14.12 and Remark 14.13, for the statement that algebraic \(\mathbf{G}_m\)-representations remain \(\mathbf{Z}\)-graded, as used in the supplied homotopy argument.
- Talpo–Vistoli, arXiv:1006.0497, Proposition 6.36, for the ordinary hull only.
- Supplied carrier arguments: PR #1, comments 6104475229 and 6104506387.
- Fixed-carrier central defect: PR #1, comment [6104798062](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6104798062), \(\operatorname{length}_B(Q)=12\) for this carrier, excluding G2 for this carrier only and retaining G1. Independent SymPy Groebner-basis reproduction: PR #1, comment [6104803214](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6104803214). As of the earlier checkpoint, before 6104798062, that length was uncomputed. The original theorem, the central conditions for other carriers, and the Horrocks–Mumford second-order obstruction computation are not settled by these certificates.
