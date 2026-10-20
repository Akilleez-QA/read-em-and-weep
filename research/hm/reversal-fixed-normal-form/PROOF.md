# Reversal-fixed marked classes and a parity normal-form criterion

## 0. Statement and scope

Retain the exact marked setting of PR436 and PR438: a connected complex abelian variety \(X\), geometric inversion \(\iota\) fixing \(h\), the stipulated individually inversion-stable affine acyclic cover, and regular normalized differential descent cochains, including arity zero. Fix a literal reversal-compatible presentation \(P\) modulo \(h^M\), \(M\geq3\). All higher product, overlap-map, and triple-unit coefficients may vary. Every equivalence is invariant and literally the identity modulo \(h^M\). Each differential coefficient has finite order; no uniform order bound is required.

Write \(R_n,U_n\) for the parity and unrestricted marked object-class sets modulo \(h^n\), respectively, and \(J_n:R_n\to U_n\) for forgetting parity, as in PR438. Use arbitrary inner chart 2-units in the unrestricted category. The parity category can use unitary chart 2-units; enlarging its 2-unit convention does not change its object classes.

There is a natural involution \(\mathcal I\) on the unrestricted presentation and gauge category, defined by reversal of the formal parameter combined with passage to opposite products. It does not reverse the Čech indices:

\[
\begin{aligned}
\mu_i^{\mathcal I}(f,g)&=\tau\bigl(\mu_i(\tau g,\tau f)\bigr),&
F_{ij}^{\mathcal I}&=\tau F_{ij}\tau,&
A_{ijk}^{\mathcal I}&=\tau(A_{ijk}^{-1}),\\
E_i^{\mathcal I}&=\tau E_i\tau,&
B_{ij}^{\mathcal I}&=\tau(B_{ij}^{-1}),&
C_i^{\mathcal I}&=\tau(C_i^{-1}),
\end{aligned}
\]

where \(\tau(h)=-h\), \(\tau\) fixes ordinary functions, and each inverse uses its indicated source product. It induces involutions on \(U_n\) and \(U_\infty\).

**Theorem.** Under the literal parity-continuation premise retained by PR416, and the other hypotheses above,

\[
J_n(R_n)=U_n^{\mathcal I}\quad(n\geq M),\qquad
J_\infty(R_\infty)=U_\infty^{\mathcal I}.
\]

The maps \(J_n,J_\infty\) are already known to be injective from PR438. Thus a marked unrestricted formal presentation has a parity representative if and only if it is marked-equivalent to its reversed opposite. Equivalently, this happens if and only if every finite truncation is equivalent to its reversed opposite.

This is a theorem about fixed **object classes**. A fixed class means that some marked equivalence \(x\to\mathcal I x\) exists. No square-one equation or chosen coherence for that equivalence is imposed. The theorem does not classify coherent involutive 2-actions, homotopy fixed-point data, unmarked objects, or non-invariant equivalences.

The new work is the exact noncommutative involution, its affine action on genuine finite class fibers, and identification of the previously proper parity image as precisely its fixed locus. PR425 gives a one-step subspace, PR436 gives the parity tower, and PR438 gives forgetful injectivity and finite detection; none of those cited results identifies the image with reversal-fixed classes.

## 1. Source pins and imported results

All repository links below are pinned to the specified commits.

1. [PR425 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/df433cdd359fa9c7750bf9c8b9765229eac534f6/research/hm/reversal-relative-lift-freedom/PROOF.md), commit `df433cdd359fa9c7750bf9c8b9765229eac534f6`, Sections 2–6: the exact top difference equations, gauge and 2-unit formulas, unrestricted \(HH^2\)-torsor, and injective one-step parity image.
2. [PR436 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/502c978a17cd7037d740d4d08d373c1cb8bd5829/research/hm/formal-parity-tower/PROOF.md), commit `502c978a17cd7037d740d4d08d373c1cb8bd5829`: Lemma 2.1, lines 70–86, lifts parity coordinate and unit data; Lemma 3.1 and Corollary 3.2, lines 96–118, remove full lower parity automorphisms and align gauges; Section 4, lines 120–134, identifies genuine parity fibers; Section 5, lines 136–164, proves the parity formal/inverse-limit bijection.
3. [PR438 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/971c16a67b1e7d12fce0a8e2d2165ca4839911de/research/hm/formal-forgetful-comparison/PROOF.md), commit `971c16a67b1e7d12fce0a8e2d2165ca4839911de`: Lemmas 2.1–2.2, lines 50–77, remove full lower unrestricted automorphisms and align existing upper equivalences; Theorem 3.2, lines 91–103, proves finite injectivity; Lemma 4.1 and Theorems 4.2–4.3, lines 105–129, prove unrestricted inverse-limit comparison, formal injectivity, and finite detection of the image.
4. [PR416 literal parity continuation](https://github.com/Akilleez-QA/read-em-and-weep/blob/c71356722bc7bd1a426d26ea0ca6d050f4c3ed81/research/hm/parity-separated-ambient-lifting/REVERSAL-COMPATIBLE-CONTINUATION.md), commit `c71356722bc7bd1a426d26ea0ca6d050f4c3ed81`, retaining the [invariant literal small-extension input](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6259748725). The explicit source application is the stipulated elliptic fourfold; the general abelian statement remains conditional on the same literal lifting premise.
5. The current coordination record distinguishes these earlier results: [PR425 announcement](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6287045361), [PR436 announcement](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6289938301), [PR438 announcement](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6290072077), and [scoped review](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6290132737). These are coordination evidence, not substitutes for the pinned proofs.

The main imported vanishing is
\[
H^0(T_X)^\iota=H^1(\mathcal O_X)^\iota=0.
\]
PR438 upgrades it from top-layer vanishing to actual 2-triviality of every full finite relative unrestricted automorphism. It is that upgrade, not only the displayed groups, that will remove the ambiguity in the finite fiber.

## 2. The reversed opposite is an exact involution

Write \(*\) for a source local product and \(\diamond\) for its reversed opposite. Directly from the definition,
\[
\tau(a*b)=\tau(b)\diamond\tau(a).
\tag{2.1}
\]
Thus \(\tau\) is a semilinear anti-isomorphism from the source algebra to its reversed opposite. In particular, although \(\tau\) is anti-multiplicative, the unit map
\[
d_x(a):=\tau(a^{-1})
\tag{2.2}
\]
is a **group homomorphism**:
\[
d_x(a*b)=d_x(a)\diamond d_x(b).
\tag{2.3}
\]
It also satisfies
\[
\tau\operatorname{Ad}_*(a)\tau
 =\operatorname{Ad}_\diamond(d_x(a)),\qquad
d_x(F(a))=F^{\mathcal I}(d_y(a))
\tag{2.4}
\]
for an algebra map \(F:y\to x\). These identities determine the required inversions and preserve the order of unit factors.

### 2.1 Descent, including the pentagon

The source descent equations are
\[
F_{ij}F_{jk}=\operatorname{Ad}_i(A_{ijk})F_{ik},\qquad
A_{ijk}*_i A_{ikl}=F_{ij}(A_{jkl})*_i A_{ijl}.
\tag{2.5}
\]
Conjugating the first by \(\tau\) and using (2.4) yields
\[
F_{ij}^{\mathcal I}F_{jk}^{\mathcal I}
 =\operatorname{Ad}_{\diamond_i}(A_{ijk}^{\mathcal I})
   F_{ik}^{\mathcal I}.
\]
Applying the homomorphism \(d_i\) to the second gives exactly
\[
A_{ijk}^{\mathcal I}\diamond_i A_{ikl}^{\mathcal I}
 =F_{ij}^{\mathcal I}(A_{jkl}^{\mathcal I})
   \diamond_i A_{ijl}^{\mathcal I}.
\tag{2.6}
\]
There is no unproved interchange of noncommuting factors.

One can separately check passage to the ordinary opposite before applying parameter reversal. Its triple unit is \(A^{-1}\), not \(A\). In the opposite product the pentagon is
\[
A_{ikl}^{-1}*_i A_{ijk}^{-1}
 =A_{ijl}^{-1}*_i F_{ij}(A_{jkl}^{-1}),
\]
which is precisely the inverse of the source pentagon. This checks the orientation independently.

Associativity and multiplicativity are preserved by opposite and conjugation. Applying \(\mathcal I\) twice returns every product and map. Since an anti-isomorphism preserves the inverse of an individual unit, \(d_{\mathcal I x}d_x(a)=a\); hence the triple units return as well. Classical reductions, normalization, invariance, differential regularity, and the fixed marking are preserved. In particular \(\mathcal I(P)=P\) literally.

### 2.2 Gauge transport and arrow direction

Use the PR425 convention that a gauge \(g=(E,B):x\to y\) means \(y=x^g\), with
\[
\begin{aligned}
\mu_i^y(f,g)&=E_i^{-1}(\mu_i^x(E_i f,E_i g)),\\
F_{ij}^y&=E_i^{-1}\operatorname{Ad}_x(B_{ij})F_{ij}^xE_j,\\
A_{ijk}^y&=E_i^{-1}
  (B_{ij}*_xF_{ij}^x(B_{jk})*_xA_{ijk}^x*_xB_{ik}^{-1}).
\end{aligned}
\tag{2.7}
\]
Thus \(E_i\), as an algebra map, runs from the transported chart algebra to the source chart algebra. With this convention,
\[
\mathcal I(x^g)=(\mathcal I x)^{\mathcal I g},
\qquad
\mathcal I g=(\tau E\tau,d_x(B)).
\tag{2.8}
\]
For the products this is direct conjugation. For the maps it follows from (2.4). For the triple units, \(E_i^{-1}\) is an algebra map between the indicated endpoint products, so
\[
d_y(E_i^{-1}(Z))=(E_i^{\mathcal I})^{-1}(d_x(Z)).
\]
Apply this to the ordered product \(Z\) in (2.7), and use (2.3). Its four factors become, in the same order,
\[
d_x(B_{ij}),\quad F_{ij}^{\mathcal I}(d_x(B_{jk})),\quad
d_x(A_{ijk}),\quad d_x(B_{ik})^{-1}.
\]
This proves the triple-unit formula exactly.

In particular \(\mathcal I\) is covariant on these gauge arrows, not an arrow-reversing operation. For an explicit composition check, if \(g=(E,B):x\to y\) and \(q=(L,K):y\to z\), (2.7) gives
\[
q\circ g=(EL,\ E_i(K_{ij})*_x B_{ij}).
\tag{2.9}
\]
The identities (2.3) and \(d_xE_i=E_i^{\mathcal I}d_y\) show that applying \(\mathcal I\) to (2.9) gives precisely \((\mathcal I q)\circ(\mathcal I g)\). The inverse gauge is \((E^{-1},E_i^{-1}(B_{ij}^{-1}))\), which is preserved in the same fashion. Identity gauges and \(\mathcal I^2=\mathrm{id}\) are literal.

### 2.3 Inner chart 2-units

The PR425 formula for a chart 2-unit \(C\) is
\[
E_i'= \operatorname{Ad}_x(C_i)E_i,\qquad
B_{ij}'=C_i*_xB_{ij}*_xF_{ij}^x(C_j^{-1}).
\tag{2.10}
\]
Using (2.3)–(2.4) sends it to the same formula with
\(\mathcal I C=d_x(C)\), from \(\mathcal I g\) to \(\mathcal I g'\), without exchanging the endpoints. Vertical composition has chart unit \(C' *_x C\), and (2.3) preserves this order. For horizontal composition, chart units \(C:g\Rightarrow g'\) and \(D:q\Rightarrow q'\) combine as
\[
C_i *_x E_i(D_i);
\]
substitution in (2.9)–(2.10) verifies this formula. Its image is
\[
d_x(C_i)\diamond_x E_i^{\mathcal I}(d_y(D_i)),
\]
the horizontal composite of the images. Thus the involution respects the displayed 2-morphism conventions as well.

### 2.4 Strict fixed data

The equality \(x=\mathcal I x\) says exactly
\[
\mu_{r,i}(g,f)=(-1)^r\mu_{r,i}(f,g),\qquad
\tau F_{ij}=F_{ij}\tau,\qquad
\tau(A_{ijk})=A_{ijk}^{-1}.
\tag{2.11}
\]
For the last equivalence one uses the product equality, which makes \(\tau\) an anti-automorphism of the fixed local product. These are precisely the parity object conditions.

Between strict fixed objects, \(g=\mathcal I g\) says exactly that \(E\) is even and \(B\) reversal-unitary. Fixed chart 2-units are precisely reversal-unitary \(C\). Thus the strict fixed 2-data use the unitary convention, not the enlarged parity category with extra ordinary chart 2-units. These are statements about literal fixed data, not yet about fixed classes. A class may be fixed through a non-fixed gauge, so (2.11) alone does not prove the theorem.

## 3. The one-step affine involution

Fix a literal parity presentation \(p\) modulo \(h^n\), \(n\geq M\), and choose a literal parity lift \(o\) modulo \(h^{n+1}\). Existence is the retained PR416 input. Put \(\epsilon=h^n\), so \(\epsilon^2=h\epsilon=0\).

An unrestricted lift differs from \(o\) by
\[
\mu'=\mu+\epsilon u,\qquad F'=F+\epsilon v,\qquad A'=A+\epsilon a.
\]
The pinned PR425 equations and gauge action are
\[
bu=0,\quad\delta u=bv,\quad\delta v=0,\quad\delta a=0;
\qquad
(u,v,a)\longmapsto(u+bt,v+\delta t,a+\delta c).
\tag{3.1}
\]
Consequently the literal unrestricted lift classes form a torsor under
\[
H=H^0(\Lambda^2T_X)^\iota
\oplus H^1(T_X)^\iota
\oplus H^2(\mathcal O_X)^\iota.
\tag{3.2}
\]

Since \(o\) is literally fixed, the involution is linear on differences from this origin. If \(\sigma=(-1)^n\), its exact top action is
\[
(u,v,a)\longmapsto(\sigma u^{\mathrm{op}},\sigma v,-\sigma a).
\tag{3.3}
\]
For the scalar sign, varying the inverse of \(A\) by the top scalar term gives \(-\epsilon a\). Changing the product by \(\epsilon u\) contributes no additional term: its only classical arguments in the inverse equation are \(1,1\), and \(u(1,1)=0\). Parameter reversal supplies the factor \(\sigma\).

The top gauge components transform as
\[
(t,c)\longmapsto(\sigma t,-\sigma c).
\tag{3.4}
\]
Thus (3.3) respects the actual gauge quotient, also directly guaranteed by Section 2.

For clarity, the splitting in (3.2) can be implemented without a hidden formality assumption. The antisymmetrization of \(u\) is a biderivation on each chart. Since \(bv\) is symmetric, these biderivations glue to a global bivector \(w\). Write \(u=w+bt\) using local normalized differential Hochschild primitives, averaged to be invariant. Gauge by \(-t\); then \(v-\delta t\) is a derivation-valued Čech 1-cocycle. The scalar Čech class of \(a\) is independent. This represents each class by \((w,z,a)\) with \(w\) alternating and \(z\) derivation-valued.

On this representative, (3.3) is diagonal. The induced linear involution \(L_n\) on \(H\) has signs
\[
\begin{array}{c|ccc}
 &H^0(\Lambda^2T_X)^\iota&H^1(T_X)^\iota&H^2(\mathcal O_X)^\iota\\
\hline
L_n&(-1)^{n+1}&(-1)^n&(-1)^{n+1}.
\end{array}
\tag{3.5}
\]
Its fixed subspace is exactly
\[
P_n=
\begin{cases}
H^1(T_X)^\iota,&n\text{ even},\\
H^0(\Lambda^2T_X)^\iota\oplus H^2(\mathcal O_X)^\iota,&n\text{ odd}.
\end{cases}
\tag{3.6}
\]
With the parity origin \(o\), the fixed literal unrestricted classes are therefore \(o+P_n\). By PR425 Section 5, this is precisely the image of the literal parity lift torsor, not merely a matching dimension.

## 4. Why this calculation applies to genuine class fibers

Let
\[
\mathscr F_p=\{u\in U_{n+1}:u|_{h^n}=[p]\}.
\]
The map from literal unrestricted one-step lift classes \(T_U(p)\) to \(\mathscr F_p\) is a bijection:

- For surjectivity, choose any representative of a class in \(\mathscr F_p\), choose a marked lower gauge carrying its reduction to \(p\), lift that gauge as unrestricted coordinate data, and transport. The resulting upper representative reduces literally to \(p\). No target of a lifted equivalence is prescribed independently.
- For injectivity, a marked gauge between two literal lifts of \(p\) reduces to a lower automorphism of \(p\). PR438 Lemma 2.1 makes that full lower automorphism 2-trivial. Lift the trivializing ordinary chart unit into the upper source product and apply (2.10). This changes no endpoint and replaces the gauge by one literally identity modulo \(h^n\). Thus the two points were already equal in \(T_U(p)\).

Because \(p=\mathcal I p\) literally, \(T_U(p)\) is stable under \(\mathcal I\). Section 2 makes the displayed bijection equivariant. Consequently the fixed locus in the **true** finite class fiber is exactly the fixed locus calculated in Section 3.

Here is also the explicit lower-transport check. If a gauge \(g:x\to y\) is used to place a representative over the parity lower object, and \(q:x\to\mathcal I x\) witnesses a fixed class, then
\[
(\mathcal I g)\circ q\circ g^{-1}:y\longrightarrow\mathcal I y
\tag{4.1}
\]
witnesses the same property after transport. The lower gauge \(g\) need not itself be parity. The reduction of (4.1) is a possible nonidentity automorphism of \(p\); it is removed by the preceding endpoint-preserving 2-unit correction. This is why one may use the fixed literal-lower calculation without presuming that a weak fixed-class witness has been strictly equivariant all along.

The \(H\)-torsor action is independent of the literal representative of the lower class. Indeed common lifted unrestricted coordinate data can be used on two upper lifts: units with constant term 1 are invertible for either product. Their classical chart and edge parts are \(\mathrm{id}\) and \(1\). At the new top coefficient, their transport sends a difference \((u,v,a)\) to the same difference: every positive-order gauge contribution costs another \(h\), while product variations evaluated on classical units vanish by normalization. Different lifts of fixed lower gauge data differ by a top gauge. Two lower gauges differ by a full lower relative automorphism, whose lifted 2-unit trivialization shows that its induced action on relative classes is the identity.

Thus these are genuine affine fibers with the claimed linear action, not an unexamined quotient by lower automorphisms. We do not infer this merely from graded automorphism vanishing.

## 5. Finite fixed classes are exactly the parity image

Induct on \(n\).

At \(n=M\), both categories have the one prescribed object \(P\), which is fixed.

Assume \(J_n(R_n)=U_n^{\mathcal I}\), and let \(u\in U_{n+1}\) be fixed. Its reduction \(\bar u\) is fixed. By induction it has a parity representative \(p\) modulo \(h^n\). Place \(u\) over this literal \(p\) using the surjectivity argument of Section 4.

The resulting point of \(\mathscr F_p\) is fixed, so the equivariant bijection of Section 4 makes its literal relative class fixed. Choose a parity lift \(o\) of \(p\). Its difference from \(u\) is some \(\alpha\in H\), and fixedness gives \(L_n\alpha=\alpha\). By (3.6), \(\alpha\in P_n\). PR425's exact one-step image theorem therefore supplies a parity lift representing \(u\). Hence \(u\in J_{n+1}(R_{n+1})\).

Conversely, any parity presentation is literally fixed by Section 2.4, so its unrestricted class is fixed. This completes the induction.

This proves existence of a parity representative. Its parity-equivalence class is unique by the already established injectivity of \(J_{n+1}\), not by a new unproved uniqueness of representatives.

## 6. The formal criterion and the first failed normal-form test

For an unrestricted marked formal object \(x\), the following conditions are equivalent:

1. \(x\) is marked-equivalent to \(\mathcal I x\).
2. Every finite class \(x_n\in U_n\) is fixed by \(\mathcal I\).
3. Every \(x_n\) belongs to \(J_n(R_n)\).
4. \(x\) has a marked parity formal representative.

The implication \(1\Rightarrow2\) is reduction. The implication \(2\Rightarrow1\) follows from the injectivity of the unrestricted formal/inverse-limit map in PR438 Lemma 4.1: \(x\) and \(\mathcal I x\) have the same finite classes, so they are formally equivalent. This uses the proven construction of compatible gauges, not an exchange of inverse limit and quotient.

The equivalence \(2\Leftrightarrow3\) is Section 5. The equivalence \(3\Leftrightarrow4\) is PR438 Theorem 4.3, whose proof uses finite injectivity and the two established inverse-limit comparisons. Finally \(4\Rightarrow1\) follows directly from Section 2: transport an equivalence to a strict fixed representative and apply its reversed opposite.

There is a useful intrinsic one-step failure test. Suppose \(u\in U_{n+1}\) has parity-normalizable reduction. Its genuine fiber is an \(H\)-torsor stable under \(\mathcal I\). Choose a parity origin \(o\), write \(u=o+\alpha\), and put
\[
q_n(u)=\frac12\bigl(\alpha-L_n\alpha\bigr)\in Q_n:=\ker(L_n+1).
\tag{6.1}
\]
Equivalently, \(2q_n(u)\) is the affine difference \(u-\mathcal I u\), with the torsor convention \((o+\alpha)-(o+\beta)=\alpha-\beta\). The choice of parity origin changes \(\alpha\) by an element of \(P_n\), so it does not change \(q_n\). Section 4's identity-linear transport and lower-automorphism removal show independence of the lower parity representative and its identifying gauge as well.

Thus
\[
q_n(u)=0\ \Longleftrightarrow\ u\in J_{n+1}(R_{n+1}),
\]
provided its reduction is in \(J_n(R_n)\), and
\[
Q_n=
\begin{cases}
H^0(\Lambda^2T_X)^\iota\oplus H^2(\mathcal O_X)^\iota,
   &n\text{ even},\\
H^1(T_X)^\iota,&n\text{ odd}.
\end{cases}
\tag{6.2}
\]
This is an obstruction to marked parity **normalization**, not to unrestricted continuation. On the fourfold its dimensions are 12 at even new degrees and 16 at odd new degrees. They are the complementary dimensions already present in PR438, now characterized intrinsically as the anti-fixed defect of reversal on the genuine fiber.

If a formal class is not parity-normalizable, finite detection gives at least one failed finite order, and hence a first one. At that order its \(q_n\) is nonzero. No numerical uniform bound on this first order is claimed. Nor is a later \(q_n\) defined by this construction after the lower parity-normalization condition has already failed.

## 7. Contribution and boundaries

The new normal-form criterion replaces “belongs to the proper parity image” by the symmetry condition “is equivalent to its reversed opposite,” and provides the origin-independent anti-fixed defect at a first failing step. It does not assert that every unrestricted marked class is fixed: PR438's nonzero complementary constructions give non-fixed classes.

The first-order product and all coefficients below \(M\) remain supplied, literal data. This result neither constructs nor changes their original geometric or module meaning. The new assertion concerns all **higher-order marked ambient object classes**, conditional on the stated literal parity-lifting input. The formal conclusion is coefficientwise only.

No algebraicity, analytic convergence, period interpretation, moduli representability, fixed-product all-orders theorem, module lift, first-star-to-second-star implication, or six-pure-condition vanishing follows. No selected HM/source function, source obstruction, retained detector, matrix, or source-dependent coefficient is evaluated. The proof is symbolic algebra and a deduction from the pinned structural results, not a machine-verification claim or a claim of exhaustive literature novelty.
