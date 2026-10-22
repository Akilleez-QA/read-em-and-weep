# Independent review: whole-fiber base-locus exclusion

## Verdict and scope

**Review status: PASS**, conditional on the pinned representation-theoretic, canonical endpoint, and secant-bundle interfaces stated in the accompanying proof.

The proposed structural argument is valid over \(\mathbb C\), conditional on the stated representation-theoretic assumptions. It proves the exclusion for **every** nonzero parameter and **every** nonzero evaluation vector, not merely for generic parameters or non-isotropic vectors.

The projected Veronese map and the universal parameterized map are both closed immersions. The degree of the universal image is **12**, not 24.

This review checks the mathematical implications of the supplied assumptions associated with PR661, proof commit `1325647fd916bf2daa71b11efeae6d52cfefa2cd`. It does not independently authenticate that source, evaluate an HM expression, or establish any additional condition concerning an unspecified subspace \(K_a\).

## 1. Assumptions and conventions

Let \(G=A_5\). Let \(A\) be a three-dimensional irreducible representation with a nondegenerate invariant symmetric bilinear form \(B\). Write \(\Omega\in\operatorname{Sym}^2 A\) for the inverse-metric tensor, so that its contraction with \(B\) is 3. Set

\[
D_{\mathrm{par}}=\operatorname{Sym}^2_0 A,
\qquad
\pi(s)=s-\frac{\operatorname{tr}_B(s)}{3}\Omega.
\]

Thus \(\operatorname{Sym}^2 A=\mathbb C\Omega\oplus D_{\mathrm{par}}\), with \(D_{\mathrm{par}}\) irreducible of dimension five. Distinguish this parameter representation from a source representation \(D_{\mathrm{src}}\) of the same irreducible type. Let \(P\) be the four-dimensional irreducible representation and assume

\[
M=\operatorname{Hom}(D_{\mathrm{src}},P)
\simeq A\oplus V\oplus P\oplus 2D_{\mathrm{par}},
\]

where \(V\) is the other three-dimensional irreducible. In particular, \(\dim M=20\), \(M^G=0\), and \(D_{\mathrm{par}}\) occurs in \(M\) with multiplicity two.

Projective spaces below parameterize one-dimensional subspaces. For \(a\in A\), write

\[
v_a=\pi(a\otimes a)
=a\otimes a-\frac{B(a,a)}{3}\Omega.
\]

## 2. Identifying the parameter space

Tensor adjunction identifies

\[
Q=\operatorname{Hom}_G(D_{\mathrm{src}},P\otimes\operatorname{Sym}^2 A^*)
\simeq\operatorname{Hom}_G(\operatorname{Sym}^2 A,M).
\]

Because \(M^G=0\), every such map vanishes on \(\mathbb C\Omega\). Restriction therefore gives an isomorphism

\[
Q\simeq\operatorname{Hom}_G(D_{\mathrm{par}},M),
\qquad \dim Q=2.
\]

Under this identification, the parameter corresponding to \(T\) evaluates as

\[
q(a,-)=T(v_a)\in M.
\]

The formula is exact with the above tensor/evaluation conventions. Alternative symmetric-tensor normalization conventions can introduce a fixed nonzero overall scalar, which changes none of the conclusions.

## 3. Whole-fiber vanishing is impossible

First, \(v_a\ne0\) whenever \(a\ne0\). Indeed, if \(v_a=0\), then

\[
a\otimes a=\frac{B(a,a)}{3}\Omega.
\]

Viewed as maps \(A^*\to A\), the left side has rank one, whereas the right side has rank three if its scalar is nonzero and rank zero otherwise. Neither alternative is possible. This argument includes the isotropic case \(B(a,a)=0\).

Second, any nonzero \(G\)-equivariant map \(T:D_{\mathrm{par}}\to M\) is injective: its kernel is a proper invariant subspace of the irreducible representation \(D_{\mathrm{par}}\).

Consequently,

\[
q\ne0,\quad a\ne0
\quad\Longrightarrow\quad
q(a,-)=T(v_a)\ne0.
\]

Equivalently, no nonzero parameter vanishes on an entire source fiber at any point of \(\mathbb P(A)\).

For each fixed nonzero \(a\), the linear map

\[
Q\longrightarrow M,\qquad T\longmapsto T(v_a)
\]

is injective. The quadratic evaluation morphism of vector bundles is therefore everywhere of rank two:

\[
0\longrightarrow Q\otimes\mathcal O_{\mathbb P(A)}
\longrightarrow M\otimes\mathcal O_{\mathbb P(A)}(2)
\longrightarrow\mathcal C\longrightarrow0,
\]

with \(\mathcal C\) locally free of rank \(20-2=18\). Equivalently, after twisting by \(\mathcal O(-2)\), one has a rank-two subbundle \(Q\otimes\mathcal O(-2)\subset M\otimes\mathcal O\). Local freeness follows from constant rank: an invertible maximal minor locally splits the inclusion.

## 4. The trace-free quadratic map is a closed immersion

The nonvanishing just proved defines a morphism

\[
v:\mathbb P(A)\longrightarrow\mathbb P(D_{\mathrm{par}}),
\qquad [a]\longmapsto[v_a].
\]

It is the quadratic Veronese embedding followed by projection from \([\Omega]\). The center has rank three, whereas every tensor on a secant or tangent line to the Veronese has rank at most two. The following direct checks make the embedding claim precise.

### Separation of points

Suppose \([v_a]=[v_b]\). There is \(\lambda\ne0\) and some \(\mu\) such that

\[
a\otimes a-\lambda b\otimes b=\mu\Omega.
\]

The left side has rank at most two, so \(\mu=0\). Equality of the remaining rank-one tensors implies \(\mathbb C a=\mathbb C b\). Thus \(v\) separates points.

### Separation of tangent vectors

A tangent vector at \([a]\) can be represented by \(b\in A/\mathbb C a\). Its differential is represented, modulo \(\mathbb C v_a\), by

\[
\pi(a\otimes b+b\otimes a).
\]

If this differential vanishes, there are scalars \(\lambda,\mu\) with

\[
a\otimes b+b\otimes a-\lambda a\otimes a=\mu\Omega.
\]

Again the left side has image contained in \(\operatorname{span}(a,b)\), hence rank at most two. Therefore \(\mu=0\). If \(b\notin\mathbb C a\), choose \(\ell\in A^*\) with \(\ell(a)=0\) and \(\ell(b)\ne0\). Contracting the equality with \(\ell\) in the first factor gives \(\ell(b)a=0\), a contradiction. Hence \(b\in\mathbb C a\), so the original tangent vector was zero.

The linear system defining \(v\) is base-point free and separates points and tangent vectors on the smooth projective variety \(\mathbb P(A)\). The standard point-and-tangent criterion therefore shows that \(v\) is a closed immersion. Equivalently, the same rank arguments over algebraically closed field extensions give universal point separation; tangent separation gives an unramified morphism, and properness upgrades this to a closed immersion.

One has

\[
v^*\mathcal O_{\mathbb P(D_{\mathrm{par}})}(1)
\simeq\mathcal O_{\mathbb P(A)}(2).
\]

Thus each fixed nonzero \(q\), or \(T\), gives the closed immersion

\[
\mathbb P(A)\xrightarrow{v}\mathbb P(D_{\mathrm{par}})
\xrightarrow{\mathbb P(T)}\mathbb P(M).
\]

Its image is a degree-four surface, lying in the projective four-space \(\mathbb P(T(D_{\mathrm{par}}))\).

## 5. Universal family and its degree

Let \(M_D\subset M\) denote the \(D_{\mathrm{par}}\)-isotypic component. Semisimplicity and Schur's lemma give the canonical evaluation isomorphism

\[
\operatorname{ev}:D_{\mathrm{par}}\otimes Q\xrightarrow{\sim}M_D,
\qquad d\otimes T\longmapsto T(d).
\]

In particular, \(\dim M_D=10\). The universal morphism

\[
F:\mathbb P(A)\times\mathbb P(Q)\longrightarrow\mathbb P(M_D),
\qquad ([a],[T])\longmapsto[T(v_a)]
\]

is well-defined everywhere and, via \(\operatorname{ev}\), factors as

\[
\mathbb P(A)\times\mathbb P(Q)
\xrightarrow{v\times\mathrm{id}}
\mathbb P(D_{\mathrm{par}})\times\mathbb P(Q)
\xrightarrow{\mathrm{Segre}}
\mathbb P(D_{\mathrm{par}}\otimes Q).
\]

Both arrows are closed immersions. Hence \(F\) is a closed immersion into \(\mathbb P^9\), and its pullback hyperplane bundle is \(\mathcal O(2,1)\).

Writing \(h=c_1(\mathcal O_{\mathbb P^2}(1))\) and \(t=c_1(\mathcal O_{\mathbb P^1}(1))\), with \(h^3=t^2=0\) and \(\int h^2t=1\), gives

\[
\deg F(\mathbb P^2\times\mathbb P^1)
=\int(2h+t)^3
=\int12h^2t
=\boxed{12}.
\]

There is no extra factor of two from the dimension of \(Q\); that parameter direction has already been accounted for by \(t\) and the binomial coefficient.

## 6. Exact limitation of the result

The injection used in the proof is

\[
T:D_{\mathrm{par}}\hookrightarrow M,
\]

not an injection of the evaluated map

\[
q(a,-):D_{\mathrm{src}}\longrightarrow P.
\]

Indeed, the latter is a map from a five-dimensional space to a four-dimensional space, so it always has a nontrivial kernel. The argument proves only that it is not the zero map.

For any subspace \(K_a\subset D_{\mathrm{src}}\), one has

\[
q(a,-)|_{K_a}=0
\quad\Longleftrightarrow\quad
K_a\subseteq\ker q(a,-).
\]

Nonzeroness of \(q(a,-)\) does not rule out that containment. Therefore this structural lemma does **not** establish nonvanishing on \(K_a\), including at any locus described as “nonsquares,” and it does not by itself settle an HM/source restriction that depends on such nonvanishing. Any such strengthened conclusion needs an independent argument about \(K_a\) and the evaluated kernels.

## 7. Review of the accompanying `PROOF.md`

The accompanying proof was also read directly. Its refinement from \(A_5\) to the binary group \(G=\mathrm{SL}_2(\mathbb F_5)\) is consistent: the binary module \(W\) need not descend, while the channel modules used in this argument do. The argument depends only on those descended modules and the stated decomposition.

The following additional statements in that file are correct:

- Let \(R\) be defined by \(0\to\mathcal O_X(-2)\to D\otimes\mathcal O_X\to R\to0\). Then \(R\) is a vector bundle of rank four.
- If \(M_{\mathrm{non}\text{-}D}\) is the sum of the other isotypic components, the cokernel of the twisted evaluation inclusion is canonically \((R\otimes Q)\oplus(M_{\mathrm{non}\text{-}D}\otimes\mathcal O_X)\). Its summands have ranks eight and ten, totaling eighteen. The original, untwisted cokernel is this direct sum tensored by \(\mathcal O_X(2)\). These are quotient splittings along isotypic components; there is no claim that \(\mathcal O_X(-2)\subset D\otimes\mathcal O_X\) itself splits globally.
- With a chosen nonzero representative \(a\) and \(\lambda\in D^*\) satisfying \(\lambda(v_a)=1\), contraction \(\lambda\otimes\mathrm{id}_Q\) recovers \(q\in Q\) from \(f=v_a\otimes q\). It is independent of the choice of normalized \(\lambda\) on this compatible two-plane. The compatibility requirement in the proof is essential and correctly stated.
- The two-dimensional image provides a minimal **linear** certificate: an injective linear map on the two-dimensional space \(Q\) cannot take values in a vector space of smaller dimension. This does not mean all twenty matrix entries are independent.
- The point-and-tangent argument for the closed immersion is valid. Over \(\mathbb C\), the base-point-free linear-system criterion on the smooth projective plane applies exactly as used there.
- Recoverability of both projective direction and projective family from a compatible nonzero full map follows from the closed immersion of the product. It is an intrinsic uniqueness statement, not an assertion that every element of \(\mathbb P(M_D)\) is compatible.

### Finite restricted-degeneracy observation

The accompanying proof explicitly states the pinned secant-bundle input

\[
0\longrightarrow K\longrightarrow D_{\mathrm{src}}\otimes\mathcal O_X
\longrightarrow A\otimes\mathcal O_X(1)\longrightarrow0,
\]

where \(K\) is a globally defined \(G\)-equivariant rank-two vector subbundle with fibers \(K_a\). Under that premise, the restricted evaluation

\[
Q\otimes\mathcal O_X\longrightarrow K^*\otimes P\otimes\mathcal O_X(2)
\]

has a closed determinantal locus where its rank is less than two. Equivariance makes that locus \(G\)-invariant. Assuming the quoted PR661 restricted-fiber result, it is disjoint from the square conic. Any positive-dimensional closed subset of \(\mathbb P^2\) contains a projective curve, and every such curve meets the conic. Therefore this degeneracy locus is empty or zero-dimensional, hence has finite support.

This conclusion allows a nonempty, possibly nonreduced finite degeneracy scheme off the conic. It neither excludes that finite locus nor replaces the pinned global bundle premise. With that premise explicitly included, the finite-or-empty conclusion is valid as stated. There is no outstanding mathematical objection to the accompanying proof within its declared conditional scope.

