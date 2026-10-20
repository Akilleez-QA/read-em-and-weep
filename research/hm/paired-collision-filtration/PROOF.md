# Exact collision filtration in the full paired character

## Result and scope

Work over \(\mathbf C\). Let
\[
 Z=(\mathbf P^1)^4,\qquad Y=\operatorname{Sym}^4(\mathbf P^1)=\mathbf P^4,
 \qquad q:Z\longrightarrow Y,
\]
and give \(A=q^*\mathcal O_Y(1)\) its ordinary, ungraded permutation
linearization. Let \(I=I_D\) be the **ordinary** ideal of the reduced union
of the four triple diagonals. Put
\[
 H=\langle(12),(34),(13)(24)\rangle,\qquad \chi=\operatorname{sgn}|_H.
\]
Fix the binary determinant and weight lines as in the cited coefficient
proofs. Choose the pairing weights with the normalization of PR158, and write
\[
 \sigma=\sigma_1,\quad d=\sigma_2-\sigma_3,\quad
 u=t_2=2\sum_i\sigma_i^2,\quad v=t_3=2\sum_i\sigma_i^3,\quad
 \tau=\sigma^2-u/6.
\]
The sections \(u,v\) descend to \(Y\), with degrees two and three.
For every integer \(n\), set
\[
 K_n=
 \begin{cases}
 \mathcal O_Y,&n\leq0,\\
 (u^a v^b: a,b\geq0,\ 2a+3b\geq n),&n>0.
 \end{cases}
\]
For any locally free \(B_0\) on \(Y\), put \(E=q^*B_0\otimes A^{-2}\).

The cubic basis and multiplication by \(d\) identify the following
**filtered subsheaves**, for every \(k\geq0\):
\[
 (q_*(I^kE))_\chi
 \cong
 B_0(-3)K_{k-1}\ \oplus\
 B_0(-4)K_{k-2}\ \oplus\
 B_0(-5)K_{k-3}.                                      \tag{1}
\]
The maps to unrestricted coefficients are the usual three ideal
inclusions in this same basis. Consequently
\[
\begin{split}
 (q_*(E/I^kE))_\chi\cong&
 B_0(-3)/B_0(-3)K_{k-1}\\
 &\oplus B_0(-4)/B_0(-4)K_{k-2}\\
 &\oplus B_0(-5)/B_0(-5)K_{k-3}.                       \tag{2}
\end{split}
\]
These identities include every quadruple collision and every
partial-infinity chart. They are not generic-order calculations.

For the normalized HM coefficient \(B_0=\operatorname{End}_0(F)\), the
positive-twist vanishings of PR167 imply
\[
 H^2(Z,I^kE)_\chi=0\qquad(k\geq7).                    \tag{3}
\]
This is zero of the **entire ideal-coefficient group**, not only zero of
its image on an admitted paired subspace. It gives no new numerical
sufficient order or optimality claim. It constructs neither a primitive
nor an order-seven representative for an actual source.

## 1. Exact imports and difference from prior results

PR158 proves that \(I\) is the global reduced regular-sequence ideal
generated locally by
\[
 x=\sigma_1-\sigma_2,\qquad y=\sigma_1-\sigma_3,
\]
that \(\sum_i\sigma_i=0\), and that its image is the reduced
complete-intersection surface \(N=V(u,v)\). Its all-powers proof gives
\[
 \operatorname{gr}_K\mathcal O_Y=\mathcal O_N[U,V],
 \qquad \deg U=2,\quad\deg V=3,                       \tag{4}
\]
locally in a descended line frame. The corresponding global formula
retains the line twists. That proof already establishes the full
\(S_4\)-sign contraction
\((q_*I^k)_{\rm sign}=\mathcal O_Y(-3)K_{k-3}\) for \(k\geq3\), and the
ordinary-power Vandermonde colon identities. These are not new claims
of the present note.

PR139 supplies the global basis \(1,\sigma,\tau\) of the block-even
cubic algebra
\[
 \mathcal C=(m_*\mathcal O_{\mathbf P^2\times\mathbf P^2})^+
 =\mathcal O_Y\oplus\mathcal O_Y(-1)\sigma
                    \oplus\mathcal O_Y(-2)\tau,
\]
with presentation
\[
 \sigma^3-(u/4)\sigma-v/6=0.                         \tag{5}
\]
Here notation such as \(\mathcal O(-1)\sigma\) denotes the image of
the corresponding line under multiplication by the weight section.
The basis remains a basis at ramification; it does not arise by
inverting the function-trace pairing.

PR387 identifies \(\mathbf P^2\times\mathbf P^2=Z/K\), where
\(K=\langle(12),(34)\rangle\). The block swap is induced by
\((13)(24)\). It follows that
\[
 \mathcal C=(q_*\mathcal O_Z)^H.                     \tag{6}
\]
Only this coefficient identification, not an actual-source comparison,
is needed for the filtration calculation.

PR167 proves \(H^2(B_0(t))=0\) for \(t\geq2\) and \(H^1(B_0(t))=0\)
for \(t\geq7\), and uses PR158's adjacent-monomial resolutions. Its
finite-neighborhood argument retains a distinction between its
transported paired subspace and the full \(H\)-character sector.
The added result here is the exact filtration of the **whole**
character coefficient and its whole ideal-coefficient vanishing,
not another proof of the earlier full-sign contraction.

No action of binary-coordinate changes on \(B_0\) is assumed. The
ordinary \(H\) action is the action on the ordered roots with the
pulled-back coefficient fixed.

## 2. Two-divisor alternant and exact order shift

On common finite-root coordinates, the specified weight differences give
\[
 d=\sigma_2-\sigma_3=3(x_1-x_2)(x_4-x_3),            \tag{7}
\]
up to the fixed bracket orientation. Homogeneously \(d\) is a section
of \(A\) with divisor \(\Delta_{12}+\Delta_{34}\), both multiplicities
one. Its \(H\)-character is \(\chi\): the two inner swaps interchange
\(\sigma_2,\sigma_3\), while the block swap fixes them.

On a quotient-adapted open, an \(H\)-\(\chi\) section of a coefficient
pulled back from \(Y\), tensored by any power of \(A\), vanishes on
\(\Delta_{12}\) and \(\Delta_{34}\). Each corresponding transposition
fixes that diagonal pointwise and acts trivially on the coefficient
there, whereas \(\chi=-1\). In a local bundle frame on the smooth
variety \(Z\), these two distinct prime Cartier divisors therefore
jointly divide the section. Division by \(d\) is regular and carries
the \(A^{-1}\) twist. The quotient is \(H\)-invariant. Conversely,
multiplying an invariant section by \(d\) gives a \(\chi\) section.
This is regular divisor division, not a meromorphic inversion.

Locally \(d=y-x\). Since \(I=(x,y)\) is a regular-sequence ideal,
\[
 \operatorname{gr}_I\mathcal O_Z=\mathcal O_D[X,Y].
\]
The initial form \(Y-X\) is a nonzerodivisor over every coefficient
ring, since it is monic in \(Y\). Hence
\[
 (I^k:d)=I^{k-1}\qquad(k\geq1).                    \tag{8}
\]
Indeed, for \(k\geq2\), if \(f\notin I^{k-1}\), choose the largest
\(r<k-1\) such that \(f\in I^r\). Its nonzero initial class multiplied
by \(Y-X\) remains nonzero in degree \(r+1\), so
\(df\notin I^{r+2}\), and therefore \(df\notin I^k\).
The reverse inclusion is immediate. For \(k=1\), (8) is simply
\((I:d)=\mathcal O_Z\). Outside \(D\) all ideal powers are the unit
ideal. Changes of line frame multiply the expressions by units,
so the formula glues.

In particular, this calculation works at the quadruple locus. It
does not use generic smoothness of an individual triple diagonal.
It gives, for \(k\geq1\),
\[
 (q_*I^k)_\chi
 =d\cdot\bigl((q_*I^{k-1})^H\otimes\mathcal O_Y(-1)\bigr).       \tag{9}
\]
Here \(d\) denotes the multiplication map on the indicated twisted
domain. For \(k=0\), unrestricted alternant division gives the same
formula with \(I^0\) on the right.

## 3. Filter the whole cubic algebra

Inside \(\mathcal C\), define
\[
 F_n=K_n\cdot1\ \oplus\ \sigma K_{n-1}\
                     \oplus\ \tau K_{n-2},\qquad n\geq0,       \tag{10}
\]
where the second and third summands include their
\(\mathcal O_Y(-1)\) and \(\mathcal O_Y(-2)\) line factors.
The sum is direct because \(1,\sigma,\tau\) is the global cubic
basis. The filtration is independent of local line frames: the
weights of \(u,v,\sigma,\tau\) are \(2,3,1,2\).

The linear expressions for the \(\sigma_i\) show that
\(\sigma_i\in IA\), \(u\in I^2A^2\), and \(v\in I^3A^3\).
Thus
\[
 F_n\subseteq(q_*I^n)^H.                            \tag{11}
\]
We prove the reverse inclusion without omitting quadruple collisions.
Replacing \(\tau\) by \(\sigma^2\) preserves every \(F_n\):
\(\tau=\sigma^2-u/6\), and \(uK_{n-2}\subset K_n\).

On an \(\mathcal O_Y(1)\)-trivializing affine open, (4) and the
shifted free cubic basis identify the associated graded as
\[
 \operatorname{gr}_F\mathcal C
 =
 \mathcal O_N[U,V,T]/(T^3-UT/4-V/6),\qquad \deg T=1.             \tag{12}
\]
This is both a module and algebra identity: it is free over
\(\mathcal O_N[U,V]\) on \(1,T,T^2\), and its multiplication relation
is the homogeneous relation (5).

The induced map into the upstairs associated graded sends
\[
\begin{gathered}
 T\longmapsto s_1=(X+Y)/3,\quad
 U\longmapsto q_2=2(s_1^2+s_2^2+s_3^2),\\
 V\longmapsto q_3=2(s_1^3+s_2^3+s_3^3),\\
 s_2=(Y-2X)/3,\qquad s_3=(X-2Y)/3.
\end{gathered}
\]
This scalar substitution is injective over **any** \(\mathbf C\)-algebra.
For a direct proof, put
\[
 S=s_1,\qquad D=s_2-s_3=Y-X.
\]
This is an invertible linear change from \(X,Y\), and
\[
 q_2=3S^2+D^2,\qquad q_3=6S^3-\tfrac32q_2S.          \tag{13}
\]
The scalar algebra in (12) eliminates \(V\) and is simply
\(\mathbf C[U,T]\). After the invertible change \(U'=U-3T^2\),
the substitution is \(T\mapsto S,\ U'\mapsto D^2\).
The distinct monomials \(S^aD^{2b}\) are linearly independent over
every coefficient ring. No domain or smoothness assumption on
\(N\) is involved.

The coefficient map \(\mathcal O_N\to q_*\mathcal O_D\) is injective
because \(N\) is the reduced scheme-theoretic image of reduced \(D\),
as proved in PR158. Tensoring this injection over \(\mathbf C\)
with the polynomial vector space preserves injectivity. Composing
with (13) proves
\[
 \operatorname{gr}_F\mathcal C
       \longrightarrow q_*(\operatorname{gr}_I\mathcal O_Z)
 \quad\hbox{is injective}.                          \tag{14}
\]
The local descriptions glue with the stated line weights. This
argument explicitly retains the nonnormal image and the quadruple
root locus.

Suppose a local section \(f\in\mathcal C\) does not belong to \(F_n\).
Since \(F_0=\mathcal C\), a largest \(r<n\) satisfies
\(f\in F_r\) but \(f\notin F_{r+1}\). Its nonzero initial class
maps injectively by (14) to degree \(r\) upstairs. Thus its pullback
does not belong to \(I^{r+1}\), and hence does not belong to \(I^n\).
Together with (11), this proves
\[
 (q_*I^n)^H=F_n\qquad(n\geq0).                       \tag{15}
\]
Only a finite leading-order argument was used, not completion or
an infinite coefficient-correction process.

## 4. Exact paired-character coefficients and quotients

Combining (9) and (15), then tensoring by \(B_0(-2)\), proves (1).
The three generators \(d,d\sigma,d\tau\) have \(A\)-degrees
one, two, three, respectively. For \(k=0\), the convention
\(K_j=\mathcal O_Y\) for \(j\leq0\) gives the unrestricted result.
The construction identifies the actual inclusions, not only
abstract bundle types.

Finite pushforward and the characteristic-zero \(H\)-character
projector are exact. Applying them to
\(0\to I^kE\to E\to E/I^kE\to0\) therefore proves (2).

Equivalently, write a regular \(\chi\) cochain uniquely as
\[
 R=d(a_0+\sigma a_1+\tau a_2).
\]
The coefficients have types \(B_0(-3),B_0(-4),B_0(-5)\).
Then \(R\in I^kE\) if and only if they belong, respectively, to
\[
 B_0(-3)K_{k-1},\qquad B_0(-4)K_{k-2},\qquad B_0(-5)K_{k-3}.
\]
The decomposition is a regular sheaf map and commutes with the
Čech differential. These are cubic-basis coefficients. No numerical
identification with separately normalized weighted duality traces
is asserted.

## 5. Entire order-seven ideal-coefficient vanishing

For \(n>0\), PR158 supplies the adjacent-monomial resolution
\[
 0\longrightarrow\bigoplus_i\mathcal O_Y(-e_i)
 \longrightarrow\bigoplus_i\mathcal O_Y(-d_i)
 \longrightarrow K_n\longrightarrow0.
\]
If the minimal generators are \(u^{a_i}v^{b_i}\), ordered with
strictly increasing \(b_i\), then
\[
 d_i=2a_i+3b_i\geq n,\qquad
 e_i=2a_i+3b_{i+1}=d_i+3(b_{i+1}-b_i)\geq n+3.       \tag{16}
\]
This gives the needed stronger syzygy estimate explicitly.

Tensor by \(B_0(-a)\), \(a=3,4,5\). The groups controlling
\(H^2(B_0(-a)K_n)\) are the generator \(H^2\)'s and the syzygy
\(H^3\)'s. Trace self-duality and Serre duality on \(\mathbf P^4\)
identify their duals with
\[
 H^2(B_0(a+d_i-5)),\qquad H^1(B_0(a+e_i-5)).
\]
For the three terms of (1), \(n=k-1,k-2,k-3\), while
\(a=3,4,5\), respectively. In every case \(a+n=k+2\). At \(k\geq7\),
\[
 a+d_i-5\geq k-3\geq4,\qquad
 a+e_i-5\geq k\geq7.
\]
PR167's vanishings kill both outer groups. Every summand in (1)
has zero \(H^2\), proving (3).

In particular, on a quotient-adapted affine cover, every regular
closed \(I^7E\)-valued \(\chi\) two-cochain has a regular \(\chi\)
primitive in the **same ideal-valued complex**. This is stronger
than exactness after forgetting \(I^7\), but does not choose or
compute such a primitive.

## 6. Finite-neighborhood and source consequences

Let \(Q_7=E/I^7E\). Equation (3) makes restriction
\[
 H^2(Z,E)_\chi\longrightarrow H^2(Z,Q_7)_\chi
\]
injective on the entire character sector, with no paired-space
exhaustion or cohomology-dimension premise. Equation (2) presents
its target by the three actual quotient coefficients with ideals
\(K_6,K_5,K_4\), in that order.

This does not split each thickening into its reduced conormal
layers, and does not prove surjectivity from unrestricted
cohomology. The latter still has its separate \(H^3(I^7E)_\chi\)
obstruction.

For any closed regular \(\chi\) cochain \(R\),
\([R]=0\) if and only if it has a regular primitive modulo \(I^7\).
For the nontrivial direction, lift the quotient primitive to an
\(E\)-valued one-cochain by affine section exactness, and average
to \(\chi\). The remaining closed cochain is \(I^7E\)-valued and
has an ideal-valued primitive by (3). Adding the two primitives
gives a primitive of \(R\).

It follows also that \(R\) has a cohomologous closed \(I^7E\)
representative if and only if \([R]=0\). In the reverse direction,
the zero representative suffices. The new structural statement
is the entire coefficient calculation and vanishing, not this
elementary logical consequence by itself.

For a source application, retain all hypotheses of PR434's
complete-source comparison \([R_0]=j_0(C)\), and first apply the
\(\chi\)-projector if necessary; it preserves the paired class.
PR387 and PR139 identify zero of \(C\) with zero of its constant,
first-weight, and centered second-weight coordinates. If the
separate constant-zero certificate applies, high-order
representability of this **same class** is therefore equivalent
to vanishing of the two weighted traces. It is not an automatic
additional consequence of coefficient geometry.

PR435's nonzero factor four and binary-volume scalar rescale this
equivalence but cannot create ideal membership. Its comparison
boundary remains necessary for a literal primitive reconstruction.

No actual source coordinate, order-seven representative, pure-square
condition, module lift, higher continuation, or algebraicity is
established. No selected source-instance evaluation, generator,
checker, or large computation was performed.

## Exact public dependencies

All paths below belong to `Akilleez-QA/read-em-and-weep`.

1. [PR158 weight geometry](https://github.com/Akilleez-QA/read-em-and-weep/blob/aab61d34a84c9b8b5a908606a7beb7212d45fe7c/research/conductor-normalization/ideal-power-contractions/WEIGHT-GEOMETRY-INPUTS.md).
   Commit `aab61d34a84c9b8b5a908606a7beb7212d45fe7c`,
   blob `507b5281144debc5395f88ac605e5a89c4867b87`.
   Used for the reduced regular-sequence geometry and exact weight differences.
2. [PR158 fourth-power proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/aab61d34a84c9b8b5a908606a7beb7212d45fe7c/research/conductor-normalization/fourth-ideal-pushforward/PROOF.md).
   Same commit, blob `9ac68fc3222ec751864310a74bebffd95bbd2cb4`.
   Used for global \(N\), the reduced image injection, and existing
   ordinary-power and full-sign calculations.
3. [PR158 all-powers proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/aab61d34a84c9b8b5a908606a7beb7212d45fe7c/research/conductor-normalization/sixth-ideal-pushforward/ALL-POWERS.md).
   Same commit, blob `cea0e8cf665c2800bc141759e97921ec71277032`.
   Used for the weighted associated graded and adjacent resolutions.
4. [PR139 cubic reconstruction](https://github.com/Akilleez-QA/read-em-and-weep/blob/c5fb4a0bcc3c8e35093fcfcff9a73a79a45a18e5/research/hm/cubic-reconstruction/PROOF.md).
   Commit `c5fb4a0bcc3c8e35093fcfcff9a73a79a45a18e5`,
   blob `daf01b27c34233f81aa2f2a2eae0f4f90827ef89`.
   Part I supplies the global cubic basis, centered \(\tau\), and relation.
   The conditional source corollary additionally uses its trace reconstruction.
5. [PR387 normalized coefficient transport](https://github.com/Akilleez-QA/read-em-and-weep/blob/e276e0e181e62a60c3ae24759b8bfed746f2492b/research/regular-trace-transport/PROOF.md).
   Commit `e276e0e181e62a60c3ae24759b8bfed746f2492b`,
   blob `35c0afd278af0d6a106e3514239080d4a3576953`.
   Used for the quotient tower and ordinary/canonical sign conventions.
6. [PR167 sharper regularity](https://github.com/Akilleez-QA/read-em-and-weep/blob/063da90fc4543304e87e701cdefcc08225412f17/research/conductor-normalization/sharper-hm-regularity/SHARPEST-BOUND.md).
   Commit `063da90fc4543304e87e701cdefcc08225412f17`,
   blob `58785a8799c43fd2c7da089d0ddc5e05822132a9`.
   Used only for the stated HM cohomology consequences.
7. Source application only:
   [PR434 complete-source transport](https://github.com/Akilleez-QA/read-em-and-weep/blob/9a37da0a0ef67d8790b20e8edbf8d930de658251/research/hm/weighted-class-transport/PROOF.md)
   and
   [PR435 legacy normalization](https://github.com/Akilleez-QA/read-em-and-weep/blob/da5a08b7fba20a3c8f87050a5a1bd237276b93d0/research/hm/legacy-volume-comparison/PROOF.md).
   Their complete-source, regularity, marking, and comparison hypotheses
   remain imports, not conclusions of this note.

For nonduplication, the compared prior results include
[PR167 finite-neighborhood proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/063da90fc4543304e87e701cdefcc08225412f17/research/conductor-normalization/finite-collision-detection/PROOF.md)
and
[PR383 full-target criterion](https://github.com/Akilleez-QA/read-em-and-weep/blob/35348bd2145bd4c2997937960ddedc4de7842428/research/conductor-prerequisites/full-target-collision-criterion/PROOF.md),
along with PR418/419 at `acd667b30e1ed54a64c646ba728b9357ebefbd85`
and `c7c35a8ec40983ed1e0ede4f80e359ad34a7fefc`.
The present note does not count their already proved paired-space
criterion, full-sign filtration, selection, or Koszul splitting as new.
