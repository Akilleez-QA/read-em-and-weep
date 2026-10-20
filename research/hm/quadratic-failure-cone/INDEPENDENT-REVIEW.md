# Independent mathematical review

## Verdict

**PASS for the structural theorem and its stated conditional endpoint consequences.**
No mathematical correction is required. This is a mathematical text review,
not a formal-verification certificate.

Reviewed artifact: `PROOF.md`

SHA256:
`12a180158754aeffaa64b709d1033ffdae10f12f7ba6fc6bf321c54b85b658ae`

Review date: 2026-10-20.

## Primary-source audit

The review directly inspected the relevant page images of
[Horrocks–Mumford, Topology 12 (1973), 63–81](https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf).
The PDF SHA256 is
`db786d5ee732e0b70d122a39823d22088c60930492a83582b2b1028de7d1e482`.

The exact inputs check as follows:

- Printed pp.64–65, §1 and (1.2): the representations V_i are irreducible on
  H, their central weights are 2^i modulo five, they extend to N, and
  V_i^vee is V_(i+2). The quotient N/H is SL_2(F_5).
- Printed p.67, opening of §2 and (2.2): H^0(O(1))=V^vee; the isotypic
  evaluation construction and its irreducibility criterion apply.
- Printed p.68, first paragraphs, (2.3), and Lemma 2.4: the bundle construction
  is N-equivariant, N/H is perfect, U=Sym^2(W_original), and W' is the
  indicated conjugate.
- Printed p.70: the Chern-class display gives c_1(E)=5. Lemma 3.3(v) is
  h_2=chi_3'·theta h_1. Its dual, not the undualized formula, supplies S_2.
- Printed p.72, (4.2): the cohomology quotient is compatible with
  multiplication, so the shifted M is generated in degree zero.
- Printed p.73, (4.6): H^1(E(-2)) has character chi_2'·theta h_1.
- Printed p.74, (4.12): H^1(E) has character chi_2'.
- Printed p.81, appendix: chi_3' labels U' and chi_2' labels W'.

Thus the normalization and all primes, duals, and central weights used in
the proof agree with the primary source.

## Mathematical checks

1. **Determinant and trace-zero factor.** The determinant of W' is trivial
   because it is a character of the perfect quotient. Its invariant
   alternating form gives W'≅(W')^vee and
   Sym^2(W')≅sl(W'). There is no omitted determinant character. In
   particular the dual U' appearing on dualizing Lemma 3.3(v) is
   legitimately replaced by U'.

2. **Uniqueness and nonvanishing.** With A=V_1 and W=W', the target is the
   direct sum of the distinct irreducibles A^vee and
   A^vee⊗sl(W), of dimensions five and fifteen. Observation (2.2)
   justifies irreducibility using the full N-action. Generation gives
   S_2 M_1=M_3≠0, so Schur's lemma selects the second summand with a
   nonzero scalar. This proves injectivity without testing any particular
   quadratic.

3. **Failure support.** If the multiplication image is a line L, every
   contracted trace-zero endomorphism lies in Hom(W/L,L), a
   one-dimensional subspace. Hence the nonzero tensor is a⊗n_L,
   and the converse holds. The nilpotent lines form the Veronese conic.
   The resulting reduced projective locus is therefore
   P(A^vee)×P(W), embedded by O(1,2), of dimension five and codimension
   nine. The proof correctly separates the zero tensor and does not
   assert an unproved affine determinantal-scheme statement.

4. **Dual contraction.** For each nonzero lambda, the map
   sl(W)→W^vee, B↦lambda B, is onto. Tensoring by A^vee proves
   rank C_lambda=10 and a five-dimensional kernel.

5. **Endpoint implication.** Injectivity implies the primary degree-three
   quotient has dimension at most one for every nonzero u_0, independently
   of v_0. The stated presentation from PR440 then implies dim Q_0≤15;
   the stated doubled-dual identification from PR439 implies the bound
   thirty. These deductions are correct. This review does not
   independently re-audit PR440 or PR439 and treats their quoted
   presentations as dependencies, rather than results of HM1973.

## Boundaries and remaining questions

The proof explicitly distinguishes multiplication-map rank from the rank of
a quadratic form. It does not identify the tensor representing the fixed
binary-quartic u_0 or decide whether that point lies on the failure cone.
On that cone, the cubic image and the retained incoming endpoint map remain
necessary to determine Q_0. Neither vanishing nor nonvanishing of the fixed
Q_0 follows from the stated upper bound.

No selected HM multiplication map, source-instance generator or checker,
selected matrix, rank sample, or source evaluation was used in this review.
Only published representation inputs, general linear algebra, and the
declared endpoint dependencies were used.
