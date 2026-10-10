# Geometry of the rank-seven Segre projection

## Verdict and precise scope

Over the complex numbers, all three central assertions are correct:

1. The displayed quadratic form has rank exactly seven and its projective radical is disjoint from the Segre fourfold.
2. The resulting finite morphism has generic degree four. Its scheme-theoretic image is exactly the complete intersection of the displayed quadric and cubic in projective six-space.
3. Pulling a normalized Cayley bundle back from the smooth five-dimensional target quadric produces a rank-two vector bundle with centered second Chern class `3H²/4`.

There are useful qualifications. The four-dimensional image is singular; the finite map is not flat along its branch image; and “centered” is a rational Chern-class normalization, not an actual half-hyperplane twist. None of these qualifications obstructs the vector-bundle construction. Stability needs a separate argument, whereas indecomposability follows from the Chern classes alone. That separate argument has now been independently verified and is given in `cayley_pullback_stability.md`: the pullback is slope-stable with respect to `H` for every normalized Cayley bundle.

The scheme-image, quotient, and singularity arguments below are exact proofs. `verify_geometry.py` separately verifies the polynomial identities and coordinate changes using rational arithmetic. The supplied `primitive_certificate.py` was also run successfully, including all sixteen geometric-basepoint checks.

## 1. Setup

Write

\[
X=(\mathbf P^1)^4,\qquad H=h_1+h_2+h_3+h_4,
\qquad z_{i_1i_2i_3i_4}=\prod_{j=1}^4a_j^{1-i_j}b_j^{i_j}.
\]

Binary indices are ordered from `0000` to `1111`. Set

\[
\begin{aligned}
A&=z_0,&B&=z_1+z_2+z_4+z_8,\\
D&=z_7+z_{11}+z_{13}+z_{14},&E&=z_{15},\\
U&=z_3+z_{12},&V&=z_5+z_{10},&W&=z_6+z_9,
\end{aligned}
\]

and

\[
q=4AE-BD+UV+UW+VW,\qquad
k=AD^2+B^2E-4AE(U+V+W)-UVW.
\]

The supports of the seven linear forms are pairwise disjoint and nonempty, so their coefficient matrix `M` has rank seven. Direct homogeneous substitution proves that both `q` and `k` vanish on `X`.

In coordinate order `(A,B,D,E,U,V,W)`, the Hessian of `q` is

\[
G=\begin{pmatrix}
0&0&0&4&0&0&0\\
0&0&-1&0&0&0&0\\
0&-1&0&0&0&0&0\\
4&0&0&0&0&0&0\\
0&0&0&0&0&1&1\\
0&0&0&0&1&0&1\\
0&0&0&0&1&1&0
\end{pmatrix},\quad\det G=32.
\]

The ambient sixteen-variable Hessian is `MᵀGM`. Because `M` is surjective as a linear map to the seven-dimensional coordinate space and `G` is nonsingular, its rank is seven and its kernel is `ker M`. The radical is therefore a vector nine-plane, or projective eight-plane.

This determinant refers to the Hessian, not the coefficient matrix in `q(v)=vᵀSv`; the latter is `G/2` and has determinant `1/4`.

The smooth target quadric is even split over the rational numbers, as witnessed by

\[
q=4AE-BD+(U+W)(V+W)-W^2.
\]

For Cayley bundles, the assertions below are made over `C`, where no field-of-definition issue arises.

## 2. No basepoints; finiteness

At every geometric point of `X`,

\[
\prod_{j=1}^4(a_jt+b_js)
 =At^4+Bt^3s+(U+V+W)t^2s^2+Dts^3+Es^4.
\]

Each factor is nonzero. Consequently this polynomial cannot be zero in the domain `C[t,s]`. Thus the seven projection coordinates cannot vanish simultaneously, and the radical misses `X` geometrically, not merely on rational points.

We obtain

\[
g:X\longrightarrow Q^5=V(q)\subset\mathbf P^6,
\qquad g^*\mathcal O_{Q^5}(1)=\mathcal O_X(H).
\]

The target quadric is smooth. The pullback hyperplane bundle is ample. If a fiber had positive dimension, it would contain a complete curve on which this ample bundle had degree zero, a contradiction. Thus the projective morphism is quasi-finite, hence finite onto its image. Its image has dimension four.

## 3. Generic degree exactly four

Let

\[
K=\{1,(12)(34),(13)(24),(14)(23)\}\cong(\mathbf Z/2)^2
\]

act on `X` by permuting factors. All seven projection coordinates are `K`-invariant.

On the source chart where all `a_i` are nonzero, put `t_i=b_i/a_i` and normalize `A=1`. Then

\[
B=e_1(t),\quad D=e_3(t),\quad E=e_4(t),
\]

\[
U=t_1t_2+t_3t_4,\quad V=t_1t_3+t_2t_4,
\quad W=t_1t_4+t_2t_3,
\]

with `U+V+W=e_2(t)`. The binary quartic coefficients determine the unordered set of four factors. On the open locus of four distinct factors, the possible orderings form an `S_4`-torsor of size 24. The quotient `S_4/K=S_3` permutes the three pairings `U,V,W`, and

\[
\begin{aligned}
U-V&=(t_1-t_4)(t_2-t_3),\\
U-W&=(t_1-t_3)(t_2-t_4),\\
V-W&=(t_1-t_2)(t_3-t_4).
\end{aligned}
\]

These differences are nonzero for four distinct `t_i`. Hence remembering the ordered triple `(U,V,W)` leaves exactly the four orderings in one `K`-orbit. This proves that the separable generic degree of `g` is four.

Since

\[
\int_XH^4=4!=24,
\]

the image `Y` has degree `24/4=6`.

## 4. Scheme-theoretic image: the degree argument completed

The quadric `q` is irreducible, since it is nondegenerate in seven variables. The cubic `k` is not a multiple of `q`: at `(A,B,D,E,U,V,W)=(1,0,1,0,0,0,0)` one has `q=0` and `k=1`. Thus `(q,k)` is a regular sequence. Its projective zero scheme `Y₀` is a codimension-two complete intersection, is Cohen–Macaulay and unmixed, and has degree six.

The scheme-theoretic image `Y` of the integral variety `X` is integral, has dimension four, and is contained in `Y₀`. Its degree is already six. Therefore the cycle of `Y₀` has exactly one component, namely `Y`, with generic multiplicity one; there is no degree left for any additional component or larger multiplicity. The complete intersection has no embedded associated primes. An unmixed scheme with this single generically reduced component is reduced. Consequently

\[
\boxed{\ I(Y)=(q,k),\qquad Y=V(q,k)\ \text{scheme-theoretically}.\ }
\]

In particular, “degree six equals degree six” is sufficient here only together with the regular-sequence/unmixedness argument; equality of degrees alone would not generally rule out embedded structure.

The homogeneous complete-intersection ideal is saturated, for example because its coordinate ring has depth five. Thus the statement describes the actual homogeneous ideal, not just its saturation or its support.

## 5. Stronger result: the image is the Klein-four quotient

Let

\[
R=\bigoplus_{n\geq0}H^0(X,\mathcal O_X(nH)).
\]

In degree one, the seven displayed forms are exactly the orbit-sum basis of `R₁ᴷ`: the binary strings have seven `K`-orbits, classified as weights zero, one, three, four, and three pairings of weight two.

Let `S` be the subring generated by these seven invariants. Section 4 identifies

\[
S\cong\mathbf C[A,B,D,E,U,V,W]/(q,k).
\]

There is an inclusion `S ⊂ Rᴷ`. On `R_n ≅ H⁰(P¹,O(n))^{\otimes4}`, the identity has trace `(n+1)^4`; each nonidentity double transposition has trace `(n+1)^2`. Averaging traces gives

\[
\dim R_n^K=\frac{(n+1)^4+3(n+1)^2}{4}.
\]

Its generating series is

\[
\sum_{n\geq0}\dim R_n^K\,t^n
=\frac{1+2t+2t^2+t^3}{(1-t)^5}
=\frac{(1-t^2)(1-t^3)}{(1-t)^7},
\]

exactly the Hilbert series of `S`. Therefore `S=Rᴷ` in every degree. It follows that

\[
\boxed{\ Y\cong X/K,\qquad g\text{ is the quotient map}.\ }
\]

In particular `Y` is normal, every geometric fiber has one `K`-orbit as its underlying point set, and the generic extension of function fields is Galois with group `K`.

## 6. Exact local equation and singular scheme

On `A=1`, put `C=U+V+W` and make the polynomial coordinate change

\[
\begin{aligned}
s&=B,\\
X&=B^2-4(V+W),\\
Y&=B^2-4(U+W),\\
Z&=B^2-4(U+V),\\
T&=B^3-4BC+8D.
\end{aligned}
\]

Here the local variable `Y` is distinct from the global image notation. The inverse formulas are

\[
\begin{aligned}
U&=(s^2+X-Y-Z)/8,\\
V&=(s^2-X+Y-Z)/8,\\
W&=(s^2-X-Y+Z)/8,\\
D&=(s^3-s(X+Y+Z)+2T)/16.
\end{aligned}
\]

The quadric eliminates `E=(BD-UV-UW-VW)/4`. After this elimination and change of variables,

\[
\boxed{\ 64k=T^2-XYZ.\ }
\]

Thus

\[
Y\cap\{A\ne0\}\cong
\mathbf A^1_s\times\operatorname{Spec}
\mathbf C[X,Y,Z,T]/(T^2-XYZ).
\]

For the quotient interpretation, use Hadamard source coordinates

\[
\begin{aligned}
s&=t_1+t_2+t_3+t_4,\\
x&=t_1+t_2-t_3-t_4,\\
y&=t_1-t_2+t_3-t_4,\\
z&=t_1-t_2-t_3+t_4.
\end{aligned}
\]

The three nonidentity elements of `K` fix respectively `x,y,z` and negate the other two. The invariant coordinates are precisely `X=x²`, `Y=y²`, `Z=z²`, `T=xyz`, with relation `T²=XYZ`.

The hypersurface Jacobian ideal is

\[
(T,XY,XZ,YZ).
\]

This is radical, being the ideal of the union of the three coordinate axes in `(X,Y,Z)` with `T=0`, times the `s`-line. So the singular scheme is reduced, not merely reduced after forgetting multiplicities.

These local descriptions cover the whole quotient after diagonal projective changes of coordinates on the four factors. Indeed, any four points of `P¹` avoid some chosen point at infinity. The diagonal `PGL₂` action commutes with `K`, preserves the seven-dimensional invariant linear system, and therefore acts on the quotient. There are no additional singularities hidden in `A=0`.

## 7. Global singular locus: three Veronese surfaces

The three nonidentity elements of `K` have fixed loci

\[
F_{12|34}=\{x_1=x_2,\ x_3=x_4\},
\quad F_{13|24},\quad F_{14|23},
\]

each isomorphic to `P¹×P¹`. They meet pairwise in the small diagonal `P¹` of quadruples with all four entries equal. The singular locus is exactly the union of their images.

For `F_{12|34}`, write the tuple as `([a:b],[a:b],[c:d],[c:d])`. Its quotient identifies the two pairs, so it is `Sym²(P¹)≅P²`. With

\[
[r:h:v]=[ac:ad+bc:bd],
\]

its image is parametrized by

\[
\boxed{
[A:B:D:E:U:V:W]
=[r^2:2rh:2hv:v^2:h^2-2rv:2rv:2rv].
}
\]

These coordinates span the full quadratic Veronese linear system on `P²`. Thus this is a Veronese surface of degree four inside the hyperplane `V=W`; the other two are obtained by permuting `U,V,W`.

Their pairwise and triple scheme-theoretic intersections are the same reduced rational normal quartic

\[
[a:b]\longmapsto
[a^4:4a^3b:4ab^3:b^4:2a^2b^2:2a^2b^2:2a^2b^2].
\]

At a point on one surface away from this quartic, the analytic singularity is a smooth two-dimensional factor times the ordinary `A₁` surface singularity `uv=w²`. At a point of the quartic it is a smooth line times the three-dimensional quotient singularity `T²=XYZ`, equivalently `C³/K` for the even-sign action.

As a consistency check, adjunction gives `ω_Y≅O_Y(−2)` and `g*ω_Y≅ω_X`, matching the absence of divisorial ramification.

## 8. Finiteness is not flatness

The quotient is étale wherever the `K`-action is free, and the fixed loci have codimension two. Thus the cover is quasi-étale: there is no branch divisor, although there is a codimension-two branch image.

Its fibers have the following scheme lengths:

- Off the singular locus: four reduced points, total length four.
- On a singular Veronese surface, off the common quartic: two support points, each with local fiber length three, total length six.
- On the common quartic: one support point, with fiber length seven.

For the middle assertion, the stabilizer is `C₂` acting by sign on two normal coordinates `u,v`, and its origin fiber is

\[
\mathbf C[u,v]/(u^2,uv,v^2),
\]

of length three. For the last assertion, the origin fiber of the even-sign quotient is

\[
\mathbf C[x,y,z]/(x^2,y^2,z^2,xyz),
\]

with basis `1,x,y,z,xy,xz,yz`, of length seven. This proves in particular that `g` is not flat on the branch image. “Degree four” here means generic degree, not constant fiber length.

## 9. Cayley-bundle application

Let `h=c₁(O_{Q⁵}(1))`. A normalized Cayley bundle `C` on the smooth complex quadric `Q⁵` is a rank-two bundle with

\[
c_1(C)=-h,\qquad c_2(C)=h^2.
\]

For the standard normalization and existence, see Giorgio Ottaviani, *On Cayley bundles on the five-dimensional quadric*, Bollettino U.M.I. (7), 4-A (1990), 87–100: [author-hosted paper](https://people.dimai.unifi.it/ottavian/pubblic/cayleybundle.pdf). His normalized numerical `c₂=1` means the coefficient of `h²` on `Q⁵`. This should not be confused with conventions on a three-dimensional hyperplane section, where `h²` is twice the line class.

Set `E=g*C`. Pullback of a vector bundle is locally free for every morphism; flatness of `g` is unnecessary. Chern classes are functorial, so

\[
\operatorname{rk}(E)=2,\qquad c_1(E)=-H,
\qquad c_2(E)=H^2=2\sum_{i<j}h_ih_j.
\]

For the convention

\[
\overline c_2(E):=c_2(E)-\frac14c_1(E)^2,
\]

one gets

\[
\boxed{\ \overline c_2(E)=\frac34H^2,
\qquad 4c_2(E)-c_1(E)^2=3H^2.\ }
\]

Equivalently, rationally centering the Chern character gives

\[
e^{H/2}\operatorname{ch}(E)
=2-\frac34H^2+\frac{3}{64}H^4
\]

through degree four.

Important limitations and consequences:

1. There is no line bundle `O_X(H/2)`: `Pic(X)≅Z⁴` and `H=(1,1,1,1)` is not divisible by two. The centered expression is formal/rational. The construction does not provide an honest rank-two bundle with `c₁=0` and `c₂=3H²/4`; indeed that latter `c₂` would have nonintegral coefficient `3/2` on each `h_i h_j`.
2. The singular image causes no obstruction: the actual target on which `C` is defined is the smooth `Q⁵`, and `g` is an everywhere-defined morphism into it.
3. Stability of `C` on `Q⁵` does not by itself establish stability of this pullback, because the map is not dominant onto `Q⁵`. The separate stability proof is supplied in `cayley_pullback_stability.md`; any additional test criterion remains a separate question.
4. Indecomposability does follow. If `E=L⊕M`, write `c₁(L)=Σa_i h_i`, so `c₁(M)=Σ(−1−a_i)h_i`. Matching `c₂(E)=H²` gives `−a_i−a_j−2a_ia_j=2` for all `i<j`, equivalently

\[
(2a_i+1)(2a_j+1)=-3\quad\text{for all }i<j.
\]

For three distinct indices these nonzero integer products force two factors equal and hence an integer square equal to `−3`, impossible. Thus the pulled-back rank-two bundle cannot split into line bundles.
5. Dualizing gives another version with `c₁=H`, the same `c₂=H²`, and the same centered class.

## Final conclusion

The rank-seven projection is a valid exact construction, and its bundle application is valid with the stated meaning of centered Chern class. Its geometry is unusually explicit: the image is the normal Klein-four quotient `(P¹)⁴/K`, embedded as a singular `(2,3)` complete intersection in the smooth target quadric. No smoothness of the image and no flatness of the projection are needed for the Cayley pullback.
