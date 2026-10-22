# Independent deductive review

Result: PASS for PROOF.md with SHA-256

    db4abd6aeb81da64c79558941412862585c4b6dd5043413ddea12dfb302dac96

The review uses the exact identity of PR747 at 0a0ee30a5142477e54245b7c6f22d561abb4f5f1 and the dichotomy of PR760 at d798dceb77b94b5dbb9457fb303984e595ce1874. These pinned proofs were read directly. The certificate itself is proved for the abstract five-dimensional space of trace-free self-adjoint operators, with the canonical map K left unevaluated.

## Checks

1. Evaluation at every nonzero a is onto the three-dimensional A. In the nonisotropic case an arbitrary symmetric-matrix column is compatible with trace zero. In the isotropic Witt basis the independent entries x,e,g give an arbitrary first column. Thus P_a has dimension two in both cases. Multiplication by gamma d/a is injective, so the common-direction formula gives C-rank three, precisely kernel P_a, and precisely the complete rational system a^(-1)A. Basepoint-freeness gives the exact maximal pole divisor, with no unproved absence of cancellation assumed.

2. The two normal forms have common kernel exactly Ca. Their displayed adjugates are respectively -(x^2+y^2)E33 and -2b^2 E13. Since adjugate entries are the signed two-by-two minors, these also verify the claimed schemes, not merely their supports. Over C the first quadratic has two distinct roots; the second is a double root. Nonzero matrices at these rank-drop directions have rank one and square zero. The generic isotropic member has nonzero square and zero cube.

3. For the converse recognition criterion, writing adj(sS+tT)=q(s,t)R is justified by the nonzero one-dimensional coefficient span. The determinant identity and the polynomial-domain property imply SR=TR=0. Nonzero adjugate and zero determinant at a generic parameter give rank two for the pencil and rank one for R. Hence its image is a common line, and the dimension-two containment J subset P_a is equality. The normal forms then give uniqueness of that line. The nonzero adjugate condition correctly excludes pencils of generic rank at most one.

4. The normalization condition is essential and sufficient. Both maps from H to rational sections vanish on J=P_a, and equality on the three-dimensional quotient basis extends to all H. No prior regularity of a r_h is needed. The formula is independent of representative and of the nonzero scale of a. The formal rescaling argument correctly explains why kernel and image alone do not fix this induced quotient isomorphism.

5. Failure of the exact certificate excludes the common branch; PR760, not a new equivariance assumption, then supplies the proper-closed exceptional-source conclusion. No actual alternative is selected. The use of C-rank is explicit and is not confused with rank over k.

## Scope of verification

This is an independent deductive mathematical review, not a proof-assistant check. No executable algebra calculation, selected actual HM coefficient, source, point, derivative, matrix-rank evaluation, or scan was used. The imported modular nonvanishing implication remains one-way. The distinct fifth-neighborhood beta4 boundary and algebraicity remain unresolved.
