# Theorem-and-map audit and gate ladder

Status: an audit of published theorems against two deformation problems. No value of the ambient second-order class is computed here, and no length computation for the carrier module is repeated. Nothing in this note promotes either route.

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

The comparison that would be needed, and that is not in the sources below, is the following statement.

> Comparison statement, not a theorem. Let \(\mathcal{A}\) be a star-algebroid on \(X\) extending \(\xi\), and let \(o\in\operatorname{Ext}^2(E,E)_\chi\) be the obstruction to lifting \(E\) to an \(\mathcal{A}\)-module. There is a published semiregularity map, or another named all-order map, defined on this obstruction, whose restriction to the \(352\)-dimensional sector is not the zero map, and whose kernel does not contain that sector.

Every source checked either addresses a different category, or lands in a kernel that already contains the sector.

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
- Corollary 1.20 extends the vanishing \(\mathsf{I}\mathcal{L}(o)=0\) to perfect complexes over an admissible dg subcategory of the perfect complexes on a smooth proper scheme. The remark following it allows a quasi-coherent presheaf of simplicial associative algebras. This is the closest public noncommutative statement. Its conclusion is that a cyclic-homology image of the obstruction vanishes. It does not prove injectivity on \(\operatorname{Ext}^2(E,E)_\chi\). The ordinary specialization of that image is already zero on the sector, so the conclusion is the one already recorded in Section 1.

### 3.3. Markman, arXiv:2502.03415 and arXiv:2509.23403

- arXiv:2502.03415, Section 7.1, recalls the ordinary semiregularity map. That is the map which vanishes on the \(352\)-space.
- Definition 7.3.5 and the surrounding discussion extend the Atiyah class to a sheaf twisted by a \(\mu_r\)-cocycle. Conjecture 7.3.9 asks for the Buchweitz–Flenner extension theorem in that twisted setting. Section 7.4 proves the conjecture when the base is a family of abelian varieties and the Brauer class extends to a projective bundle on the total space. The sheaves to which the proof applies are not \(E\). The construction that Markman proves semiregular, in Section 9, is an equivariant reflexive sheaf built from ideal sheaves of translates of an Abel–Jacobi curve on a Jacobian, descended to a quotient and twisted by \(\mu_{8d}\).
- The global consequence used for Weil classes is Theorem 1.5.1 of that paper: algebraicity for abelian sixfolds of Weil type of discriminant \(-1\), for every imaginary quadratic field, and then for every abelian fourfold of Weil type by Schoen's degeneration. The input sheaf is the secant sheaf just described.
- arXiv:2509.23403, Theorem 1.2, quotes that result. Its Sections 2–10 set up secant sheaves and Orlov's equivalence \(D^b(X\times X)\to D^b(X\times\widehat{X})\) for a general CM field. The algebraicity conclusion is conditional on semiregularity of the resulting object, and the paper states that this semiregularity is not established beyond the imaginary-quadratic range already treated. Section 12 asks for a stronger semiregularity theorem in dimension at least \(8\) and does not prove one.

No theorem in either paper takes the Horrocks–Mumford pullback, the class \(\xi\), or the residual \(O_{\mathrm{full}}\) as input. The eightfold object in these papers is not this \(E\).

### 3.4. Lie-algebroid and formality statements

Bandiera–Lepri–Manetti, arXiv:2208.00694:

- Theorem 4.4: for a locally free module over a Lie algebroid \(\mathcal{A}\), the Thom–Whitney totalization of \(\Omega^*(\mathcal{A},\mathcal{E}nd(E))\) controls deformations as an \(\mathcal{A}\)-module. The obstruction space is Lie-algebroid hypercohomology \(\mathbb{H}^2(\mathcal{A};\mathcal{E}nd(E))\).
- Theorem 8.2: for a Lie pair \(\mathcal{A}\subset\mathcal{L}\) and a locally free \(\mathcal{A}\)-module, the composite of the semiregularity map with the map into the truncated quotient of \(\Omega^*(\mathcal{L})\) annihilates those obstructions. If the Leray spectral sequence of the pair degenerates at \(E_1\), each semiregularity component itself annihilates obstructions.

The ambient residual is the failure of an associative module equation over a star product, after the D'Agnolo–Schapira descent. A Lie-algebroid module structure sees a flat connection along an anchor, not the order-\(h^2\) associative terms \(\mu_2\), \(T(g)\), and \(b^2\). No theorem identifies \(C_2\) with a class in \(\mathbb{H}^2(\mathcal{A};\mathcal{E}nd(E))\). Even under such an identification, annihilation by a map that factors through the ordinary \(\sigma\) would again be automatic on the full-sign sector.

Bandiera–Manetti–Meazzini, *Deformations of polystable sheaves on surfaces: quadraticity implies formality*, Moscow Mathematical Journal 22 (2022), no. 2, 239–263: for a polystable coherent sheaf on a smooth complex projective surface, the differential graded Lie algebra of derived endomorphisms is formal if and only if the Kuranishi family is quadratic. The base here is a fourfold, the category is the star-algebroid category rather than the ordinary sheaf category, and the ordinary hull is already a power-series ring. The surface theorem does not apply.

### 3.5. Sources that define the category and do not kill the obstruction

These are the sources that match the category actually in use. None of them asserts vanishing of \(O_{\mathrm{full}}\).

- D'Agnolo–Schapira, arXiv:math/0506064, Section 3: algebra-isomorphism and triple-unit descent for a quantized algebroid, and the module equation. Their existence theorem is for Lagrangian submanifolds, not for this rank-two bundle.
- Yekutieli, arXiv:0905.0488: twisted deformation quantization and crossed-groupoid descent on algebraic varieties. It does not force the module obstruction to vanish.
- Bressler–Gorokhovsky–Nest–Tsygan, arXiv:0810.0030: the Deligne groupoid of an algebroid stack. It identifies the deformation problem; it does not solve this instance.
- Lowen, arXiv:0707.2602: the characteristic morphism from Hochschild cohomology to the obstruction of deforming an object. This is the evaluation \(\operatorname{ev}_E\) used to compare two ambient lifts. It computes neither lift.

## 4. Unproved hypotheses

Listed here, before any retire or promote rule. An open item blocks promotion. A proved-false item retires the route that needs it.

### Horrocks–Mumford route

- **H1.** The ambient residual \(C_2\) equals the obstruction class of \(E\) in one of the categories of Section 3.1–3.4. Open. This is the comparison statement. No cited theorem proves it.
- **H2.** After any such comparison, the image of the \(352\)-dimensional sector is not forced into the kernel of the target map. Open, and in conflict with every ordinary specialization: those maps vanish on the sector.
- **H3.** Some named theorem then kills every higher-order obstruction of the star-algebroid module, rather than only placing the second-order class in a kernel that contains the sector. Open. No such theorem was found.
- **H4.** The infinitesimal gerbe class \(15\Pi\) may be replaced by a \(\mu_r\)-twist to which Markman, Section 7.4, or Pridham, Remark 2.26, applies. Open, and not implied by those statements. Their cocycle is torsion.
- **H5.** An Orlov transform of \(E\), or of a deformation of \(E\), is one of the semiregular secant sheaves of Markman, arXiv:2502.03415, Section 9, or satisfies the semiregularity hypothesis left open in arXiv:2509.23403. Open. The constructions differ, and the discriminants are not matched by any cited comparison.

H1 and H3 are the two obligations that sit above the kill test. Both lack a theorem. H2 is the reason an ordinary semiregularity theorem cannot be substituted for them.

### Carrier-continuation route

The proposed all-order mechanism has three layers: a weight vanishing for the normal jet, algebraization by effective Lefschetz, and an isolated-defect criterion for the reflexive hull. The weight-slot arithmetic is not recomputed in this note.

- **C1. Equivariance.** The \(\mathbf{G}_m\)-action of weights \((2,1,1,0,-1)\) on \((z,X,Y,W,h)\) preserves \(L\), the ideal sheaf of \(D\), the cover, and the structured lift \((\alpha,v,\beta)\). In particular \(\beta(v)=+t_0 h\) is homogeneous, so the weight of \(t_0\) plus the weight \(-1\) of \(h\) equals the weight required by the section equation. Open. No cited source fixes \(\operatorname{wt}(t_0)\).
- **C2. Input to Lefschetz.** The homogeneous jet continuation defines a locally free coherent sheaf on the formal completion of \(\mathbf{P}^1\times\mathbf{P}^3\) along \(D\), which is the input category of the theorem in Section 5. Open. Vanishing of graded pieces \(H^2(\operatorname{Sym}^2 B\otimes L^{-1}I^k)\) for \(k\ge 7\) is not that sheaf.
- **C3. Confinement.** The non-free locus of the reflexive hull \(R^{**}\), not merely of \(R\), is closed and \(\mathbf{G}_m\)-stable, and the flat-limit argument places it at the single point \(o=[0:0:0:1]\). Open. Abe–Yoshinaga, Theorem 0.2, is a splitting criterion for reflexive sheaves on \(\mathbf{P}^n\), \(n\ge 3\), and does not address this locus. Stacks Project, Lemma 0EBJ, extends reflexive sheaves across a closed set whose local rings have depth at least \(2\); it does not confine the locus.
- **C4. Depth upgrade.** At the stalk at \(o\), reflexivity of \(R_0\) is taken to give \(\operatorname{depth}(R)\ge 3\). Open, and not the published bound. Abe–Yoshinaga, Proposition 1.2, gives depth at least \(2\) at points of dimension at least \(2\), and Corollary 1.3 gives codimension at least \(3\) for the non-free locus. Stacks Project, Proposition 00O7, gives a free resolution of length \(d-e\) for a finite module of depth \(e\) over a regular local ring of dimension \(d\). A second syzygy of a nonzero finite-length module over a \(4\)-dimensional regular local ring therefore has depth \(2\). A contradiction with alternating self-duality needs an input of depth at least \(3\), which reflexivity does not supply.

C1 and C2 are independent of the length of \(Q=R_0^{**}/R_0\). C3 and C4 are the reason that length, once computed, is not yet a local-freeness theorem.

## 5. The Lefschetz input that does exist

SGA 2, Exposé XII, Corollaire 3.4, as printed on page 127 of arXiv:math/0511279, is the relative statement. It is not the absolute ample statement. The absolute statement is Corollaire 3.5 on the following page. In the recomposed HTML edition the same pair is Corollaire 42.4 and Corollaire 42.5.

Corollaire 3.4 assumes a projective flat morphism \(f:X\to S\) to a locally Noetherian base, an invertible sheaf \(\mathcal{O}_X(1)\) ample relative to \(S\), and a section \(t\) whose restriction to every fibre is regular. Let \(X_0\) be the zero scheme of \(t\). Assume that every fibre of \(X_0\) has depth at least \(2\) at its closed points and every fibre of \(X\) has depth at least \(2\) at its closed points. Then the pair \((X,X_0)\) satisfies effective Lefschetz:

1. For every open neighborhood \(U\) of \(X_0\), completion is fully faithful on locally free coherent sheaves.
2. Every locally free coherent sheaf on the formal completion along \(X_0\) is the completion of a locally free coherent sheaf on some open neighborhood of \(X_0\).

For \(X=\mathbf{P}^1\times\mathbf{P}^3\), \(S=\mathbf{P}^1\), and \(\mathcal{O}_X(1)=\mathcal{O}(0,1)\), relative ampleness holds, and \(D=\mathbf{P}^1\times\mathbf{P}^2\) is the zero scheme of a relative hyperplane section. The depth bounds hold because the fibres are \(\mathbf{P}^3\) and \(\mathbf{P}^2\). The base \(\mathbf{P}^1\) is Noetherian and carries an ample line bundle, which is the gluing hypothesis used in the proof of the corollary. So Corollaire 3.4 applies to the pair \((X,D)\) inside its stated category: locally free sheaves on the formal completion.

It does not apply to a finite normal jet, to a complex that is only reflexive, or to a lift whose \(\mathbf{G}_m\)-weights have not been checked. Granting Corollaire 3.4 does not discharge C1, C2, C3, or C4.

Abe–Yoshinaga, RIMS preprint 1496, Theorem 0.2: a reflexive sheaf on \(\mathbf{P}^n\), \(n\ge 3\), splits as a sum of line bundles if and only if its restriction to some hyperplane does. The carrier lives on a product of projective spaces and is not claimed to split. The theorem is not a confinement statement.

## 6. Retire / promote rule

This rule is applied only after the hypotheses of Section 4.

A route is promoted only when L0, L1, L2, and L3 have passed for that route and every L4 gate of that route has passed. A pass of L2 is never a promotion. In particular, neither route is promoted by \(O_{\mathrm{full}}=0\), by \(\sigma(O_{\mathrm{full}})=0\), or by \(Q=0\).

A route is retired when any one of its gates records the retire observable of that gate. Retirement is not reversed by a later vanishing. An open hypothesis, or an L4 gate with no theorem, blocks promotion and does not retire.

## 7. Gate ladder

### L0 — Category

| Route | Pass observable | Retire observable | Promotion |
|---|---|---|---|
| Horrocks–Mumford | The object is the star-algebroid module residual \(O_{\mathrm{full}}\in\operatorname{Ext}^2(E,E)_\chi\). | The writeup treats \(O_{\mathrm{full}}\) as an ordinary Yoneda class, as a \(\mu_r\)-twisted class, or as the obstruction of a Markman secant sheaf, without proving H1 or H5. | None at L0. |
| Carrier continuation | The object is the structured rank-four data on \(\mathbf{P}^1\times\mathbf{P}^3\), kept distinct from \(E\). | The writeup identifies this construction with the Horrocks–Mumford pullback or with the eightfold secant sheaf. | None at L0. |

L0 passes for both routes on the descriptions fixed above.

### L1 — First-order necessity

| Route | Pass observable | Retire observable | Promotion |
|---|---|---|---|
| Horrocks–Mumford | \(\operatorname{ev}_E(\xi)=0\), with gerbe sign \(b=-15\Pi\). | A certified nonzero value of \(\operatorname{ev}_E(\xi)\). | None. |
| Carrier continuation | The sixth normal jet satisfies the cocycle, symplectic, and section equations, in a pinned certificate. | A published counterexample to one of those three equations. | None. |

The Horrocks–Mumford pass is the first-order cancellation already recorded. This note does not recompute it. The carrier pass is not claimed here; that gate stays open, which blocks promotion and does not retire.

### L2 — Kill test

| Route | Pass observable | Retire observable | Promotion |
|---|---|---|---|
| Horrocks–Mumford | \(O_{\mathrm{full}}=0\) in the \(352\)-dimensional space. | \(O_{\mathrm{full}}\ne 0\). | Forbidden. A zero is one necessary test. |
| Carrier continuation | \(Q=R_0^{**}/R_0=0\), after C3 and C4 have passed. | \(Q\ne 0\) at the stalk at \(o\), after C3 has passed. | Forbidden. |

Neither class is evaluated in this note. Both L2 gates stay open.

### L3 — Hypothesis sheet

L3 passes for a route only when every hypothesis that route uses is marked proved. L3 retires the route when any such hypothesis is proved false.

| Hypothesis | Mark | Effect on L3 |
|---|---|---|
| H1–H5 | Open | Horrocks–Mumford L3 does not pass. |
| C1–C4 | Open | Carrier L3 does not pass. |
| SGA 2, XII, Corollaire 3.4, for locally free formal sheaves on \((\mathbf{P}^1\times\mathbf{P}^3,D)\) | Proved external input | Available to the carrier route, and not a substitute for C1–C4. |

### L4 — Gates above L3

These are the theorem obligations that remain after L0–L3. A gate passes only by a cited theorem whose hypotheses are satisfied by the object of that route.

| Gate | Obligation | Theorem available? |
|---|---|---|
| L4.H1 | Prove H1: identify the star-algebroid residual with the input of some theorem in Section 3. | No. |
| L4.H2 | Prove H3: an all-order vanishing theorem whose map is not identically zero on the \(352\)-space. | No. Ordinary \(\sigma\) is identically zero there, so Buchweitz–Flenner Theorems 7.2 and 7.3, Pridham Corollaries 2.24 and 2.25, and Markman Section 7.4 do not fill this gate. |
| L4.C1 | Prove C1 and C2: \(\mathbf{G}_m\)-homogeneous \(\beta(v)=+t_0 h\), and a locally free formal sheaf to which Corollaire 3.4 applies. | No. Corollaire 3.4 is the target statement, not this identification. |
| L4.C2 | Prove C3 and C4: confinement of the non-free locus of the reflexive hull to \(o\), and depth at least \(3\) at that stalk. | No. Proposition 00O7 and Lemma 0EBJ supply the homological algebra around the stalk, not these two inputs. |

Four gates above L3 have no theorem. The comparison gate is L4.H1.

## 8. Fault tree

Top event: a route is reported as promoted, or as all-order unobstructed, without a pass of its L4 gates.

Horrocks–Mumford branch.

- \(O_{\mathrm{full}}=0\) is read as promotion. Blocked by the rule in Section 6 and by L2.
- Or ordinary \(\sigma\) is read as an all-order mechanism. The map is zero on the sector, so every class lies in the kernel. Blocked by Section 1 and by L4.H2.
- Or a \(\mu_r\) theorem is applied to \(15\Pi\). The cocycle orders differ. This is H4, still open, and it is not a pass of L4.H1.
- Or the Orlov transform of \(E\) is treated as Markman's semiregular secant sheaf. This is H5, still open.
- Or a Lie-algebroid semiregularity theorem is applied to the associative residual. Theorem 8.2 of arXiv:2208.00694 controls a different DGLA. This is part of H1.

Carrier branch.

- \(Q=0\) is read as promotion. Blocked by L2.
- Or the sixth jet is fed to Corollaire 3.4 as if it were a locally free sheaf on the formal completion. That identification is C2, still open. The corollary itself is not the failure; the input mismatch is.
- Or the section equation is treated as homogeneous while \(\operatorname{wt}(t_0 h)\) is unchecked. This is C1.
- Or the depth contradiction is run with the reflexive bound. Reflexivity gives depth at least \(2\), and the second syzygy also has depth \(2\), so there is no contradiction until C4 is proved.
- Or the non-free locus of \(R\), rather than of \(R^{**}\), is the locus that is shown to be \(\mathbf{G}_m\)-stable. This is C3.

The ordinary smooth hull, the automatic vanishing of \(\sigma\) on the full-sign sector, and Corollaire 3.4 for an already locally free formal sheaf are not branches of this tree. They are settled statements about different objects.

## 9. FMEA

Severity is an integer from \(1\) to \(5\). Severity \(5\) is a false promotion, or a genuine obstruction reported as an open computation. Severity \(3\) is a kill test reported as progress. Detection names the gate that sees the failure. Occurrence is not scored: several of these modes are documents that do not yet exist.

| Failure mode | Effect | Cause | Detection | Severity |
|---|---|---|---|---|
| \(O_{\mathrm{full}}=0\) reported as all-order unobstructedness | Horrocks–Mumford route promoted with no mechanism | L2 pass read as an L4 pass | Section 6; L2 column forbids promotion | 5 |
| Ordinary \(\sigma\) declared injective on the \(352\)-space | A vacuous kernel is treated as a smoothness theorem | Serre duality with the \(\chi\)-volume pairs the sector with invariant vector fields that extend \(E\) | L0 and L4.H2; rank of \(\sigma\) on the sector is \(0\) | 5 |
| Star-algebroid residual identified with an ordinary or \(\mu_r\) obstruction | A theorem from the wrong category is quoted as H1 | H1 assumed instead of proved | L4.H1; comparison statement unmatched | 5 |
| Markman Theorem 1.5.1 cited as a theorem about this \(E\) | The eightfold secant sheaf is confused with the fourfold pullback | H5 assumed | L0 retire observable; Section 3.3 | 4 |
| Bandiera–Lepri–Manetti Theorem 8.2 cited as killing \(C_2\) | Lie-algebroid hypercohomology substituted for the associative residual | No comparison of the two DGLAs | L4.H1 | 4 |
| Coarse \(j\)-line used for the four invariant directions | The extension of \(E\) is not a deformation at the CM point | The coarse moduli space is not fine, and it is ramified at \(j=0\) and \(j=1728\) | L1, versal pointed families | 3 |
| Sign \(b=+15\Pi\) instead of \(b=-15\Pi\) | A nonzero first-order residual, or a cancelled residual reported as nonzero | Gerbe sign opposite the Atiyah contraction | L1 retire observable; first-order calibration | 4 |
| \(Q=0\) reported as an algebraic vector bundle | Carrier route promoted | L2 pass read as L4 | Section 6 | 5 |
| Weight of \(\beta(v)=t_0 h\) off by the weight of \(h\) | The section obstruction is placed in the wrong weight, and the \(k\ge 7\) vanishing moves | C1 unchecked; \(h\) has weight \(-1\) | L4.C1 | 4 |
| Corollaire 3.4 applied to the sixth jet | Algebraization claimed for an object outside the input category | C2 unchecked. The corollary wants a locally free formal sheaf | L4.C1. Corollaire 3.5, the absolute ample case, is the wrong citation and does not apply to \(\mathcal{O}(0,1)\) | 4 |
| Non-free locus of \(R\) confined, locus of \(R^{**}\) not checked | A singularity of the hull survives outside \(o\) | Flat limit used on \(R\) only; C3 | L4.C2 | 4 |
| Depth at least \(3\) inferred from reflexivity | The syzygy contradiction does not fire; a non-free stalk of depth \(2\) survives | C4. The published bound is depth at least \(2\) | L4.C2, against Abe–Yoshinaga Proposition 1.2 and Proposition 00O7 | 5 |
| \(\sigma(O_{\mathrm{full}})=0\) used as a numerical gate | Computation spent on an identity | The identity holds for every full-sign class | L0; convention check only | 2 |

## 10. Prediction

The prediction was that at least two gates above L3 have no available theorem, and that no public source settles the needed comparison.

It holds. The gates above L3 are L4.H1, L4.H2, L4.C1, and L4.C2. All four lack a theorem. The comparison is L4.H1. Buchweitz–Flenner, Pridham, both Markman papers, Bandiera–Lepri–Manetti, and Bandiera–Manetti–Meazzini were read against that gate. Each either addresses a different category or produces a map that vanishes on the \(352\)-dimensional sector.

One nearby theorem does exist and was easy to mis-file. SGA 2, Exposé XII, Corollaire 3.4 is relative effective Lefschetz for a relatively ample divisor, and the pair \((\mathbf{P}^1\times\mathbf{P}^3,\mathcal{O}(0,1))\) meets its geometric hypotheses. It sits at L3 as an external input. It is not one of the four gates above L3, because those gates ask for the jet, the weight of \(\beta(v)\), and the reflexive hull, which the corollary does not provide.

## 11. Sources read

- Buchweitz–Flenner, arXiv:math/9912245, Definition 4.1, Proposition 4.4, Corollary 4.3, Theorem 5.1, Theorem 7.2, Theorem 7.3.
- Pridham, arXiv:1208.3111, Corollary 1.20, Corollaries 2.24 and 2.25, Remark 2.26.
- Markman, arXiv:2502.03415, Section 7.1, Definition 7.3.5, Conjecture 7.3.9, Section 7.4, Theorem 1.5.1.
- Markman, arXiv:2509.23403, Theorem 1.2, Theorem 2.1, Section 12.
- Bandiera–Lepri–Manetti, arXiv:2208.00694, Theorem 4.4, Theorem 8.2.
- Bandiera–Manetti–Meazzini, Moscow Mathematical Journal 22 (2022), no. 2, 239–263, main theorem as stated in the abstract: formality for a polystable sheaf on a smooth projective surface is equivalent to quadraticity of the Kuranishi family.
- D'Agnolo–Schapira, arXiv:math/0506064, Section 3.
- Yekutieli, arXiv:0905.0488.
- Bressler–Gorokhovsky–Nest–Tsygan, arXiv:0810.0030.
- Lowen, arXiv:0707.2602.
- Grothendieck, SGA 2, Exposé XII, Corollaire 3.4 and Corollaire 3.5, arXiv:math/0511279, pages 127–128.
- Abe–Yoshinaga, RIMS preprint 1496, Theorem 0.2, Proposition 1.2, Corollary 1.3.
- Stacks Project, Proposition [00O7](https://stacks.math.columbia.edu/tag/00O7) and Lemma [0EBJ](https://stacks.math.columbia.edu/tag/0EBJ).
- Talpo–Vistoli, arXiv:1006.0497, Proposition 6.36, for the ordinary hull only.
