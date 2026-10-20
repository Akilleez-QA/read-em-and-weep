> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# Independent audit of the isolated-defect bound

## Verdict

The argument in PROOF.md proves length Ext²(B,O) ≤ 390 for a slope-semistable rank-two reflexive sheaf B on complex P4 with finite singular locus, c1=0 and c2=5. No mathematical gap was found. This verdict imports the P4-to-P3 semistable restriction theorem at the same explicitly documented source-verification level as the existing rank-eight-third-chern-bound proof. It does not independently audit the lower bound 480 or the earlier rank-eight reduction to these hypotheses.

## The properly semistable issue is resolved

It would be false to assert h0(F(1))≤3 for an arbitrary semistable bundle F on P2 with c1=0,c2=5. Five reduced collinear points Z admit locally free extensions 0→O→F→I_Z→0; then h0(F(1))=4. For example existence follows from the complete-intersection resolution of I_Z of degrees (1,5), taking an extension component which is nonzero at all five points. This observation is an abstract bundle counterexample, not an evaluation of the task's physical source or operation.

The proof does not make that false assertion. Its F is the restriction of a bundle E on P3 to a general plane. Ellia–Gruson, arXiv:1409.3789, Proposition 6, printed page 4, was independently opened and read. It states precisely that a properly semistable indecomposable rank-two bundle E has h0(E|P(1))=3 for a general plane. Their proof uses the section curve and Strano's theorem; no reducedness assumption on that curve is added. Their Theorem 1, page 1, supplies ≤2 for stable normalized E with c2≥4. Since c2=5 excludes a decomposable semistable E with c1=0, these two results cover every E under consideration.

The numerical bound 3 is consequently justified, including the properly semistable case. The stronger stable bound is not needed.

## Restriction and generic line

A hyperplane avoiding the finite singular locus makes E an actual vector bundle, not merely reflexive. Exactness follows from torsion-freeness of B and its nonzero hyperplane equation. Its Chern classes restrict as stated. Semistability of E is supplied by the previously documented Flenner theorem.

For the further restriction to P2, the proof now records two routes. In the stable case, Barth's theorem as stated in the introduction of Ellia–Gruson applies because c2=5 is not the null-correlation exception c2=1. In the properly semistable case, 0→O→E→I_C→0 restricts exactly to a general plane; the curve is a local complete intersection and a general plane meets it properly. The resulting extension implies H0(F(-1))=0 and therefore slope-semistability of F.

Vitter, arXiv:math/0310076, Introduction page 1, was independently opened and read: for a semistable bundle the generic splitting gaps are at most one; for normalized rank two with c1=0 this is O_L⊕O_L. This checks the precise semistable hypothesis needed here. It is a research-paper statement of the classical Grauert–Mülich theorem, not a fresh reading of its original proof.

Brambilla, arXiv:math/0509599, Theorem 2.3, page 2, was also independently read and has exactly the Flenner inequality recorded in the earlier proof. Its substitutions for P4 and P3 are correct. This is a scholarly statement of Flenner's theorem, not original-paper verification.

## Regularity

Hein, arXiv:math/9904102, Lemma 2.2, printed page 9, was independently read. Its second assertion is exactly the lifting bound used: if restriction to an exact hyperplane is m-regular, the original sheaf is (m+h1(G(m−1)))-regular.

One can also check the relevant vector-bundle instance directly. Restriction regularity and the long exact sequence force H^i(G(t))=0 for i≥2 and t≥m−i, by propagation to large t and Serre vanishing. For k≥m, multiplication by the hyperplane equation gives a surjection H1(G(k−1))→H1(G(k)). If the dimensions are equal while positive, the restriction map on H0 in degree k is surjective. Generation of sections of the regular restriction then makes all subsequent restriction maps surjective, forcing the H1 dimensions to remain constant forever, contrary to Serre vanishing. Thus the dimension drops at every such step until zero. After at most h1(G(m−1)) steps, the stated regularity follows. This also confirms the indexing in both uses of the lemma.

## Local defect and arithmetic

Serre duality on P4 for the coherent sheaf B(t) gives the dual global Ext² into O(-5), with no local-freeness requirement. After twisting positively in the second argument, Serre vanishing collapses the local-to-global Ext spectral sequence. Hence h2(B(t)) equals length of the sheaf Ext²(B,O) for all sufficiently negative t. It is zero for sufficiently positive t. The hyperplane long exact sequence bounds each difference h2(B(t−1))−h2(B(t)) by h1(E(t)), with the correct sign. Telescoping therefore yields the first asserted inequality.

The plane RR formula, duality t↔−t−3, 5-regularity, h0(F)≤1, and resulting ten-term table are consistent. In the proof of h0(F)≤1, “saturated rank-one line subsheaf” is slightly more precise than “line subbundle”; this terminology does not affect the argument.

The P3 cumulative table sums to 165. The bound h0(E(4))≤55 and χ(E(4))=40 give h1(E(4))≤15 because the stated higher cohomology vanishes. The second regularity application yields 20-regularity and hence h1(E(t))=0 for t≥19. The fourteen degrees 5 through 18 contribute at most 210; degree 4 contributes at most 15. Total: 165+15+210=390.

## Source and scope boundary

Primary research PDFs independently checked: https://arxiv.org/pdf/1409.3789 ; https://arxiv.org/pdf/math/9904102 ; https://arxiv.org/pdf/math/0310076 ; https://arxiv.org/pdf/math/0509599 . All citations above distinguish an author's own result from a recalled classical theorem. No original physical source, evaluation, matrix, input, rank instance, jet, detector, external write, installation, or large computation was used. The only new deliverable is this local audit.
