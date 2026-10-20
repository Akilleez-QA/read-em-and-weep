# Explicit total Čech–de Rham lift of the scalar two-cocycle

## Result and scope

On the original cover and with the Alexander–Whitney conventions of PR16static, the regular total degree-two cochain

\[
\beta=\lambda(\eta_1\eta_2+\eta_3\eta_4),\qquad
\eta_i=a_i\omega_i+q_i,
\]

is closed and lifts the chosen scalar Čech cocycle
\(b=\lambda(q_1\smile q_2+q_3\smile q_4)\). Its degree-(1,1) component is exactly \(\iota_T\omega\), for PR16's derivation cochain \(T\) and \(\omega=\omega_1\wedge\omega_2+\omega_3\wedge\omega_4\).

This is a direct universal cochain calculation, not a period comparison. In particular, it does **not** identify the central period of the given algebroid with \(\pm h[\beta]\), establish a comparison to central connective data, or compute a module obstruction. No rational functions were evaluated or differentiated, and no finite-model or jet products were used.

Source: `https://github.com/Akilleez-QA/read-em-and-weep/blob/c8aec970fd65a105f39f4e8aeb8a17f0f0053f89/research/hm/second-order-algebroid.md`, Sections 1–4. All products below are symbolic cochain products in the declared original-cover complex.

## 1. Conventions and hypotheses

Write \(C^{p,q}=\check C^p(\mathcal U,\Omega_X^q)\), with

\[
D=\delta+(-1)^p d,\qquad
u v=(-1)^{q p'}u\smile v
\quad(u\in C^{p,q},\ v\in C^{p',q'}),
\]

where the form parts are wedged. This total product is associative and \(D\) obeys the total-degree Leibniz rule; it need not be strictly graded commutative on an ordinary ordered nerve.

The input consists of the regular zero-cochains \(a_i\), regular scalar one-cocycles \(q_i\), and global closed one-forms \(\omega_i\), with

\[
\delta q_i=0,\quad \delta\omega_i=0,\quad
\delta a_i=V_iq_i,\quad dq_i=(\delta a_i)\omega_i,
\quad da_i\wedge\omega_i=0,\quad d\omega_i=0.
\]

Here \(\delta q_i=0\) is the source's stated rational-cocycle property, not a consequence of the derivative-primitive relation alone. Regularity is on each prescribed chart or intersection, as in that source; no global regularity of the chart coefficients is asserted.

## 2. Closed degree-one lifts

The components of \(\eta_i\) have bidegrees \((0,1)\) and \((1,0)\). Consequently

\[
D\eta_i=d(a_i\omega_i)+\delta(a_i\omega_i)-dq_i+\delta q_i=0.
\]

The minus sign on \(dq_i\) is essential. Thus each \(\eta_i\) is an explicit regular total de Rham lift of \(q_i\).

## 3. Expansion and contraction identity

For \((i,j)=(1,2)\) or \((3,4)\), put \(\omega_{ij}=\omega_i\wedge\omega_j\). The total product expands as

\[
\eta_i\eta_j=
 a_i a_j\omega_{ij}
 - (a_i\smile q_j)\omega_i
 + (q_i\smile a_j)\omega_j
 +q_i\smile q_j.
\]

In particular, \(\beta=\zeta+\alpha+b\), with

\[
\begin{aligned}
\zeta&=\lambda(a_1a_2\omega_{12}+a_3a_4\omega_{34}),\\
\alpha&=\lambda[-(a_1\smile q_2)\omega_1
 +(q_1\smile a_2)\omega_2
 -(a_3\smile q_4)\omega_3
 +(q_3\smile a_4)\omega_4],\\
b&=\lambda(q_1\smile q_2+q_3\smile q_4).
\end{aligned}
\]

The asymmetric endpoint evaluation is literal: on \(U_u\cap U_v\),
\((a_i\smile q_j)_{uv}=a_{i,u}q_{j,uv}\) and
\((q_i\smile a_j)_{uv}=q_{i,uv}a_{j,v}\). They must not be silently replaced by common-endpoint products.

Since \(\iota_{V_i}\omega_{ij}=\omega_j\) and
\(\iota_{V_j}\omega_{ij}=-\omega_i\), PR16's

\[
T=\lambda[(a_1\smile q_2)V_2+(q_1\smile a_2)V_1
 +(a_3\smile q_4)V_4+(q_3\smile a_4)V_3]
\]

satisfies exactly \(\boxed{\alpha=\iota_T\omega}\).

## 4. All four cocycle equations

For one ordered pair \((i,j)\), suppress the common scalar \(\lambda\). The ordinary Čech Leibniz rule gives

\[
\delta(a_i a_j)=(\delta a_i)\smile a_j+a_i\smile\delta a_j.
\]

Using only the declared differential relations and wedge signs,

\[
\begin{aligned}
d[-(a_i\smile q_j)\omega_i+(q_i\smile a_j)\omega_j]
&=[a_i\smile\delta a_j+(\delta a_i)\smile a_j]\omega_{ij}\\
&=\delta(a_i a_j\omega_{ij}).
\end{aligned}
\]

The terms containing \(da_i\wedge\omega_i\) or \(da_j\wedge\omega_j\) vanish. Meanwhile,

\[
\begin{aligned}
\delta[-(a_i\smile q_j)\omega_i+(q_i\smile a_j)\omega_j]
&=-((\delta a_i)\smile q_j)\omega_i
 -(q_i\smile\delta a_j)\omega_j\\
&=-d(q_i\smile q_j).
\end{aligned}
\]

Here \(\delta(q_i\smile a_j)=-q_i\smile\delta a_j\), whereas the ordinary de Rham differential of scalar coefficient products has no such Čech sign. Finally,

\[
d(a_i a_j\omega_{ij})=0,\qquad
\delta(q_i\smile q_j)=0.
\]

Adding the two pairs proves

\[
\boxed{d\zeta=0,\quad\delta\zeta=d\alpha,
\quad\delta\alpha=-db,\quad\delta b=0.}
\]

These are precisely the four bidegree components of \(D\beta=0\). Projection of the total complex onto its form-degree-zero quotient is a chain map; it sends \(\beta\) to \(b\). Thus the result is a lift to total de Rham cohomology on this cover, not merely an informal Hodge-component assignment.

## 5. Ordered-nerve commutativity homotopy and repeated factors

For any \(i,j\), define a scalar Čech one-cochain by an ordinary product **on the same double overlap**:

\[
c_{ij,uv}=q_{i,uv}q_{j,uv}.
\]

This is not the Čech cup product, whose degree would be two. The scalar cocycle identities imply directly on a triple overlap

\[
\delta c_{ij}=-(q_i\smile q_j+q_j\smile q_i).
\]

The \((0,2)\) component of \(\eta_i\eta_j+\eta_j\eta_i\) vanishes. Its \((1,1)\) component is

\[
q_j(\delta a_i)\omega_i+q_i(\delta a_j)\omega_j=dc_{ij}.
\]

Since \(Dc_{ij}=\delta c_{ij}-dc_{ij}\), the exact chain identity is

\[
\boxed{\eta_i\eta_j+\eta_j\eta_i=-Dc_{ij}.}
\]

In particular, repeated odd factors need not vanish as ordinary Alexander–Whitney cochains:

\[
\eta_i^2=-\tfrac12D c_{ii},\qquad
q_i\smile q_i=-\tfrac12\delta c_{ii},
\quad c_{ii,uv}=q_{i,uv}^2.
\]

They vanish in cohomology. In a strictly supercommutative tensor model such vanishings and independent-factor anticommutation can instead hold on the chain level. No such strict identification is assumed here.

For example, the antisymmetrized total lift

\[
\beta_{\rm anti}=\tfrac\lambda2
 (\eta_1\eta_2-\eta_2\eta_1+\eta_3\eta_4-\eta_4\eta_3)
\]

obeys the explicit ordinary-nerve comparison

\[
\beta_{\rm anti}-\beta=\tfrac\lambda2D(c_{12}+c_{34}).
\]

Likewise, for PR16's exact scalar representative,

\[
\Pi_{\rm AW}=-\tfrac18(Q_{12}-Q_{21}+Q_{34}-Q_{43}),
\quad Q_{ij}=q_i\smile q_j,
\]

and its shorter representative \(\Pi_{\rm short}=-\tfrac14(Q_{12}+Q_{34})\),

\[
\boxed{\Pi_{\rm AW}-\Pi_{\rm short}
=-\tfrac18\delta(c_{12}+c_{34}).}
\]

This supplies the missing coboundary whenever these two representatives are compared on the ordinary nerve.

## 6. Polarization and the precise meaning of the lifted Π

There is already an exact total-cochain identity

\[
\tfrac12\eta_i\omega_i=\tfrac12q_i\omega_i
=-\tfrac12\omega_i\eta_i.
\]

Both omitted \((0,2)\) pieces contain \(\omega_i\wedge\omega_i=0\); the last minus sign is the total-product sign for a form crossing a Čech one-cochain. Thus the source's polarization class is represented by

\[
\theta_i=\tfrac12[\eta_i][\omega_i].
\]

Define abstract degree-one cohomology classes \(b_i=-[\eta_i]/2\), using the subscript to distinguish them from the scalar two-cocycle \(b\). Then

\[
\theta=\sum_i[\omega_i]b_i,
\qquad
[\beta]=4\lambda(b_1b_2+b_3b_4).
\]

Define the total de Rham lift

\[
\Pi_{\mathrm{dR}}:=-(b_1b_2+b_3b_4)
=-\tfrac14([\eta_1\eta_2]+[\eta_3\eta_4]).
\]

Then

\[
\boxed{[\beta]=-4\lambda\Pi_{\mathrm{dR}},}
\]

and its form-degree-zero edge is the original
\(\Pi\in H^2(X,\mathcal O_X)\) from PR16. Equivalently, the cochain
\(-\tfrac14(\eta_1\eta_2+\eta_3\eta_4)\) lifts \(\Pi_{\rm short}\), while
\(-\tfrac18(\eta_1\eta_2-\eta_2\eta_1+\eta_3\eta_4-\eta_4\eta_3)\) lifts \(\Pi_{\rm AW}\); their difference is \(-\tfrac18D(c_{12}+c_{34})\).

For the abstract exterior-algebra contraction that satisfies
\(\iota_{V_k}[\omega_i]=\delta_{ki}\), \(\iota_{V_k}b_i=0\), and
\(\iota_{V_i\wedge V_j}=\iota_{V_j}\iota_{V_i}\), one gets

\[
\tfrac12\iota_\pi(\theta^2)=-(b_1b_2+b_3b_4)=\Pi_{\mathrm{dR}}.
\]

The sign follows from
\((\omega_i b_i)(\omega_j b_j)=-\omega_i\omega_j b_i b_j\), and the factor two in the cross terms of \(\theta^2\) cancels its prefactor \(1/2\). Terms with repeated \(\omega_i\) vanish; odd repeated \(b_i\) vanish in cohomology, with the explicit homotopy above if chain representatives are used.

**Type and contraction caution.** PR16's original \(\Pi\) is an \(H^2(\mathcal O_X)\) class, whereas \([\beta]\) is a total de Rham class. Writing \([\beta]=-4\lambda\Pi\) without the de Rham subscript is valid only after explicitly declaring that \(\Pi\) now denotes this chosen de Rham lift. The abstract contraction killing the \(b_i\) is not contraction applied to the actual total cochains: for example \(\iota_{V_i}\eta_i=a_i\), not zero. Ordinary geometric contraction does not in general commute with \(D\). Nothing in this calculation establishes a canonical period comparison by replacing that contraction with the abstract one.

For \(\lambda=15/4\), the explicit identity specializes to \([\beta]=-15\Pi_{\mathrm{dR}}\), with scalar edge \([b]=-15\Pi\), agreeing with PR16's first-order normalization. The actual central-period sign and comparison remain unproved.
