# Independent scoped review: septic multiplication channels

## Verdict and frozen input

**PASS, within the explicitly imported geometric and Eagon–Northcott hypotheses.**
No mathematical correction is required to the reviewed text.

The reviewed file is `PROOF.md`, with SHA256

`49e1cd6d0db85e093a087d6023823d91bd8c72cd166fa60b6e3f4c609d818f75`.

This verdict applies to those exact bytes. In particular, it certifies the structural conclusion

\[
g_7\in\{0,20\},
\]

and the nonvanishing of the quotient-channel scalar \(\alpha_Q\). It does not determine the remaining primary-channel scalar \(\alpha_T\).

The following local dependencies were read:

- Sextic saturation proof, SHA256 `105812f9f0414a744c3d8b881edf4d3cd3b651ab0a59d6ee4e82a6ef0e9c1a3e`.
- Septic saturation proof, SHA256 `2d60f124d55bae90989b39051c88057e5a083237b0b4603a6128b483433146fd`.
- HM1973 layout text, SHA256 `500a4ffd3d5035c9262cac3d12c8ee83a33d098f5b2f9532704e752fb75bd448`.
- HM1973 Appendix page image, SHA256 `e86c3aaa42356321664f2f454860982bc831dbb814f858f0af9976cf15b1e112`. The character table was inspected visually, rather than relying on its imperfect OCR.

The exactness of the evaluation Eagon–Northcott resolution for the specified line union and the prior identification of its six quintics remain imported foundational inputs. Their entire earlier geometric proof chains were not re-proved in this review.

## 1. Primary representation conventions and determinant twists

HM1973, section 1, identifies the finite normalizer \(N\subset SL(V)\), its quotient \(N/H=SL_2(\mathbf F_5)\), the four Galois-conjugate representations \(V_i\), and \(V_i^*\simeq V_{i+2}\). Section 2 identifies \(H^0\mathcal O(1)=V^*\), so the proof's \(S_1=V_2\) and \(A^*=V_3\) are consistent.

The Appendix has real-valued characters for all quotient factors used. Thus they are self-dual as complex representations; this observation does not require, or assert, that every such representation has a real form. Its two degree-four rows are different:

- \(\chi_4(-I)=4\);
- \(\chi_4^\#(-I)=-4\).

Consequently \(T_4\) and \(Q_4\) cannot be exchanged. The two Galois-conjugate degree-two rows and degree-three rows are exchanged by \(\theta\), while \(\theta^2\) fixes them.

Section 2 gives \(\Lambda^2V=A\otimes W\), and Lemma 3.3(v) gives \(\operatorname{Sym}^2V=A\otimes U'\), with the prime exactly as used in the reviewed proof. Multiplication of the displayed Appendix characters verifies

\[
W\otimes W'=T_4,\qquad
W\otimes U=W\oplus Q_4,\qquad
W'\otimes U'=W'\oplus Q_4.
\]

For example, writing \(\eta=\zeta+\zeta^4\) and \(\eta'=\zeta^2+\zeta^3\), the unipotent columns use \(\eta\eta'=-1\) and \(\eta^2=1-\eta\). These give precisely the displayed degree-four row, not its inequivalent partner. The symmetric-cube descriptions agree as well.

HM1973, section 4, printed pp. 73–74, proves that \(H^0E\) is \(H\)-trivial with quotient character \(\chi_4\). Its determinant is therefore a character of the perfect quotient group and is trivial. Hence

\[
\Lambda^3V_s\simeq V_s^*\otimes\det V_s\simeq T_4.
\]

All ambient determinant corrections in equivariant Serre duality and in \(\Lambda^3V^*\simeq\Lambda^2V\) vanish on \(N\subset SL(V)\). Choosing a scalar trivialization of the determinant line does not affect the canonical submodules, vanishing tests, or unique splitting claims.

## 2. Sextic source and irreducibility

The sextic dependency identifies the new quotient, and its unique equivariant complement, with

\[
U_6\simeq D\otimes(\Lambda^2V_3)^*.
\]

Applying \(\theta^3\) to \(\Lambda^2V=V_1\otimes W\) gives

\[
\Lambda^2V_3=V\otimes W',
\]

and hence \(U_6=V^*\otimes W'\). Applying \(\theta^2\) to the full symmetric/exterior decomposition of \(V\otimes V\) gives

\[
V^*\otimes V^*=A^*\otimes(W\oplus U').
\]

Combining these identities independently reproduces

\[
S_1\otimes U_6
 =A^*\otimes(W'\oplus Q_4\oplus T_4).
\]

Its summand dimensions are \(10,20,20\), totaling 50.

Criterion (2.2) applies because \(A^*\) is irreducible on \(H\) and each second factor is irreducible on \(N/H\). It establishes both irreducibility and pairwise inequivalence. Thus the three isotypic summands are intrinsic, even though an explicit tensor identification is only determined up to scalar.

## 3. Septic target and unique splitting

The septic dependency proves the injection

\[
A\otimes W\hookrightarrow U\otimes T',
\]

and its universal cup lemma identifies \(T'\) with \(H^0\Omega^2(3)=\Lambda^3V^*\). As \(N\) is unimodular,

\[
T'=\Lambda^2V=A\otimes W.
\]

The codomain is therefore \(A\otimes(W\oplus Q_4)\). The injected irreducible \(A\otimes W\) occurs there exactly once, so its cokernel is exactly \(A\otimes Q_4\). Duality gives

\[
H^2B(-3)=A^*\otimes Q_4.
\]

The normalized monad also directly confirms \(H^1F=V_3\): its left and middle terms are acyclic, and its right term is \(V_3\otimes\mathcal O\). This agrees with HM1973's section 4 cohomology character after normalization.

The imported Eagon–Northcott cohomology sequence consequently has outer terms \(A^*\otimes T_4\) and \(A^*\otimes Q_4\). They are inequivalent. Semisimplicity supplies a splitting, and the space of differences of two sections is

\[
\operatorname{Hom}_N(A^*\otimes Q_4,A^*\otimes T_4)=0.
\]

Thus the equivariant section is unique, as claimed. The \(T_4\) summand is the actual submodule coming from cohomology, and the \(Q_4\) summand is its unique equivariant complement.

The second Eagon–Northcott short exact sequence identifies the quotient by quadratic quintic products with \(H^1K_7\). Its injected old-product space has dimension \(15\cdot6=90\), leaving the claimed 40-dimensional target

\[
R_7=A^*\otimes(T_4\oplus Q_4).
\]

## 4. Schur decomposition and preliminary generator count

Polynomial multiplication and the quotient maps are \(N\)-equivariant. There is no target of the \(X_{10}\) representation type. Each other source type occurs once in the target and cannot map to the other target type. Thus Schur's lemma yields exactly the two scalar tests described in the proof.

Each nonzero block is an isomorphism of a 20-dimensional irreducible module. Therefore

\[
\operatorname{rank}m\in\{0,20,40\},\qquad
\dim\ker m=10+g_7,\qquad
g_7=\dim\operatorname{coker}m\in\{0,20,40\}.
\]

The identification of this cokernel with minimal septic generators is valid: using the sextic splitting,

\[
S_1H^0I_C(6)=S_2H^0I_C(5)+S_1U_6.
\]

Accordingly \(I_7/(S_1I_6)\) is precisely the displayed cokernel. These are the three possibilities at the representation-reduction stage; the new Euler-complex argument subsequently excludes 40. The proof never asserts that all preliminary possibilities are realized.

## 5. Naturality and the adjoint test

The claimed quotient-channel identity follows from two natural diagrams, not merely from matching representation types.

At degree six and degree seven, multiplication by a linear form maps both short exact sequences in the Eagon–Northcott resolution to the corresponding next-twist sequences. Naturality of their long exact sequences gives:

1. the multiplication map on the ideal quotients corresponds to the multiplication \(H^1K_6\to H^1K_7\);
2. its composition with \(H^1K_7\to D\otimes H^2B(-3)\) corresponds to \(D\otimes[H^2B(-4)\to H^2B(-3)]\).

At degree six, the relevant cohomology of \(F(-1)\) vanishes, making \(H^1K_6\simeq D\otimes H^2B(-4)\). Combining the two diagrams gives precisely the asserted tensor identity. This does not require choosing sextic representatives or an arbitrary projection onto a 20-dimensional vector space.

Since \(B\) is equivariantly self-dual and \(\omega_{\mathbf P^4}=\mathcal O(-5)\) on \(N\), the dual of

\[
S_1\otimes H^2B(-4)\longrightarrow H^2B(-3)
\]

is indeed

\[
H^2B(-2)\longrightarrow S_1^*\otimes H^2B(-1).
\]

The twists, cohomological degrees, and \(S_1^*\) factor are correct. Nonvanishing is preserved by duality. The reviewed proof properly refrains from inferring this nonvanishing solely from the differential used to compute \(H^2B(-2)\), instead using the independent comparison checked below.

## 6. Full linear syzygies

The canonical sextic splitting identifies the old part of \(S_1\otimes I_6\) with \(S_1\otimes S_1\otimes I_5\). Its multiplication factors through \(S_2\otimes I_5\), and the latter injects into \(I_7\). Its kernel is therefore exactly

\[
\Lambda^2S_1\otimes I_5,
\]

of dimension \(10\cdot6=60\).

Projection of a full syzygy onto \(S_1\otimes U_6\) lands in \(\ker m\). Conversely, every element of \(\ker m\) has product in the old quadratic-product subspace; an old-product preimage cancels that product. This proves surjectivity to \(\ker m\), and hence the exact sequence claimed in the text. It is equivariant and splits by Maschke; no unjustified uniqueness is asserted.

Its dimension is \(60+(10+g_7)=70+g_7\), as stated.

## 7. Strengthened Euler-complex comparison

The new section 6 was reviewed in its complete written form, not only from a summary. Its chain-map argument is sound.

### 7.1 The universal complex and its multiplication

The exterior Euler sequence is exactly

\[
0\longrightarrow K=\Lambda^2Q^*
\longrightarrow L\otimes\mathcal O
\longrightarrow Q^*(1)\longrightarrow0,
\qquad L=\Lambda^2V^*.
\]

For a locally split injection \(K\hookrightarrow L\otimes\mathcal O\) with quotient \(R\), the complex

\[
[\operatorname{Sym}^2K\longrightarrow K\otimes L
\longrightarrow\Lambda^2L\otimes\mathcal O]
\]

has only the cohomology sheaf \(\Lambda^2R\) in degree 2. Locally, the first map sends \(k_1k_2\) to \(k_1\otimes k_2+k_2\otimes k_1\), and the second sends \(k\otimes l\) to \(k\wedge l\). Splitting \(L=K\oplus R\) verifies exactness in the first two degrees and identifies the final cokernel with \(\Lambda^2R\). Here \(\Lambda^2R=K(2)\).

It follows functorially that

\[
\mathbb H^2(U^\bullet(t))=H^0K(t+2).
\]

Both \(K\) and \(\operatorname{Sym}^2K\) are indeed acyclic at twist zero. This is consistent with, and follows from, the Bott calculation in the sextic dependency: the nonzero central cohomology there belongs to the \(\Lambda^2K\) factor, not to \(\operatorname{Sym}^2K\). Thus the canonical edge identifies

\[
\Lambda^2L\simeq\mathbb H^2(U^\bullet)\simeq H^0K(2).
\]

The dimension is \(\binom{10}{2}=45\). The target \(H^0\Omega^2(4)\) is an irreducible \(GL(V)\)-module, while \(H^0K(1)=H^0\Omega^2(3)=\Lambda^3V^*\) has dimension 10. The multiplication

\[
S_1\otimes H^0K(1)\longrightarrow H^0K(2)
\]

is nonzero: multiplication by a nonzero linear form is injective on a locally free sheaf over integral projective space. Equivariance and target irreducibility therefore imply surjectivity. The functorial identification with hypercohomology preserves this multiplication.

### 7.2 Existence and uniqueness of the constant extensions

Dualizing the exterior Euler sequence gives

\[
0\longrightarrow Q(-1)\longrightarrow L^*\otimes\mathcal O
\longrightarrow K^*\longrightarrow0.
\]

The ordinary Euler sequence twisted by \(-1\) expresses \(Q(-1)\) as the cokernel of \(\mathcal O(-2)\to V\otimes\mathcal O(-1)\). Both line-bundle terms are acyclic on \(\mathbf P^4\), so \(Q(-1)\) is acyclic. Therefore

\[
L^*\simeq H^0K^*.
\]

For each \(w\in W\), this identifies the sheaf map \(q_w:K\to C_0\otimes\mathcal O\) with one and only one constant linear map \(c_w:L\to C_0\). No values of that linear map need be chosen or computed.

### 7.3 The chain map and its edge

The displayed degree-zero map to \(\operatorname{Sym}^2(W\otimes K)\), degree-one map to \(W\otimes K\otimes C_0\), and degree-two map \(\Lambda^2c_w\) form a chain map.

Explicitly, applying the target differential to
\((w\otimes k_1)(w\otimes k_2)\) gives

\[
(w\otimes k_1)\otimes c_w(k_2)
+(w\otimes k_2)\otimes c_w(k_1),
\]

which is the image of the source differential. In degree one the two routes both give \(c_w(k)\wedge c_w(l)\). These are the usual compatible symmetric-square and exterior-square conventions; any coherent nonzero normalization yields the same conclusion.

The additional \(A\otimes C_0\otimes\mathcal O(-1)\) target summand has zero source component. The negative target degrees impose no extra equation because the source complex has no negative-degree terms. Thus there is no missing compatibility with the first monad arrow.

The sextic dependency's vanished transgression makes the edge

\[
\Lambda^2C_0\longrightarrow\mathbb H^2(J^\bullet)
=H^2B(-1)
\]

an isomorphism. Naturality of the edge maps consequently identifies the zero-twist hypercohomology map with \(\Lambda^2c_w\). This is the crucial point connecting the universal comparison to the actual cohomological multiplication, and it is justified.

### 7.4 The contradiction and its relation to the quotient channel

Assume that

\[
S_1\otimes H^2B(-2)\longrightarrow H^2B(-1)
\]

vanishes. The chain maps at twists \(-1\) and 0 give a commutative multiplication square. Surjectivity of the universal top multiplication forces the zero-twist comparison to vanish. Hence \(\Lambda^2c_w=0\) for every \(w\in W\).

Over \(\mathbf C\), vanishing of the second exterior power of a linear map is equivalent to its image having dimension at most one. Taking any two-element basis of \(W\) then confines the entire image of \(q:W\otimes K\to C_0\otimes\mathcal O\) to the sum of two constant subspaces of total dimension at most two. This is incompatible with its established surjectivity onto the rank-five bundle \(C_0\otimes\mathcal O\).

Thus the actual multiplication is nonzero. Currying it gives

\[
H^2B(-2)\longrightarrow S_1^*\otimes H^2B(-1),
\]

which is exactly the Serre adjoint of the quotient-channel multiplication in section 5, not a different test. Therefore \(\alpha_Q\ne0\).

The final consequences follow:

\[
g_7\in\{0,20\},\qquad
\ker m=X_{10}\ \text{or}\ X_{10}\oplus X_T,\qquad
\operatorname{coker}m=0\ \text{or}\ A^*\otimes T_4.
\]

The full syzygy dimension is correspondingly 70 or 90. Only \(\alpha_T\) remains unresolved.

## Boundary

This review used exact representation identities, the source character table, universal cohomological functoriality, and the stated dependency proofs. It did not select or evaluate an actual HM/source-instance matrix, polynomial coefficient instance, numerical rank, generator/checker, or parameter search. No large computation or publication was performed.

The exterior-square rank implication is a universal linear-algebra statement used in a contradiction, not a numerical rank evaluation on a selected instance. The argument uses only the monad's already established sheaf-surjectivity.

The result does not resolve \(\alpha_T\), fixed-pair intersections, actual-source membership, pure conditions, higher lifting, or algebraicity. It is a mathematical review, not formal proof-assistant certification.
