# Exceptional cubic Gauss corner: dual splitting and exclusion

## Result and scope

For the actual equivariant inclusion on the icosahedral parameter line,

\[
 E\subset H\mathcal O_T,\qquad Q=H\mathcal O_T/E,
 \qquad \operatorname{rk}E=17,\quad\deg E=-54,
\]

a hypothetical generic second-fundamental-form rank three has maximal
rank-three plateau lengths \(k,l\leq3\), as previously proved. **The corner
\(k=l=3\) is impossible.** Thus at least one of \(k,l\) is at most two.
This is not an exclusion of generic rank three, a maximal-rank assertion,
or a smoothing-closure result. In particular, the established lower bound
on the positive square remains 27, not 28.

The proof obtains two useful intermediate constraints:

1. If \(H^0(Q^*(2))=0\), there are exactly five formal equivariant splitting
   possibilities for \(Q^*\), listed below. This hypothesis holds if \(k=3\).
2. In the hypothetical corner, the cubic evaluation pairing forces the
   full second-fundamental-form image and its backward kernel:
   \[
   \operatorname{im}(\beta_E)(3)
       \simeq\mathcal O(7)\oplus W'\mathcal O(2),
   \qquad E^-\simeq(2V+2P_4)\mathcal O(-4).
   \]
   The next derivative then contradicts section persistence.

Only abstract representation arithmetic, bundle splitting, differentiation,
and invariant-divisor bounds are used. No actual coefficient, map, matrix,
rank evaluation, or local-model experiment is used. An equivariant splitting
of a bundle is never assumed to be horizontal for the ambient connection.

## 1. Inputs and conventions

The frozen inputs are proved in
`ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`,
`RANK-TWO-GAUSS-EXCLUSION-BY-ENDPOINT-FLAGS.md`, and
`GAUSS-DETERMINANT-ORBIT-RAMIFICATION.md`. Their files are unchanged.

Here \(T=\mathbb P(W^*)\), \(G=2.A_5\), and all named irreducible
representations are self-dual. The center-even irreducibles are
\(1,A,V,P_4,D_5\), of dimensions \(1,3,3,4,5\); the center-odd ones are
\(W,W',S_4,T_6\), of dimensions \(2,2,4,6\). The standard linearization
of \(\mathcal O(d)\) has central character \((-1)^d\). Since \(G\) is
perfect, there is no nontrivial one-dimensional character.

The actual presentations and modules are

\[
\begin{split}
0&\longrightarrow E\longrightarrow M_3\mathcal O(-1)
                      \longrightarrow M_4\mathcal O\longrightarrow0,\\
0&\longrightarrow Q^*\longrightarrow M_3\mathcal O(-1)
                      \longrightarrow M_2\mathcal O\longrightarrow0,\\
M_2&=A+2V+3P_4+4D_5,\\
M_3&=3W'+3S_4+6T_6,\\
M_4&=2V+4P_4+3D_5.
\end{split}
\]

The bundle \(Q\) is ample. Every \(G\)-equivariant bundle on \(T\)
has an equivariant Birkhoff--Grothendieck splitting: the canonical slope
filtration splits ordinarily, and its splittings can be averaged over
the finite group. This does not split any differential data.

Write a maximal rank-three plateau as
\(F_0\subset\cdots\subset F_m\), with \(F_k=E\), \(m=k+l\).
For each interior stage,

\[
F_i^-=F_{i-1},\qquad F_i^+=F_{i+1},\qquad
\operatorname{rk}(F_{i+1}/F_i)=3.
\]

Each plateau subbundle and Gauss transform is saturated. Images of
displayed maps are not assumed saturated unless this is explicitly proved. No interior stage
\(F_i\), \(i<m\), contains a nonzero constant subbundle. The corresponding
statement for the dual plateau also holds. These facts include equality
of the derivative kernels as sheaves, not just generically.

We will repeatedly use the following strengthened form of section
persistence. If \(i+d<m\), then

\[
                       H^0(F_i(d))=0.                 \tag{1}
\]

Indeed a nonzero section saturates to a line \(\mathcal O(-e)\subset F_i\)
with \(e\leq d\). Its polynomial coefficient span is reached by at most
\(e\) derivatives; that constant span lies in \(F_{i+e}\subset F_{i+d}\).
This contradicts the interior-stage property. This proof works for an
individual section: no invariant line or orbit of sections is assumed.

Every effective \(G\)-invariant divisor has degree in
\[
                         \mathcal S=\langle12,20,30\rangle.       \tag{2}
\]
The projective stabilizers have orders \(1,2,3,5\), with orbit sizes
\(60,30,20,12\). This also applies to the length of an equivariant
torsion cokernel between same-rank bundles, by taking determinants.

## 2. The five dual cubic splitting types

Write \(Q^*=\bigoplus_{j\geq1}R_j\mathcal O(-j)\). The lower bound on
\(j\) follows from ampleness of \(Q\). Cohomology of the second actual
presentation and its twist by \(-1\) gives the positive identities

\[
 M_3=\sum_{j\geq1}R_j\operatorname{Sym}^{j-1}W,
 \qquad
 M_2=\sum_{j\geq2}R_j\operatorname{Sym}^{j-2}W.             \tag{3}
\]

There is no cancellation in either identity. Central parity requires
\(R_j\) to have parity \((-1)^j\). If \(H^0(Q^*(2))=0\), all nonzero
blocks have \(j\geq3\). The first identity also gives the finite bound
\(j\dim R\leq54\) for each irreducible block.

For completeness, checking both positive identities leaves the following
twenty possible individual irreducible blocks \((j,R)\):

\[
\begin{gathered}
(3,W'),(3,T_6),\quad
(4,1),(4,V),(4,P_4),\quad
(5,W),(5,W'),\quad
(6,1),(6,A),\\
(7,W),(7,S_4),\quad
(8,1),(8,A),\quad
(9,W),(10,1),(11,W'),\quad
(16,1),(17,W),(18,1),(28,1).
\end{gathered}
\]

Matching the nonnegative multiplicities in (3) gives exactly five types:

\[
 Q^*=T_6\mathcal O(-3)\oplus V\mathcal O(-4)\oplus R,
                                                               \tag{4}
\]
where, in the order used below,

\[
\begin{array}{c|l}
1&R=(1+A)\mathcal O(-6)\\
2&R=W\mathcal O(-5)\oplus W\mathcal O(-7)\\
3&R=W\mathcal O(-5)\oplus\mathcal O(-6)\oplus\mathcal O(-8)\\
4&R=\mathcal O(-4)\oplus\mathcal O(-6)\oplus W\mathcal O(-7)\\
5&R=\mathcal O(-4)\oplus2\mathcal O(-6)\oplus\mathcal O(-8).
\end{array}                                                    \tag{5}
\]

This finite character calculation is reproduced exhaustively by the
companion verifier, using exact characters and nonnegative integer
multiplicities, not actual maps. Every listed type has rank 13 and degree
\(-54\). No assertion that all five occur geometrically is made.

In particular, if \(k=3\), section persistence forces the hypothesis and

\[
 H^0(Q^*(3))=T_6,\qquad
 G_0:=\operatorname{im}\bigl(H^0(Q^*(3))\mathcal O(-3)\to Q^*\bigr)
       =T_6\mathcal O(-3).                                    \tag{6}
\]

This is a canonical saturated evaluation subbundle. Each ordinary line
degree of \(Q(1)\) is at most 9.

## 3. A universal small-image lemma

Put \(U=W'+2T_6\). Consider any equivariant bundle map

\[
                 B:U\mathcal O\longrightarrow T_6\mathcal O(4)
                                                               \tag{7}
\]
whose generic rank is at most three. If \(B\ne0\), its image bundle
\(J\) is one of

\[
 W'\mathcal O,\quad W'\mathcal O(2),\quad
 V\mathcal O(1),\quad V\mathcal O(3).                          \tag{8}
\]
In particular, rank one is impossible.

To prove this, \(J\) is a locally free image on the smooth curve, is
globally generated as a quotient of \(U\mathcal O\), and embeds in
\(T_6\mathcal O(4)\). Its ordinary splitting degrees therefore lie
between 0 and 4, inclusive, and its central character is odd. An
equivariant direct summand \(R\mathcal O(e)\) must admit both a nonzero
map from the source and a nonzero map to the target:

\[
 \operatorname{Hom}_G(U,R\operatorname{Sym}^{e}W)\ne0,
 \qquad
 \operatorname{Hom}_G(R,T_6\operatorname{Sym}^{4-e}W)\ne0.       \tag{9}
\]

A one-dimensional coefficient representation is trivial, so the possible
line summands would be \(\mathcal O(1)\) and \(\mathcal O(3)\).
Their sections \(W,S_4\) have no source constituent. For coefficient
rank two, test \(W,W'\) and \(e=0,2,4\); for rank three, test \(A,V\)
and \(e=1,3\). Conditions (9) give exactly (8). Every surviving block
has rank at least two, so there can be only one such block in \(J\).

In fact \(J\) is saturated in \(T_6\mathcal O(4)\). Its saturation has
degree at most \(4\operatorname{rk}J\); the four upper bounds for the
torsion length are respectively \(8,4,9,3\). By (2), all are zero.

## 4. The cubic pairing in the corner

Assume for contradiction \(k=l=3\). The frozen exceptional primal
splitting is

\[
 E=U\mathcal O(-3)\oplus V\mathcal O(-4),\qquad U=W'+2T_6.
                                                               \tag{10}
\]
Let \(F=U\mathcal O(-3)\) be its canonical cubic evaluation subbundle,
and use \(G_0\) from (6). Formula (1), applied one step backward in
each of the dual plateaux, gives

\[
       H^0(E^-(3))=H^0((Q^*)^-(3))=0.                         \tag{11}
\]

Restrict the two second fundamental forms and twist by 3:

\[
 \phi:U\mathcal O\longrightarrow Q(1),\qquad
 \psi:T_6\mathcal O\longrightarrow E^*(1).
                                                               \tag{12}
\]
Both maps are injective on global sections by (11). The pairing of
\(\beta_E|_F\) with \(G_0\) is the quartic map (7): it is the
composition of \(\phi\) with the canonical projection
\(\pi:Q(1)\to T_6\mathcal O(4)\) dual to the inclusion of \(G_0\).
The two second fundamental forms are negative transposes, as follows by
differentiating the identity pairing \(E\perp Q^*\).

Set \(a=\operatorname{rk}\phi\), \(b=\operatorname{rk}\psi\),
\(t=\operatorname{rk}B\). All are at most three. Factoring the rank-three
second fundamental form through its generic rank-three quotient gives
the elementary inequalities

\[
       t\geq a+b-3,\qquad t\leq\min(a,b).                    \tag{13}
\]

Neither \(a\) nor \(b\) can be one. A rank-one image of \(\phi\) would
be a line of degree at most 9, with at most 10 global sections, whereas
\(\phi\) is injective on the 14-dimensional space \(U\). A rank-one
image of \(\psi\) would be a globally generated, center-odd line
\(\mathcal O(e)\), with odd \(e\leq5\), because
\(E^*(1)=U\mathcal O(4)\oplus V\mathcal O(5)\). Containing \(T_6\)
in its sections requires \(e=5\), but there is no equivariant map
\(\mathcal O(5)\to U\mathcal O(4)\oplus V\mathcal O(5)\).
Both ranks are nonzero by global injectivity. Thus \(a,b\geq2\), and
(13) and the small-image lemma give \(t\geq2\).

Every possibility (8) has fewer than 14 sections. Hence
\(H^0(\ker B)\ne0\). If \(a=t\), the kernels of \(\phi\) and \(B\)
are equal: both are saturated in the source and have the same generic
kernel. This contradicts (11). Consequently

\[
                        (a,b,t)=(3,2,2).                    \tag{14}
\]

If \(J=W'\mathcal O\), the global kernel of \(B\) is \(2T_6\), of
dimension 12. Its \(\phi\)-image has rank one, because the kernel of
\(\operatorname{im}\phi\to J\) has rank one. But that line has degree
at most 9 and cannot contain12 independent global sections. Therefore

\[
             J=W'\mathcal O(2),\qquad
             K_0:=\ker H^0(B)=W'+T_6.                        \tag{15}
\]
Here \(H^0(W'\mathcal O(2))=T_6\); the induced map on sections is a
nonzero map to this irreducible representation, hence is surjective.

The image \(L=\phi(K_0\mathcal O)\) is a globally generated, center-odd
line of degree \(e\leq9\), whose sections contain \(W'+T_6\).
Its degree is at least 7. The only odd possibilities are7 and 9, and

\[
 \operatorname{Sym}^7W=W'+T_6,\qquad
 \operatorname{Sym}^9W=S_4+T_6.
\]
It follows that \(L=\mathcal O(7)\). Let
\(N=\ker(\operatorname{im}\phi\to J)\). This is a line containing
\(L\); as a subbundle sheaf of \(Q(1)\), it has degree at most 9.
Thus the invariant torsion length of \(N/L\) is at most 2, and (2)
forces \(N=L\). The extension

\[
0\longrightarrow\mathcal O(7)\longrightarrow\operatorname{im}\phi
 \longrightarrow W'\mathcal O(2)\longrightarrow0
\]
splits, since \(H^1(\mathcal O(5))=0\); averaging makes the splitting
equivariant. We have proved

\[
                      I:=\operatorname{im}\phi
                       =\mathcal O(7)\oplus W'\mathcal O(2).
                                                               \tag{16}
\]

## 5. Ambient saturation and the full derivative image

Let \(\overline I\) be the saturation of \(I\) in \(Q(1)\). Its
determinant defect \(\tau=\deg\overline I-11\) belongs to \(\mathcal S\).
The largest three ordinary line degrees of the five types of \(Q(1)\)
have sums, respectively,

\[
                            21,22,22,23,23.                  \tag{17}
\]
Every rank-three subsheaf has degree at most this sum, by its determinant
inclusion into \(\bigwedge^3 Q(1)\). Thus \(\tau=0\) in the first
three types, and \(\tau\in\{0,12\}\) in the last two.

If \(\tau=12\), the degree 23 bound is attained. The unique highest-degree
line component of \(\bigwedge^3 Q(1)\) is the determinant of the
canonical top rank-three subbundle

\[
 W\mathcal O(8)\oplus\mathcal O(7)\quad\text{in type 4},
 \qquad
 \mathcal O(9)\oplus2\mathcal O(7)\quad\text{in type 5}.
                                                               \tag{18}
\]
Indeed the third and fourth ordinary degrees are7 and 5 in both cases.
The determinant map from \(\mathcal O(23)\) cannot have a component
in a smaller-degree summand. Its Pluecker line therefore equals the
determinant line in (18); over the function field this identifies the
rank-three subspaces, and saturation identifies the subbundles.

But every map from either bundle (18) to \(T_6\mathcal O(4)\) vanishes
by degree. This would make \(\pi|_I\), and therefore \(B\), zero.
This contradiction proves \(\tau=0\) in all five cases.

The full image of \(\beta_E(3):E(3)\to Q(1)\) contains \(I\) and
has the same generic rank. Since \(I\) is saturated in \(Q(1)\),
the two images coincide. Consequently

\[
 E/E^-=I(-3)=\mathcal O(4)\oplus W'\mathcal O(-1),
 \qquad \deg E^-=-56.                                      \tag{19}
\]
The rank 14 bundle \(E^-(3)\) has degree \(-14\) and has no sections
by (11). Its ordinary splitting is therefore \(14\mathcal O(-1)\).
Its equivariant coefficient representation is determined at twist 4:

\[
\begin{split}
 H^0(E^-(4))
  &=U W+V-\bigl(\operatorname{Sym}^8W+W'\operatorname{Sym}^3W\bigr)\\
  &=2V+2P_4.
\end{split}
\]
Here \(H^1(E^-(4))=0\), so this is an equality of genuine
representations. This proves

\[
                       E^-=(2V+2P_4)\mathcal O(-4).           \tag{20}
\]

## 6. The next derivative contradicts persistence

Since \(E^-\) is an interior plateau stage, its forward transform is
\(E\), and its derivative kernel is \(E^{--}\). The derivative descends
regularly to a bundle map

\[
 E^-(4)\longrightarrow(E/E^-)(2)
          =\mathcal O(6)\oplus W'\mathcal O(1).               \tag{21}
\]
The source has14 sections. The target has \(7+2\cdot2=11\) sections.
Equivariantly, their representations are respectively
\(2V+2P_4\) and \(V+2P_4\). Thus the kernel on sections contains
at least one copy of \(V\):

\[
                          H^0(E^{--}(4))\ne0.                \tag{22}
\]

On the other hand, \(E^{--}=F_{k-2}\), and
\((k-2)+4=k+2<m=k+3\). Formula (1) gives
\(H^0(E^{--}(4))=0\), contradicting (22). Singular or ramified parameters
cannot change this argument: the derivative maps and their kernels are
sheaf maps on the whole curve, saturation is explicit, and every torsion
correction is effective and constrained by (2).

This excludes \(k=l=3\), and only that maximal corner. The remaining
rank-three profiles require additional arguments.

## Reproduction

Run `python3 verify_exceptional_cubic_gauss_corner.py` in this directory.
It checks the exact positive-character enumeration, all five dual types,
the complete small-image list, the line-character eliminations, the
saturation degree bounds, and the final section-character discrepancy.
The geometric jet, saturation, and derivative arguments are the proof
above, not claims that a finite arithmetic script independently proves
the geometry.
