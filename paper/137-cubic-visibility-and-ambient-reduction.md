# 137. Stronger cubic visibility and actual ambient reduction

**Checkpoint: 23 October 2026 · Structural results and one profile-(1,1) shape exclusion through PR1145**

## What changed

The actual Gauss quotient must carry two independent cubic T channels, not merely one. For the D-type source, a nonzero cubic Gauss kernel forces a specific coherent line image O(2). This excludes two additional quotient shapes. Separately, a complete polynomial system permits removal of an entire coefficient graph by a constant ambient shear, so the actual second fundamental form splits. PR1145 then applies that mechanism to exclude the exact shape O(-8)+O(2)+O(16) in maximal profile (1,1). These are different advances: sharper necessary conditions, quotient-shape exclusions, and a reusable geometric reduction.

The previously established closures of maximal profiles (1,2) and (2,1) are unchanged. This checkpoint does not exclude the whole profile (1,1), prove the separate other-profile exhaustion, or complete the original repair. Historical row counts below are not new live totals.

## Two independent cubic channels

[PR1140, immutable proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/7a2488bcd36d95f79b5198001111b1a31fe5c3ba/research/hm/primary-gauss-double-channel/PROOF.md) works in the actual constant rank-30 Gauss ambient, with K=ker(beta_E) and A_q=E/K. This K is not the canonical rank-15 complement of chapter 133. For each of the four primary-compatible source types, it proves

    W′+2T ↪ H0(A_q(3)).

This is an inclusion of coefficient representations, not a fiberwise rank-14 inclusion. In the D, P and V types, the degree-minus-two top block contributes a T channel: its cubic kernel is too small to kill the six-dimensional constituent. The displayed T O(-3) supplies a second channel. If the two were dependent, subtracting the corresponding map into the top block would produce a saturated negative graph summand killed by the actual Gauss derivative. The near-top derivative lemma prohibits that graph. This argument does not assume that a Birkhoff splitting is horizontal.

The complete cubic-kernel alternatives are 0 or S for D-type, 0 or W′ for P-type, and zero for V- and Z-type. The stronger condition excludes five quotient shapes having only one cubic T. On the fixed historical 182-row overlist it rejects 15 additional records relative to the earlier W′+T test, giving 45 rejected and 137 passing this condition alone. Neither number describes the current remaining geometric frontier; passing this necessary condition is not realization.

## A forced quartic image and two shape exclusions

[PR1142, immutable proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/df2fd3d35dac577d7f1e1c4d51fe68b1fcc824ad/research/hm/gauss-cubic-kernel-exclusions/PROOF.md) treats the actual D-type source. If H0(K(3)) is nonzero, it is S and lies in the top block D O(-2). Its kernel is S O(-3), so the actual coherent image of that top block has rank one and degree two:

    0 → S O(-3) → D O(-2) → O(2) → 0.

The last arrow is the complete quartic system. The resulting O(2)→A_q is an actual sheaf injection, not an assertion that its image is saturated in A_q.

Therefore Hom_G(O(2),A_q)=0 forces H0(K(3))=0. Strict-top applied to this actual kernel then injects H0(K(4)) into H0(A_q(2)), yielding the necessary genuine character

    H0(A_q(2)) + chi_G(A_q(4)) − chi_G(E(4)).

There is no extra H0(A_q) term in this improved envelope. The negative O(-8) contribution to H1 is retained in the Euler character.

For A_q=O(-8)+O(4)+O(8), or O(-8)+O(4)+O(10), the Hom space above vanishes. Each resulting character has V multiplicity −1, a contradiction. These are two actual quotient-shape exclusions; their four original profile-(1,1) occurrences are historical references, not four newly counted live cases. The argument alone does not exclude O(-8)+O(2)+O(16), where the O(2) map is allowed.

## Complete coefficients give an actual constant-ambient splitting

[PR1144, immutable proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/7eb85f05723cdbd12780514e4758cf6a8f230bf3/research/hm/complete-system-ambient-splitting/PROOF.md) supplies the following general lemma. Let E be saturated in H O. Suppose a constant projection H→V restricts to a split surjection E→L=O(-e), followed by a complete degree-e polynomial system L→V O, with dim V=e+1. Choose a section s:L→E.

The coefficient span V1 of the actual inclusion s(L) into H O projects isomorphically to V. Consequently H=ker(pi)⊕V1 and E=ker(q)⊕s(L) as actual embedded bundles. Equivalently, the entire graph is removed by one constant shear. The residual bundle remains saturated, and constant differentiation respects the decomposition. For e>0 the rational-normal line contributes one to Gauss rank; the residual quotient is the remaining direct summand. An equivariant section can be obtained by averaging. The complement depends on that section and is not canonical.

Completeness is essential. A basepoint-free partial quadratic system (x²,y²) does not absorb the additional graph coefficient xy by a constant shear.

The height-seven application in this proof is explicitly conditional: if the actual D-type source has the stated complete degree-eight osculating containment and quotient O(-8)+O(2)+O(16), the lemma removes its O(-8) line in a constant nine-dimensional summand. It leaves a saturated rank-16 bundle of degree −46 in constant dimension 21, with Gauss rank two and quotient O(2)+O(16). Establishing those actual equality hypotheses and excluding the residual core are separate steps, not conclusions of the general lemma. The stronger top(Q*)≤−2 bound from profile (2,1) is not imported into profile (1,1).

## The actual height-seven application excludes one profile-(1,1) shape

[PR1145, immutable proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/2e2da6c1226b7671c79e55b3c9f8bb14a0f8719b/research/hm/profile11-apolar-exclusion/PROOF.md) supplies the actual application that the preceding general lemma deliberately leaves conditional. Under the original maximal profile-(1,1) necessity theorem, A_q=O(-8)+O(2)+O(16) has exactly two original ordered records, indices 119 and 127, with defects twelve and zero respectively. These are historical identifiers, not two newly counted live possibilities.

For record 119, the actual endpoint degree −26 exceeds its maximum capacity −50. Record 127 has degree −38, attaining capacity only at heights seven and eight. Height eight forces the full degree-ten polynomial system. Its apolar annihilator W O(-9) receives no map from the actual D-type source, contradicting absence of constant sections in Q*. This uses only top(Q*)≤−1.

At height seven, the actual complete degree-eight coefficient system gives the genuine constant decomposition described above. The residual F has rank 16 and degree −46 in a constant space of dimension 21. Its rank-five dual bundle has a rank-three endpoint. Exact degree equality forces a three-step chain ending in O(-10), with four independent derivative directions.

Crucially, four directions do not imply that this degree-ten coefficient system is complete. The proof initially allows a proper quotient Sym10 W→R. Its dual injection R*→(Sym10 W)* pulls actual annihilation back to the full apolar bundle Sym6 W O(-4). Degree vanishing leaves only the V O(-4) source block, whose scalar channel must be nonzero or else R would be a forbidden constant subspace of the dual bundle.

The sextic net V is basepoint-free: a nonempty invariant common-zero divisor would have degree at most six, below the minimum orbit size twelve. Its two syzygy degrees a,b satisfy a,b≥1 and a+b=6. Twisting the evaluation sequence by four kills H1 and proves V·Sym4 W=Sym10 W. Thus the fibers l⁴V span the full eleven-dimensional coefficient space, forcing R to be full. The remaining rank-13 source block would then inject into the constant kernel of dimension 21−11=10, a contradiction.

This excludes the exact A_q shape within maximal profile (1,1), including both original defect possibilities. It does not exclude every profile-(1,1) shape or establish global rank-three coverage. Completeness is a conclusion of the net-span argument, not an assumption inserted into the partial-system step.

## Marked-doublet rank and ramification

[PR1143, immutable proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/b43695a7f306fcf5d0281cc59033efd5842539a0/research/hm/marked-doublet-ramification/PROOF.md) studies the nonzero actual restriction W′O(-3)→A_q without assuming that the canonical retraction commutes with Gauss differentiation.

A generic rank-one map would have saturated line image O(e) with e≥4, because W′ first occurs in Sym7 W. Thus maximum target degree at most three forces generic rank two. If generic rank two is known and the top two target degrees sum to at most five, its determinant defect has degree below twelve. The minimum nonempty invariant divisor has degree twelve, so the defect is zero and the image is saturated. These are separate rank and saturation conditions, both sharp for abstract equivariant maps.

For the conditional target O(-8)+W O(3), the unique nonzero channel has determinant divisor equal to the reduced twelve-point orbit. Its fiber rank is two off that orbit and one on it. The positive-block cokernel has length twelve; the full cokernel also retains O(-8). This does not establish occurrence of that target or a new profile exclusion.

## Exact endpoint-capacity certificates

[PR1141, immutable proof and implementation](https://github.com/Akilleez-QA/read-em-and-weep/blob/583cca10b404d63ed145e7c5a0d9ef4d4c445fbd/research/hm/endpoint-capacity-certificate/PROOF.md) generalizes the two-height bound used in chapter 136. With h1+h2=N and h1≥h2≥0, the degree capacity is a concave integer quadratic. Its complete maximizer set is obtained from at most two clipped integers nearest its rational vertex. A separate certificate verifier checks both optimality and completeness, including omitted ties, without enumerating an interval of length N.

The equality-only strict-top filter requires independently proved equality of actual top-image flags. It does not lower the unconditional capacity and does not apply below the maximum. The four earlier profile-(2,1) examples are regression controls, not new exclusions. The implementation passes 62,442 production and 385,882 independent checks; the geometric hypotheses remain obligations of each application.

## Verification and boundaries

The full immutable source proofs were read. Independent whole-proof review accepted PR1140 and PR1142 relative to their pinned input theorems; 341 and 130 supplied checks and 5,907 independent exact character controls reproduce normally and with Python optimization. PR1143 and PR1144 include independent whole-proof reviews; their production checks reproduce 151 and 17,709 assertions respectively, with the latter covering 78 formal symbolic cases. Independent whole-proof review of PR1145 also passed against seven freshly matched immutable originals; its 194 supplied checks and 83 independent formal apolar/net controls reproduce in both Python modes. The reviewed proof has SHA256 47ce243076419081917682b9ab78990e7cf8066598d8eae1f4a175e80ab91b98. These finite tests support the written proofs and do not formally certify the full geometric project. No actual HM/source coefficient, point, parameter, jet or instance-rank experiment is used.

The delivered Craig Ward v0.3 PDF remains the unchanged 23 October 2026, 19:16 UTC snapshot through PR1117. This chapter is a living Markdown supplement. The original fixed-pair problem, full-adjoint conclusion, higher lifting and algebraicity remain open.
