# A rank-seven quadric with radical disjoint from the Segre fourfold

Work over an algebraically closed field of characteristic zero. Let

\[
X=(\mathbf P^1)^4\hookrightarrow\mathbf P^{15},\qquad
z_{i_1i_2i_3i_4}=\prod_{j=1}^4 a_j^{1-i_j}b_j^{i_j}.
\]

Indices below are written in binary, or equivalently as integers from 0 to 15. Define seven linear forms on the ambient sixteen-dimensional vector space:

\[
\begin{aligned}
A&=z_{0000}=z_0,&E&=z_{1111}=z_{15},\\
B&=z_{0001}+z_{0010}+z_{0100}+z_{1000}=z_1+z_2+z_4+z_8,\\
D&=z_{0111}+z_{1011}+z_{1101}+z_{1110}=z_7+z_{11}+z_{13}+z_{14},\\
U&=z_{0011}+z_{1100}=z_3+z_{12},\\
V&=z_{0101}+z_{1010}=z_5+z_{10},\\
W&=z_{0110}+z_{1001}=z_6+z_9.
\end{aligned}
\]

The seven supports are nonempty and disjoint, so these forms are linearly independent.

## The quadric and its rank

The ambient quadratic form

\[
\boxed{q_0=4AE-BD+UV+UW+VW}
\]

vanishes identically on the Segre fourfold. This follows by expanding after the Segre substitution; a conceptual identity is given below. In coordinates ordered as `(A,B,D,E,U,V,W)`, its Hessian is

\[
G=\begin{pmatrix}
0&0&0&4&0&0&0\\
0&0&-1&0&0&0&0\\
0&-1&0&0&0&0&0\\
4&0&0&0&0&0&0\\
0&0&0&0&0&1&1\\
0&0&0&0&1&0&1\\
0&0&0&0&1&1&0
\end{pmatrix},\qquad\det G=32.
\]

If `M` is the seven-by-sixteen coefficient matrix of the displayed linear forms, the sixteen-by-sixteen Hessian is `MᵀGM`. Since `M` has rank seven and `G` is nonsingular, this Hessian has rank exactly seven. Its radical is precisely

\[
\operatorname{rad}(q_0)=\{A=B=D=E=U=V=W=0\},
\]

a nine-dimensional vector subspace, or a projective eight-plane.

## Algebraic certificate that the radical misses X

At a Segre point, form the binary quartic

\[
F(t,s)=\prod_{j=1}^4(a_jt+b_js)
      =At^4+Bt^3s+(U+V+W)t^2s^2+Dts^3+Es^4.
\]

If a Segre point lay in the radical, every coefficient of `F` would vanish. But every pair `(a_j,b_j)` is nonzero, and the polynomial ring in `t,s` is an integral domain. A product of four nonzero linear forms cannot be zero. Therefore

\[
\boxed{\mathbf P(\operatorname{rad}(q_0))\cap X=\varnothing.}
\]

This argument is over the algebraic closure and is stronger than checking rational or finite-field points. An independent exact computational check substitutes the Segre coordinates on all sixteen standard affine charts; on every chart, the seven radical equations generate the unit ideal, with Gröbner basis `[1]`.

## Resulting finite morphism

The seven forms define a basepoint-free morphism

\[
g:X\longrightarrow Q^5=\{q_0=0\}\subset\mathbf P^6,
\qquad g^*\mathcal O_{Q^5}(1)=\mathcal O_X(1,1,1,1).
\]

The quadric `Q⁵` is smooth by the determinant above. The pullback hyperplane bundle is ample, so `g` has no positive-dimensional fiber and is finite onto its four-dimensional image.

## The image and its generic degree

The image also satisfies the cubic identity

\[
\boxed{k=AD^2+B^2E-4AE(U+V+W)-UVW=0.}
\]

Its generic degree is four. Indeed, forgetting the distinction between `U,V,W` gives the binary quartic multiplication map, whose generic fiber is the 24 orderings of four distinct roots. The simultaneous invariants `U,V,W` are fixed by the Klein four subgroup

\[
\{1,(12)(34),(13)(24),(14)(23)\}\subset S_4.
\]

The quotient `S₄/V₄≅S₃` permutes `U,V,W`. For a generic quartic these three values are pairwise distinct, leaving exactly four orderings over a generic image point. For example, the factors `t`, `t+s`, `t+3s`, `t+7s` give `(U,V,W)=(21,7,3)`.

Since `deg X=24`, the image has degree six. It lies in the complete intersection of the independent equations `q₀` and `k`, whose degree is also six, and therefore is that `(2,3)` complete intersection. In particular, this image is singular: the point

\[
[A:B:D:E:U:V:W]=[1:0:0:0:0:0:0]
\]

lies on the image, the gradient of `q₀` there is nonzero, and the gradient of `k` there is zero.

This construction consequently does not require a finite morphism onto a smooth four-dimensional quadric. The target five-dimensional quadric is smooth; the four-dimensional image inside it is singular.

## Binary-quartic explanation of the quadratic identity

Write `[ij]=a_i b_j-b_i a_j`, `p=[12][34]=V-W`, `r=[13][24]=U-W`, and `C=U+V+W`. The classical invariant of the quartic written without binomial coefficient normalization satisfies the direct polynomial identity

\[
12AE-3BD+C^2=p^2-pr+r^2.
\]

Subtracting the right side and replacing `C,p,r` gives precisely `3q₀=0`. Likewise, for

\[
J=72ACE+9BCD-27AD^2-27B^2E-2C^3,
\]

one has `J+(p+r)(2p-r)(p-2r)=0`; adding `9Cq₀` to the left side gives `−27k`.

## Scope of the result

This gives an explicit rational rank-seven quadratic form and an algebraic, geometric-basepoint-free certificate. Stability of any pulled-back bundle and additional arithmetic or “weak-test” conditions are separate questions; they are not asserted here.
