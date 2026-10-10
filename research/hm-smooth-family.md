# A smooth 87-parameter family of Horrocks–Mumford pullbacks with injective Kodaira–Spencer map

## Scope

This note proves an ordinary, fixed-base deformation statement for one explicit rank-two bundle on an abelian fourfold. It does **not** compute a noncommutative deformation obstruction or establish an all-order deformation theorem.

The unconditional conclusion is the existence of a smooth 87-dimensional parameter germ whose Kodaira–Spencer map is injective. The consequence that every Yoneda square vanishes is conditional on the separate equality
\[
h^1(X,\mathcal End E)=87.
\]
That equality is not assumed or proved in this note.

All varieties and vector spaces are over \(\mathbb C\).

## 1. The bundle and the parameter family

Let
\[
C:\ y^2=x^3-x,\qquad o=\infty,\qquad X=C^4.
\]
Write \(p_i:X\to C\) for the projections and set
\[
N=\bigotimes_{i=1}^4p_i^*\mathcal O_C(o),\qquad
\theta=c_1(N),\qquad L=N^2.
\]
Then \(N\) is the product principal polarization and
\[
h^0(X,L)=2^4=16.
\]

The degree-two morphism \(C\to\mathbb P^1\) associated with \(|2o|\) is given on the affine chart by \([u:v]=[1:x]\). Let
\[
q:X\longrightarrow Y=(\mathbb P^1)^4
\]
be its fourfold product. Put \(A=\mathcal O_Y(1,1,1,1)\), so \(q^*A=L\).

Let
\[
\rho:Y\longrightarrow\operatorname{Sym}^4(\mathbb P^1)\simeq\mathbb P^4
\]
send four binary linear forms to the coefficients of their product:
\[
\prod_{i=1}^4(u_iT+v_iS)
 =\sum_{j=0}^4 z_j T^{4-j}S^j.
\]
The five coefficients have no common zero, because the product of four nonzero linear forms is not the zero polynomial. Thus
\[
f=\rho\circ q:X\longrightarrow\mathbb P^4,\qquad f^*\mathcal O(1)=L.
\]
The maps \(q,\rho,f\) are finite of degrees \(16,24,384\), respectively.

Let \(H\) be the normalized Horrocks–Mumford bundle:
\[
\operatorname{rk}H=2,\qquad
c_1(H)=-h,\qquad c_2(H)=4h^2,
\]
where \(h=c_1(\mathcal O_{\mathbb P^4}(1))\). Define
\[
E=f^*H\otimes N.
\]
The rank-two twisting formulas give
\[
\det E\simeq\mathcal O_X,\qquad
c_2(E)=15\theta^2,\qquad
\operatorname{ch}_2(E)=-15\theta^2.
\]

Let \(U\) be the open subset of
\[
\mathbb P\!\left(H^0(X,L)^{\oplus5}\right)
\]
consisting of basepoint-free ordered five-tuples, and let \(s_0\in U\) be the tuple defining \(f\). For \(s\in U\), denote the associated morphism by \(f_s\). The space \(U\) is smooth of dimension
\[
5\cdot16-1=79.
\]

Work near \(s_0\), trivializing the tautological line on this parameter neighborhood. Then \(f_s^*\mathcal O(1)\simeq L\) is an identification in the family. For \(a\) near \(0\in X\), let \(t_a\) denote translation. For \(M\) near \(\mathcal O_X\) in \(\widehat X=\operatorname{Pic}^0(X)\), consider
\[
\mathcal E_{s,a,M}
   =t_a^*\!\left(f_s^*H\otimes N\right)\otimes M.
\tag{1}
\]
Using a normalized Poincaré bundle gives this expression as an actual family on \(X\) over a neighborhood in \(U\times X\times\widehat X\). Its central fiber is \(E\).

### Theorem

The source germ of (1) is smooth of dimension \(87=79+4+4\), and its Kodaira–Spencer map
\[
T_{s_0}U\oplus T_0X\oplus T_{\mathcal O_X}\widehat X
 \longrightarrow H^1(X,\mathcal End E)
\tag{2}
\]
is injective.

The proof occupies Sections 2–5.

## 2. A projective Atiyah vanishing lemma for \(H\)

Write
\[
\operatorname{ad}H=\mathcal End_0H
\]
and let \(\mathcal A\) be the Atiyah sheaf of the projective bundle \(\mathbb P(H)\). Its symbol sequence is
\[
0\longrightarrow\operatorname{ad}H
 \longrightarrow\mathcal A
 \longrightarrow T_{\mathbb P^4}
 \longrightarrow0.
\tag{3}
\]
The extension class is the projective Atiyah class. Its pullback controls the infinitesimal variation of \(\mathbb P(g^*H)\) when a morphism \(g\) varies. This is the principal-bundle version of the Atiyah construction [A].

We use the following classical properties of \(H\):

1. \(H\) is stable, hence
   \[
   H^0(\operatorname{ad}H)=0,\qquad
   H^0(\operatorname{ad}H(-j))=0\quad(j>0).
   \]
2. The standard five-dimensional representation of the Heisenberg group \(H_5\) is irreducible, and the Horrocks–Mumford construction is \(H_5\)-equivariant [HM, §§1–2].
3. The full projective-base stabilizer of \(H\) has zero Lie algebra. One direct reference is [M, Proposition 2, printed p.9], which states that its \(\mathrm{SL}_5\)-orbit has dimension \(24\). Section 6 below gives an independent proof from [HM].

For clarity, stability can be checked from the normalized monad
\[
5\mathcal O(-1)\longrightarrow2\Omega^2_{\mathbb P^4}(2)
 \longrightarrow5\mathcal O.
\]
The vanishing \(H^0(\Omega^2(2))=H^1(\mathcal O(-1))=0\) gives \(H^0(H)=0\). A destabilizing rank-one subsheaf of a rank-two bundle with \(c_1(H)=-h\) would give a nonzero section of \(H(-a)\) for some \(a\ge0\), hence a nonzero section of \(H\), a contradiction.

The stability vanishing for negative twists can also be read as
\[
H^0(\mathcal End H(-j))
 =\operatorname{Hom}(H,H(-j))=0
\quad(j>0),
\]
using stability and the strict slope inequality.

### Lemma 2.1

For \(j=0,1,2,3\),
\[
H^0(\mathbb P^4,\mathcal A(-j))=0.
\tag{4}
\]

#### Proof

For \(j=0\), a section of \(\mathcal A\) is an infinitesimal projective-bundle automorphism. There are no vertical sections because \(H^0(\operatorname{ad}H)=0\), and there are no nonzero base symbols because the projective stabilizer has zero Lie algebra.

For \(j\ge2\), the Euler sequence gives
\[
H^0(T_{\mathbb P^4}(-j))=0.
\]
Together with \(H^0(\operatorname{ad}H(-j))=0\), the twisted sequence (3) proves the assertion.

It remains to consider \(j=1\). The symbol image
\[
W=\operatorname{im}\!\left[
 H^0(\mathcal A(-1))
 \longrightarrow H^0(T_{\mathbb P^4}(-1))
\right]
\]
is invariant under \(H_5\). The Euler sequence identifies the target with its irreducible five-dimensional representation \(V\), so \(W=0\) or \(W=V\).

Suppose \(W=V\). Choose linear lifts of all five symbols and evaluate them to obtain an \(\mathcal O_{\mathbb P^4}\)-linear map
\[
\ell:V\otimes\mathcal O(1)\longrightarrow\mathcal A
\]
whose symbol is the Euler surjection. In the Euler sequence
\[
0\longrightarrow\mathcal O
 \longrightarrow V\otimes\mathcal O(1)
 \longrightarrow T_{\mathbb P^4}
 \longrightarrow0,
\tag{5}
\]
the kernel \(\mathcal O\) therefore maps into \(\operatorname{ad}H\). This map is zero because \(H^0(\operatorname{ad}H)=0\). Consequently \(\ell\) descends to a splitting
\[
T_{\mathbb P^4}\longrightarrow\mathcal A
\]
of (3).

Such a splitting gives a holomorphic connection on the principal \(\operatorname{PGL}_2\)-bundle associated with \(\mathbb P(H)\), hence a holomorphic connection on the associated bundle \(\operatorname{ad}H\). Its Atiyah class, and therefore its positive-degree Hodge Chern character, vanishes [A]. But
\[
\operatorname{ch}_2(\operatorname{ad}H)
 =\operatorname{ch}_2(\mathcal End H)
 =c_1(H)^2-4c_2(H)
 =-15h^2\ne0.
\]
This contradiction excludes \(W=V\). Thus \(W=0\), and the absence of vertical sections proves \(H^0(\mathcal A(-1))=0\). \(\square\)

The projective-bundle and vector-bundle base stabilizers agree here. An isomorphism of projectivizations implies \(g^*H\simeq H\otimes M\) for a line bundle \(M\) on \(\mathbb P^4\). Taking determinants gives \(M^2\simeq\mathcal O\), because base automorphisms preserve \(\mathcal O(-1)\). Since \(\operatorname{Pic}(\mathbb P^4)\simeq\mathbb Z\) has no two-torsion, \(M\simeq\mathcal O\). Thus the vector-bundle stabilizer input used above also excludes nonzero projective-bundle base symbols.

The degree \(-1\) argument is essential: finiteness of the ordinary projective stabilizer alone would not control the additional section-deformation directions after a finite pullback.

## 3. The 79 section directions

### Lemma 3.1

For the symmetric-product morphism \(\rho:Y\to\mathbb P^4\),
\[
\rho_*\mathcal O_Y
 \simeq
 \mathcal O\oplus\mathcal O(-1)^{\oplus11}
 \oplus\mathcal O(-2)^{\oplus11}\oplus\mathcal O(-3).
\tag{6}
\]

#### Proof

The finite map \(\rho\) is flat: its source is Cohen–Macaulay and its target is smooth of the same dimension. Hence \(\rho_*\mathcal O_Y\) is a vector bundle.

For every integer \(k\), Künneth gives
\[
H^i\!\left(Y,\mathcal O_Y(k,k,k,k)\right)=0
\quad(1\le i\le3).
\]
Indeed, the only possible cohomology is \(H^0\) for \(k\ge0\), none for \(k=-1\), and \(H^4\) for \(k\le-2\). Since \(\rho^*\mathcal O(1)=A\), the projection formula and Horrocks' splitting criterion [Ho] show that \(\rho_*\mathcal O_Y\) is a sum of line bundles.

There are no positive summands, since its negatively twisted \(H^0\) groups vanish. The summands are determined by
\[
\sum_{k\ge0}h^0(Y,A^k)t^k
 =\sum_{k\ge0}(k+1)^4t^k
 =\frac{1+11t+11t^2+t^3}{(1-t)^5}.
\]
This gives (6). \(\square\)

### Lemma 3.2

The Kodaira–Spencer map
\[
T_{s_0}U\longrightarrow H^1(X,\mathcal End E)
\tag{7}
\]
is injective.

#### Proof

The double-cover splitting on each elliptic factor gives
\[
q_*\mathcal O_X
 =\bigoplus_{S\subset\{1,2,3,4\}}
   \mathcal O_Y(-2S),
\]
where \(-2S\) denotes degree \(-2\) in factors in \(S\), and degree \(0\) elsewhere. Therefore
\[
H^0(Y,A)\xrightarrow{\sim}H^0(X,L):
\]
each nonempty \(S\) contributes a factor \(\mathcal O_{\mathbb P^1}(-1)\) after tensoring with \(A\), so contributes no sections.

Thus every fixed-\(L\) section deformation descends to a morphism \(\rho_s:Y\to\mathbb P^4\). The pulled-back Euler sequence and \(H^1(Y,\mathcal O_Y)=0\) identify its tangent space with
\[
H^0(Y,\rho^*T_{\mathbb P^4})
 \simeq H^0(Y,A)^{\oplus5}/\mathbb C\cdot(z_0,\ldots,z_4),
\]
of dimension \(79\).

Pull back (3) along \(\rho\). The connecting homomorphism
\[
H^0(Y,\rho^*T_{\mathbb P^4})
 \longrightarrow H^1(Y,\rho^*\operatorname{ad}H)
\tag{8}
\]
is the projective Kodaira–Spencer map of the pullback family. Its kernel is the image of \(H^0(Y,\rho^*\mathcal A)\). By (6), the projection formula and Lemma 2.1,
\[
H^0(Y,\rho^*\mathcal A)=0.
\]
Hence (8) is injective.

Finally, pullback along \(q\) is injective on the cohomology of every vector bundle on \(Y\): the unit
\[
\mathcal O_Y\longrightarrow q_*\mathcal O_X
\]
is split by \(\frac1{16}\operatorname{Tr}_q\). Tensoring and applying cohomology preserves this splitting. Tensoring the resulting family by the fixed line bundle \(N\) does not change its endomorphism bundle or its Kodaira–Spencer class. This proves (7). \(\square\)

## 4. Translation and Picard directions

Let
\[
G=(\mathbb Z/2)^4
\]
be the deck group, generated by inversion on each elliptic factor. The line bundle \(N\) has its natural divisor linearization, and every section of \(L\) is invariant: on one factor the two sections of \(\mathcal O_C(2o)\) are \(1,x\). Consequently the fixed-\(L\) family is \(G\)-equivariant with trivial action on its parameter space. Its 79-dimensional tangent image lies in the trivial-character part of \(H^1(\mathcal End E)\).

The four translation directions transform in the four singleton characters of \(G\). Their Kodaira–Spencer map is
\[
T_0X=H^0(X,T_X)\longrightarrow H^1(X,\mathcal End E),
\qquad
v\longmapsto \iota_v\operatorname{At}(E).
\tag{9}
\]
It has trace zero because \(\det E\simeq\mathcal O_X\).

If the class in (9) vanished, functoriality of the Chern character as a trace of powers of the Atiyah class would imply
\[
\iota_v\operatorname{ch}_2(E)=0.
\]
However,
\[
\iota_v\operatorname{ch}_2(E)
 =-30\,\theta\wedge\iota_v\theta.
\tag{10}
\]
The polarization identifies \(T_0X\) with \(H^1(X,\mathcal O_X)\) by \(v\mapsto\iota_v\theta\), and multiplication by \(\theta\) is injective on \(H^1(X,\mathbb C)\) by hard Lefschetz. Thus (10) is nonzero whenever \(v\ne0\). The four translation directions inject.

Their singleton characters separate them from the 79 trivial-character directions. Hence the determinant-trivial part of (2) has rank \(83\).

For the final four directions, the tangent space to \(\widehat X\) is \(H^1(X,\mathcal O_X)\), and tensoring by a varying line bundle has Kodaira–Spencer map
\[
\lambda\longmapsto \lambda\,\mathrm{id}_E.
\]
Its trace is \(2\lambda\). All 83 preceding directions have zero trace, while multiplication by \(2\) is injective. These four additional directions are therefore independent. This proves the theorem. \(\square\)

## 5. Relation with the full morphism space

The preceding construction already supplies the required smooth family. It also accounts for all tangent directions of \(\operatorname{Hom}(X,\mathbb P^4)\) at \(f\).

Locally over the component of \(\operatorname{Pic}(X)\) containing \(L\), a Poincaré line bundle has a rank-16 bundle of sections: higher cohomology of the ample fibers vanishes. Five basepoint-free sections modulo common scalar form an open subset of a projective bundle of relative dimension \(79\). Therefore
\[
\operatorname{Hom}(X,\mathbb P^4)
\]
is smooth of dimension \(79+4=83\) near \(f\).

The polarization map
\[
X\longrightarrow\widehat X,\qquad
a\longmapsto t_a^*L\otimes L^{-1}
\]
is an isogeny, so translation supplies all four line-bundle tangent directions. Taking a square root of \(f_s^*\mathcal O(1)\) is locally étale. The determinant-trivial normalization by that root recovers the same 83-dimensional tangent family used above.

No inference of Kodaira–Spencer injectivity is drawn merely from this parameter count; injectivity was proved separately in Sections 2–4.

## 6. Independent verification of the full projective stabilizer

For completeness, the zero-stabilizer-Lie-algebra input has a short proof using the original Horrocks–Mumford paper.

Put \(F=H(3)\), so \(\det F\simeq\mathcal O(5)\), and define the intrinsic subspace
\[
W_F=\operatorname{im}\!\left[
 \Lambda^2H^0(F)\longrightarrow H^0(\det F)
\right]\subset H^0(\mathcal O(5)).
\]
The original paper proves that \(W_F\) has dimension \(6\), that the Heisenberg normalizer \(N_5\) acts on \(F\), and that its conjugation representation on \(\mathfrak{sl}_5\) is irreducible [HM, p.66; Theorem 3.5 and the wedge calculation in §4].

Let \(T\subset\operatorname{PGL}_5\) be the stabilizer of \(W_F\). It is a closed algebraic group. Every projective-base automorphism preserving \(F\) preserves \(W_F\), independently of scalar choices of determinant trivialization; thus the full base stabilizer is contained in \(T\). Also \(N_5/\mu_5\subset T\).

It follows that \(\operatorname{Lie}(T)\subset\mathfrak{sl}_5\) is \(N_5\)-invariant, hence is \(0\) or all of \(\mathfrak{sl}_5\). The latter is impossible: \(W_F\) is nonzero and proper in
\[
H^0(\mathcal O(5))=\operatorname{Sym}^5(\mathbb C^5)^*,
\]
an irreducible \(\mathfrak{sl}_5\)-representation of dimension \(126\). Therefore \(\operatorname{Lie}(T)=0\), so \(T\), and consequently the full base stabilizer of \(H\), is finite.

This argument does not infer finiteness merely from the existence of the familiar finite symmetry subgroup.

## 7. Conditional consequence for Yoneda squares

### Corollary, conditional on an Ext-dimension equality

If
\[
h^1(X,\mathcal End E)=87,
\tag{11}
\]
then the Kodaira–Spencer map (2) is an isomorphism. In particular, for every
\[
u\in\operatorname{Ext}^1_X(E,E),
\]
the Yoneda square satisfies
\[
u\cup u=0\quad\text{in }\operatorname{Ext}^2_X(E,E).
\tag{12}
\]

#### Proof

The theorem gives an injective linear map between two vector spaces of dimension \(87\), so it is an isomorphism. Every \(u\) is therefore the tangent of a curve in the smooth parameter germ of (1). Pulling the family back along that curve extends the corresponding first-order bundle deformation to second order. Its ordinary second-order obstruction is the Yoneda square \(u\cup u\), so (12) follows. \(\square\)

The dimension equality (11) requires a separate calculation. Even after it is established, (12) concerns ordinary deformations of the bundle on the fixed \(X\). It does not compute the obstruction caused by deforming the ambient category, a Poisson structure, a gerbe, or a Weil-type abelian variety.

## References

- **[HM]** G. Horrocks and D. Mumford, *A rank 2 vector bundle on \(\mathbb P^4\) with 15,000 symmetries*, Topology **12** (1973), 63–81. [Author-hosted PDF](https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf). The original bundle has Chern classes \(c_1=5h,c_2=10h^2\); the normalization here is \(H=F(-3)\).
- **[M]** N. Manolache, *On the normal bundle to abelian surfaces embedded in \(\mathbb P^4(\mathbb C)\)*, INCREST Preprint 34/1985. [Institute-hosted PDF](https://imar.ro/~increst/1985/34_1985.pdf), Proposition 2, printed p.9, PDF page index 10.
- **[Ho]** G. Horrocks, *Vector bundles on the punctured spectrum of a local ring*, Proceedings of the London Mathematical Society **14** (1964), 689–713. [DOI](https://doi.org/10.1112/plms/s3-14.4.689).
- **[A]** M. F. Atiyah, *Complex analytic connections in fibre bundles*, Transactions of the American Mathematical Society **85** (1957), 181–207. [AMS PDF](https://www.ams.org/journals/tran/1957-085-01/S0002-9947-1957-0086359-5/S0002-9947-1957-0086359-5.pdf).
