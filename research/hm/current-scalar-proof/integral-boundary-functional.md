# A characteristic-independent integer boundary functional

## 1. Hypotheses

Use the representative, coordinates, and orientation of the residue theorem.
Let

\[
f=A/(h_1^{13}h_2^{14}h_3^{14}h_4^{14}),\qquad
\deg_{x_i}A\le272. \tag{H0}
\]

For each relevant boundary coordinate `i`, write `A_i=[x_i^272]A` and
assume the additional source bounds

\[
A_i\text{ is divisible by }\prod_{j\ne i}x_j^{48},\qquad
\deg_{x_j}A_i\le212\quad(j\ne i). \tag{H1}
\]

These are hypotheses about the exact source in the coefficient ring being
used. A support statement modulo one prime cannot establish them over
`Q` or another prime. The actual rational source has separate certificates
for all four boundary coordinates. This note proves the universal
functional under (H0) and (H1), not those source certificates.

For `m in {0,1,2}^4`, set `S=sum_i m_i`. Write `i` active when `m_i=2`.

## 2. Boundary reciprocity, before Cartier

At `x_i=1/t_i`, the denominator has coordinate degree 275 and the
largest numerator degree in `x_i` is `272+m_i`. Including
`dx_i=-dt_i/t_i^2` leaves lowest order `t_i^(1-m_i)`. Thus infinity poles
occur only at active coordinates and are simple.

Group the active infinity divisors with the first denominator group
`h_1`, keeping `h_2,h_3,h_4` as the other ordered groups. There is no
common point of the latter three groups at a corner with two or more
infinite coordinates: at a point with exactly `r>=2` infinite factors,
`v_r` is nonzero and `h_r=v_r^5`, while `r` is among `2,3,4`.
The four `h_j` likewise have no common zero at infinity.

On the individual divisor `x_i=infinity`, the remaining variables `z`
in their original increasing order satisfy

\[
h_1=1,\qquad h_2=e_1(z)^5,\quad h_3=e_2(z)^5,\quad h_4=e_3(z)^5.
\]

Their common zero is `z=0`, with its full scheme structure. Put
`q=e_1e_2e_3`. The substitution minus sign cancels the minus from global
reciprocity, and moving `dt_i` to the first position gives `(-1)^(i-1)`:

\[
\lambda_m=
\sum_{i:m_i=2}(-1)^{i-1}
 \operatorname{Res}_{z=0}
 \frac{z^{m_{\widehat i}}A_i(z)\,dz}{e_1(z)^{70}e_2(z)^{70}e_3(z)^{70}}.
\tag{1}
\]

The ordered denominator sequence is `(e_1^70,e_2^70,e_3^70)`.
Its homogeneous degrees are 70, 140, 210. Only numerator degree 417
contributes, so the exact source filter is

\[
\operatorname{Hom}_{419-S}(A_i)
 =[x_i^{272}]\operatorname{Hom}_{691-S}(A). \tag{2}
\]

This is a filter, not a claim that the source is homogeneous.

## 3. A prime-field derivation

Temporarily work over `F_p`, `p>5`, and choose a power `P=p^k>=71`.
Let `C_P` be the `k`-fold Cartier operator on top forms. It selects
exponents congruent to `P-1`, subtracts that vector, and divides by `P`.
Over the prime field coefficients are unchanged. The semilinearity
`C_P(Q^P omega)=Q C_P(omega)` and compatibility with the residue give

\[
\operatorname{Res}\frac{z^{m_{\widehat i}}A_i\,dz}{q^{70}}
 =\operatorname{Res}\frac{R_i\,dz}{q},\qquad
R_i=C_P(z^{m_{\widehat i}}A_iq^{P-70}). \tag{3}
\]

This includes the nonreduced support. Over a general perfect field the
coefficients and residue instead acquire their inverse Frobenius; the
prime-field statement must not be copied unchanged to that setting.

Even (H0) gives coordinate degree at most 2 for `R_i`, because before
Cartier it is at most `272+2+3(P-70)=3P+64` and
`floor((2P+65)/P)=2`. Finite-map trace through the elementary-symmetric
map in three variables then makes the residue the signed sum of the six
coefficients with exponent permutations of `(2,1,0)`. There is no factor
six. Index a summand by a permutation `(i,j,k,l)` of `(1,2,3,4)`, with
`m_i=2`; put `(u,a,b)=(x_j,x_k,x_l)`. Its full sign is
`sgn(i,j,k,l)`, and its coefficient is

\[
[u^{3P-1-m_j}a^{2P-1-m_k}b^{P-1-m_l}]A_i(u,a,b)q^{P-70}.
\tag{4}
\]

## 4. The bounded source window

Put `C_i=A_i/(uab)^48`, `d=3+m_j`, and `L=21-m_l`.
For `0<=r<=d`, define the homogeneous binary polynomial

\[
B_{m,e,r}=\operatorname{Hom}_{111-S+r}([u^{164-r}]C_i),
\quad e=(i,j,k,l). \tag{5}
\]

Writing `s=a+b`, `p_0=ab` gives

\[
q=p_0[su^3+(s^2+p_0)u^2+sp_0u].
\]

The largest possible pivot degree in (4) is `212+3(P-70)=3P+2`, so
only source deficits `r=0,...,d` contribute. If `N=P-70`, set

\[
E_{N,t}(1,z)=[T^t]G(T,z)^N,\quad
G(T,z)=1+z+(1+3z+z^2)T+z(1+z)T^2.
\tag{6}
\]

Removing the factor `(ab)^(48+N)` leaves target degrees
`(P+21-m_k,21-m_l)`. When `r+t=d`, the binary product has exactly
the sum of these target degrees. Therefore the contribution is

\[
[z^L]\sum_{r=0}^{d}B_{m,e,r}(1,z)E_{N,d-r}(1,z). \tag{7}
\]

Setting `a=1` is legitimate only after the homogeneous filter (5).
Doing so beforehand would mix distinct total degrees.

## 5. Six fixed integer kernels

Work in the finite ring `Z[T,z]/(T^6,z^22)`. Since `G` has constant
term one, define

\[
K_t(z)=[T^t]G(T,z)^{-70}\pmod{z^{22}},\qquad 0\le t\le5.
\tag{8}
\]

They contain 132 integer coefficients. An explicit formula is

\[
K_t=(1+z)^{-70-t}
 \sum_{v=0}^{\lfloor t/2\rfloor}
 \binom{-70}{t-v}\binom{t-v}{v}
 z^v(1+z)^{2v}(1+3z+z^2)^{t-2v}\pmod{z^{22}}. \tag{9}
\]

The coefficient rows in increasing `v` are

```text
0: 1
1: -70
2: 2485, -70
3: -59640, 4970
4: 1088430, -178920, 2485
5: -16108764, 4353720, -178920
```

In the finite quotient over `F_p`, Frobenius gives `G^P=1`, since
`P>5` and `P>21`. Thus `G^(P-70)=G^-70` there, and the kernels in (7)
are reductions of the same six integer polynomials for every allowed
prime. It follows that

\[
\boxed{\lambda_m=
\sum_{e=(i,j,k,l):m_i=2}\operatorname{sgn}(e)
 \sum_{r=0}^{3+m_j}\sum_{\ell=0}^{21-m_l}
 b_{m,e,r,\ell}[z^{21-m_l-\ell}]K_{3+m_j-r}(z)}
\tag{10}
\]

where

\[
b_{m,e,r,\ell}
 =[x_i^{272}x_j^{212-r}x_k^{159-S+r-\ell}x_l^{48+\ell}]A.
\tag{11}
\]

Each source exponent tuple has total degree `691-S`, agreeing with (2).
If no `m_i` equals 2, the sum is empty and gives the sixteen geometric
annihilator coordinates. Different active coordinates all contribute;
there is no assumption that the source is permutation symmetric.

## 6. The integral and rational proof

For any integral polynomial `H(z)`, the exact finite-map trace under
`z -> (e_1,e_2,e_3)` gives

\[
\operatorname{Res}_0\frac{H(z)\,dz}{e_1^{70}e_2^{70}e_3^{70}}
 =[a_1^{69}a_2^{69}a_3^{69}]S_H(a),\quad
S_H(e(z))=\operatorname{Alt}(H)/\Delta_3.
\tag{12}
\]

Division by the Vandermonde is exact over the integers; its quotient is
symmetric with an integral elementary-symmetric expression. Equation
(12) is consequently an integer linear functional. Its normalization is
`Res z_1^2 z_2 dz/(e_1e_2e_3)=1`, with no division by six.

Under (H1), the right side of (10) is also an integer linear functional
on the allowed source polynomials. Sections 3–5 show that the two
functionals agree modulo every prime greater than 5. On each integral
source, their difference is an integer divisible by infinitely many
primes, hence zero. The identity therefore holds over `Z`; linearity
and localization give it over `Q` and any localization of `Z`.
Combined with (1), this proves the rational formula without inventing a
Cartier operator in characteristic zero.

This is an equality of universal functionals, proved at all allowed
primes. It is not an inference from a single modular zero to a rational
zero. Exact rational extraction must use all integer kernel coefficients.

## 7. Useful specialization and implementation boundary

Modulo 71 the six kernels become

```text
K0=1+z; K1=1+3z+z^2; K2=z+z^2; K3=K4=K5=0.
```

The corresponding edge uses seven source entries, with weights
`1,1,1,3,1,1,1`. Those sparse prime-field kernels are not rational kernels.

If a certified source also has `deg A_i<=449`, then `C_i` has coordinate
bounds 164 and total bound 305, so its reversal

\[
F_e(v,w,z)=v^{164}w^{305}C_i(1/(vw),1/w,z/w)
\]

is polynomial and
`b_(m,e,r,ell)=[v^r w^(30+S) z^ell]F_e`.
All 81 targets fit in quotient lengths `(6,39,22)`. The 46 targets outside the 35 forced-zero positions have `3<=S<=6`, so lengths `(6,37,22)`
suffice for them. The reversal must preserve grading and nonnegative
shifts. An enlarged quotient cannot recover coefficients discarded by an
earlier smaller evaluation. These are source-representation requirements,
not conclusions from the functional alone.
