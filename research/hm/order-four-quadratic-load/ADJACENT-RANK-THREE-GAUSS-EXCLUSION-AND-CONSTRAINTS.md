# Adjacent rank-three Gauss profiles: exclusion and constraints

## Result and scope

For the actual equivariant bundle inclusion, the hypothetical generic
second-fundamental-form rank-three profile **\((k,l)=(2,3)\) is impossible**.
Together with the frozen exclusion of \((3,3)\), this proves

\[
             \text{generic SF rank three and }l=3\quad\Longrightarrow\quad k=1.
                                                               \tag{1}
\]

For the adjacent profile \((3,2)\), two of the 28 formal primal splitting
types are excluded, and three other types satisfy the additional dual
restriction in Section 8. The profile \((3,2)\) itself is not excluded.

These statements do not exclude generic SF rank three. The established
numerical bounds remain generic SF rank at least three and positive-square
rank at least 27. No maximal-rank, generic-section-count, or smoothing
conclusion is asserted.

Everything below concerns abstract equivariant representations, bundle
degrees, ordinary differentiation, and universal jet persistence. There
are no selected HM coefficients, actual-instance map evaluations, matrix/rank tests,
or local-model experiments. All earlier published files remain unchanged.

## 1. Frozen inputs and notation

We use the notation and proved geometric facts of
`ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md` and
`EXCEPTIONAL-CUBIC-GAUSS-CORNER-EXCLUSION.md`.

On \(T=\mathbb P(W^*)\), with \(G=2.A_5\),

\[
 E\subset H\mathcal O,\quad Q=H\mathcal O/E,\quad
 (\operatorname{rk}E,\deg E)=(17,-54),\quad
 (\operatorname{rk}Q^*,\deg Q^*)=(13,-54).
\]

Both bundles are center-even, and \(Q\) is ample. Write a maximal
rank-three plateau as \(F_0\subset\cdots\subset F_m\), with
\(E=F_k\), \(m=k+l\). All plateau bundles and Gauss transforms are
saturated. Their interior derivative kernels and forward transforms are
the adjacent stages. The dual plateau exchanges \(k\) and \(l\).

The section-persistence fact needed here is

\[
             i+d<m\quad\Longrightarrow\quad H^0(F_i(d))=0.    \tag{2}
\]

A section saturates to a polynomial line of degree at most \(d\); its
coefficient span is reached by at most \(d\) derivatives, inside
\(F_{i+d}\). An interior stage has no nonzero constant subbundle.
This argument applies also when \(F_i=F_0\), and to the dual plateau.

Equivariant Birkhoff--Grothendieck splitting is legitimate by finite-group
averaging; it is never treated as a horizontal splitting. Central parity
and the absence of nontrivial characters determine the parity of each
coefficient representation. An equivariant torsion determinant has length
in \(\langle12,20,30\rangle\). In particular, a positive such length
cannot be smaller than 12.

The positive dual splitting identities are

\[
\begin{split}
Q^*&=\bigoplus_{j\geq1}R_j\mathcal O(-j),\\
M_3&=\sum R_j\operatorname{Sym}^{j-1}W,
&M_3&=3W'+3S_4+6T_6,\\
M_2&=\sum_{j\geq2}R_j\operatorname{Sym}^{j-2}W,
&M_2&=A+2V+3P_4+4D_5.
\end{split}                                                   \tag{3}
\]

All named irreducibles are self-dual. We use \(1,A,V,P_4,D_5\) for the
center-even representations and \(W,W',S_4,T_6\) for the center-odd ones.

## 2. A stronger derivative-image degree bound when \(l=3\)

Suppose \(l=3\) and \(k\geq2\). The unique possible primal splitting is

\[
 E=U\mathcal O(-3)\oplus V\mathcal O(-4),\qquad U=W'+2T_6.
                                                               \tag{4}
\]

Put \(K=E^-\) and let \(I=\operatorname{im}(\beta_E)(3)\subset Q(1)\)
be the actual image sheaf, not its saturation. It is a bundle of rank
three, and

\[
 I\simeq(E/K)(3),\qquad D:=\deg I=-45-\deg K.                 \tag{5}
\]

Persistence gives \(H^0(K(3))=0\) and \(H^0(E^{--}(4))=0\).
The first implies \(\deg K\leq-56\), so \(D\geq11\).
Moreover, \(I(1)\) is a quotient of the globally generated bundle
\(E(4)=U\mathcal O(1)\oplus V\mathcal O\). Every ordinary degree of
\(I\) is therefore at least \(-1\).

If \(D=11\), the rank-14 bundle \(K(3)\) has degree \(-14\) and no
sections, hence is \(14\mathcal O(-1)\). The next derivative is

\[
 K(4)\longrightarrow(E/K)(2)=I(-1),\qquad
 \ker=E^{--}(4).                                             \tag{6}
\]

Its source has 14 sections. If \(n_{-1}\) is the number of degree
\(-1\) summands of \(I\), then
\(h^0(I(-1))=11+n_{-1}\leq13\): at most two such summands are possible
in a rank-three bundle of degree 11. This contradicts the second
persistence vanishing. Finally, \(I\) is center-odd of rank three, so
its determinant has odd degree. We have proved the new universal bound

\[
                              D\geq13.                       \tag{7}
\]

For later use, the saturated full dual-image bundle in \(E^*\) is

\[
        S_0:=(E/K)^*=I^*(3),\qquad \deg S_0=9-D\leq-4.        \tag{8}
\]
The actual image of \(\beta_{Q^*}(2)\) is contained in \(S_0\), and
equals it if \(I\) is saturated in \(Q(1)\). This follows by dualizing
the factorization of \(\beta_E(3)\) through its image.

## 3. Thirty-seven dual types for \(k=2\)

Assume now \((k,l)=(2,3)\). Dual persistence gives \(H^0(Q^*(1))=0\),
so all blocks in (3) have \(j\geq2\).

The exhaustive positive-character calculation gives 23 eligible
individual blocks: the twenty blocks in the frozen cubic-corner proof,
together with \((2,V),(2,P_4),(2,D_5)\). The bound
\(j\dim R\leq\dim M_3=54\) makes this calculation finite. Matching
nonnegative multiplicities in both identities gives exactly 37 formal
splittings. Their quadratic section modules
\(R_2=H^0(Q^*(2))\) have the following counts:

\[
\begin{array}{c|rrrrrrr}
R_2&0&D_5&P_4&P_4+D_5&2P_4&V&V+P_4\\\hline
\text{count}&5&7&8&6&3&5&3.
\end{array}                                                   \tag{9}
\]

The companion verifier reproduces the full nonnegative-integer recursion.
No realization of these formal splitting types is presumed.

### 3.1 Nonzero quadratic evaluation

Suppose \(R_2\ne0\). The canonical evaluation subbundle is
\(R_2\mathcal O(-2)\subset Q^*\). Restricting the dual derivative gives

\[
                  \psi_2:R_2\mathcal O\longrightarrow E^*.
                                                               \tag{10}
\]

It is injective on global sections: its kernel is contained in
\((Q^*)^-(2)\), which has no sections by (2).
Its image cannot have rank three. A globally generated rank-three
image would lie in the negative-degree rank-three bundle \(S_0\),
contradicting effectiveness of the determinant inclusion.

A rank-one image is also impossible. It would be an even-degree line
\(\mathcal O(e)\), \(0\leq e\leq4\), with sections receiving a
constituent of \(R_2\), which is supported on \(V,P_4,D_5\).
Degrees zero and two give \(1,A\); degree four gives \(D_5\), but
\(\operatorname{Hom}_G(\mathcal O(4),E^*)=0\).

The image therefore has rank two. Equivariant splitting and the source
and target Hom conditions give exactly

\[
             J_2=W'\mathcal O(1)\quad\text{or}\quad W'\mathcal O(3).
                                                               \tag{11}
\]
There can be no line summand for the same reason as above. For the
irreducible rank-two coefficient spaces, test \(W,W'\) at degrees one
and three. The maximum possible saturation defects in \(E^*\) are six
and two, respectively, so both images are saturated.

Their sections are \(P_4\) and \(V+D_5\). Thus global injectivity and
(9) force

\[
\begin{array}{c|c}
J_2&R_2\\\hline
W'\mathcal O(1)&P_4\\
W'\mathcal O(3)&V\ \text{or}\ D_5.
\end{array}                                                   \tag{12}
\]
The mixed module \(V+D_5\) is absent by (9), not by injectivity alone.

Because \(J_2\) is saturated in \(E^*\), dualizing gives a surjection
\(E\to J_2^*\). The corresponding projection of the full derivative
image is therefore an exact sequence

\[
        0\longrightarrow N\longrightarrow I
          \longrightarrow J_2^*(3)\longrightarrow0,             \tag{13}
\]
where \(N\) is an equivariant line subsheaf of \(Q(1)\).

If \(R_2=V\) or \(D_5\), the quotient is \(W'\mathcal O\), so
\(\deg N=D\geq13\). But all twelve such types have maximum ordinary
degree at most nine in \(Q(1)\). This is impossible.

### 3.2 The two high-line types

It remains to consider \(R_2=P_4\). In this case the quotient in
(13) is \(W'\mathcal O(2)\), so \(n=\deg N=D-4\geq9\) is odd.
The extension splits, since \(H^1(\mathcal O(n-2))=0\). Injectivity
of \(H^0(E(3))=U\) in \(H^0(I)\) implies

\[
                    W'+T_6\subset\operatorname{Sym}^{n}W.      \tag{14}
\]

Among the eight \(P_4\) types, five have maximum degree at most nine
in \(Q(1)\), one has maximum degree twelve, and two have maximum degree
nineteen. Degrees nine and eleven fail (14). For the last two types,
the only section-compatible degrees from nine through nineteen are
thirteen, seventeen, and nineteen. A line of degree thirteen or seventeen
could map only to the highest \(\mathcal O(19)\) summand, but this
would require an invariant of degree six or two, respectively; neither
exists. Thus necessarily

\[
                    I=\mathcal O(19)\oplus W'\mathcal O(2),   \tag{15}
\]
and the only two formal dual types are

\[
\begin{split}
Q^*&=P_4\mathcal O(-2)\oplus T_6\mathcal O(-3)
             \oplus W\mathcal O(-5)\oplus\mathcal O(-18),\\
Q^*&=P_4\mathcal O(-2)\oplus T_6\mathcal O(-3)
             \oplus\mathcal O(-4)\oplus\mathcal O(-6)
             \oplus\mathcal O(-18).
\end{split}                                                   \tag{16}
\]

The image \(I\) in (15) is saturated in \(Q(1)\). Indeed its projection
to \(P_4\mathcal O(3)\) has the saturated image \(W'\mathcal O(2)\),
the dual of the evaluation surjection in (10). Its kernel
\(\mathcal O(19)\) is the unique highest-degree line of \(Q(1)\).
Saturating \(I\) cannot enlarge either this kernel or the projected
image. It therefore cannot enlarge \(I\).

Consequently (8) is the actual full dual image. Put \(K_d=(Q^*)^-\).
Dualizing the saturated inclusion gives

\[
 Q^*/K_d=S_0(-2)=\mathcal O(-18)\oplus W'\mathcal O(-1),
 \qquad \operatorname{rk}K_d=10,\quad\deg K_d=-34.             \tag{17}
\]

The next dual derivative has the form

\[
 K_d(3)\longrightarrow(Q^*/K_d)(1)
             =\mathcal O(-17)\oplus W'\mathcal O,\qquad
 \ker=(Q^*)^{--}(3).                                         \tag{18}
\]
Riemann--Roch gives \(h^0(K_d(3))\geq\chi(K_d(3))=6\), whereas the
target has only two sections. But dual persistence gives
\(H^0((Q^*)^{--}(3))=0\): the dual plateau has \((k_d,l_d)=(3,2)\),
and stage index \(1+3=4<5\). This contradiction excludes both types (16).

## 4. The zero-quadratic branch

The remaining five types in (9) are exactly the frozen cubic types:

\[
Q^*=T_6\mathcal O(-3)\oplus V\mathcal O(-4)\oplus R,
\]
where

\[
\begin{array}{c|l}
1&R=(1+A)\mathcal O(-6)\\
2&R=W\mathcal O(-5)\oplus W\mathcal O(-7)\\
3&R=W\mathcal O(-5)\oplus\mathcal O(-6)\oplus\mathcal O(-8)\\
4&R=\mathcal O(-4)\oplus\mathcal O(-6)\oplus W\mathcal O(-7)\\
5&R=\mathcal O(-4)\oplus2\mathcal O(-6)\oplus\mathcal O(-8).
\end{array}                                                   \tag{19}
\]

### 4.1 The cubic derivative must vanish

Consider the canonical cubic evaluation bundle
\(G_0=T_6\mathcal O(-3)\subset Q^*\), and its restricted derivative

\[
                    \psi_3:T_6\mathcal O\longrightarrow E^*(1).
                                                               \tag{20}
\]
If this map is nonzero, it is injective on global sections because
\(T_6\) is irreducible. This injectivity is not inferred from cubic
persistence at \((2,3)\).

Rank three is impossible: the globally generated image would lie in
\(S_0(1)\), whose degree is \(12-D<0\). Rank one is also impossible:
the only odd line of degree at most five whose sections contain \(T_6\)
is \(\mathcal O(5)\), and it has no equivariant map to
\(E^*(1)=U\mathcal O(4)\oplus V\mathcal O(5)\).

The exhaustive rank-two Hom calculation leaves
\(J_3=W'\mathcal O(2)\) or \(W'\mathcal O(4)\). Both are saturated
in \(E^*(1)\), since their maximum determinant defects are six and two.
Dualizing gives a quotient of \(I\) equal to \(J_3^*(4)\), namely
\(W'\mathcal O(2)\) or \(W'\mathcal O\).

The kernel line would have degree at least nine or thirteen, respectively.
Every \(Q(1)\) in (19) has maximum degree at most nine. The latter case
is impossible; in the former, the line must be \(\mathcal O(9)\), so
\(I=\mathcal O(9)\oplus W'\mathcal O(2)\). Its sections are
\(S_4+2T_6\), which cannot contain \(U=W'+2T_6\). Thus

\[
                   \psi_3=0,\qquad G_0\subset K_d=(Q^*)^-.     \tag{21}
\]

### 4.2 The next derivative contradicts the primal splitting

Dual persistence again makes the next derivative injective on sections:

\[
 H^0(K_d(3))\hookrightarrow H^0((Q^*/K_d)(1))
                  \hookrightarrow H^0(S_0(-1)).              \tag{22}
\]
The second inclusion uses only that the actual dual image
\(Q^*/K_d\) is a subsheaf of \(S_0(-2)\); no saturation is assumed.
By (21), the source contains \(T_6\). Therefore
\(H^0(S_0(-1))\) contains \(T_6\).

Classify the equivariant rank-three bundle \(S_0\subset E^*\), of
degree \(9-D\leq-4\). Any line summand is \(\mathcal O(e)\) with
even \(e\leq4\). None of the possibilities \(e=0,2,4\) maps
equivariantly to \(U\mathcal O(3)\oplus V\mathcal O(4)\): the relevant
invariants are absent from
\(U\operatorname{Sym}^3W+V\operatorname{Sym}^4W\),
\(UW+VA\), and \(V\). Thus every such line has \(e\leq-2\), and
contributes no sections after twisting by \(-1\).

If \(S_0\) had an irreducible rank-three coefficient block, its degree
would be \(3e<0\), with even \(e\leq-2\), again giving no sections.
The only remaining way to obtain \(T_6\) in (22) is a rank-two coefficient
block. Its odd degree is at most three. Degrees at most one cannot give
\(T_6\) after twisting by \(-1\); \(W\mathcal O(3)\) does not map
equivariantly to \(E^*\); and \(W'\mathcal O(3)\) does map and gives
\(T_6\) in that twist. Consequently

\[
 S_0=W'\mathcal O(3)\oplus\mathcal O(3-D),
 \qquad I=S_0^*(3)=W'\mathcal O\oplus\mathcal O(D).            \tag{23}
\]

But \(D\geq13\), while every ordinary degree of \(Q(1)\) in (19)
is at most nine. The inclusion \(I\subset Q(1)\) is impossible.
This excludes the zero-quadratic branch and completes the exclusion of
\((k,l)=(2,3)\).

## 5. A cubic-pairing lemma for \((k,l)=(3,2)\)

We now record a separate, more limited result for the other adjacent
profile. Put \(R=H^0(E(2))\). The frozen 28-type classification implies
that \(R\) is supported on \(V,P_4,D_5\). It is important that \(R=0\)
is still possible: the exceptional splitting (4) does not force \(l=3\).

The five dual types are (19), so \(H^0(Q^*(3))=T_6\) and all ordinary
degrees of \(Q\) are at most eight. Persistence gives

\[
 H^0(E^-(2))=H^0((Q^*)^-(3))=0.
\]

The restricted derivatives and their pairing are

\[
 \phi:R\mathcal O\to Q,\qquad
 \psi:T_6\mathcal O\to E^*(1),\qquad
 B:R\mathcal O\to T_6\mathcal O(3).                           \tag{24}
\]
Both derivative maps are injective on global sections. If their ranks
are \(a,b\), and \(t=\operatorname{rk}B\), then
\(a+b-3\leq t\leq\min(a,b)\).

Every nonzero image of \(B\) is exactly one of

\[
           V\mathcal O,\quad W'\mathcal O(1),\quad V\mathcal O(2),
                                                               \tag{25}
\]
with section representations \(V,P_4,P_4+D_5\), respectively. This
follows by testing all center-even equivariant blocks of rank at most
three and ordinary degree zero through three, using both source and
target Hom spaces. A line block is impossible. The possible saturation
defects are at most nine, four, and three, so the images are saturated.

We also use two elementary character bounds. A center-even line of
degree at most eight has at most one copy of each of \(V,P_4,D_5\) in
its sections. A globally generated center-even rank-two bundle with all
degrees at most eight has at most two \(P_4\) copies. If its coefficient
representation is irreducible of dimension two, it has at most one
\(D_5\) copy. These are the finite lists
\(\operatorname{Sym}^{e}W\), even \(e=0,2,4,6,8\), and
\(W\operatorname{Sym}^{e}W,W'\operatorname{Sym}^{e}W\), odd
\(e=1,3,5,7\).

## 6. Excluding the type with \(R=2V\)

The corresponding formal splitting is

\[
       E=2V\mathcal O(-2)\oplus W'\mathcal O(-3)
                           \oplus3V\mathcal O(-4).             \tag{26}
\]

The line-section bound gives \(a\geq2\). Also \(b\geq2\): a rank-one
image of \(\psi\) would have to be \(\mathcal O(5)\), but there is
no equivariant map from that line to
\(2V\mathcal O(3)\oplus W'\mathcal O(4)\oplus3V\mathcal O(5)\).
Hence \(B\ne0\). List (25) leaves only \(V\mathcal O\), so
\(t=a=3\). The saturated kernels of \(B\) and \(\phi\) then coincide,
but the global kernel of \(B\) contains \(V\). This contradicts
injectivity of \(\phi\) on sections.

## 7. Excluding the type with \(R=3P_4\)

Here the formal splitting is

\[
       E=3P_4\mathcal O(-2)\oplus2W'\mathcal O(-5)
                              \oplus\mathcal O(-10).          \tag{27}
\]

The rank-two character bound forces \(a=3\). Since \(b\geq1\),
\(B\ne0\). Either rank-three possibility in (25) has too few sections
to receive \(3P_4\) injectively. Equality of the generic kernels of
\(B\) and \(\phi\) would again contradict section injectivity.

Thus the only remaining image is \(W'\mathcal O(1)\). Its global
kernel is \(2P_4\), whose \(\phi\)-image has rank one. A line in
\(Q\) has degree at most eight and cannot contain two \(P_4\) copies
in its sections. This is again a contradiction.

Thus at most 26 of the original 28 formal primal types remain for
\((3,2)\); this is not a classification of the realizable types.

## 8. A further restriction when \(R\) contains two \(D_5\) copies

For the three formal types with
\(R=2D_5\) or \(R=P_4+2D_5\), necessarily

\[
 B=0,\qquad(a,b)=(2,1),\qquad
 \operatorname{im}\phi=\mathcal O(4)\oplus\mathcal O(8),
                                                               \tag{28}
\]
and \(Q^*\) must be type 3 or type 5 in (19).

A rank-three image in (25) has at most one \(D_5\) in its sections,
so equality of kernels would contradict injectivity. A rank-two image
would leave \(2D_5\) in the global kernel, mapping under \(\phi\) into
a line, which is also impossible. Thus \(B=0\). The section bounds and
rank inequality force \(a=2,b=1\).

The rank-two image of \(\phi\) cannot have an irreducible rank-two
coefficient block, since such a block supplies at most one \(D_5\).
It must split into two lines, each of degree four or eight. Put
\(L=\ker(Q\to T_6\mathcal O(3))\). Since \(B=0\), both line
summands map into \(L\). For the five types (19), exact character
arithmetic gives

\[
 \dim\operatorname{Hom}_G(\mathcal O(4),L)=1,
 \qquad
 \dim\operatorname{Hom}_G(\mathcal O(8),L)=(0,0,1,0,1).
                                                               \tag{29}
\]
Two copies of the same line cannot inject when its Hom space has
dimension one. Thus only degrees four and eight, and only dual types
3 and 5, remain. This is a necessary restriction, not a realization.

## Verification

Run `python3 verify_adjacent_rank_three_gauss.py` in this directory.
It checks exact characters, all 37 formal dual splittings, both small-image
lists, the line-degree filters, the final numerical contradictions, and
the two primal exclusions and conditional restriction. The geometric
arguments are those above; the script does not evaluate an actual map
or substitute finite arithmetic for a proof about differentiation.
