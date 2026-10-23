# An exact criterion for equivariant marked factorization

## Status and scope

This is a standalone universal linear-algebra result. It does not evaluate any actual HM/source-instance coefficient, matrix, point, or rank. It neither solves the other equations in a positive window nor asserts that an actual HM target violates or satisfies the criterion. The result is intended for independent review before any source-specific use.

All representations below are finite-dimensional complex representations of a finite group \(G\), and all maps are \(G\)-equivariant. No additional constraints on the two unknown maps are imposed unless explicitly stated. In particular, further symmetry, grading, decomposability, or module-homomorphism requirements on the factors themselves would need separate treatment.

## 1. The marked factorization problem

Fix representations \(X,Y,P,Z,L\) and maps
\[
\gamma:Y\longrightarrow P,\qquad
\delta:P\longrightarrow L,\qquad
C:Y\longrightarrow Z,\qquad
D:X\longrightarrow L,\qquad
Q:X\longrightarrow Z.
\]
Seek maps
\[
a:X\longrightarrow P,\qquad b:P\longrightarrow Z
\]
satisfying
\[
\delta a=D,\qquad b\gamma=C,\qquad ba=Q. \tag{1}
\]

Two necessary conditions are
\[
\ker\gamma\subseteq\ker C,\qquad
\operatorname{im}D\subseteq\operatorname{im}\delta. \tag{2}
\]
If the first holds, put \(U=\operatorname{im}\gamma\), and let
\(c:U\to Z\) be the unique induced map satisfying \(c\gamma=C\).
The condition \(b\gamma=C\) is then equivalent to \(b|_U=c\).

Assume (2), and define
\[
K=\ker\delta,\quad A=U\cap K,\quad B=c(A),\quad
E=\operatorname{im}\delta,\quad T=\delta(U),
\]
\[
X_0=D^{-1}(T),\qquad M=K/A.
\]
Write \(q:Z\to Z/B\) for the quotient map. There is a unique induced map
\[
\bar c:T\longrightarrow Z/B,\qquad
\bar c(\delta u)=q(cu).
\]
It is well-defined because the kernel of \(\delta|_U\) is \(A\), whose image under \(c\) is \(B\).

The **marked obstruction map** is
\[
\Theta:X_0\longrightarrow Z/B,\qquad
\Theta=qQ|_{X_0}-\bar cD|_{X_0}. \tag{3}
\]
Equivalently, for \(x\in X_0\), choose any \(u\in U\) with \(\delta u=Dx\); then
\[
\Theta(x)=Qx-cu\pmod B.
\]
The result is independent of the choice of \(u\).

## 2. Exact criterion

**Theorem.** Equation (1) has a solution if and only if (2) holds and there is a \(G\)-equivariant embedding
\[
\operatorname{im}\Theta\hookrightarrow M=\ker\delta/(\ker\delta\cap\operatorname{im}\gamma). \tag{4}
\]
Equivalently, for each irreducible representation \(S\) of \(G\),
\[
\operatorname{mult}_S(\operatorname{im}\Theta)
\leq
\operatorname{mult}_S(M). \tag{5}
\]
Thus the criterion involves only the prescribed data, not an existential choice of either factor.

### Splittings used in the proof

Finite-dimensional complex representations of a finite group are semisimple. In particular, invariant subspaces have invariant complements, and equivariant surjections have equivariant linear sections. These statements can also be obtained directly by averaging any linear projection or section over \(G\). Accordingly:

- A map from an invariant subspace can be extended equivariantly by setting it to zero on an invariant complement.
- A map into the image of an equivariant map can be lifted equivariantly by composing with an equivariant section onto that image.

Every lift and extension below uses precisely these facts.

### Necessity

Suppose \(a,b\) satisfy (1). Conditions (2) follow immediately. Let \(\pi:P\to P/U\) be the quotient map. The map \(\delta\) induces a surjection
\[
\bar\delta:P/U\longrightarrow E/T.
\]
Its kernel is
\[
\ker\bar\delta=(K+U)/U\cong K/A=M. \tag{6}
\]
For \(x\in X_0\), the element \(\pi a(x)\) belongs to this kernel because \(\delta a(x)=Dx\in T\). Hence \(\pi a|_{X_0}\) defines an equivariant map
\[
\phi:X_0\longrightarrow M.
\]
If \(x\in\ker\phi\), then \(a(x)\in U\). Therefore
\[
Qx=ba(x)=ca(x),\qquad \delta a(x)=Dx,
\]
which implies \(\Theta(x)=0\). Thus \(\ker\phi\subseteq\ker\Theta\), and the rule
\[
\phi(x)\longmapsto\Theta(x)
\]
defines an equivariant surjection \(\operatorname{im}\phi\to\operatorname{im}\Theta\). Semisimplicity splits this surjection. Since \(\operatorname{im}\phi\subseteq M\), condition (4) follows.

### Sufficiency

Assume (2) and choose an equivariant embedding
\(j:\operatorname{im}\Theta\hookrightarrow M\).
Set
\[
\phi=j\Theta:X_0\longrightarrow M,\qquad
S_0=\ker\Theta=\ker\phi.
\]
Regard \(M\) as the kernel in (6). Choose an invariant complement
\[
X=X_0\oplus X_1.
\]
Let \(\bar D:X\to E/T\) be the composite of \(D\) with the quotient. Its kernel is exactly \(X_0\), so \(\bar D|_{X_1}\) is injective. Choose an equivariant section \(\sigma:E/T\to P/U\) of \(\bar\delta\), and define
\[
\bar a(x_0+x_1)=\phi(x_0)+\sigma\bar D(x_1).
\tag{7}
\]
Then \(\bar\delta\bar a=\bar D\).

Importantly, this construction does not impose an uncontrolled kernel condition outside \(X_0\). If \(\bar a(x_0+x_1)=0\), applying \(\bar\delta\) gives \(\bar D(x_1)=0\). Injectivity on \(X_1\) implies \(x_1=0\), after which \(\phi(x_0)=0\). Conversely, \(S_0\) plainly maps to zero. Therefore
\[
\ker\bar a=S_0\subseteq X_0. \tag{8}
\]

Choose an equivariant section \(\tau:P/U\to P\) of \(\pi\), and put \(a_1=\tau\bar a\). Since \(\bar\delta\bar a=\bar D\), the discrepancy \(\delta a_1-D\) takes values in \(T\). Choose an equivariant section \(s:T\to U\) of \(\delta|_U\), and put
\[
a_2=a_1-s(\delta a_1-D).
\]
Then
\[
\delta a_2=D,\qquad \pi a_2=\bar a.
\tag{9}
\]

Consider
\[
r:U\longrightarrow T\oplus Z,\qquad r(u)=(\delta u,cu).
\]
For \(x\in S_0\), the equality \(\Theta(x)=0\) implies
\((Dx,Qx)\in\operatorname{im}r\): choose \(u_0\in U\) with \(\delta u_0=Dx\); then \(Qx-cu_0\in B=c(A)\), so add a suitable element of \(A\) to \(u_0\). The map
\(x\mapsto(Dx,Qx)\) on \(S_0\) can therefore be lifted through the equivariant surjection \(U\to\operatorname{im}r\). This gives an equivariant map \(u_0:S_0\to U\) satisfying
\[
\delta u_0=D|_{S_0},\qquad cu_0=Q|_{S_0}.
\]
By (8) and (9), \(a_2(S_0)\subseteq U\). Consequently
\[
h_0=u_0-a_2|_{S_0}:S_0\longrightarrow A.
\]
Choose an equivariant projection \(p_0:X\to S_0\), and set
\[
a=a_2+h_0p_0.
\]
Because \(A\subseteq K\cap U\), this modification preserves both equations in (9), and it gives
\[
a|_{S_0}=u_0,\qquad ca|_{S_0}=Q|_{S_0}.
\]

Define a map on the invariant subspace \(U+a(X)\subseteq P\) by
\[
b_0(u+ax)=cu+Qx. \tag{10}
\]
To check well-definedness, suppose \(u+ax=0\). Then \(\bar a x=0\), so \(x\in S_0\), and
\[
cu+Qx=-cax+Qx=0.
\]
Thus (10) is a well-defined equivariant linear map. Extend it equivariantly to \(P\) using an invariant complement of \(U+a(X)\). The resulting \(b\) satisfies \(b|_U=c\) and \(ba=Q\), while \(\delta a=D\) already holds. This proves sufficiency and the theorem.

## 3. Independent duality check

Dualize the problem, interchanging the two factors:
\[
\gamma'=\delta^*,\quad \delta'=\gamma^*,\quad
C'=D^*,\quad D'=C^*,\quad Q'=Q^*.
\]
The corresponding unknowns are \(a'=b^*\) and \(b'=a^*\).
The elementary conditions are interchanged. Using annihilators in the appropriate dual spaces,
\[
U'=K^\perp,\qquad K'=U^\perp,\qquad
A'=(U+K)^\perp.
\]
Restriction of functionals to \(K\) gives
\[
M'=U^\perp/(U+K)^\perp\cong(K/A)^*=M^*.
\]
The induced marked map \(c':U'\to X^*\) is characterized by
\(c'(\delta^*\ell)=D^*\ell\). Its image on \(A'\) is
\[
B'=D^*(T^\perp)=X_0^\perp.
\]
The domain \(X_0'\subseteq Z^*\) in the dual construction is exactly
\[
X_0'=B^\perp\cong(Z/B)^*.
\]
Indeed, \(C^*z^*\) lies in \(\gamma^*(K^\perp)\) precisely when the functional \(z^*c\) on \(U\) annihilates \(A=U\cap K\).

For \(z^*\in B^\perp\), choose \(\ell\in L^*\) such that
\(\gamma^*\delta^*\ell=C^*z^*\). For \(x\in X_0\), choose \(u\in U\) with \(\delta u=Dx\). Then
\[
\ell(Dx)=(\delta^*\ell)(u)=z^*(cu).
\]
Pairing the dual obstruction with \(x\) therefore yields
\[
z^*(Qx)-\ell(Dx)=z^*(Qx-cu).
\]
Under the identifications above, this says exactly that \(\Theta'=\Theta^*\). The obstruction criterion is thus invariant under transposition, with reservoir \(M^*\), as the original factorization problem requires.

## 4. Minimal quotient-image size

For any solution, let \(\bar a=\pi a\). The map \(\bar\delta\) restricts to a surjection
\(\operatorname{im}\bar a\to\operatorname{im}\bar D\), with kernel \(\bar a(X_0)\). By necessity, \(\operatorname{im}\Theta\) is a quotient, hence a direct summand, of \(\bar a(X_0)\). Consequently, irreducible by irreducible,
\[
[\operatorname{im}\bar a]
\geq [\operatorname{im}\bar D]+[\operatorname{im}\Theta].
\tag{11}
\]
Here brackets denote multiplicity vectors, and the inequality is coordinatewise. Construction (7) attains equality because \(\bar a(X_0)=j(\operatorname{im}\Theta)\). Thus the obstruction measures exactly the additional quotient-image capacity needed inside \(K/A\), beyond the part forced by \(D\) modulo \(T\).

## 5. Unrestricted feasible-locus corollary

Fix \(\gamma,\delta,C,D\) satisfying (2), and now allow \(Q\) to vary over
\[
H=\operatorname{Hom}_G(X,Z).
\]
The assignment
\[
F:H\longrightarrow\operatorname{Hom}_G(X_0,Z/B),
\qquad F(Q)=qQ|_{X_0}-\bar cD|_{X_0},
\]
is an affine surjection. To see surjectivity of its linear part, any map \(X_0\to Z/B\) can be lifted through an equivariant section of \(q\), then extended from \(X_0\) to \(X\) using an invariant complement.

For each irreducible \(S\), put
\[
n_S=\operatorname{mult}_S(X_0),\quad
p_S=\operatorname{mult}_S(Z/B),\quad
m_S=\operatorname{mult}_S(M),\quad
r_S=\min(n_S,p_S,m_S).
\]
After choosing multiplicity-space coordinates, equivariant maps \(X_0\to Z/B\) are tuples of matrices \(\Theta_S\) of size \(p_S\times n_S\). The exact feasible locus is
\[
F^{-1}\!\left(\prod_S\{\Theta_S:\operatorname{rank}\Theta_S\leq m_S\}\right).
\tag{12}
\]
Each factor is an ordinary determinantal variety. It is closed by the vanishing of the \((m_S+1)\)-minors when \(m_S<\min(n_S,p_S)\), and otherwise is the entire matrix space. It is irreducible: every matrix of rank at most \(r_S\) factors through a vector space of dimension \(r_S\), so this closed locus is the image of an irreducible product of two matrix spaces under matrix multiplication. Its codimension is \((n_S-r_S)(p_S-r_S)\); this follows, for example, from the rank-\(r_S\) stratum, of dimension \(r_S(n_S+p_S-r_S)\), which is dense in that locus.

Choosing a splitting of the affine surjection \(F\) identifies (12) with an affine space times this product of determinantal varieties. Therefore the unrestricted feasible locus is nonempty, closed, irreducible, and has codimension
\[
\sum_S(n_S-r_S)(p_S-r_S)
\]
in \(H\).

## 6. Symmetric positive curries and limits of this slice

Suppose, in a proposed positive-factorization application, the representations are identified as
\[
X=V\otimes N_2,\qquad
Y=W\otimes K_3^{-},\qquad
Z=V^*\otimes N_4,\qquad
L=W^*\otimes K_5^{-}.
\]
The canonical currying identification is
\[
\operatorname{Hom}_G(V\otimes N_2,V^*\otimes N_4)
\cong
\operatorname{Hom}_G(N_2,V^*\otimes V^*\otimes N_4).
\]
The symmetric-curry condition selects the linear subspace
\[
\mathcal S=
\operatorname{Hom}_G(N_2,\operatorname{Sym}^2(V^*)\otimes N_4)
\subseteq H.
\]
Provided the isolated equations are exactly (1), the exact feasible symmetric targets are
\[
\mathcal S\cap F^{-1}\!\left(\prod_S\{\operatorname{rank}\Theta_S\leq m_S\}\right).
\tag{13}
\]
This statement does not assert irreducibility, nonemptiness, or the unrestricted codimension formula for (13). Restriction to \(\mathcal S\) need not preserve affine surjectivity onto the obstruction-map space, and a linear section of an irreducible determinantal variety need not be irreducible.

In the motivating window terminology, \(\gamma\) and \(\delta\) are the prescribed negative arrows, while \(C\) and \(D\) remain prescribed mixed-square composites made from the other positive arrows. Fixing \(C,D\) is an assumption of this slice; they are not automatically independent parameters in the full problem. If those other positive arrows vary, the theorem applies fiberwise to the resulting \(C,D\), rather than proving a single global irreducibility claim. The other window equations are not solved here.

No identification with an actual HM/source instance, compatibility of its factor spaces with these unrestricted equivariant unknowns, or violation of the resulting bounds is claimed. Such applicability and any actual exclusion require separate authorized verification.

## 7. Useful degenerate cases

If \(\delta\gamma=0\), then \(U\subseteq K\), \(T=0\), \(X_0=\ker D\), \(B=C(Y)\), and the exact additional condition is
\[
\operatorname{im}\!\left(\ker D\xrightarrow{Q}Z/C(Y)\right)
\hookrightarrow \ker\delta/\operatorname{im}\gamma.
\]
If also \(\ker\delta=\operatorname{im}\gamma\), this reduces to
\[
Q(\ker D)\subseteq C(Y),
\]
together with (2).

More generally, if \(M=0\), the exact additional condition is simply \(\Theta=0\). If \(\gamma=0\), the criterion becomes the multiplicity bound for \(Q|_{\ker D}\) against \(\ker\delta\), after requiring \(C=0\) and \(\operatorname{im}D\subseteq\operatorname{im}\delta\).

## Contribution

The theorem replaces two bilinear unknown factors by one explicit canonical quotient map and finitely many representation-theoretic rank bounds. Necessity and sufficiency are both proved, including the equivariant extension steps and the exact kernel control in the complement construction. The result supplies a universal obstruction/construction slice only; it does not settle the full positive window or an actual HM/source instance.
