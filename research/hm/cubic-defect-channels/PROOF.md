# The degree-two defect has three normalizer channels

Let \(F\) be the normalized Horrocks–Mumford bundle on complex \(\mathbf P^4\), and set \(B=\operatorname{End}_0(F)\). The degree-two section-resolution defect of PR451 has dimension exactly 65 and canonically decomposes into three nonisomorphic normalizer representations of dimensions 15, 20, and 30. Its quotient sequence admits a unique normalizer-equivariant splitting, giving canonical lifts of the three channels and a universal cubic multiplication map into \(H^1B(5)\).

The proof uses the section resolution and primary cohomology from PR451/PR167, the finite normalizer representations in Horrocks–Mumford (1973), and the twist-two vanishing proved in PR94. It does not evaluate a chosen HM matrix, a selected multiplication map, or a tensor-cohomology table. The selected cubic maps and the order-five endpoint quotient remain unevaluated.

## 1. Conventions, including the primes

Let \(N=H_5\rtimes G\), \(G=\mathrm{SL}_2(\mathbf F_5)\), and use the standard five-dimensional representation \(V\) of \(N\) from HM §1. Let \(\theta\) be their Galois operation, and set

\[
A=\theta V=V_1,\qquad A^*=\theta^3V=V_3.
\]

Their central weights are respectively \(2\) and \(3\) modulo five. Put \(S=\operatorname{Sym}(V^*)\), so \(S_d=H^0(\mathcal O(d))\).

The following symbols denote representations of \(G=N/H_5\), inflated to \(N\):

\[
\begin{array}{c|c|c}
\text{symbol}&\text{HM character}&\text{dimension}\\ \hline
W&\chi_2&2\\
W'&\chi_2'&2\\
U=\operatorname{Sym}^2W&\chi_3&3\\
U'=\operatorname{Sym}^2W'&\chi_3'&3\\
T&\chi_4&4\\
Q=\operatorname{Sym}^3W=\operatorname{Sym}^3W'&\chi_4^\#&4\\
J&\chi_5&5\\
R&\chi_6&6 .
\end{array}
\]

In particular, \(T\) and \(Q\) are different representations. The central element \(-I\) of \(G\) acts as \(+I\) on \(T\) and as \(-I\) on \(Q\). All the displayed \(G\)-representations are self-dual. The representations \(W,W'\) are symplectic.

Let \(F\) be normalized, and \(E=F(3)\) be the bundle in the HM paper. The primary cohomology identities, with this normalization, are

\[
\begin{aligned}
M_0&=H^1F=A^*,&
M_1&=H^1F(1)=A\otimes W',\\
M_2&=H^1F(2)=V\otimes W',&
M_3&=H^1F(3)=W',\\
H^2F(-2)&=W,&
H^0F(3)&=T.
\end{aligned}                                                    \tag{1}
\]

These are HM (4.2), (4.4), (4.6), (4.11), and (4.12), not just their dimensions. HM Lemma 3.3 and duality give

\[
S_1=V^*,\qquad
S_2=A^*\otimes U',\qquad
S_3=A\otimes(J\oplus W'),\qquad
S_1\otimes A^*=A\otimes(U\oplus W').                 \tag{2}
\]

The last formula is the dual of HM Lemma 3.3(ix). No prime on \(U\) belongs in that last formula.

The small \(G\)-tensor identities used below are

\[
\begin{aligned}
W'\otimes U'&=W'\oplus Q,\\
U\otimes Q&=W\oplus Q\oplus R,\\
W'\otimes Q&=U'\oplus J,\\
W'\otimes J&=Q\oplus R,\\
W'\otimes W'&=\mathbf1\oplus U',\\
W\otimes W&=\mathbf1\oplus U,\\
W\otimes J&=Q\oplus R.
\end{aligned}                                                     \tag{3}
\]

They follow from the ordinary symmetric-power identities for the two-dimensional representations and the character identities in the HM Appendix. Equivalently they can be checked as identities of the nine named characters there. This is abstract finite-group representation theory, not evaluation of an HM/source matrix. In particular \(\operatorname{Sym}^3 W=\operatorname{Sym}^3 W'=Q\) and \(\operatorname{Sym}^4 W=\operatorname{Sym}^4 W'=J\).

## 2. Recovering the section-resolution multiplicities by duality

Write the minimal equivariant section resolution as

\[
0\longrightarrow B_3\otimes\mathcal O(-8)
\longrightarrow B_2\otimes\mathcal O(-6)
\longrightarrow B_1\otimes\mathcal O(-5)
\longrightarrow B_{0,4}\otimes\mathcal O(-4)\oplus B_{0,3}\otimes\mathcal O(-3)
\longrightarrow F\longrightarrow0.                                 \tag{4}
\]

The dimensions of \(B_3,B_2,B_1,B_{0,4},B_{0,3}\) are \(2,20,35,15,4\). The resolution can and will be made \(N\)-equivariant: the finite-group action lifts to a minimal graded section-module resolution, and its multiplicity representations are the corresponding equivariant Tor spaces. Minimality follows also directly from the strictly positive degrees of every possible differential entry. Moreover

\[
B_{0,3}=H^0F(3)=T.                                      \tag{5}
\]

There is no ambiguity from an equivariant determinant character. The action on \(S_1=V^*\) has determinant one, so Serre duality has its standard equivariant form. The rank-two duality \(F^*=F(1)\) is equivariant as well. One can also note that \(N\) has no nontrivial characters.

Dualize (4) and twist by \(\mathcal O(t)\). Set

\[
\begin{aligned}
D_0(t)&=B_{0,4}^*\otimes\mathcal O(t+4)
       \oplus T^*\otimes\mathcal O(t+3),\\
D_1(t)&=B_1^*\otimes\mathcal O(t+5),\\
D_2(t)&=B_2^*\otimes\mathcal O(t+6),\\
D_3(t)&=B_3^*\otimes\mathcal O(t+8).
\end{aligned}
\]

The dual sequence is exact because it is a locally free resolution of a locally free sheaf. It reads

\[
0\longrightarrow F(t+1)\longrightarrow D_0(t)
\longrightarrow D_1(t)\longrightarrow D_2(t)
\longrightarrow D_3(t)\longrightarrow0.                \tag{6}
\]

Here is the exact cohomological step needed at \(t=-8,-6,-5\). Put
\(J_0(t)=\operatorname{im}(D_0(t)\to D_1(t))\) and
\(J_1(t)=\operatorname{im}(D_1(t)\to D_2(t))\). All line bundles on \(\mathbf P^4\) have vanishing cohomology in degrees one, two, and three. The three short exact sequences from (6) therefore give

\[
H^1J_0(t)=H^2F(t+1),\qquad
H^2J_0(t)=H^3F(t+1),\qquad
H^1J_1(t)=H^2J_0(t).
\]

For these three values of \(t\), we also have
\(H^0D_0(t)=0\), \(H^1F(t+1)=0\), and \(H^2F(t+1)=0\).
Thus \(H^0J_0(t)=H^1J_0(t)=0\), and the same short exact sequences splice to the equivariant exact sequence

\[
0\longrightarrow H^0D_1(t)\longrightarrow H^0D_2(t)
\longrightarrow H^0D_3(t)\longrightarrow H^3F(t+1)
\longrightarrow0.                                      \tag{7}
\]

Only intermediate line-bundle acyclicity was used: at \(t=-8\), the summand \(T^*\otimes\mathcal O(-5)\) in \(D_0(t)\) does have nonzero \(H^4\). It does not enter these three cohomological identifications or the exact sequence (7).

### The two-dimensional top coefficient

Set \(t=-8\) in (7). The first two section spaces vanish, while the last two are \(B_3^*\) and \(H^3F(-7)=M_3^*\). Thus

\[
B_3^*=M_3^*.
\]

Consequently

\[
B_3=W'.                                                \tag{8}
\]

It would be incorrect to treat the two copies at the top of the section resolution as two copies of the trivial \(N\)-representation.

### The twenty-dimensional coefficient

Set \(t=-6\) in (7), and use \(H^3F(-5)=M_1^*\). This gives the exact sequence

\[
0\longrightarrow B_2^*
\longrightarrow B_3^*\otimes S_2
\longrightarrow M_1^*
\longrightarrow0.
\]

By (1)–(3), the middle term is

\[
W'\otimes A^*\otimes U'=A^*\otimes(W'\oplus Q),
\]

and the last term is \(A^*\otimes W'\). The two displayed constituents are nonisomorphic irreducible \(N\)-representations, so exactness gives

\[
B_2^*=A^*\otimes Q,\qquad B_2=A\otimes Q.              \tag{9}
\]

### The thirty-five-dimensional coefficient

Set \(t=-5\) in (7), and use \(H^3F(-4)=M_0^*\). This gives the exact sequence

\[
0\longrightarrow B_1^*
\longrightarrow B_2^*\otimes S_1
\longrightarrow B_3^*\otimes S_3
\longrightarrow M_0^*
\longrightarrow0.
\]

Using (1), (2), (8), (9), its representation-ring identity is

\[
[B_1^*]
=[A]\bigl([(U\oplus W')\otimes Q]
-[(J\oplus W')\otimes W']+[\mathbf1]\bigr).
\]

The bracket simplifies explicitly, using (3), to

\[
\begin{aligned}
&(W\oplus Q\oplus R)\oplus(U'\oplus J)\\
&\hspace{1cm}-(Q\oplus R)-(\mathbf1\oplus U')+\mathbf1
=W\oplus J.
\end{aligned}
\]

Since complex representations of the finite group \(N\) are semisimple, equality of these characters gives the actual representations

\[
B_1^*=A\otimes(W\oplus J),\qquad
B_1=A^*\otimes(W\oplus J).                             \tag{10}
\]

This derives the needed \(35\)-term coefficient without choosing or evaluating any resolution differential.

## 3. The degree-two differential and its exact cokernel

Use the tensor-resolution notation of PR451:

\[
E_3(2)=B_3\otimes F(-5),\quad
E_1(2)=B_1\otimes F(-2),\quad
E_0(2)=B_{0,4}\otimes F(-1)\oplus T\otimes F.
\]

The canonical identifications of PR451 give

\[
H^2L(2)=B_3\otimes M_1^*
=A^*\otimes(\mathbf1\oplus U'),                       \tag{11}
\]

and

\[
H^2E_1(2)=B_1\otimes W
=A^*\otimes(\mathbf1\oplus U\oplus Q\oplus R).         \tag{12}
\]

All maps are \(N\)-equivariant. The scalar section space

\[
H^0\mathcal O(2)=S_2=A^*\otimes U'
\]

injects into \(\ker a_2\). Its multiplicity is one in (11), so its image is exactly that \(15\)-dimensional irreducible summand. The only possible remaining part of \(a_2\) is a map from the \(A^*\) summand of (11) to the unique \(A^*\) summand of (12). It follows without importing twist-two vanishing that

\[
\operatorname{rank}a_2\in\{0,5\}.                     \tag{13}
\]

In particular, central weight alone gives the divisibility by five, while the top-coefficient refinement locates the unique possible source and target summands.

Also

\[
H^1E_0(2)=T\otimes M_0=A^*\otimes T
\]

is irreducible of dimension \(20\), by the HM nontrivial-central-character equivalence (2.2). The kernel of \(p_2\) has dimension at most five by the PR451 exact sequence: \(H^1K(2)\) has dimension at most twenty and contains the fifteen-dimensional scalar space in its kernel toward \(H^1E_0(2)\). An invariant subspace of this irreducible \(20\)-dimensional source cannot have dimension between one and five. Hence

\[
p_2\text{ is injective}.                              \tag{14}
\]

Equivalently, the map from \(\ker a_2\), whose types are among \(A^*\) and \(A^*\otimes U'\), to \(A^*\otimes T\) must vanish.

Now import PR94's structural conclusion

\[
H^0B(2)=0.
\]

Then \(H^0\operatorname{End}(F)(2)=S_2\), and (14) together with the PR451 exact sequence forces \(\ker a_2=S_2\), so \(a_2\) is nonzero on its sole remaining \(A^*\) summand. Therefore

\[
\operatorname{rank}a_2=5,\qquad
\dim C_2=65,
\]

and (12) gives the precise representation

\[
\boxed{C_2=(A^*\otimes U)\oplus(A^*\otimes Q)\oplus(A^*\otimes R).}   \tag{15}
\]

The three summands are nonisomorphic irreducible \(N\)-representations of dimensions \(15,20,30\). The decomposition into isotypic subspaces is canonical. Abstract identifications with tensor-product models in (15) can differ by scalar; the actual isotypic subspaces do not.

The \(15\)-dimensional defect channel in (15) is \(A^*\otimes U\), with the unprimed \(U\). It is not the scalar kernel \(A^*\otimes U'\). The \(20\)-dimensional defect channel uses \(Q=\chi_4^\#\), not the \(T=\chi_4\) primary-image channel.

## 4. A unique normalizer-equivariant lift of the entire defect

Set \(I_2=\operatorname{im}p_2\). Equation (14) identifies

\[
I_2=A^*\otimes T.
\]

The short exact sequence

\[
0\longrightarrow I_2\longrightarrow H^1B(2)
\overset{\pi}{\longrightarrow}C_2\longrightarrow0       \tag{16}
\]

splits as \(N\)-representations by semisimplicity. More strongly,

\[
\operatorname{Hom}_N(C_2,I_2)=0,
\]

because \(T\) is distinct from \(U,Q,R\). Two equivariant splittings differ by an element of this Hom space. Thus (16) has a **unique \(N\)-equivariant splitting**

\[
j:C_2\longrightarrow H^1B(2),\qquad \pi j=1.           \tag{17}
\]

The lift is intrinsic relative to the classical \(N\)-action; no arbitrary vector-space complement is needed. The image \(I_2\) is itself intrinsic: at twist two the only nonzero part of the section-evaluation source is \(H^0F(3)\otimes H^1F\), and \(p_2\) is its cup product followed by the trace-free identification in intermediate cohomology. Thus the assertion is not contingent on choices of the degree-four minimal generators in (4).

In particular,

\[
H^1B(2)
=(A^*\otimes T)\oplus(A^*\otimes U)
\oplus(A^*\otimes Q)\oplus(A^*\otimes R),               \tag{18}
\]

with dimensions \(20+15+20+30=85\). The four distinct isotypic subspaces are canonical.

## 5. Universal and selected cubic multiplication

The splitting (17) produces a canonical \(N\)-equivariant universal cubic map into the full target:

\[
\mathcal M_3:S_3\otimes C_2\longrightarrow H^1B(5),
\qquad s\otimes c\longmapsto s\,j(c).                  \tag{19}
\]

The word “canonical” here means canonical with respect to the fixed classical normalizer action, not invariant under arbitrary changes of that action.

For the fixed regular pair \(u\in S_2,v\in S_3\), let

\[
P_5=H^1B(5)/(uH^1B(3)+vI_2),
\]

as in PR451. Its cubic defect map is exactly

\[
\delta_v(c)=[\mathcal M_3(v\otimes c)]\in P_5.          \tag{20}
\]

Write \(C_{15},C_{20},C_{30}\) for the three canonical summands in (15), and \(\delta_{v,d}\) for the restriction to \(C_d\). Then the exact endpoint becomes

\[
C_{15}\oplus C_{20}\oplus C_{30}
\overset{\delta_{v,15}+\delta_{v,20}+\delta_{v,30}}{\longrightarrow}
P_5\longrightarrow Q_5\longrightarrow0,               \tag{21}
\]

or equivalently

\[
Q_5=P_5/
\bigl(\operatorname{im}\delta_{v,15}
+\operatorname{im}\delta_{v,20}
+\operatorname{im}\delta_{v,30}\bigr).                  \tag{22}
\]

The sum of the three images is not asserted to be direct. For general fixed \(u,v\), \(P_5\) need not be an \(N\)-representation and none of the selected \(\delta_{v,d}\) need be equivariant. Consequently Schur's lemma does not imply that a selected channel is zero or injective, and (15) alone does not determine any selected cubic rank or prove endpoint vanishing.

Without using (17), there is also a canonical, more lossy map

\[
S_3\otimes C_2\longrightarrow H^1B(5)/(S_3I_2)
\]

defined by arbitrary lifts in (16). This quotient kills all cubic multiples of \(I_2\), not only \(vI_2\). It should not be silently substituted for (20), since it need not recover the original \(P_5\). The unique splitting allows (19) and is therefore the more precise refinement.

## 6. Checked dependency and scope

The degree-two defect sequence, its map \(a_2\), and the order-five exact endpoint are from PR451 at the exact commit

https://github.com/Akilleez-QA/read-em-and-weep/blob/ed8841c18f103e71b84c0e9376e20a2a4ed2ef9c/research/hm/order-five-cubic-defect/PROOF.md

The section resolution and primary cohomology are also pinned in PR167 at

https://github.com/Akilleez-QA/read-em-and-weep/blob/063da90fc4543304e87e701cdefcc08225412f17/research/conductor-normalization/sharper-hm-regularity/PROOF.md

The twist-two vanishing dependency is PR94 at the exact commit

https://github.com/Akilleez-QA/read-em-and-weep/commit/73917b562c26be3c7999b005bf6f2514206eaf43

Its files are

- `research/hm/twist-two-vanishing/PROOF.md`,
- `research/hm/twist-two-vanishing/AUDIT.md`.

The independent review is

https://github.com/Akilleez-QA/read-em-and-weep/pull/94#pullrequestreview-5581064573

The proof derives \(H^0B(2)=0\) by excluding the five-dimensional section alternative via the full evaluation map, reflexive semistable rank-two kernel, Bogomolov, Ou's reflexive flatness criterion, and a negative leading codimension-three defect cycle. The proof and audit explicitly retain their twist-one prerequisite, PR91 at `ee7c4d4627c2efa07ea167a535cf1582002ef335`; the review also records its subsequent explanatory update `872aca45943d3758e261a900e5984b981c18b3c4`. This proof imports PR94 as a mathematical dependency, not as a claim of merger, formal verification, or independent reproof of those geometric theorems.

Primary representation source:

https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

Use HM §§1–2, Lemma 3.3, equations (4.2), (4.4), (4.6), (4.11), (4.12), and the Appendix on printed p.81. The distinction between \(\chi_4\) and \(\chi_4^\#\) is retained throughout.

No matrix instance, generator list, checker, rank routine, or large computation was used. The new conclusions are the abstract multiplicity identification (10), the exact three-channel defect (15), the canonical normalizer-equivariant lift (17), and its universal cubic realization (19)–(22). The selected cubic maps and the order-five quotient remain unevaluated.
