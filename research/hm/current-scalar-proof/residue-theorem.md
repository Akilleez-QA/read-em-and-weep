# A corrected local-duality representative

## 1. Setup and regularity hypotheses

On `Y=(P^1)^4` write coordinates `(X_i:Y_i)` and `x_i=X_i/Y_i`.
Define `v_j` by

\[
\prod_{i=1}^4(Y_i+X_i z)=\sum_{j=0}^4v_jz^j,
\qquad h_j=v_j^5-v_0v_1v_2v_3v_4.
\]

Let `U_0=D(v_0)` and `U_j=D(h_j)` for `1<=j<=4`.
For each primary carrier refine by the legal opens

\[
W_{i0}=D(Y_i),\qquad W_{i1}=D(X_i(X_i^2-Y_i^2)).
\]

A vertex `(j,m)` has `m in {0,1}^4` and open
`U_j intersect product_i W_i,m_i`. There is one unrefined vertex over
`U_0`. Write `r` for the carrier map. Let `c` be the closed alternating
`F=O(-4,-4,-4,-4)`-valued degree-four scalar cochain of the preceding note.

Assume the completed scalar and its restrictions have primary pole bound
13, first-open pole bound 1, legal-0 pole bound 1 along `Y_i=0`, and
finite legal-1 pole bounds 1 along both `x_i=0` and `x_i^2-1=0`.
The allocation must hold for the fixed-cochain projection and prism below.
The application to the geometric source uses separately certified bounds;
this theorem does not infer them from polynomial degrees.

## 2. One fixed legal-line partition

For a polynomial of degree five in `(X_i,Y_i)`, define

\[
T_{i1}P=X_i^3(X_i^2-Y_i^2)P|_{X_i=1,Y_i=0},\qquad
T_{i0}P=P-T_{i1}P.
\]

The first expression is divisible by `X_i^3(X_i^2-Y_i^2)` and the second
by `Y_i`. Operators in different coordinates commute. Set

\[
P_{j,m}=\left(\prod_i T_{i,m_i}\right)h_j,\qquad
\rho_{j,m}=P_{j,m}/h_j.
\]

These are regular functions on `U_j`, sum to one, and have sufficient
vanishing along the respective complements to clear the stated legal
poles. They are chosen once on `U_j` and then restricted; independently
choosing weights on each target intersection would not give the chain
identities below. Set `rho_0=1`.

On the finite chart,
`T_i1 P=(x_i^5-x_i^3)[x_i^5]P` and `T_i0=Id-T_i1`.
These identities, the sum of the weights, and their divisibility can be
checked coefficientwise. A zero weight may be omitted, but a nonzero
mask term may not be dropped merely because it is inconvenient.

## 3. Weighted projection and ordered prism

Use the Čech differential

\[
(\delta c)_{a_0\ldots a_{q+1}}
 =\sum_{k=0}^{q+1}(-1)^k c_{a_0\ldots\widehat a_k\ldots a_{q+1}}.
\]

Define

\[
(Pc)_{j_0\ldots j_q}
 =\sum_{r(b_i)=j_i}\left(\prod_{i=0}^q\rho_{b_i}\right)c_{b_0\ldots b_q}.
\tag{1}
\]

The weights clear the inserted vertices' legal poles. Summing over an
omitted vertex gives `P delta=delta P` and `P r*=Id`.
The projection is alternating even on repeated carrier tuples: swap the
two independent summation indices to negate the summand; terms with an
identical repeated vertex already vanish. No factorial is divided out.

For `q>=1`, define the following on **increasing target tuples**, and
extend its output alternatingly:

\[
(Hc)_{a_0\ldots a_{q-1}}
 =\sum_{k=0}^{q-1}(-1)^k
   \sum_{r(b_i)=r(a_i),\,i\le k}
   \left(\prod_{i=0}^k\rho_{b_i}\right)
   c_{b_0\ldots b_k a_k\ldots a_{q-1}}.
\tag{2}
\]

Set `H=0` on degree zero. Then

\[
\delta H+H\delta=\mathrm{Id}-r^*P. \tag{3}
\]

To prove this, expand on an increasing tuple. Terms deleting a vertex
away from the pivot cancel between consecutive prism terms. Deleting a
chosen vertex uses `sum rho=1`. The two endpoint terms are `c` and
`-r*Pc`. Every face remains increasing, so the same identity holds after
alternating extension. Applying the raw expression (2) to arbitrary
unsorted target tuples would not define the required alternating cochain.
Repeated carriers must remain in the prism sum.

## 4. Relative lift and all-mask formula

Let `V=U_1 union ... union U_4=Y\Z`, with `Z=V(h_1,...,h_4)`.
The coarse cover of `V` has only four vertices, hence zero alternating
Čech group in degree four. From (3), `b=(Hc)|_V` satisfies `delta b=c|_V`.
This produces the relative class `(c,b)` and a genuine local-cohomology
lift represented on `U_0` by

\[
f=(Pc)_{01234}
 =\sum_{m_1,\ldots,m_4}\rho_{1,m_1}\cdots\rho_{4,m_4}
   c_{0,1m_1,2m_2,3m_3,4m_4}. \tag{4}
\]

In the scalar prefix, the first primary anchor is line-mask independent;
its sum is one. Thus (4) reduces to the full three-mask sum over carriers
`2,3,4`. For an unsigned row residual `M`, its scalar entry is

\[
c_{0,1,2m_2,3m_3,4m_4}
 =-\big[E_1(I_2M_{2m_2,3m_3,4m_4}^tP_2)H_{1,1}\big]_{10,0}
\quad(v_0=1). \tag{5}
\]

All terms use the same original finite frame and the same alternating
residual. The original minus is retained once. The legal denominators
are cleared; the three remaining weights each add one primary factor.
A sufficient denominator is

\[
f=\frac{A}{h_1^{13}h_2^{14}h_3^{14}h_4^{14}}. \tag{6}
\]

The simple first-open pole implies that
`v_0 product_j h_j^n_j f` is a global section of
`F tensor O(1+5 sum n_j,...,1+5 sum n_j)`.
For `n=(13,14,14,14)`, `sum n_j=55`, so the finite numerator satisfies

\[
\deg_{x_i}A\le 272. \tag{7}
\]

A syntactic circuit degree of 273 does not contradict (7), but the
source identification and global regularity must justify cancellation
of that layer before it is discarded.

The single all-zero-mask value is generally insufficient. Already on
`P^1` with `F=O(-2)`, refine `D(X)` into `D(XY)` and
`D(X(X^2-Y^2))`. The cocycle values
`c_(0,a)=0`, `c_(0,b)=1/x`, `c_(a,b)=1/x`, with weights
`rho_a=x^-2`, `rho_b=1-x^-2`, give coarse value `x^-1-x^-3` and residue 1.
The raw all-zero-mask value is zero. The prism supplies the missing class.

## 5. Residue normalization and duality

The local class represented by (4) lies in

\[
H_Z^4(U_0,F)=
R_{h_1h_2h_3h_4}/\sum_j R_{\prod_{i\ne j}h_i},
\quad R=k[x_1,x_2,x_3,x_4],
\]

using the finite frame. Its image in `H^4(Y,F)` is `[c]` by the relative
construction above. Serre duality pairs with `x^m dx_1...dx_4` times the
inverse frame, for `0<=m_i<=2`. With ordered denominator sequence
`(h_1,h_2,h_3,h_4)`,

\[
\lambda_m([c])=\sum_{z\in Z}\operatorname{Res}_z(x^m f\,dx_1\cdots dx_4).
\tag{8}
\]

Residue-field traces are implicit when points are not rational. The
normalization is `Res dx/(x_1x_2x_3x_4)=1`; (8) therefore agrees with
Laurent coefficient extraction at exponent `(-m_1-1,...,-m_4-1)`.
The four-dimensional product/ordered-Čech sign is `(-1)^6=+1`.
The theorem follows by multiplying the local-to-global map by the dual
section and applying the proper Serre trace, whose trace with support is
the sum of local residues. This is a residue of the entire generalized
fraction in (6), including all denominator powers.

## 6. Why nonreduced points cannot be omitted

In elementary-symmetric coordinates `a_j=e_j(x)`, set `p=a_1a_2a_3a_4`.
The support equations are `g_j=a_j^5-p=0`. At a geometric point, either
all `a_j=0`, or all are nonzero. In the latter case multiplying the four
equations gives `p^5=p^4`, hence `p=1`; the four entries are fifth roots
of unity with product one. For characteristic zero or a prime greater
than 5 there are 125 such points. The matrix determinant lemma gives
Jacobian determinant 125 at each, so these are simple.

The leading terms `a_j^5` are pairwise coprime. They form a monic
Gröbner basis for a degree-compatible order, giving quotient length
`5^4=625`. The origin therefore has length 500. The elementary-symmetric
map has finite flat degree 24, giving total pullback length 15,000 and
length 12,000 at its sole point over the origin. Denominator powers in
(6) further thicken the support. A simple-root Jacobian sum that omits
the origin is not (8).

For an unpowered numerator `Q`, finite-flat differential trace gives

\[
\operatorname{Res}_x\frac{Q\,dx}{\prod h_j}
 =\operatorname{Res}_a\frac{S\,da}{\prod g_j},\qquad
S(e(x))=\frac{\operatorname{Alt}(Q)}{\Delta_4},
\]

where `Delta_4=det(de_j/dx_i)=product_(i<j)(x_i-x_j)` and `Alt` is the
signed sum over all permutations. The quotient is polynomial; no inverse
Jacobian is taken at a ramified point, and there is no extra factor 24.
The right-hand residue is the coefficient of `a_1^4a_2^4a_3^4a_4^4` in
the normal form modulo `g`. Indeed the standard monomials have exponents
at most four; the leading-system residue vanishes below total degree 16
and gives one on this unique degree-16 basis monomial. Equivalently,
expanding the monic equations formally gives coefficient conditions
`u_i+K-5k_i=4`, `K=sum k_i`; for `0<=u_i<=4` these force `K=0` and
`u_i=4` for every `i`.

## 7. An immediate structural consequence

Because `v_0 f` has no first-open pole, it extends to the intersection
`U_1 intersect ... intersect U_4`. As the sole degree-three coarse
component there, its coboundary is `v_0 f`. Thus

\[
v_0[c]=0\quad\text{in }H^4(Y,F(1,1,1,1)).
\]

The dual multiplication map shows that all 16 pairings with every
`m_i<=1` vanish. This is a geometric consequence of a simple first-open
pole. The further 19 single-coordinate zeros in the finite-model
relations have a separate differential certificate.
