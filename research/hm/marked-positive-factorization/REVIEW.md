# Independent mathematical review

Independent mathematical review dated 2026-10-23.

Reviewed document: `PROOF.md`.

Exact reviewed SHA256: `4063a19ef350dc39550843774020bef7b29784342175553c05acb8caff08ccf9`.

## Verdict

The theorem and all stated corollaries are correct under the document's hypotheses: finite-dimensional complex representations of a finite group, equivariant prescribed maps, and otherwise unrestricted equivariant factors. No correction is required. The complement construction has the asserted exact kernel, the dual obstruction is the transpose with no sign discrepancy, and the unrestricted feasible locus has precisely the stated determinantal description and codimension.

This is a mathematical verification of the universal statement only. No actual HM/source instance, coefficient, matrix, point, or rank has been evaluated. No assertion about the other equations of a positive window follows from this review.

## 1. Necessity and a direct residual factorization

Use the notation of the reviewed document. The elementary conditions are necessary: \(b\gamma=C\) implies \(C(\ker\gamma)=0\), and \(\delta a=D\) implies \(D(X)\subseteq\delta(P)\). Under those conditions, the maps \(c\), \(\bar c\), and \(\Theta\) are well-defined and equivariant. In particular, replacing a lift \(u\in U\) of \(Dx\in T\) changes \(cu\) by an element of \(c(A)=B\).

For any solution, \(qb|_K\) vanishes on \(A\), since \(b|_A=c|_A\). It therefore induces an equivariant map

\[
\beta:K/A\longrightarrow Z/B.
\]

For \(x\in X_0\), choose \(u\in U\) with \(\delta u=Dx\). Then \(a(x)-u\in K\), and its class in \(K/A\) is independent of \(u\). This is precisely the map \(\phi\) obtained from \(\pi a|_{X_0}\) in the proof. Direct computation gives

\[
\beta\phi(x)=qb(a(x)-u)=q(Qx-cu)=\Theta(x).
\]

Thus necessity can also be read as the actual factorization \(\Theta=\beta\phi\) through \(M=K/A\). Its image is a quotient of the subrepresentation \(\operatorname{im}\phi\subseteq M\). Semisimplicity splits that quotient, giving the required embedding of \(\operatorname{im}\Theta\) into \(M\). This independently confirms the proof's kernel argument and the direction of its inclusion.

## 2. Independent sufficiency construction

An independent block decomposition reduces sufficiency to the same residual factorization. Choose equivariant direct sums

\[
U=A\oplus U_T,\qquad K=A\oplus\widetilde M,
\qquad E=T\oplus E_R.
\]

Choose an equivariant lift \(R\subseteq P\) of \(E_R\). Then

\[
P=A\oplus U_T\oplus\widetilde M\oplus R,
\]

where \(\delta|_{U_T}:U_T\to T\) and \(\delta|_R:R\to E_R\) are isomorphisms, and \(\widetilde M\cong M\). Let \(D_T,D_R\) be the two components of \(D\), and define

\[
a_T=(\delta|_{U_T})^{-1}D_T,\qquad
a_R=(\delta|_R)^{-1}D_R,\qquad
H=Q-c|_{U_T}a_T.
\]

Then \(X_0=\ker a_R\) and \(qH|_{X_0}=\Theta\).

An embedding \(\operatorname{im}\Theta\hookrightarrow\widetilde M\) produces equivariant maps \(\phi:X_0\to\widetilde M\) and \(\beta:\widetilde M\to Z/B\) such that

\[
\beta\phi=\Theta,\qquad \ker\phi=\ker\Theta.
\]

Indeed, take \(\phi=j\Theta\) and extend the inverse of \(j\), followed by the inclusion of \(\operatorname{im}\Theta\) into \(Z/B\), from \(j(\operatorname{im}\Theta)\) to an invariant complement in \(\widetilde M\).

Choose \(X=X_0\oplus X_1\). Extend \(\phi\) by zero on \(X_1\) to a map \(t:X\to\widetilde M\). Lift \(\beta\) through \(q\) to an equivariant map \(b_M:\widetilde M\to Z\). Since \(a_R|_{X_1}\) is injective, the formula

\[
b_R(a_Rx_1)=Hx_1\qquad(x_1\in X_1)
\]

defines an equivariant map on \(a_R(X_1)\); extend it to \(R\). The residual map

\[
J=H-b_Mt-b_Ra_R
\]

vanishes on \(X_1\), and its quotient by \(B\) vanishes on \(X_0\). Consequently \(J(X)\subseteq B\). Lift \(J\) through the surjection \(c|_A:A\to B\) to obtain \(a_A:X\to A\).

Define

\[
a=a_A+a_T+t+a_R,
\]

and define \(b\) on the displayed decomposition of \(P\) by \(c|_A,c|_{U_T},b_M,b_R\), respectively. Every map and choice is equivariant. Direct substitution gives

\[
\delta a=D,\qquad b|_U=c,\qquad
ba=J+c|_{U_T}a_T+b_Mt+b_Ra_R=Q.
\]

This independently proves sufficiency without assuming any unproved extension compatibility.

## 3. Exact kernel and the reviewed construction

In equation (7) of the reviewed proof, the two terms lie in complementary subrepresentations of \(P/U\): \(\phi(X_0)\) lies in \(\ker\bar\delta\), and \(\sigma\bar D(X_1)\) lies in the image of a section of \(\bar\delta\). Moreover, \(\bar D|_{X_1}\) is injective because \(\ker\bar D=X_0\). Therefore

\[
\ker\bar a=\ker\phi=\ker\Theta=S_0,
\]

as claimed, including elements initially having both \(X_0\) and \(X_1\) components.

The correction from \(a_1\) to \(a_2\) changes only the \(U\)-component and fixes \(\delta a_2=D\). On \(S_0\), the condition \(\Theta=0\) is exactly the condition that \((D,Q)\) lands in the image of \(r:u\mapsto(\delta u,cu)\). The two lifts \(u_0\) and \(a_2|_{S_0}\) have the same \(\delta\)-image and both lie in \(U\), so their difference really does land in \(A\). Its extension therefore changes neither \(\delta a\) nor \(\pi a\).

Finally, any relation \(u+ax=0\) forces \(x\in S_0\), where \(ca(x)=Qx\). This proves the well-definedness of \(b_0\), not merely its consistency on a chosen decomposition. Extending \(b_0\) to an invariant complement introduces no further constraint. All steps of the original sufficiency proof are valid.

## 4. Duality

The dual problem has \(X'=Z^*,Y'=L^*,P'=P^*,Z'=X^*,L'=Y^*\). Its elementary conditions are exactly the two original elementary conditions in the opposite order.

The identifications

\[
U'=K^\perp,\qquad K'=U^\perp,\qquad
A'=(U+K)^\perp,\qquad
M'\cong(K/A)^*
\]

are correct. For the last identification, restriction \(U^\perp\to K^*\) has kernel \((U+K)^\perp\) and image the functionals annihilating \(A\).

Here \(T^\perp\) is taken in \(L^*\), and

\[
B'=D^*(T^\perp)=\bigl(D^{-1}(T)\bigr)^\perp=X_0^\perp.
\]

The equality uses the finite-dimensional annihilator identity for a preimage. Likewise, the condition defining \(X'_0\) is equivalent to \(z^*c\) vanishing on \(A\), so

\[
X'_0=B^\perp\cong(Z/B)^*,\qquad
Z'/B'\cong X_0^*.
\]

For \(z^*\in B^\perp\), a lift \(\ell\in L^*\) with \(\gamma^*\delta^*\ell=C^*z^*\) exists by that same condition. Evaluation on \(x\in X_0\), using any \(u\in U\) with \(\delta u=Dx\), gives

\[
\langle\Theta'z^*,x\rangle
=z^*(Qx)-\ell(Dx)
=z^*(Qx-cu)
=\langle z^*,\Theta x\rangle.
\]

Thus \(\Theta'=\Theta^*\) under the stated identifications. The reservoir dualizes to \(M^*\), and the image representation dualizes as well; no irreducible multiplicity or sign is lost.

## 5. Minimal quotient-image claim

For every solution there is an exact sequence

\[
0\longrightarrow\bar a(X_0)\longrightarrow
\operatorname{im}\bar a\xrightarrow{\bar\delta}
\operatorname{im}\bar D\longrightarrow0.
\]

Its kernel is exactly \(\bar a(X_0)\): if \(\bar\delta\bar a(x)=0\), then \(\bar D(x)=0\), hence \(x\in X_0\). Semisimplicity makes multiplicities additive in this sequence. Necessity gives \(\operatorname{im}\Theta\) as a direct summand of \(\bar a(X_0)\), proving the lower bound coordinatewise. Construction (7), or the independent construction above, has \(\bar a(X_0)\cong\operatorname{im}\Theta\) and attains equality simultaneously for all irreducibles.

## 6. Exact unrestricted feasible locus

The affine map \(F\) is surjective: an arbitrary equivariant map \(X_0\to Z/B\) can first be lifted to \(Z\), then extended to \(X\). The constant term in \(F\) does not change this property.

Over the complex numbers, Schur's lemma identifies equivariant maps between isotypic summands with ordinary matrices on multiplicity spaces. The multiplicity of \(S\) in \(\operatorname{im}\Theta\) is therefore exactly the rank of its \(p_S\times n_S\) matrix. The theorem yields precisely the determinantal rank conditions in (12), with no extra equations or existential conditions.

For \(r_S=\min(n_S,p_S,m_S)\), the rank-at-most-\(r_S\) locus is closed by minors and irreducible: the multiplication map from the two matrix spaces of sizes \(p_S\times r_S\) and \(r_S\times n_S\) maps onto the entire locus. Its dense rank-\(r_S\) stratum has dimension \(r_S(n_S+p_S-r_S)\). This includes \(r_S=0\) and the full-matrix-space cases. Its codimension is consequently \((n_S-r_S)(p_S-r_S)\).

An affine section of \(F\) identifies the preimage with the product of its affine kernel and these determinantal varieties. Nonemptiness, closedness, irreducibility, and the stated sum of codimensions all follow. These assertions concern the unrestricted space \(H=\operatorname{Hom}_G(X,Z)\), not an arbitrary constrained subspace.

## 7. Symmetric curry, degenerations, and scope

The currying identification and the inclusion using \(\operatorname{Sym}^2(V^*)\subseteq V^*\otimes V^*\) are valid and equivariant. If only \(Q\) is restricted to that subspace while the unknown factors remain exactly those in (1), taking the intersection in (13) is the exact feasible-target condition. The document correctly does not transfer nonemptiness, irreducibility, or the unrestricted codimension formula to this section. It also correctly makes no claim about extra symmetry or other restrictions on the factors themselves.

The cases \(\delta\gamma=0\), \(K=U\), \(M=0\), and \(\gamma=0\) are the stated substitutions into the theorem, with the elementary conditions retained. In particular, when \(U\subseteq K\), one has \(B=c(U)=C(Y)\) and \(X_0=\ker D\), exactly as used.

The theorem is a complete universal resolution of the marked factorization slice. Its hypotheses do not establish that a particular source problem realizes this slice with unrestricted equivariant factors, nor do they resolve equations involving other arrows. The document states these limits accurately.
