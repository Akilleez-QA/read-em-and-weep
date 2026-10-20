# Mathematical review: the three degree-two defect channels

Reviewed on 2026-10-20.

Reviewed artifact: `PROOF.md`, 16,189 bytes.

SHA-256: `01a2c84b7c4ca74e037316a5bb935e8e65957fbb53ae2316e478ae34147a3602`.

## Verdict and verification status

The arguments in the reviewed artifact establish its stated conclusions, conditional on its explicitly imported section-resolution, primary-cohomology, and twist-two-vanishing inputs. No mathematical defect was found in the reviewed argument.

This is an independent mathematical text review, not formal verification. The reviewer authored this review, not the proof. The review checks the derivation and its scope; it does not independently reprove the geometric theorems underlying PR94 or certify publication, merger, exhaustive novelty, or any unevaluated multiplication map.

## Material checked

- The complete final proof identified above.
- The local PR451 order-five defect proof, particularly its degree-two kernel sequences, definition of \(C_2\), primary image \(I_2\), and exact sequence \(C_2\to P_5\to Q_5\to0\).
- Horrocks–Mumford (1973), the representation-theoretic conventions and cohomology formulas in §§1–4, including Lemma 3.3 on printed p.70 and the character table on printed p.81. The p.70 formulas and Appendix table were checked against page images.

PR94's \(H^0B(2)=0\) is an imported dependency, not a newly verified theorem in this review. Its exact commit and retained prerequisite are disclosed in the proof. The consequences after invoking that vanishing have been checked.

## Specific checks

1. **Primes, duals, and irreducible types.** With \(A=\theta V\) and \(S_1=V^*\), the formulas
   \[
   S_2=A^*\otimes U',\qquad
   S_3=A\otimes(J\oplus W'),\qquad
   S_1\otimes A^*=A\otimes(U\oplus W')
   \]
   have the stated primes. The small tensor identities in (3) agree with the Appendix. In particular \(T=\chi_4\) and \(Q=\chi_4^\#\) are distinct; replacing either with the other would invalidate the splitting argument.

2. **Dual-resolution cohomology.** Dualizing the locally free section resolution is legitimate. Its two image sheaves give exactly the cohomology identifications and exact sequence (7). The twists \(t=-8,-6,-5\) recover \(B_3^*=M_3^*\), the short exact sequence determining \(B_2^*\), and the four-term exact sequence determining \(B_1^*\). At \(t=-8\), the nonzero \(H^4\) of \(T^*\otimes\mathcal O(-5)\) does not affect those intermediate-cohomology identifications; the proof explicitly retains this distinction. The resulting coefficients are
   \[
   B_3=W',\qquad B_2=A\otimes Q,\qquad
   B_1=A^*\otimes(W\oplus J).
   \]
   These follow from exactness and abstract characters, without determining a selected differential.

3. **Injectivity and exact defect.** PR451 bounds \(\dim\ker p_2\) by five. Its source \(A^*\otimes T\) is irreducible of dimension twenty by HM (2.2), so \(p_2\) is injective. Independently, the source of \(a_2\) has types \(A^*\oplus(A^*\otimes U')\), and the scalar sections occupy precisely the latter summand. Once \(H^0B(2)=0\) is imported, the kernel is exactly that scalar summand and the image is the unique \(A^*\) summand in the target. Thus
   \[
   \dim C_2=65,\qquad
   C_2=(A^*\otimes U)\oplus(A^*\otimes Q)\oplus(A^*\otimes R).
   \]
   The unprimed fifteen-dimensional defect constituent is different from the primed scalar kernel.

4. **Uniqueness and canonicity of the splitting.** The finite-group representation category over \(\mathbf C\) is semisimple. The three defect constituents are disjoint from \(I_2=A^*\otimes T\), giving \(\operatorname{Hom}_N(C_2,I_2)=0\). Therefore the quotient sequence has exactly one \(N\)-equivariant section. The cup-product description of \(I_2\) also makes its independence from choices of degree-four section generators explicit. The assertion is relative to the fixed classical normalizer action, as the proof states.

5. **Universal versus fixed cubic maps.** Multiplication composed with the unique section gives the canonical \(N\)-equivariant map \(S_3\otimes C_2\to H^1B(5)\). Specialization at \(v\), followed by the actual quotient defining \(P_5\), recovers PR451's \(\delta_v\). The proof correctly refrains from assigning an \(N\)-equivariant quotient structure to arbitrary fixed \(u,v\), applying Schur's lemma to their selected maps, or asserting directness of the three selected images. The quotient by all of \(S_3I_2\) is correctly distinguished from the original quotient by \(vI_2\).

## Boundary of the conclusion

The new result identifies the defect's three abstract irreducible channels and their unique equivariant lifts. It does not evaluate the selected cubic images, determine \(P_5\) or \(Q_5\), prove order-five endpoint vanishing, or establish order-six optimality or actual-source filtration membership.

No selected HM/source matrix, generator list, computational checker, or rank routine was used in this review. The structural deduction \(\operatorname{rank}a_2=5\) is a consequence of exactness, irreducibility, and the imported vanishing, not a matrix evaluation.
