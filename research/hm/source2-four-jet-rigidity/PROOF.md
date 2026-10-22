# Universal four-jet spanning and the next actual source2 Gauss flag

## Result and scope

Let \(G\) be the binary icosahedral group, \(W\) its defining representation, and
\[
\mathcal H\subset H^0(\mathbf P(W),\mathcal O(18)),\qquad
\mathcal H\simeq A_{\rm std}\oplus V\oplus P,\quad \dim\mathcal H=10.
\]
Here \(A_{\rm std}=\operatorname{Sym}^2W\), \(V\) is the other center-even three-dimensional irreducible, and \(P\) is the four-dimensional irreducible. Every basepoint-free such subsystem spans jets through order four at every point:
\[
\mathcal H\longrightarrow \mathcal O(18)\otimes\mathcal O_{\mathbf P^1,p}/\mathfrak m_p^5
\quad\text{is onto for every }p. \tag{1}
\]

For the hypothetical actual source **G3.21.d610e381ed75**, source index 2, apply this to the final constant-quotient line \(C=\mathcal O(-18)\) of PR751. Write \(R^{(k)}\) for its actual residual's \(k\)-fold saturated forward transform, with \(R^{(0)}=R\). Then
\[
0\longrightarrow U_{k+2}^{8}\longrightarrow R^{(k)}
 \longrightarrow U_k^{18}\longrightarrow0,\qquad 0\le k\le4, \tag{2}
\]
where \(U_j^e=\operatorname{Sym}^jW\otimes\mathcal O(j-e)\). The last term is embedded by projection into the genuine final constant quotient. All the derivative-generated sheaves in (2) are already saturated. In particular,
\[
\begin{array}{c|rrrrr}
k&0&1&2&3&4\\ \hline
\operatorname{rk}R^{(k)}&4&6&8&10&12\\
\deg R^{(k)}&-36&-54&-68&-78&-84
\end{array}
\]
and, as equivariant bundles,
\[
R^{(3)}\simeq \operatorname{Sym}^5W\,\mathcal O(-3)
 \oplus\operatorname{Sym}^3W\,\mathcal O(-15),
\]
\[
R^{(4)}\simeq \operatorname{Sym}^6W\,\mathcal O(-2)
 \oplus\operatorname{Sym}^4W\,\mathcal O(-14). \tag{3}
\]
These are bundle splittings, not horizontal splittings.

Using the genuine full inverse-image theorem of PR784, the next actual backward transforms of \(E\) satisfy
\[
(\operatorname{rk}E^{---},\deg E^{---})=(9,-78),\qquad
(\operatorname{rk}E^{----},\deg E^{----})=(7,-84). \tag{4}
\]
Their consecutive quotient bundles are
\[
J_3=E^{--}/E^{---}\simeq\mathcal O(-2)\oplus\mathcal O(12),\qquad
J_4=E^{---}/E^{----}\simeq\mathcal O(-4)\oplus\mathcal O(10). \tag{5}
\]
The induced Gauss injection \(J_3\to J_2(-2)\), where
\(J_2=\mathcal O(-10)\oplus\mathcal O\oplus\mathcal O(14)\), has image exactly the top two summands. The induced \(J_4\to J_3(-2)\) is an isomorphism.

This gives necessary same-source compatibility beyond zero second defect. It does not exclude the source2 label, change the fixed frontier of 23 labels, choose the abstract \(P\)-multiplicity parameter, or prove realization. No claim about a parameter-space Wronskian map or jets of order five is made.

## 1. Pinned inputs

All transforms use the original constant connection on \(\mathbf P(W)\).

1. [PR751, full residual span](https://github.com/Akilleez-QA/read-em-and-weep/blob/e21d50b6bd7d124dc419beeb8c27fa3b9ef3e169/research/hm/order-four-quadratic-load/TWO-ONE-INDEX-TWO-RESIDUAL-FULL-SPAN.md) gives a 19-dimensional genuine constant space \(\overline H\), an invariant constant \(V_1=\operatorname{Sym}^8W\subset\overline H\), and an actual saturated \(R\subset\overline H\otimes\mathcal O\) with
   \[
   R\cap(V_1\otimes\mathcal O)=U_2^8,\qquad
   0\to U_2^8\to R\to C\to0.
   \]
   Here \(H_{\rm fin}=\overline H/V_1\simeq A_{\rm std}+V+P\), and
   \[
   0\to C=\mathcal O(-18)\to H_{\rm fin}\otimes\mathcal O
   \to(P+\operatorname{Sym}^4W)\mathcal O(2)\to0
   \]
   is exact. Both quotient maps are sheaf-surjective. In particular the dual ten-section system is basepoint-free.

2. [PR754, abstract degree-eighteen systems](https://github.com/Akilleez-QA/read-em-and-weep/blob/044add76ebb14043a0edf73171517c90b9ef0c13/research/hm/order-four-quadratic-load/ABSTRACT-DEGREE-EIGHTEEN-BALANCED-SYSTEMS.md) identifies the irreducibles and the degree-eighteen family. The theorem here applies uniformly to every basepoint-free member, not only to the balanced open locus.

3. [PR784, zero second primal defect](https://github.com/Akilleez-QA/read-em-and-weep/blob/66aa488fb10158abcc2d35ce58b05b901d44b81a/research/hm/source2-second-defect-zero/PROOF.md) proves \(s=0\), \(J_2=\mathcal O(-10)+\mathcal O+\mathcal O(14)\), and
   \[
   (Q^*)^{++}=p^{-1}(R^{++}), \tag{6}
   \]
   where \(p:H^*\otimes\mathcal O\to\overline H\otimes\mathcal O\) is the actual constant quotient by \(V_0=\operatorname{Sym}^{10}W\), of dimension 11, and \(\dim H=30\). The proof's reviewed SHA-256 is
   \[
   \texttt{b0695ab0fbbfa9a4a4985f29c2818b15a8f6ec1977a5c2eae944d7c3b1bfe766}.
   \]
   Equation (6) is equality as saturated subbundles, not a statement only at the generic point.

The projective \(G\)-action is \(A_5\); point orbits have sizes 12, 20, 30, or 60. Stabilizers are cyclic, and the size-12 orbit has projective stabilizer of order five. The binary group is perfect, so its one-dimensional characters are trivial.

## 2. Wronskian degree and local weight

Put \(L=\mathcal O(18)\). The order-nine jet evaluation of \(\mathcal H\) has determinant
\[
\mathcal W_{\mathcal H}\in
H^0\!\left(\det(\mathcal H)^*\otimes L^{10}\otimes
(\Omega^1)^{0+1+\cdots+9}\right)
=H^0(\mathcal O(90)). \tag{7}
\]
This follows either from the filtration of principal parts, whose successive quotients are \(L\otimes(\Omega^1)^j\), or from the triangular coordinate and frame-change law of the Wronskian. The degree is \(10\cdot18-2\cdot45=90\).

At an arbitrary point let
\[
0\le a_0<a_1<\cdots<a_9\le18
\]
be the vanishing sequence of \(\mathcal H\). A basis adapted to the vanishing filtration has leading orders \(a_i\). The leading coefficient of its Wronskian is a nonzero scalar times
\(\prod_{i<j}(a_j-a_i)\), the Vandermonde determinant of the falling-factorial polynomials. Characteristic zero makes this nonzero. Consequently the Wronskian is not identically zero, and its vanishing order at the point is exactly
\[
w=\sum_{i=0}^9(a_i-i). \tag{8}
\]
This is a universal local identity; it evaluates no selected source section or point.

The jet determinant is equivariant. Thus its zero divisor is \(G\)-invariant. In fact the determinant character in (7) is trivial because \(G\) is perfect, so the canonical section itself is invariant. The total effective Wronskian weight is 90.

If jets through order four fail at a point, then \(a_4\ge5\). Strict increase then gives \(a_i\ge i+1\) for every \(i=4,\ldots,9\), hence
\[
w\ge6. \tag{9}
\]
Every orbit other than the size-12 orbit has at least 20 points. A failure on any of these would contribute at least \(20\cdot6=120>90\). It remains only to examine order-five stabilizers.

## 3. The order-five fiber character, with its twist retained

Fix an arbitrary point with projective stabilizer of order five. Its stabilizer in \(G\) is cyclic of order ten. Choose a generator \(g\) whose eigenvalue on the tautological line \(\ell\subset W\) is \(\lambda\), a primitive tenth root; the other eigenvalue is \(\lambda^{-1}\). Put \(\zeta=\lambda^2\). The tangent character at \(\ell\) is \(\lambda^{-2}\), the cotangent character is \(\zeta\), and the fiber character of \(L=\mathcal O(18)\) is \(\lambda^{-18}=\zeta\). Therefore the degree-\(j\) associated graded piece of the local jet filtration has character
\[
L_p\otimes(\mathfrak m_p^j/\mathfrak m_p^{j+1})
:\quad \lambda^{-18}\lambda^{2j}=\zeta^{j+1}. \tag{10}
\]
Thus the fiber twist is not discarded. Reversing the generator or using the opposite character convention merely permutes the five residue classes; no multiplicity conclusion changes.

The restrictions of the three summands are
\[
A_{\rm std}|_{\langle g\rangle}=1+\zeta+\zeta^{-1},\qquad
V|_{\langle g\rangle}=1+\zeta^2+\zeta^{-2},
\]
\[
P|_{\langle g\rangle}=\zeta+\zeta^2+\zeta^3+\zeta^4. \tag{11}
\]
For \(P\), this is the five-cycle permutation representation on five letters minus its invariant line. The \(A_{\rm std}\) formula is \(\operatorname{Sym}^2W\); the \(V\) formula also follows by subtracting \(P\) from \(\operatorname{Sym}^6W=V+P\). Hence each of the five characters occurs exactly twice in \(\mathcal H\).

The vanishing filtration of \(\mathcal H\) is stabilizer-invariant, and each nonzero associated graded piece is one-dimensional. Equation (10) shows that orders congruent to \(j\pmod5\) account exactly for the character \(\zeta^{j+1}\). There are therefore exactly two vanishing orders in each residue class \(j=0,\ldots,4\). Their smallest possible values are \(j,j+5\), and the sum of all ten baseline orders is
\[
\sum_{j=0}^4(2j+5)=45. \tag{12}
\]

Failure of four-jet spanning omits at least one of the orders \(0,1,2,3,4\). If order \(j\) is omitted, the two orders in its residue class are at least \(j+5,j+10\), raising the total in (12) by at least 10. All other classes retain their baseline lower bounds. Thus \(w\ge10\). The invariant size-12 orbit would contribute at least \(12\cdot10=120>90\), again impossible.

This proves (1). It uses no order-two fiber-sign argument.

## 4. The endpoint's first four osculating bundles

For the complete degree-eighteen system, the \(k\)-th osculating subbundle is
\[
U_k^{18}=\operatorname{Sym}^kW\otimes\mathcal O(k-18),
\]
with fiber \(\ell^{18-k}\operatorname{Sym}^kW\). Project it from the complete constant space to \(H_{\rm fin}\). The dual of (1), and its lower-order consequences, says this projection is fiberwise injective for \(0\le k\le4\). Its image is therefore a subbundle. It is locally generated by \(c,c',\ldots,c^{(k)}\) for a local generator \(c\) of \(C\); coordinate and generator changes act triangularly with invertible diagonal.

Accordingly the derivative-generated sheaf is already saturated, and
\[
C^{(k)}\simeq U_k^{18}\quad(0\le k\le4). \tag{13}
\]
No choice of a splitting of the ambient representation changes its connection.

## 5. Exact and saturated forward residual growth

Use the genuine constant quotient \(q:\overline H\to H_{\rm fin}\). Locally choose a regular lift \(r\in R\) of a generator \(c\in C\). Together with a frame of \(U_2^8\), it is a frame of \(R\); this uses only the sheaf-surjectivity in Section 1.

The complete degree-eight osculating flag has
\[
(U_j^8)^+=U_{j+1}^8\quad(j<8).
\]
Its universal leading coefficient is \(8-j\): the derivative of
\(\ell^{8-j}y^j\), for \(\ell=x+ty\), is
\((8-j)\ell^{7-j}y^{j+1}\) modulo \(U_j^8\). For \(j=2,3,4,5\), the coefficients are \(6,5,4,3\), all nonzero. Thus these transformations are generated without a saturation correction.

By the Leibniz rule, the sheaf generated by derivatives of a local frame of \(R\) through order \(k\le4\) is exactly
\[
\mathcal G_k=
\left\langle U_{k+2}^8,r,r',\ldots,r^{(k)}\right\rangle. \tag{14}
\]
Changing the lift adds only sections and derivatives of \(U_2^8\), already in \(U_{k+2}^8\). Constant projection sends the extra generators to \(c,c',\ldots,c^{(k)}\), which are independent at every point by (13). A local frame of \(U_{k+2}^8\), followed by these \(k+1\) generators, is therefore everywhere independent in the constant ambient space. Its image is a subbundle, and is already saturated. Inductively it is exactly \(R^{(k)}\).

The intersection with \(V_1\otimes\mathcal O\) is exactly \(U_{k+2}^8\), and projection is onto \(C^{(k)}\) everywhere. This proves (2), including exactness and saturation. The rank and degree are
\[
\operatorname{rk}R^{(k)}=(k+3)+(k+1)=2k+4,
\]
\[
\deg R^{(k)}=(k+3)(k-6)+(k+1)(k-18)
=2k^2-20k-36. \tag{15}
\]
The extension group in (2) is a constant coefficient space tensored with
\(H^1(\mathcal O(12))=0\). Hence the sequence splits as bundles; averaging a splitting over the finite group makes it equivariant. This proves (3), without making the splitting horizontal.

## 6. Full inverse images continue under forward growth

For a constant quotient \(p:\mathcal V\otimes\mathcal O\to\overline{\mathcal V}\otimes\mathcal O\), and a saturated subbundle \(S\) of the quotient, let \(F=p^{-1}(S)\). Then
\[
F^+=p^{-1}(S^+). \tag{16}
\]
Indeed \(F\) contains the entire constant kernel of \(p\). Local sections of \(S\) lift regularly to \(F\), and constant projection commutes with differentiation. Thus the unsaturated derivative-generated sheaf of \(F\) is the inverse image of the derivative-generated sheaf of \(S\). Saturation commutes with inverse image under a quotient with locally free constant kernel: this follows locally from the induced identification of the two quotient sheaves. This proves (16) as equality of saturated bundles.

Apply (16) twice to PR784's (6). It gives
\[
(Q^*)^{(k)+}=p^{-1}(R^{(k)})\quad(k=2,3,4), \tag{17}
\]
where the left-hand side means \(k\) forward transforms. Therefore its rank is \(11+\operatorname{rk}R^{(k)}\), and its degree is \(\deg R^{(k)}\).

For the original constant pairing, \(E^{(-k)}=\operatorname{ann}((Q^*)^{(k)+})\). This follows by differentiating the pairing and taking saturation at each stage. If \(F\subset H^*\otimes\mathcal O\) is saturated, its annihilator has rank \(30-\operatorname{rk}F\) and degree \(\deg F\), by the exact dual quotient sequence. Equations (15) and (17) now prove (4). No new plateau-rank assumption is introduced.

## 7. Consecutive quotients and their actual Gauss maps

For \(k=3,4\), compare the exact rows (2) for \(k-1\) and \(k\). Their inclusions are the actual osculating inclusions. The quotient sequence is
\[
0\to U_{k+2}^8/U_{k+1}^8
 \to R^{(k)}/R^{(k-1)}
 \to U_k^{18}/U_{k-1}^{18}\to0. \tag{18}
\]
The complete osculating quotient formula
\[
U_j^e/U_{j-1}^e=\mathcal O(2j-e)
\]
holds equivariantly: its fiber is
\(\ell^{e-j}\operatorname{Sym}^j(W/\ell)\simeq\ell^{e-2j}\), using \(\det W=1\). Hence (18) is
\[
0\to\mathcal O(2k-4)\to R^{(k)}/R^{(k-1)}
 \to\mathcal O(2k-18)\to0. \tag{19}
\]
Its extension group is \(H^1(\mathcal O(14))=0\), so it splits equivariantly.

Full inverse images in (17) identify the forward consecutive quotient with \(R^{(k)}/R^{(k-1)}\). Annihilator duality then identifies
\[
J_k=E^{(-(k-1))}/E^{(-k)}
 \simeq\bigl(R^{(k)}/R^{(k-1)}\bigr)^*
 =\mathcal O(4-2k)\oplus\mathcal O(18-2k).
\]
This is (5), derived from actual nested subbundles rather than numerical splitting alone.

For completeness, the derivative induces an injection
\(J_{k+1}\hookrightarrow J_k(-2)\): differentiating a section of \(E^{(-k)}\) lands in \(E^{(-(k-1))}\otimes\Omega^1\); modulo \(E^{(-k)}\otimes\Omega^1\), its kernel is precisely \(E^{(-(k+1))}\). These are sheaf injections, with no assumption of equal ranks before the ranks are established.

For \(k=2\), the target is
\[
J_2(-2)=\mathcal O(-12)\oplus\mathcal O(-2)\oplus\mathcal O(12).
\]
The determined \(J_3=\mathcal O(-2)+\mathcal O(12)\) has no nonzero morphism to the \(\mathcal O(-12)\) summand. Its injection consequently factors through the top two summands. Both sides then have rank two and degree 10; their nonzero determinant is a constant section of \(\mathcal O\), so this factorization is an isomorphism. Thus the image is the actual maximal-degree rank-two subbundle and the remaining cokernel is \(\mathcal O(-12)\), not torsion.

For \(k=3\), source and target are both \(\mathcal O(-4)+\mathcal O(10)\), of rank two and degree 6. The determinant argument again shows \(J_4\to J_3(-2)\) is an isomorphism.

## Novelty and boundary

The latest checked PR758 head is 063216038f3aefd65617651c2426721efafc7f9b. Its [exact residual flag](https://github.com/Akilleez-QA/read-em-and-weep/blob/063216038f3aefd65617651c2426721efafc7f9b/research/hm/order-four-quadratic-load/TWO-ONE-INDEX-TWO-EXACT-RESIDUAL-GAUSS-FLAG.md) concerns the backward flag \(R,R^-,R^{--},R^{---}\), of ranks \(4,2,1,0\). It does not establish the forward four-jet theorem or (4)–(5). PR751 gives the constant quotients, and PR754 classifies the abstract balanced locus. PR784 establishes second jets, the first two forward residual transformations, and \(s=0\); those are acknowledged inputs, not claimed new here.

The new step is the universal degree-90 Wronskian bound with the correctly twisted order-five jet characters, yielding four-jet spanning everywhere and its exact transfer to the third and fourth actual primal kernels and quotients. The proof uses no coefficient assignment, selected actual point, source derivative evaluation, actual-instance matrix or rank evaluation, scan, experiment, or numerical parameter choice. Universal local coordinates and symbolic derivative identities are not selected-instance evaluations.

There is no additional contradiction with source2 established here. Its quotient label and the fixed 23-label count remain unchanged. Source realization, any stronger jet statement, and overall rank-three exclusion remain open. This is a written mathematical proof, not proof-assistant certification.

