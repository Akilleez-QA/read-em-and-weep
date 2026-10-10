# Stability of the Cayley pullback for the explicit rank-seven Segre map

## Result

Work over the complex numbers. Let

\[
X=(\mathbf P^1)^4,\qquad h_i=c_1\bigl(p_i^*\mathcal O_{\mathbf P^1}(1)\bigr),\qquad H_X=h_1+h_2+h_3+h_4.
\]

Let \(g:X\to Q^5\) be the explicit seven-coordinate morphism in `rank7_construction.md`, with target coordinates \((A,B,D,E,U,V,W)\) and equation

\[
q=4AE-BD+UV+UW+VW=0.
\]

For **every normalized Cayley bundle** \(C\) on \(Q^5\), the bundle

\[
\boxed{V=g^*C\text{ is slope-stable with respect to }H_X.}
\]

Consequently, let \(\pi:A=E_1\times\cdots\times E_4\to X\) be the product of elliptic double covers, chosen so that

\[
\pi^*\mathcal O_X(1,1,1,1)\simeq \mathcal O_A(2\Theta),
\]

where \(\Theta\) is the product principal polarization. Then

\[
\boxed{F=(g\circ\pi)^*C\otimes\mathcal O_A(\Theta)
\text{ is }\Theta\text{-slope-stable},\quad
\det F\simeq\mathcal O_A,\quad c_2(F)=3\Theta^2.}
\]

The argument does not assert stable restriction to the singular cubic image. It proves stability directly on the smooth source \(X\), then uses a finite-pullback stability theorem for \(\pi\).

## 1. Properties of the map used in the proof

Only the following properties of the explicit map are needed:

1. \(g^*\mathcal O_Q(1)=\mathcal O_X(1,1,1,1)\).
2. \(g\circ\sigma=g\) for the Klein four group
   \[
   K=\{1,(12)(34),(13)(24),(14)(23)\}\subset S_4,
   \]
   acting by permutation of the four \(\mathbf P^1\) factors. This action is transitive on the four factors and preserves \(H_X\).
3. The image contains the two points
   \[
   p=[1:0:0:0:0:0:0],\qquad r=[0:0:0:1:0:0:0].
   \]
   They are the images of \(([1:0],\ldots,[1:0])\) and \(([0:1],\ldots,[0:1])\), respectively. Their affine representatives satisfy \(q(p+r)=4\).

For (2), the degree-one and degree-three symmetric sums \(B,D\), and \(A,E\), are invariant under all permutations. Each of the three pair-partition sums \(U,V,W\) is individually fixed by the Klein four subgroup. No statement about the image being smooth, normal, or factorial is needed.

## 2. Cayley monad and vanishing of global sections

Let \(S\) be the negative rank-four spinor bundle on \(Q^5\), with \(c_1(S)=-2H_Q\). Ottaviani's construction gives a rank-three bundle \(G\) and exact sequences

\[
0\longrightarrow\mathcal O_Q\longrightarrow S^*\longrightarrow G\longrightarrow0,
\]

\[
0\longrightarrow\mathcal O_Q\longrightarrow G^*(1)\longrightarrow C(1)\longrightarrow0.
\]

Dualizing the first and twisting the second by \(-1\) gives

\[
0\longrightarrow G^*\longrightarrow S\longrightarrow\mathcal O_Q\longrightarrow0,
\tag{2.1}
\]

\[
0\longrightarrow\mathcal O_Q(-1)\longrightarrow G^*\longrightarrow C\longrightarrow0.
\tag{2.2}
\]

Thus the normalized Cayley monad is \(\mathcal O_Q(-1)\to S\to\mathcal O_Q\), with cohomology \(C\). These sequences are stated in Ottaviani, *On Cayley bundles on the five-dimensional quadric*, p. 88, and the construction covers every Cayley bundle. [Primary source](https://people.dimai.unifi.it/ottavian/pubblic/cayleybundle.pdf).

### 2.1 The spinor embedding, with signs fixed

Let \(W\) be the seven-dimensional quadratic vector space defining \(Q\), and let \(\Delta\) be an eight-dimensional irreducible Clifford module. Write Clifford multiplication as

\[
c:W\longrightarrow\operatorname{End}(\Delta),\qquad c(v)^2=q(v)\operatorname{id}_\Delta.
\]

The negative spinor bundle has the standard realization

\[
S_{[v]}=\ker c(v)\subset\Delta
\qquad ([v]\in Q),
\tag{2.3}
\]

so \(S\subset\Delta\otimes\mathcal O_Q\). The kernel has dimension four at every nonzero isotropic \(v\). Indeed, \(c(v)^2=0\), and choosing \(w\) with \(q(v+w)-q(v)-q(w)\ne0\) shows from the Clifford anticommutator that \(\ker c(v)=\operatorname{im}c(v)\).

This is the negative normalization: Clifford multiplication yields

\[
0\longrightarrow S\longrightarrow\mathcal O_Q^{\oplus8}\longrightarrow S(1)\longrightarrow0,
\qquad S^*\simeq S(1),
\]

the exact sequence and duality in Ottaviani, *Spinor bundles on quadrics*, Theorem 2.8(i), p. 309. [Primary source](https://people.dimai.unifi.it/ottaviani/pubblic/spinor.pdf).

For a concrete algebra model of (2.3), choose split coordinates with \(q=\sum_{i=1}^3x_i y_i+z^2\), take \(\Delta=\bigwedge^*\mathbf C^3\), and put

\[
c(v)=\sum_i x_i\varepsilon_i+\sum_i y_i\iota_i+z\tau,
\]

where \(\varepsilon_i\) is exterior multiplication, \(\iota_i\) contraction, and \(\tau\) parity. The identities \(\varepsilon_i\iota_j+\iota_j\varepsilon_i=\delta_{ij}\), together with anticommutation of parity with both, give \(c(v)^2=q(v)\). The kernel construction is the usual homogeneous spinor construction; at an isotropic coordinate vector its fiber is the four-dimensional spin representation of the Levi factor \(\operatorname{Spin}(5)\).

### 2.2 Vanishing on the Segre source

A section of \(g^*S\subset\Delta\otimes\mathcal O_X\) is a constant vector \(s\in\Delta\), since \(H^0(X,\mathcal O_X)=\mathbf C\). By evaluating it over the two points in §1, it satisfies

\[
c(p)s=c(r)s=0.
\]

But the Clifford relation gives

\[
c(p)c(r)+c(r)c(p)
=\bigl(q(p+r)-q(p)-q(r)\bigr)\operatorname{id}_\Delta
=4\operatorname{id}_\Delta.
\]

Hence \(s=0\), proving

\[
H^0(X,g^*S)=0.
\tag{2.4}
\]

Pullback preserves both exact sequences (2.1)–(2.2), since all their terms are vector bundles. The first gives \(H^0(X,g^*G^*)=0\). By Künneth,

\[
H^1\bigl(X,\mathcal O_X(-1,-1,-1,-1)\bigr)=0
\]

(in fact every cohomology group of this line bundle vanishes). The second sequence therefore gives

\[
\boxed{H^0(X,V)=0.}
\tag{2.5}
\]

### 2.3 Reproducible coordinate certificate

The companion `clifford_certificate.py` uses the above exterior-algebra model with

\[
N=W\tau-4A\varepsilon_1+E\iota_1+B\varepsilon_2+D\iota_2-(U+W)\varepsilon_3+(V+W)\iota_3.
\]

It verifies symbolically that \(N^2=-q\operatorname{id}_8\) and that the common kernel of all seven coefficient matrices is zero. Multiplication by \(\sqrt{-1}\) changes this to the \(c(v)^2=q(v)\) convention used above without changing any kernel. In particular, the coefficient matrices of \(A\) and \(E\) anticommute to \(-4\operatorname{id}_8\), providing the two-point vanishing argument directly in the original target coordinates. The certificate was executed successfully. It checks the Clifford algebra step; the stability argument itself is the geometric proof below.

## 3. Semistability from the Klein four symmetry

The Chow ring and Chern classes are

\[
\operatorname{CH}^*(X)=\mathbf Z[h_1,h_2,h_3,h_4]/(h_1^2,h_2^2,h_3^2,h_4^2),
\]

\[
c_1(V)=-H_X,\qquad c_2(V)=H_X^2.
\tag{3.1}
\]

For a line bundle \(L=\mathcal O_X(a_1,a_2,a_3,a_4)\),

\[
\mu_{H_X}(L)=6\sum_i a_i,\qquad \mu_{H_X}(V)=-12,
\tag{3.2}
\]

because \(H_X^4=24\).

Suppose \(V\) is unstable. Its unique maximal destabilizing subsheaf has rank one. Being saturated in a vector bundle on the smooth variety \(X\), it is reflexive of rank one, hence a line bundle \(L\). Since \(g\circ\sigma=g\), there are canonical identifications \(\sigma^*V\simeq V\). Uniqueness of the maximal destabilizing subsheaf and invariance of the polarization imply \(\sigma^*L\simeq L\) for every \(\sigma\in K\).

Transitivity of \(K\) on the four factors forces

\[
L\simeq\mathcal O_X(a,a,a,a).
\]

Its destabilizing slope inequality is \(24a>-12\), hence the integer \(a\) satisfies \(a\ge0\). A nonzero section of \(\mathcal O_X(a,a,a,a)\), followed by \(L\hookrightarrow V\), would give a nonzero section of \(V\), contradicting (2.5). Therefore \(V\) is semistable.

## 4. Strict semistability is impossible

First, \(V\) cannot be a direct sum of two line bundles. If

\[
V\simeq\mathcal O_X(a_1,\ldots,a_4)\oplus\mathcal O_X(-1-a_1,\ldots,-1-a_4),
\]

comparison of the \(h_i h_j\) coefficients of \(c_2(V)=H_X^2\) gives

\[
-a_i-a_j-2a_i a_j=2\quad (i<j),
\]

or, with \(t_i=2a_i+1\),

\[
t_i t_j=-3\quad(i<j).
\]

The equations for \((1,2)\) and \((1,3)\) force \(t_2=t_3\), whereas the equation for \((2,3)\) then says \(t_2^2=-3\), impossible for integers. Thus

\[
\boxed{V\text{ does not split into line bundles}.}
\tag{4.1}
\]

Now suppose \(V\) is strictly semistable. It has a saturated rank-one subsheaf \(L\) of slope \(-12\), again a line bundle. There cannot be two distinct such saturated line subsheaves \(L_1,L_2\): their generic fibers would be different (saturation determines a subsheaf from its generic fiber), so the determinant of

\[
L_1\oplus L_2\longrightarrow V
\]

would be a nonzero section of

\[
\det V\otimes L_1^{-1}\otimes L_2^{-1}.
\]

This line bundle has \(H_X\)-degree zero. Its section cannot vanish on a nonzero effective divisor, since every such divisor has positive intersection with \(H_X^3\). A nonzero section of a line bundle has either a Cartier divisor of zeros or no zeros, so this determinant is everywhere invertible. The displayed map is therefore an isomorphism of vector bundles, contradicting (4.1).

Thus the equal-slope saturated line subsheaf is unique. It must be \(K\)-invariant, so it is \(\mathcal O_X(a,a,a,a)\). Equality of slopes would require \(24a=-12\), which is impossible for an integer \(a\). This excludes strict semistability and proves stability.

## 5. The elliptic double covers preserve stability

The map \(\pi:A\to X\) is finite, separable and surjective between smooth irreducible projective varieties. The variety \(X=(\mathbf P^1)^4\) has trivial étale fundamental group, so

\[
\pi_*:\pi_1^{\mathrm{et}}(A)\longrightarrow\pi_1^{\mathrm{et}}(X)=1
\]

is surjective. Thus \(\pi\) is genuinely ramified in the precise sense of Definition 2.1 of Biswas–Das–Parameswaran, *Genuinely ramified maps and stable vector bundles*. Their Theorem 2.5 states that pullback by such a map preserves slope stability, using the pullback polarization. [Primary source](https://arxiv.org/pdf/2203.03246).

Apply that theorem to the stable vector bundle \(V\) on \(X\). It gives stability of \(\pi^*V\) with respect to \(\pi^*H_X=2\Theta\). Multiplying a polarization by a positive scalar multiplies all slopes by the same positive factor, and tensoring by a line bundle shifts all slopes by the same amount. Therefore

\[
F=\pi^*V\otimes\mathcal O_A(\Theta)
\]

is \(\Theta\)-stable.

Finally,

\[
c_1(\pi^*V)=-2\Theta,\qquad c_2(\pi^*V)=4\Theta^2,
\]

and the rank-two twisting formulas give

\[
c_1(F)=0,\qquad
c_2(F)=4\Theta^2+(-2\Theta)\Theta+\Theta^2=3\Theta^2.
\]

The asserted line-bundle identity \(\pi^*\mathcal O_X(1,1,1,1)\simeq\mathcal O_A(2\Theta)\), together with \(\det C\simeq\mathcal O_Q(-1)\), proves actual triviality of \(\det F\), not just numerical triviality.

## Scope

This establishes slope stability and the displayed Chern classes for the explicit Segre–Cayley construction. Any additional property of a proposed test bundle remains a separate question.
