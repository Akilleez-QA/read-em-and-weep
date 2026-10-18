# Thirty explicit weighted tests for the remaining permutation sector

## Result

**Yes. The existing frozen 32-test family reduces to its first 30 tests.** The two omitted tests are

\[
D_{5,0;v_0^2},\qquad D_{5,0;v_1v_4}.
\]

They are genuine full-\(S_4\)-sign functionals, not merely two rows with a convenient block label. The checked global primitive kills their whole source sector. The remaining thirty tests restrict to a basis of the dual of the thirty-dimensional residual target. Their independence follows from the already authenticated 32-test theorem; no rank is recomputed here.

This is a theorem about global classes and the exact published weighted outputs. It supplies no physical source values, no new cutoff/domain certificate, no permission for coefficient arithmetic, and no vanishing assertion for the residual thirty-dimensional class.

## 1. Fixed objects and evidence

Work over \(\mathbb Q\). Put \(Y=(\mathbf P^1)^4\), let \(\rho:Y\to\mathbf P^4\) be the symmetric-product map, and let \(B=\operatorname{End}(K)\) for the pinned perfect complex. Let

\[
T=\mathcal O_Y(-2,-2,-2,-2),\qquad
H=\mathbb H^2(Y,\rho^*B\otimes T).
\]

Here \(T\) has the authenticated **ordinary product deck linearization**. Write \(\varrho(g)\) for the genuine factor-permutation action, including source-cover and physical-frame transport. Let

\[
W=H^{D_8,\epsilon},\qquad
e=\frac1{24}\sum_{g\in S_4}\operatorname{sgn}(g)\varrho(g),\qquad
W_{30}=\ker(e|_W).
\]

The accepted permutation-sector theorem gives \(\dim W=32\), \(\dim eW=2\), and \(\dim W_{30}=30\). The latter is the \(D_8\)-epsilon line in each of thirty copies of the \((2,2)\) representation. It is not itself an \(S_4\)-stable subrepresentation.

The following public files are read at the immutable PR89 commit
`e93cf712f9da4926a8450cc870ed45a7bfc379ab`:

- [Twenty-map derived completeness](https://github.com/Akilleez-QA/read-em-and-weep/blob/e93cf712f9da4926a8450cc870ed45a7bfc379ab/research/codex-swarm/twenty-map-completeness.md).
- [Separation of the rational epsilon sector](https://github.com/Akilleez-QA/read-em-and-weep/blob/e93cf712f9da4926a8450cc870ed45a7bfc379ab/research/codex-swarm/constant-scalars-separate-epsilon.md).
- [32-test proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/e93cf712f9da4926a8450cc870ed45a7bfc379ab/research/codex-swarm/detector-selection/proof.md) and its [independent final acceptance](https://github.com/Akilleez-QA/read-em-and-weep/blob/e93cf712f9da4926a8450cc870ed45a7bfc379ab/research/codex-swarm/detector-selection/review-final.md).
- [Exact labels and normalization](https://github.com/Akilleez-QA/read-em-and-weep/blob/e93cf712f9da4926a8450cc870ed45a7bfc379ab/research/codex-swarm/detector-selection/README.md).
- [Independent source-duality review](https://github.com/Akilleez-QA/read-em-and-weep/blob/e93cf712f9da4926a8450cc870ed45a7bfc379ab/research/codex-swarm/reports/Codex-D03-output-duality.md).
- [selection.json](https://github.com/Akilleez-QA/read-em-and-weep/blob/e93cf712f9da4926a8450cc870ed45a7bfc379ab/research/codex-swarm/detector-selection/selection.json), SHA-256 `54603e2e3634d73da740837081297800f3b2b3bb219aeccd22141ac27e58368d`.
- [weighted-requests.json](https://github.com/Akilleez-QA/read-em-and-weep/blob/e93cf712f9da4926a8450cc870ed45a7bfc379ab/research/codex-swarm/detector-selection/weighted-requests.json), SHA-256 `f256746fbfd0897fd4a5241e13715198004d277fec700b7ba5c4b3ace9bfe5e0`.

The last two source files were fetched independently at this pin and match the already inspected PR83 copies byte for byte. The accepted full-alternation primitive and its independent review, together with the authenticated ordered-nerve construction, are additional premises for application to the actual residual. No rank producer, finite-model driver, physical source, or previous source experiment was run for this deduction.

## 2. The scalar source-dual identification

The constant rows are actual global chain maps

\[
L_{i,b}:B\longrightarrow\mathcal O_{\mathbf P^4}(-2)[2],\qquad
L_{i,b}(X)=X_{13}[i,b]-\sum_{a,k}\gamma[i,a,k]X_{02}[a,5b+k].
\]

The coefficient \(\gamma[i,a,k]\) is constant. The target term has internal degree \(-2\). Reversing the Hom directions in the supertrace pairing identifies this map with

\[
c_{i,b}=-K_{15b+i}\in\mathbb H^2(B(-2)),\qquad
\operatorname{str}(XK_{15b+i})=-L_{i,b}(X).
\]

The ten published \(d_5\) relations are relations of derived morphisms, not pointwise identities among polynomial rows. They leave the twenty classes indexed by

\[
I_{20}=\{(i,0):5\le i\le10\}\ \cup\
\{(i,1):0\le i\le14,\ i\ne5\}
\]

as a basis of \(\mathbb H^2(B(-2))\). The selected ten linear multiples and two quadratic multiples are bases of the twist-minus-one and twist-zero groups. Their existing exact-cycle and quotient-rank certificates are imported as established premises, not inferred anew from dimensions or from hashes.

Pullback of \(L\), followed by tensoring with \(T\), gives the scalar cohomology map

\[
S_L:H\longrightarrow H^4(Y,F),\qquad F=\mathcal O_Y(-4,-4,-4,-4).
\]

Both the coefficient matrices and \(L\) descend from \(\mathbf P^4\), on which factor permutations act trivially. The ordinary product frames of \(T\) and \(F\) introduce no permutation sign. Hence \(S_L\) intertwines the genuine permutation actions. An ordered contraction need not itself be equivariant for this statement: it is an equality of the geometric cohomology maps.

For \(f\in H^0(Y,\mathcal O_Y(2,2,2,2))\), the frozen output test is

\[
D_{L,f}(x)=[x_1^{-1}x_2^{-1}x_3^{-1}x_4^{-1}]\bigl(f\,S_L(x)\bigr).
\tag{1}
\]

This is the pinned residue/Serre pairing after the original-frame, deck-product, and \(\tau^{-4}\) identifications. It is not a point evaluation. If \(f=\sum_m f_mx^m\), it requests the exact weighted sum of coefficients at \(-m-\mathbf1\), with no factorial or extra sign.

## 3. Derive the actual permutation sign

Use the standard two-chart Cech complex in each factor. The harmonic classes of \(H^1(\mathbf P^1,\mathcal O(-4))\) are represented by \(x^{-3},x^{-2},x^{-1}\) in Cech degree one. The Kunneth tensor of four such classes represents \(H^4(Y,F)\).

Interchanging two factors interchanges two degree-one Cech factors. The tensor-complex symmetry therefore contributes \(-1\). The ordinary tensor line frames contribute no further sign. Consequently, for a harmonic Laurent monomial class,

\[
\varrho_F(g)[x^a]=\operatorname{sgn}(g)[x^{g a}].
\tag{2}
\]

This is the action on the genuine scalar target, not a guessed action on a pruned End-model basis. Equivalently, the canonical bundle has the additional sign from the wedge of four differentials, while the deck line has the ordinary product linearization.

Combining (1), (2), and the naturality of \(S_L\) gives the exact covariance law

\[
D_{L,f}(\varrho(g)x)
 =\operatorname{sgn}(g)D_{L,g^{-1}f}(x).
\tag{3}
\]

In particular, for a symmetric polynomial section \(f\),

\[
D_{L,f}\circ\varrho(g)=\operatorname{sgn}(g)D_{L,f},\qquad
D_{L,f}\circ e=D_{L,f}.
\tag{4}
\]

Thus symmetric weights yield full-sign functionals. No source computation or numerical action matrix is needed to establish (3) or (4).

## 4. Identify precisely the two removable tests

The last two requests in the frozen file are zero-based IDs 30 and 31:

\[
D_{30}=D_{L_{5,0},v_0^2},\qquad D_{31}=D_{L_{5,0},v_1v_4}.
\]

Homogeneously,

\[
v_k=\sum_{|I|=k}\prod_{i\in I}X_i\prod_{j\notin I}Y_j.
\]

Every \(v_k\) is fixed by every factor permutation. This includes \(v_0=\prod_iY_i\); its finite-chart expression is 1, but its homogeneous degree is retained. Therefore both displayed weights are fixed by \(S_4\), and (4) proves

\[
D_{30}|_{W_{30}}=D_{31}|_{W_{30}}=0.
\tag{5}
\]

In the frozen 81-coordinate scalar convention, these two exact equations are

\[
D_{30}=s_{5,0}[80],\qquad
D_{31}=s_{5,0}[13]+s_{5,0}[31]+s_{5,0}[37]+s_{5,0}[39].
\tag{6}
\]

The second equation does not assert that its four summands vanish separately. The notation \(s_{5,0}[k]\) denotes the transported harmonic scalar output coordinates.

The pre-existing theorem states that \(D_0,\ldots,D_{31}\) form a basis of \(W^\vee\). Since \(W=W_{30}\oplus eW\), the annihilator of \(W_{30}\) in \(W^\vee\) has dimension two. By (5), the independent \(D_{30},D_{31}\) form a basis of that annihilator. If

\[
\sum_{a=0}^{29}t_aD_a|_{W_{30}}=0,
\]

then \(\sum_{a=0}^{29}t_aD_a\) lies in the span of \(D_{30},D_{31}\). Independence of all 32 forces every \(t_a=0\). Hence

\[
(D_0,\ldots,D_{29}):W_{30}\xrightarrow{\sim}\mathbb Q^{30}.
\tag{7}
\]

The conclusion is stronger than an abstract existence of thirty rows and does not require a new restricted-rank calculation. It uses the actual source-dual linearization and exact last-two weights. Merely knowing a 32=30+2 dimension split, without those facts, would not suffice.

## 5. The thirty tests, explicitly

Retain the twenty tests \(D_{L_{i,b},Q^2}\) for every pair in \(I_{20}\), in the frozen order, where

\[
Q=X_1X_2Y_3Y_4+Y_1Y_2X_3X_4.
\]

Retain also these ten tests, in order:

1. \(D_{L_{5,0},v_0Q}\)
2. \(D_{L_{5,0},v_1Q}\)
3. \(D_{L_{5,0},v_4Q}\)
4. \(D_{L_{6,0},v_0Q}\)
5. \(D_{L_{6,0},v_1Q}\)
6. \(D_{L_{6,0},v_2Q}\)
7. \(D_{L_{7,0},v_1Q}\)
8. \(D_{L_{7,0},v_2Q}\)
9. \(D_{L_{8,0},v_3Q}\)
10. \(D_{L_{9,0},v_4Q}\)

The companion `weighted-requests-30.json` is an exact subsequence, retaining the first thirty record objects unchanged. It has 122 listed weighted terms and 116 distinct (map, exponent) requests. These are request counts only; they do not bound physical coefficient work, owner traversal, runtime, or memory.

The twenty \(Q^2\) tests and ten \(v_kQ\) tests need not individually annihilate \(eW\). Their restrictions to \(W_{30}\) are the basis in (7). Do not misidentify the three original free-module summands with orthogonal \(S_4\)-isotypic subspaces.

## 6. Optional genuinely projected dual rows

For any weight, averaging (3) gives

\[
D_{L,f}\circ e=D_{L,\operatorname{Sym}f},\qquad
\operatorname{Sym}f=\frac1{24}\sum_{g\in S_4}gf.
\]

Thus \(D_{L,f-\operatorname{Sym}f}=D_{L,f}\circ(1-e)\) is a canonical projected functional on all of \(H\), with the same restriction to \(W_{30}\).

If \(Q_1,Q_2,Q_3\) are the three pair-partition conjugates of \(Q\), then

\[
\operatorname{Sym}Q=\frac{v_2}{3},\qquad
\operatorname{Sym}(Q^2)=\frac{v_2^2-2v_1v_3+8v_0v_4}{3}.
\]

The formulas follow from \(\sum Q_i=v_2\) and \(\sum_{i<j}Q_iQ_j=v_1v_3-4v_0v_4\). Therefore one can use the exact centered weights

\[
Q^2-\frac{v_2^2-2v_1v_3+8v_0v_4}{3},\qquad
v_k\left(Q-\frac{v_2}{3}\right)
\]

for the corresponding thirty projected rows. This identifies their dual projection without any change-of-basis matrix or rank recomputation. It is unnecessary to replace the frozen requests: on the actual residual class the original thirty and centered thirty have equal values. No promise of lower evaluation cost is made for the centered expressions.

## 7. Canonical residual class and a fixed-source cochain

First work on the full ordered source nerve, allowing repeated vertex labels. Let \(\overline R_{\rm raw}\) be the complete fresh raw representative with every baseline, gerbe, scalar, and transport term retained. The genuine action permutes coordinates and legal-mask labels, preserves tuple positions, and transports the fixed physical source data. It is not “sort the tuple and permute a harmonic row.” It commutes with the row-End Cech differential \(\delta\).

The accepted full-alternation theorem supplies the regular edge cochain

\[
P_{ij}=-\frac1{72}\,
\iota_{V_1\wedge V_2\wedge V_3\wedge V_4}
\left((Z_i+Z_j)\wedge L_{ij}\right),
\quad
Z_i=\operatorname{str}(B_i^3),\quad L_{ij}=g_{ij}^{-1}dg_{ij},
\]

in the prescribed first-row physical frame, with no extra evaluation factorial, and proves

\[
e\overline R_{\rm raw}=\delta P.
\]

Define

\[
\boxed{\overline R_{30}=\overline R_{\rm raw}-\delta P
       =(1-e)\overline R_{\rm raw}.}
\tag{8}
\]

Then \(\delta\overline R_{30}=0\) and \(e\overline R_{30}=0\) literally on the ordered nerve. Only afterward restrict to the increasing source cover. The resulting class is

\[
[R_{30}]=(1-e)[R_{\rm raw}]=[R_{\rm raw}]=[R^\sharp]\in W_{30}.
\tag{9}
\]

The final equality uses the accepted fresh raw/N14 global comparison for the same physical source and ambient problem. The class (9) is canonical under the authenticated comparisons. The cochain (8) is canonical relative to the fixed raw source and genuine action; no representative is claimed independent of all cover/frame/first-lift choices pointwise. The displayed primitive may be replaced by another with the same differential without changing (8).

Raw cochains need not be strictly \(D_8\)-epsilon cochains. Equation (9) needs only the authenticated class membership. If a strict epsilon cochain is required, apply the genuine \(D_8\) projector to (8) on the ordered nerve; it represents the same class. The shorter three-pair-partition projector is valid at class level, but must not replace the full cochain action without its required comparisons.

Since every \(D_{L,f}\) is a global cohomological functional,

\[
D_{L,f}([R^\sharp])=D_{L,f}([R_{\rm raw}])=D_{L,f}([R_{30}]).
\]

There is therefore no need to implement \(P\) in a finite-cutoff coefficient provider just to use the thirty-test reduction. Its regular global boundary proves the class theorem; it does not place \(P\) inside any numerical cutoff. The same complete-source transport and domain obligations continue to govern actual evaluation of either admitted representative. In particular, the genuine nonzero highest mixed-second-jet symbol is not discarded from the remaining sector.

## 8. Exact outcome and limits

For the complete authenticated obstruction class,

\[
[R^\sharp]=0\quad\Longleftrightarrow\quad
D_a([R^\sharp])=0\ \text{for every }a=0,\ldots,29.
\]

The two omitted assembled values are already zero by the full-sign boundary theorem and (4). None of the thirty retained values is determined here. One authenticated nonzero retained value would prove nonvanishing; thirty authenticated zero values would prove vanishing.

In particular, an evaluation plan whose sole target is frozen zero-based request 30, \(D_{L_{5,0},v_0^2}\), now targets a globally redundant pairing. Executing that target cannot decide the remaining obstruction. This does **not** say that the raw cochain, its requested local coefficients, or its individual owner/staircase contributions vanish. Only their complete, correctly transported global pairing is forced to vanish by the theorem.

No extra action matrix or quotient-basis selection is missing for this reduction: the pinned chain-map naturality, scalar top-cohomology sign, symmetric last-two weights, and established 32-test independence suffice. What remains missing is the actual source evaluation, with all previously required source/domain and resource authorization. No claim about characteristic three, all orders, finite-cutoff exactness, or a changed computational permission follows.

The companion control checks only immutable file hashes, exact request subsequence, symmetric weight identities, and request counts. It performs no source evaluation, rank calculation, or model reconstruction. Its role is transcription control; the proof of the action and independence is above.

## Immutable boundary-theorem input

The full alternating primitive is published with independent review at [PR79 commit 3b3f249](https://github.com/Akilleez-QA/read-em-and-weep/blob/3b3f24971bc5fca9876f8d46f5c2e456a056b726/research/hm/null-alternating-primitive/review/REVIEW.md). Root independently checked the present deduction against the pinned 32-test proof and final acceptance, the actual last-two request labels, and the genuine scalar-target action. Root reproduced check_metadata.py normally and with optimization. This review adds no actual source or rank computation.
