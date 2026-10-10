# An explicit first-order lift and its executable source

## 1. The actual local split complex

Use the exact model of
[the geometric package](https://github.com/Akilleez-QA/read-em-and-weep/tree/dc60a859a0157b1d2d1b57b37324509abc22c600/research/hm/current-scalar-geometric-dependencies).
For each of its six carriers the matrices `I,P,H0,H1,eta` satisfy
\[
PI=1,\quad E=IP=1-\gamma H_0-H_1\delta_K,\quad
H_0\gamma=1,\quad\delta_KH_1+\eta\mathrm{ev}=1,\quad
\mathrm{ev}\eta=1,
\]
together with `δK I=P γ=H0 I=P H1=H0 H1=H1 eta=0`.
These are exact homogeneous rational identities checked there, not point
samples. Its physical-frame proof specifies their conversion on all product
charts. The present determinant checker additionally proves all 36 identities
`det(P_i I_j)=1` by integer polynomial cross multiplication.

For pivot `j` let `W` be the eight columns in `ker(ev)` obtained, in each
five-coordinate block, by `e_k-(v_k/v_j)e_j` for `k != j`. Let `L` select
those eight nonpivot coordinates, and let `eta` have pivot entries `1/v_j`.
Then `LW=1`, `W L+eta ev=1`, `ev W=L eta=0`. The source uses
\[
U_0=(\gamma,I,H_1W),\quad Q_0=(H_0;P;L\delta_K),\qquad
U_1=(W,\eta),\quad Q_1=(L;\mathrm{ev}).
\]
The identities above give `U0 Q0=Q0 U0=1`, and likewise for `U1,Q1`.
For example `U0 Q0=γH0+IP+H1(1-eta ev)δK=1`.
In these bases the differential is the identity on each paired contractible
summand and zero on the two cohomology coordinates. Thus the displayed
source gives the required constant-differential splittings explicitly.

The cover also refines the two line charts of every elliptic factor:
\[
U_0=C\setminus\{\infty\},\qquad
U_1=C\setminus\{(0,0),(1,0),(-1,0)\}.
\]
Frames of `N` are `e0=1` and `e1=y/x`. If `ell` is the old `N²` frame with
transition `x`, then `e0²=ell0`, `e1²=(1-x^-2)ell1`.
The old connection induced by half the frame-flat `N²` connection has
\[
\gamma_0=0,\qquad\gamma_1=\frac{dx}{x(x^2-1)}.
\]
On `N^k` use `k gamma`; at infinity transport this same connection to
`-t dt/(1-t²)`. It must not be reset to the zero connection there.

In a line chart with ratio `nu=product_r (y_r/x_r)^(m_r)`, the differential
in the `e` frames has coefficients `nu^-2` times the old polynomial matrices.
Correspondingly, the columns of `U0` are scaled by
\[
(\nu^{-2}I_5,\ 1,\ \nu^{-2},\ \nu^2I_8),
\]
and those of `U1` by `(I8,nu² I2)`. Their inverse rows have reciprocal
scalings; extreme split bases are identities. Directly, `nu^-2 γ` becomes
the first five columns of `U0`, `nu^-2 δK` sends the last eight columns
of `U0` to the first eight of `U1`, and `nu^-2 ev` sends the last two
columns of `U1` to the identity. These are precisely `w0,w1` in
`globalBuild2`. No compatible quantization of the separate line summands
is assumed.

## 2. Unsymmetrized transgression

Let `nabla` be these old connections, and `nabla'=nabla+B` the connections
flat in the split bases. In the old local frames
\[
B_i=-(dU_i)U_i^{-1}-\operatorname{diag}(k\gamma_i),
\qquad k=(-1,1,3,5).
\]
Transport to a common frame for products. Let `Aij=nabla_j-nabla_i`, so
`A'=A+δB` and `δA=0`. Distinguish two products: `wedge` below means
ordinary wedge of form coefficients with Alexander–Whitney composition,
without an extra Čech–forms sign; `star_tot` is the total product, with
sign `(-1)^(form_degree * next_Cech_degree)`. Thus, for the bidegree
`(1,1)` cochains `A`, `A'`, `A^E`, and `theta0`,
\[
A\star_{\rm tot}A=-A\wedge A,\qquad
\theta_0\star_{\rm tot}\theta_0=-\theta_0\wedge\theta_0.
\]
Define the transgression using the total product:
\[
\mathcal T=\operatorname{str}
(B\star_{\rm tot}A+A\star_{\rm tot}B+B\star_{\rm tot}\delta B).
\]
The graded derivation rule gives
`δT=str(A' star_tot A' - A star_tot A)`. In the ordinary-wedge
notation used in every displayed square below, this is exactly
\[
\delta\mathcal T=\operatorname{str}
\bigl(A\wedge A-(A+\delta B)\wedge(A+\delta B)\bigr).
\tag{3}
\]
For clarity, in the total product `δ(B star_tot A)=δB star_tot A`,
`δ(A star_tot B)=A star_tot δB`, and
`δ(B star_tot δB)=δB star_tot δB`. The two first terms are retained
separately. Ordinary Alexander–Whitney products do not justify replacing
their sum by twice the first term using a putative cyclic cochain trace.

Each `nabla'` commutes with the split differential. A product of its
difference endomorphisms is a chain endomorphism, so its supertrace equals
the trace of the induced endomorphism on `E`: the paired contractible
diagonal blocks cancel. In particular
`str(A' wedge A')=tr(A^E wedge A^E)` as cochains.

Write `theta0=(1/2)sum_r dlog(x_r)` in Čech degree one. The old difference
on `N^k` is `-k theta0`, whence
\[
\operatorname{str}(A\wedge A)
=(-5+15-90+50)\theta_0\wedge\theta_0
=-30\theta_0\wedge\theta_0.
\]
Equivalently, the totalized identity is
`str(A star_tot A)=-30(theta0 star_tot theta0)`; both square factors
must be totalized together. Let `iOrd_π` denote ordinary contraction of
form coefficients, with `i_(Vr wedge Vs)=i_Vs i_Vr`. Put
`Qrs=q_r cup q_s`. Then
\[
\Pi_{AW}=-\tfrac12\iota^{\rm ord}_\pi(\theta_0\wedge\theta_0)
=-\tfrac18(Q_{12}-Q_{21}+Q_{34}-Q_{43}),\quad
r_{ij}=q_{1,ij}q_{2,ij}+q_{3,ij}q_{4,ij}.
\]
Since `δr=-(Q12+Q21+Q34+Q43)`, the exact representative conversion is
\[
-15\Pi_{AW}=b+\tfrac{15}{8}\delta r.
\]
Consequently the explicit scalar cochain
\[
s=-\tfrac14\iota^{\rm ord}_\pi\mathcal T-\tfrac{15}{8}r
\tag{4}
\]
satisfies, directly from (3),
\[
\begin{aligned}
\delta s
&=\tfrac{30}{4}\iota^{\rm ord}_\pi(\theta_0\wedge\theta_0)
 +\tfrac14\iota^{\rm ord}_\pi\operatorname{tr}(A^E\wedge A^E)
 -\tfrac{15}{8}\delta r\\
&=b+\tfrac14\iota^{\rm ord}_\pi\operatorname{tr}(A^E\wedge A^E).
\end{aligned}
\]

## 3. The rank-two trace-free solution

Use column transitions `Gij=gij^t`, so `Gik=Gij Gjk` and
`A^E_ij=-dGij Gij^-1`. Reversal of order on transposition gives,
in the same ordinary-wedge convention,
\[
C_{ijk}=g_{ik}^{-1}\mu_1(g_{jk},g_{ij}),\qquad
\operatorname{tr}C=-\tfrac12\iota^{\rm ord}_\pi
\operatorname{tr}(A^E\wedge A^E).
\]
Thus `δs=b-(1/2)tr C`, unchanged. To see the sign directly, write
`P_r=gij^-1 V_r(gij)` and `Q_r=gij^-1 gjk^-1 V_r(gjk) gij`.
The two column difference forms, in a common frame, have coefficients
`-P_r^t` and `-Q_r^t`. For a bivector pair `(a,b)`, their ordinary wedge
has contracted trace `tr(Q_b P_a-Q_a P_b)`, which is minus twice
the corresponding trace of `C`.

For a determinant-one transition define `K(g)=μ1(g^-1,g)`.
The logarithmic derivatives `P_r,Q_r` above are traceless, and
\[
C=\tfrac12\pi^{rs}Q_rP_s,\qquad
\delta K=\tfrac12\pi^{rs}[Q_r,P_s].
\]
The elementary identity for traceless two-by-two matrices
`[Q,P]=2QP-tr(QP)I` proves
\[
\delta K=2C-\operatorname{tr}(C)I.
\]
Therefore
\[
x_{ij}=s_{ij}I-\tfrac12K(g_{ij}),\qquad u_{ij}=g_{ij}x_{ij}
\tag{5}
\]
solves `δx=bI-C`, exactly the first-order module equation (1).
The scalar projection's factor `1/2` is specific to rank two.
The integrated regression in `checks/verify_algebra.py` follows (3), the
`-30` ordinary-wedge coefficient, the exact gerbe correction, this row/column
trace calculation, and the rank-two identity all the way to `δx=bI-C`.
It explicitly rejects either an isolated reversal of the ordinary
transgression sign or an isolated reversal of the row/column trace sign.
This clarifies the square notation; the cochains (4)–(5), the source
generator, and the first-order equation are not changed.

## 4. Equality with the pinned generator

The complete source is
[PR #35's reduced generator](https://github.com/Akilleez-QA/read-em-and-weep/blob/6032b64d3f748c7ac37cb283db4a527e49d06ac8/research/hm/current-scalar-source-bridge/public_generate_hm_mask_coefficients_reduced.js).
Its five function excerpts are bundled in the geometric package; their exact
hash and the complete-generator hash are checked here. The bridge proves
rational equality of the reduced and original primitive model entries.

The generator strips one invariant `y_r` factor for each used coordinate.
Its square-free jets use ordinary `partial/partial x_r`, so `md(A,r)` means
the stripped invariant derivative. Every derivative in the mixed expression
uses distinct coordinates; thus it introduces no unrecorded `V_r(y_r)` term.
Only the zero, single, and distinct-pair jet slots are needed. A derivative
of the `(1,2)` first lift in coordinate 3 or 4, for example, differentiates
only these pair jets and their complementary first derivative.

Here is the source-to-formula dictionary, using zero-based source indices:

- `rf=(x²+1)/(2x(x²-1))` is `dlog(y/x)/dx`;
  `ga=1/(x(x²-1))` is the old half-connection coefficient.
- `q(i,j,a)=(mask_j[a]-mask_i[a])/x_a` is the Čech cocycle `q_a`
  after its `y_a` factor is removed. It is not the logarithmic derivative
  `rf` of the refined line frame.
- `nu[0]=1` fixes a constant frame normalization at the evaluation point;
  the nonzero derivative slots are retained as products of `mask[a] rf[a]`.
  This is the jet of a nonconstant frame, not differentiation of the
  identically-one function. Constant diagonal frame factors cancel after
  normalized residual, transpose, inclusion, and projection, as verified
  in the geometric package.
- `g=transpose(diag(nu_i^-1,nu_i) (P_i I_j)
  diag(nu_j,nu_j^-1))`. Each diagonal factor has determinant one.
  Together with all 36 exact model checks this justifies the source's
  two-by-two adjugate formulas for `g^-1` without a determinant denominator.
- `blocks[a][k]` is the coefficient of `B` in degree `k`: the raw
  `-(partial_a U)Q`, minus `k gamma` on the diagonal, with supertrace
  signs `(-,+,-,+)` on ranks `(5,15,10,2)`.

There is a particularly transparent check of the scalar implementation.
On an edge, write `Aij=-k theta_ij I`. From the *unsymmetrized* formula,
\[
\mathcal T_{ij}=
-\operatorname{str}\bigl(B_i\wedge B_j
 +k\theta_{ij}\wedge(B_i+B_j)\bigr).
\tag{6}
\]
Here only the legitimate ordinary coefficient identity
`tr(B_i wedge B_i)=0` was used. For the pair `(a,b)`, the source's
`wedge` is `tr(Bi_a Bj_b-Bi_b Bj_a)`, while `linear` is
\[
k[\theta_a\operatorname{tr}(B_{i,b}+B_{j,b})
-\theta_b\operatorname{tr}(B_{i,a}+B_{j,a})],\quad\theta_a=q_a/2.
\]
Its `scalar=sum/4-15 q_a q_b/8` is exactly (4) by (6).
Its `K` is `μ1(g^-1,g)`, `Z=-K/2+scalar I`, and return value `G Z`
is exactly (5). This explains every first-order scalar and matrix term,
including the Čech representative correction, rather than just matching
byte hashes or observing that numerical first-order tests pass.

The split-basis, old connection, and column weights above instantiate the
ingredients of (3)–(5) for these precise source formulas. No global finite
RHom projection is needed to prove this first-order equation.
