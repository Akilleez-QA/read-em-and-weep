# What second-jet symmetry leaves in the complete raw obstruction

## Result

In the physical row convention, the accepted complete raw representative admits the exact decomposition

\[
R_{\rm raw}=\Omega+Q_2(L,U;H^0,J^0)+Q_4(L,U)
             +E_p(s_{{\rm raw},q})+E_q(s_{{\rm raw},p}). \tag{1}
\]

Here \(Q_2\) and \(Q_4\) are given explicitly below. The decomposition retains all seven kinetic terms, all three gerbe terms before their proved cancellation, both curvature corrections, and both raw-scalar derivative terms. It uses determinant one, rank-two identities and the product rule only. It does not evaluate the physical source.

Consequently the cross-Gram symmetry criterion \(J^t S H=(J^t S H)^t\) kills precisely \(\Omega\) in this formula. Even after that criterion is established on every actual overlap, the exact remaining global obligation is

\[
Q_2+Q_4+E_p(s_{{\rm raw},q})+E_q(s_{{\rm raw},p})=\delta P \tag{2}
\]

for a regular, correctly transported row-End edge cochain \(P\) on the full common cover. An equivalent total-resolution primitive would also suffice. No such source identity is supplied by the symmetry theorem or by the accepted raw/N14 comparison. Equation (2), rather than an unspecified “other terms” caveat, is the missing lemma.

An invented determinant-one two-jet control has \(H^0=J^0=0\), hence symmetric cross-Gram matrix, but \(Q_4=-h/8\ne0\). This disproves universal pointwise elimination of the remainder from symmetry alone. It is not a counterexample to a global boundary theorem, and its scalar choices are not the pinned raw transgression.

## 1. Public inputs and conventions

The complete source is the frozen PR89 compiler and its RS/BI proofs:

- [Compiler, `Source.k`, `mu`, `mu2`, `E`, `residual`](https://github.com/Akilleez-QA/read-em-and-weep/blob/e93cf712f9da4926a8450cc870ed45a7bfc379ab/research/codex-swarm/scalar-compiler/compiler.py)
- [RS full-source application, especially §§3–5](https://github.com/Akilleez-QA/read-em-and-weep/blob/e93cf712f9da4926a8450cc870ed45a7bfc379ab/research/codex-swarm/full-source-application/PROOF.md)
- [BI raw/N14 comparison, especially §§1–5 and7](https://github.com/Akilleez-QA/read-em-and-weep/blob/e93cf712f9da4926a8450cc870ed45a7bfc379ab/research/codex-swarm/source-boundary-analysis/PROOF.md)

For the second-jet reduction and exact symmetry criterion:

- [Second-jet survivor, §1 equation(A)](https://github.com/Akilleez-QA/read-em-and-weep/blob/10810ee877fdaf291399198ad60d7dd0c316a42d/research/hm/null-proof-foundations/m0-second-jet-survivor.md)
- [PR79 source-second-jet degeneracy certificate, §§1,3,5](https://github.com/Akilleez-QA/read-em-and-weep/blob/5df68750f766b18a746e50bff662b09829225ab1/research/hm/null-support-certificates/source-second-jet-degeneracy-certificate.md)
- [PR79 abstract tests](https://github.com/Akilleez-QA/read-em-and-weep/blob/5df68750f766b18a746e50bff662b09829225ab1/research/hm/null-support-certificates/test_source_second_jet_degeneracy.py)

The last two inputs were read at their own immutable commit, not falsely attributed to the PR89 tree. The PR79 tests'144 single-slot basis pairs verify the bilinear cross-Gram identity; they do not address the complete raw remainder.

Use coordinate indices1,2,3,4, so the compiler's0,1,2,3 are shifted by1. Put \(p=(1,2)\), \(q=(3,4)\). On a fixed increasing cover triple \((i,j,k)\), write

\[
A=g_{ij},\quad B=g_{jk},\quad G=g_{ik}=BA.
\]

Every derivative is the physical moving-frame derivative. All matrices below are expressed in the first row frame:

\[
L_a=A^{-1}V_aA,\quad U_a=A^{-1}B^{-1}(V_aB)A,
\]
\[
H_{ab}=A^{-1}V_aV_bA,\quad
J_{ab}=A^{-1}B^{-1}(V_aV_bB)A.
\]

Thus \(L_a,U_a\) are traceless and the current of the composite transition is \(L_a+U_a\). Write \(X^0=X-\operatorname{tr}(X)I/2\), and define

\[
K_{ab}(X)=\tfrac14[X_a,X_b],\qquad
c_{ab}=\tfrac14\operatorname{tr}(U_aL_b-U_bL_a).
\tag{3}
\]

The source's normalized first curvature is \(C_{ab}=\tfrac12(U_aL_b-U_bL_a)\), so \(c_{ab}=\operatorname{tr}(C_{ab})/2\). In particular \(k_{r,ik}=K_r(L+U)\).

Let the signed complementary pairs be

\[
\mathcal S=\{(13,24,+1),(14,23,-1),(23,14,-1),(24,13,+1)\}.
\]

## 2. Gerbe terms cancel with the explicit parts of both Fk corrections

Let \(\mathcal K\) denote the seven-term kinetic expression before left normalization and trace projection. The compiler's complete baseline is

\[
M_0=G^{-1}\mathcal K-b_pK_q(L+U)-b_qK_p(L+U)-b_pb_q I.
\]

Since the two \(K\)'s are traceless and \(F_r=b_r-c_r\), the complete five-term raw representative becomes

\[
R_{\rm raw}=(G^{-1}\mathcal K)^0-c_qK_p(L+U)-c_pK_q(L+U)
 +E_p(s_{{\rm raw},q})+E_q(s_{{\rm raw},p}). \tag{4}
\]

This is an algebraic cancellation, not permission to start from an incomplete baseline. The scalar \(-b_pb_qI\) disappears only under trace projection. The two \(-bK\) terms cancel the corresponding \(+bK\) parts of \(Fk\). The raw scalar still includes its own gerbe representative correction, as prescribed in BI equation(7); none of its contributions to \(E\) has been deleted.

## 3. Normalize all seven kinetic terms

For a pair \(r=(a,b)\), put

\[
\nabla^H_dK_r(L)=\tfrac14\bigl([H_{da}-L_dL_a,L_b]
                              +[L_a,H_{db}-L_dL_b]\bigr),
\tag{5}
\]

and define \(\nabla^J_dK_r(U)\) by replacing \((H,L)\) with \((J,U)\).

The notation on the B side is important: \(\nabla^J\) is the transported derivative of the untransported B-side current. It is not ordinary differentiation of \(U\). Explicitly,

\[
A^{-1}V_d(B^{-1}V_aB)A=J_{da}-U_dU_a,
\]

whereas \(V_dU_a=J_{da}-U_dU_a+[U_a,L_d]\).

For \(r=(a,b)\) and the other pair \(s\), define

\[
\begin{aligned}
T_{r|s}=\tfrac12\{&
(U_aK_s(U)+\nabla^J_aK_s(U))L_b
-(U_bK_s(U)+\nabla^J_bK_s(U))L_a\\
&+U_a(L_bK_s(L)+\nabla^H_bK_s(L))
-U_b(L_aK_s(L)+\nabla^H_aK_s(L))\}.
\end{aligned}\tag{6}
\]

The first line is exactly \(G^{-1}\mu_r(Bk_s(B),A)\); the second is \(G^{-1}\mu_r(B,Ak_s(A))\). Hence the product rule gives the full normalized seven-term expression

\[
G^{-1}\mathcal K=K_p(U)K_q(L)+K_q(U)K_p(L)
 +T_{p|q}+T_{q|p}+\tfrac14\sum_{(ab,cd,\epsilon)\in\mathcal S}
 \epsilon J_{ab}H_{cd}. \tag{7}
\]

No permutation of matrix factors or assumption of cross-edge commutativity enters this normalization.

## 4. A rank-two cancellation inside the differentiated k terms

Determinant one supplies

\[
\operatorname{tr}H_{ab}=\operatorname{tr}(L_aL_b),\qquad
\operatorname{tr}J_{ab}=\operatorname{tr}(U_aU_b).
\]

For traceless2×2 matrices, \(XY+YX=\operatorname{tr}(XY)I\). Therefore

\[
H_{da}-L_dL_a=H^0_{da}-\tfrac12[L_d,L_a].
\]

Define the traceless expression

\[
N_{d|ab}(X,Y)=\tfrac14\bigl([Y_{da},X_b]+[X_a,Y_{db}]\bigr), \tag{8}
\]

where \(Y=H^0\) or \(J^0\). Substitution in(5), then the Jacobi derivation identity, gives

\[
\nabla_dK_{ab}(X)=N_{d|ab}(X,Y)-\tfrac12[X_d,K_{ab}(X)].
\]

Consequently

\[
X_dK_{ab}(X)+\nabla_dK_{ab}(X)
=N_{d|ab}(X,Y)+\tfrac12\operatorname{tr}(X_dK_{ab}(X))I. \tag{9}
\]

This removes the nested quartic commutators from each differentiated transition-times-k term. Taking tracefree parts of(6) gives a clean split

\[
T_{r|s}^0=T^{(2)}_{r|s}+T^{(4)}_{r|s},
\]

with

\[
\begin{aligned}
T^{(2)}_{r|s}=\tfrac14\{&[N_{a|s}(U,J^0),L_b]-[N_{b|s}(U,J^0),L_a]\\
 &+[U_a,N_{b|s}(L,H^0)]-[U_b,N_{a|s}(L,H^0)]\},
\end{aligned}\tag{10}
\]

and the purely current term

\[
\begin{aligned}
T^{(4)}_{r|s}=\tfrac14\{&
\operatorname{tr}(U_aK_s(U))L_b-\operatorname{tr}(U_bK_s(U))L_a\\
&+\operatorname{tr}(L_bK_s(L))U_a-\operatorname{tr}(L_aK_s(L))U_b\}.
\end{aligned}\tag{11}
\]

The superscript2 means linear dependence on the displayed second jets; it does not say the term has total derivative order2. All terms here have total derivative order4.

## 5. Explicit Q2 and Q4

The survivor identity gives

\[
\left(\tfrac14\sum\epsilon J_{ab}H_{cd}\right)^0
=\Omega+\tfrac18\sum\epsilon\{
\operatorname{tr}(U_aU_b)H^0_{cd}
+\operatorname{tr}(L_cL_d)J^0_{ab}\}, \tag{12}
\]

where

\[
\Omega=\tfrac18\sum\epsilon[J_{ab},H_{cd}].
\]

One can already define \(Q_2\) as the last sum in(12) plus both expressions(10). It simplifies further. The rank-two identity

\[
[[X,Y],Z]=2\{\operatorname{tr}(YZ)X-\operatorname{tr}(XZ)Y\}
\]

eliminates the double brackets in(10). The resulting compact expression is

\[
\begin{aligned}
Q_2=\tfrac18\sum_{(ab,cd,\epsilon)\in\mathcal S}\epsilon\Bigl\{&
 [\operatorname{tr}(U_aU_b)+\operatorname{tr}(U_aL_b)+\operatorname{tr}(U_bL_a)]H^0_{cd}\\
&-\operatorname{tr}(H^0_{cd}U_a)L_b-\operatorname{tr}(H^0_{cd}U_b)L_a\\
&+[\operatorname{tr}(L_cL_d)+\operatorname{tr}(U_cL_d)+\operatorname{tr}(U_dL_c)]J^0_{ab}\\
&-\operatorname{tr}(J^0_{ab}L_c)U_d-\operatorname{tr}(J^0_{ab}L_d)U_c
\Bigr\}.
\end{aligned}\tag{13}
\]

The remaining purely quartic-current expression is

\[
\begin{aligned}
Q_4={}&\tfrac12\{[K_p(U),K_q(L)]+[K_q(U),K_p(L)]\}\\
&+T^{(4)}_{p|q}+T^{(4)}_{q|p}
-c_qK_p(L+U)-c_pK_q(L+U).
\end{aligned}\tag{14}
\]

Equations(4), (7), (10)–(14) prove(1). In particular the reduction does more than rename the seven kinetic terms: it cancels the explicit gerbe/Fk pieces, removes scalar second-jet traces, and eliminates nested current commutators and double current/jet brackets.

The two retained scalar terms are exactly

\[
E_{ab}(t)_{ijk}=\tfrac12\{(V_at_{jk})L_b-(V_bt_{jk})L_a
 +(V_bt_{ij})U_a-(V_at_{ij})U_b\}. \tag{15}
\]

Their arguments in(1) are the complete BI raw transgression, with all four split-connection blocks, both mixed trace terms, transported infinity connections, physical frame derivatives, and the raw edge gerbe correction. Equation(1) makes no claim that these scalar derivatives are independent of \(L,U,H,J\) for the actual source. They may participate in a source-specific cancellation; proving that cancellation is part of(2).

## 6. What the symmetry criterion proves globally, and what it does not

The PR79 criterion is exact: form4×3 arrays from the traceless components of the four ordered cross-jets in the basis \((h,e,f)\), and use the fixed signed complementary matrix \(S\). Then

\[
J^t S H\text{ symmetric}\quad\Longleftrightarrow\quad\Omega=0.
\]

This is a pointwise matrix statement on the complete, correctly transported arrays. It is neither a boundary statement nor an assertion about \(Q_2,Q_4,E\).

RS and BI give \(\delta R_{\rm raw}=0\) and equality of its global class with the accepted N14 representative. Without symmetry, equation(1) only gives

\[
\delta(Q_2+Q_4+E_p+E_q)=-\delta\Omega.
\]

There is no reason here to call either side a closed cochain independently. If actual owner-complete cross-Gram symmetry is proved, \(\Omega=0\) and the remainder is closed. Since the accepted common cover is acyclic, its global class is zero precisely when a regular edge cochain \(P\) as in(2) exists. Correct restriction compatibility, row transport, alternating extension and legal-overlap regularity are part of this statement.

BI's identity \(E_r(\delta f)=\delta B_r(f)\) proves independence of the global class from the scalar primitive. It does not set \(E_r(s_{{\rm raw},s})\) to zero: the raw scalar has \(\delta s_{{\rm raw},s}=F_s\), not generally0, and is not asserted to be a scalar coboundary. Likewise the comparison \(s_{N14}-s_{\rm raw}=\delta f\) concerns their difference only.

A source proof of(2) can use additional vertex-connection data; the older no-go for universal transition-local two-jet boundaries does not forbid that. A global primitive need not satisfy the detector's finite cutoff. A direct finite-cutoff calculation, in contrast, needs its own domain certificate. Merely observing local nonzero \(Q_4\), or even nonzero \(\Omega\), gives no global obstruction verdict.

## 7. Tiny formal countercontrol and verification

Use the standard traceless matrices \(h=\operatorname{diag}(1,-1)\), \(e=E_{12}\), \(f=E_{21}\). Set

\[
(L_1,L_2,L_3,L_4)=(h,e,f,0),\qquad
(U_1,U_2,U_3,U_4)=(0,0,0,h),\qquad H^0=J^0=0.
\]

These are consistent determinant-one two-jets: at the origin take the formal germs

\[
A=\exp(x_1h+x_2e+x_3f),\qquad B=\exp(x_4h).
\]

Indeed their normalized symmetric Hessians are \(\{L_a,L_b\}/2\) and \(\{U_a,U_b\}/2\), which are central. Here \(\Omega=Q_2=c_p=c_q=0\). All terms in(14) vanish except the contribution \(-\operatorname{tr}(L_3K_p(L))U_4/4\), so

\[
Q_4=-h/8.
\]

If one additionally chooses the scalar derivatives on the entering edges \((i,j)\), \((j,k)\) to vanish, both operators(15) vanish at that point. The scalar first-order equation on this one triple can still be met by choosing the third edge to satisfy \(s_{ik}=s_{jk}+s_{ij}-F\). This establishes only universal pointwise insufficiency of the symmetry criterion plus a first-order scalar equation. Those scalar choices are not claimed to be the actual raw transgression; the example is not a source specialization, a global cocycle construction, or a nonzero cohomology class. Even a nonzero pointwise Čech cocycle can be a boundary.

`test_current_remainder.py` uses only invented rational2×2 matrices and Python's standard library. Its four tests verify:

1. The normalized derivative identity(9), for both current families.
2. The equality of(13) with(10) plus the trace-jet part of(12).
3. The complete seven-term reduction(1), omitting only identical opaque E terms on both sides, and a wrong-sign curvature-correction negative control.
4. The sparse \(\Omega=0,Q_4=-h/8\) control.

Each of the first three tests uses eight invented inputs; all four pass normally and with `python -O`. The companion `test_gerbe_cancellation.py` supplies separate exact controls for(4). These checks supplement the displayed algebraic proof; finite examples alone are not offered as the universal proof. No physical model, source polynomial, coefficient, jet, fiber, owner scan, or physical runtime was executed.
