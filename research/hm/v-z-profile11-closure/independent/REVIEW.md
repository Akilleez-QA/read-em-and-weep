# Independent review of V/Z source-conditioned profile (1,1) closure

Status: PASS for the precise source-conditioned theorem. Final authored proof Sections1-6 independently read and checked, including table rows143 and149 and the full saturated negative flag argument.

## Independently established checks

Freshly retrieved eight complete public originals at the exact immutable commits in FETCH.json. AUTHENTICATION.json records exact Git blob, UTF-8 byte count and SHA256. These include the original159 necessity theorem and ordered JSON, actual splitting and Gauss embedding, strict-top lemma, PR1123 source theorem, PR1140 cubic theorem and character implementation. All eight author input bytes match these independent retrievals.

The character evaluator uses exact conjugacy-class inner products over Q(sqrt(5)), with closed-binomial symmetric-power traces, rather than the author's McKay multiplication. The transparent class-character base is reused from the independent P-source review, but no P partition/count/output is imported. V and Z compatibility and every exclusion are recomputed afresh. Orthogonality and all nine irreducibles through symmetric degree40 agree with the separate pinned McKay implementation.

Run:

    python independent_check.py > RESULT.json
    python -O independent_check.py > RESULT-optimized.json
    cmp RESULT.json RESULT-optimized.json
    python compare_packet.py

The independent runs complete 5,248 explicit controls and have identical output. Author verify.py separately reproduces RESULT.json byte-for-byte in normal and optimized Python, with1,135 explicit controls plus81 character controls.

V tuple(1,1,2,0,0,0,0,0) and Z tuple(1,2,1,0,0,0,0,0) each have rank17, degree−54, H0(E(3))=W'+2T and signed chi(E(4))=3V+3P+2D. For every one of the original159 ordered records and every twist−10 through10, the two source-conditioned inequalities are recomputed, exactly matching the original stored tuple membership. There are34 compatible records for each source, independently.

Disjoint exhaustive partition for each source:

-16 cubic:42,43,53,62,63,64,65,66,67,73,74,76,102,103,110,111.
-7 quartic:86,87,88,89,96,116,134. Every signed quartic envelope has V multiplicity−1.
-11 capacity:130,132,141,142,143,144,145,148,149,150,151.

Every author first failed source-compatibility inequality for the other125 rows per source is independently verified. All six capacity values for each final row are separately computed by height pairs and nonincreasing quotient-rank sequences. Exact maxima range from−125 to−70; actual deg L is−38,−36 or−34. The smallest contradiction gap is34 at record144. Record150 has gap36. Negative doublet degrees−1 are correctly retained.

## Geometry checked against originals

The original necessity theorem covers every actual maximal profile(1,1) pair by the fixed159 overlist; it does not claim realization or global frontier completeness. Source tuple compatibility is a necessary quotient/transpose condition, not an assumed realization. Exact V/Z tuples follow directly from PR1123's displayed source equations.

PR1140 proves both cubic visibility and H0(K(3))=0 for V/Z using the actual constant30-dimensional embedding. This is not the unrelated54-dimensional coefficient presentation. Strict-top then gives H0(K^-(4))=0, and the actual derivative gives H0(K(4)) into H0(A(2)). Additivity of Euler characters gives the necessary genuine envelope H0(A(2))+chi(A(4))−chi(E(4)); signed multiplicities are preserved.

For capacity, let F0=Q*, F1=L and F(j+1)=ker beta(Fj). Kernels are saturated in the constant ambient because derivative images on the smooth curve are torsion-free, hence locally free. Each nonzero negative F(j) has nonzero derivative: a horizontal saturated subbundle would be constant, contradicting negative degree. Thus the flag terminates without a hidden horizontal remainder. Actual induced injections G(j) into G(j−1)(−2) imply nonincreasing positive quotient ranks at most2 and sum10. Composing injections into B(−2j), taking determinants, and summing bounds yields the stated two-column capacity. Saturation of derivative images in their targets is never assumed. No stronger profile(2,1) top-degree hypothesis is imported.

## Scope

This supports excluding V and Z actual source types in maximal profile(1,1), relative to the pinned actual-geometric and original necessity theorems. It is not proof-assistant verification, not a proof of original list generation, not an exclusion of P or D, not a global rank-three closure, and not a complete original proof repair. No historical enumeration, actual coefficients, selected parameters or points, instance matrix or rank experiment was run. This review is supporting verification, not a new mathematical deduction claimed as progress.

## Hash-bound reviewed packet

- PROOF.md: b344bb861ac283d1f997de2ac7d281938913a4a9e471a0c7545e81ed2e6d8e61
- verify.py: ea899edb42a72001fd2660e544358be2a3fa28d70f37b91d43c2b66867ddd1a8
- RESULT.json: c651d43d108b882267b9f749ed2c0b02f59837350a8026f2e9da81469b9dfca4
- INPUTS.json: e35b8022a1e460530cbd6f229bfbc53f7d512fc8cd0856b354c3ee2eff17e27c
- characters.py: 5b3b1d415f26ca467670afeb73357cbb0e9c125a6b1acd25155b6d85eef4e4f1

No blocking gap found in this frozen packet. The conclusion remains relative to the pinned original necessity and actual-geometric inputs; no broader closure is inferred.
