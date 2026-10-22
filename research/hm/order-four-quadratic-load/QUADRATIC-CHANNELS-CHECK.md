# Universal quadratic-channel check

Work over characteristic zero. Let \(V\) be one irreducible three-dimensional representation of \(A_5\), let \(A\) be the other, and put

\[
L=V\oplus\mathbf4\subset H^0(\mathbf P(V),\mathcal O(3)).
\]

Assume this linear series embeds \(T\simeq\mathbf P^2\) in \(\mathbf P^6\), with \(\mathcal O_T(1)=\mathcal O_{\mathbf P^2}(3)\). The arguments below use only the representation decomposition and this embedding assumption. They do not evaluate any selected multiplication matrix or impose maximal rank in a matching channel.

## 1. Character verification

Use class order \((1,2,3,5_a,5_b)\), with sizes \((1,15,20,12,12)\), and set \(\phi=(1+\sqrt5)/2\), \(\phi'=1-\phi\). Choose labels so that

\[
\begin{aligned}
\chi_V&=(3,-1,0,\phi,\phi'),\\
\chi_A&=(3,-1,0,\phi',\phi),\\
\chi_{\mathbf4}&=(4,0,1,-1,-1),\\
\chi_{\mathbf5}&=(5,1,-1,0,0).
\end{aligned}
\]

All these representations are self-dual. Since
\(\chi_L=(7,-1,1,\phi-1,\phi'-1)\), the identity

\[
\chi_{\operatorname{Sym}^2L}(g)
=\tfrac12\bigl(\chi_L(g)^2+\chi_L(g^2)\bigr)
\]

gives

\[
\chi_{\operatorname{Sym}^2L}=(28,4,1,\phi',\phi),
\qquad
\boxed{\operatorname{Sym}^2L=2\mathbf1\oplus A\oplus2\mathbf4\oplus3\mathbf5.}
\]

For \(\operatorname{Sym}^6V^*\), use the generating function
\(\det(1-tg\mid V)^{-1}\). At an involution its coefficient of \(t^6\) is
\(1-2+3-4+5-6+7=4\); at an element of order three it is the coefficient of \(t^6\) in \((1-t^3)^{-1}\), namely 1. At a fifth-order element with eigenvalues \(1,\zeta,\zeta^{-1}\),

\[
\frac1{(1-t)(1-\zeta t)(1-\zeta^{-1}t)}
=\frac{1-(\zeta^2+\zeta^{-2})t+t^2}{1-t^5}.
\]

Its sixth coefficient is \(-(\zeta^2+\zeta^{-2})=\phi\); the other fifth-order class gives \(\phi'\). Consequently

\[
\chi_{\operatorname{Sym}^6V^*}=(28,4,1,\phi,\phi'),
\qquad
\boxed{\operatorname{Sym}^6V^*=2\mathbf1\oplus V\oplus2\mathbf4\oplus3\mathbf5.}
\]

## 2. Forced equations and failure of 2-normality

The restriction/multiplication map is equivariant:

\[
\mu_2:\operatorname{Sym}^2L\longrightarrow
H^0(T,\mathcal O_T(2))=\operatorname{Sym}^6V^*.
\]

The source's entire \(A\)-summand maps to zero, because the target has no \(A\). The target's entire \(V\)-summand is absent from the image, because the source has no \(V\). Semisimplicity and equal source/target multiplicities in every other channel give

\[
\ker\mu_2\simeq A\oplus E,\qquad
\operatorname{coker}\mu_2\simeq V\oplus E,
\]

for some
\(E=e_1\mathbf1\oplus e_4\mathbf4\oplus e_5\mathbf5\), with
\(0\le e_1\le2\), \(0\le e_4\le2\), \(0\le e_5\le3\).
This notation records unspecified channel defects; it does not assert that every such choice can occur geometrically.

The ideal-sheaf sequence and \(H^1(\mathbf P^6,\mathcal O(2))=0\) identify these with \(H^0(\mathcal I_T(2))\) and \(H^1(\mathcal I_T(2))\), respectively. Thus

\[
\boxed{h^0(\mathcal I_T(2))=h^1(\mathcal I_T(2))\ge3.}
\]

In particular, \(T\) is not 2-normal. Exactly three quadrics, or exactly three dimensions of failure of 2-normality, requires the additional assertion \(E=0\); neither follows from representation theory alone.

## 3. A genuine linear-syzygy restriction for the forced net

Let \(Q\simeq A\) be the forced three-dimensional space of quadrics in \(S=\operatorname{Sym}L\). Its three independent quadrics have no common factor: a common quadratic factor would make their span one-dimensional; a common linear factor would span an invariant line in \(L\), since the gcd is preserved up to scalar by \(A_5\). The group has no nontrivial one-dimensional characters, and \(L=V\oplus\mathbf4\) has no invariant line.

**Elementary lemma.** Three independent quadrics with gcd 1 have at most two linearly independent linear syzygies.

Indeed, every nonzero linear syzygy vector has relatively prime entries, since a common linear factor would yield a constant relation between the quadrics. Two such vectors proportional over the fraction field must consequently be constant multiples, by homogeneity and unique factorization. Thus two linearly independent syzygies \(s,t\) are independent over the fraction field. Their cross product is proportional to the vector of quadrics \(q\). The gcd-1 hypothesis makes the proportionality factor polynomial, and homogeneity makes it a nonzero constant: \(s\times t=cq\), \(c\ne0\).

For any third linear syzygy \(u\), the same argument gives \(s\times u=aq\) and \(t\times u=bq\), with constants \(a,b\) (possibly zero). Over the fraction field, all three lie in the two-dimensional space perpendicular to \(q\). The cross-product identities then give \(u=-(b/c)s+(a/c)t\), a constant linear combination. If no independent pair exists, the syzygy space instead has dimension at most one. No perfectness hypothesis or determinantal-height conclusion is used.

Now

\[
Q\otimes L=A\otimes(V\oplus\mathbf4)
=V\oplus2\mathbf4\oplus2\mathbf5.
\]

The linear-syzygy space is an \(A_5\)-subrepresentation of this representation, so it has no trivial summand. Every nonzero nontrivial \(A_5\)-representation has dimension at least three. The lemma therefore forces

\[
\boxed{\ker(Q\otimes L\longrightarrow\operatorname{Sym}^3L)=0.}
\]

Hence the 21 linear multiples of the three forced quadrics are linearly independent. This assertion concerns this forced net, not unknown additional quadratic equations. It does not assert that the net is a regular sequence or determine its height.

## 4. The degree-eight inference is not valid

Three quadrics of height three in \(\mathbf P^6\) cut out a threefold of degree eight, whereas \(T\) is a surface. A threefold can contain surfaces of degree larger than its own; degree monotonicity does not apply to subschemes of different dimensions. Thus the surface's degree nine does not force these quadrics to have height at most two. No height-two, determinantal-presentation, or complete-intersection exclusion follows from that numerical comparison.
