# Current independent mathematical audit

Review date: 20 October 2026. Verdict: PASS under the written hypotheses. This is a formal mathematical review, not machine-checked verification.

## S007: algebraic Thom–Whitney reduction

1. The finite semicosimplicial family model is closed under products and differential. Whitney extension and integration are chain maps, not algebra maps. Lunardon's Definition 2.1, Construction 3.6, Theorem 3.8 and Remark 3.9 have the opposite homotopy sign; K=-h_D gives exactly id-WI=dK+Kd. Fiorenza–Iacono–Martinengo §3.2 confirms the semicosimplicial passage.
2. Combining K with W h I gives id-W iota pi I. On scalar positive degrees the projection disappears, so the prescribed primitives and their scalar exact ambiguities are valid. All integrations are finite polynomial integrations in auxiliary simplex variables, not analytic inverses or base-pole constructions.
3. Affine acyclicity supplies regular local Atiyah lifts of each vector field. Subtraction of half the determinant discrepancy gives the prescribed determinant lift. Linear choices in sl_5 do not assert a Lie splitting or a global bundle lift.
4. Barycentric interpolation is face-compatible. Its simplex differential is order zero because the sum of dt_i is zero, and determinant normalization makes it trace-free. Edge integration gives D_j-D_i with the stated connecting-map convention.
5. The balanced tensor action has a single base derivative. Its line term is simplex-independent, yielding [d,L_X]=ad(a_X), not an action by cochain maps. Trace-free inputs remain trace-free.
6. Over graded-commutative coefficients, rank two gives uv-vu=tr(uv)Id for odd trace-free u,v. Consequently h_ab=L_Xb/2+t_ab Id has differential ab. For a proof-only primitive q_bc, the negative scalar term in M_tf is forced by a t_bc=-t_bc a. The identity dL_Xq_bc=B(L_Xb,c)+B(b,L_Xc)+2B(a,q_bc) gives M_tf=C+dL_Xq_bc/2. Thus C is closed and has the intended class. No class is assigned to an individual nonclosed summand.
7. Multiplicative DGA comparison, rather than I or W multiplicativity, identifies the operation. Scalar target H2 vanishing and the separate zero-indeterminacy hypothesis are used for their correct, different purposes. Trace-free preparation of supplied ordinary Čech representatives follows from the degree-one scalar contraction.

The result is a finite algebraic recipe relative to supplied regular lifts and representatives, not a selected-source implementation or complexity bound. S196 is smooth comparison context only; its CURRENT-SCOPE qualification was also checked and no global unresolved-case claim is revived.


## Exact reviewed files

- `DEPENDENCIES.md`: SHA-256 `757308681e5c52a5ef737a8f1559829a81b8b7a78112d08e43c719df52ad4be8`.
- `MATHEMATICAL-NOTES.md`: SHA-256 `d8188601ef680c854df4824775b85ba9f6cd70503053533a0b17816509c52687`.
- `PROOF.md`: SHA-256 `f5af687cecf62a6e675b045c79881788e80034196a8feb2994d48ec0026d745b`.
- `PUBLIC-SOURCES.md`: SHA-256 `46e3423d538a2872190a56cd54712fc1217c57fe6cbb24b86d1cf694eed8f58c`.
- `README.md`: SHA-256 `46513aaebbfe8ba43f89cc551ab0b45a64310ba6fc34336949b68aa8714882ca`.

The proof and supplementary mathematical arguments were read in full. Existing dependency files were independently fetched at their immutable commits; contents and Git-blob hashes matched the recorded pins. Newly published predecessors were read back before binding their immutable links. Reference substitutions change no mathematical statement.

The primary contraction sources were checked directly: [Lunardon, Definition 2.1, Construction 3.6, Theorem 3.8 and Remark 3.9](https://arxiv.org/pdf/1807.02517), and [Fiorenza–Iacono–Martinengo, §3.2](https://ems.press/content/serial-article-files/31821).

No selected HM/source-instance operation, source matrices, product values, ranks, jets, residuals, detectors or actual Massey values were evaluated. No mathematical experiment or large computation was run. No nonvanishing witness, positive-characteristic TW comparison, or source implementation is asserted.
