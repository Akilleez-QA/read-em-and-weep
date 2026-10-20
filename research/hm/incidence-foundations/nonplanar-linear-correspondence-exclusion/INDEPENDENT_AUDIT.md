# Independent audit: exclusion of nonplanar linear correspondences

## Verdict

**The stated impossibility and the proposed proof are correct.** This audit interprets \(K\) as a vector subspace of \(\operatorname{Sym}^2 E\), so \(\dim K\leq 5\) is vector-space dimension, and interprets “dense compatibility” as compatibility on a Zariski-dense subset of the integral surface. There is no exception for an irreducible rank-three quadric cone or for a degenerate binary restriction of its equation.

Two presentational details should be made explicit in a final proof:

1. Since \(v\) is initially defined only on \(K\), extend it linearly to \(\operatorname{Sym}^2 E\) before treating the wedge expression as a polynomial on all of \(E\). Equivalently, work with the regular map from the affine cone to \(K\).
2. Dense compatibility gives a polynomial wedge identity on the entire affine cone. The argument uses the **derivative** of this identity at a diagonal point; merely evaluating the identity there would give no information.

Everything else in the proposed reduction is valid. The following supplies the details independently.

## 1. Linearization and its kernel bound

Write products in the symmetric algebra, and set

\[
L_T(ab)=\frac{aT(b)+bT(a)}2.
\]

Then \(L_T(a^2)=aT(a)\). Let

\[
E=\bigoplus_\lambda E_\lambda,
\qquad
T|_{E_\lambda}=\lambda I+N_\lambda,
\qquad
m_\lambda=\dim E_\lambda,
\]

be the generalized eigenspace decomposition. All \(\lambda\) are nonzero because \(T\) is invertible. On the summands of

\[
\operatorname{Sym}^2E=
\bigoplus_\lambda\operatorname{Sym}^2 E_\lambda
\;\oplus\!
\bigoplus_{\lambda<\mu}E_\lambda E_\mu,
\]

the operator \(L_T\) is scalar plus nilpotent, with scalar \(\lambda\) on \(\operatorname{Sym}^2 E_\lambda\) and scalar \((\lambda+\mu)/2\) on \(E_\lambda E_\mu\). The nilpotent assertion follows because the two induced nilpotent operators commute. Consequently only opposite-eigenvalue blocks can contribute to its kernel, and

\[
\dim\ker L_T\leq
\sum_{\{\lambda,-\lambda\}}m_\lambda m_{-\lambda}\leq4,
\]

where the sum is over unordered opposite pairs appearing in the spectrum.

For completeness, let an opposite pair have dimensions \(x_i,y_i>0\), and put \(s_i=x_i+y_i\). Then

\[
\sum_i x_i y_i
\leq\frac14\sum_i s_i^2
\leq\frac14\left(\sum_i s_i\right)^2
\leq\frac{4^2}{4}=4.
\]

Equality requires that there be exactly one opposite pair, that it exhaust \(E\), and that its two dimensions be equal. Thus equality in the kernel bound requires

\[
E=P\oplus Q,\quad \dim P=\dim Q=2,
\quad T|_P=\lambda I+N_P,\quad T|_Q=-\lambda I+N_Q.
\]

The cross block \(PQ\simeq P\otimes Q\) has dimension four. Since all other blocks are invertible and the kernel has dimension four, \(L_T\) vanishes identically on this cross block. Hence

\[
N_P\otimes I_Q+I_P\otimes N_Q=0.
\]

Taking the partial trace over \(Q\) gives

\[
2N_P+\operatorname{tr}(N_Q)I_P=2N_P=0,
\]

and likewise \(N_Q=0\). Therefore equality has precisely the claimed form: \(T\) is semisimple, with eigenvalues \(\lambda,-\lambda\), each of multiplicity two. In particular,

\[
\operatorname{rank}L_T\geq6.
\]

## 2. The surface must be an integral quadric

An integral nonplanar projective surface in \(\mathbb P(E)=\mathbb P^3\) is a hypersurface \(F=V(f)\) for an irreducible homogeneous polynomial \(f\) of degree \(d\geq2\). If one starts with a locally closed integral surface, replace it by its projective closure; the relevant polynomial identities extend to that closure.

Let

\[
H=\operatorname{span}\{a^2:[a]\in F\}
\subseteq\operatorname{Sym}^2 E.
\]

Its annihilator under the natural perfect pairing with \(\operatorname{Sym}^2 E^*\) is exactly the vector space of quadratic equations vanishing on \(F\).

If \(d\geq3\), there is no nonzero quadratic equation vanishing on \(F\): the homogeneous ideal of this integral hypersurface is \((f)\), whose degree-two piece is zero. Thus \(H=\operatorname{Sym}^2E\). The assumption that all \(aT(a)\) belong to \(K\) then implies

\[
L_T(\operatorname{Sym}^2E)=L_T(H)\subseteq K,
\]

contradicting \(\operatorname{rank}L_T\geq6>\dim K\).

Hence \(d=2\). Now the quadratic ideal is \(\mathbb C f\), so \(H=f^\perp\) is a hyperplane of dimension nine. Therefore

\[
5\geq\dim L_T(H)
=9-\dim(H\cap\ker L_T)
\geq9-4=5.
\]

Every inequality is an equality. In particular,

\[
\dim\ker L_T=4,
\qquad \ker L_T\subseteq H,
\qquad \dim K=5.
\]

This dimension argument does not assume that \(L_T(H)\) is a hyperplane in the image in advance; that fact follows from the displayed equalities.

## 3. Normalization and the quadric equation

The kernel-equality classification gives \(E=P\oplus Q\), with \(T\) acting by \(\lambda\) and \(-\lambda\), respectively. Multiplying \(T\) by a nonzero scalar does not affect any hypothesis:

- the vectors \(aT(a)\) are multiplied by that scalar and remain in \(K\);
- by linearity of \(v\), compatibility is unchanged;
- \(\operatorname{span}(a,T(a))\) is unchanged;
- the square-avoidance condition on \(v\) and \(K\) is unchanged.

After normalization, write

\[
T|_P=I,\qquad T|_Q=-I,\qquad \ker L_T=PQ.
\]

Since \(PQ\subseteq H=f^\perp\), the polarized form of \(f\) vanishes on all mixed pairs. Equivalently,

\[
f(p+q)=f_P(p)+f_Q(q).
\]

An integral quadric over \(\mathbb C\) has rank at least three: ranks one and two give a double plane or a product of two linear forms. Because the above quadratic form is block diagonal,

\[
\operatorname{rank}(f)=\operatorname{rank}(f_P)+\operatorname{rank}(f_Q).
\]

Each binary block has rank at most two. Thus at least one has rank two. Relabel the eigenspaces and, if needed, replace \(T\) by \(-T\), so that \(f_P\) has rank two and \(T|_P=I\).

## 4. A smooth isotropic eigenvector and its tangent directions

A nondegenerate binary quadratic form over \(\mathbb C\) has a nonzero isotropic vector. Choose \(e\in P\setminus\{0\}\) with \(f_P(e)=0\). Then

\[
[e]\in F,\qquad T(e)=e,\qquad e^2=eT(e)\in K.
\]

Nondegeneracy of \(f_P\) implies \(df_P(e)\neq0\). Hence \([e]\) is a smooth point of \(F\), and \(e\) is a smooth point of its affine cone away from the origin. Since \(f_Q\) is quadratic, its differential at zero vanishes. Therefore

\[
T_e\widehat F
=\ker df_P(e)\oplus Q
=\mathbb C e\oplus Q.
\]

Here \(\ker df_P(e)\subset P\) is one-dimensional and contains \(e\) by Euler's identity. In particular, every vector of \(Q\) is an affine-cone tangent vector at \(e\). The two-dimensional projective tangent space is naturally represented by these \(Q\)-directions.

This explicitly covers the rank-three cone: its block ranks are \((2,1)\) after relabeling, and the chosen \(e\) is outside its radical and hence outside its vertex. For rank four the block ranks are \((2,2)\). There is no remaining integral case with both blocks singular.

## 5. Dense compatibility extends, and its derivative is decisive

Choose a linear extension

\[
\widetilde v:\operatorname{Sym}^2 E\longrightarrow E
\]

of \(v\), and form the homogeneous polynomial map

\[
W(a)=\widetilde v(aT(a))\wedge a\wedge T(a)
\quad\text{with values in }\bigwedge^3 E.
\]

Compatibility on a dense subset of \(F\) makes \(W\) vanish on a dense subset of its affine cone. Therefore \(W\) vanishes on the whole affine cone. This step requires no extension of the original span-membership assertion to diagonal points: only the polynomial wedge identity is extended.

For every \(\xi\in T_e\widehat F\), differentiating this identity gives

\[
\begin{aligned}
0=dW_e(\xi)
={}&\widetilde v\bigl(\xi T(e)+eT(\xi)\bigr)\wedge e\wedge T(e)\\
&+\widetilde v(eT(e))\wedge\xi\wedge T(e)\\
&+\widetilde v(eT(e))\wedge e\wedge T(\xi).
\end{aligned}
\]

Since \(T(e)=e\), the first line vanishes. Since \(e^2\in K\), the other occurrences of \(\widetilde v\) equal \(v(e^2)\). The result is exactly

\[
v(e^2)\wedge e\wedge(T-I)\xi=0.
\]

For \(\xi\in Q\), the vector \((T-I)\xi=-2\xi\). Thus

\[
v(e^2)\wedge e\wedge q=0
\qquad\text{for every }q\in Q.
\]

Choose independent \(q_1,q_2\in Q\). The vectors \(e,q_1,q_2\) are independent, and the two wedge equations imply

\[
v(e^2)\in\operatorname{span}(e,q_1)
\cap\operatorname{span}(e,q_2)
=\mathbb C e.
\]

This contradicts square avoidance for the nonzero square \(e^2\in K\). The contradiction proves the theorem.

## 6. Projective and differential subtleties checked

- All membership conditions are independent of rescaling a representative of \([a]\), since \(aT(a)\) scales quadratically and \(K\) is linear.
- Dense span compatibility implies the wedge identity even at points where \(a\) and \(T(a)\) are dependent. The converse need not hold there, but the proof never uses that converse.
- The affine-cone calculation avoids choices of projective lifts. If expressed projectively, the derivative of \([T]\) at \([e]\), after the chosen normalization, is induced by \(T\) on \(E/\mathbb C e\). Consequently its difference from the identity is \(-2I\) on the tangent subspace represented by \(Q\), and has rank two as claimed.
- Extending \(v\) is harmless: its value at \(e^2\) is fixed, and the differentiated term involving any other value is multiplied by \(e\wedge e=0\).
- Smoothness at the chosen point is proved, not assumed. No deformation through the vertex of the rank-three cone is used.
- The proof uses \(\mathbb C\) substantively to obtain a nonzero isotropic vector in a nondegenerate binary block. It also uses characteristic zero in the linearization, the partial-trace argument, and the factor \(-2\).

## Recommended final presentation

The direct affine-cone derivative is sufficient. A separate discussion of the graph and its diagonal is optional and can be omitted. Use either the linear extension of \(v\) or the intrinsic regular map on the cone, and retain the explicit dimension equality and the smooth rank-two-block choice. With these details included, the proposed proof is complete without further assumptions.

## Final proof-file check

The mathematical argument in `PROOF.md` was read after completing the independent derivation above. It agrees with this audit. Its corrected converse statement, restricted to integral quadrics, is valid. Its explicit formula

\[
K=\{u+w\in\operatorname{Sym}^2P\oplus\operatorname{Sym}^2Q:
f_P(u)-f_Q(w)=0\}
\]

has the correct sign: \(L_T\) acts by \(+1\) on \(\operatorname{Sym}^2P\) and \(-1\) on \(\operatorname{Sym}^2Q\).

The proof file already handles the domain of \(v\) correctly by explicitly regarding the expression as a regular map on the cone. A linear extension is an optional way to expand that explanation, not a missing hypothesis or a necessary repair.

One minor wording refinement is advisable: rather than calling \(Q\) a projective tangent subspace “disjoint from \(\mathbb Ce\),” say that \(Q\cap\mathbb Ce=0\) in \(E\), and that its image in \(E/\mathbb Ce\) represents the full projective tangent space. This does not affect the proof.

