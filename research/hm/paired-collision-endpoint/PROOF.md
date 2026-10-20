# The exact order-six paired-character endpoint

## Result and limits

Retain the geometric conventions, fixed weight lines, and exact filtered
coefficient identification in
[the paired-character filtration proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/50e82ed233cd7729c38608194f990376eb832418/research/hm/paired-collision-filtration/PROOF.md).
In particular
\[
 (q_*(I^kE))_\chi
 \cong B_0(-3)K_{k-1}\oplus B_0(-4)K_{k-2}
                       \oplus B_0(-5)K_{k-3},       \tag{1}
\]
where \(B_0=\operatorname{End}_0(F)\) for normalized HM,
\(E=q^*B_0\otimes A^{-2}\), \(\chi=\operatorname{sgn}|_H\), and
\[
 K_n=(u^a v^b:2a+3b\geq n),\qquad u=t_2,\quad v=t_3.
\]
Define the finite-dimensional multiplication quotient
\[
 Q=
 \frac{H^1(Y,B_0(6))}
 {u\,H^1(Y,B_0(4))+v\,H^1(Y,B_0(3))}.                \tag{2}
\]
Then, with the fixed one-dimensional weight factors understood,
\[
 H^2(Z,I^6E)_\chi^\vee\cong Q\oplus Q.                \tag{3}
\]

Thus zero of the whole order-six ideal-coefficient group is equivalent
to the surjectivity of the one map
\[
 H^1(B_0(4))\oplus H^1(B_0(3))
 \xrightarrow{(u,\ v)}H^1(B_0(6)).                  \tag{4}
\]
Neither this map's rank nor the quotient \(Q\) is evaluated.
This does not assert that order six suffices, that seven is optimal,
or that a particular source has either order.

In particular, (3) concerns the whole ideal-coefficient group.
Even a nonzero \(Q\) would not by itself prove nonzero of its image
in unrestricted \(H^2(E)_\chi\), or nonzero of any source class.

## 1. Inputs

The coefficient identity (1) is the new filtered calculation used here;
its proof includes all quadruple collisions, line twists, and regularity.
The remaining inputs are the public prior results:

- The exact adjacent-monomial resolutions of \(K_n\) in PR158.
- Trace self-duality \(B_0^\vee\simeq B_0\).
- \(H^2(B_0(t))=0\) for \(t\geq2\) and
  \(H^1(B_0(t))=0\) for \(t\geq7\), from PR167.
- Only for the numerical upper bound at the end:
  \(h^1(B_0(6))\leq30\), also from PR167.

No cohomology dimension at a lower twist or surjectivity of a
multiplication map is assumed.

## 2. The three exact ideal resolutions

At order six, (1) is
\[
 B_0(-3)K_5\oplus B_0(-4)K_4\oplus B_0(-5)K_3.      \tag{5}
\]
The minimal generators and adjacent syzygies are explicit.

For \(K_3=(v,u^2)\),
\[
 0\longrightarrow\mathcal O(-7)
 \xrightarrow{(u^2,-v)}
 \mathcal O(-3)\oplus\mathcal O(-4)
 \xrightarrow{(v,u^2)}K_3\longrightarrow0.          \tag{6}
\]

For \(K_4=(u^2,uv,v^2)\),
\[
 0\longrightarrow\mathcal O(-7)\oplus\mathcal O(-8)
 \xrightarrow{S_4}
 \mathcal O(-4)\oplus\mathcal O(-5)\oplus\mathcal O(-6)
 \longrightarrow K_4\longrightarrow0,              \tag{7}
\]
with columns
\[
 S_4=\begin{pmatrix}v&0\\-u&v\\0&-u\end{pmatrix}.
\]

For \(K_5=(u^3,uv,v^2)\),
\[
 0\longrightarrow\mathcal O(-9)\oplus\mathcal O(-8)
 \xrightarrow{S_5}
 \mathcal O(-6)\oplus\mathcal O(-5)\oplus\mathcal O(-6)
 \longrightarrow K_5\longrightarrow0,              \tag{8}
\]
with columns
\[
 S_5=\begin{pmatrix}v&0\\-u^2&v\\0&-u\end{pmatrix}.
\]
These are the actual adjacent resolutions, not merely degree lists.
Their exactness at \(N=V(u,v)\) follows from the flat polynomial-base
argument in PR158; away from \(N\) they resolve the unit ideal and
are split exact after localization. Thus the quadruple-root curve
has not been removed.

## 3. The \(K_3\) summand vanishes already

Tensor (6) by \(B_0(-5)\). Its generator terms are
\(B_0(-8)\oplus B_0(-9)\), and its syzygy term is \(B_0(-12)\).
By Serre duality on \(\mathbf P^4\) and self-duality of \(B_0\),
the dual controlling groups are
\[
 H^2(B_0(3))\oplus H^2(B_0(4)),\qquad H^1(B_0(7)).
\]
All vanish by PR167. Hence
\[
 H^2(Y,B_0(-5)K_3)=0.                               \tag{9}
\]

## 4. The \(K_4\) summand produces \(Q\)

Tensor (7) by \(B_0(-4)\), and call the resulting sequence
\(0\to F_1\to F_0\to G\to0\). The generator \(H^2(F_0)\) is zero:
its dual groups have twists \(3,4,5\), within the proven vanishing range.
The long exact sequence therefore identifies
\[
 H^2(G)=\ker[H^3(F_1)\to H^3(F_0)].
\]
All these groups are finite-dimensional. Dualizing, and using the
naturality of Serre duality for the actual sheaf map \(S_4\), gives
\[
 H^2(G)^\vee
 =\operatorname{coker}\bigl[H^1(F_0^\vee(-5))
                       \to H^1(F_1^\vee(-5))\bigr].            \tag{10}
\]
The source in (10) is
\[
 H^1(B_0(3))\oplus H^1(B_0(4))\oplus H^1(B_0(5)),
\]
and the target is \(H^1(B_0(6))\oplus H^1(B_0(7))\).
The latter's second summand is zero. The transpose of the first
column of \(S_4\) gives the surviving map
\[
 (a,b,c)\longmapsto va-ub.
\]
Its image is precisely
\(vH^1(B_0(3))+uH^1(B_0(4))\). Thus
\[
 H^2(Y,B_0(-4)K_4)^\vee\cong Q.                     \tag{11}
\]
This retains the incoming multiplication ambiguity; replacing the
cokernel by \(H^1(B_0(6))\) would be unjustified.

## 5. The \(K_5\) summand produces the same quotient

Tensor (8) by \(B_0(-3)\). Its generator \(H^2\)'s are again zero:
their Serre-dual twists are \(4,3,4\).
As above, the dual \(H^2\) of the ideal coefficient is a cokernel.
Its source is
\[
 H^1(B_0(4))\oplus H^1(B_0(3))\oplus H^1(B_0(4)),
\]
and its target is \(H^1(B_0(7))\oplus H^1(B_0(6))\).
Now the first target is zero, and the transpose of the second
column of \(S_5\) gives the surviving map
\[
 (a,b,c)\longmapsto vb-uc.
\]
Its image is the same sum as in (11). Therefore
\[
 H^2(Y,B_0(-3)K_5)^\vee\cong Q.                     \tag{12}
\]
The signs do not affect the sum of images, but the two different
syzygy positions and all twists have been retained.

Finite pushforward, exact \(\chi\)-projection, (5), (9), (11), and
(12) now prove (3).

## 6. What the endpoint resolves

The previous filtered theorem proves entire coefficient vanishing
at order seven. Formula (3) identifies exactly what must additionally
vanish to lower that whole-coefficient result to order six.
It is a single degree-six \(H^1\)-module quotient appearing twice,
not three unspecified cohomology groups.

The public endpoint estimate \(h^1(B_0(6))\leq30\) yields
\[
 h^2(Z,I^6E)_\chi=2\dim Q\leq60.
\]
No equality, positivity, rank, or optimality is asserted.

If (4) were separately proved surjective, the order-six restriction
would be injective on the whole character sector, by the same
coefficient exact sequence as at order seven. Conversely, failure
of (4) would only disprove whole-coefficient vanishing; restriction
could still be injective if the nonzero ideal cohomology mapped
to zero in unrestricted cohomology.

No actual HM multiplication, matrix, selected source, generator,
checker, or large computation was evaluated. No actual high-order
representative or primitive, obstruction value, module lift,
pure-square vanishing, or algebraicity conclusion is supplied.

## Exact dependency pins and prior-work comparison

The first dependency is
[the paired-character filtration proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/50e82ed233cd7729c38608194f990376eb832418/research/hm/paired-collision-filtration/PROOF.md),
specifically its actual filtered subsheaf identity (1).
Its reviewed edition is commit `50e82ed233cd7729c38608194f990376eb832418`,
Git blob `9697423e880070cdf34cbc3548f5a2b32b2a40a0`, SHA-256
`41fd8967a1bd876c0375ab35c889d3eec431e5a72cd66ca2fa74937e503cbca1`.
A Git stack alone does not supply this mathematical dependency.

The remaining public inputs are:

- [PR158 all-powers contractions and resolutions](https://github.com/Akilleez-QA/read-em-and-weep/blob/aab61d34a84c9b8b5a908606a7beb7212d45fe7c/research/conductor-normalization/sixth-ideal-pushforward/ALL-POWERS.md),
  commit `aab61d34a84c9b8b5a908606a7beb7212d45fe7c`,
  blob `cea0e8cf665c2800bc141759e97921ec71277032`.
- [PR167 sharper regularity and endpoint bound](https://github.com/Akilleez-QA/read-em-and-weep/blob/063da90fc4543304e87e701cdefcc08225412f17/research/conductor-normalization/sharper-hm-regularity/SHARPEST-BOUND.md),
  commit `063da90fc4543304e87e701cdefcc08225412f17`,
  blob `58785a8799c43fd2c7da089d0ddc5e05822132a9`.

The prior full-sign sixth-power theorem was also inspected:
[PR158 sixth-power proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/aab61d34a84c9b8b5a908606a7beb7212d45fe7c/research/conductor-normalization/sixth-ideal-pushforward/PROOF.md),
blob `8838faef24065d5e0bab027163e51b6a34faabee`.
It concerns the full-sign coefficient \(B_0(-4)K_3\), not the
full \(H\)-character coefficient (5). The different
[PR171 socle-syzygy detector](https://github.com/Akilleez-QA/read-em-and-weep/blob/8236d128910c667610361966011456aa9478747f/research/conductor-normalization/socle-syzygy-detector/PROOF.md),
blob `d450a7e58e0abd39bc0ba88223f2df22b2d4e674`,
uses coordinate-Koszul transgressions for the degree-minus-one
\(H^2\) socle. Its quotient and maps are not the multiplication
quotient (2).
