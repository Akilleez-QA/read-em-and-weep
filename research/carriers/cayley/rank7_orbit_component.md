# Rank-seven Segre quadrics: exact local rigidity and exclusion of good boundary points

Work over an algebraically closed field of characteristic zero. Put
\(V=(k^2)^{\otimes4}\), \(X=(\mathbf P^1)^4\subset\mathbf P(V)\), and
\[
R_7=\{[q]\in\mathbf P I_2(X):\operatorname{rank}(q)\le7\}.
\]
Let \(q_0=4AE-BD+UV+UW+VW\) be the form in `rank7_construction.md`.

## Conclusions

1. **The projective Zariski tangent dimension of \(R_7\) at \([q_0]\) is exactly 9.** It is a smooth point of \(R_7\), and belongs to exactly one irreducible component \(C_0\).
2. **Its full projective stabilizer in \(G=\operatorname{PGL}_2^4\) is diagonal \(\operatorname{PGL}_2\).** Its orbit has dimension 9 and is open in \(C_0\). With factor permutations allowed, the stabilizer is \(\operatorname{PGL}_{2,\mathrm{diag}}\times S_4\).
3. **Every point of \(C_0\) whose radical is disjoint from \(X\) lies in the orbit of \([q_0]\).** Every boundary point \(C_0\setminus G[q_0]\), including any point of rank seven, has a decomposable radical vector.
4. Consequently, changing \(q_0\) slightly, or taking a radical-disjoint specialization anywhere on its component, cannot produce a genuinely different finite map to a smooth five-dimensional quadric. A genuinely new example must occur on another irreducible component of \(R_7\). This calculation **does not prove that there are no other such components**.

## Exact tangent calculation

Order tensor coordinates lexicographically by binary indices \(0000,\ldots,1111\), and let \(Q\) be the Hessian of \(q_0\). It has rank 7. An integral basis of \(K=\ker Q\), in the order used by the certificate, is
\[
\begin{split}
k_1&=e_2-e_1, & k_2&=e_4-e_1, & k_3&=e_8-e_1,\\
k_4&=e_9-e_6, & k_5&=e_{10}-e_5, & k_6&=e_{11}-e_7,\\
k_7&=e_{12}-e_3, & k_8&=e_{13}-e_7, & k_9&=e_{14}-e_7.
\end{split}
\]
Here \(e_i\) denotes the coordinate vector indexed by integer \(i\).

The tangent space to the affine symmetric rank-at-most-seven locus at \(Q\) consists of symmetric matrices \(H\) with \(H|_{K\times K}=0\). Therefore its intersection with \(I_2(X)\) is the kernel of
\[
T:I_2(X)\longrightarrow\operatorname{Sym}^2K^*,\qquad
f\longmapsto\left.\operatorname{Hess}(f)\right|_{K\times K}.
\]
The dimensions of source and target are 55 and 45.

An integral basis of \(I_2(X)\) is constructed without solving a linear system. Partition unordered coordinate monomials \(z_i z_j\), \(i\le j\), by their coordinatewise binary-index sum in \(\{0,1,2\}^4\). There are 136 monomials and 81 distinct sums. In each fiber, take every other monomial minus its first monomial, using lexicographic pair order. These 55 differences form a basis because their restrictions to \(X\) are exactly the 81 distinct monomials of multidegree \((2,2,2,2)\).

In this ordered basis and the lexicographic upper-triangular entries of a symmetric \(9\times9\) matrix, \(T\) is a \(45\times55\) integer matrix. It has rank 45. An explicit nonzero minor uses all 45 rows and zero-indexed columns

```
0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,
18,19,20,21,22,23,24,25,26,27,28,29,30,31,
32,33,34,35,36,37,38,39,41,42,43,44,45,52,53,54.
```

Its determinant is **−2048**. Thus the affine tangent dimension is \(55-45=10\), and the projective tangent dimension is **9**.

The symmetric determinantal locus is smooth of codimension 45 at every rank-seven matrix. Surjectivity of \(T\) is precisely transversality of its intersection with the 55-dimensional linear space \(I_2(X)\). This proves smoothness and the local dimension, not just a numerical upper bound.

## Orbit tangent and full stabilizer

Use the standard \(E,F,H\) generators of \(\mathfrak{sl}_2\) on each tensor factor. If \(R\) is the resulting \(16\times16\) infinitesimal matrix, the induced Hessian variation, up to the immaterial action-sign convention, is
\[
R^TQ+QR.
\]
The 12 such variations span a 9-dimensional vector space. Adding the scalar direction \(Q\) raises the dimension to 10. The kernel of the 12-column variation matrix is precisely the three vectors
\[
E_1+E_2+E_3+E_4,\quad
F_1+F_2+F_3+F_4,\quad
H_1+H_2+H_3+H_4.
\]
No additional infinitesimal projective stabilizer arises from allowing a scalar multiple of \(Q\).

The diagonal \(\operatorname{SL}_2\) therefore fixes \(q_0\). The action on quadratic forms descends to \(G=\operatorname{PGL}_2^4\), since each central sign acts trivially in degree two. Its connected projective stabilizer is diagonal \(\operatorname{PGL}_2\).

Every element of the full stabilizer normalizes its identity component. But
\[
N_{\operatorname{PGL}_2^4}(\operatorname{PGL}_{2,\mathrm{diag}})
=\operatorname{PGL}_{2,\mathrm{diag}}.
\]
Indeed, if \((g_1,g_2,g_3,g_4)\) normalizes the diagonal subgroup, all four conjugation automorphisms agree, so \(g_i g_1^{-1}\) is central in \(\operatorname{PGL}_2\), hence trivial. This proves the full stabilizer assertion. The displayed polynomial is invariant under \(S_4\), which permutes \(U,V,W\), so the extra permutation factor is exactly as claimed.

The orbit has dimension \(12-3=9\), equal to the smooth local dimension. Its closure is the unique component \(C_0\), and the orbit is open there.

## Why no good boundary point can occur

The following argument upgrades local rigidity to a classification on the whole component.

### Lemma: an unstable quadratic form has a Segre radical point

For the \(\operatorname{SL}_2^4\) action on quadratic forms on \(V\), if a nonzero form \(q\) is GIT unstable, then \(\mathbf P(\operatorname{rad}q)\cap X\ne\varnothing\).

By the Hilbert–Mumford criterion, after choosing bases in the four factors there is a one-parameter subgroup for which every monomial occurring in \(q\) has strictly positive weight. The coordinate weights on \(V^*\) are all sums of four chosen signs \(\pm a_1\pm a_2\pm a_3\pm a_4\). Their minimum is \(-M\), their maximum is \(M\), where \(M=\sum_i|a_i|\). Choose a coordinate \(z_{\min}\) of minimum weight. Every monomial \(z_{\min}z_j\) has weight at most zero. None can occur in \(q\). Thus the entire \(z_{\min}\) Hessian row and column is zero. The corresponding coordinate vector is decomposable and belongs to \(\operatorname{rad}q\).

In particular, every radical-disjoint quadratic form is semistable. The lemma is independent of the rank bound and of the condition \(q\in I_2(X)\).

### Lemma: \(q_0\) has closed affine orbit

It is fixed by the reductive diagonal subgroup \(H=\operatorname{PGL}_{2,\mathrm{diag}}\), whose normalizer in \(G\) is itself. Consequently \(N_G(H)q_0=\{q_0\}\) is closed. Luna's closed-orbit criterion implies that \(Gq_0\) is closed in the affine representation \(I_2(X)\).

For a complex-analytic proof of this particular application, choose an \(\operatorname{SU}_2^4\)-invariant Hermitian norm. The moment map of \(q_0\) is fixed by diagonal \(\operatorname{SU}_2\), since \(q_0\) is fixed. Each of its four components belongs to the coadjoint representation of \(\mathfrak{su}_2\), which has no nonzero invariant vector. Thus the moment map is zero, and the Kempf–Ness criterion gives the same closedness result.

The nonzero closed affine orbit means that \([q_0]\) is projectively polystable: its projective orbit is closed in the semistable locus. Therefore
\[
\overline{G[q_0]}\setminus G[q_0]\subset\mathbf P I_2(X)^{\mathrm{unstable}}.
\]
The preceding lemma implies that all these boundary points have a Segre radical point, as desired.

For the standard closed-orbit theorem, see Ivan Losev, *The Kempf–Ness theorem and Invariant Theory*, Theorems 2 and 4: https://arxiv.org/abs/math/0605756 . For the projective polystable-orbit terminology and semistable locus, see Victoria Hoskins, *Moduli Problems and Geometric Invariant Theory*, Definition 5.12 and the surrounding projective GIT discussion: https://userpage.fu-berlin.de/hoskins/M15_Lecture_notes.pdf . The application and the radical-vector lemma above are proved here; the cited works do not classify these Segre quadrics.

## What this does and does not settle for variants

- Precomposing the resulting map by \(\operatorname{Aut}(X)\), changing bases of its seven projection coordinates, or moving \(q_0\) within its rank-seven component while preserving radical disjointness yields the same geometric construction up to the stated equivalences.
- Any cohomological condition invariant under automorphisms of \(X\) and isomorphisms of the target cannot improve through these map changes. If all target Cayley bundles have already been tested for \(q_0\), those tests cover this entire radical-disjoint component.
- The global rank-at-most-seven locus can have other components, including large components consisting entirely of radical-incident quadrics. No irreducibility statement is asserted.
- The remaining geometric search is precise: find another irreducible component containing a rank-seven point with radical disjoint from \(X\), or prove that every other component is contained in the radical-incidence locus.
- The radical-disjoint rank-seven locus containing \([q_0]\) is an open-and-closed connected component isomorphic to \(\operatorname{PGL}_2^4/\operatorname{PGL}_{2,\mathrm{diag}}\). Other good components, if any, cannot meet it while keeping the radical disjoint.

## Reproduction

Run

```
python rank7_tangent_certificate.py
```

The script uses only Python and SymPy, exact integer/rational arithmetic, and explicit tensor-coordinate matrices. Its output is saved in `rank7_tangent_certificate.txt`. The calculation takes under a second in the current environment. The proof of the boundary statement is separate from the tangent calculation and uses the standard GIT criteria stated above.
