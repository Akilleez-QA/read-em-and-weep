# A second-order algebraic algebroid calculation for the Horrocks–Mumford pullback

## Status and scope

This note gives an authored chain-level derivation through order \(h^2\), including the sign calibration, the noncentral algebroid descent data, the module residual, and an exact comparison procedure into a finite RHom model. It does not report an executed second-order obstruction calculation or assert that the full-sign obstruction vanishes.

The separate [finite-RHom model and certificates](https://github.com/Akilleez-QA/read-em-and-weep/pull/5) is the dependency for the classical complex, its finite Čech–homological-perturbation model, and the character-rank statements used below. Local four-term contractions are instantiated and checked in the separate local-contractions certificate. The global refinement comparison, first-order lift, and projected second-order residual remain to be instantiated.

The [commit-pinned executable Ext certificate](https://github.com/Akilleez-QA/read-em-and-weep/blob/13b0cf86ef83d587290b13d8d51577b0a1e8f802/research/hm/verify-hm-ext.js) supplies the reproduced classical calculation. [Local contractions](https://github.com/Akilleez-QA/read-em-and-weep/pull/10), [six-chart transitions](https://github.com/Akilleez-QA/read-em-and-weep/pull/14), and the [line calibration target](https://github.com/Akilleez-QA/read-em-and-weep/pull/15) are separate checked artifacts.

## 1. Geometry and conventions

Let \(C\) be the smooth projective completion of \(y^2=x^3-x\), let \(X=C^4\), and write
\[
V_i=y_i\partial_{x_i}+\frac{3x_i^2-1}{2}\partial_{y_i},
\qquad
\pi=V_1\wedge V_2+V_3\wedge V_4.
\]
The \(V_i\) commute. Let \(\omega_i=dx_i/y_i\), so that \(\omega_i(V_i)=1\).

All calculations are in \(\mathbf C[h]/(h^3)\). The star product is
\[
f\star g=fg+h\mu_1(f,g)+h^2\mu_2(f,g),
\]
where
\[
\mu_1(f,g)=\frac12\pi(df,dg),\qquad
\mu_2(f,g)=\frac18\sum\pi^{ij}\pi^{k\ell}
 (V_iV_kf)(V_jV_\ell g).
\]
For matrix arguments, the same bidifferential operators include ordinary matrix multiplication and summation over the intermediate matrix index.

Use the usual Čech differential and Alexander–Whitney cup product. On Čech–forms of bidegrees \((p,q)\) and \((p',q')\), use the total product
\[
(\alpha,\eta)(\beta,\zeta)
 =(-1)^{q p'}(\alpha\smile\beta,\eta\wedge\zeta).
\]
Set \(\iota_{V_i\wedge V_j}=\iota_{V_j}\iota_{V_i}\).

The bundle of interest is the determinant-trivial rank-two pullback of the normalized Horrocks–Mumford bundle, twisted by \(N=\mathcal O_X(\Theta)\). Its classical model is
\[
K=\bigl[5N^{-1}\longrightarrow15N
       \longrightarrow10N^3\longrightarrow2N^5\bigr],
\]
in degrees \(-1,0,1,2\), with cohomology \(E\) in degree zero. The finite-RHom certificate supplies the specific classical matrices and the verification of this model. The characteristic-class normalization is \(c_2(E)=15\theta^2\), with \(\theta=c_1(N)\), and
\[
\Pi=\iota_\pi(\theta^2)/2,\qquad B=15\Pi.
\]

## 2. The rational cocycle and its derivative primitive

On one elliptic factor use the inverse images of the standard \(x\)- and \(t=1/x\)-charts. On their overlap put
\[
q=y/x.
\]
Direct differentiation gives
\[
V(q)=\frac{x+x^{-1}}2.
\]
For the Čech zero-cochain
\[
a_0=-x/2,\qquad a_\infty=x^{-1}/2,
\]
one therefore has \(\delta a=V(q)\). Pull these cochains back to the four factors.

Let
\[
b=\sum_{r,s}\beta_{rs}\,q_r\smile q_s
\]
be a chosen scalar Čech two-cocycle. Define degree-one cochains
\[
s_k=\sum_{r,s}\beta_{rs}
 \bigl(\delta_{kr}a_r\smile q_s
       -\delta_{ks}q_r\smile a_s\bigr).
\]
The sign is forced by
\[
\delta(q_r\smile a_s)=-q_r\smile\delta a_s.
\]
It follows that
\[
\delta s_k=V_kb.
\]
Consequently the Čech one-cochain of ordinary derivations
\[
T=\sum_{k,\ell}\pi^{k\ell}s_kV_\ell
\]
satisfies
\[
\delta T=\{b,-\}.
\]

For the convenient representative
\[
b=\lambda(q_1\smile q_2+q_3\smile q_4),
\]
the formula becomes
\[
T=\lambda\bigl[
 (a_1\smile q_2)V_2+(q_1\smile a_2)V_1+
 (a_3\smile q_4)V_4+(q_3\smile a_4)V_3
 \bigr].
\]
Thus \(T_{\alpha\beta}\), for cover multi-indices \(\alpha,\beta\), is explicitly
\[
\lambda\bigl[
 a_{1,\alpha}q_{2,\alpha\beta}V_2+
 q_{1,\alpha\beta}a_{2,\beta}V_1+
 a_{3,\alpha}q_{4,\alpha\beta}V_4+
 q_{3,\alpha\beta}a_{4,\beta}V_3
 \bigr].
\]

## 3. Algebroid descent through \(h^2\)

On every cover member take the restriction of the same Moyal algebra. Define
\[
F_{ij}=\mathrm{id}+h^2T_{ij},\qquad
A_{ijk}=\exp(hb_{ijk})
       =1+hb_{ijk}+\frac{h^2}{2}b_{ijk}^2.
\]
Here \(A\) denotes the triple-overlap unit; \(a_r\) remains the scalar derivative primitive of Section 2.

The descent equations are
\[
F_{ij}F_{jk}=\operatorname{Ad}_\star(A_{ijk})F_{ik},
\qquad
A_{ijk}\star A_{ikl}=F_{ij}(A_{jkl})\star A_{ijl}.
\]
The first follows from
\[
\operatorname{Ad}_\star(1+hb)=\mathrm{id}+h^2\{b,-\}
\quad\bmod h^3
\]
and \(\delta T=\{b,-\}\). The second follows from \(\delta b=0\): to order \(h^2\), the products of the exponential factors are ordinary products, and the action of \(h^2T\) on \(hb\) first occurs at order \(h^3\).

Because \(T_{ij}\) is an ordinary derivation, \(F_{ij}\) preserves \(\star\) modulo \(h^3\). No assertion of a full formal extension of this particular presentation is needed.

These are the algebra-isomorphism and triple-inner-gluing conditions of [D’Agnolo–Schapira, Section 3](https://arxiv.org/abs/math/0506064). The algebraic descent formalism is also treated by [Yekutieli](https://arxiv.org/abs/0905.0488).

## 4. Polarization normalization and the sign \(b=-B\)

The transition \(x\) trivializes \(\mathcal O_C(2\infty)\) on the original two-chart cover. Thus \(\theta_i\) is represented by
\[
\frac12\,d\log x_i=\frac12q_i\omega_i
\]
in the stated Čech–forms convention.

An exact Alexander–Whitney representative of \(\Pi\) is
\[
-\frac18\bigl(
 q_1\smile q_2-q_2\smile q_1+
 q_3\smile q_4-q_4\smile q_3
 \bigr).
\]
Cohomologically one may use
\[
\Pi=-\frac14[q_1\smile q_2+q_3\smile q_4].
\]
In a tensor Čech model in which independent odd factors anticommute strictly, the shorter expression is already the corresponding chain representative. On an ordinary nerve, choosing the shorter cocycle is a choice of representative; an asserted equivalence to a different representative must include its Čech coboundary.

To calibrate the gerbe sign, represent left modules by row vectors and use semilinear maps
\[
\phi_{ij}(v)=F_{ij}(v)\star G_{ij}.
\]
The module equation is
\[
\phi_{ij}\phi_{jk}=A_{ijk}\phi_{ik},
\qquad\text{equivalently}\qquad
F_{ij}(G_{jk})\star G_{ij}=A_{ijk}\star G_{ik}.
\]

For scalar line-bundle transitions \(l_{ij}\), set
\(\alpha_{ij}=d\log l_{ij}\). The normalized first-order Moyal defect is
\[
\frac{\mu_1(l_{jk},l_{ij})}{l_{ik}}
 =\frac12\pi(\alpha_{jk},\alpha_{ij})
 =-\frac12\pi(\alpha_{ij},\alpha_{jk}).
\]
The total Čech–forms product gives
\[
(\operatorname{At}L)^2_{ijk}
 =-\alpha_{ij}\wedge\alpha_{jk}.
\]
Hence the defect is
\[
\frac12\iota_\pi(\operatorname{At}L)^2,
\]
the usual characteristic contribution of the bivector with the chosen HKR normalization.

The triple-overlap unit contributes \(-b\,\mathrm{id}\) to the first-order module obstruction. Therefore
\[
o_1=\operatorname{ev}_E(\pi)-b\,\mathrm{id}.
\]
To represent the compensated HKR direction
\(\xi=\pi+B\), one must use
\[
\boxed{b=-B=-15\Pi.}
\]
In the shorter cocycle normalization of this section, this means
\[
b=\frac{15}{4}(q_1\smile q_2+q_3\smile q_4).
\]
With \(\operatorname{ev}_E(\pi)=-15\Pi\,\mathrm{id}\), this gives the required first-order cancellation.

## 5. Module transitions and the second-order residual

Write
\[
G_{ij}=g_{ij}+hu_{ij}+h^2v_{ij},
\qquad g_{jk}g_{ij}=g_{ik}.
\]
The order-one equation is
\[
u_{jk}g_{ij}+g_{jk}u_{ij}-u_{ik}
 =b_{ijk}g_{ik}-\mu_1(g_{jk},g_{ij}).
\]

At order two one obtains
\[
v_{jk}g_{ij}+g_{jk}v_{ij}-v_{ik}=-R_{ijk},
\]
where
\[
\begin{aligned}
R_{ijk}={}&u_{jk}u_{ij}
 +\mu_1(u_{jk},g_{ij})+\mu_1(g_{jk},u_{ij})\\
&+\mu_2(g_{jk},g_{ij})
 +T_{ij}(g_{jk})g_{ij}\\
&-b_{ijk}u_{ik}
 -\tfrac12b_{ijk}^2g_{ik}
 -\mu_1(b_{ijk},g_{ik}).
\end{aligned}
\]
Unlabelled products in this formula are ordinary matrix products.

Set
\[
x_{ij}=g_{ij}^{-1}u_{ij},\qquad
y_{ij}=g_{ij}^{-1}v_{ij}.
\]
For the chosen row frames the End\((E)\)-valued Čech differential is
\[
(\delta x)_{ijk}
 =x_{ij}+g_{ij}^{-1}x_{jk}g_{ij}-x_{ik}.
\]
Define
\[
C_{1,ijk}=g_{ik}^{-1}\mu_1(g_{jk},g_{ij})-b_{ijk}\mathrm{id},
\qquad
C_{2,ijk}=g_{ik}^{-1}R_{ijk}.
\]
Then
\[
\delta x=-C_1,\qquad \delta y=-C_2.
\]

The full algebroid descent identities and the first-order module equation imply
\(\delta C_2=0\). Thus
\[
[C_2]\in H^2(X,\operatorname{End}E)
      =\operatorname{Ext}^2(E,E)
\]
is the second-order obstruction for the selected first-order lift.

The order matters. In the column/right-module convention
\(\phi_{ij}(v)=G_{ij}\star F_{ij}(v)\), the consistent equation instead reads
\[
G_{ij}\star F_{ij}(G_{jk})=G_{ik}\star A_{ijk}^{-1}.
\]
A noncentral \(A_{ijk}\) cannot be moved across \(G_{ik}\) without changing the order-two terms.

## 6. An explicit refinement that trivializes \(N\)

The original inverse-image \(x\)- and \(1/x\)-charts trivialize \(N^2\), but they do not automatically trivialize \(N\).

A rational refinement for one elliptic factor is
\[
U_0=C\setminus\{\infty\},\qquad
U_1=C\setminus\{(0,0),(1,0),(-1,0)\}.
\]
Use \(e_0=1\) and \(e_1=q=y/x\) as frames of \(\mathcal O_C(\infty)\). Since
\[
\operatorname{div}(q)=(1,0)+(-1,0)-(0,0)-\infty,
\]
the restriction of this divisor to \(U_1\) is \(-\infty\), as required.

In coordinates \(t=1/x,\ z=y/x^2\), the original second chart has equation
\(z^2=t-t^3\); \(U_1\) inverts \(1-t^2\). The frame identity is
\[
q^2=x(1-t^2).
\]
Hence the squared new frame differs from the original \(N^2\) frame \(x\) by the explicit unit \(1-t^2\). Take products of this refinement on \(X\), then refine further by nonvanishing minors as needed to trivialize \(E\) and construct the local monad splittings.

## 7. Comparison with total Čech End\((K)\)

A classical End\((K)\) complex alone does not determine the characteristic action: tensoring \(E\) by a line bundle preserves its endomorphism algebra but changes its Atiyah class. The module data and comparisons must therefore be retained.

On a sufficiently fine affine cover, choose local contractions
\[
K\ \underset{i}{\overset{p}{\rightleftarrows}}\ E,
\qquad dH+Hd=1-ip,
\]
with \(pi=1\) and the usual side conditions \(Hi=pH=H^2=0\).
The local contraction matrices use column coordinates. The residuals in Section 5 use row coordinates. Therefore first convert \(g_{\mathrm{col}}=g_{\mathrm{row}}^t\) and \(C_{\mathrm{col}}=C_{\mathrm{row}}^t\). The input to the following inclusion is \(C_{\mathrm{row}}^t\), not \(C_{\mathrm{row}}\). Transposition intertwines the linear Čech differentials here but reverses matrix products; the nonlinear residual must be formed in its declared row convention before transposing.

Put \(e=ip\). The induced contraction of endomorphism complexes is
\[
j(f)=ifp,\qquad p_{\mathrm{End}}(F)=pFi,
\]
\[
h_{\mathrm{End}}(F)=HF+(-1)^{|F|}eFH.
\]
A direct calculation gives
\[
[d,-]h_{\mathrm{End}}+h_{\mathrm{End}}[d,-]
 =1-jp_{\mathrm{End}},
\]
because the right-hand side sends \(F\) to \(F-eFe\).

On Čech degree \(r\), put
\[
D_0=(-1)^r[d,-],\qquad h_0=(-1)^r h_{\mathrm{End}}.
\]
Perturb by the Čech differential \(\delta\). With the convention
\(D_0h_0+h_0D_0=1-jp_{\mathrm{End}}\), the perturbed inclusion is
\[
J=(1+h_0\delta)^{-1}j
  =\sum_{n\ge0}(-h_0\delta)^n j.
\]
The sum is finite: each \(h_0\delta\) raises Čech degree and lowers internal degree. The transferred differential on Čech End\((E)\) is its ordinary Čech differential; higher corrections have nonzero negative internal degree and vanish after projection to End\((E)\), which is concentrated in internal degree zero.

This gives a concrete chain map for \(C_1\) and \(C_2\) without assuming that the individual \(N^{2r+1}\) summands possess compatible quantizations.

### Exact refinement comparison

If the scalar Laurent SDR uses the original cover, first compare the refined complex to that cover. On an original affine Čech intersection \(U\), express the refinement as a finite principal cover \(D(f_i)\). Choose one finite subcomplex containing all cochains to be transferred and closed under the differentials and comparison operations used in the calculation. On that common domain:

1. Choose one common \(N\) large enough to clear the denominators throughout that domain.
2. Compute a Bézout identity
   \[
   \sum_i a_i f_i^N=1\quad\text{in }\mathcal O(U).
   \]
3. Use the standard Čech contraction with these denominator-clearing weights.
4. Increase \(N\) if any of the finitely many resulting coefficients still needs denominators cleared.

Weights chosen afresh for unrelated cochains do not define a single linear comparison. A certificate records the common finite domain and closure, actual \(f_i\), exponent bounds, Bézout coefficients, and chain-map/homotopy identities. This finite algebraic comparison replaces any unjustified fixed Laurent cutoff.

### Compatibility across original intersections

Separate affine Bézout contractions need not commute with restriction maps. Use the double Čech complex of the original cover and its refinement. On each original intersection, contract the augmented refinement complex onto sections there, on one common denominator-cleared finite domain.

Perturb this contraction by the original Čech differential (and by the internal differential if the chosen contraction is only complex-linear). With the stated homotopy convention, the corrected projection is P'=p(1+δh)⁻¹. Compose it with the natural augmentation from the refined Čech complex to the double complex.

The terms are finite because h lowers refinement degree. The transferred differential is the original total differential when the inclusion by restriction is already a chain map and hi=0. The actual finite implementation must check these hypotheses and D·P'=P'·D. Applying unrelated affine contractions termwise is not a certified global chain map.

### Mandatory first-order calibration

Before interpreting any second-order value, the implemented comparison must send the compensated first-order residual for N and N⁻¹ to 16Π=−4[q₁∪q₂+q₃∪q₄], and the residual for E to zero. These tests jointly calibrate the gerbe sign, row-to-column transpose, refinement and finite projection. A failure invalidates the implemented comparison before any second-order conclusion.

## 8. Full-sign character projection

Let the deck group be \((\mathbf Z/2)^4\), where the \(i\)-th generator sends \(y_i\) to \(-y_i\). Both \(q_i\) and \(V_i\) have character \(\chi_i\), while \(a_i\) is invariant.

Write \(b=b_{12}+b_{34}\). The derivation cochain \(T\) of Section 2 has character zero. Moreover,
\[
\pi_{12}(db_{34},dg)=0,\qquad
\pi_{34}(db_{12},dg)=0.
\]
Therefore the normalized terms \(T(g)g\) and \(\mu_1(b,g)\) have no
\(\chi_{1234}\) component.

The cross part of \(\mu_2\) is
\[
\begin{aligned}
\mu_{2,1234}(f,g)=\frac14\bigl[
 &(V_1V_3f)(V_2V_4g)
 -(V_1V_4f)(V_2V_3g)\\
 &-(V_2V_3f)(V_1V_4g)
 +(V_2V_4f)(V_1V_3g)
 \bigr].
\end{aligned}
\]
For an equivariantly selected first-order lift \(u=u_{12}+u_{34}\), the full-sign residual consists of:

- \(u_{12,jk}u_{34,ij}+u_{34,jk}u_{12,ij}\);
- the four cross terms pairing \(\mu_{1,12}\) with \(u_{34}\), and \(\mu_{1,34}\) with \(u_{12}\);
- \(\mu_{2,1234}(g_{jk},g_{ij})\);
- \(-b_{12,ijk}u_{34,ik}-b_{34,ijk}u_{12,ik}\);
- \(-b_{12,ijk}b_{34,ijk}g_{ik}\).

The noncentral corrections must still be included when checking the unprojected cocycle identity.

### Independence from first-order module choices

Assume the character-rank statement in the [finite-RHom model and certificates](https://github.com/Akilleez-QA/read-em-and-weep/pull/5):
\[
\operatorname{Ext}^1(E,E)_S=0\qquad (|S|=2,3,4).
\]
A change of first-order lift then has only weights zero and one. Its quadratic contribution has weight at most two; its cross term with a weight-two baseline or ambient first-order class has weight at most three. It cannot alter the full-sign obstruction class. Equivariant comparison maps and SDRs make this decomposition explicit.

### Independence from second-order ambient choices

After identifying the first-order ambient and module data, two order-two ambient lifts differ by a total Hochschild two-cocycle \(\eta\). Their module obstructions differ by \(\operatorname{ev}_E([\eta])\). The natural deck linearization of \(E\) makes this map equivariant.

The HKR decomposition
\[
HH^2(X)=H^0(\Lambda^2T_X)\oplus H^1(T_X)\oplus H^2(\mathcal O_X)
\]
has only deck weights zero and two. Thus its evaluation cannot change the weight-four component. Equality of the entire second-order obstruction would require more than this argument.

The characteristic-map interpretation is described by [Lowen](https://arxiv.org/abs/0707.2602); the algebroid Maurer–Cartan framework is treated by [Bressler–Gorokhovsky–Nest–Tsygan](https://arxiv.org/abs/0810.0030).

## 9. Required computational certificate and stopping test

The remaining implementation must record:

1. The actual affine refinement, line frames, rank-two \(g_{ij}\), and frame-change identities.
2. Local matrices \(i,p,H\), including their contraction identities.
3. The explicit refinement comparison and its denominator-clearing certificate.
4. The specified scalar Laurent SDR and the composed comparison to its finite complex.
5. An exact first-order solution \(u\) of the transition equation.
6. Every term of \(R\), its normalization \(C_2\), and the exact check \(\delta C_2=0\).
7. The finite projected vector and its deck-character decomposition.

The finite stopping oracle for the full-sign component is to project the certified \(C_2\) into the full-sign Ext² block. These must be cohomology coordinates modulo the image of the finite differential, not raw finite cochain entries. A nonzero exact Ext² coordinate certifies an obstruction. Zero cohomology coordinates certify vanishing of that component alone.

For the fixed algebroid two-jet specified above, the complete second-order existence problem can be tested by parameterizing first-order lifts by finite Ext¹ coordinates \(t\). The projected obstruction \(Q(t)\) has degree at most two. Over an algebraically closed effective coefficient field, its coordinate ideal is the unit ideal exactly when no such second-order lift exists. A solution of \(Q(t)=0\), followed by homotopy back-substitution and direct verification of the transition equations, is a positive certificate.

No value of this projected second-order vector, no Gröbner calculation, and no reconstructed second-order module are claimed in this note.

## 10. Primary sources and precise use

- [Andrea D’Agnolo and Pierre Schapira, *Quantization of complex Lagrangian submanifolds*](https://arxiv.org/abs/math/0506064), Section 3: supplies the algebra-isomorphism and triple-unit descent identities and the corresponding module formalism. Its Lagrangian existence theorem does not establish a quantization of the rank-two bundle considered here.
- [Amnon Yekutieli, *Twisted Deformation Quantization of Algebraic Varieties*](https://arxiv.org/abs/0905.0488): supplies the algebraic twisted-deformation and crossed-groupoid descent setting. It is not used as a theorem forcing this bundle's second-order obstruction to vanish.
- [Paul Bressler, Alexander Gorokhovsky, Ryszard Nest, Boris Tsygan, *Deformations of algebroid stacks*](https://arxiv.org/abs/0810.0030): supplies the DGLA/Maurer–Cartan description of algebroid deformation theory. The specific \(b,T,A\) formulas and character projection above are direct calculations.
- [Wendy Lowen, *Hochschild cohomology, the characteristic morphism and derived deformations*](https://arxiv.org/abs/0707.2602): identifies the characteristic evaluation of a Hochschild deformation class with the obstruction to deforming an object. It supports the evaluation step in comparing ambient lifts; it does not itself compute the present residual.

The equations in this note are a symbolic derivation. The separate finite-RHom certificate and any future exact second-order output must be distinguished from these authored formulas.
