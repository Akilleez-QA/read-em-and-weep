# Independent whole-proof review

Verdict: PASS, conditional on the five explicitly pinned imported theorems. No mathematical correction requested. This is a fresh structural mathematical review, not formal proof-assistant verification and not an evaluation of the remaining actual obstruction ranks or vertex scalar.

Reviewed after the author's byte-ready signal on 2026-10-23. The reviewer read the entire proof, the five imported local originals, the final verifier and reproduction instructions. The freshly fetched originals were byte-compared with the copies read during the review; all five matched. The verifier independently authenticated their Git-blob identities recorded in INPUTS.json.

## Geometric and homological checks

1. The length-two symmetric-square Steiner resolution has the correct twists: exterior-square A contributes O(-5), A tensor D contributes O(-4), and Sym2 D contributes O(-3). Stability gives only the nonpositive section vanishing. The additional twist-one argument genuinely supplies the missing vanishing: rank-one and rank-two tensors in exterior-square A tensor V would contradict fiberwise injectivity of the original Steiner map. Thus every nonzero member of its kernel, viewed as a square matrix, would have full rank. Over C such a linear subspace has dimension at most one. Equivariance and A tensor V=P+D exclude that remaining dimension. This is universal linear algebra, not an actual coefficient or rank evaluation.

2. The remaining plane cohomology follows from this vanishing, the exact resolution, and Serre duality. In particular H0(B_R(4)) has character 2A+2V+2P+2D and no invariants. The H1 characters at twists -1, 0, 1 are respectively A+V+P+D, V+P+D, and A+V. The use of Euler characters here is legitimate because both other cohomology groups have already been shown to vanish.

3. For the lines convention on P(N), O_E(E) is the tautological relative O(-1). Relative duality gives R1 of O_E(-j) as Sym^(j-2) N tensor det N, hence the essential positive base twist j. With N=W* tensor O_R(1), this gives exactly G_j=Sym^(j-2)W tensor B_R(j-9), using the determinant-form identification of W and its dual. The divisor sequences give actual short exact sequences for K_j because p_*O(jE)=O and p has fiber dimension at most one. They do not make K_j an O_R-module or split its thickening filtration.

4. Central parity removes precisely the odd layers. The six even invariant layer entries are (h0,h1,h2): j=2: (0,0,0); j=4: (0,0,1); j=6: (0,1,0); j=8: (0,2,0); j=10: (0,0,0); j=12: (2,0,0). The finite-group invariant functor is exact in characteristic zero, so the subsequent long exact sequences are valid.

5. The ambient H3 and H4 vanishings used for the incidence sequence follow from the cited primary tensor resolution on the correct resolution diagonals. The resulting R2 and R3 of π vanish without a degeneration assumption. Since the base of π is a curve, H3(X,M)=0 follows. In the two-row p-Leray sequence the relevant segment is H3(X,M) -> H2(K12) -> H4(B(-9)); the end terms vanish, the latter by H0(B(4))=0. This forces H2(K12)=0 and hence H2(K10)^G=0. The Euler calculation then forces dim H1(K10)^G=2.

6. The final clarification correctly identifies only invariant cohomology across odd steps, not the thickening sheaves themselves. The lower connecting maps have the stated canonical sources and targets. Exactness gives H1(K6)^G=ker α and H2(K6)^G=coker α, followed by the nonsplit exact sequence involving ker β. Vanishing of H2(K10)^G makes β surjective, so rank α+rank β=1. The argument does not silently choose a complement or decide which actual map is nonzero.

7. The top boundary has source and target of dimension two. The p-Leray identification of its kernel uses H1(B(-9))=H2(B(-9))=0, which follow by ambient duality. The π-Leray identification uses the independently verified absence of A in Sym16 W. Together they canonically identify ker σ with H0(C(-12))^G. The imported dimension bound at most one therefore really forces σ to be nonzero, without selecting rank one or rank two.

8. For the vertex ideal, disjointness from E is used only to identify the actual higher direct-image sheaf with K12; it is not used to kill a global differential. The restriction sequence gives H1(I_L B(-9))=0 and H2(I_L B(-9))^G=C. The positive O(-16) channel contributes no invariants because Sym14 W has none. On π the absence of W in Sym17 W kills the section-bundle H1 invariant term. The comparison of the two restriction sequences identifies the actual p-Leray d2 with the published extension functional δ, up to the harmless overall sign of consistent boundary conventions. Equality is justified by naturality, not just equality of kernels or dimensions.

9. The canonical bundle formula is ω_X=p*O(-5) tensor O(E)=p*O(-4) tensor π*O(-1). Thus the Serre-dual coefficient is exactly N=p*B(4) tensor O(-11E). Negative exceptional twists have no higher p-direct images and push forward to I_R^11. The codimension-three regular vertex immersion has normal bundle V tensor O_L(1), producing B|L(7) in the local-duality term. Its H1 is zero and its invariant H0 is one-dimensional. The Ext long exact sequence therefore gives precisely the displayed Gysin cokernel sequence, and its map is dual to d2. No self-duality of D_vert is presumed.

## Arithmetic and reproducibility

The reviewer separately recomputed the plane Euler characters and six layer multiplicities from the Steiner resolution, using the existing exact nine-class character arithmetic engine rather than any actual HM maps. These computations reproduced all values above, Sym16 W=V+P+2D, Sym17 W=W'+S+2T6, and the absence of a trivial constituent in Sym14 W. This is an independent derivation of the required expressions, not a second independently implemented character table.

The final package's python3 verify.py and python3 -O verify.py both passed. Optimization cannot remove its checks, which use explicit exceptions rather than assertions. The script checks only fixed abstract characters and universal dimension alternatives; the geometric proof, not the arithmetic script, establishes actual nonvanishing. No actual HM/source coefficient, point, parameter, matrix, derivative, instance rank, scan, or large computation was used. No external publication or submission was performed by the reviewer.

The proof correctly leaves rank σ, the scalar δ, the actual splitting type and source compatibility undecided. Its parameter twist -12 is not identified with physical normal order twelve.

## Exact reviewed bytes

SHA-256 of the four final artifacts, excluding this review to avoid self-reference:

- PROOF.md: 03f7909a73ebe2cd2ff7c8639f3bea3384741058297156f51f38b2b6094354e6
- verify.py: 1f98776d94cb73ffc664d5c4645a88986e56ac5bc228dfc0cd70adfb8908f88b
- INPUTS.json: ffa77c74417d1301b9bb9a379f2d72ce10b03b25e9747c94764e76c83a97178c
- REPRODUCE.md: 9e0d2baee3f86daf035e6cdc741e31e4de24d05753b14b6d73d4ae17a78f812b

SHA-256 of the five checked original input copies:

- REDUCED.md: 69e72653c1b7fe6925743c877210f0ee5714b284d9e1d370afd8bff279e4c1d8
- AMBIGUITY.md: 2bf246913d0eb0456b7939b73ccc09d83baac4d39b5b9841e151afab221803d8
- STEINER.md: 036a45ff8998e84c9a967808faed91d6ce9283cc686e2fbb8c378b095beb7b2d
- REGULARITY.md: 91334643653347f002f37a4b4346fb96e6e0edad31306a935a732858ef66a067
- AMBIENT.md: fc43f4c854b95b487b196cacc2c92d1dde74404bd630e8b39a2baca165749276
